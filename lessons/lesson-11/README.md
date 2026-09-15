# 第 11 课内容入口（MOC）

> 实验自动化与 AutoResearch 循环。本文件是第 11 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。


## 整体复审修订轮（2026-09-15，当前状态）

- 目标与课程结构：未变；正式提交仍为第 6、9、13、16 课。
- 内容：现行 Markdown 已完成本轮修订；板书、诊断答案与串词在教师教案；待教师复核本轮实质变化。
- 教学门：原时段与总时长不变，本轮复核；诊断嵌入既有开场，课堂包不替代本人项目的门条件。
- 逐页映射：标题、内容与互动按新母稿核对；页数保持不变。
- PPT：文件未变更，上轮技术与视觉记录仍描述旧文件；它们不证明本轮新内容已同步。旧 PPT 不应直接作为本轮修订后的讲授稿。
- 推迟项：教师内容复核后同步 PPT，再做文件级、视觉和实际投影检查；第 16 课继续保留内容门阻塞。
- 执行记录：[本轮修订与验证](../../docs/course-integrated-revision-20260915.md)；助教分工见[演示准备清单](../../docs/lesson-demo-assignment-20260915.md)。

下方先前通过记录均保留为历史。当前内容与呈现的状态以上述修订轮为准。


## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生正式讲义 v0.4.0 | 聚焦固定指标、预算、停止与回退；区分冻结的批量执行队列与优化循环；使用人工基准评价限定条件遗漏率 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.5.0 | 整数时长的 90 分钟流程、分段实践与中点点评、三种 trace 演示与备用路径 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.6.0（20 页） | 逐页屏显文案、对象化视觉结构、讲述备注、互动、整数时长与来源边界 |
| [slides.pptx](./slides.pptx) | 现行·课堂 PPT（20 页） | 已按 v0.5.1 母稿完成定点修订；保留交大原生 Master/Layout、校徽、红标题带、主题字体和页码 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.1.0 | 14 个关键页的现行视觉契约；历史模板与制作记录保留 |

## 2026-08-20 课件修订

- 封面标题改为“第11讲 实验自动化、AutoResearch 循环与结果追踪”，并上移至两条横线之间。
- 新增 P19“本讲知识点总结”，原退出卡顺延为 P20；总页数 19→20。

## 文件关系

### 内容同步修订轮（2026-09-13）

| 门 | 本轮状态与证据 |
| --- | --- |
| 课次目标 | 复核通过；第 11 课定位、上下游输入输出和正式提交节点不变 |
| 内容门 | 复核通过；修正冻结队列与方法优化混淆、结果导向停止和恢复口径；同步讲义、教案、20 页母稿与关键页规格 |
| 90 分钟教学门 | 降级复核通过；原结构合计 90 分钟，个人实践 10 + 10 分钟，中间 5 分钟教师点评；最低产出与纸面/预置 trace 备用路径不变 |
| 逐页映射 | 20/20 页标题及屏显回写母稿；恢复每页讲述、学生动作、时间和来源 notes；完整八维表保留为课后查阅 |
| PPT 制作 | 20 页正式文件已替换；替换前 PowerPoint 打开文稿数为 0，lsof 无目标持有，未运行 Impress/soffice |
| 技术检查 | 正式文件包结构、布局与 Artifact Tool 重开通过（0 finding；19 个源文件已有的隐藏标题重叠 warning，逐页可见画面正常）；Master/Layout/Theme 归一化与源文件相同；20/20 页含教学 notes 和 Sources；教学文字 ≥18 pt；屏显无课堂分钟 |
| 教学检查 | P10 不含 Keep/Discard，明确评价不回流调参；P7/P9 不按结果好坏停或删；P11 保留不利结果与技术失败；P15-P17 明确执行类型及恢复冻结配置 |
| 视觉检查 | 最终正式路径重开渲染 20 页，与已全尺寸复核候选逐张像素相同；修正 P10 标签孤字换行、P16 红底红字序号、P18 互查问题换行；维持原对象化版式 |
| 原生应用/投影 | 本轮未做 Microsoft PowerPoint 原生验收或教室投影；上一轮通过不得代替本轮验证 |
| 里程碑与推迟项 | 本轮为同一视觉语言的内容修复，不新增归档里程碑；正式路径已复核指纹、解包及重开渲染；推迟项仅为课前 PowerPoint 原生与实际投影复检 |

- 本轮正式文件 SHA-256：`8b9d66a0de05967ea018b56f13adbe56e8150b3565e38fec6f4c2deddb364ce3`。
- 本轮修订：P10 改为配置冻结→队列运行→失败恢复→原始输出→独立评价；P6/P11 增加虚构工件身份；P7/P9/P11/P15-P17 消除同源语义矛盾。
- QA：`.work/ppt/lesson-11/2026-09-13-sync-fix/`；`gate-review.md`、`lesson-11-sync-fix-v4-validation.json`、`qa-final.json`、`formal-reopen.json`、`app-hold-check.md`、`formal-render/`。所有渲染与构建材料仅保留在 `.work/`。
- 旧记录订正：2026-09-12 虽宣称“120 份输出不被误写为优化循环”，实际 P10 含 Keep/Discard 分支；该教学结论撤回，历史文件指纹和当时原生打开记录保留。

### 对象化视觉提升轮（2026-09-12，历史；本轮发现语义缺陷，教学通过结论失效）

- 内容与教学：内容口径、课堂最低产出和 90 分钟结构不变；视觉提升教学门复核通过。
- 正式文件：20 页；`slides.pptx`；SHA-256 `725e634acc892e951e938e8e6064cfb600d7a2fc47dc25e47540bb40539b5317`。
- 技术检查：包结构与布局 0 finding；1 个 Master、4 个 Layout；20/20 页 notes 含 `[Sources]`；教学文字不低于 18 pt。
- 教学检查：固定指标、预算/停止、回退与失败账本保持同一冻结循环；120 份输出不被误写为优化循环。
- 视觉检查：Artifact Tool 全尺寸与联系图已复核；`metric.yaml` 与虚构日志标签无裁切；AutoResearch/AI Scientist 页脚显示作者/系统与年份。
- Microsoft PowerPoint 原生检查：通过；最新正式候选已原生打开、导出并逐页复核，P06 指标文件标签、P18 同伴互查页和来源页均可读。LibreOffice 的字体替换结果不作为本轮通过依据。
- QA：`.work/ppt/lesson-11/2026-09-12-visual-upgrade/lesson-11-visual-upgrade-v5-render/`、`.work/ppt/lesson-11/2026-09-12-visual-upgrade/lesson-11-visual-upgrade-v5-contact.webp`、`.work/ppt/lesson-11/2026-09-12-visual-upgrade/lesson-11-visual-upgrade-v5-validation.json`。

### 课程减负修订轮（2026-09-12，历史；已由本页“对象化视觉提升轮（正式）”取代）

- 课次目标门与内容门通过：仍从第 10 课一次受限执行升级为可重复执行与失败恢复，不新增正式提交。
- 90 分钟教学门通过：各段为整数时长且合计 90；个人实践为 10 + 10 分钟，中间插入 5 分钟教师点评。
- 逐页映射门通过：20 页保留原页码，但系统对照改为短分析，屏显无课堂计时。
- 案例口径统一：`20 篇 × 2 条件 × 3 次 = 120 份输出`；指标为相对人工限定条件基准的遗漏率，不再使用“缺失字段数/5”。
- PPT 制作与三重检查：已依新母稿完成 20 页正式 PPTX；技术、教学和 Artifact Tool 视觉检查通过，终版 Microsoft PowerPoint 原生视觉复检待补。

### 正式 PPT 验证记录（2026-09-12，历史；已由本页对象化视觉提升轮取代）

> 以下为当时事实记录；其中笼统的视觉通过与“锁屏/原生待补”状态不代表当前验收状态。

- 页数与指纹：20 页；SHA-256 `4b45dd3b5a018f896adf92a267bf492b84921b4400c0c7a62886cea4839b78b7`。
- 技术检查：包结构、Master/Layout 关系和磁盘重开校验通过；20/20 页 notes 含闭合 `[Sources]`；空 placeholder 0；包级 OOXML 审计确认承担课堂阅读任务的正文、表格、提示、风险和动作文字均不低于 18 pt，页码、来源和许可文字按规则豁免。
- 教学检查：屏显与 `slides.md` v0.4.0 一致；固定指标、预算、停止、回退和失败保留集中在同一循环，明确冻结批量队列不等于优化循环，并把产出直接交给第 12 课最小工作流设计。
- 视觉检查：已完成 Artifact Tool 全尺寸逐页检查与 contact sheet 检查；修正 P04 Keep/Discard 标签和 P10 卡片密度后未见裁切、遮挡、异常换行或空可见对象。
- 兼容性检查：最终版经 LibreOffice 无界面导出为 20 页 PDF，提取文本含中文；该结果不替代 Microsoft PowerPoint 验收。字号修订前候选曾在 Microsoft PowerPoint Slide Sorter 检查，中文与版式正常；最终 18 pt 版因 macOS 锁屏未能再次原生复检，待补。
- QA 证据：`.work/ppt/lesson-11/2026-09-12-load-revision/validation-18pt-v4.json`、`.work/ppt/lesson-11/2026-09-12-load-revision/artifact-render-18pt-v4/`、`.work/ppt/lesson-11/2026-09-12-load-revision/libreoffice-18pt/slides-final-18pt-validated-v4.pdf`。

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 10 课受限 Agent 执行：本课把"跑通一次"扩展为可重复运行的受限循环，把任务契约草稿升级为四要素（输入/输出/成功标准/不适用范围）。
- 承接第 9 课实验规格与可复现说明：本课把第 9 课的停止条件扩展为循环的预算与三类停止触发器，把可复现字段保留在循环中以防指标漂移。
- 为第 12 课个人工作流设计铺垫：本课的循环骨架（任务契约/Context/工具权限/状态/执行循环/工件追踪/Evals/失败恢复）是第 12 课个人工作流设计的直接输入；第 12 课先拆解现成 Agent/Skill，再把这些要素重组为个人工作流。
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

## 门控状态（2026-08-07，历史；当前 gate5/gate6 以对象化视觉提升轮为准）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 `备课规划.md` 第 11 课目标段；八阶段定位阶段七"原型验证（实验追踪）"；承接第 10 课受限 Agent，为第 12 课个人工作流设计铺垫） |
| 2. 内容门 | ✅ 复核通过（三件套已统一为受限循环五步、四约束、失败保留和八维分析；AutoResearch / AI Scientist 只作分析对象；AutoResearch 固定为 commit `228791f`；AI Scientist workshop 证据已按 Nature 正文精确改写；课程教学参数与日志均明确标为示意；不新增正式提交） |
| 3. 90 分钟教学门 | ✅ 复核通过（`备课规划.md` 第 11 课权威六段：0-18/18-35/35-55/55-75/75-85/85-90；P02 从 2:15 开始 1 分钟工件缺口标记，55 分钟开始持续实践；最小产出=受限循环说明（四约束+五步骨架+审核点）+失败迭代记录（七字段）+八维拆解表（≥4 维）；无环境时使用纸面/Markdown 备用路径） |
| 4. 逐页映射门 | ✅ 复核通过（19 页均映射 handout 小节；P09/P10/P17 的教学反例/样例边界已同步；P12-P15 的分析对象与外推边界一致；P19 明确衔接第 12 课个人工作流设计） |
| 5. PPT 制作 | ✅ 通过（19 页；以 `lesson-07/slides.pptx` 为直接模板基线，使用 `@oai/artifact-tool` 模板跟随流程；保留 1 个 master、4 个 layout、交大品牌、页眉页脚与页码；13 个关键页先完成四字段设计契约；19/19 页 speaker notes 含 `[Sources]`） |
| 6. 三重检查 | ✅ 通过（技术：19 页、19 组 notes、`[Sources]` 19/19、空结构 placeholder 0、默认提示文本 0、越界对象 0、模板忠实度 0 问题；教学：五步/四约束/失败保留/分析对象边界/第 12 课衔接闭环，19 页均映射 handout；视觉：Artifact Tool 逐页渲染与关键页全尺寸检查，无可见 overlap、clipping、wrapping 失败；最终磁盘文件经 LibreOffice 重开并导出 19 页 PDF，再逐页复渲染检查） |
| 7. 里程碑归档 | ✅ 完成判断（本课沿用第 7 课已确立的交大正式视觉语言，没有形成需单独保留的新模板里程碑；不向 `archive/` 复制重复 PPTX。构建脚本、frame map、双重渲染和 QA 台账保留在 `.work/ppt/lesson-11/2026-08-07-formal/`） |

## 修订轮登记（2026-08-12，handout v0.2.0，历史）

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
