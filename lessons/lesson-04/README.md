# 第 4 课内容入口（MOC）

> AI 辅助精读与主张核验。本文件是第 4 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.4.0 | 面向学生、可脱离课堂独立阅读：AI 辅助精读五步流程、主张核验、完整阅读卡字段、偏差审计与 L3/L4 移交边界 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.6.0 | 90 分钟流程、PPT 执行索引、真实原文演示、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.6.0（17 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [slides.pptx](./slides.pptx) | 待同步·上一版课堂 PPT（17 页） | 对应 v0.5.0 母稿；相关边界与路径页须同步后重新执行三重检查 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 规范 v1.1.0 | 风险触发关键页的设计契约、证据边界、模板例外与制作后验收 |
| [reading-card-demo.md](./reading-card-demo.md) | 现行·教学资产 v1.0.0 | Keshav 2007 真实原文的完整阅读卡、偏差审计与断网备用对象 |

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

## 门控状态（2026-08-07）

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

## 2.0 口径同步（2026-08-09）

- 内容、90 分钟节奏和 17 页映射已复核；L3/L4 边界与项目路径现已一致。
- 现有 PPTX 对应上一版母稿，本轮未重建；相关内容页同步与三重检查留待第 4 课 2.0 制作轮。
