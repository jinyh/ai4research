# 课程网站（web/）

本目录是“智能科研方法”课程门户，用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建。内容以软链接方式从仓库根的 `course/` 与 `lessons/` 引入，源文件改后自动跟随，无需手动同步。

## 本地预览

```sh
cd web
uv sync                       # 首次安装依赖
uv run python scripts/link_content.py   # 建立/刷新内容软链接
uv run mkdocs serve           # 启动本地预览：http://127.0.0.1:8000
```

## 构建静态站点

```sh
cd web
uv run mkdocs build            # 输出到 web/_build/
```

## 不展示的元数据

源文件正文里的版本行、最后更新行、变更记录节由 `scripts/hide_metadata.py`（MkDocs 钩子）在渲染前剥离，不显示在网页上。front matter 由 MkDocs 自动剥离。钩子只影响站点展示，不改源文件。

## 发布范围

只发布面向学生的内容，**发布清单在 `scripts/link_content.py` 顶部维护**：

- `course/`：`syllabus`、`assessment`、`assignments`、`reading-list`、`resources` 与三份学生项目模板（`starter-template`、`project-template`、`ethics-and-compliance-template`）
- `lessons/lesson-NN/`：仅 `handout.md`（学生讲义）；已登记的 `assets/` 图形资产（逐文件软链）与课级学生向示例（第 3 课 `source-audit-demo.md`）

**不发布**：教师教案 `teaching-plan.md`、逐页母稿 `slides.md`、文献精读卡 `reading-notes.md`、课级 `assets/README.md` 等备课元数据、协作规范（`sync-rules`、`ppt-quality-gates`）、申报底稿、`archive/`、`references/library/`、`AGENTS.md`/`CLAUDE.md`。

## 增加新课次讲义

1. 在 `scripts/link_content.py` 的 `PUBLISH` 字典加一行：
   ```python
   "lessons/lesson-03/handout.md": "lessons/lesson-03/handout.md",
   ```
2. 重新运行 `uv run python scripts/link_content.py`。
3. 在 `mkdocs.yml` 的 `nav > 课程讲义` 加对应条目。

## 目录约定

| 路径 | 说明 |
| --- | --- |
| `mkdocs.yml` | MkDocs 配置（主题、nav、中文搜索） |
| `pyproject.toml` | `uv` 管理的依赖（mkdocs、mkdocs-material） |
| `docs/` | 站点源：手写页面 + 软链接引入的内容 |
| `docs/index.md`、`docs/teacher.md` | 手写的门户首页与课程介绍 |
| `docs/course/`、`docs/lessons/` | 软链接内容（由脚本生成，勿手改） |
| `scripts/link_content.py` | 发布清单与软链接维护脚本 |
| `_build/` | `mkdocs build` 输出（.gitignore 忽略） |
| `.venv/` | uv 虚拟环境（.gitignore 忽略） |

## 部署（后续）

部署到 GitHub Pages 时再在 `mkdocs.yml` 配置 `site_url` / `repo_url`，可用 `uv run mkdocs gh-deploy` 或仓库 Actions 自动构建。
