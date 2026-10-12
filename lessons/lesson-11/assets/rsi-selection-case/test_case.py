"""Critical selection/evidence contracts; injected failures are test fixtures."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run


class SelectionContracts(unittest.TestCase):
    def setUp(self):
        self.config = json.loads(Path(__file__).with_name("config.json").read_text())
        self.config.update(pool_size=4, candidate_counts=[1, 4], repeats=3, bootstrap_samples=20)

    def test_ties_unknown_and_invalid(self):
        self.assertEqual(run.choose({3: (2, 4), 1: (1, 2), 0: (0, 0)}), 1)
        self.assertEqual(run.choose({0: (0, 1), 1: (0, 0)}), 0)
        for observations in ({}, {0: (0, 0)}, {0: (2, 1)}, {0: (-1, 1)}):
            with self.assertRaises(ValueError):
                run.choose(observations)

    def test_reproducibility_and_nested_evidence(self):
        a = run.simulate(self.config)
        self.assertEqual(a, run.simulate(self.config))
        run.validate_records(*a, self.config)
        self.assertEqual(run.summarize(a[1], self.config), run.summarize(a[1], self.config))

    def test_final_data_cannot_change_selection(self):
        normal = run.simulate(self.config)
        original = run.sample_counts
        def changed_final(probability, trials, seed):
            return (0, trials) if trials == self.config["final_trials"] else original(probability, trials, seed)
        with patch.object(run, "sample_counts", side_effect=changed_final):
            changed = run.simulate(self.config)
        self.assertEqual([r["selected_candidate"] for r in normal[1]], [r["selected_candidate"] for r in changed[1]])
        self.assertNotEqual([r["final_score"] for r in normal[1]], [r["final_score"] for r in changed[1]])
        run.validate_records(*changed, self.config)

    def test_selector_has_no_oracle_or_final_argument(self):
        import inspect
        self.assertEqual(list(inspect.signature(run.choose).parameters), ["observations"])
        with self.assertRaises(TypeError):
            run.choose({0: (1, 2)}, oracle=[0.9], final=[0.8])

    def test_budget_and_shared_final_evidence(self):
        raw, results = run.simulate(self.config)
        for row in results:
            if row["method"] != "history":
                self.assertEqual(row["additional_cost"], row["candidate_count"] * 32)
        groups = {}
        for row in results:
            key = (row["scenario"], row["repeat"], row["selected_candidate"])
            self.assertEqual(groups.setdefault(key, row["final_evidence_id"]), row["final_evidence_id"])
        self.assertEqual(len(raw), len({r["record_id"] for r in raw}))

    def test_hand_checked_counts(self):
        # Both truths are 0.65: historical optimism 3/4 - .65 = .10;
        # oracle regret is zero despite a large observed ranking difference.
        observations = {0: (1, 4), 1: (3, 4)}
        selected = run.choose(observations)
        self.assertEqual(selected, 1)
        self.assertAlmostEqual(observations[selected][0] / 4 - 0.65, 0.10)
        self.assertEqual(max([0.65, 0.65]) - 0.65, 0)
        raw, results = run.simulate(self.config)
        self.assertTrue(all(r["selection_loss"] == 0 for r in results if r["scenario"] == "equal"))

    def test_missing_wrong_role_and_tampered_reports_rejected(self):
        raw, results = run.simulate(self.config)
        cases = []
        cases.append((raw, results[:-1]))
        wrong = copy.deepcopy(results); wrong[0]["selection_evidence_id"] = wrong[0]["final_evidence_id"]
        cases.append((raw, wrong))
        wrong = copy.deepcopy(results); wrong[0]["additional_cost"] = 99
        cases.append((raw, wrong))
        wrong = copy.deepcopy(results); wrong[0]["final_score"] = -1
        cases.append((raw, wrong))
        cases.append((raw[1:], results))
        extra = copy.deepcopy(raw); extra[0]["role"] = "undeclared"
        cases.append((extra, results))
        for field, value in (("final_cost", 1), ("parent_candidate", 2), ("result_id", "bad-id"), ("final_score", float("nan"))):
            wrong = copy.deepcopy(results); wrong[0][field] = value
            cases.append((raw, wrong))
        for records, reported in cases:
            with self.assertRaises(ValueError):
                run.validate_records(records, reported, self.config)

    def test_invalid_configs(self):
        for field, value in (("repeats", 0), ("candidate_counts", [4, 1]),
                             ("equal_probability", 1.1), ("heterogeneous_range", [0.8, 0.2])):
            cfg = dict(self.config); cfg[field] = value
            with self.assertRaises(ValueError):
                run.simulate(cfg)


if __name__ == "__main__":
    unittest.main()
