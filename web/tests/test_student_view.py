"""学生入口、权威条件与发布边界的回归检查。"""

import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from mkdocs.exceptions import PluginError

WEB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WEB / "scripts"))
import hide_metadata
import strip_dead_links
import student_view


def page(src):
    return SimpleNamespace(file=SimpleNamespace(src_path=src, abs_src_path=str(WEB / "docs" / src)))


class StudentViewTests(unittest.TestCase):
    def test_conditions_are_from_authority(self):
        source = (WEB.parent / "course/assignments.md").read_text()
        result = student_view.on_page_markdown((WEB / "docs/project.md").read_text(), page=page("project.md"), config={})
        self.assertNotIn("<!-- course:", result)
        self.assertEqual(result.count('??? note "展开'), 4)
        for n, title in enumerate(("问题门", "判断门", "验证门", "论证门与最终个人项目"), 1):
            for line in student_view.section(source, f"Checkpoint {n}：{title}").splitlines():
                if line.startswith("- "):
                    self.assertIn(line, result)
        for weight in ("25%", "30%", "20%"):
            self.assertIn(weight, result)

    def test_missing_authority_fails(self):
        with self.assertRaises(PluginError):
            student_view.section("# Empty", "Checkpoint 1：问题门")

    def test_explicit_heading_anchor(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("course_links", WEB.parent / "scripts/check_links.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertIn("checkpoint-1", module.headings_in("### 问题门 {#checkpoint-1}"))

    def test_draft_is_not_published(self):
        result = student_view.on_page_markdown("SECRET DRAFT BODY", page=page("lessons/lesson-16/handout.md"), config={})
        self.assertNotIn("SECRET DRAFT BODY", result)
        self.assertIn("讲义待复核", result)
        self.assertIn("../../learn/16.md", result)

    def test_reference_title_not_filename(self):
        reference = page("lessons/lesson-08/handout.md")
        student_view.on_page_markdown("# 第八讲｜学生研究方案分享与设计诊所\n\n正文", page=reference, config={})
        self.assertEqual(reference.title, "第八讲｜学生研究方案分享与设计诊所")

    def test_case_status_does_not_block_whole_lesson(self):
        self.assertFalse(student_view.draft_handout("状态：现行\n# 课程\n案例状态：草稿，待教师复核"))
        self.assertTrue(student_view.draft_handout("状态：草稿，待教师复核\n# 课程"))

    def test_metadata_removed_but_risk_kept(self):
        result = hide_metadata.on_page_markdown("版本：v1.0.0\n适用课次：第 1 课\n文档类型：讲义\n状态：gates 1-4 通过\n# 内容\n\n状态：pending\n虚构案例\n")
        self.assertNotIn("gates", result)
        self.assertNotIn("适用课次", result)
        self.assertIn("状态：pending", result)
        self.assertIn("虚构案例", result)

    def test_all_guides_have_reading_and_handout(self):
        for n in range(1, 16):
            result = student_view.on_page_markdown("# 任务", page=page(f"learn/{n:02}.md"), config={})
            self.assertIn(f"lesson-{n:02}/handout.md", result)
            self.assertIn("reading-list.md#", result)

    def test_teacher_section_removed_from_pack(self):
        src = "lessons/lesson-01/classroom-pack.md"
        result = student_view.on_page_markdown((WEB / "docs" / src).read_text(), page=page(src), config={})
        self.assertNotIn("纸面验收三项（教师用）", result)
        self.assertIn("预期非实际", result)

    def test_missing_student_asset_fails(self):
        with self.assertRaises(PluginError):
            strip_dead_links.on_page_markdown("[材料](../lessons/lesson-01/missing.md)", page=page("learn/01.md"), config={"docs_dir": str(WEB / "docs")})

    def test_private_source_is_explicit(self):
        result = strip_dead_links.on_page_markdown("[备课规划](../../lessons/备课规划.md)", page=page("lessons/lesson-01/handout.md"), config={"docs_dir": str(WEB / "docs")})
        self.assertIn("未公开", result)

    def test_outside_docs_not_treated_as_published(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "docs").mkdir()
            (root / "private.md").touch()
            self.assertFalse(strip_dead_links._target_exists("../private.md", root / "docs/index.md", root / "docs"))


if __name__ == "__main__":
    unittest.main()
