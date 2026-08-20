# 第 14 课内容入口（MOC）

> 论文式写作、证据回写与 AI 使用披露。本文件是第 14 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.1.2 | 面向学生、可脱离课堂独立阅读：论文式写作结构（IMRaD/可追溯叙事、基本论证单元、贡献列表、主题位重音位）、证据回写（结论追踪表、不选择性删除失败、从验证门材料到论文段）、AI 使用披露（七字段、AI 输出只作线索）、引用与署名规范、贯穿案例动作链、论证门条件预演（对齐 assignments.md Checkpoint 4 之 10 项）、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.2.3 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.3.0（18 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.0.1 | 视觉基线、叙事弧、P01/P08/P11/P13/P14/P16 四字段契约与验收边界 |
| [slides.pptx](./slides.pptx) | 正式课堂 PPT（18 页） | 封面只保留课程大纲正式课名；第 15 课预告前含独立知识点总结；逐页 speaker notes 含 `[Sources]` |

## 2026-08-20 课件修订

- 封面标题按课程大纲改为“第14讲 论文式表达与回写”，并上移至两条横线之间。
- 新增 P16“本讲知识点总结”，原预告与阅读页顺延为 P17-P18；总页数 17→18。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 13 课验证门产出：本课把第 13 课的评价报告、证据充分性、威胁有效性、失败审计回写为论文结果段与讨论段。
- 承接第 9 课判断门材料：本课把第 9 课实验规格、研究判断、baseline 用作论文方法段和结论追踪表的上游研究判断字段。
- 承接第 12 课工作流说明：本课把第 12 课任务契约、Context、权限、可演示原型用作论文方法段的工作流边界。
- 为第 15 课同行评审铺垫：本课产出的论文式短文初版、结论追踪表、AI 使用披露段是第 15 课同行评审的直接输入。
- 为第 16 课论证门预演：本课做 Checkpoint 4 论证门条件预演，发现缺口留给第 15-16 课补全；本课非正式提交门。
- 本课非提交门（[assignments.md](../../course/assignments.md) 第 14 课行："将证据、实验和研究判断回写为论文式短文"，无正式提交列）。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)（"表达、伦理与复盘"维度，20%）、[assignments.md](../../course/assignments.md)（Checkpoint 4 论证门条件——本课预演，第 16 课正式提交） |
| handout（AI 使用披露口径） | [AGENTS.md](../../AGENTS.md) 证据标准与 AI 使用披露口径、[assessment.md](../../course/assessment.md) 学术规范红线 |
| handout（论文式短文字段） | [project-template.md](../../course/project-template.md) §9 报告与论文式短文 |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 14 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 14 课 → 课后准备第 15 课同行评审
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 备课规划 第 14 课目标段；八阶段定位阶段八"回写与表达"，承接第 13 课验证门，向第 15 课同行评审输出） |
| 2. 内容门 | ✅ 通过（三件套已对齐口径；讲义为内容源；Checkpoint 4 十项、AI 使用披露七字段、AI 输出仅作线索、失败与冲突证据不选择性删除、`stable` 双独立证据原则以及第 15 课衔接均已复核） |
| 3. 90 分钟教学门 | ✅ 通过（已对齐备课规划第 14 课权威 5 段时间表 0-15/15-35/35-60/60-78/78-90；页量预算 17 页；第一次学生动手 35 分钟；最小产出与备用路径明确） |
| 4. 逐页映射门 | ✅ 通过（17 页映射表已复核，每页标 handout 小节；页码、教学活动、学生动作、证据边界与 90 分钟节奏同步） |
| 5. PPT 制作 | ✅ 通过（17 页；以第 7 课正式课件为模板基线，经 source inventory → frame map → starter → Artifact Tool 编辑流程生成；保留 1 个 master、4 个 layout、交大校徽/红标题带/页脚/页码；17/17 页 notes 含 `[Sources]`） |
| 6. 三重检查 | ✅ 通过（技术：17/17 页、0 越界、0 空 placeholder、0 默认提示词、模板保真 0 问题；教学：逐页对照 handout/slides、Checkpoint 4 十项与第 15 课衔接；视觉：逐页 Artifact Tool 渲染与接触表复核，P13 二行流程定位已修正；最终磁盘文件经 LibreOffice 重开并导出 17 页 PDF 复渲染） |
| 7. 里程碑归档 | ✅ 已判断（本课沿用第 7 课已确立视觉语言，未形成新的跨课次设计系统，不重复归档到 `archive/ppt-experiments/`；正式文件保留在本课目录） |

## 授课前准备与已关闭项

- **论证门条件对齐**：handout §七 的 10 项门条件与 [assignments.md](../../course/assignments.md) Checkpoint 4 逐项对齐，已核对一致：
  1. 论文式短文完整（问题/方法/实验/结果/局限） ↔ 条件之一
  2. 结果表/图可追溯到证据项/实验 ID/工作流运行记录 ↔ 条件之二
  3. 讨论有效性威胁或等价分析 ↔ 条件之三
  4. 已处理第 15 课同行评审意见 ↔ 条件之四（本课留给第 15 课）
  5. 每个关键结论绑定直接证据+上游研究判断 ↔ 条件之五
  6. `stable` 结论两项独立证据；不满足已降级 ↔ 条件之六
  7. Agent Workflow 有运行说明/权限/评价/失败记录 ↔ 条件之七
  8. 伦理/数据许可/贡献说明/AI 使用披露完整 ↔ 条件之八
  9. 工件状态追踪表与门检查结果一致 ↔ 条件之九
  10. 完成个人展示/复现抽查/课程复盘 ↔ 条件之十（本课留给第 16 课）

  本课非正式提交门（[assignments.md](../../course/assignments.md) 第 14 课行无正式提交列），预演目的是发现缺口。上述 10 项已与 assignments.md Checkpoint 4 逐项复核一致。

- `备课规划.md` 第 14 课权威 5 段时间表已完成对齐（0-15/15-35/35-60/60-78/78-90）；
- 演示用第 13 课 evaluation-report.md 完整版样例需在授课前准备可投屏版本；
- 演示用"流畅但证据断裂的 AI 文本"反例已纳入 PPT P13；授课前只需确认讲述顺序；
- 演示用"AI 使用披露只写声明"反例已纳入 PPT P11；
- 贯穿案例的 IMRaD 骨架、结论追踪表与 AI 使用披露动作链已纳入 PPT P04-P13；
- 论证门条件预演清单 10 项已拆分到 PPT P14（1–5）与 P15（6–10 + 同伴追问），正文均按后排可读字号设计；
- 页数密度：现行母稿为 17 页（旧 P12+P13 合并），已按权威 5 段预算完成桌面推演；
- 与第 15 课的衔接已在 PPT P16-P17 明确为 `report.md` 初版、结论追踪表、AI 使用披露段和反馈处理表；
- 贯穿案例是否需要在第 10-14 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡 / 第 9 课实验规格与 baseline / 第 12 课工作流原型 / 第 13 课评价报告同一案例族）；
- 论文式短文字段是否需要根据本课新增"结论追踪表"和"AI 使用披露七字段"更新 [project-template.md](../../course/project-template.md) §9（当前 §9 报告字段可能未含独立"结论追踪表"和"AI 使用披露七字段"段——可能需要扩展）；
- handout §六贯穿案例的虚构数值（0.18±0.03 vs 0.31±0.04）已在讲义和 slides 明确标注为"虚构教学示例，仅用于课堂演示动作链，不预设真实数值"，与第 13 课一致，待教师在授课前确认是否替换为真实可投屏数值或保留虚构标注。

## 正式 PPT 验证记录（2026-08-07）

- 正式路径：`lessons/lesson-14/slides.pptx`
- 页数：17；文件大小：422841 bytes；SHA-256：`2b7500ef605e26baa0c6d5af427b7d152236c80f4d8ec48df0fab2d46ed1d84d`
- 模板：`lessons/lesson-07/slides.pptx`；源模板 SHA-256：`34bfad2dda3703277b6120dd2afc61c9935eef21e6e1f4002f0d34df711dbc6d`
- 技术检查：master=1，layout=4，media=5；17 个 notes 页，17 个 `[Sources]` 块；空结构 placeholder=0；默认提示词=0；Artifact Tool layout 越界=0；模板保真问题=0。
- 教学检查：17 页标题与 `slides.md` 一致；Checkpoint 4 十项、IMRaD 回写、结论追踪、失败与冲突证据保留、AI 使用披露七字段、`stable` 证据要求和第 15 课输入均有对应页面。
- 最终重开：LibreOffice 从正式磁盘路径重开并导出 PDF；PDF 为 17 页、16:9（960.009 × 540 pt）；逐页复渲染接触表通过。
- 工具说明：内置 `slides_test.py` 因当前运行环境缺少 `numpy` 未能启动；已用 Artifact Tool layout/fidelity、只读 ZIP/XML 审计、逐页渲染与 LibreOffice 重开复渲染完成等价闭环。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
