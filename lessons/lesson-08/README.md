# 第 8 课内容入口（MOC）

> 学生研究方案分享与设计诊所。本文件是第 8 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.2.0 | 面向学生、可脱离课堂独立阅读：3 分钟陈述五段结构、同伴互查“四个诊断维度（问题重要性/证据充分性/可检验性/课程周期可行性）+一个行动性检查（下一步实验是否能改变研究判断）”、边界横切字段、同伴互查三问、设计诊所流程、反馈记录表与采纳决策（六字段）、与第 9 课判断门衔接、AI 只作反馈线索、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.4.0 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.4.0（15 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [slides.pptx](./slides.pptx) | 现行·正式课堂 PPT（15 页） | 封面与收束修订轮已通过技术、教学与视觉检查 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.1.0 | 关键页任务、主视觉锚点、叙事关系与最小成立内容；记录模板例外和验收结果 |

## 封面与收束修订轮（2026-08-20）

- 90 分钟总时长不变；P14 总结、P15 退出/预告各 2.5 分钟。
- 15/15 notes 含来源块，布局 0 越界，Office 校验与 LibreOffice 重开通过；封面、P14-P15 已做视觉检查。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 7 课机制假设与实验规格：本课把第 7 课的机制假设列表、研究判断记录初版和实验规格草图压缩为 3 分钟陈述，并暴露给同伴按 rubric 质询。
- 承接第 6 课问题门产出：3 分钟陈述第 1 段"研究问题"以第 6 课 `problem-definition.md` 为内容源；陈述起点是问题门收敛后的可证伪命题，不是重新选题。
- 为第 9 课判断门铺垫：本课产出的"同伴反馈处理记录"和"至少 2 条研究判断（采纳决策）"是判断门材料之一（[assignments.md](../../course/assignments.md) Checkpoint 2 第 4、6 项）；同伴反馈口径为“问题重要性、证据充分性、可检验性、课程周期可行性”四个诊断维度，加上“下一步实验是否能改变研究判断”行动性检查；边界作为陈述与研究判断的横切字段。
- 强调：本课是形成性活动，不新增正式提交、不计周作业分（[assignments.md](../../course/assignments.md) "第 8 课"段；v2.1.0 变更记录）。同伴反馈只作输入，采纳决策由作者本人作出并记录理由。
- 采纳决策表写入个人项目 `hypothesis-and-design.md`（或沿用 `starter-template.md` 对应小节），合并到研究判断记录，第 9 课随判断门统一检查。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)、[assignments.md](../../course/assignments.md)（"第 8 课"段、Checkpoint 2 判断门条件——权威来源） |
| handout（rubric 对齐判断门） | [assignments.md](../../course/assignments.md) Checkpoint 2 |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 8 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 8 课（Booth et al. 选段，约 20 分钟）
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 `备课规划.md` 第 8 课目标段；八阶段定位"阶段三+六+七草案的跨同学外部校准"，承接第 7 课机制假设与实验规格，为第 9 课判断门铺垫；形成性活动不正式提交） |
| 2. 内容门 | ✅ 保守审校通过（2026-08-07 复核：三件套已统一为“四个诊断维度 + 一个行动性检查”，同时对齐 syllabus 的高层风险口径和 assignments 的 5 项反馈细则；边界保留为横切字段；讲义为内容源；关键结论绑定可核验来源；AI 输出仅作线索；形成性不提交口径不动） |
| 3. 90 分钟教学门 | ✅ 通过（2026-08-07 复核：节奏表仍对齐 `备课规划.md` v2.1.0 权威 8 段；第一次学生动手 40 分钟；最小产出=分享页+反馈记录表+采纳决策表 2 条（含 1 采纳 1 拒绝/暂缓）+判断门预检缺口清单+一条 AI 使用记录；四维度修正未改变时间、活动、最小产出或备用路径） |
| 4. 逐页映射门 | ✅ 通过（2026-08-07 复核：14 页映射表仍逐页指向 handout 小节；P02/P03/P05-P07/P11/P14 的四维度、三问、验收和贯穿案例已同步；P10 演示展开 P04 压缩的贯穿案例五段） |
| 5. PPT 制作 | ✅ 通过（14 页；以 `lesson-07/slides.pptx` 为直接模板基线，使用 `@oai/artifact-tool` 的模板跟随流程生成；保留原 master/layout、交大品牌、页眉页脚与版式语言；9 个关键页先完成设计契约；每页 speaker notes 均含 `[Sources]`） |
| 6. 三重检查与归档 | ✅ 通过（技术：14 页、14 组 notes、`[Sources]` 覆盖 14/14、空结构 placeholder 0、默认提示文本 0、越界对象 0、master 1、layout 4；教学：14 页逐页映射 handout，90 分钟节奏与最小产出闭环；视觉：Artifact Tool 逐页渲染与关键页复查，模板忠实度 0 问题；磁盘重开：LibreOffice 重新打开并导出 14 页 PDF，再逐页渲染复核，无可见 overlap/clipping/wrapping 失败。正式文件 SHA-256：`780aae79256266a506c8d3f7d92abb8360753252e0de392659a9787625539b05`） |

## 待复核项

- PPT 已内置第 7 课输出到五段陈述、同伴三问到三类决策、反馈记录字段和判断门预检表的教学示意；若课堂需要学生现场编辑，仍需在授课前另备可填写模板；
- 固定同伴组分组名单与轮次表需在授课前确认；
- 互查节奏是否超时：4 人组 20 分钟一轮，21-40 人班级按组数并行，需在授课前确认两轮或单轮；
- 贯穿案例是否需要在第 7-9 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡同一案例族）；
- `hypothesis-and-design.md` 字段模板是否需要根据本课新增"采纳决策表"段更新 [starter-template.md](../../course/starter-template.md)；
- 已用 LibreOffice 完成最终磁盘重开与重新渲染；授课机上的 Microsoft PowerPoint 和实际投影环境仍需在课前做一次现场字体、比例和动画兼容性抽查。`slides_test.py` 因本机缺少 `numpy` 未直接运行，已用 Artifact Tool layout 检查、模板忠实度检查、ZIP/XML 结构审计和 LibreOffice 重开替代覆盖。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
