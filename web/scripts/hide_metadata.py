"""MkDocs 钩子：剥离页面上不应展示的版本元数据与变更记录。

源文件（course/、lessons/）把版本 / 最后更新 / 变更记录写在正文或 front matter。
front matter 由 MkDocs 自动剥离；正文里的这类元数据由本钩子在渲染前删除。
只影响站点展示，不改源文件，不破坏仓库内部链接。
"""

from __future__ import annotations

import re

# “变更记录：”起，到后续连续列表项结束的整块（含其后的一个空行）
_CHANGELOG = re.compile(
    r"\n+[ \t]*变更记录：[ \t]*\n(?:[ \t]*\n)*(?:[-*][^\n]*\n)+[ \t]*\n?",
    re.MULTILINE,
)

# 单行的版本 / 最后更新行
_VERSION_LINE = re.compile(r"^[ \t]*版本：[^\n]*\n", re.MULTILINE)
_UPDATED_LINE = re.compile(r"^[ \t]*最后更新：[^\n]*\n", re.MULTILINE)

# 标题后连续空行（剥离元数据后清理版面）
_LEADING_BLANKS = re.compile(r"(\n*[^ \t\n].*)\n{2,}", re.MULTILINE)


def on_page_markdown(markdown: str, **_kwargs) -> str:
    md = _CHANGELOG.sub("\n\n", markdown)
    md = _VERSION_LINE.sub("", md)
    md = _UPDATED_LINE.sub("", md)
    # 只清理首个正文标题前的内部登记；正文中的风险/来源状态必须保留。
    heading = re.search(r"^# ", md, re.MULTILINE)
    if heading:
        prefix = re.sub(r"^(?:适用课次|文档类型|状态)：[^\n]*\n", "", md[:heading.start()], flags=re.MULTILINE)
        md = prefix + md[heading.start():]
    # 顶部 H1 后若留出连续空行，压成单个空行
    md = _LEADING_BLANKS.sub(r"\1\n\n", md)
    return md
