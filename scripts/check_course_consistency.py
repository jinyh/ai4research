#!/usr/bin/env python3
"""检查课程核心口径、课次入口元数据与归档边界（只读）。"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
LESSONS = REPO / "lessons"
VERSION_RE = re.compile(r"版本：\s*(v\d+\.\d+\.\d+)")
MOC_ROW_RE = re.compile(
    r"^\| \[([^]]+\.md)\]\(\./([^)]+\.md)\) \|[^|]*?\b(v\d+\.\d+\.\d+)\b",
    re.MULTILINE,
)
SLIDE_XML_RE = re.compile(r"ppt/slides/slide\d+\.xml$")


class Checks:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passes: list[str] = []

    def check(self, condition: bool, success: str, failure: str) -> None:
        if condition:
            self.passes.append(success)
        else:
            self.failures.append(failure)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def table_rows(text: str, first_cell: str) -> list[list[str]]:
    rows: list[list[str]] = []
    active = False
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if line.startswith("|") and cells and cells[0] == first_cell:
            active = True
            continue
        if not active:
            continue
        if not line.startswith("|"):
            break
        if cells and set(cells[0]) <= {"-", ":"}:
            continue
        rows.append(cells)
    return rows


def check_lesson_structure(checks: Checks) -> None:
    expected = set(range(1, 17))
    dirs = {
        int(match.group(1))
        for path in LESSONS.glob("lesson-*")
        if path.is_dir() and (match := re.fullmatch(r"lesson-(\d{2})", path.name))
    }
    checks.check(dirs == expected, "第 1-16 课目录齐全", f"课次目录异常：{sorted(dirs)}")

    syllabus = read(REPO / "course/syllabus.md")
    rows = table_rows(syllabus, "次数")
    numbers = [int(row[0]) for row in rows if row and row[0].isdigit()]
    checks.check(numbers == list(range(1, 17)), "syllabus 课次连续且唯一", f"syllabus 课次为 {numbers}")
    if len(rows) == 16:
        checks.check(
            "不新增正式提交" in rows[7][6],
            "第 8 课明确不新增正式提交",
            "第 8 课阶段产出未明确“不新增正式提交”",
        )


def check_submissions_and_scores(checks: Checks) -> None:
    assignments = read(REPO / "course/assignments.md")
    rows = table_rows(assignments, "课次")
    formal = {
        int(row[0]): row[2].strip("*")
        for row in rows
        if len(row) >= 3 and row[0].isdigit() and row[2] != "—"
    }
    expected = {
        6: "问题门材料包",
        9: "判断门材料包",
        13: "验证门材料包",
        16: "论证门材料与最终项目",
    }
    checks.check(formal == expected, "正式提交仅在第 6/9/13/16 课且门名一致", f"正式提交表为 {formal}")

    assessment = read(REPO / "course/assessment.md")
    score_rows = table_rows(assessment, "项目")
    scores = [int(match.group(1)) for row in score_rows if len(row) >= 2 and (match := re.fullmatch(r"(\d+)%", row[1]))]
    checks.check(sum(scores) == 100 and len(scores) == 4, "四项评分比例合计 100%", f"评分比例为 {scores}，合计 {sum(scores)}%")


def check_application_hours(checks: Checks) -> None:
    form = read(REPO / "course/application-form-draft.md")
    zh = table_rows(form, "模块")
    en = table_rows(form, "Module")
    zh_hours = [int(row[2]) for row in zh if len(row) >= 3 and row[2].isdigit()]
    en_hours = [int(row[2]) for row in en if len(row) >= 3 and row[2].isdigit()]
    checks.check(sum(zh_hours) == 32 and len(zh_hours) == 5, "中文模块课时合计 32", f"中文模块课时为 {zh_hours}")
    checks.check(sum(en_hours) == 32 and len(en_hours) == 5, "英文模块课时合计 32", f"英文模块课时为 {en_hours}")


def check_lesson_metadata(checks: Checks) -> None:
    mismatches: list[str] = []
    page_mismatches: list[str] = []
    for number in range(1, 17):
        lesson = LESSONS / f"lesson-{number:02d}"
        moc = read(lesson / "README.md")
        for _label, target_name, declared in MOC_ROW_RE.findall(moc):
            target = lesson / target_name
            match = VERSION_RE.search(read(target)) if target.exists() else None
            actual = match.group(1) if match else None
            if actual != declared:
                mismatches.append(f"L{number:02d} {target_name}: README {declared}, 文件 {actual or '无版本'}")

        pptx = lesson / "slides.pptx"
        page_match = re.search(r"\[slides\.pptx\]\(\./slides\.pptx\).*?（(\d+) 页）", moc)
        try:
            with zipfile.ZipFile(pptx) as archive:
                actual_pages = sum(bool(SLIDE_XML_RE.fullmatch(name)) for name in archive.namelist())
        except (OSError, zipfile.BadZipFile):
            actual_pages = -1
        declared_pages = int(page_match.group(1)) if page_match else -1
        if actual_pages != declared_pages:
            page_mismatches.append(f"L{number:02d}: README {declared_pages}, PPTX {actual_pages}")

    checks.check(not mismatches, "课次 README 的现行 Markdown 版本与源文件一致", "；".join(mismatches))
    checks.check(not page_mismatches, "16 套 PPTX 页数与课次 README 一致", "；".join(page_mismatches))


def check_authoritative_sources_and_archive(checks: Checks) -> None:
    root_contract = REPO / "references/material-contracts.md"
    duplicate = REPO / ".agents/skills/prepare-course-lesson/references/material-contracts.md"
    skill = read(REPO / ".agents/skills/prepare-course-lesson/SKILL.md")
    checks.check(
        root_contract.exists() and not duplicate.exists() and "../../../references/material-contracts.md" in skill,
        "课程材料契约只有一个权威源，skill 使用显式链接",
        "课程材料契约仍有重复副本或 skill 未链接权威源",
    )

    retired = {
        "course/course-proposal.md": "archive/superseded-docs/course-proposal-v1.3.0.md",
        "docs/project-reorganization-proposal.md": "archive/superseded-docs/project-reorganization-proposal.md",
        "docs/research-question-to-search-skill-plan.md": "archive/superseded-docs/research-question-to-search-skill-plan-v1.1.2.md",
        "lessons/ppt-production-progress.md": "archive/superseded-docs/ppt-production-progress-v0.9.0.md",
        "lessons/lesson-03/mi-search-trace-ai-suggestions.md": "archive/superseded-docs/lesson-03/mi-search-trace-ai-suggestions-v0.1.0.md",
    }
    bad = [source for source, target in retired.items() if (REPO / source).exists() or not (REPO / target).exists()]
    checks.check(not bad, "被替代文档已退出活动路径并进入统一归档", f"归档映射异常：{bad}")

    l16_handout = read(LESSONS / "lesson-16/handout.md")
    l16_moc = read(LESSONS / "lesson-16/README.md")
    checks.check(
        "状态：草稿" in l16_handout and "待定稿·学生讲义" in l16_moc and "课堂 PPT 候选" in l16_moc,
        "第 16 课草稿内容门与 PPT 候选状态保持一致",
        "第 16 课草稿、README 或 PPT 状态边界不一致",
    )


def main() -> int:
    checks = Checks()
    check_lesson_structure(checks)
    check_submissions_and_scores(checks)
    check_application_hours(checks)
    check_lesson_metadata(checks)
    check_authoritative_sources_and_archive(checks)

    for item in checks.passes:
        print(f"[PASS] {item}")
    for item in checks.failures:
        print(f"[FAIL] {item}")
    print(f"\n{len(checks.passes)} passed, {len(checks.failures)} failed")
    return 1 if checks.failures else 0


if __name__ == "__main__":
    sys.exit(main())
