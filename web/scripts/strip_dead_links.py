"""已知内部资料明确标为未公开；缺失的学生资源使构建失败。"""

from __future__ import annotations

import os
import re
from pathlib import Path
from urllib.parse import unquote

from mkdocs.exceptions import PluginError

# 匹配 markdown 链接 [label](url)，label 可含 ] 转义但此处取简单形式；
# url 不以 http:// https:// mailto: # 开头（外部链接和锚点不动）。
_LINK_RE = re.compile(
    r"\[(?P<label>[^\]]+)\]\((?P<url>[^)]+)\)",
)


def _is_internal(url: str) -> bool:
    if not url:
        return False
    lower = url.lower()
    if lower.startswith(("http://", "https://", "mailto:", "#", "//")):
        return False
    return True


def _target_exists(url: str, page_src: Path, docs_dir: Path) -> bool:
    """url 相对 page_src 所在目录解析；检查目标文件是否存在于站点内。

    path.exists() 会自动归约 .. 并跟随软链接，因此 docs/ 下的软链接
    （指向仓库源）算作存在；指向 docs/ 外或未发布目标的链接算作不存在。
    url 可能含 #anchor、?query 和 % 编码，先剥离再解码。
    """
    path_part = url.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return True  # 纯锚点，视为存在

    decoded = unquote(path_part)
    # 归约字面路径，不跟随已授权的内容软链接；拒绝 docs/ 外的偶然同名文件。
    target = Path(os.path.abspath(page_src.parent / decoded))
    return target.is_relative_to(docs_dir.absolute()) and target.exists()


def _private_target(url: str, page_src: Path, docs_dir: Path) -> bool:
    target = Path(os.path.abspath(page_src.parent / unquote(url.split("#", 1)[0])))
    relative = os.path.relpath(target, docs_dir)
    return (relative.startswith(("references/", "archive/"))
            or relative in {"AGENTS.md", "CLAUDE.md", "course/curriculum.md", "lessons/备课规划.md"}
            or (relative.startswith("lessons/lesson-") and relative.endswith("/assets/README.md")))


def on_page_markdown(markdown: str, *, page, config, **_kwargs) -> str:
    docs_dir = Path(config["docs_dir"])
    page_src = docs_dir / page.file.src_path

    def _replace(match: re.Match) -> str:
        url = match.group("url").strip().removeprefix("<").removesuffix(">")
        if not _is_internal(url):
            return match.group(0)
        if _target_exists(url, page_src, docs_dir):
            return match.group(0)
        if _private_target(url, page_src, docs_dir):
            return match.group("label") + "（未公开；请查对应公开来源）"
        raise PluginError(f"学生资源未发布或链接错误：{page.file.src_path} -> {url}")

    return _LINK_RE.sub(_replace, markdown)
