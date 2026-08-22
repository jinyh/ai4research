# 逐课备课工作区

最后更新：2026-08-22

当前正式课件制作与可恢复状态见 [PPT 制作进度](./ppt-production-progress.md)。

`lessons/` 用于制作课程正式教学材料。试讲材料与正式授课材料必须分开管理。

## 材料状态

| 状态 | 含义 | 使用规则 |
| --- | --- | --- |
| 现行内容 | 当前用于对齐课程事实、规则和课堂叙事的讲义、教案与逐页内容母稿 | 修改课程口径时先更新这些文件，并做跨文档检查 |
| 视觉试制 | `visual-*`、`pilot-*`、样张、对比图及其 PPTX | 只验证视觉方向；必须映射到现行内容母稿，不得自行产生课程规则或案例事实 |
| 历史稿 | 已被现行材料替代、但为追踪决策而保留的文件 | 文件内标明状态与替代文件；不得用作新 PPT 或课堂活动的制作依据 |

同一课只保留一套现行内容口径。PPTX 是该口径的视觉交付，不是独立的事实来源。

当前状态（2026-08-22）：全 16 课均已有讲义、教案、逐页母稿与可编辑课堂 PPT，PPT 共 16 套、332 页；现有 PPT 已完成结构、重开与渲染检查。第 1-15 课沿用各课 README 登记的门控状态；**第 16 课讲义 front matter 仍明确为“草稿，待教师复核与第二轮审校”，因此其正式内容门和整课正式发布尚未通过**，PPT 的技术/教学/视觉检查不能替代该内容门。课程 2.0 当前只完成批次 0（L3）与批次 1（L4-L6），其余课次仍按 [2.0 改版计划](../docs/course-2.0-plan.md) 推进。四次研究门名称、条件与 100% 评分结构已对齐权威课程文件，但最终发布仍需教师复核、实际 Microsoft PowerPoint/教室投影检查和发布里程碑。

## 文件类型

每次课原则上包含以下材料：

| 文件 | 使用者 | 内容边界 |
| --- | --- | --- |
| `teaching-plan.md` | 教师 | 教学目标、90 分钟流程、课堂活动、演示脚本、时间控制和课后复盘 |
| `handout.md` | 学生 | 可独立阅读的正式讲义，包含概念、方法、案例、练习、术语和延伸阅读 |
| `slides.md` / `slides.pptx` | 课堂展示 | 中文为主的逐页内容母稿与现行可编辑 PPT；尚无现行 PPT 时不放置过时占位文件 |
| `activity-*` | 教师与学生 | 课堂练习、反馈卡、rubric、示例输入和参考答案 |

## 试讲材料

名称中含 `trial-lecture` 或“试讲”的文件只用于开课评审和历史追踪，不能直接视为正式讲义或正式课堂 PPT。试讲关注课程价值和整体结构；正式教学材料必须围绕单次课的学习目标、方法深度、案例和学生练习重新制作。

## 第 1 课

- 现行材料与门控状态统一从 [第 1 课内容入口](./lesson-01/README.md) 查看，避免在两处重复维护版本号。
- 旧 39 页 PPTX 已归入 [PPT 试制里程碑](../archive/ppt-experiments/lesson-01/2026-07-30-pre-gate-39-page-baseline/decision-record.md)；现行 34 页正式课件见 [slides.pptx](./lesson-01/slides.pptx)。
- 2026-07-07 的详细教学包与旧详细讲义已迁入 [被替代文稿归档](../archive/superseded-docs/lesson-01/)，不参与现行制作。
- [教师文献精读卡集](./lesson-01/reading-notes.md)：第 1 课涉及 8 份文献按 AI 辅助阅读协议产出的精读卡；原文定位已完成，待教师复核与定稿。

## 第 2 课

- 现行材料与门控状态统一从 [第 2 课内容入口](./lesson-02/README.md) 查看。
- 现行 30 页正式课件见 [slides.pptx](./lesson-02/slides.pptx)，已通过技术、教学与视觉检查；P29 为独立知识点总结。

## 第 3 课

- 现行材料与门控状态统一从 [第 3 课内容入口](./lesson-03/README.md) 查看。
- 现行 21 页正式课件见 [slides.pptx](./lesson-03/slides.pptx)，已通过技术、教学与视觉检查。

## 第 4 课

- 现行材料与门控状态统一从 [第 4 课内容入口](./lesson-04/README.md) 查看。
- 现行 18 页正式课件见 [slides.pptx](./lesson-04/slides.pptx)，已通过技术、教学与视觉检查；封面只保留正式课名，P17 为独立知识点总结，P18 为退出卡与第 5 课预告。

## 第 5 课

- 现行材料与门控状态统一从 [第 5 课内容入口](./lesson-05/README.md) 查看。
- 现行 21 页正式课件见 [slides.pptx](./lesson-05/slides.pptx)，已通过技术、教学与视觉检查；封面只保留正式课名，P20 为独立知识点总结，P21 为退出卡与第 6 课预告。

## 第 6 课

- 现行材料与门控状态统一从 [第 6 课内容入口](./lesson-06/README.md) 查看。
- 现行 22 页正式课件见 [slides.pptx](./lesson-06/slides.pptx)，已通过技术、教学与视觉检查；封面只保留正式课名，P20-P22 依次为知识点总结、提交/回退、退出/第 7 课预告。

## 第 7 课

- 现行材料与门控状态统一从 [第 7 课内容入口](./lesson-07/README.md) 查看。
- 现行 17 页正式课件见 [slides.pptx](./lesson-07/slides.pptx)，已通过技术、教学与视觉检查；P16 为独立知识点总结。

## 第 8-16 课

| 课次 | 页数 | 现行入口 | PPT 文件 |
| --- | ---: | --- | --- |
| 8 | 15 | [README](./lesson-08/README.md) | [slides.pptx](./lesson-08/slides.pptx) |
| 9 | 21 | [README](./lesson-09/README.md) | [slides.pptx](./lesson-09/slides.pptx) |
| 10 | 17 | [README](./lesson-10/README.md) | [slides.pptx](./lesson-10/slides.pptx) |
| 11 | 20 | [README](./lesson-11/README.md) | [slides.pptx](./lesson-11/slides.pptx) |
| 12 | 21 | [README](./lesson-12/README.md) | [slides.pptx](./lesson-12/slides.pptx) |
| 13 | 20 | [README](./lesson-13/README.md) | [slides.pptx](./lesson-13/slides.pptx) |
| 14 | 18 | [README](./lesson-14/README.md) | [slides.pptx](./lesson-14/slides.pptx) |
| 15 | 17 | [README](./lesson-15/README.md) | [slides.pptx](./lesson-15/slides.pptx) |
| 16 | 20 | [README](./lesson-16/README.md) | [slides.pptx](./lesson-16/slides.pptx) |

九套课件均继承交大 master/layout 与品牌系统；逐课关键页规格、来源 notes、技术/教学/视觉检查及剩余授课现场风险见各课 README 与 `.work/ppt/lesson-NN/` QA 台账。

## 备课复盘

- [备课教训与待验证假设](./备课教训.md)：记录可复用的课程设计结论、前两课尚待课堂检验的节奏判断和逐课制作检查项。
- [博士助教课前审阅与桌面推演协议](../docs/ta-review-guide.md)：统一学生路径试走、真实课题试填、三层失败归因、关键课次推演和现场检查的反馈格式。

## 制作顺序

1. 先确定该课在 [课程大纲](../course/syllabus.md) 中的目标和项目产出。
2. 对齐正式讲义、教师教案和逐页内容母稿，确认只有一套现行规则、案例与来源口径。
3. 做 90 分钟桌面推演，检查每段时间、第一次学生动手时间、最小课堂产出与备用路径。
4. 建立逐页映射：每页写明页面任务、内容母稿位置、证据角色和学生动作。
5. 前三项通过后再制作正式 PPT；不以历史稿、试讲页或视觉样张为内容母版。
6. 渲染并重新打开检查 PPT，同时验证课堂活动材料；技术通过、教学通过和视觉通过分别记录。
