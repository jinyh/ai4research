import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('workflow', HERE / 'run.py')
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)

class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.original_root = workflow.ROOT
        self.assets = self.root / 'assets'
        shutil.copytree(HERE, self.assets, ignore=shutil.ignore_patterns('__pycache__'))
        workflow.ROOT = self.assets
        self.out = self.root / 'run'
        self.out.mkdir()
    def tearDown(self):
        workflow.ROOT = self.original_root
        self.temp.cleanup()
    def test_complete_replay_and_semantic_annotation_totals(self):
        self.assertEqual(workflow.replay(self.out), 0)
        result = workflow.evaluate(self.out)
        self.assertEqual(result['totals']['card']['missing'], 3)
        self.assertEqual(result['totals']['free']['missing'], 4)
        self.assertEqual(result['card_minus_free'], -0.125)
        self.assertEqual(result['per_source']['T02']['card']['rate'], result['per_source']['T02']['free']['rate'])
        self.assertGreater(result['per_source']['T03']['card']['rate'], result['per_source']['T03']['free']['rate'])
        self.assertEqual(workflow.replay(self.out), 0)
        self.assertEqual(workflow.evaluate(self.out)['totals'], result['totals'])
        self.assertEqual(sum(e['event']=='replayed' for e in workflow.read_events(self.out)), 6)
    def test_failure_is_retained_and_resume_has_new_run_id(self):
        self.assertEqual(workflow.replay(self.out, True), 2)
        with self.assertRaises(ValueError): workflow.evaluate(self.out)
        self.assertEqual(workflow.replay(self.out, True), 0)
        events=workflow.read_events(self.out)
        failed=next(e for e in events if e['event']=='controlled_failure')
        resumed=next(e for e in events if e['event']=='replayed' and e['job_id']==failed['job_id'])
        self.assertNotEqual(failed['run_id'],resumed['run_id'])
        self.assertEqual(sum(e['event']=='controlled_failure' for e in events),1)
        self.assertEqual(workflow.evaluate(self.out)['outputs'],6)
    def test_resource_access_and_path_traversal_are_denied(self):
        for role,name in [('executor','gold'),('executor','../gold'),('unknown','sources')]:
            with self.assertRaises(PermissionError): workflow.read_resource(role,name,self.out)
        self.assertEqual(len(workflow.read_resource('evaluator','gold',self.out)),8)
        self.assertEqual(sum(e['event']=='access_denied' for e in workflow.read_events(self.out)),3)
    def test_changed_frozen_inputs_cannot_resume(self):
        workflow.replay(self.out, True)
        path=self.assets/'outputs.json';path.write_text(path.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'frozen inputs'):workflow.replay(self.out)
    def test_missing_or_fabricated_annotation_fails(self):
        workflow.replay(self.out)
        path=self.assets/'annotations.json';original=json.loads(path.read_text())
        path.write_text(json.dumps(original[:-1]))
        with self.assertRaisesRegex(ValueError,'missing annotation'):workflow.evaluate(self.out)
        original[0]['output_quote']='不存在的引用'
        path.write_text(json.dumps(original))
        with self.assertRaisesRegex(ValueError,'quote not found'):workflow.evaluate(self.out)

if __name__ == '__main__': unittest.main()
