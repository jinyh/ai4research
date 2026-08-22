# 第 10 课内容入口（MOC）

> AI 辅助编码、调试与受限 Agent 执行。本文件是第 10 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.2.1 | 面向学生、可脱离课堂独立阅读：从模糊 prompt 到任务契约五字段（Context / Permission / Non-goal / 人工审核点 / 失败恢复）、权限分层与人工审核点、Agent 代码人工核验（diff 审查 / 测试先行 / 不外包判断）、修复根因 / 绕过失败 / 污染实验三区分、SWE-bench 视角、贯穿案例（承接第 9 课实验规格的一步）、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.4.0 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.4.0（17 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.1.0 | 10 个风险触发关键页的页面任务、视觉锚点、叙事关系、模板映射与验收条件 |
| [slides.pptx](./slides.pptx) | 正式·课堂 PPT（17 页） | 封面只保留正式课名；退出卡前含独立知识点总结；每页含 `[Sources]` speaker notes |
| [assets/agent-task-example/](./assets/agent-task-example/) | 现行·课次本地真实教学工件 | 可核验的 before/after、`generate.diff`、`unittest`、测试输出与越权失败日志；供 P12 演示和无执行环境备用路径使用 |

## 2026-08-20 课件修订

- 封面标题改为“第10讲 AI 辅助编码、调试与受限 Agent 执行”，并上移至两条横线之间。
- 新增 P16“本讲知识点总结”，原退出卡顺延为 P17；总页数 16→17。

## 文件关系

### 学生入口呈现增强轮（2026-08-22）

- 门 1 与内容门已复核通过：只补任务契约与失败记录的具体链接，课堂闭环、案例事实和来源边界不变。
- 90 分钟教学门、逐页映射门、PPT 制作与三重检查不受影响，沿用下方既有通过记录；本轮不修改 `teaching-plan.md`、`slides.md` 或 `slides.pptx`。
- 待延后项：无；本机 Python、预置 diff 与测试输出的课堂可用性仍由助教按审阅协议复核。

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 9 课判断门：本课把第 9 课实验规格中"哪些步骤拟用 Agent、哪些步骤必须人工"标注改写为任务契约五字段，作为受限 Agent 执行的直接输入。
- 为第 11 课铺垫：本课的受限"一次执行"是第 11 课"自动化循环"（Edit → Evaluate → Keep/Discard → Repeat）的前提——没有边界的一次执行不能被安全地重复，更不能被自动化。
- 本课非正式提交门（[assignments.md](../../course/assignments.md) 第 10 课行只有"在受限权限下完成一次 Agent 辅助代码或研究任务迭代"，无正式提交）。产出回写个人项目，作为第 13 课验证门材料的过程证据。
- 任务契约写入 `agent-tasks/`（本课新建目录），代码 diff 与失败日志写入 `experiments/*/agent-traces/`，AI 使用记录沿用第 1 课最小字段。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)（学术规范红线）、[assignments.md](../../course/assignments.md)（第 10 课非正式提交门） |
| handout（模板） | [project-template.md](../../course/project-template.md)（任务契约写入 `agent-tasks/`） |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 10 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 10 课 → 课后完善原型（不正式提交）
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 `备课规划.md` 第 10 课目标段；八阶段定位阶段七"原型验证"中的受限 Agent 执行；承接第 9 课判断门，向第 11 课自动化循环输出） |
| 2. 内容门 | ✅ 保守审校通过（三件套已对齐口径；讲义为内容源；关键结论绑定可核验来源——Russell & Norvig 2020 Ch 2 / Yao et al. ReAct ICLR 2023 / Amershi et al. CHI 2019 / Jimenez et al. SWE-bench ICLR 2024 / assignments.md 第 10 课非正式提交门 / assessment.md 学术规范红线；AI 输出仅作线索；第二轮去 AI 痕迹完成：去 3 处 meta 自白、blockquote 保留 4 处张力其余转正面、视觉结构否定式转正面；handout 正文/案例/证据未动） |
| 3. 90 分钟教学门 | ✅ 通过（按 `备课规划.md` 第 10 课权威 5 段 re-fit 页量预算 20→16 页，4 处合并；per-page 时间在 0-90 段内均分；40-60 分钟持续个人实践；课堂最低闭环=选一个受限步骤 + 任务契约五字段/权限 + 检查真实或预置 diff + 一项验证证据与一次失败/越权处理 + 启动 AI 披露；无执行环境时改审课次本地真实工件，产出不降级） |
| 4. 逐页映射门 | ✅ 通过（16 页映射表已复核，每页标 handout 小节；六段主题块保留，合并不跨块；90 分钟节奏表页码列与 teaching-plan §五 PPT 执行索引已同步） |
| 5. PPT 制作 | ✅ 通过（按 `slides.md` v0.3.0 完成 16 页正式课堂 PPT；以第 7 课正式 PPT 为模板基线，保留 master/layout、交大校徽、红标题带、主题字体、页脚与页码；10 个关键页按 `keystone-design-spec.md` 实现；16/16 页 speaker notes 均含闭合 `[Sources]`） |
| 6. 三重检查 | ✅ 通过（技术：模板保真 issueCount=0、overflow=0、空 placeholder=0、16/16 sources、LibreOffice 磁盘重开与 16 页重渲染通过；教学：16 页映射、90 分钟五段、40 分钟首次动手、最小产出闭环一致；视觉：16/16 页逐页检查，10/10 关键页复核，未见阻断性 overlap/clipping/wrapping/密度问题；证据见 `.work/ppt/lesson-10/run-20260807/qa-ledger.txt`） |
| 7. 里程碑归档 | ✅ 无需单独归档（本轮为首个正式课堂 PPT，无被替代正式稿；渲染、解包、layout 与 QA 证据保留在 `.work/ppt/lesson-10/run-20260807/`） |

## 待复核项

- **承接第 9 课**：第 9 课 handout §三·5 已要求实验规格中标出"哪些步骤拟用 Agent、哪些步骤必须人工"，本课 handout §五 第一步直接使用该标注。待教师在正式授课前确认学生第 9 课产出中是否已填写该标注；未填写者需在课堂内补标。
- **本课非正式提交门**：与 [assignments.md](../../course/assignments.md) 第 10 课行一致（"在受限权限下完成一次 Agent 辅助代码或研究任务迭代 | —"）。产出回写个人项目，作为第 13 课验证门材料的过程证据。
- **学术规范红线对齐**：handout §四·2 与 §六、slides P09（修复根因/绕过失败/污染实验）与 P16（失败与越权复盘）、teaching-plan §一与 §六均对齐 [assessment.md](../../course/assessment.md) 学术规范红线——绕过失败与污染实验列为红线，删除失败日志等同伪造记录。
- **来源核验**：四项正式书目与课堂案例的 URL/DOI 已按 [reading-list.md](../../course/reading-list.md) 第 10 课核对：
  1. Russell & Norvig 2020 Ch 2（核心，约 30 分钟）——Pearson 出版社页面
  2. Yao et al. ReAct ICLR 2023（任选，约 25 分钟）——ICLR 虚拟会议页面
  3. Amershi et al. CHI 2019（任选，约 20 分钟）——DOI 10.1145/3290605.3300233
  4. Jimenez et al. SWE-bench ICLR 2024（基准案例）——项目页面 swebench.com
- `备课规划.md` 第 10 课段已补权威 5 段逐时间表（0-20/20-40/40-60/60-78/78-90），slides.md v0.2.0 与 teaching-plan 已据此 re-fit；
- 演示用第 9 课贯穿案例实验规格（"拟用 Agent"步骤标注）需在授课前准备可投屏版本；
- 演示用任务契约样例（`generate_summary()` 任务五字段）需在授课前准备可投屏版本；
- 演示用真实 diff、`unittest` 输出与越权失败日志已放入 `assets/agent-task-example/`；授课前只需确认投屏路径与本机 Python 可用，无执行环境时直接审查这些预置工件；
- 16 页密度已按权威 5 段 re-fit（原 20 页→16 页，4 处合并：旧 P02+P03、旧 P07+P08、旧 P10+P11、旧 P15+P16），并通过逐页渲染、模板保真、溢出、空 placeholder 与 LibreOffice 重开检查；真实课堂桌面推演后的节奏微调仍由教师决定；
- 与第 11 课的衔接点：本课"一次执行"如何扩展为第 11 课"Edit → Evaluate → Keep/Discard → Repeat"循环，任务契约五字段中哪些字段需要为循环增加"预算"与"停止条件"字段；
- 贯穿案例是否需要在第 9-10 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡 / 第 7 课实验规格草图 / 第 9 课判断门材料同一案例族）；
- [project-template.md](../../course/project-template.md) v1.1.0 已纳入 `agent-tasks/` 与 `experiments/*/agent-traces/`，本课写入路径已对齐。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
