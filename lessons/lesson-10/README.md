# 第 10 课内容入口（MOC）

> AI 辅助编码、调试与受限 Agent 执行。本文件是第 10 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。


## 内容与 PPT 同步轮（2026-09-16，当前状态）

- 教师确认：用户已明确“通过，你修改后续课程和PPT”；据此完成后续内容和课件同步。此确认解除本轮内容与制作前置阻塞，现场授课验收另行登记。
- 内容、教学与映射：现行讲义、教案和 17 页母稿已同步；90 分钟安排保持原定结构，板书、诊断反馈和过渡见教案。
- PPT：共 17 页；本轮屏显重绘：P04、P05、P06、P11；17/17 页讲述备注及来源已更新。
- 检查：文件结构、画布和字号检查无阻断项；全页渲染与 LibreOffice 重开通过。保留交大模板及原生可编辑研究工件。
- 待现场：全套 Microsoft PowerPoint、授课电脑及教室投影；助教按实际人数、环境和换场复演。旧文件的原生通过记录不代表本轮文件已通过现场验收。
- 文件指纹：`32be95a38017ede80995e85801df2a0149049817a7e834e46ef6caf0f780a3f0`。
- 记录：[全课同步与验证](../../docs/course-ppt-sync-20260916.md)；[逐课助教准备清单](../../docs/lesson-demo-assignment-20260915.md)。

下方历史轮次按日期保留，当前状态以本节及文件清单为准。

## 历史：整体复审修订轮（2026-09-15）

- 目标与课程结构：未变；正式提交仍为第 6、9、13、16 课。
- 内容：现行 Markdown 已完成本轮修订；板书、诊断答案与串词在教师教案；待教师复核本轮实质变化。
- 教学门：原时段与总时长不变，本轮复核；诊断嵌入既有开场，课堂包不替代本人项目的门条件。
- 逐页映射：标题、内容与互动按新母稿核对；页数保持不变。
- PPT：文件未变更，上轮技术与视觉记录仍描述旧文件；它们不证明本轮新内容已同步。旧 PPT 不应直接作为本轮修订后的讲授稿。
- 推迟项：教师内容复核后同步 PPT，再做文件级、视觉和实际投影检查；第 16 课继续保留内容门阻塞。
- 执行记录：[本轮修订与验证](../../docs/course-integrated-revision-20260915.md)；助教分工见[演示准备清单](../../docs/lesson-demo-assignment-20260915.md)。

下方先前通过记录均保留为历史。当前内容与呈现的状态以顶部 2026-09-16 同步轮为准。


## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.4.1 | 学生可独立阅读的当前内容源 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.6.1 | 90 分钟流程、板书、诊断反馈、过渡与演示安排 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.7.1 | 17 页屏显、讲述、动作与来源；已同步 PPT |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.2.1 | 本轮实际构图、可编辑对象与验收；旧规格保留历史 |
| [slides.pptx](./slides.pptx) | 现行·可编辑课堂 PPT（17 页） | 已同步本轮内容；文件与渲染通过，现场核验待完成 |
| [assets/agent-task-example/](./assets/agent-task-example/) | 现行·课次本地真实教学工件 | 可核验的 before/after、`generate.diff`、`unittest`、测试输出与越权失败日志；供 P12 演示和无执行环境备用路径使用 |

## 母稿与讲述备注同步修订轮（2026-09-13，当前）

- 课次目标与内容门：复核通过；现行讲义与教案的目标、案例口径、最低产出、研究门条件保持不变。
- 90 分钟教学门：复核通过；逐页建议时长合计 90 分钟，原个人实践分段与教师中点点评不变，屏显无课堂计时。
- 逐页映射门：17/17 页标题、实际屏显工件与讲义对应位置已复核。`slides.md` v0.6.1 为唯一标题与屏显母稿，正文之外的完整解释留在讲述备注。关键页规格补齐当前映射，旧规格明确归入历史。
- PPT 制作：Artifact Tool 恢复 17/17 页讲述提示、学生动作、时间与闭合 `[Sources]`。全部屏显页、Master/Layout、图表与资产逐字节保持原样。
- 技术检查：包完整性、布局和 Artifact Tool 重新导入通过；已对最终磁盘文件核对页数、notes 与允许变更的包内文件。覆盖前确认 PowerPoint 打开演示文稿数为 0，LibreOffice/Impress 无运行进程。
- 教学检查：清除 README 与 P17 notes 中将第 11 课冻结队列误写为按评价结果 Keep/Discard 的旧衔接。不新增提交或课堂任务。
- 视觉检查：最终导出文件全页重新渲染并扫描；屏显图层未修改，原生视觉基线可继续追溯。
- Microsoft PowerPoint 原生检查：本轮未执行，2026-09-12 的原生通过仅对应当时文件；本轮不得记为原生通过。教室投影仍待授课机复核。
- 正式文件：`slides.pptx`，17 页；SHA-256 `da80d27420ffe7df7ab83d742b8b6a0b0cad0492b2108f0bac4bb6db38bf4158`。
- QA：`.work/ppt/lesson-10/2026-09-13-sync-fix/validation.json`、`package-diff.json`、`final-path-check.json`、`formal-reopen.json`、`final-render/`；无须新增里程碑副本。

## 2026-08-20 课件修订

- 封面标题改为“第10讲 AI 辅助编码、调试与受限 Agent 执行”，并上移至两条横线之间。
- 新增 P16“本讲知识点总结”，原退出卡顺延为 P17；总页数 16→17。

## 文件关系

### 对象化视觉提升轮（正式，2026-09-12）

- 内容与教学：内容口径、课堂最低产出和 90 分钟结构不变；视觉提升教学门复核通过。
- 正式文件：17 页；`slides.pptx`；SHA-256 `6c075708e561bd251da46d0c9b8c77bf5a390ca66ab4ee8556570602a2de1d40`。
- 技术检查：包结构与布局 0 finding；1 个 Master、4 个 Layout；17/17 页 notes 含 `[Sources]`；教学文字不低于 18 pt。
- 教学检查：真实 diff 完整显示 `paper_id`、`summary` 与合法换行的缺失校验，受限执行继续直接交给第 11 课冻结循环。
- 视觉检查：Artifact Tool 全尺寸与联系图已复核；P06 标签不溢出，P12 采用 720px 代码区与 410px 测试/失败区，短字符串不自动折断；ReAct、SWE-bench 页脚显示作者与年份。
- Microsoft PowerPoint 原生检查：通过；最新正式候选已原生打开、导出并逐页复核，P12 代码完整、缩进与换行可读。LibreOffice 的字体替换结果不作为本轮通过依据。
- QA：`.work/ppt/lesson-10/2026-09-12-visual-upgrade/lesson-10-visual-upgrade-v8-render/`、`.work/ppt/lesson-10/2026-09-12-visual-upgrade/lesson-10-visual-upgrade-v8-contact.webp`、`.work/ppt/lesson-10/2026-09-12-visual-upgrade/lesson-10-visual-upgrade-v8-validation.json`。

### 课程减负修订轮（2026-09-12，历史；已由本页“对象化视觉提升轮（正式）”取代）

- 课次目标门：复核通过；仍是阶段七中的受限 Agent 执行，不新增提交。
- 内容门：通过；三件套已统一为配对阅读卡案例，并区分普通技术失败与伪造、隐瞒、越权等规范红线。
- 90 分钟教学门：通过；各段为整数时长且合计 90，个人实践为 10 + 10 分钟，中间插入 5 分钟教师点评。
- 逐页映射门：通过；17 页页码与讲义小节保持一一映射，学生屏显无课堂计时。
- PPT 制作与三重检查：已依新母稿完成 17 页正式 PPTX；技术、教学和 Artifact Tool 视觉检查通过，终版 Microsoft PowerPoint 原生视觉复检待补。
- 推迟项：最终 18 pt 版因 macOS 锁屏未能再次在 Microsoft PowerPoint 中复检，须在授课机解锁后补做 Slide Sorter、全尺寸页面和投影可读性检查。

### 正式 PPT 验证记录（2026-09-12，历史；已由本页对象化视觉提升轮取代）

> 以下为当时事实记录；其中笼统的视觉通过与“锁屏/原生待补”状态不代表当前验收状态。

- 页数与指纹：17 页；SHA-256 `97e2b25e7eec4c66ae7863c4627c240fe779298a5ad70d34884d6d81ab62bc99`。
- 技术检查：包结构、Master/Layout 关系和磁盘重开校验通过；17/17 页 notes 含闭合 `[Sources]`；空 placeholder 0；包级 OOXML 审计确认承担课堂阅读任务的正文、表格、提示、风险和动作文字均不低于 18 pt，页码、来源和许可文字按规则豁免。
- 教学检查：屏显与 `slides.md` v0.5.1 一致；保持“第 10 课受限执行→第 11 课冻结队列与失败恢复”的输入输出，真实 diff、测试以及根因/绕过/污染辨析可见。
- 视觉检查：已完成 Artifact Tool 全尺寸逐页检查与 contact sheet 检查；修正 P04 长命令换行和 P06 密度后未见裁切、遮挡、异常换行或空可见对象。
- 兼容性检查：最终版经 LibreOffice 无界面导出为 17 页 PDF，提取文本含中文；该结果不替代 Microsoft PowerPoint 验收。字号修订前候选曾在 Microsoft PowerPoint Slide Sorter 检查，中文与版式正常；最终 18 pt 版因 macOS 锁屏未能再次原生复检，待补。
- QA 证据：`.work/ppt/lesson-10/2026-09-12-load-revision/validation-18pt-v3.json`、`.work/ppt/lesson-10/2026-09-12-load-revision/artifact-render-18pt-v3/`、`.work/ppt/lesson-10/2026-09-12-load-revision/libreoffice-18pt/slides-final-18pt-validated-v3.pdf`。

### 学生入口呈现增强轮（2026-08-22，历史；当前 PPT 验收以对象化视觉提升轮为准）

- 门 1 与内容门已复核通过：只补任务契约与失败记录的具体链接，课堂闭环、案例事实和来源边界不变。
- 90 分钟教学门、逐页映射门、PPT 制作与三重检查不受影响，沿用下方既有通过记录；本轮不修改 `teaching-plan.md`、`slides.md` 或 `slides.pptx`。
- 待延后项：无；本机 Python、预置 diff 与测试输出的课堂可用性仍由助教按审阅协议复核。

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 9 课判断门：本课把第 9 课实验规格中"哪些步骤拟用 Agent、哪些步骤必须人工"标注改写为任务契约五字段，作为受限 Agent 执行的直接输入。
- 为第 11 课铺垫：本课的受限“一次执行”是第 11 课冻结运行队列与失败恢复的前提；优化循环作为另一个分析对象，不能据结果筛掉冻结评价队列中的运行。
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

## 门控状态（2026-08-07，历史；当前 gate5/gate6 以对象化视觉提升轮为准）

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
- **学术规范红线对齐**：handout §四·2 与 §六、slides P09（修复根因/绕过失败/污染实验）、P12（失败日志）与 P17（退出卡）、teaching-plan §一与 §六均对齐 [assessment.md](../../course/assessment.md) 学术规范红线——普通技术失败或被拒绝的绕过建议进入复盘；伪造、隐瞒、擅改评价协议与实际越权按红线处理。
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
