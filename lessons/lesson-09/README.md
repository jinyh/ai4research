# 第 9 课内容入口（MOC）

> Baseline、实验规格、可复现性与判断门。本文件是第 9 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生讲义 v0.4.1 | 公平 baseline、完整实验规格、可重运行记录和判断门边界；统一阅读卡实验口径 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.6.1 | 整数分钟合计 90；完整工程规格集中在本课，个人实践分段并含中点点评 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.7.2（21 页） | P07 虚构反例与 P18 文件树／宽注释重排已同步；原生复核通过 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.2.0 | 13 个风险触发关键页的四字段契约、模板例外与验收约束 |
| [slides.pptx](./slides.pptx) | 现行·课堂 PPT v0.7.2（21 页） | 技术、教学、全尺寸视觉与 PowerPoint 原生检查分别通过；正式发布仍依课程发布门 |
| [assets/reproducibility-example/](./assets/reproducibility-example/) | 现行·真实可运行教学工件 | 合成输入上的七字段 `experiment-spec.md`、实际 `config.json`、复算脚本、`results.json` 与 `run-log.jsonl`；P11 真实工件锚点，不作为实证结论 |

## 封面与收束修订轮（2026-08-20）

- 90 分钟总时长不变；P20 总结 4 分钟，P21 提交/回退/退出/预告 8 分钟。
- 21/21 notes 含来源块，布局 0 越界，Office 校验与 LibreOffice 重开通过；封面、P20-P21 已做视觉检查。

## 课程减负与完整规格集中轮（2026-09-12）

- 同一批 20 篇论文分别进入两个条件，每条件运行 3 次，共 120 次输出；指标、H1/A1/A2/A3 与结果三态统一；
- 课堂最低产出收敛为公平 baseline 和一条可重运行记录，模板迁移与判断门其余材料课后补全；
- 内容、90 分钟教学和逐页映射门已通过；PPTX 已完成视觉提升与包级、教学、全页视觉及 Microsoft PowerPoint 原生复核。

## 判断门九项条件同步轮（2026-08-22）

- 内容门：同步 [assignments.md](../../course/assignments.md) v2.2.0 已批准的真实失败记录条件；第八项要求记录已经遇到的执行失败或已经放弃的备选方案，原模板迁移顺延为第九项。
- 90 分钟门：总时长与六段结构不变；P15 快速参考、P17-P18 持续实践、P19 同伴互查中补入事实失败记录。
- 逐页映射门：仍为 21 页；P02/P03/P15/P17-P19/P21 与讲义、教案和权威门条件同步。
- PPT 与三重检查：21 页正式 PPTX 已重建；当前验证结果见本文末“正式 PPT 验证记录”。

## 文件关系

### 学生入口呈现增强轮（2026-08-22）

- 门 1 与内容门已复核通过：只把复现工件目录入口改为具体 `README.md` 链接，判断门条件、案例事实和来源边界不变。
- 90 分钟教学门、逐页映射门、PPT 制作与三重检查不受影响，沿用下方既有通过记录；本轮不修改 `teaching-plan.md`、`slides.md` 或 `slides.pptx`。
- 待延后项：无；复现工件在具体授课设备上的运行结果仍由助教按审阅协议记录。
- 上述说明只描述“学生入口呈现增强轮”；同日稍后的“判断门九项条件同步轮”已按新权威条件修改三件套与 PPT。

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 承接第 7 课机制假设与实验规格草图：本课把第 7 课的"假设—指标—实验—可能结论映射"和变量清单草案补全为七字段完整规格，把 J1 研究判断补出 J2。
- 承接第 8 课同伴反馈：本课把结构化反馈逐条记录为采纳、澄清、补证、保留异议或暂缓，并写明理由与回写位置，作为判断门条件之六的提交材料。
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

## 历史门控状态（2026-08-22）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 `备课规划.md` 第 9 课目标段；八阶段定位阶段六"研究判断成案"+阶段七"原型验证起始"，承接第 7-8 课，向第 10 课受限 Agent 输出） |
| 2. 内容门 | ✅ 通过（三件套对齐；判断门以 assignments.md 为唯一条件源；随机化/重复为条件性或等价复现口径；前瞻失败预案与已经发生的失败/放弃备选记录分开；真实来源与虚构教学工件分层） |
| 3. 90 分钟教学门 | ✅ Re-fit 通过（`备课规划.md` 第 9 课权威五段与 slides v0.5.0 对齐；P14-P16 在 36-40 分钟完成快速参考，P17-P18 覆盖 40-60 分钟持续个人实践；课堂最低产出=experiment-spec 七字段 + 复现说明 + J2 + 同伴反馈处理 + 最大风险预案 + 已遇失败/放弃备选记录；模板迁移和九项自查课堂内启动、课后完成；无执行环境时使用 Markdown/纸面完成同一工件） |
| 4. 逐页映射门 | ✅ 复核通过（21 页映射表已复核，每页标 handout 小节；同一 handout 小节被多页引用已标注角色区分——P07/P11 共引 §四·1、P15/P19 共引 §六·2；页码列与 90 分钟节奏表同步；待教师桌面推演后定稿） |
| 5. PPT 制作 | ✅ 通过（21 页正式 `slides.pptx` 已完成；使用 `@oai/artifact-tool`，逐页映射第 7 课正式课件模板页，保留 master/layout、校徽、红色标题带、主题字体、品牌图形与页码；13 个关键页按 `keystone-design-spec.md` 契约制作） |
| 6. 三重检查 | ✅ 通过（技术：画布越界 0、空 placeholder 0、默认 prompt 0、21/21 notes 含 `[Sources]`；教学：21 页与 `slides.md` P01-P21、0-90 分钟节奏、40 分钟首次持续个人补全、判断门 9 项条件一致；视觉：逐页原尺寸与 contact sheet 复核，LibreOffice 从最终磁盘路径重开后导出 21 页 PDF 并再次渲染，P15/P17/P18/P19/P21 高风险页通过） |
| 7. 里程碑归档 | ✅ 已决定（本次为第 9 课首个正式版本，现行 `slides.pptx` 作为正式基线；构建、模板审计和 QA 证据保存在 `.work/ppt/lesson-09/2026-08-07-formal-build/`，不另建重复归档副本） |

## 历史准备记录（旧页号与时间安排不再适用）

- **判断门条件对齐**：handout §六·2 的 9 项门条件与 [assignments.md](../../course/assignments.md) Checkpoint 2 逐项对齐，已核对一致：
  1. 可执行 baseline 或最小验证原型 ↔ 条件之一
  2. 数据、材料、评价指标和使用限制说明 ↔ 条件之二
  3. 环境、配置、随机种子或等价复现条件 ↔ 条件之三
  4. ≥2 条研究判断（取舍理由、适用边界、依据、待验证状态）↔ 条件之四
  5. 实验规格完整（假设对应、变量、步骤、度量标准、对照、停止条件）↔ 条件之五
  6. 第 8 课同伴反馈处理记录 ↔ 条件之六
  7. 当前最大风险和失败预案 ↔ 条件之七
  8. 已遇执行失败或已放弃备选记录（发生条件、处理方式、回写位置）↔ 条件之八
  9. 迁移到完整项目模板，不丢失 AI 使用记录和伦理说明 ↔ 条件之九

  提交方式（链接/tag/压缩包）、未通过处理（一周内修订、不扣重分）和评分维度（"实验设计与可复现性"30%）均对齐。待教师在正式提交前复核。
- `备课规划.md` 第 9 课段权威 5 段逐时间表已纳入（slides v0.5.0 节奏表对齐，旧"未给逐时间表"口径已清除）；
- 演示用第 7 课实验规格草图（贯穿案例：自由摘要 vs 阅读卡摘要，七字段草案）需在授课前准备实际可投屏版本；
- 演示用"不可复现实验"反例（缺种子、单次运行、baseline 不公平）需在授课前准备；
- 演示用 experiment-spec.md 完整版样例（七字段填满 + 复现说明 + J2 + 同伴反馈处理 + 失败预案 + 已遇失败记录）需在授课前准备可投屏版本；
- starter-template → project-template 迁移对照表可投屏版本；
- 21 页密度已按 0-90 分钟节奏完成正式 PPT 验收；课堂实授后再依据停留时长与后排可读性决定是否迭代，不在本轮预先删页；
- 与第 10 课的衔接点：实验规格中"哪些步骤拟用 Agent、哪些步骤必须人工"是否在 slides P21 进一步细化；
- 贯穿案例是否需要在第 7-9 课之间保持一致（当前沿用第 1 课证据追踪表 / 第 5 课结构化阅读卡 / 第 7 课实验规格草图同一案例族）；
- [project-template.md](../../course/project-template.md) v1.1.0 已补齐实验规格七字段、研究判断影响工件与 Agent trace 路径；本课迁移说明已据此对齐。

制作顺序与材料状态表见 [lessons/README.md](../README.md)。

## 正式 PPT 验证记录（2026-08-22，历史）

- 页数：21；画布：16:9。
- 最终文件 SHA-256：`61de826d1175dd3637c5154bd8b040dea8695f336904b109d25b8c1c28715cbc`。
- 模板跟随：源为 `lessons/lesson-07/slides.pptx`；模板保真检查通过，0 issues。
- 结构检查：21 张 slide、21 张 notes、21 个 `[Sources]` 块；空结构 placeholder 0；默认 prompt 0。
- 边界检查：21 页 layout JSON 画布越界 0；未发现标题异常换行、正文裁切、品牌遮挡或空白页。
- 重开检查：LibreOffice 从最终 `slides.pptx` 重开并导出 21 页 PDF，逐页重新渲染；P15 九项门条件、P17-P18 实践停留、P19 互查、P21 收束均可读。
- 构建与 QA 证据保存在 `.work/ppt/lesson-09/2026-08-22-cp2-nine-condition-sync/`，不纳入 Git。

剩余风险：尚未在实际授课电脑、Microsoft PowerPoint 和教室后排投影环境中检查字体替换、动画/切换与可读性；课前仍需打开正式文件做现场复核。演示用实验规格草图、不可复现实验反例与完整样例仍需按教案准备实际可投屏工件。

## 正式 PPT 验证记录（2026-09-12，v0.6.3 历史）

> 本记录已被 v0.7.0 视觉提升版取代，仅保留旧版验证轨迹。

- 页数：21；SHA-256：`d2c54be5f1550d05e0253d75fac75430aa6703b80bf977f8be7770f80208bb2c`。
- 技术：21 张 slide、21 张 notes、21/21 个 `[Sources]` 块；master 1、layout 4、空 placeholder 0；显式教学文字最小 18 pt；包完整性、布局与 Artifact Tool 重开通过。
- 教学：屏显含 20×2×3=120、人工基准标注的限定条件遗漏率及 H1/A1/A2/A3；P19 使用五类真实处理动作且不要求拒绝；P21 只保留提交、回退、第 10 课输入与退出卡。
- 视觉：最终磁盘文件完成全尺寸逐页与 contact sheet 复核；P08/P16/P19/P21 密页已按 18 pt 下限重排；系统安装版 LibreOffice 串行重开并导出 21 页，中文完整。
- 原生检查：Microsoft PowerPoint 已从正式路径发起打开，但因 macOS 锁屏未能完成 Slide Sorter 逐页确认；本项不计通过，也不以 LibreOffice 或 Artifact Tool 结果替代。
- QA：`.work/ppt/lesson-09/2026-09-12-load-revision/`；系统 LibreOffice 证据位于其 `lo-system-final-v2/`。

剩余风险：捆绑 headless LibreOffice 存在同样的微软雅黑错误映射，不能作为兼容验收；Microsoft PowerPoint 原生 Slide Sorter 检查因 macOS 锁屏待完成；实际教室后排投影尚未检查。

## 视觉提升首轮记录（2026-09-12，v0.7.0 历史）

> 首轮包级通过不等同于最终视觉通过；以下记录已由文末 v0.7.2 的实际阅读验收取代。

- 页数：21；SHA-256：`6269410549e61174abf93facdf657955428824da172e87615d02936e8f0f03c6`。
- 技术：21 张 slide、21 张 notes、21/21 个 `[Sources]` 块；master 1、layout 4、空提示文本 0；最终器包完整性、布局与重导入检查通过。
- 教学：90 分钟结构与课堂／课后边界未改；20×2×3=120、人工基准标注的限定条件遗漏率、H1/A1/A2/A3、五类真实反馈动作及第 10 课输入均已核对。
- 视觉：实际标题 30–32 pt；正文 22–24 pt regular；表格／工件 18–20 pt。21 页全尺寸与 contact sheet 逐页检查通过，P11 复现链、P15 九项门条件、P19 反馈处理和 P21 交接页无裁切、遮挡或异常换行。
- QA：`.work/ppt/lesson-09/2026-09-12-visual-upgrade/`；最终渲染 `lesson-09-visual-v6-render/`，联系图 `lesson-09-visual-v6-contact.webp`，包级证据 `package-audit-final/`。
- 原生检查：Microsoft PowerPoint 已完成 21 页原生导出复核，页数与 SHA 匹配；证据为 `.work/ppt/lesson-09/2026-09-12-visual-upgrade/native-checked-01.png` 至 `native-checked-21.png`。LibreOffice 的微软雅黑替换只记兼容风险，不作为 PowerPoint 外观等价证据。

剩余风险：实际教室后排投影尚未完成。

## v0.7.1 原生复核记录（2026-09-12，历史）

- 候选文件名：`lesson-09-visual-v7.pptx`；SHA-256：`107bddfecfb45e061568c06bbdf5659be9a86640dd8f7b537d5df35a6af03388`。
- 修订：P07 明示教学反例／虚构实验记录并统一缺口红色；P09、P19 消除孤立断行；P18 将文件树与三组注释分列，代码保持 18 pt。
- 已通过：最终器包完整性、布局、重导入、全尺寸与 contact sheet 检查，0 finding、0 warning。
- 原生复核结论：未通过；Microsoft PowerPoint 原生导出显示 P18 窄注释列覆盖文件名且注释互相穿行。本候选已由 v0.7.2 取代，未覆盖正式 PPTX。

## 当前验收（2026-09-12，v0.7.2）

- 文件：现行 `slides.pptx`，21 页；SHA-256 `19b2fcbef19c44fa5396f169602a5a2736453c8922eb7ef89d6f1a19ad347ce6`。
- 修订：只重排 P18；取消窄注释列，右侧保留纯文件树，判断／规格／日志三条说明移到文件树下方的横向宽行，底部总结下移，代码与注释保持 18 pt。
- 文件与技术：最终器包完整性、布局、重导入检查通过；1 个交大原生 Master、4 个 Layout、主题、页码和 21/21 个来源 notes 保留。
- 实际字体与对象：标题 30–32 pt、常规正文 22–24 pt regular，代码与注释 18 pt；文件树、文字及注释可编辑。
- 教学表达：21 页及整数 90 分钟结构不变；实验口径、九项判断门、反馈动作与第 10 课输入一致；P07 的虚构身份和 P18 的文件对应关系清晰可见。
- 视觉效果：21 页全尺寸与 contact sheet 复核；最终同 SHA 文件经 Microsoft PowerPoint 重开、原生导出 21 页，最终 P18 再次核验无文件名覆盖或注释穿行。
- 证据目录：`.work/ppt/lesson-09/2026-09-12-visual-upgrade/`；原生逐页图 `native-checked-01.png` 至 `native-checked-21.png`，总览 `native-contact.webp`。
- 剩余风险：教室后排投影与其他系统的字体替换尚待现场复核；不把 LibreOffice 渲染等同于 PowerPoint 外观。
