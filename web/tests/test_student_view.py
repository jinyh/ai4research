"""学生入口、权威条件与发布边界的回归检查。"""

import sys
import re
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
import build_downloads
import link_content
import check_site
from zipfile import ZipFile


def page(src):
    return SimpleNamespace(file=SimpleNamespace(src_path=src, abs_src_path=str(WEB / "docs" / src)))


class StudentViewTests(unittest.TestCase):
    def test_classroom_clock_excludes_explicit_homework_budget(self):
        self.assertFalse(check_site.has_classroom_timing("课堂怎么做 独立判断 课外与下课去向 课外总投入最多60分钟"))
        self.assertTrue(check_site.has_classroom_timing("课堂怎么做 独立判断10分钟 课外与下课去向 60分钟"))
        self.assertTrue(check_site.has_classroom_timing("课堂怎么做 实践15分钟"))
        self.assertFalse(check_site.has_classroom_timing("课堂怎么做 独立判断与验证"))

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
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "handout.md"
            source.write_text("状态：草稿，待教师复核\n# 草稿\nSECRET DRAFT BODY")
            draft_page = page("lessons/lesson-16/handout.md")
            draft_page.file.abs_src_path = str(source)
            result = student_view.on_page_markdown("SECRET DRAFT BODY", page=draft_page, config={})
        self.assertNotIn("SECRET DRAFT BODY", result)
        self.assertIn("讲义待复核", result)
        self.assertIn("../../learn/16.md", result)

    def test_approved_final_lesson_is_published(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "handout.md"
            source.write_text("状态：现行，教师复核通过\n# 第十六讲\n## 学习目标\n可追溯论证")
            current = page("lessons/lesson-16/handout.md")
            current.file.abs_src_path = str(source)
            self.assertFalse(student_view.draft_handout(source.read_text()))
            result = student_view.on_page_markdown(source.read_text(), page=current, config={})
        self.assertIn("## 学习目标", result)
        self.assertNotIn("当前不作为正式学习材料发布", result)

    def test_reference_title_not_filename(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "handout.md"
            source.write_text("状态：现行，教师复核通过\n# 第八讲｜学生研究方案分享与设计诊所\n\n正文")
            reference = page("lessons/lesson-08/handout.md")
            reference.file.abs_src_path = str(source)
            student_view.on_page_markdown(source.read_text(), page=reference, config={})
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
        for n in range(1, 17):
            result = student_view.on_page_markdown("# 任务", page=page(f"learn/{n:02}.md"), config={})
            self.assertIn(f"lesson-{n:02}/handout.md", result)
            self.assertIn("reading-list.md#", result)
            if n == 16:
                self.assertNotIn("17.md", result)
                self.assertIn("project.md#checkpoint-4", result)

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

    def test_reading_list_keeps_core_without_private_entries(self):
        source = (WEB.parent / "course/reading-list.md").read_text()
        visible = hide_metadata.on_page_markdown(source)
        self.assertNotIn("../references/", visible)
        self.assertNotIn("../archive/", visible)
        for title in ("Mathematics in the Age of AI", "Responses to Referee",
                      "How to Look for Ideas", "Coming up with New Ideas",
                      "沈向洋", "胡晓峰", "霍强", "Stanford Scientific Writing",
                      "How to Write a Great Research Paper"):
            self.assertNotIn(title, visible)
        lessons = re.findall(r"^## 第 (\d+) 课：", visible, re.MULTILINE)
        self.assertEqual(lessons, [str(n) for n in range(1, 17)])
        self.assertEqual(visible.count("**核心｜"), 12)
        self.assertEqual(visible.count("**参考（研究门课不加必读）｜"), 4)
        self.assertIn("Keshav", visible)
        self.assertIn("未经授权", visible)

    def test_rsi_download_is_exact_student_whitelist(self):
        with tempfile.TemporaryDirectory() as folder:
            build_downloads.build_rsi_download({"docs_dir": folder}, link_content.PUBLISH)
            with ZipFile(Path(folder) / "downloads/rsi-selection-case.zip") as archive:
                self.assertEqual(set(archive.namelist()),
                                 {f"rsi-selection-case/{name}" for name in build_downloads.RSI_FILES})
                for name in archive.namelist():
                    self.assertNotIn("teacher", name)
                    self.assertNotIn(".work", name)
                    self.assertNotIn(b"/Users/bright", archive.read(name))
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(PluginError):
                build_downloads.build_rsi_download({"docs_dir": folder}, set())

    def test_judgment_bundles_keep_teacher_answers_private(self):
        for n in range(1, 17):
            self.assertIn(f"lessons/lesson-{n:02}/judgment-task.md", link_content.PUBLISH)
            self.assertNotIn(f"lessons/lesson-{n:02}/judgment-teacher.md", link_content.PUBLISH)
        with tempfile.TemporaryDirectory() as folder:
            build_downloads.build_judgment_downloads({"docs_dir": folder}, link_content.PUBLISH)
            with ZipFile(Path(folder) / "downloads/judgment-tasks.zip") as archive:
                self.assertEqual(set(archive.namelist()), set(build_downloads.JUDGMENT_FILES))
                for name in archive.namelist():
                    self.assertNotIn("teacher", name)
                    self.assertNotIn(b"/Users/bright", archive.read(name))
                    self.assertNotIn(b".work/", archive.read(name))
            for name in ("micro-project.zip", "search-diagnosis.zip"):
                with ZipFile(Path(folder) / "downloads" / name) as archive:
                    self.assertIn("README.md", archive.namelist())
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(PluginError):
                build_downloads.build_judgment_downloads({"docs_dir": folder}, {})

    def test_outside_docs_not_treated_as_published(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "docs").mkdir()
            (root / "private.md").touch()
            self.assertFalse(strip_dead_links._target_exists("../private.md", root / "docs/index.md", root / "docs"))


if __name__ == "__main__":
    unittest.main()
