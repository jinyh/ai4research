# 第 11 课内容入口（MOC）

> 实验自动化与 AutoResearch 循环。本文件是第 11 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生正式讲义 v0.2.0 | 面向学生、可脱离课堂独立阅读：实验自动化循环五步、四约束（固定指标/预算/停止条件/回退）、AutoResearch 元模式与 AI Scientist 案例分析（八维框架，不外推为通用自主科研）、失败实验记录与不选择性删除、贯穿案例改写为受限循环、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.3.0 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘；正式 PPT 已完成 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.3.0（20 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界；正式 PPT 已按此版本验收 |
| [slides.pptx](./slides.pptx) | 现行·正式课堂 PPT（20 页） | 封面只保留正式课名；退出卡前含独立知识点总结；逐页 speaker notes 含 `[Sources]` |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.0.2 | 13 个关键页的视觉契约、模板例外与正式验收记录 |

## 2026-08-20 课件修订

- 封面标题改为“第11讲 实验自动化、AutoResearch 循环与结果追踪”，并上移至两条横线之间。
- 新增 P19“本讲知识点总结”，原退出卡顺延为 P20；总页数 19→20。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 10 课受限 Agent 执行：本课把"跑通一次"扩展为可重复运行的受限循环，把任务契约草稿升级为四要素（输入/输出/成功标准/不适用范围）。
- 承接第 9 课实验规格与可复现说明：本课把第 9 课的停止条件扩展为循环的预算与三类停止触发器，把可复现字段保留在循环中以防指标漂移。
- 为第 12 课个人工作流设计铺垫：本课的循环骨架（任务契约/Context/工具权限/状态/执行循环/工件追踪/Evals/失败恢复）是第 12 课个人工作流设计的直接输入；第 12 课把这些要素重新组合而非拆解别人的系统。
- AutoResearch / AI Scientist 在本课只作**分析对象**，不作结论外推的依据——不表述为"AI 已能自主科研""自动评审替代同行""端到端适用于所有学科""失败可被自动删除"。
- 本课无正式提交（验证门在第 13 课后）。本课产出（受限循环说明、失败迭代记录、八维拆解表）持续回写同一项目，验证门统一检查实验记录与失败保留。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)、[assignments.md](../../course/assignments.md)（验证门 Checkpoint 3 在第 13 课后，本课无正式提交） |
| handout（循环骨架） | [starter-template.md](../../course/starter-template.md)、[project-template.md](../../course/project-template.md) |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 11 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 11 课 → 课后跑通受限循环骨架与至少一次失败迭代记录
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 `备课规划.md` 第 11 课目标段；八阶段定位阶段七"原型验证（实验追踪）"；承接第 10 课受限 Agent，为第 12 课个人工作流设计铺垫） |
| 2. 内容门 | ✅ 复核通过（三件套已统一为受限循环五步、四约束、失败保留和八维分析；AutoResearch / AI Scientist 只作分析对象；AutoResearch 固定为 commit `228791f`；AI Scientist workshop 证据已按 Nature 正文精确改写；课程教学参数与日志均明确标为示意；不新增正式提交） |
| 3. 90 分钟教学门 | ✅ 复核通过（`备课规划.md` 第 11 课权威六段：0-18/18-35/35-55/55-75/75-85/85-90；P02 从 2:15 开始 1 分钟工件缺口标记，55 分钟开始持续实践；最小产出=受限循环说明（四约束+五步骨架+审核点）+失败迭代记录（七字段）+八维拆解表（≥4 维）；无环境时使用纸面/Markdown 备用路径） |
| 4. 逐页映射门 | ✅ 复核通过（19 页均映射 handout 小节；P09/P10/P17 的教学反例/样例边界已同步；P12-P15 的分析对象与外推边界一致；P19 明确衔接第 12 课个人工作流设计） |
| 5. PPT 制作 | ✅ 通过（19 页；以 `lesson-07/slides.pptx` 为直接模板基线，使用 `@oai/artifact-tool` 模板跟随流程；保留 1 个 master、4 个 layout、交大品牌、页眉页脚与页码；13 个关键页先完成四字段设计契约；19/19 页 speaker notes 含 `[Sources]`） |
| 6. 三重检查 | ✅ 通过（技术：19 页、19 组 notes、`[Sources]` 19/19、空结构 placeholder 0、默认提示文本 0、越界对象 0、模板忠实度 0 问题；教学：五步/四约束/失败保留/分析对象边界/第 12 课衔接闭环，19 页均映射 handout；视觉：Artifact Tool 逐页渲染与关键页全尺寸检查，无可见 overlap、clipping、wrapping 失败；最终磁盘文件经 LibreOffice 重开并导出 19 页 PDF，再逐页复渲染检查） |
| 7. 里程碑归档 | ✅ 完成判断（本课沿用第 7 课已确立的交大正式视觉语言，没有形成需单独保留的新模板里程碑；不向 `archive/` 复制重复 PPTX。构建脚本、frame map、双重渲染和 QA 台账保留在 `.work/ppt/lesson-11/2026-08-07-formal/`） |

## 修订轮登记（2026-08-12，handout v0.2.0）

按 `prepare-course-lesson` skill"修订已有课次"条款登记，原门控记录保留不动：

| 门 | 状态 |
| --- | --- |
| 课次目标门 | ✅ 复核通过（课次目标不变） |
| 内容门 | ✅ 重走：handout 新增 §四·5"同谱系对照案例簇"边界小节与 §十延伸阅读第 5 条（逐字同步 reading-list v2.2.0 第 11 课新条目）；新增内容仅分析对象、预印本已标注、明确不进学生安装清单、不外推；既有案例与来源口径未变 |
| 90 分钟教学门 | ⬇️ 降级复核：学习目标与权威 6 段时间结构不变；新增小节为 §四 的边界延伸与课后延伸阅读，不占用课堂时间段，已对照既有节奏表核对 |
| 逐页映射门 | 未变更（未动 `slides.md`，原记录有效） |
| PPT 制作 / 三重检查 | 未变更，原记录有效（未重建 `slides.pptx`） |
| 推迟项 | 无新增推迟素材；Prime Agent 案例簇的授课前复核清单（服务依赖、国内可用性、两篇预印本后续版本）登记在 `references/notes/pi-and-prime-agent.md` §10 |

## 待复核项

- syllabus 表格与 `备课规划.md` 均把 AutoResearch / AI Scientist 分析放在第 11 课；syllabus v1.1.0 变更记录中的“第 12 课增加”属于历史摘要差异，本课不据此改动 `course/` 权威源；
- AutoResearch 已固定为 commit `228791f`；若授课前更换版本，必须重新核对 README、`program.md`、评价口径与日志字段；
- PPT 已内置八维拆解表、指标篡改教学反例、七字段失败记录样例和第 12 课衔接；若学生需要现场编辑，仍需另备可填写 Markdown 模板；
- 贯穿案例是否需要在第 9-11 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡 / 第 7 课实验规格草图 / 第 9 课判断门 / 第 10 课受限执行同一案例族）；
- 不外推清单（handout §四·4）是否需要在验证门（第 13 课）材料中再次出现作为自查项；
- 授课机上的 Microsoft PowerPoint 和实际投影环境仍需在课前抽查字体、16:9 比例和静态页面兼容性。`slides_test.py` 因本机缺少 `numpy` 未直接运行，已用 Artifact Tool layout 检查、模板忠实度检查、ZIP/XML 结构审计和 LibreOffice 重开复渲染替代覆盖。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
