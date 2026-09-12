# 第 12 课内容入口（MOC）

> Agent/Skill 背后的逻辑与个人工作流设计。本文件是第 12 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生正式讲义 v0.3.1 | 面向学生、可脱离课堂独立阅读：把第 10–11 课同一阅读卡任务升级为可审计工作流，并明确最小原型、trace 与评价前置状态 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v0.4.1 | gate1 定位、整数时长 90 分钟流程、PPT 执行索引、演示脚本、课堂/课后边界 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.5.0（21 页） | gate4 逐页六段；同一任务的对象化工作流契约、最小原型、trace、个人实践与同伴互查 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 现行·关键页设计规格 v1.0.2 | 14 个关键页四字段契约、模板偏离许可与验收边界 |
| [slides.pptx](./slides.pptx) | 现行·课堂 PPT（21 页） | 已依 v0.5.0 母稿完成对象化视觉提升；保留交大原生 Master/Layout、校徽、红标题带、主题字体、页码和 notes |

## 2026-08-20 课件修订

- 封面标题改为“第12讲 Agent/Skill 逻辑与自主 Research Workflow 设计”，并上移至两条横线之间。
- 新增 P20“本讲知识点总结”，原退出卡顺延为 P21；总页数 20→21。

## 修订轮登记（2026-09-12）

### 对象化视觉提升轮（正式）

- 内容与教学：内容口径、课堂最低产出和 90 分钟结构不变；视觉提升教学门复核通过。
- 正式文件：21 页；`slides.pptx`；SHA-256 `08bcdbaecf3bba21299d2853de8cdddd25b7075b2c9385b356a2c768304b266a`。
- 技术检查：包结构与布局 0 finding；1 个 Master、4 个 Layout；21/21 页 notes 含 `[Sources]`；教学文字不低于 18 pt。
- 教学检查：同一工作流从契约、冻结循环升级为最小原型；P14 保持 20×2×3、人工基准与 H1/A1/A2/A3，P16 失败 trace 可直接交给第 13 课。
- 视觉检查：Artifact Tool 全尺寸与联系图已复核；流程线不穿文字中线，人工基准评价保持蓝色，红色仅用于“执行器不可读”等实际风险。
- Microsoft PowerPoint 原生检查：通过；最新正式候选已原生打开、导出并逐页复核，P03 契约、P14 工作流链与 P16 失败 trace 可读。LibreOffice 的字体替换结果不作为本轮通过依据。
- QA：`.work/ppt/lesson-12/2026-09-12-visual-upgrade/lesson-12-visual-upgrade-v5-render/`、`.work/ppt/lesson-12/2026-09-12-visual-upgrade/lesson-12-visual-upgrade-v5-contact.webp`、`.work/ppt/lesson-12/2026-09-12-visual-upgrade/lesson-12-visual-upgrade-v5-validation.json`。

### 课程减负修订轮（2026-09-12，历史；已由本页“对象化视觉提升轮（正式）”取代）

| 门 | 状态 |
| --- | --- |
| gate1 备课规划定位 | ✅ 复核：承接第 10 课受限执行与第 11 课受限循环，向第 13 课评价输出 |
| gate2 内容门 | ✅ 通过：取消“每周证据地图”另起项目；统一同一批 20 篇、两条件各 3 次、120 次输出、人工基准限定条件遗漏率及 H1/A1/A2/A3 |
| gate3 90 分钟教学门 | ✅ 通过：`5+10+10+15+10+5+10+15+10=90`；个人实践为两段各 10 分钟，中间点评 5 分钟 |
| gate4 逐页映射门 | ✅ 通过：现行 `slides.md` v0.4.0 共 21 页，与 handout、teaching-plan 的目标、案例、产出一致 |
| gate5/gate6（历史） | ✅ 已依 `slides.md` v0.4.0 完成 21 页 PPTX；技术、教学和 Artifact Tool 视觉检查通过，终版 Microsoft PowerPoint 原生视觉复检待补；当前验收以本页对象化视觉提升轮为准 |

### 正式 PPT 验证记录（2026-09-12，历史；已由本页对象化视觉提升轮取代）

> 以下为当时事实记录；其中笼统的视觉通过与“锁屏/原生待补”状态不代表当前验收状态。

- 页数与指纹：21 页；SHA-256 `e724befde88cb35461412d5b13bf07af7e37a64495194e0e3ad7e3c46aa6ae98`。
- 技术检查：包结构、Master/Layout 关系和磁盘重开校验通过；21/21 页 notes 含闭合 `[Sources]`；空 placeholder 0；包级 OOXML 审计确认承担课堂阅读任务的正文、表格、提示、风险和动作文字均不低于 18 pt，页码、来源和许可文字按规则豁免。
- 教学检查：屏显与 `slides.md` v0.4.0 一致；在第 10–11 课同一任务上组合最小工作流，不重开项目；课堂产出为可运行或可演示的最小原型，并把课后运行结果直接交给第 13 课评价。
- 视觉检查：已完成 Artifact Tool 全尺寸逐页检查与 contact sheet 检查；修正 P05 顶部标签与说明的几何冲突、缩短 P15 标签后未见裁切、遮挡、异常换行或空可见对象。
- 兼容性检查：最终版经 LibreOffice 无界面导出为 21 页 PDF，提取文本含中文；该结果不替代 Microsoft PowerPoint 验收。字号修订前候选曾在 Microsoft PowerPoint Slide Sorter 检查，中文与版式正常；最终 18 pt 版因 macOS 锁屏未能再次原生复检，待补。
- QA 证据：`.work/ppt/lesson-12/2026-09-12-load-revision/validation-18pt-v3.json`、`.work/ppt/lesson-12/2026-09-12-load-revision/artifact-render-18pt-v3/`、`.work/ppt/lesson-12/2026-09-12-load-revision/libreoffice-18pt/slides-final-18pt-validated-v3.pdf`。

课堂最低产出为工作流契约、模式选择、可运行或可复现演示的最小原型、一条 trace 与失败恢复位置。课后补齐批量运行结果，作为第 13 课直接输入。

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 本课承接第 10-11 课（受限编码、受限循环），把"用一次 Agent"升级为"看懂并设计可审计工作流"。
- 本课为第 13 课验证门铺垫：个人 Agent Workflow 是验证门产出之一。
- 第 11 课的受限循环作为本课“执行循环”输入；其余任务契约、权限、工件、评价与恢复在本课补齐。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md) 第 12 课、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（定位/提交） | [assignments.md](../../course/assignments.md) 验证门条件、[assessment.md](../../course/assessment.md) |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 12 课 |

## 阅读路径

- **学生**：`handout.md` → [第 1 课讲义 §四](../lesson-01/handout.md) → [reading-list.md 第 12 课](../../course/reading-list.md)
- **教师**：`teaching-plan.md` → `slides.md` → [ppt-design-criteria.md](../ppt-design-criteria.md) → [ppt-quality-gates.md](../../course/ppt-quality-gates.md)
- **维护者**：[AGENTS.md](../../AGENTS.md) → [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07，历史；当前 gate5/gate6 以对象化视觉提升轮为准）

- [x] **gate1 备课规划定位**：第 12 课目标、八阶段定位（阶段七原型验证·工作流设计子阶段）、模块归属已对齐 `备课规划.md`、`syllabus.md`、`curriculum.md`。
- [x] **gate2 内容门（通过）**：三件套只有一套现行口径；第 11 课受限循环明确作为第 12 课“执行循环”输入；八要素严格按任务契约 / Context / Memory-状态 / 工具与权限 / 执行循环 / 工件与追踪 / Evals 与人工审核 / 失败恢复组合；Checkpoint 3 十项条件均有本课前置状态与第 13 课完成项；P14 与 P16 的虚构案例均完成屏显与 notes 双标。
- [x] **gate3 90 分钟教学门（通过）**：`teaching-plan.md` §四与 `slides.md` §一逐项对齐 `备课规划.md` 第 12 课权威 8 段；20 页连续覆盖 0-90 分钟；32 分钟开始个人设计，60-78 分钟持续实践与自检；最小产出、故障备用路径、同伴互查和退出卡明确。
- [x] **gate4 逐页映射门（通过）**：20 页逐页标明 handout 小节、页面任务、证据角色、学生动作与建议时间；P03-P08 六页覆盖八要素拆解，P11-P14 覆盖设计，P15-P16 覆盖演示，P17-P18 覆盖实践与八要素自检；P17 时间表述已修正。
- [x] **gate5 PPT 制作（通过）**：20 页正式 `slides.pptx` 已完成；使用 `@oai/artifact-tool`，P01 复用第 7 课封面，P02-P20 复用标准内容页；保留 master/layout、校徽、红色标题带、主题字体、品牌图形与页码；关键页按 `keystone-design-spec.md` 制作。
- [x] **gate6 三重检查（通过）**：技术检查为模板保真 0 issues、画布越界 0、空 placeholder 0、默认 prompt 0、20/20 notes 含 `[Sources]`；教学检查确认 20 页、权威 8 段、32 分钟开始设计、60-78 分钟持续实践、Checkpoint 3 十项前置边界一致；视觉检查完成全卷 contact sheet、关键页原尺寸与 LibreOffice 20 页重开渲染。
- [x] **里程碑记录**：首个正式版本以现行 `slides.pptx` 为基线；构建、模板审计和 QA 台账保存在 `.work/ppt/lesson-12/2026-08-07-formal-build/`，不另建重复归档副本。

## 修订轮登记（2026-08-12，handout v0.2.0，历史）

按 `prepare-course-lesson` skill"修订已有课次"条款登记，原门控记录保留不动：

| 门 | 状态 |
| --- | --- |
| gate1 备课规划定位 | ✅ 复核通过（课次目标与八阶段定位不变） |
| gate2 内容门 | ✅ 重走：handout §2.4/2.5 拆解观察点增 Pi Coding Agent 最小 harness 对照指引，§九延伸阅读新增第 5 条（逐字同步 reading-list v2.2.0 第 12 课新条目），承第 11 课案例顺延为第 6-7 条；新增内容仅分析对象、钉 commit、明确不进学生安装清单；八要素口径与既有案例来源未变 |
| gate3 90 分钟教学门 | ⬇️ 降级复核：学习目标与权威 8 段时间结构不变；新增内容为拆解观察点内的对照指引与课后延伸阅读，不改变 32 分钟开始设计、60-78 分钟实践的课堂节奏 |
| gate4 逐页映射门 | 未变更（未动 `slides.md`，原记录有效） |
| gate5/gate6 PPT 制作与三重检查 | 未变更，原记录有效（未重建 `slides.pptx`） |
| 推迟项 | pi 钉死 SHA 授课前建议用 earendil-works/pi 新仓库路径复核一次（当前经旧路径 badlogic/pi-mono 重定向核验，见 `references/notes/pi-and-prime-agent.md` §10） |

## 待复核项

1. **第 11 课承接**：已复核。第 11 课的任务契约 / Context / 工具权限 / 状态 / 执行循环 / 工件追踪 / Evals / 失败恢复骨架在本课映射为完整八要素；其中受限循环明确只是“执行循环”部分，本课补齐其余设计决定。
2. **演示对象选择**：teaching-plan 与 slides 假设以 AutoResearch 或课程案例池 MCP server 作为拆解对象，需教师圈定并固定 commit/版本。
3. **贯穿案例虚构性标注**：已复核。handout §五、slides P14 屏显、讲述和来源边界均标明“课程虚构教学案例，不预设真实效果”。
4. **页量与节奏微调**：已复核。20 页连续覆盖权威 8 段；P03-P08 共 14 分钟用于拆解，P11-P14 共 18 分钟用于设计，P17-P18 合计 18 分钟用于个人实践与自检；正式 PPT 已通过当前屏幕渲染，实授后再依据停留时长与后排可读性迭代。
5. **阅读书目核验**：Wooldridge & Jennings 1995 与 van der Aalst 2003 的 DOI/链接需在授课前核验有效性；Anthropic *Building Effective Agents* 与 MCP Architecture 须标注为工程经验/协议文档而非经典理论。
6. **验证门条件对齐**：已复核。teaching-plan §七逐条记录 Checkpoint 3 十项条件的本课前置状态与第 13 课完成项；P18 的八要素验收明确不替代运行、评价、影响报告、证据回写与合规更新。
7. **PPT 设计准则**：已完成 `keystone-design-spec.md`；P02/P05/P06/P14/P15/P16 等关键页按四字段契约验收，P14-P16 的虚构案例、工件与 trace 均显式标注。

## 正式 PPT 验证记录（2026-08-07，历史；当前验收以对象化视觉提升轮为准）

- 页数：20；画布：16:9；最终文件 SHA-256：`c458670701b79fdae422e5c71553a585208bbbb7cab9ec28892bd43df18e96a2`。
- 模板跟随：源为 `lessons/lesson-07/slides.pptx`；完整审计源 16 页，模板保真检查 0 issues。
- 结构检查：20 张 slide、20 张 notes、20 个 `[Sources]` 块；空结构 placeholder 0；默认 prompt 0。
- 边界检查：20 页 layout JSON 画布越界 0；未发现标题异常换行、正文裁切、品牌遮挡或空白页。
- 教学检查：P01-P20 与逐页母稿、0-90 分钟权威 8 段、八要素组合、Checkpoint 3 十项前置映射一致；P14 虚构案例和 P15-P16 虚构工件 / trace 均显式标注。
- 重开检查：LibreOffice 从最终 `slides.pptx` 重开并导出 20 页 PDF，逐页重新渲染；P03/P05/P06/P12/P14/P18/P20 原尺寸复核通过。
- 构建与 QA 证据保存在 `.work/ppt/lesson-12/2026-08-07-formal-build/`，不纳入 Git。

剩余风险：尚未在实际授课电脑、Microsoft PowerPoint 和教室后排投影环境中检查字体替换、动画/切换与可读性；课前仍需打开正式文件并固定 AutoResearch 课堂 commit。P15-P16 为虚构教学工件，教师若改用真实演示，必须重新核验权限、数据与来源。
