# 第 6 课内容入口（MOC）

> 问题定义、第一性原理与问题门。本文件是第 6 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。


## 内容与 PPT 同步轮（2026-09-16，当前状态）

- 教师确认：用户已明确“通过，你修改后续课程和PPT”；据此完成后续内容和课件同步。此确认解除本轮内容与制作前置阻塞，现场授课验收另行登记。
- 内容、教学与映射：现行讲义、教案和 22 页母稿已同步；90 分钟安排保持原定结构，板书、诊断反馈和过渡见教案。
- PPT：共 22 页；本轮屏显重绘：P04、P10、P11、P14、P16、P22；22/22 页讲述备注及来源已更新。
- 检查：文件结构、画布和字号检查无阻断项；全页渲染与 LibreOffice 重开通过。保留交大模板及原生可编辑研究工件。
- 待现场：全套 Microsoft PowerPoint、授课电脑及教室投影；助教按实际人数、环境和换场复演。旧文件的原生通过记录不代表本轮文件已通过现场验收。
- 文件指纹：`fab97a09981e31f41222744cdd3a4261cf1a5dd439335dcffaa0c8b53c231ebc`。
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
| [handout.md](./handout.md) | 现行·学生讲义 v1.3.1 | 学生可独立阅读的当前内容源 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v1.4.1 | 90 分钟流程、板书、诊断反馈、过渡与演示安排 |
| [slides.md](./slides.md) | 现行·逐页母稿 v1.4.1 | 22 页屏显、讲述、动作与来源；已同步 PPT |
| [slides.pptx](./slides.pptx) | 现行·可编辑课堂 PPT（22 页） | 已同步本轮内容；文件与渲染通过，现场核验待完成 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.4.1 | 本轮实际构图、可编辑对象与验收；旧规格保留历史 |
| [mi-problem-definition-demo.md](./mi-problem-definition-demo.md) | 课后迁移教学资产 v1.0.0 | MI 结构性问题、H-eff/H-rob/H-faith、第一性原理与九项 CP1 自查；不作为第 7-9 课主线输入 |
| [assets/](./assets/) | 现行·图形资产 | MI 问题到 baseline 接口 SVG 与出处/许可登记 |

### 视觉升级（2026-09-12）

- 逐页映射门：✅ `slides.md` v1.3.2 仅更新视觉结构与字号层级，屏显语义、页数与 90 分钟教案不变。
- PPT 构建：✅ 22 页候选 r3 已提升为现行 [slides.pptx](./slides.pptx)；构建目录 `.work/ppt/lesson-06/2026-09-12-visual-upgrade/`；SHA256 `81d2a8ee1b2b592b95872ca20074a172913c14ebcb81865ceecd0f78e0b2c713`。
- 技术检查：✅ finalizer、Artifact Tool 最终文件重导入、22/22 notes `[Sources]`、1 Master/4 Layout、空 placeholder 与字号审计通过。
- 教学检查：✅ P14 保持阅读卡案例与 H1/A1/A2/A3/L9 接口，P18 只形成候选题取舍、边界、可证伪命题、一个待验证前提与替代解释标记。
- 视觉检查：✅ 22 页全尺寸和 contact sheet 逐页复核通过；标题 30–32pt、常规正文 22–24pt、清单/工作表 18–20pt，正文以 regular 为主；r3 已重构 P7 双分支并修正 P10 句号孤行。
- PowerPoint 原生检查：✅ Microsoft PowerPoint 已打开 r3 并原生导出；22/22 张 `native-checked-*.png` 全尺寸逐页复核通过，P7 双分支与 P10 可证伪命题无重叠或异常换行，中文与品牌元素完整；原生 PDF 为 `.work/ppt/visual-upgrade-20260912/representatives/lesson-06-slides-v1.3.2-visual-r3-native.pdf`。
- 替代关系：本节视觉检查取代下方减负轮的旧视觉通过记录；旧记录仅保留为历史，不再证明当前候选通过。
- 状态：✅ 候选已写回正式 `slides.pptx` v1.3.2；正式文件 SHA256 `81d2a8ee1b2b592b95872ca20074a172913c14ebcb81865ceecd0f78e0b2c713`。LibreOffice 中文字体回退单独记为兼容性风险，本轮不宣称 LibreOffice 通过。
- QA：`.work/ppt/visual-upgrade-20260912/audit/lesson-01-06-qa.md`。

> 状态说明：以上视觉升级记录是现行 PPT 的唯一验收口径。下方减负轮、旧门控表与 2.0 修订轮仅保留当时事实；其中旧的笼统“视觉通过”记录已被本轮技术、教学、视觉和 PowerPoint 原生检查取代。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 5 课证据地图与研究空白：本课把第 5 课通过三步检验的研究空白候选收敛为可检验问题。第 5 课 G1（缺角空白"阅读卡是否强制定位原文→降低遗漏"）在本课改写为结构性研究问题。
- 为第 7 课机制假设铺垫：本课第一性原理推导的"待验证前提"将成为第 7 课机制假设的直接输入；可证伪命题的推翻条件将成为第 7 课实验设计的依据。
- 问题门提交指向当前个人项目版本（链接/tag/压缩包），不重复制作汇报文档。`problem-definition.md` 字段对齐 [starter-template.md](../../course/starter-template.md) §3。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)、[assignments.md](../../course/assignments.md)（Checkpoint 1 问题门条件——权威来源） |
| handout（第一性原理边界） | [备课规划.md](../备课规划.md) 执行原则 9、[AGENTS.md](../../AGENTS.md) 证据标准 |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 6 课 |
| 问题定义字段 | [starter-template.md](../../course/starter-template.md) §3 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 6 课 → 课后提交问题门材料包
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 内容复核与历史修订记录

### 课程减负修订轮（2026-09-12）

| 门 | 状态 |
| --- | --- |
| 课次目标 | ✅ 保持不变：从候选题收敛到问题定义与第一性原理，并完成问题门提交准备 |
| 内容门 | ✅ 通过：新颖性改为诊断项；课堂只形成一个替代解释标记，完整 H1/A1/A2/A3 设计移交第 7 课 |
| 90 分钟教学门 | ✅ 通过：整数时长合计 90；个人实践拆为 12+5+8 分钟，含教师中点点评 |
| 逐页映射门 | ✅ 通过：handout v1.2.1、teaching-plan/slides v1.3.1 同步课堂最低产出、课后补全和九项问题门边界；P14 保持阅读卡贯穿案例 |
| PPT 制作 | ✅ 22 页现行 PPTX 已按 `slides.md` v1.3.1 重建；SHA256：`03a05af942e174ce63df1fdd247eb631f9e558352abd842e54f2cae1372b38b6` |
| 三重检查 | ✅ 技术：包完整性、Artifact Tool 重开、22/22 notes `[Sources]`、1 Master/4 Layout、空 placeholder、屏显计时和布局 finding 通过，正文实际字号均 ≥18pt；教学：P14 阅读卡案例与 H1/A1/A2/A3 接口一致；视觉：全尺寸、contact sheet 与 PowerPoint Slide Sorter 22 页原生检查通过 |
| 里程碑归档 | 不适用 |

**本轮处理结果**：MI 平行案例降为课后迁移阅读；课堂 P14 已替换为阅读卡贯穿案例，只向第 7-9 课移交替代解释标记并按全局口径展开 H1/A1/A2/A3，不再使用 `mi-question-to-baseline.svg` 作为课堂主线图。技术记录：`.work/ppt/lesson-06/2026-09-12-load-revision/validation-r6.json`、`qa-summary.json`、`.work/course-load-revision/font-audit-r6.json`；联系表：`.work/ppt/lesson-06/2026-09-12-load-revision/contact-sheet-r6/contact-sheet.png`。L06 P07 的两条几何 warning 经全尺寸与 PowerPoint 复核为嵌套卡片边框的预期重叠，不构成文字碰撞。

**剩余风险**：LibreOffice 对 Artifact Tool 生成 PPTX 的 PDF 导出存在中文丢失兼容性问题，本轮不宣称 LibreOffice 通过；实际 PowerPoint 已通过，教室投影仍需课前现场检查。

### 修订轮登记（2026-08-10，G3 选题训练增强）

| 门 | 状态 |
| --- | --- |
| 课次目标 | ✅ 复核通过（课次目标不变；备课规划 v2.3.1 第 6 课段已同步问题来源交叉检查与四维选题标准卡） |
| 内容门 | ✅ 重走通过（handout/teaching-plan/slides.md 三件套 v1.0.0：§一 新增问题来源交叉检查与候选题池比较；问题门八项条件不变，候选题池与选题理由为 problem-definition.md 课程扩展字段；霍强案例已对本地副本核验） |
| 90 分钟教学门 | ⬇ 降级复核通过（时间结构不变；0-25 段 P01-P11 各约 2:16，P02 首次短互动与 40 分钟持续实践位置不变） |
| 逐页映射门 | ✅ 重走通过（新增 P07 问题来源与四维选题标准卡；原 P07-P20 重编号为 P08-P21；映射表与章节引用已同步） |
| PPT 制作 | ✅ 重走通过（21 页重建：构建目录 `.work/ppt/lesson-06/2026-08-10-g3-rebuild/`；由模板页 duplicate 出第 21 页，继承交大 master/layout；每页 speaker notes 含 `[Sources]`） |
| 三重检查 | ✅ 技术/教学通过（布局检查 0 越界；LibreOffice 重开导出 21 页；21/21 notes；新 P07 标题与来源核验）；视觉逐页抽查渲染图已生成（`final-render/`），待授课教师确认 |
| 里程碑归档 | 不适用 |

### 2026-08-06 基线记录

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 备课规划 第 6 课目标段；八阶段定位阶段一"问题定义"+阶段二"第一性原理分析"，承接第 5 课研究空白，向第 7 课机制假设输出） |
| 2. 内容门 | ✅ 通过（三件套与 assignments.md 八项门条件一致；证据地图统一为直接/补充/冲突/空白；虚构教学样例不承担真实检索或实证证据角色；AI 风险字段保留错误/过度概括/遗漏或已检查风险两条合法路径） |
| 3. 90 分钟教学门 | ✅ 通过（权威 5 段覆盖 0-90；P02 约 2:30 首次短互动，40 分钟开始持续项目实践；最小产出为 problem-definition 更新版 + 第一性原理推导初版；备用路径已标） |
| 4. 逐页映射门 | ✅ 通过（20 页显式标注页面任务、handout 位置、证据角色和学生动作；关键页契约已建立） |
| 5. PPT 制作 | ✅ 通过（20 页正式 PPTX；继承交大模板 master/layout、红色标题带、校徽、主题字体与页码；每页 speaker notes 含 `[Sources]`） |
| 6. 三重检查 | ✅ 通过（内容映射、90 分钟节奏、技术结构与逐页视觉检查；LibreOffice 重开导出 20 页；无空占位符、无越界对象） |
| 7. 里程碑归档 | 不适用（本次为第 6 课首个正式基线，不另存重复历史副本） |

## 待复核项

- **问题门条件对齐**：handout §五·2、slides P15-P16 与 [assignments.md](../../course/assignments.md) Checkpoint 1 九项条件已逐项核对；第 8 项是真实失败/死路的原因、处理与回写位置，第 9 项是 AI 来源与人工核验。
- 演示用 problem-definition.md 完整版样例需在授课前准备实际可投屏版本；
- 演示用失败案例（主题当问题、第一性原理脱离文献）需在授课前准备；
- 与第 7 课的衔接点已经在 P14/P22 固定为阅读卡案例的待验证前提与替代解释标记 → H1/A1/A2/A3 → 第 9 课完整实验规格；第 7-9 课仍需核对字段是否原样承接；
- `problem-definition.md` 字段模板是否需要根据本课新增"第一性原理推导"段更新 [starter-template.md](../../course/starter-template.md) §3。
- 授课前仍需在教室电脑、实际 PowerPoint 版本和投影设备上做一次现场放映检查；LibreOffice 检查不能替代真实教学设备验收。

### 2.0 批次 1 修订轮（2026-08-20）

- **内容门**：✅ CP1 九项条件、`failure-log.md` 与 starter/project template 已同步；MI 演示把 C02/C16/C31 的证据缺口拆成 H-eff/H-rob/H-faith，不报告未执行实验结果。
- **90 分钟门**：✅ 五段时间结构不变；P14 仍处于 25-40 分钟教师演示段，40 分钟开始个人实践。
- **逐页映射门**：✅ 21 页不增页，P14-P16 承担 MI 接口、九项条件和累计工件自查。
- **PPT 与三重检查**：✅ 21 页正式 PPTX 已重建；21/21 notes 含来源块，布局 0 越界，OOXML 验证通过，LibreOffice 重开导出 21 页并完成全页与高风险页视觉检查。

### 封面与收束修订轮（2026-08-20）

- **内容门**：✅ 课次目标、九项问题门条件和 MI baseline 接口不变；只重组封面识别信息和收束层级。
- **90 分钟门**：✅ 原 78-90 分钟段拆为 P20 总结、P21 提交/回退、P22 退出/预告，各 4 分钟；总时长仍为 90 分钟。
- **逐页映射门**：✅ 新 P20 映射结构性问题、可证伪命题、第一性原理和问题门主链；原 P20-P21 顺延为 P21-P22。
- **PPT 与三重检查**：✅ 22 页正式 PPTX 已重建；22/22 notes 含来源块，布局 0 越界，Office 校验通过，LibreOffice 重开导出 22 页并完成全卷、封面、P20-P22 视觉检查。
- **剩余风险**：授课前仍需在实际 PowerPoint 与教室投影环境确认字体替换和长课名的最终行宽。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
