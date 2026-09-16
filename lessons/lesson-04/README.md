# 第 4 课内容入口（MOC）

> AI 辅助精读与主张核验。本文件是第 4 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。


## 内容与 PPT 同步轮（2026-09-16，当前状态）

- 教师确认：用户已明确“通过，你修改后续课程和PPT”；据此完成后续内容和课件同步。此确认解除本轮内容与制作前置阻塞，现场授课验收另行登记。
- 内容、教学与映射：现行讲义、教案和 18 页母稿已同步；90 分钟安排保持原定结构，板书、诊断反馈和过渡见教案。
- PPT：共 18 页；本轮屏显重绘：无屏显改动；更新全页讲述备注；18/18 页讲述备注及来源已更新。
- 检查：文件结构、画布和字号检查无阻断项；全页渲染与 LibreOffice 重开通过。保留交大模板及原生可编辑研究工件。
- 待现场：全套 Microsoft PowerPoint、授课电脑及教室投影；助教按实际人数、环境和换场复演。旧文件的原生通过记录不代表本轮文件已通过现场验收。
- 文件指纹：`bea382b73d9e7b6a8ae7d6864aa866cf5ca01f9908586a6bc870d13692010e88`。
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
| [handout.md](./handout.md) | 现行·学生讲义 v0.6.1 | 学生可独立阅读的当前内容源 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.10.1 | 90 分钟流程、板书、诊断反馈、过渡与演示安排 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.10.1 | 18 页屏显、讲述、动作与来源；已同步 PPT |
| [slides.pptx](./slides.pptx) | 现行·可编辑课堂 PPT（18 页） | 已同步本轮内容；文件与渲染通过，现场核验待完成 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.3.1 | 本轮实际构图、可编辑对象与验收；旧规格保留历史 |
| [reading-card-demo.md](./reading-card-demo.md) | 现行·教学资产 v1.0.0 | Keshav 2007 真实原文的完整阅读卡、偏差审计与断网备用对象 |
| [mi-reading-card-demo.md](./mi-reading-card-demo.md) | 现行·教学资产 v1.0.0 | C02/C16/C31 三张公开论文主张级阅读卡与受限判断 |
| [assets/](./assets/) | 现行·图形资产 | MI 精读证据阶梯 SVG 与出处/许可登记 |

### 视觉升级（2026-09-12）

- 逐页映射门：✅ `slides.md` v0.9.1 仅更新视觉结构与字号层级，屏显语义、页数与 90 分钟教案不变。
- PPT 构建：✅ 18 页候选 r2 已提升为现行 [slides.pptx](./slides.pptx)；构建目录 `.work/ppt/lesson-04/2026-09-12-visual-upgrade/`；SHA256 `a1dd50fe5dbe6e5b02eae401a08883b36c8a4a2b1bdcec9732e0e7e79a383a24`。
- 技术检查：✅ finalizer、Artifact Tool 最终文件重导入、18/18 notes `[Sources]`、1 Master/4 Layout、空 placeholder 与字号审计通过。
- 教学检查：✅ P11 使用 Keshav p.83 §2 真实原文裁图，课堂构造 AI 输出与原文身份分离；P15 保持单主张精读的完整工作表。
- 视觉检查：✅ 18 页全尺寸和 contact sheet 逐页复核通过；标题 30–32pt、常规正文 22–24pt、原文/工作表 18–20pt，正文以 regular 为主，未见裁切、遮挡或异常换行。
- PowerPoint 原生检查：✅ Microsoft PowerPoint 已打开 r2 并原生导出；18/18 张 `native-checked-*.png` 全尺寸逐页复核通过，原文裁图、MI 图、表格换行与中文显示完整；原生 PDF 为 `.work/ppt/visual-upgrade-20260912/representatives/lesson-04-slides-v0.9.1-visual-r2-native.pdf`。
- 替代关系：本节视觉检查取代下方减负轮的旧视觉通过记录；旧记录仅保留为历史，不再证明当前候选通过。
- 状态：✅ 候选已写回正式 `slides.pptx` v0.9.1；正式文件 SHA256 `a1dd50fe5dbe6e5b02eae401a08883b36c8a4a2b1bdcec9732e0e7e79a383a24`。LibreOffice 中文字体回退单独记为兼容性风险，本轮不宣称 LibreOffice 通过。
- QA：`.work/ppt/visual-upgrade-20260912/audit/lesson-01-06-qa.md`。

> 状态说明：以上视觉升级记录是现行 PPT 的唯一验收口径。下方减负轮、旧门控表与 2.0 修订轮仅保留当时事实；其中旧的笼统“视觉通过”记录已被本轮技术、教学、视觉和 PowerPoint 原生检查取代。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 贯穿案例承接第 1-3 课"结构化阅读卡与 AI 摘要遗漏率"，与第 3 课候选文献表的 verified 条目衔接。
- 阅读卡统一写入个人项目 `reading-cards.md`；第 5 课再重组进证据地图，第 6 课问题门统一检查至少 3 张完整精读卡。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)、[assignments.md](../../course/assignments.md) |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 4 课（v1.4.0 含 AI 导航—原文核验—偏差审计阅读流程） |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 4 课
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 内容复核与历史门控记录（基线日期 2026-08-07）

### 课程减负与单主张精读（修订轮，2026-09-12）

- 内容门：重走通过。当堂只围绕一条关键主张完成原文位置、证据、限定、判断和偏差审计；Keshav 是动作校准，C02/C16/C31 共同收窄一条主张。
- 90 分钟教学门：重做通过。方法与演示各 15 分钟；个人实践为 12+10 分钟，中间插入 5 分钟教师点评；合计 90 分钟。
- 逐页映射门：重走通过。P11–P15 已同步单主张及分段实践口径，18 页结构不变。
- PPT 制作：✅ 18 页现行 PPTX 已按 `slides.md` v0.9.0 重建；保留交大原生 Master/Layout、校徽、红标题带、主题字体、页码与 notes。SHA256：`2e23ce7987d009af294bcb3596e5cdae7673c88c53c7a9e6738f8ea37665c571`。
- 技术检查：✅ 包完整性、Artifact Tool 重开、18/18 notes `[Sources]`、1 个 Master/4 个 Layout、空 placeholder、屏显计时和布局 finding 均通过；包级审计确认全部课堂正文实际字号 ≥18pt。记录：`.work/ppt/lesson-04/2026-09-12-load-revision/validation-r6.json`、`qa-summary.json`、`.work/course-load-revision/font-audit-r6.json`。
- 教学检查：✅ 当堂围绕一条关键主张完成原文位置、证据、限定、判断与偏差审计；屏显、互动和来源与现行逐页母稿一致。
- 视觉检查：✅ Artifact Tool 全尺寸逐页渲染与 contact sheet 复核通过；Microsoft PowerPoint 原生打开并在 Slide Sorter 中检查 18 页，中文、换行和品牌元素完整。联系表：`.work/ppt/lesson-04/2026-09-12-load-revision/contact-sheet-r6/contact-sheet.png`。
- 剩余风险：LibreOffice 对 Artifact Tool 生成 PPTX 的 PDF 导出存在中文丢失兼容性问题，本轮不宣称 LibreOffice 通过；实际 PowerPoint 已通过，教室投影仍需课前现场检查。

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 备课规划 第 4 课目标段；八阶段定位阶段四"外部输入摄取"→阶段五"证据整理"起始） |
| 2. 内容门 | ✅ 通过（完整阅读卡全字段验收与四态进入规则已统一；P11-P13 使用 Keshav 2007 真实原文对象，课堂构造 AI 输出双重标注） |
| 3. 90 分钟教学门 | ✅ 通过（节奏表对齐备课规划 v2.2.0 第 4 课八段；P02 约 4:00 首次短互动，P06 使用个人论文微练习，P15 48:00 开始 27 分钟持续项目实践；课堂至少 1 张完整阅读卡，第 6 课前累计至少 3 张） |
| 4. 逐页映射门 | ✅ 通过（17 页映射表，方法段合并 3 处去重后重编号；每页标 handout 小节） |
| 5. PPT 制作 | ✅ 完成（17 页正式 PPTX；交大模板 master/layout、标题带、校徽、页码和 notes 保留） |
| 6. 三重检查 | ✅ 通过（模板/notes/画布/ZIP；90 分钟节奏与最低产出；LibreOffice 重开、17 页逐页与高风险页视觉复核） |
| 7. 里程碑归档 | 本轮为首个通过全部门控的正式版，无被替代正式稿，不单独归档 |

## 授课前复核

- 复核 Keshav 2007 公开 PDF 可访问；不可访问时使用 `reading-card-demo.md` 的已核验记录，不伪造现场访问。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。

## 2.0 批次 1 修订轮（2026-08-20）

- **内容门**：✅ C02/C16/C31 的模型、任务、对照、原文位置和 caveat 已核验；Keshav P11 保留为定位动作校准，P12-P13 换入 MI 主张级证据阶梯与 `review` 判断。
- **90 分钟门**：✅ 时间结构不变，MI 只替换 27-43 分钟教师演示后半段；48-75 分钟学生实践负荷不变。
- **逐页映射门**：✅ 17 页不增页，P12-P13 与 v0.7.0 母稿逐页对应。
- **PPT 与三重检查**：✅ 17 页正式 PPTX 已重建；17/17 notes 含来源块，Artifact Tool 布局 0 越界，OOXML 验证通过，LibreOffice 重开导出 17 页并完成全页与高风险页视觉检查。
- **剩余风险**：授课前仍需在实际 PowerPoint 与教室投影环境做现场放映；公开论文链接不可用时使用本地阅读卡与 SVG 备用。

## 封面与收束修订轮（2026-08-20）

- **内容门**：✅ 课次目标、案例与证据口径不变；只把封面识别信息和既有收束知识重新分层。
- **90 分钟门**：✅ 原 85-90 分钟收束段拆为 P17 知识点总结与 P18 退出/预告，各 2.5 分钟；总时长仍为 90 分钟。
- **逐页映射门**：✅ 新 P17 映射讲义五步流程、主张核验与偏差审计；原 P17 顺延为 P18。
- **PPT 与三重检查**：✅ 18 页正式 PPTX 已重建；18/18 notes 含来源块，布局 0 越界，Office 校验通过，LibreOffice 重开导出 18 页并完成全卷、封面、P17-P18 视觉检查。
- **剩余风险**：授课前仍需在实际 PowerPoint 与教室投影环境确认字体替换和标题在两横线之间的最终观感。
