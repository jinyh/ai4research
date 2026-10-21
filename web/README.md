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

构建时按明确清单生成阅读卡回放、RSI、检索诊断、共同判断任务和微型项目下载包，不收集本机文件或运行目录。16课现行学生材料按本轮发布授权同步；教师内容复核、助教计时试做及现场验证另行登记，草稿拦截仍按源文件状态生效。

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

## 当前部署（2026-10-21）

用户明确要求更新 <https://jinyh.github.io/ai4research/>。课程源为 `8e2ca19655512338fa44128cfa4a1954dac529d0`（`codex/ai-research-revision`），学生静态快照为 `1a9bde13423ef06f2063b98052efb8639238714a`（`codex/student-site`），部署指针为 `f8d8c157096369bcc35cf6c858aa2c4650eb9b5e`（`main`）。两个发布分支均沿用远端历史；主分支仅更新工作流中的快照提交号。

本轮将L01–L04现行学生讲义、共同任务、阅读清单、逐课路径、L04阅读指南及下载包同步到网页，并校正四课入口的个人项目与阅读预算要求。新增L01开发观察说明及原始精度JSON；输入是课程构造，数值身份和来源指纹保留。补齐逐文件发布清单与下载清单，L01任务使用固定锚点，前沿研究链接直接指向公开来源。快照共206个文件、97个HTML页面、6个学生下载ZIP；较10月20日新增2个文件、修改21个文件，无删除。

发布前17项网站测试、严格构建、97页内部链接／锚点／发布边界、6个ZIP完整性、12项课程一致性、248份Markdown链接及44项Harness测试通过。L04与新增观察页完成浏览器核对。教师答案、教案、逐页母稿、PPT和本机评审记录不进入学生快照；既有课件和现场待核状态按课次记录保留。

[GitHub Actions发布任务](https://github.com/jinyh/ai4research/actions/runs/39571308260)成功。线上117项文件（全部97个HTML、6个ZIP、10个SVG、搜索索引、两份站点地图及新增观察JSON）与验收快照逐字节一致；L04教师答案和教案路径均返回404。L04线上页面已在浏览器确认新阅读范围与预算。发布清单、差异、原始核验报告及截图保存在本机 `.work/publish-20261021/`；此目录不纳入Git。

## 上一次部署（2026-10-20）

用户明确授权提交、推送与发布。课程源提交为 `eaeadca84a424b85c5cbf15013c741e9a21a600c`（`codex/ai-research-revision`）；学生网站快照为 `ba1acc4a0778381323ed881670f40a40fe626ee8`（`codex/student-site`）；部署指针提交为 `955c2ea009ac4b4ae9df2e9fda10f96abcdca452`（`main`）。网站快照延续原分支历史，主分支仅更新部署指针。

本轮同步“MI 教师 Demo＋学生个人项目”、16课学生材料、L3检索和L4精读修订，以及相应阅读输入、项目说明和下载包。快照共204个文件、96个HTML页面、6个学生下载ZIP。教师教案、判断答案、逐页母稿、PPT和原始评审日志不进入学生网站；课程源仓库另行维护这些源材料。L4候选PPT仍在本地 `.work/`，未进入正式交付。

发布前12项课程一致性检查、241份Markdown链接、44项Harness回归、17项网站测试、严格构建及96页链接／锚点／发布边界检查通过，6个ZIP完整性检查通过。构建HTML保留主题模板空白，以逐字节指纹核对，不为消除生成文件的空白提示改写输出。

[GitHub Actions发布任务](https://github.com/jinyh/ai4research/actions/runs/39446561574)成功。线上115项文件（全部96个HTML、6个ZIP、10个SVG、搜索索引及两份站点地图）与验收快照逐字节一致，L4教师答案和教案路径均返回404。原始清单与核验记录保存在本机 `.work/publish-20261020/`。教师内容确认、真实助教试做和教室投影仍待完成，网站发布状态单独登记。

## 上一次部署（2026-10-14）

本轮按用户明确授权更新课程修订后的学生网站。课程源提交为 `d64c2d5c019ad4abef2f26089ecd4c9ad43a7836`（分支 `codex/ai-research-revision`）；学生网站静态快照为 `13fb1e7c8b420123e4d596102730219c4c6d3427`（分支 `codex/student-site`）；部署指针提交为 `d944e467e72d4cc0fab09ef7fbd815fe77b5e275`（`main`）。

快照共 197 个文件、93 个 HTML 页面和 6 个学生下载 ZIP，含第 9 课 MI IOI 学生实验包；教师教案、判断答案、逐页母稿、PPT 与内部复核材料未进入快照。17 项学生网站测试、严格构建、站点链接/锚点/发布边界检查、12 项课程一致性检查和 MI 包内 4 项测试通过；6 个 ZIP 均通过完整性检查。

[GitHub Actions 发布任务](https://github.com/jinyh/ai4research/actions/runs/38553647982)已成功。线上首页、L3 入口、L3 完整讲义、L9 入口、MI 下载包与搜索索引共 6 项均返回 HTTP 200，并与验收快照逐字节一致。教师内容复核、助教计时、授课电脑、教室投影及跨系统视觉检查仍单独待完成；网站上线不代表正式课件验收完成。

## 上一次部署（2026-10-12）

用户明确授权提交、推送和网站材料发布。课程源提交为 `148aedf998ac1a3e000a70cfbb3b8f7f10ba780d`；学生网站静态快照为 `cc78f488ed5c101605ad2e879ca9112064760593`，沿用 `codex/student-site` 历史，不合入完整备课提交链。部署工作流固定到本次快照。

本轮更新全部16个课堂入口、讲义、核心判断任务、项目与阅读要求、模板和搜索；课外总预算每课最多60分钟。发布包共186个文件、91个HTML页面，包含5个学生下载ZIP。教师判断依据、教案、逐页母稿、PPT、申报底稿和复核台账不进入网站快照。

发布前17项学生网站测试、严格构建、91页链接与锚点及发布边界检查、12项课程一致性检查通过。桌面与390像素窄屏显示已检查。快照逐项核对允许清单与课程源提交一致；不纳入无关参考研究笔记。

部署配置提交为 `48bd18e290d59a3a9f58907f961b14f89b73948f`。[GitHub Actions 发布任务](https://github.com/jinyh/ai4research/actions/runs/38258747493)已成功。线上62项文件与验收快照逐字节一致：16个课堂入口、16个共同任务、16份讲义、首页、模板、逐课路径、项目与阅读/提交要求、搜索索引、站点地图和5个下载ZIP。两处教师答案入口返回404。首次核验有一项TLS连接失败，只重查该项后匹配；记录保留首次失败与恢复结果。浏览器确认L3的新诊断任务和60分钟课外预算已生效。

教师内容复核、助教实际计时、授课电脑及教室投影仍待独立登记，不以网站上线替代。

## 上一次部署（2026-10-07）

本次按用户授权同步第 2 讲学生讲义、课堂材料包及对应搜索记录，内容源提交为 `d2ddcaeec4b0816861cd7601c61d9c4132e79fb1`。学生快照为 `0018165fb2d01d0ddf0868fb2cf97c5e67001c97`，延续 `codex/student-site` 历史；部署配置提交为 `e6873de3bdcb1703fc8782cc0454dcf7fe9b50ad`。

本地 14 项网站测试、严格构建、69 页文件/锚点/发布边界检查通过，并检查第 2 讲讲义和课堂包排版。与上次快照相比，仅第 2 讲讲义、课堂包、对应搜索记录及站点地图变化，其余文件与上次快照逐字节一致。

[GitHub Actions 发布任务](https://github.com/jinyh/ai4research/actions/runs/37588810262)已成功。线上首页、第 2 讲入口、完整讲义、课堂包、第 1/16 讲讲义、搜索索引、两份站点地图和材料 ZIP 共 10 项与验收快照逐字节一致；浏览器确认第 2 讲课堂包展示更新后的输入授权与处理环境说明。

## 上一次部署（2026-09-23）

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
