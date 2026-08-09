# 第 3 课内容入口（MOC）

> 文献检索与证据角色。本文件是第 3 课所有材料的导航入口，说明各文件角色、关系与阅读路径。门控流程见 [prepare-course-lesson skill](../../.agents/skills/prepare-course-lesson/SKILL.md)。

## 文件清单

| 文件 | 角色 | 用途 |
| --- | --- | --- |
| [handout.md](./handout.md) | 现行·学生正式讲义 v1.2.0 | 面向学生、可脱离课堂独立阅读：可复盘检索、证据角色四类、角色/状态/决定三分、入口核验、三类记录和候选文献表 |
| [teaching-plan.md](./teaching-plan.md) | 现行·教师教案 v1.1.0 | 90 分钟流程、PPT 执行索引、演示脚本、课堂产出验收、讲后复盘 |
| [slides.md](./slides.md) | 现行·逐页母稿 v0.5.0（20 页） | 逐页屏显文案、视觉结构、讲述备注、互动、时间、来源与事实边界 |
| [slides.pptx](./slides.pptx) | 待同步·上一版课堂 PPT（20 页） | 对应 v0.4.0 母稿；P05-P19 相关内容页须重建并重新执行三重检查 |
| [keystone-design-spec.md](./keystone-design-spec.md) | 规范 v1.2.0 | 10 个风险触发关键页的设计契约、模板例外与制作约束 |
| [source-audit-demo.md](./source-audit-demo.md) | 现行·教学资产 v1.1.0 | Keshav 2007 真实 Crossref—DOI—原文—候选表 trace，含断网备用记录 |
| [mi-search-trace-demo.md](./mi-search-trace-demo.md) | 现行·教学资产 v0.1.1 | MI 宽泛主题检索真实 trace：分支确定方法审计、17 条待筛选线索、4 条幻觉引用 rejected 实例；方向收敛段待真实方向指认后升版 |
| [assets/](./assets/README.md) | 现行·2.0 视觉资产 | 4 张自绘教学结构图，逐图出处块登记；课级唯一图源 |
| [research-question-to-search skill](../../.agents/skills/research-question-to-search/SKILL.md) | 教学工具资产 | “问题初稿→检索式→公开源检索→入口核验→筛选/审计/候选表”受限流程；v1 仅学术文献，含确定性公开源脚本与三端入口；不属三件套，不参与本课门控 |

## 文件关系

- **三件套（口径唯一）**：`handout.md`（教什么）↔ `teaching-plan.md`（怎么教）↔ `slides.md`（逐页屏显）。讲义是内容源，教案不替代讲义，slides 不自造事实。
- 贯穿案例承接第 1 课"结构化阅读卡与 AI 摘要遗漏率"，与第 1-2 课项目工件衔接。
- 检索、筛选、审计和候选文献表统一写入个人项目 `notes/literature-search.md`；第 4 课把已完成入口核验的论文写入 `reading-cards.md`，第 5-6 课继续回写。

## 关联课程文档

| 本课文件 | 对应 `course/` 权威源 |
| --- | --- |
| handout / slides | [syllabus.md](../../course/syllabus.md)、[curriculum.md](../../course/curriculum.md) |
| teaching-plan（提交/门） | [assessment.md](../../course/assessment.md)、[assignments.md](../../course/assignments.md) |
| slides（视觉规则） | [ppt-quality-gates.md](../../course/ppt-quality-gates.md)、[ppt-design-criteria.md](../ppt-design-criteria.md) |
| 跨文档同步 | [sync-rules.md](../../course/sync-rules.md) |
| 阅读书目 | [reading-list.md](../../course/reading-list.md) 第 3 课 |

## 阅读路径

- **学生**：`handout.md` → `course/reading-list.md` 第 3 课
- **教师**：`teaching-plan.md` → `slides.md` → `course/ppt-quality-gates.md`
- **维护者**：`AGENTS.md`（项目根）→ [备课规划.md](../备课规划.md) → 本 README → 各文件

## 门控状态（2026-08-07）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 通过（取自 备课规划 第 3 课目标段；八阶段定位阶段四"外部输入摄取"） |
| 2. 内容门 | ✅ 通过（三件套统一四态与进入规则；P13-P15 使用真实 Keshav 2007 trace，P16 虚构失败案例屏显/notes 双标；正式讲义与教案状态已转现行） |
| 3. 90 分钟教学门 | ✅ 通过（P02 约 2:30 首次短互动；P18 48:00 开始 27 分钟持续实践；最低产出为 1 条检索记录 + 2 条审计 + 1 条已核验候选记录 + 1 条 AI 记录；断网备用路径使用 source-audit-demo.md） |
| 4. 逐页映射门 | ✅ 通过（20 页映射表已复核，每页标 handout 小节；无合并故无行变更；90 分钟表页码列同步） |
| 5. PPT 制作 | ✅ 完成（20 页正式 PPT；继承交大模板母版、版式、字体与品牌元素；每页含 `[Sources]` speaker notes） |
| 6. 三重检查 | ✅ 通过（技术：20/20 notes、模板层级、画布边界 0 越界、LibreOffice 重开导出 20 页；教学：与 8 段 90 分钟节奏、课堂产出和逐页母稿一致；视觉：全页 contact sheet 与高风险页复核通过） |
| 7. 里程碑归档 | ✅ 无需单独归档（本次为首个正式版本，现行 `slides.pptx` 直接作为正式基线） |

## 授课前复核

- 复核 Crossref 和滑铁卢大学公开 PDF 链接可访问；若不可访问，使用 `source-audit-demo.md` 的已核验记录，不伪造现场检索。

## 门控状态（2.0 批次 0 骨架轮，2026-08-08）

修订轮登记（依据 prepare-course-lesson skill"修订已有课次"条款；上方 2026-08-07 原表保留不动）：

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 复核通过（学习目标未变，八阶段定位未变） |
| 2. 内容门 | ✅ 限定范围重走：handout 嵌 4 图并附出处块 + G5 文本清理；三件套规则、案例与来源口径未变；MI 演示线登记为推迟项 |
| 3. 90 分钟教学门 | ✅ 降级复核（时间结构未变，依修订条款对照既有节奏表核对） |
| 4. 逐页映射门 | ✅ 复核通过（slides.md 未动，20 页映射不变） |
| 5. PPT 制作 | ⏸ 未变更（slides.pptx 维持 v1.0 基线；重建推迟至 MI 素材到位） |
| 6. 三重检查 | ⏸ 未变更（PPT 未重建，原记录有效） |
| 7. 里程碑归档 | ✅ 无需（骨架轮不产生 PPTX 试制件） |

**推迟项清单**（MI 素材到位后的第二阶段补齐）：

- slides.md P13-P16 MI 演示段增改；
- teaching-plan.md MI 演示脚本与断网备用更新；
- slides.pptx 受影响页重建与三重检查重走；
- MI 幻觉引用审计失败实例（≥1 条真实科研失败演示）——素材已到位：[mi-search-trace-demo.md](./mi-search-trace-demo.md) §6（4 条真实 rejected）；剩余工作为将该实例织入 slides/teaching-plan 演示段；
- 批次 0 完整验收（7 项试点标准）与范式冻结 v1；tag `lesson-prep-v2.0-batch0`。

**G5 必要边界清单**（清理前建立、复测逐条复核未误删；基线 26 处→清理后 20 处，削减 6 处）：

- 学术红线：虚构论文 A–E"不对应真实文献、不得引用"；AI 输出不自动成证据（导读、学习目标、§三·4）；
- 审计纪律：不得为达数量把未核验条目升级（§八练习 5）；
- 证据标准：`verified-with-caveat` 不得单独支撑 `stable`（§四·3，与 material-contracts 镜像）；冲突证据双方保留（§三要点 3，已转肯定式）；证据角色表"不能做什么"列属证据边界定义（§三）；
- 范围限定：延伸阅读"不要求 CS/AI 项目机械套用"属功能性限定（§十）；
- 术语名：错误分类"来源不可追溯""检索过程不可复盘"（§四·1、§六）；
- 事实性判定与对仗点睛保留：§一"不是…而是"（课定位）、§四·3"不是'大概正确'"（caveat）、导读/§二·1/§四·4 事实性否定判断。

## 门控状态（2.0 口径校正轮，2026-08-09）

| 门 | 状态 |
| --- | --- |
| 1. 课次目标 | ✅ 复核通过；明确八阶段为方法链，学生以问题初稿进入本课 |
| 2. 内容门 | ✅ 通过；三件套统一角色/状态/决定、L3/L4 边界、三类记录和十字段候选表 |
| 3. 90 分钟教学门 | ✅ 通过；页数与八段时间不变，最低产出数量不变 |
| 4. 逐页映射门 | ✅ 通过；P05-P19 相关页已同步母稿并登记映射 |
| 5. PPT 制作 | ⏸ 待同步；现有 PPTX 对应上一版母稿 |
| 6. 三重检查 | ⏸ 待新 PPTX 完成后重走 |
| 7. 里程碑归档 | ⏸ 本轮不产生新 PPTX |

制作顺序与材料状态表见 [lessons/README.md](../README.md)。
