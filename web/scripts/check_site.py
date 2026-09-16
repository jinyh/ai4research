"""只读检查构建后的网站：实际链接/锚点、课堂入口与草稿发布边界。"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from student_view import draft_handout

WEB = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.article = []
        self.in_article = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for name in ("href", "src"):
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == "article":
            self.in_article = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False

    def handle_data(self, data):
        if self.in_article:
            self.article.append(data)

    @property
    def text(self):
        return "".join(self.article)


def main():
    site = WEB / "_build"
    base_path = urlsplit(yaml.safe_load((WEB / "mkdocs.yml").read_text())["site_url"]).path
    files = sorted(site.rglob("*.html"))
    if not files:
        print("FAIL: 先构建网站")
        return 1
    pages = {p: Page(p.read_text(encoding="utf-8")) for p in files}
    errors = []
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            url_path = unquote(url.path)
            if url_path.startswith("/"):
                url_path = url_path.removeprefix(base_path)
                target = site / url_path.lstrip("/")
            else:
                target = path.parent / url_path if url_path else path
            target = target.resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_relative_to(site) or not target.exists():
                errors.append(f"{path.relative_to(site)} -> {link}: 文件不存在")
            elif url.fragment and target.suffix == ".html":
                if unquote(url.fragment) not in pages[target].ids:
                    errors.append(f"{path.relative_to(site)} -> {link}: 锚点不存在")

    for n in range(1, 17):
        target = site / f"learn/{n:02}/index.html"
        if target not in pages:
            errors.append(f"第 {n} 讲缺少任务入口")
        elif re.search(r"\d+\s*分钟", pages[target].text):
            errors.append(f"第 {n} 讲任务入口出现课堂计时")

    for n in range(1, 17):
        target = site / f"lessons/lesson-{n:02}/handout/index.html"
        raw = (WEB.parent / f"lessons/lesson-{n:02}/handout.md").read_text()
        text = pages[target].text
        if draft_handout(raw):
            if "讲义待复核" not in text or "学习目标" in text:
                errors.append(f"第 {n} 课草稿正文未被拦截")
        elif "学习目标" not in text or "当前不作为正式学习材料发布" in text:
            errors.append(f"第 {n} 课已通过讲义未正确发布")
    search = json.loads((site / "search/search_index.json").read_text())
    removed_reading_cases = (
        "Mathematics in the Age of AI", "Responses to Referee",
        "How to Look for Ideas", "Coming up with New Ideas",
        "沈向洋", "胡晓峰", "霍强", "Stanford Scientific Writing",
        "How to Write a Great Research Paper",
    )
    reading = pages[site / "course/reading-list/index.html"].text
    if any(title in reading for title in removed_reading_cases):
        errors.append("阅读清单残留已移除的本地案例")
    for relative in ("course/reading-list/index.html", "course/resources/index.html"):
        if "未公开；请查对应公开来源" in pages[site / relative].text:
            errors.append(f"{relative}: 阅读资源仍有不可用的内部入口")
    for entry in search["docs"]:
        if entry["location"].startswith("course/reading-list/"):
            text = entry["title"] + entry["text"]
            if any(title in text for title in removed_reading_cases):
                errors.append("已移除的阅读案例残留在阅读清单搜索记录中")
        if entry["location"].startswith("lessons/") and entry["title"] == "Handout":
            errors.append("搜索结果缺少实际课名")
        match = re.match(r"lessons/lesson-(\d{2})/handout/", entry["location"])
        if match:
            raw = (WEB.parent / f"lessons/lesson-{match[1]}/handout.md").read_text()
            if draft_handout(raw) and "学习目标" in entry["title"] + entry["text"]:
                errors.append(f"第 {match[1]} 课草稿进入搜索结果")
    for path, page in pages.items():
        if re.search(r"gates\s*1[-–]4|适用课次：|文档类型：|最后更新：", page.text):
            errors.append(f"{path.relative_to(site)}: 内部备课元数据仍可见")
        if re.search(r"0\.18|0\.31|120\s*次|讲义待复核", page.text) and path.is_relative_to(site / "learn"):
            errors.append(f"{path.relative_to(site)}: 课堂入口残留旧案例或旧状态")
    forbidden = {"teaching-plan.md", "teacher-review-ledger.md", "application-form-draft.md", "AGENTS.md", "CLAUDE.md"}
    for path in site.rglob("*"):
        if path.is_symlink() or path.name in forbidden or path.suffix == ".pptx":
            errors.append(f"{path.relative_to(site)}: 不应进入学生发布物")
    if errors:
        print("\n".join(sorted(set(errors))))
        print(f"FAIL: {len(set(errors))} 项")
        return 1
    counts = [len(re.sub(r"\s", "", pages[site / f"learn/{n:02}/index.html"].text)) for n in range(1, 17)]
    print(f"PASS: {len(pages)} 个 HTML 页面，内部文件与实际锚点有效；16 个课堂入口齐全；草稿与内部元数据未泄漏。")
    print(f"课堂入口正文非空白字符：{counts}；合计 {sum(counts)}。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
