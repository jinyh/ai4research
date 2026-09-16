# 课程网站（web/）

网站由学生专用静态快照部署；本目录为现行构建源。更新网站请按本文末尾“当前部署”执行。

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

发布前检查：

```sh
uv run python -m unittest discover -s tests -v
uv run mkdocs build --strict
uv run python scripts/check_site.py
```

构建时按明确文件清单生成 `downloads/reading-card-workflow.zip`；下载包含运行器、测试和 5 份 JSON，不收集运行目录或本机文件。第 16 课讲义已通过本轮内容确认并正常发布；草稿拦截仍按源文件状态生效。

## 不展示的元数据

源文件正文里的版本行、最后更新行、变更记录节由 `scripts/hide_metadata.py`（MkDocs 钩子）在渲染前剥离，不显示在网页上。front matter 由 MkDocs 自动剥离。钩子只影响站点展示，不改源文件。

## 发布范围

只发布面向学生的内容，**发布清单在 `scripts/link_content.py` 顶部维护**：

- `course/`：`syllabus`、`assessment`、`assignments`、`reading-list`、`resources` 与三份学生项目模板（`starter-template`、`project-template`、`ethics-and-compliance-template`）
- `lessons/lesson-NN/`：`handout.md`（学生讲义），以及发布清单中逐文件登记的课堂材料包、模板、教学示例、可复现工件和图形资产；不软链整个目录

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
| `docs/index.md`、`docs/teacher.md`、`docs/templates.md` | 手写的门户首页、课程介绍与模板/示例聚合入口 |
| `docs/course/`、`docs/lessons/` | 软链接内容（由脚本生成，勿手改） |
| `scripts/link_content.py` | 发布清单与软链接维护脚本 |
| `_build/` | `mkdocs build` 输出（.gitignore 忽略） |
| `.venv/` | uv 虚拟环境（.gitignore 忽略） |

## 当前部署（2026-09-16）

学生网站使用 `codex/student-site` 分支中的已审阅静态快照，由主分支的 `.github/workflows/deploy-web.yml` 固定到具体提交后部署至 <https://jinyh.github.io/ai4research/>。本次发布目标为 `b2465696d4621eef2c3fd79668f7cdceda28676c`，包含 67 个 HTML 页面、16 个课堂入口、第 16 课完整讲义及可复演阅读卡材料包。

本轮同步第 6–15 课的命题、机制、评价、写作与评审入口，保留原布局与已在线的精简阅读资源。学生快照包含讲义和明确列入清单的课堂工件；教师教案、PPT、申请底稿与复核台账不进入该快照。课程仓库与网站发布物分别管理。

本地验证：14 项学生页测试、严格构建、67 页链接/锚点/发布边界检查通过；下载 ZIP 解压后实际运行退出码为 `2/0/0/3`，包内 5 项行为测试通过。浏览器已检查第 14、16 课、完整讲义、材料下载说明及 T03 搜索结果。最终线上是否生效以部署工作流和实际页面核验为准。

后续更新流程：

1. 从维护中的现行课程源构建网站，运行严格构建、学生页测试、生成站点链接与草稿隔离检查，并审阅公开内容。
2. 仅将通过检查的构建产物更新到 `codex/student-site`，保持分支历史连续；勿合入完整备课提交链。
3. 更新部署工作流的快照提交号并推送至 `main`；该配置变更触发部署。手动运行工作流会重新部署固定快照。
4. 核验 GitHub Pages 部署成功，并检查线上首页、课次入口、项目条件、搜索、第 16 讲完整讲义，以及下载 ZIP 与已验收文件的指纹一致。

发布前仍须取得明确授权。网站发布清单不限制公开 Git 仓库的可见范围；教师材料和原始图片的全仓公开应单独审核。
