# 智能科研方法课程备课项目

上海交通大学研究生课程"智能科研方法"（AI for Research: Methods and Practice）的备课仓库，2 学分、32 学时、专业选修课。课程已批准。本仓库由 Claude Code、Codex、OpenCode 三端协作维护。

## 快速入口

- **项目规则**：[`AGENTS.md`](./AGENTS.md)（`CLAUDE.md` 单向软链接到它）。所有协作者先读此文件。
- **课程大纲权威源**：[`course/syllabus.md`](./course/syllabus.md)
- **逐课备课工作区**：[`lessons/README.md`](./lessons/README.md)（含材料状态表与制作顺序）
- **备课规划与教师复核**：[`lessons/备课规划.md`](./lessons/备课规划.md)、[`lessons/teacher-review-ledger.md`](./lessons/teacher-review-ledger.md)
- **当前综合修订**：[`docs/personal-project-revision-20261020.md`](./docs/personal-project-revision-20261020.md)（MI教师Demo、学生个人项目与备课Harness；各批次完成边界）
- **上一轮全课修订**：[`docs/ai-research-revision-20261014.md`](./docs/ai-research-revision-20261014.md)（2026-10-14基线与历史状态）
- **旧版课程 2.0 计划**：[`docs/course-2.0-plan.md`](./docs/course-2.0-plan.md)（历史批次记录）

## 目录职责

| 目录 | 职责 | Git 策略 |
| --- | --- | --- |
| `course/` | 课程大纲、考核、阶段交付、申请表底稿、学生模板等跨课次权威源 | 跟踪 |
| `lessons/` | 按课次组织现行讲义、教案、逐页内容母稿、当前 PPT 和教学资产 | 跟踪 |
| `deliverables/` | 已通过内容、教学、技术和视觉检查的正式发布物 | 跟踪里程碑版本 |
| `references/notes/` | 参考资料分析、选目和核验记录 | 跟踪 |
| `references/library/` | 论文、书籍、外部 PPT、模板等原始资料 | 默认不跟踪 |
| `archive/` | 试讲、被替代文稿、有决策价值的 PPT 试制里程碑 | 仅本机保留，不随仓库分发 |
| `docs/` | 现行协作规范、工具说明、执行计划与审阅协议 | 跟踪 |
| `scripts/` | 只读验证脚本 | 跟踪 |
| `web/` | 课程门户网站（MkDocs Material），内容以软链接从 `course/` 与 `lessons/` 引入 | 跟踪配置与手写页面；忽略 `.venv/`、`_build/` |
| `.work/` | 渲染、解包、layout、QA、临时脚本环境和缓存 | 不跟踪 |
| `.local/` | 申请原件、外部数据链接、凭据相关本机配置 | 不跟踪 |

## 材料状态边界

- **现行内容**：当前用于对齐课程事实、规则和课堂叙事的讲义、教案与逐页内容母稿。每课只有一套。
- **正式交付**：`deliverables/<term>/` 下已通过检查的 PPTX/PDF。
- **试讲/历史**：全部试讲版本及内容源保存在 `archive/trial-lecture/`，只用于开课评审和历史追踪，不得作为正式讲义或课堂 PPT；可重建技术产物进入 `.work/`。
- **试制里程碑**：`archive/ppt-experiments/`，保留确立视觉语言或记录重要取舍的少量 PPT 试制稿。
- **本机归档**：`archive/` 不纳入 Git；新克隆的仓库不含历史材料，现行文档只标记其本机路径。
- **临时产物**：`.work/`，所有渲染图、解包 XML、layout、检查日志和缓存。

## 当前状态

- 课程材料与既有学生网站分别以 `course-baseline-2026-10-14` 和 `student-site-baseline-2026-10-14` 冻结，恢复说明见[冻结记录](docs/course-freeze-20261014.md)。
- 16 课修订源已推送到 `codex/ai-research-revision`；学生网站已于 2026-10-21 同步 L01–L04 本轮学生材料。L4新版PPT已于2026-10-21经教师确认提升为[现行课堂课件](lessons/lesson-04/lesson-04.pptx)；L01–L03同日经用户授权同步为现行版并进入[2026秋季交付目录](deliverables/2026-fall/README.md)，独立评审与现场待核项保留。其余课修订预览仍在本地维护。
- 课程一致性、内部链接、Harness回归、网站测试、严格构建和发布边界检查通过；GitHub Pages部署成功，线上117项文件与本轮快照逐字节一致。GPT-2实际运行与L4部分PowerPoint实查已完成；L4教师确认已登记；其他课教师复核、博士助教试做、图表数据编辑、教室投影和跨系统网站验收仍待完成。逐项状态见[综合修订记录](docs/personal-project-revision-20261020.md)，发布详情见[网站部署记录](web/README.md)。
- 正式提交仍只有四次：第 6、9、13、16 课后的研究门材料。

详见 [lessons/README.md](./lessons/README.md)。
