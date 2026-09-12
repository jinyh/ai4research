"""只读检查构建后的网站：实际链接/锚点、课堂入口与草稿发布边界。"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

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

    draft = pages[site / "lessons/lesson-16/handout/index.html"].text
    if "讲义待复核" not in draft or "学习目标" in draft:
        errors.append("第 16 课草稿正文未被拦截")
    search = json.loads((site / "search/search_index.json").read_text())
    for entry in search["docs"]:
        if entry["location"].startswith("lessons/") and entry["title"] == "Handout":
            errors.append("搜索结果缺少实际课名")
        if entry["location"].startswith("lessons/lesson-16/handout/") and "学习目标" in entry["text"]:
            errors.append("第 16 课草稿进入搜索结果")
    for path, page in pages.items():
        if re.search(r"gates\s*1[-–]4|适用课次：|文档类型：|最后更新：", page.text):
            errors.append(f"{path.relative_to(site)}: 内部备课元数据仍可见")
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
