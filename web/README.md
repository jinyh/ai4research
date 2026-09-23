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

- `course/`：`syllabus`、`assessment`、`assignments`、`reading-list`、`resources`、`pi-setup`、`opencode-setup`、`metax-compute` 与三份学生项目模板（`starter-template`、`project-template`、`ethics-and-compliance-template`）
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

## 当前部署（2026-09-23）

本次更新Lesson 01阅读卡与限定条件遗漏的具体样例，并同步课堂材料包的新页码。学生快照为`ea7940f33778ebe934bb2ac8044a5e3257c4c6bd`，延续`codex/student-site`历史；对应35页PPT在课程源仓库维护，不进入学生网站。

本地14项网站测试、严格构建、69页文件/锚点/发布边界检查通过。与上次快照相比，仅第1课讲义、课堂包、搜索索引和站点地图变化；课程首页、其他课次与下载ZIP保持一致。部署结果由GitHub Actions和线上文件核验确认。

## 上一次部署（2026-09-22）

本次按用户明确授权发布沐曦算力支持与此前课程改进，学生快照为 `74d1f1789c4f4b22c5a91e58b139fa651d454709`，部署配置提交为 `21a0d5895714a775b1265bf8f97b9aa3c1715d87`。共 69 个 HTML 页面；新增算力申请、Pi 模型接入、GPU 使用与结果保存指南，首页、资源页和第 1、9–13 讲提供入口。同步 Pi 主平台、Lesson 01 阅读卡链路及现行学生材料。

本地严格构建、14 项网站测试、69 页内部链接/锚点/发布边界检查、12 项课程一致性检查通过。浏览器检查首页、算力页及第 1 讲；下载包 SHA-256 为 `f80d50a335c599956cc4bb3b152b8344ac9416588937ee965fe39a7331fdb16b`。发布仅更新学生静态快照与部署配置；现行课程源继续在本地维护。

发布任务：[GitHub Actions](https://github.com/jinyh/ai4research/actions/runs/35720363098)已成功。线上首页经浏览器确认；另下载核对首页、算力页、Pi 指南、第 1/9/16 讲、项目条件、第 1 课完整讲义、搜索索引与材料 ZIP，共 10 项与验收构建逐字节一致。

## 上一次部署（2026-09-16）

学生网站使用 `codex/student-site` 分支中的已审阅静态快照，由主分支的 `.github/workflows/deploy-web.yml` 固定到具体提交后部署至 <https://jinyh.github.io/ai4research/>。本次发布目标为 `b2465696d4621eef2c3fd79668f7cdceda28676c`，包含 67 个 HTML 页面、16 个课堂入口、第 16 课完整讲义及可复演阅读卡材料包。

本轮同步第 6–15 课的命题、机制、评价、写作与评审入口，保留原布局与已在线的精简阅读资源。学生快照包含讲义和明确列入清单的课堂工件；教师教案、PPT、申请底稿与复核台账不进入该快照。课程仓库与网站发布物分别管理。

本地验证：14 项学生页测试、严格构建、67 页链接/锚点/发布边界检查通过；下载 ZIP 解压后实际运行退出码为 `2/0/0/3`，包内 5 项行为测试通过。浏览器已检查第 14、16 课、完整讲义、材料下载说明及 T03 搜索结果。最终线上是否生效以部署工作流和实际页面核验为准。

后续更新流程：

1. 从维护中的现行课程源构建网站，运行严格构建、学生页测试、生成站点链接与草稿隔离检查，并审阅公开内容。
2. 仅将通过检查的构建产物更新到 `codex/student-site`，保持分支历史连续；勿合入完整备课提交链。
3. 更新部署工作流的快照提交号并推送至 `main`；该配置变更触发部署。手动运行工作流会重新部署固定快照。
4. 核验 GitHub Pages 部署成功，并检查线上首页、课次入口、项目条件、搜索、第 16 讲完整讲义，以及下载 ZIP 与已验收文件的指纹一致。

发布前仍须取得明确授权。网站发布清单不限制公开 Git 仓库的可见范围；教师材料和原始图片的全仓公开应单独审核。
