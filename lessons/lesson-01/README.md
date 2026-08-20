# 第 1 课内容入口（MOC）

> AI 辅助科研导论、OpenCode 与八阶段研究链路。本文件是第 1 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 | 面向学生、可脱离课堂独立阅读的正式讲义：概念、方法、案例、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v1.7.0（34 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [slides.pptx](./slides.pptx) | 现行·课堂课件（34 页） | 封面只保留正式课名；退出卡前含独立知识点总结；每页含 `[Sources]` speaker notes |
| [keystone-design-spec.md](./keystone-design-spec.md) | 规范 | 18 个风险触发关键页的设计契约、模板例外与历史视觉基线 |
| [reading-notes.md](./reading-notes.md) | 现行·教师文献精读卡集 | 第 1 课 8 篇文献按 AI 辅助阅读协议产出的精读卡，原文定位已完成，待教师复核定稿 |
| [assets/](./assets/) | 教学资产 | 论文图重绘、概念图等课堂用图 |

## 2026-08-20 课件修订

- 封面标题按课程大纲改为“第1讲 AI 辅助科研导论、OpenCode 工作平台与八阶段研究链路”，并上移至两条横线之间。
- 新增 P33“本讲知识点总结”，原收束页顺延为 P34；总页数 33→34。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- `keystone-design-spec.md` → 指导 `slides.md` 关键页的视觉设计契约。
- `reading-notes.md` → 为 `handout.md` 提供文献来源与精读卡。
- 2026-07-07 的 `introduction.md` / `lecture-notes.md` 已移到 [被替代文稿归档](../../archive/superseded-docs/lesson-01/)，现行制作不以之为母版。
- 旧 39 页 PPTX 已移到 [PPT 试制里程碑](../../archive/ppt-experiments/lesson-01/2026-07-30-pre-gate-39-page-baseline/decision-record.md)。现行 [slides.pptx](./slides.pptx) 与 33 页母稿一致。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（评分/提交） | [assessment.md](../../course/assessment.md)、[assignments.md](../../course/assignments.md) |
| slides（视觉规则） | [ppt-design-criteria.md](../ppt-design-criteria.md)、[ppt-quality-gates.md](../../course/ppt-quality-gates.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 1 课 |

## 阅读路径

- **学生**：`handout.md` → `assets/` → `course/reading-list.md` 第 1 课
- **教师**：`teaching-plan.md` → `slides.md` → `ppt-design-criteria.md` → `keystone-design-spec.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过 |
| 2. 内容门 | ✅ 通过（按 v2.1.0 对齐：90 分钟节奏表、首课文件清单、学习目标、课后阅读要素、链路草图产出） |
| 3. 90 分钟教学门 | ✅ 通过（八阶段段 11→7 合并、P02 讲师介绍插入，全文 33 页；per-page 时间按 v2.1.0 权威 8 段重排 0:00-90:00；首次学生动手 P03 投票约 1:30；最小产出=个人工作区+problem-definition 一处修改+ai-usage-log+diff+八阶段链路草图 P30 第7步；备用路径=环境故障录屏+纸面/Markdown 模板；桌面推演/教师终审为通用最终步骤） |
| 4. 逐页映射门 | ✅ 通过（33 页逐页映射表复核，每页标 handout 小节；合并页 handout 引用已合并；90 分钟表页码列与 teaching-plan PPT 执行索引已同步） |
| 5. PPT 制作 | ✅ 通过（33 页正式 PPTX；P05 以 2023 综述框架替代与 P04 重复的 AI Scientist，P10 使用权威工件名与单一仓库树，P19-P20 改为因果链与可追溯工件，P26 展示三个固定虚构建议及四问审核轨道，P08/P25/P27/P28 关键标签为 18 pt；全量渲染、模板保真、越界、空占位符、speaker notes 与 LibreOffice 重开检查通过） |

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
