# 课程网站（web/）

当前线上版本由学生专用静态快照部署；本目录保留旧版构建源。更新网站请按本文末尾“当前部署”执行。

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

## 当前部署（2026-09-13）

学生网站使用 `codex/student-site` 分支中的已审阅静态快照，由主分支的 `.github/workflows/deploy-web.yml` 固定到具体提交后部署至 <https://jinyh.github.io/ai4research/>。本次快照包含 63 个 HTML 页面、16 个课堂入口和学生教学工件；第 16 讲完整讲义继续显示待复核提示。

本次只发布学生网站。完整备课修订留在维护者本地，公开主分支中的构建源仍是旧版，因此以上构建说明用于旧源参考，不能直接重建当前线上版本。教师教案、PPT、申请底稿与复核台账不进入本次新增快照；公开仓库已有历史保持原状。

后续更新流程：

1. 从维护中的现行课程源构建网站，运行严格构建、学生页测试、生成站点链接与草稿隔离检查，并审阅公开内容。
2. 仅将通过检查的构建产物更新到 `codex/student-site`，保持分支历史连续；勿合入完整备课提交链。
3. 更新部署工作流的快照提交号并推送至 `main`；该配置变更触发部署。手动运行工作流会重新部署固定快照。
4. 核验 GitHub Pages 部署成功，并检查线上首页、课次入口、项目条件、搜索与第 16 讲待复核页面。

发布前仍须取得明确授权。网站发布清单不限制公开 Git 仓库的可见范围；教师材料和原始图片的全仓公开应单独审核。
