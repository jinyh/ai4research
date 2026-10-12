import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('runner', HERE / 'run.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in ('inputs.json', 'reference.json', 'baseline.py'):
            shutil.copy2(HERE / name, self.root / name)
        self.out = self.root / 'run'

    def tearDown(self):
        self.temp.cleanup()

    def execute(self, fault=False):
        return runner.execute(self.root / 'inputs.json', self.root / 'baseline.py', self.out, fault)

    def evaluate(self):
        return runner.evaluate(self.out, self.root / 'reference.json')

    def test_baseline_is_actually_executed_and_gaps_remain_visible(self):
        self.assertEqual(self.execute(), 0)
        r = self.evaluate()
        self.assertEqual((r['inputs'], r['normal_preserved'], r['invalid_rejected'], r['invalid_admitted']), (8, 2, 4, 2))
        self.assertTrue(all('elapsed_ns' in e for e in runner.events(self.out) if e['event'] == 'processed'))

    def test_interruption_resume_preserves_failure_and_does_not_repeat_success(self):
        self.assertEqual(self.execute(True), 2)
        with self.assertRaises(ValueError):
            self.evaluate()
        self.assertEqual(self.execute(True), 0)
        self.assertEqual(self.execute(True), 0)
        ev = runner.events(self.out)
        self.assertEqual(sum(e['event'] == 'processed' for e in ev), 8)
        self.assertEqual(sum(e['event'] == 'controlled_failure' for e in ev), 1)
        self.assertEqual(self.evaluate()['controlled_failures'], 1)

    def test_changed_implementation_or_inputs_cannot_resume(self):
        self.execute(True)
        p = self.root / 'baseline.py'
        original = p.read_text()
        p.write_text(original + '\n# changed\n')
        with self.assertRaisesRegex(ValueError, 'frozen'):
            self.execute()
        p.write_text(original)
        p = self.root / 'inputs.json'
        p.write_text(p.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'frozen'):
            self.execute()

    def test_missing_and_duplicate_reference_cannot_shrink_denominator(self):
        self.execute()
        p = self.root / 'reference.json'
        ref = json.loads(p.read_text())
        shortened = dict(ref, cases=ref['cases'][:-1])
        p.write_text(json.dumps(shortened))
        with self.assertRaises(ValueError):
            self.evaluate()
        ref['cases'].append(ref['cases'][0])
        p.write_text(json.dumps(ref))
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_execution_does_not_need_evaluation_reference(self):
        (self.root / 'reference.json').unlink()
        self.assertEqual(self.execute(), 0)
        # Interface separation only; imported code has ordinary local process permissions.

    def test_modified_implementation_changes_actual_outcomes(self):
        self.execute()
        p = self.root / 'baseline.py'
        p.write_text('def normalize_record(record):\n    raise ValueError("reject everything")\n')
        out2 = self.root / 'changed'
        runner.execute(self.root / 'inputs.json', p, out2)
        r = runner.evaluate(out2, self.root / 'reference.json')
        self.assertEqual(r['invalid_rejected'], 6)
        self.assertEqual(r['normal_preserved'], 0)
        self.assertEqual(r['normal_errors'], 2)

    def test_snapshot_or_trace_cannot_silently_drop_a_case(self):
        self.execute()
        p = self.out / 'inputs.json'
        original = p.read_text()
        p.write_text(json.dumps(json.loads(original)[:-1]))
        with self.assertRaisesRegex(ValueError, 'snapshot'):
            self.evaluate()
        p.write_text(original)
        p = self.out / 'events.jsonl'
        rows = [e for e in runner.events(self.out) if not (e['event'] == 'processed' and e['case_id'] == 'E6')]
        p.write_text('\n'.join(json.dumps(e) for e in rows)+'\n')
        with self.assertRaises(ValueError):
            self.evaluate()


if __name__ == '__main__':
    unittest.main()
