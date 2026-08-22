# 第 9 课内容入口（MOC）

> Baseline、实验规格、可复现性与判断门。本文件是第 9 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.2.1 | 面向学生、可脱离课堂独立阅读：baseline 选择与公平性、实验规格七字段、可复现最小集合、随机种子与方差、ACM Badging 自查视角、starter→project 模板迁移、判断门提交清单（对齐 assignments.md Checkpoint 2 之 8 项）、练习、术语、延伸阅读 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.4.0 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.4.0（21 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.1.0 | 12 个风险触发关键页的四字段契约、模板例外与验收约束 |
| [slides.pptx](./slides.pptx) | 现行·正式课堂 PPT（21 页） | 封面与收束修订轮已通过技术、教学与视觉检查 |
| [assets/reproducibility-example/](./assets/reproducibility-example/) | 现行·真实可运行教学工件 | 合成输入上的七字段 `experiment-spec.md`、实际 `config.json`、复算脚本、`results.json` 与 `run-log.jsonl`；P11 真实工件锚点，不作为实证结论 |

## 封面与收束修订轮（2026-08-20）

- 90 分钟总时长不变；P20 总结 4 分钟，P21 提交/回退/退出/预告 8 分钟。
- 21/21 notes 含来源块，布局 0 越界，Office 校验与 LibreOffice 重开通过；封面、P20-P21 已做视觉检查。

## 文件关系

### 学生入口呈现增强轮（2026-08-22）

- 门 1 与内容门已复核通过：只把复现工件目录入口改为具体 `README.md` 链接，判断门条件、案例事实和来源边界不变。
- 90 分钟教学门、逐页映射门、PPT 制作与三重检查不受影响，沿用下方既有通过记录；本轮不修改 `teaching-plan.md`、`slides.md` 或 `slides.pptx`。
- 待延后项：无；复现工件在具体授课设备上的运行结果仍由助教按审阅协议记录。

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 7 课机制假设与实验规格草图：本课把第 7 课的"假设—指标—实验—可能结论映射"和变量清单草案补全为七字段完整规格，把 J1 研究判断补出 J2。
- 承接第 8 课同伴反馈：本课把第 8 课的结构化反馈逐条归档为采纳/拒绝/暂缓并写明理由，作为判断门条件之六的提交材料。
- 为第 10 课受限 Agent 铺垫：本课实验规格中标出"哪些步骤拟用 Agent、哪些步骤必须人工"，作为第 10 课任务契约的直接输入。
- 判断门提交指向当前个人项目版本（链接/tag/压缩包），不重复制作汇报文档。从 [starter-template.md](../../course/starter-template.md) 迁移到 [project-template.md](../../course/project-template.md)，字段对齐 project-template §4.2/4.4/4.5/4.6/5/7。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)（"实验设计与可复现性"维度，30%）、[assignments.md](../../course/assignments.md)（Checkpoint 2 判断门条件——权威来源） |
| handout（模板迁移） | [starter-template.md](../../course/starter-template.md)、[project-template.md](../../course/project-template.md) |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 9 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 9 课 → 课后提交判断门材料包
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 `备课规划.md` 第 9 课目标段；八阶段定位阶段六"研究判断成案"+阶段七"原型验证起始"，承接第 7-8 课，向第 10 课受限 Agent 输出） |
| 2. 内容门 | ✅ 通过（三件套对齐；判断门以 assignments.md 为唯一条件源；随机化/重复为条件性或等价复现口径，失败预案对准当前最大风险；真实来源与虚构教学工件分层） |
| 3. 90 分钟教学门 | ✅ Re-fit 通过（`备课规划.md` 第 9 课权威五段与 slides v0.3.0 对齐；P14-P16 在 36-40 分钟完成快速参考，P17-P18 覆盖 40-60 分钟持续个人实践；课堂最低产出=experiment-spec 七字段 + 复现说明 + J2 + 同伴反馈处理 + 最大风险预案；模板迁移和八项自查课堂内启动、课后完成；无执行环境时使用 Markdown/纸面完成同一工件） |
| 4. 逐页映射门 | ✅ 复核通过（20 页映射表已复核，每页标 handout 小节；同一 handout 小节被多页引用已标注角色区分——P07/P11 共引 §四·1、P15/P19 共引 §六·2；页码列与 90 分钟节奏表同步；待教师桌面推演后定稿） |
| 5. PPT 制作 | ✅ 通过（20 页正式 `slides.pptx` 已完成；使用 `@oai/artifact-tool`，逐页映射第 7 课正式课件模板页，保留 master/layout、校徽、红色标题带、主题字体、品牌图形与页码；12 个关键页按 `keystone-design-spec.md` 契约制作） |
| 6. 三重检查 | ✅ 通过（技术：模板保真 0 issues、画布越界 0、空 placeholder 0、默认 prompt 0、20/20 notes 含 `[Sources]`；教学：20 页与 `slides.md` P01-P20、0-90 分钟五段节奏、40 分钟首次持续个人补全、判断门 8 项条件一致；视觉：逐页原尺寸与 contact sheet 复核，LibreOffice 从最终磁盘路径重开后导出 20 页 PDF 并再次渲染，P08/P11/P15/P17/P18/P19/P20 高风险页通过） |
| 7. 里程碑归档 | ✅ 已决定（本次为第 9 课首个正式版本，现行 `slides.pptx` 作为正式基线；构建、模板审计和 QA 证据保存在 `.work/ppt/lesson-09/2026-08-07-formal-build/`，不另建重复归档副本） |

## 待复核项

- **判断门条件对齐**：handout §六·2 的 8 项门条件与 [assignments.md](../../course/assignments.md) Checkpoint 2 逐项对齐，已核对一致：
  1. 可执行 baseline 或最小验证原型 ↔ 条件之一
  2. 数据、材料、评价指标和使用限制说明 ↔ 条件之二
  3. 环境、配置、随机种子或等价复现条件 ↔ 条件之三
  4. ≥2 条研究判断（取舍理由、适用边界、依据、待验证状态）↔ 条件之四
  5. 实验规格完整（假设对应、变量、步骤、度量标准、对照、停止条件）↔ 条件之五
  6. 第 8 课同伴反馈处理记录 ↔ 条件之六
  7. 当前最大风险和失败预案 ↔ 条件之七
  8. 迁移到完整项目模板，不丢失 AI 使用记录和伦理说明 ↔ 条件之八

  提交方式（链接/tag/压缩包）、未通过处理（一周内修订、不扣重分）和评分维度（"实验设计与可复现性"30%）均对齐。待教师在正式提交前复核。
- `备课规划.md` 第 9 课段权威 5 段逐时间表已纳入（slides v0.3.0 节奏表对齐，旧"未给逐时间表"口径已清除）；
- 演示用第 7 课实验规格草图（贯穿案例：自由摘要 vs 阅读卡摘要，七字段草案）需在授课前准备实际可投屏版本；
- 演示用"不可复现实验"反例（缺种子、单次运行、baseline 不公平）需在授课前准备；
- 演示用 experiment-spec.md 完整版样例（七字段填满 + 复现说明 + J2 + 同伴反馈处理 + 失败预案）需在授课前准备可投屏版本；
- starter-template → project-template 迁移对照表可投屏版本；
- 20 页密度已按 0-90 分钟五段节奏完成正式 PPT 验收；课堂实授后再依据停留时长与后排可读性决定是否迭代，不在本轮预先删页；
- 与第 10 课的衔接点：实验规格中"哪些步骤拟用 Agent、哪些步骤必须人工"是否在 slides P20 进一步细化；
- 贯穿案例是否需要在第 7-9 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡 / 第 7 课实验规格草图同一案例族）；
- [project-template.md](../../course/project-template.md) v1.1.0 已补齐实验规格七字段、研究判断影响工件与 Agent trace 路径；本课迁移说明已据此对齐。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。

## 正式 PPT 验证记录（2026-08-07）

- 页数：20；画布：16:9。
- 最终文件 SHA-256：`abeb96ba0b5654ef48865a37e2f9bc7db4d667d028168efa09f81bc10e9b3e7d`。
- 模板跟随：源为 `lessons/lesson-07/slides.pptx`；模板保真检查通过，0 issues。
- 结构检查：20 张 slide、20 张 notes、20 个 `[Sources]` 块；空结构 placeholder 0；默认 prompt 0。
- 边界检查：20 页 layout JSON 画布越界 0；未发现标题异常换行、正文裁切、品牌遮挡或空白页。
- 重开检查：LibreOffice 从最终 `slides.pptx` 重开并导出 20 页 PDF，逐页重新渲染；P08 七字段、P11 复现集合、P15 八项门条件、P17-P18 实践停留、P19 互查、P20 收束均可读。
- 构建与 QA 证据保存在 `.work/ppt/lesson-09/2026-08-07-formal-build/`，不纳入 Git。

剩余风险：尚未在实际授课电脑、Microsoft PowerPoint 和教室后排投影环境中检查字体替换、动画/切换与可读性；课前仍需打开正式文件做现场复核。演示用实验规格草图、不可复现实验反例与完整样例仍需按教案准备实际可投屏工件。
