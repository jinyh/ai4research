#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 Git 管理范围内 Markdown 的内部链接与现行旧路径（只读）。

退出码：跟踪目标断链或现行文档残留旧目录根时为 1，否则为 0。
`references/library/` 是本地外部资料库；其目标缺失只告警，不导致失败。
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parent.parent
LOCAL_LIBRARY = REPO / "references" / "library"

LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
CODE_SPAN_RE = re.compile(r"`[^`]+`")
LEGACY_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:ref/|projects/|final/|ai-research-workflow-course/|"
    r"docs/archive/|\.tmp/|\.ppt_master_inputs/)"
)
LEGACY_EXCLUDED = {"docs/project-reorganization-proposal.md"}


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def tracked_markdown() -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "-z",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            "*.md",
        ],
        cwd=REPO,
        check=True,
        capture_output=True,
    )
    candidates = (
        REPO / os.fsdecode(item)
        for item in result.stdout.split(b"\0")
        if item
    )
    return sorted(
        path for path in candidates
        if path.exists() and not path.is_symlink()
    )


def strip_code_spans(line: str) -> str:
    return CODE_SPAN_RE.sub("", line)


def headings_in(text: str) -> list[str]:
    headings = []
    for line in text.splitlines():
        match = re.match(r"\s*#{1,6}\s+(.*)", line)
        if match:
            headings.append(match.group(1).strip())
            # MkDocs / attr_list 的显式标题锚点。
            if explicit := re.search(r"\{[^}]*#([A-Za-z0-9_-]+)[^}]*\}", match.group(1)):
                headings.append(explicit.group(1))
    return headings


def normalize_anchor(value: str) -> str:
    return re.sub(r"[\W_]+", "", unquote(value), flags=re.UNICODE).lower()


def parse_target(raw_target: str) -> tuple[str, str] | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if not target or target.startswith("//"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    return unquote(parsed.path), unquote(parsed.fragment)


def check_links(files: list[Path]) -> tuple[list[str], list[str], list[str]]:
    broken: list[str] = []
    anchor_warnings: list[str] = []
    local_warnings: list[str] = []

    for source in files:
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            broken.append(f"{source.relative_to(REPO)}  (无法读取：{error})")
            continue

        for line_number, line in enumerate(text.splitlines(), 1):
            for _label, raw_target in LINK_RE.findall(strip_code_spans(line)):
                parsed = parse_target(raw_target)
                if parsed is None:
                    continue
                path_part, anchor = parsed
                target = source if not path_part else (source.parent / path_part).resolve()
                location = f"{source.relative_to(REPO)}:{line_number}"

                if path_part and not target.exists():
                    message = f"{location}  →  {raw_target.strip()}  (文件不存在)"
                    if is_within(target, LOCAL_LIBRARY):
                        local_warnings.append(message)
                    else:
                        broken.append(message)
                    continue

                if anchor and target.is_file() and target.suffix.lower() == ".md":
                    try:
                        target_text = target.read_text(encoding="utf-8")
                    except (OSError, UnicodeDecodeError):
                        continue
                    normalized = normalize_anchor(anchor)
                    available = {normalize_anchor(item) for item in headings_in(target_text)}
                    if normalized and normalized not in available:
                        anchor_warnings.append(
                            f"{location}  →  {raw_target.strip()}  (锚点未匹配到标题)"
                        )

    return broken, anchor_warnings, local_warnings


def check_legacy_paths(files: list[Path]) -> list[str]:
    findings: list[str] = []
    for source in files:
        relative = source.relative_to(REPO).as_posix()
        if relative.startswith("archive/") or relative in LEGACY_EXCLUDED:
            continue
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            match = LEGACY_RE.search(line)
            if match:
                findings.append(
                    f"{relative}:{line_number}  →  {match.group(0)}  (现行文档残留旧路径)"
                )
    return findings


def print_group(title: str, findings: list[str]) -> None:
    if not findings:
        return
    print(f"\n{title} {len(findings)} 处：")
    for finding in findings:
        print(f"      {finding}")


def main() -> int:
    files = tracked_markdown()
    broken, anchor_warnings, local_warnings = check_links(files)
    legacy = check_legacy_paths(files)

    if broken or legacy:
        print(
            f"[FAIL] 扫描 {len(files)} 个 Git 管理范围 Markdown："
            f"{len(broken)} 处断链，{len(legacy)} 处现行旧路径"
        )
    else:
        print(f"[PASS] {len(files)} 个 Git 管理范围 Markdown 的内部链接与目录口径有效")

    print_group("[断链]", broken)
    print_group("[旧路径]", legacy)
    print_group("[锚点告警]", anchor_warnings)
    print_group("[本地资料告警]", local_warnings)
    return 1 if broken or legacy else 0


if __name__ == "__main__":
    sys.exit(main())
