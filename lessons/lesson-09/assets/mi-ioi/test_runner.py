import json
import tempfile
import unittest
from pathlib import Path

from run import ROOT, load_cases, summarize, validate_policy


class ProtocolTests(unittest.TestCase):
    def test_family_isolation(self):
        dev = load_cases(ROOT / 'cases.jsonl', 'dev')
        test = load_cases(ROOT / 'cases.jsonl', 'heldout')
        self.assertEqual((len(dev), len(test)), (12, 12))
        self.assertFalse({r['family'] for r in dev} & {r['family'] for r in test})

    def test_detects_family_leak(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'cases.jsonl'
            p.write_text('\n'.join(json.dumps(r) for r in [
                {'id': 'a', 'family': 'one', 'split': 'dev'},
                {'id': 'b', 'family': 'one', 'split': 'heldout'}]))
            with self.assertRaisesRegex(ValueError, 'leaks'):
                load_cases(p, 'dev')

    def test_preserves_negative_effect(self):
        result = summarize([{'id': 'a', 'family': 'f', 'clean': 4, 'corrupt': 1,
                             'noop': 1, 'random': 2, 'patch': 0}])
        self.assertEqual(result['patch_minus_corrupt'], -1)
        self.assertEqual(result['patch_minus_random'], -2)
        self.assertEqual(result['max_noop_error'], 0)

    def test_invalid_interventions_rejected(self):
        for policy in ({'layer': 12, 'position': 'last'}, {'layer': 5, 'position': 'unknown'},
                       {'layer': True, 'position': 'subject'}):
            with self.assertRaises(ValueError):
                validate_policy(policy)


if __name__ == '__main__':
    unittest.main()
