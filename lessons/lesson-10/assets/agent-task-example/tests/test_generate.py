import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "after" / "generate.py"
SPEC = importlib.util.spec_from_file_location("generate", MODULE_PATH)
generate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generate)


class GenerateTest(unittest.TestCase):
    def test_normalize_record_strips_summary(self):
        self.assertEqual(
            generate.normalize_record({"paper_id": "p1", "summary": "  result  "}),
            {"paper_id": "p1", "summary": "result"},
        )

    def test_normalize_record_rejects_missing_field(self):
        with self.assertRaisesRegex(ValueError, "summary"):
            generate.normalize_record({"paper_id": "p1"})


if __name__ == "__main__":
    unittest.main()
