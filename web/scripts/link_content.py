"""建立/刷新 web/docs 下的内容软链接。

设计：
- 源内容在仓库根的 course/ 与 lessons/lesson-NN/，更新频繁。
- 用软链接引入 web/docs/，源文件改后自动跟随，无需重新同步。
- 只链接“面向学生可发布”的子集；教案、逐页母稿、精读卡、协作规范、
  申报底稿等内部文档不在此清单，天然不会进入站点。
- 幂等：已存在且指向正确的链接跳过；否则重建。

用法：
    cd web && uv run python scripts/link_content.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# web/ 目录 = 本文件父目录的父目录
WEB_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = WEB_DIR.parent
DOCS_DIR = WEB_DIR / "docs"

# 发布清单：相对仓库根的源文件 -> 相对 docs/ 的目标路径
PUBLISH = {
    # 课程级权威文档（不含 sync-rules / ppt-quality-gates / 申报底稿 / 模板 / curriculum）
    # curriculum.md 与 syllabus.md 面向学生的内容重复，且为内部治理定位，不在网站发布
    "course/syllabus.md": "course/syllabus.md",
    "course/assessment.md": "course/assessment.md",
    "course/assignments.md": "course/assignments.md",
    "course/reading-list.md": "course/reading-list.md",
    "course/resources.md": "course/resources.md",
    # 学生项目模板（handout 和 assignments 引用，学生需要内容本身）
    "course/starter-template.md": "course/starter-template.md",
    "course/project-template.md": "course/project-template.md",
    "course/ethics-and-compliance-template.md": "course/ethics-and-compliance-template.md",
    # 每课只发布学生讲义 handout.md（不含 teaching-plan / slides / reading-notes / README）
    "lessons/lesson-01/handout.md": "lessons/lesson-01/handout.md",
    "lessons/lesson-02/handout.md": "lessons/lesson-02/handout.md",
    "lessons/lesson-03/handout.md": "lessons/lesson-03/handout.md",
    # 第 3 课学生向教学示例（2.0 G2：课级示例发布）
    "lessons/lesson-03/source-audit-demo.md": "lessons/lesson-03/source-audit-demo.md",
    "lessons/lesson-03/mi-search-trace-demo.md": "lessons/lesson-03/mi-search-trace-demo.md",
    # 第 3 课图形资产（2.0 配图管线：逐文件软链，不软链目录——
    # 规避 mkdocs 对软链目录 followlinks 的不确定性；handout 引用前必须先登记并运行生效）
    "lessons/lesson-03/assets/research-chain-stage4-structure.svg": "lessons/lesson-03/assets/research-chain-stage4-structure.svg",
    "lessons/lesson-03/assets/search-process-structure.svg": "lessons/lesson-03/assets/search-process-structure.svg",
    "lessons/lesson-03/assets/verification-states-entry-structure.svg": "lessons/lesson-03/assets/verification-states-entry-structure.svg",
    "lessons/lesson-03/assets/keshav-2007-trace-structure.svg": "lessons/lesson-03/assets/keshav-2007-trace-structure.svg",
    "lessons/lesson-04/handout.md": "lessons/lesson-04/handout.md",
    "lessons/lesson-05/handout.md": "lessons/lesson-05/handout.md",
    "lessons/lesson-06/handout.md": "lessons/lesson-06/handout.md",
    "lessons/lesson-07/handout.md": "lessons/lesson-07/handout.md",
    "lessons/lesson-08/handout.md": "lessons/lesson-08/handout.md",
    "lessons/lesson-09/handout.md": "lessons/lesson-09/handout.md",
    "lessons/lesson-10/handout.md": "lessons/lesson-10/handout.md",
    "lessons/lesson-11/handout.md": "lessons/lesson-11/handout.md",
    "lessons/lesson-12/handout.md": "lessons/lesson-12/handout.md",
    "lessons/lesson-13/handout.md": "lessons/lesson-13/handout.md",
    "lessons/lesson-14/handout.md": "lessons/lesson-14/handout.md",
    "lessons/lesson-15/handout.md": "lessons/lesson-15/handout.md",
    "lessons/lesson-16/handout.md": "lessons/lesson-16/handout.md",
}


def ensure_link(src: Path, dst: Path) -> str:
    """确保 dst 是指向 src 的相对软链接。返回操作说明。

    用相对路径（相对 dst.parent）建软链接，使仓库在任意检出环境
    （本地、CI）都能跟随源文件，不绑定绝对路径。
    """
    rel = os.path.relpath(src, dst.parent)
    if dst.is_symlink():
        if os.readlink(dst) == rel:
            return "ok"
        dst.unlink()
    elif dst.exists():
        # 目标是真实文件/目录，不覆盖，报错
        return f"SKIP (real file exists): {dst}"
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)

    dst.symlink_to(rel)
    return "linked"


def main() -> int:
    if not DOCS_DIR.exists():
        DOCS_DIR.mkdir(parents=True)

    results: list[tuple[str, str]] = []
    for src_rel, dst_rel in PUBLISH.items():
        src = (REPO_ROOT / src_rel).resolve()
        dst = DOCS_DIR / dst_rel  # 不 resolve：保留路径以便 is_symlink 正确判断已建软链接
        if not src.exists():
            results.append((src_rel, f"MISSING SOURCE"))
            continue
        results.append((src_rel, ensure_link(src, dst)))

    width = max(len(s) for s, _ in results)
    for src_rel, msg in results:
        print(f"  {src_rel.ljust(width)}  ->  {msg}")

    errors = [s for s, m in results if m not in ("ok", "linked")]
    if errors:
        print(f"\n!! {len(errors)} 个源文件缺失或目标冲突", file=sys.stderr)
        return 1
    print(f"\n完成：{len(results)} 个链接")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
