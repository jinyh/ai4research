> **核验状态（2026-07-29 建立；2026-08-08 增补 AERS 候选线索，并批量回源核验新增 skill 库与 MCP 条目）**：本文件为二手整理的 Skills/项目笔记，B/C 级。含 Star 数、skill 数量、平台兼容性等易变信息，授课前回上游仓库核验；不作为 Skills 安装教程或项目质量背书。

**针对计算机系研究生的 “AI for Research” 课程，重点推荐可在 OpenCode、Claude Code 和 Codex（三者均为主流终端/IDE AI coding agent）中复用的 agent skills（以 `SKILL.md` 模块化指令为主）。** 这些 skills 强调方法论（如何判断 gap 是否值得做、文献综合验证、实验设计与可复现、claim-evidence 对齐、peer review 模拟、防幻觉与 attribution），而非单纯工具操作。OpenCode（开源、模型无关）、Claude Code（Anthropic）和 Codex（OpenAI）对 `SKILL.md` 约定有较高兼容性，许多 skills 可跨平台加载（通过对应 skills 目录、symlink 或 plugin）。

### 核心推荐 Skills（跨平台优先 + 方法论强）
以下优先选明确支持或结构兼容三者的，按研究全流程组织：

1. **co-researcher（poemswe/co-researcher）**  
   明确兼容 Claude Code、OpenAI Codex **和 OpenCode**。提供专业研究套件 + 多 agent 编排引擎。  
   **方法论重点**：`research-methodology`（设计选择、验证、 reframing）、`literature-review`（真实数据库如 OpenAlex/arXiv + 引用验证门）、`hypothesis-testing`、`systematic-review`（PRISMA 风格）、`critical-analysis`、`peer-review`、`ethics-review`、`research-synthesis`（含不确定性量化）。支持 Interactive / Auto / Plan-Only 模式，模板覆盖 quick/rigorous/comprehensive。  
   适合课程演示“如何把 AI 作为协作伙伴而非黑箱”，强调 Systemic Honesty 与 citation integrity。

2. **Claude Scholar（及相关 Galaxy-Dawn 版本）**  
   明确支持 Claude Code、Codex CLI **和 OpenCode**（以及 Kimi 等）。半自动化研究助手，覆盖 ideation → literature → experiments → writing 的可追溯 pipeline，集成 Zotero/Obsidian。  
   **方法论重点**：问题到写作的可审计流程，适合教“如何用 AI 管理研究状态与证据链”。

3. **ai-research-skills（WenyuChiou/ai-research-skills）**  
   通用 `SKILL.md` 目录，原生支持 Claude Code / Codex / Gemini / Cursor 等，结构也可用于 OpenCode 类 agent。约 15 个 skills，面向研究生/博后。  
   **方法论核心**：以“这个 research gap 真的值得做吗？”为起点的 **3-gate 决策**（open / contribution / feasibility）→ `gap-to-topic`、`literature-triage-matrix`、`research-design-helper`、`paper-memory-builder`（claim-evidence 审计、anti-hallucination）、`academic-writing-skills`（banned-word、reviewer response）。8 阶段 pipeline 用 YAML/Markdown 机械交接，强制 schema 与 provenance。跨 agent 委托（如 mechanical 任务给 Codex）。  
   非常适合课程讲“方法论判断 + 状态管理 + 防幻觉”。

4. **Deep-Research-skills（Weizhena/Deep-Research-skills）**  
   明确支持 Claude Code / **OpenCode** / Codex，带 human-in-the-loop。两阶段（outline 可扩展 + deep investigation）。  
   **方法论重点**：结构化深度研究控制，适合学术 survey、benchmark review、文献分析，强调每步人工干预点。

5. **academic-research-skills（Imbad0202，高 star）**  
   主要针对 Claude Code（有 Codex 兄弟版），完整 pipeline：research → write → review → revise → finalize，含 citation integrity gates、claim-audit、七模式完整性检查（抓幻觉引用与方法论虚构）。  
   **方法论亮点**：强制验证与可复现质量门，适合演示“AI 生成后必须过的 rigor 检查”。可与其他 skills 组合。

6. **其他高 complementary 选项**  
   - **AI Research Skills 库**（高 star，skill 数量待回源）：把 agent 变成 AI/ML 研究助手（fine-tuning、distributed training、evaluation、RAG、paper writing + autoresearch 层），兼容 Claude Code / Codex 等。适合 CS 研究生的实验与系统部分。  
   - **nature-skills**（上游候选：Yuan1z0825/nature-skills 等社区库族，2026-08-08 回源）：Nature 级写作 + 科研绘图，Claude Code + Codex；社交媒体聚合图中另见 Nature Academic Search / Reader / Figure / Reviewer / Response 等 6 个子 skill 命名，对应该库族，不另立条目。**品牌声明**：此类 "Nature*" 命名为社区自拟，与 *Nature* 期刊无隶属或背书关系，课堂不得表述为期刊认可的标准。  
   - **PaperSpine（WUBING2023/PaperSpine）**：2026-08-08 回源登记，B/C 级线索。动机驱动的强论文学习 skill：构建论文中心论证（central argument）、证据感知蓝图、修订矩阵、LaTeX 安全审计；与第 4 课论文精读、第 15 课修订回写契合。存在个人镜像（PKUMichael/PaperSpine），引用以上游 WUBING2023 为准。  
   - **PaperCraft**：2026-08-08 回源登记，B/C 级线索，**正源待定**。同名仓库多个：charlotte-12s/paper-craft（"从 idea 到顶会接收"，17 规则 + 12 skills，CS 方向）、kimogrant/academic-paper-skill（SCI + 学位论文向镜像）。采用前须确认正源与许可。  
   - **feynman** 等 CLI 研究 agent：20+ skills（文献、复现、peer review），可装进 Codex/Claude。  
   - **scientific-agent-skills（K-Dense-AI/scientific-agent-skills）**：2026-08-08 回源登记，B/C 级线索。大型科研 skill 库，自称 "#1 Agent Skills library for science"。README 称约 158–159 个 skill（About 区与正文数字不一致），按领域组织（生物、化学、临床、数据库、研究方法等），SKILL.md 格式，含脚本的 skill 带测试要求；仓库标 MIT，但 FAQ 声明各 skill 许可独立，采用前须逐个核验。明确支持 Claude Code / Codex / Cursor；**OpenCode 兼容未见页面声明，待回源**。方法论面有文献检索/综述、证据可追溯写作（source-bound、line-pinned citations）、同行评审、假设生成、批判性思维、引用管理，与课程 claim-evidence 对齐和防幻觉要求契合。宣传语（"#1""170,000+ scientists"）不采信。**建议列为首选评估候选**。  
   - **Supervisor-Skills（HKUSTDial/Supervisor-Skills）**：2026-08-08 回源登记，B/C 级线索。港科大（广州）助理教授发起（DIAL 实验室），把导师经验蒸馏为技能：idea-evaluator、deep-research、paper-writer（证据门控正文写作）、paper-polish（忠于原意润色）、pre-submission-reviewer、figure-designer 等；"Guide + Skills" 双轨，强调引用核验、不编造，与课程"方法论判断在人类侧"取向契合。CC BY-NC-SA 4.0（非商业、改编须同许可并注明出处，课堂使用与再分发注意边界）；页面提及 Claude Code/Cursor/Codex 及 Claude、DeepSeek、Kimi 等。  
   - **Research-Paper-Writing-Skills（Master-cai）**：2026-08-08 回源登记，B/C 级线索。ML/CV/NLP 论文写作技能包，内容主要整理自彭思达公开笔记（作者自述为整理与结构化改编；引用须回原笔记核验并注明改编关系）；单一 skill 包（research-paper-writing/）含参考与模板；MIT；支持 Codex/Claude Code/Gemini。领域与 CS/AI 课程契合度高。  
   - **research-writing-skill（Norman-bury）**：2026-08-08 回源登记，B/C 级线索。把论文写作组织为可追踪、可恢复、可复用的工程化协作流程（选题、章节、图表脚本、文献整理、LaTeX、投稿前自审），面向本硕与早期科研人员；MIT；明确支持 Claude Code/Cursor/Codex/OpenCode/Gemini CLI。**注意**：含"去AI化写作"模块，与课程 AI 使用披露规范冲突（同 AERS 的 de-AIGC 问题），只可作为批判性案例，不得在课堂推荐使用。  
   - **AI-Powered-Literature-Review-Skills（stephenlzc）**：2026-08-08 回源登记，B/C 级线索。系统性文献综述 skill（8 阶段：检索策略 → 多库检索 → 去重 → 元数据校验 → 单篇分析 → 综述生成），主打 Kimi CLI，页面称也可装入 Claude Code/OpenCode 等；MIT；GB/T 7714-2015 引文格式贴合国内场景。**注意**：依赖浏览器自动化访问 CNKI/WoS/ScienceDirect/PubMed 而非授权 API，涉及订阅条款与平台规则边界，课堂使用前须说明权限与合规边界，不演示越过订阅边界的访问。  
   - **Auto-Empirical Research Skills（AERS，brycewang-stanford/Auto-Empirical-Research-Skills）**：2026-08-08 回源登记，B/C 级线索。社科实证研究方向的 skill 合集（选题、文献、数据、DID/RD/IV 因果识别、估计与稳健性、图表、写作、投稿），CC BY-SA 4.0，README 自称由 "Stanford REAP × CoPaper.AI" 维护（机构身份未核验）。**纳入理由**：仅作为缺口表"统计严谨/因果推断"维度的候选线索。**三点限定**：①面向社科计量场景，与 CS/AI 课程契合有限，不进核心推荐；②含 "de-AIGC"（降低 AI 痕迹）类 skill，与课程 AI 使用披露、人主智辅与诚信规范直接冲突，课堂上只可作为"哪些 skill 不该用"的批判性案例，不得推荐使用；③README 宣传口径不可靠（"23,000+ skills"与正文"1,096"不一致、"20 分钟完成一篇论文"式承诺），按使用规则不采信、不记录。  
   - 社区聚合与发现入口：Auto-Research-Skills hub、awesome-skills；**InternScience/Awesome-Scientific-Skills**（科研 skill 精选目录，MIT，有筛选标准与 skill-metric 质量评估，当前以链接目录为主，2026-08-08 回源）；**kael-odin/awesome-academic-research-skills**（中文学术 skill 仓库每日榜单/雷达，MIT，GitHub Actions 自动抓取，适合作为发现新库的线索而非直接依据，2026-08-08 回源）；**HughYau/AcademicForge**（学术 skill 选配安装平台，32 个技能偏生命科学与算力方向，MIT，自称跨 Claude Code/OpenCode/Codex，2026-08-08 回源）；VoltAgent/awesome-agent-skills（通用大合集，1400+ skill，无科研专门分类，与本课程相关度低，2026-08-08 回源）。建议课程精选上述核心，避免 overload。

**社媒聚合图核对注记（2026-08-08）**：就一张小红书博主截图（"科研人必备的14个codex skills"，C 级社媒线索，截图不入库）逐项回源：Nature* 系对应 nature-skills 条目，Scientific* 系对应 K-Dense scientific-agent-skills，"AI Research Skill" 对应 AI Research Skills 库，"Literature Survey" 与现有条目重叠——四类均不另立；PaperSpine 与 PaperCraft 为新登记（见上）。图内点赞/收藏等宣传数据不记录；该图仅作核对线索，不构成课程证据。

**跨平台使用提示**：多数采用 `SKILL.md`（name + description frontmatter + 正文）。Claude Code 用 `.claude/skills/` 或 marketplace；OpenCode 可读 `.opencode/skills/`、`.claude/skills/` 等；Codex 用 `.agents/skills/`（可 symlink）。安装后通常用自然语言触发或 slash/`$` 命令。始终强调本地/隐私配置与 API key 管理。

### MCP 与数据源条目（2026-08-08 回源核验）

课程主线是 Skills 方法论，MCP 在此定位为"数据源与工具接入层"的案例：用于讲权限边界、API key 管理与第三方供应链风险，不作为安装教程。以下均为 B/C 级线索。

- **paper-search-mcp（openags/paper-search-mcp）**：MIT，free-first 策略；MCP/CLI/Claude Code skill 三形态；覆盖 20+ 开放数据源（arXiv、PubMed、Semantic Scholar、OpenAlex、Crossref、dblp、CORE、Zenodo、HAL 等），对应第 3 课文献检索场景。**注意**：Sci-Hub 通道为可选项，因版权与合规问题课堂不得引入或演示。  
- **zotero-mcp（54yyyu/zotero-mcp）**：MIT，把个人 Zotero 文献库接入 agent（检索、全文、PDF 标注与笔记、集合/标签、DOI/URL/本地文件导入、去重、可选 Scite 引用分析与语义检索）；要求 Python 3.10+/Zotero 7+，可用于 Claude Code/Claude Desktop 等 MCP 客户端，521 commits 维护中；对应第 3/4 课文献管理与证据链场景。本课程工作环境已配置 Zotero MCP，可先本机体验再决定是否课堂演示。  
- **academic-mcp（linxueyuanstdio/academic-mcp）**：MIT，统一 search/download/read 三工具，自称 19+ 数据源（含 IEEE/Scopus/Springer/WoS/ACM/JSTOR 等需订阅配置的源）；小型项目、提交量有限，成熟度低，仅列为线索。  
- **awesome-mcp-servers（punkpeye）**：MIT，目前规模最大的 MCP server 目录，社区活跃，作 MCP 发现入口；LobeHub 等注册表上还有各类学术 MCP，质量参差，须逐个回源核验。  
- **MCP 使用纪律**：最小权限与 key 隔离（对应第 1 课 agent-permissions.md）；第三方 MCP 属外部供应链，安装前审查代码与权限；MCP 生态的安全与可维护性已有学术研究关注（如 arXiv:2506.13538 对 MCP server 安全性的研究，标题线索，具体结论须回源核验）。本节不构成对任何条目的质量背书。

### 课程方法论框架建议（与 skills 结合）
不要只教“怎么 prompt”，而教**研究全生命周期的人类-AI 协作纪律**（参考多门 AI-Assisted Research 课程与论文）：

- **文献与 gap**：用 research-hub / literature-triage / deep-research skills 做发现 + 验证；强制 citation 核对、矛盾识别、taxonomy 构建。强调 AI 输出是 lead，不是结论。  
- **问题与设计**：3-gate 或 hypothesis-testing skills；区分可委托任务 vs 必须人类判断的（novelty、可行性、伦理）。  
- **实验与代码**：coding agent 原生能力 + AI Research Skills / scientific-toolkit；结合 test-driven、context 管理、可复现协议（manifests）。参考 “Twelve quick tips for AI-assisted coding in science”。  
- **写作与验证**：academic-writing + peer-review + claim-audit；强制 attribution、anti-AI-ism、integrity checklist。  
- **伦理与批判**：ethics-review、始终验证、披露 AI 使用、避免 over-delegation。  
- **评估**：让学生用同一 skill 在三个 agent 上对比输出质量、幻觉率、可复现性。

相关课程/资源可参考：Lehigh 的 AI-Assisted Research（四模块：理解单篇 → taxonomy → gap → 综合）、Northwestern MECH_ENG 495、Harvard CS197 等，以及 arXiv 上 AI auto-research lifecycle 综述。

这些 skills 大多开源、可 fork，学生可直接在自己的 OpenCode/Claude Code/Codex 环境实践。建议课程以 1–2 个核心 pipeline（如 co-researcher 或 ai-research-skills 的 3-gate + design）为主线，辅以案例（CS/AI 论文复现或 survey），强调“方法论判断永远在人类侧”。如果需要某个 skill 的具体安装命令、示例 prompt 或课程大纲细化，可以继续说。

### 方法论覆盖缺口（待补，2026-07-29）

对照课程八阶段研究链路与 Agent Workflow 八要素，以下维度与课程价值取向强相关，但当前清单未核验到对应 skill。列为待补，**不在此编造具体 skill 名单**；补入前须回源确认真实存在。

| 缺口维度 | 与课程对齐点 | 状态 |
| --- | --- | --- |
| 失败实验/异常记录与归因 | “失败不得选择性删除”“失败记录是评价工作流的重要证据”（阶段七、失败恢复） | 最显著，待补或自建 |
| 可复现性/环境锁定 | 随机种子、依赖锁定、环境 manifest、数据版本 | 待补 |
| AI 使用披露与署名合规 | 第一课 ai-usage-log.md；regulation/unesco 要求披露、禁 AI 署名 | 待补，与第一课直接相关 |
| Evals/评测设计 | Agent Workflow 八要素之一；第 10–13 课重点 | 课程要求学生自建，未必用现成 skill |
| 统计严谨/因果推断 | “把相关性写成因果”风险（handout 阶段五/六） | 有候选线索（AERS，社科域，待评估；见第 6 节限定） |
| 权限/沙箱/安全边界 | 第一课最小权限、agent-permissions.md | 待补 |
| 数据许可与治理 | 外部输入摄取阶段“许可、隐私或时效性风险” | 待补 |

注意：按“课程不是 Skills 安装课”原则，不必每维度都补现成 skill；部分维度可用课程通用工件（如 ai-usage-log.md 已覆盖披露工件）或要求学生自建（如 Evals）。