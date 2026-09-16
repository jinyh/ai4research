"""学生入口与权威材料的构建期连接；不改讲义源，不发布内容门草稿。"""

from __future__ import annotations

import re
from pathlib import Path

from markdown.extensions.toc import slugify
from mkdocs.exceptions import PluginError

REPO = Path(__file__).resolve().parents[2]


def section(text: str, heading: str) -> str:
    match = re.search(r"^## " + re.escape(heading) + r"\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise PluginError(f"权威内容缺少章节：{heading}")
    return match.group(1).strip()


def first_table(text: str) -> str:
    match = re.search(r"^\|[^\n]*\n(?:\|[^\n]*(?:\n|$))+", text, re.MULTILINE)
    if not match:
        raise PluginError("评分权威源缺少比例表")
    return match.group(0).strip()


def draft_handout(raw: str) -> bool:
    """在标题前识别门控状态，不将正文虚构/风险案例误判为整课草稿。"""
    prefix = re.split(r"^# ", raw, maxsplit=1, flags=re.MULTILINE)[0]
    return bool(re.search(r"^(?:状态|文档类型)：[^\n]*(?:草稿|待教师复核|阻塞)", prefix, re.MULTILINE))


def on_page_markdown(markdown: str, *, page, config, **_kwargs) -> str:
    src = page.file.src_path
    # 参考页退出顶层导航后仍使用正文课名，避免搜索结果退化为 Handout。
    title = re.search(r"^# ([^\n]+)", markdown, re.MULTILINE)
    if title and src.startswith(("lessons/", "course/")):
        page.title = title.group(1).strip()
    if src == "project.md":
        assessment = (REPO / "course/assessment.md").read_text(encoding="utf-8")
        assignments = (REPO / "course/assignments.md").read_text(encoding="utf-8")
        table = first_table(section(assessment, "总体结构"))
        # 入口只显示评分维度与比例，完整解释仍在评分权威源。
        table = "\n".join("| " + " | ".join(cell.strip() for cell in row.strip("|").split("|")[:2]) + " |" for row in table.splitlines())
        markdown = markdown.replace("<!-- course:score-table -->", table)
        for n, title in enumerate(("问题门", "判断门", "验证门", "论证门与最终个人项目"), 1):
            content = section(assignments, f"Checkpoint {n}：{title}")
            # 从原文逐字取条件；引用的相对链接转为 project.md 所在层级。
            content = re.sub(r"\]\(\./", "](course/", content)
            detail = f'??? note "展开{title}完整条件"\n\n' + "\n".join("    " + line if line else "" for line in content.splitlines())
            markdown = markdown.replace(f"<!-- course:checkpoint-{n} -->", detail)
        if "<!-- course:" in markdown:
            raise PluginError("项目入口含未处理的权威引用")

    handout = re.fullmatch(r"lessons/lesson-(\d{2})/handout.md", src)
    if handout:
        num = handout.group(1)
        raw = Path(page.file.abs_src_path).read_text(encoding="utf-8")
        if draft_handout(raw):
            page.title = f"第 {int(num)} 讲 · 讲义待复核"
            return (f"# 第 {int(num)} 讲 · 讲义待复核\n\n"
                    "详细讲义尚待教师复核，当前不作为正式学习材料发布。\n\n"
                    f"[查看本课已确认的任务](../../learn/{num}.md) · "
                    "[查看正式提交条件](../../project.md)\n")
        markdown = f"[← 本课任务与材料](../../learn/{num}.md)\n\n" + markdown

    guide = re.fullmatch(r"learn/(\d{2})\.md", src)
    if guide:
        num = guide.group(1)
        readings = (REPO / "course/reading-list.md").read_text(encoding="utf-8")
        heading = re.search(rf"^## (第 {int(num)} 课：[^\n]+)", readings, re.MULTILINE)
        if not heading:
            raise PluginError(f"第 {num} 课缺少阅读入口")
        anchor = slugify(heading.group(1), "-")
        onward = (f"[下一讲]({int(num) + 1:02}.md)" if int(num) < 16
                  else "[论证门与项目提交](../project.md#checkpoint-4)")
        markdown += (f"\n\n---\n\n[完整讲义：方法、案例与来源](../lessons/lesson-{num}/handout.md) · "
                     f"[本课阅读范围](../course/reading-list.md#{anchor}) · {onward}\n")

    if src == "lessons/lesson-15/calibration-pack.md":
        markdown = markdown.replace("## 教师参考评审", "## 参考评审（先完成自己的判断）")

    if src == "lessons/lesson-01/classroom-pack.md":
        markdown = re.sub(r"^## 五、纸面验收三项（教师用）.*?(?=^## 六、)", "", markdown, flags=re.MULTILINE | re.DOTALL)

    back = {"course/syllabus.md": "[← 16 讲任务总览](../learn/index.md)",
            "course/assessment.md": "[← 项目与考核速览](../project.md)",
            "course/assignments.md": "[← 项目与考核速览](../project.md)"}
    if src in back:
        markdown = back[src] + "\n\n" + markdown
    return markdown
