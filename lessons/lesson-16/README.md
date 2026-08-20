# 第 16 课内容入口（MOC）

> 学生最终分享、论证门与期末项目。本文件是第 16 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义（草稿） | 面向学生、可脱离课堂独立阅读：最终论证结构（问题→证据→判断→实验→结论可追溯链路收口）、期末项目提交清单（逐项对齐 assignments.md Checkpoint 4 之 10 项 + project-template 全工件）、学生最终分享陈述结构（备课规划五项必答）、课程总结与复盘（八阶段链路反思 / AI 使用边界 / 不能自动化的判断）、AI 使用记录与伦理说明完整性检查、贯穿案例动作链、论证门+期末项目提交清单（对齐 assignments.md Checkpoint 4 之 10 项）、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案（草稿） | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.3.0（20 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.0.1 | 10 个关键页的视觉、教学与验收契约 |
| [slides.pptx](./slides.pptx) | 正式课堂 PPT（20 页） | 封面只保留正式课名；P18 为独立知识点总结；逐页含 `[Sources]` speaker notes |

## 2026-08-20 课件修订

- 封面标题改为“第16讲 最终分享、论证门与项目提交”，并上移至两条横线之间。
- P18 重构为“本讲知识点总结”；总页数保持 20。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 14 课论文式写作：本课把第 14 课的论文式短文初版、结论追踪表、AI 使用披露收口为可追溯论证链。
- 承接第 15 课同行评审预检：本课把第 15 课的同行评审表、回应记录、修改清单落实为采纳/拒绝/修改理由。
- 承接第 13 课验证门材料：本课把第 13 课的 evaluation-report（评价+失败审计+人工审核+证据充分性）收口为最终 Agent Workflow（运行/权限/评价/失败四项）。
- 承接第 1-13 课全部项目工件：本课做全链路核对，确认工件状态追踪表与四次门检查结果一致。
- 全课收口：本课是全课的最后一课，呼应第 1 课八阶段研究链路与"研究责任仍由人承担"。
- 论证门+期末项目提交指向当前个人项目版本（链接/tag/压缩包），不重复制作汇报文档。字段对齐 [project-template.md](../../course/project-template.md) 全工件。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)（"表达、伦理与复盘"维度，20%；四维度合计 100%）、[assignments.md](../../course/assignments.md)（Checkpoint 4 论证门条件——权威来源） |
| handout（可追溯链路 / stable 降级） | [AGENTS.md](../../AGENTS.md) 证据标准、[project-template.md](../../course/project-template.md) §8.4 证据充分性 |
| handout（最终工作流四项） | [project-template.md](../../course/project-template.md) §6 Agent Workflow |
| handout（伦理与 AI 披露） | [project-template.md](../../course/project-template.md) §10、[assessment.md](../../course/assessment.md) 学术规范红线 |
| handout（展示必答五问） | [备课规划.md](../备课规划.md) 第 16 课"展示必须回答"段 |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 16 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 16 课 → 课后提交论证门材料与期末项目合并包
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 备课规划 第 16 课目标段；八阶段定位阶段八"回写与表达成案+全链路收口"，承接第 14-15 课，全课收口呼应第 1 课八阶段链路与研究责任） |
| 2. 内容门 | ✅ 通过（三件套已对齐口径；讲义为内容源；关键结论绑定可核验来源——Alley 2013 / Peyton Jones 讲义 / Tao ICM 2026 / Booth et al. / Smith 1990 / assignments.md 门条件 / AGENTS.md 证据标准；AI 输出仅作线索；学术规范红线对齐 assessment.md；不残留旧口径——证据三角硬门槛/每周作业/默认小组提交均已清除；gate2 保守审校已去 4 处"不是 X，是 Y"对仗（P08 屏显+备注、P14、P19，保留 P04/P05/P07/P16 四处张力）与"本课是…最终验收""本课只确认"重复） |
| 3. 90 分钟教学门 | ✅ 通过（按备课规划第 16 课"90 分钟建议"表权威 6 段 re-fit：P12+P13 归入 12-25 讲授段，P14 单页承接 25-45 陈述+抽查停留段，P15 单页承接 45-65 个人补全停留段，P16-P18 归入 65-78 复盘+同伴互查段；每页建议时间按段时长重排，段内均分；页量预算对照 6 段无超页段，六段全部保留；陈述超时用分会场/海报/短视频） |
| 4. 逐页映射门 | ✅ 通过（20 页逐页映射表与 90 分钟节奏表页码列同步：P01-P07（seg1）/P08-P13（seg2）/P14（seg3）/P15（seg4）/P16-P18（seg5）/P19-P20（seg6）；每页标 handout 小节） |
| 5. PPT 制作 | ✅ 通过（按 `slides.md` v0.2.1 完成 20 页正式课堂 PPT；以第 7 课正式 PPT 为模板基线，保留 master/layout、交大校徽、红标题带、主题字体、页脚与页码；10 个关键页按 `keystone-design-spec.md` 实现；20/20 页 speaker notes 均含闭合 `[Sources]`） |
| 6. 三重检查 | ✅ 通过（技术：模板保真 issueCount=0、overflow=0、空 placeholder=0、20/20 sources、LibreOffice 磁盘重开与 20 页重渲染通过；教学：20 页映射、六段 90 分钟节奏、P14/P15 两个 20 分钟停留、Checkpoint 4 十项、最终分享五问、抽查/评审/AI/伦理/工件/复盘一致；视觉：20/20 页逐页检查，10/10 关键页复核，未见阻断性 overlap、clipping、title wrapping 或密度问题；证据见 `.work/ppt/lesson-16/run-20260807/qa-ledger.txt`） |
| 7. 里程碑归档 | ✅ 无需单独归档（本轮为首个正式课堂 PPT，无被替代正式稿；渲染、解包、layout 与 QA 证据保留在 `.work/ppt/lesson-16/run-20260807/`） |

## 待复核项

- **论证门+期末项目条件对齐**：handout §八·2 的 10 项门条件与 [assignments.md](../../course/assignments.md) Checkpoint 4 逐项对齐，已核对一致：
  1. 论文式短文完整（问题/方法/实验/结果/局限） ↔ 条件之一
  2. 结果表/图追溯到证据项、实验 ID 或运行记录 ↔ 条件之二
  3. 讨论威胁有效性或等价威胁分析 ↔ 条件之三
  4. 已处理第 15 课同行评审意见，记录采纳/拒绝/修改理由 ↔ 条件之四
  5. 每个关键结论绑定一项直接证据 + 一个上游研究判断 ↔ 条件之五
  6. stable 结论有两项独立证据；不满足已降级并说明缺口 ↔ 条件之六
  7. 最终 Agent Workflow 有运行/权限/评价/失败四项 ↔ 条件之七
  8. 科研伦理、数据许可、贡献说明、AI 披露完整 ↔ 条件之八
  9. 工件状态追踪表与实际门检查结果一致 ↔ 条件之九
  10. 完成个人展示、复现抽查和课程复盘 ↔ 条件之十

  提交方式（链接/tag/压缩包）、教师抽查（一次复现/一个引用/一条 trace）、未通过处理（局部问题可修订，学术规范红线不适用修订机制）和评分维度（"表达、伦理与复盘"20%；四维度合计 100%）均对齐。10 项与 assignments.md Checkpoint 4 逐项一致性已复核通过。

- **评分合计 100% 对齐**：四维度已核对——文献与问题定位 25% + 实验设计与可复现性 30% + 原型与 Agent Workflow 实践 25% + 表达、伦理与复盘 20% = 100%。本课对应"表达、伦理与复盘"20%，同时前三门（问题门/判断门/验证门）的过程证据在此汇总。评分比例与 assessment.md "总体结构"表一致。

- 演示用第 14 课 `report.md` 收口版样例（论文式短文 + 可追溯证据链 + 复盘）需在授课前准备可投屏版本；
- 演示用第 13 课 evaluation-report.md 收口版样例需在授课前准备可投屏版本；
- 演示用"分段汇报冒充论证"反例与"结果无实验 ID"反例需在授课前准备；
- Alley 2013 陈述结构投屏版（Chapter 3 Structure + Critical Errors 3/4/7）需在授课前准备；
- 陈述时间控制表需按实际选课人数在授课前确认（21 人以内 3 分钟/人；超过 21 人用分会场/海报/短视频）；
- 复现抽查准备：教师需在授课前选定 2-3 个学生的实验 ID、引用或工作流 trace；
- 与第 1 课的呼应点：本课 §五·3"不能自动化的判断"九条是否在 slides P18 进一步强化为第 1 课 §一·2 的最终验收；
- 贯穿案例是否需要在第 10-16 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡 / 第 9 课实验规格与 baseline / 第 12 课工作流原型 / 第 13 课评价 / 第 14 课短文 / 第 15 课评审同一案例族）；
- 论证门材料文件结构是否需要根据本课"课程复盘"段更新 [project-template.md](../../course/project-template.md) §12 复盘（当前 §12 已含复盘八问，但未含"AI 使用边界四部分"和"不能自动化的判断九条"独立段——可能需要扩展）；
- handout §七贯穿案例的虚构数值（0.18±0.03 vs 0.31±0.04）已在讲义和 slides 明确标注为"虚构教学示例，仅用于课堂演示动作链，不预设真实数值"，待教师在授课前确认是否替换为真实可投屏数值或保留虚构标注。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
