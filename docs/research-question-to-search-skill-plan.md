---
版本：v1.0.0
最后更新：2026-08-09
文档类型：技能建设提案与执行计划
状态：待执行
变更记录：
- v1.0.0 (2026-08-09): 建立计划——目标、handout 逐节对照、边界、交付注册、执行顺序、验证清单与风险
---

# 计划：`research-question-to-search` skill

## 一、目标

建一个通用检索 skill（`research-question-to-search`）：把任意研究问题/宽泛主题变成可复盘检索式，执行公开源检索，完成身份核验，产出与课程工件格式一致的检索记录和候选文献表行。首个使用者是课程 2.0 批次 0 阶段 A′ 的 MI 检索 trace；长期消费者是任意课次的检索需求与第 12 课八要素拆解分析对象。

建设理由（相对"暂不建 skill"判断的更新依据）：

1. **生产工具**：批次 0 阶段 A′ 的 MI 检索 trace 用它执行——handout §二-§四 方法被 v1.1.0 门控冻结过，是已验证流程，非推测性需求。
2. **教学分析对象**：`references/notes/skills_ref.md` 缺口表指出课程自建必要性；第 12 课八要素拆解框架需要学生能验证真实 trace 的本土 skill，比第三方 skill（co-researcher、ai-research-skills 均未本机核验）更可信，符合"不教安装、教看懂设计逻辑"的课程取向。
3. **第三方候选无法覆盖**：skills_ref.md 所列第三方 skill 均无课程自有的检索纪律（四态、人工判断点、失败留痕）。

## 二、与 handout v1.1.0 逐节对照表

| handout 位置 | skill 对应条款 |
| --- | --- |
| §一 外部输入 7 类 | 论文走学术 API 身份核验；仓库/规范/官方文档/工程文记为线索条目，只做可达性检查，不冒用论文核验流程 |
| §二·1 四要素问题 | 输入契约：宽泛主题 → 四要素收敛建议，问题定稿权在人 |
| §二·2 关键词扩展 | 扩展词来源三分：keywords 字段、综述术语表、AI 候选（标线索，入最终检索式前须回源） |
| §二·3 检索式元素 | 布尔/字段/截断/短语/时间文献类型；记录"库+式+日期"，注明各库语法差异以保复盘 |
| §二·4 纳入排除 | 检索前先出第一版；检索中每次调整连同理由记入迭代日志 |
| §三 证据角色四类 | 角色默认探索线索；主/补/对比需假设上下文且由人工定，附一句理由 |
| §四·1 五类失败模式 | 身份层查虚构、张冠李戴、来源不可追溯；过度概括与限定丢失显式移交精读 |
| §四·2 核验清单 7 项 | skill 执行第 1-2 项并附证据链；第 3-7 项输出为"待精读移交项" |
| §四·3 + material-contracts §三 四态 | 双层核验：身份层（存在性+元数据一致）与主张层（原文任务/结果/限定）。仅过身份层 → `pending`（注明身份已核）；身份失败/张冠李戴 → `rejected`；`verified`/`verified-with-caveat` 须主张层人工确认。状态名精确，禁用 `caveat` 缩写 |
| §四·3 进入规则 | 机械执行：`rejected` 永不入候选表；`pending` 只留线索区且显著标记；`verified-with-caveat` 必须同行携带 caveat+原文位置 |
| §四·4 Keshav 五步 trace | 输出结构镜像：检索键→Crossref→DOI/原文→核对任务→收窄主张（后三步视开放获取与人工参与而定） |
| §五 候选表 10 字段 | 输出行逐字段镜像：编号/题名(核验后)/作者/年份/来源/证据角色/纳入排除/理由/核验状态/caveat-允许主张 |
| §六 常见错误 | 对应纪律：不以主题词代检索式；冲突双方保留不偏支持项；AI 输出只作线索；不设数量目标；全程留记录；来源类型分标 |
| §七 贯穿案例七步 | 执行循环 = 该七步（收敛→抽词→检索式→纳入排除→执行记录→来源审计→按进入规则写表） |
| §八 练习 5 断网规则 | 网络/API 失败只记 trace，不编造离线条目 |

对照中发现并修正的草案问题（v1.0.0 已并入）：

1. §一：外部输入不止论文（7 类）——补非论文来源处理条款；
2. §四·3 + material-contracts §三：`verified` 语义含"主张与原文一致"——身份核验不足以给 `verified`，状态建议收紧为双层规则；
3. §三要点 4：AI 检索结果默认归探索线索——证据角色默认值明确；
4. §二·4：纳入排除"检索前先写、检索中调整"——增迭代日志条款；
5. material-contracts：状态名不得缩写为 `caveat`——skill 使用精确状态名。

## 三、边界（IN / OUT）

**IN**：

- 问题收敛建议：宽泛主题 → 四要素最小问题（对象/干预/比较/指标），人工定稿；
- 检索式生产与迭代记录：抽词、同义/上下位扩展、布尔/字段/短语组合；检索记录七字段（库、检索式、日期、时间范围、命中数、纳入排除、纳入数）；
- 公开 API 检索：Crossref（身份层）、arXiv、OpenAlex、Semantic Scholar、dblp（发现层），命令与响应全存档；
- 非论文来源线索登记与可达性检查；
- 双层核验与状态建议；进入规则机械执行；
- 失败留痕：检索死路（0 命中）、限流、DOI 解析失败记入 trace，不静默重试。

**OUT**（每条有课程内理由）：

| 边界 | 理由 |
| --- | --- |
| 主张层判断代行 | 可呈交摘要/开放全文取证，判断在人；属第 4 课精读职责 |
| 状态升级与纳入排除决定 | handout 练习 5 审计纪律：不得为数量升级未核验条目；第 12 课要拆的"人工审核点"设计 |
| 订阅源自动化（Scopus/WoS/CNKI） | skills_ref.md 已有先例警示：绕过订阅边界涉合规；人工手动检索结果可作为记录项写入，不做自动化 |
| 综述/AI 综合报告生成 | 输出只有结构化记录表；"流畅综合报告"正是第 3 课审计的失败对象，skill 必须站在其反面 |
| 未发表/敏感内容入查询 | 继承 AGENTS.md 未发表素材外部禁令；查询词只来自公开问题描述 |
| Zotero 库管理 | 可查询本地库作核验源（已配 MCP），建集合/导入/去重不属本契约 |
| 研究问题代决 | 问题定稿权在人，skill 只给收敛建议 |

**八要素组织**（第 12 课可直接拆解分析）：任务契约 / Context（引 handout §二-§五 与 material-contracts 为方法源）/ 工具与权限 / 执行循环（handout §七 七步）/ 人工审核点 / 工件与追踪 / 失败恢复 / Evals。

**通用化设计**：

- 输入为任意问题/主题，不内嵌 L3 案例；L3 handout 是方法论引用源，不是硬编码；
- 输出落点可配置：教师演示 trace（lesson assets / source-audit-demo）或个人项目 `notes/literature-search.md`，字段格式统一镜像 handout §五，可直接粘贴；
- 数据源优先级可声明；Semantic Scholar 无 key 限流时按失败恢复条款切 OpenAlex，不静默重试。

## 四、交付与注册

1. `.agents/skills/research-question-to-search/SKILL.md`——单一事实源，frontmatter 仿 prepare-course-lesson（name + 触发式 description，前置关键词"研究问题""检索式""候选文献表""来源审计"）；
2. 三端注册：`.claude/skills/` 软链 + `.opencode/agent/` 薄封装（沿用 prepare-course-lesson 先例）；
3. `docs/tooling.md` "项目 skill" 段登记；
4. `lessons/lesson-03/README.md` 登记为教学工具资产（不属三件套，不触发门控；第 12 课引用留待该课修订轮）。

## 五、执行顺序

1. 写 SKILL.md 与三端注册、tooling.md 登记；
2. **自测（回归测试）**：用 skill 重放 Keshav 2007 既有 trace——预期输出必须与 `lessons/lesson-03/source-audit-demo.md` 已核验记录一致；
3. **首条真实 trace**：MI 宽泛主题检索（命令存档于 `.work/mi-search/`），产出方向地图 + 已核验候选表 → 用户指认博士生真实方向；
4. 用实践摩擦回补 skill（升版留痕）；trace 落点文件届时决定（source-audit-demo.md 双 trace 升版 vs 并列新文件，待用户拍板）。

## 六、验证清单

- SKILL.md frontmatter 合规（name 小写连字符 ≤64 字符，description 覆盖触发场景）；
- Keshav 重放输出与 source-audit-demo.md 字段逐项一致；
- 三端入口可发现（opencode agent 列表含该 skill；软链解析正确）；
- handout 对照表 16 行全覆盖，无悬空条款；
- 不触碰三件套内容口径；git diff 只含计划内文件。

## 七、风险

| 风险 | 缓解 |
| --- | --- |
| Semantic Scholar 无 key 限流（实测 429） | 失败恢复条款：记录+切 OpenAlex，不静默重试 |
| skill 边界与第 4 课职责漂移 | 移交项机制显式输出"待精读项"，主张层判断一律不代行 |
| 通用化导致 L3 课堂演示失焦 | L3 演示仍用 Keshav+MI 手工脚本（teaching-plan 管辖），skill 是生产工具，不进 teaching-plan |

## 关联文件

- [course-2.0-plan.md](./course-2.0-plan.md) §批次 0、§素材收集前置步骤
- [tooling.md](./tooling.md) 项目 skill 段
- `lessons/lesson-03/handout.md` v1.1.0（方法论源）
- `references/material-contracts.md` §三（四态权威定义）
- `references/notes/skills_ref.md`（第三方 skill 线索与缺口表）
- `references/notes/mi-case-registry.md`（MI 素材登记）
