---
版本：v0.1.0
最后更新：2026-08-11
适用课次：第 3 课（教师演示与断网备用；与 MI trace、Keshav trace 构成三例对照）
文档类型：真实检索方法演示包（RSI 方向地图，全流程一次执行）
变更记录：
- v0.1.0 (2026-08-11): 首版——2026-08-11 Recursive Self-Improvement 宽泛主题检索 trace。与 MI trace 的五阶段演进不同，本版把 MI 第五阶段才补齐的协议（双轨检索、元层分支、独立基准集自评、群组库 linked_url 附件策略）全部前置，一轮完成：双轨宽泛检索（56 条核心短语命中）+ 9 分支检索；12 条记忆锚点先行留档后逐条核验（0 条 ID 张冠李戴，2 条题名措辞误差、1 条作者张冠李戴、1 条载体误记，§6）；42 条待筛选线索（全部 pending-身份已核）；独立基准集命中 8/10，两条缺口（FunSearch、AlphaEvolve arXiv 版）经综述原文指认补齐；Zotero GraduateCourse 群组库集合 DCNSRSZ2 入藏 42 条 + 40 条 linked_url 附件；7 条工具/来源失败留档（§9.3）。方向收敛段待博士生真实方向指认后升版
---

# RSI 方向地图：检索纪律复现 trace

> 案例边界框：本文件是 **AI agent 与教师于 2026-08-11 对 Recursive Self-Improvement（递归自我改进，RSI）主题执行检索的真实 trace**，全部材料为公开 arXiv/OpenAlex/dblp/Crossref/Semantic Scholar 元数据与公开 PDF 原文，不含任何未发表内容。它与 [mi-search-trace-demo.md](./mi-search-trace-demo.md)（Mechanistic Interpretability 方向，五阶段演进）和 [source-audit-demo.md](./source-audit-demo.md)（Keshav 2007 单篇核验）互为平行：**MI trace 演示领域级检索的失败处理与记录演进，本篇演示同一套协议在第二个方向上的一次性复现——包括协议前置后仍然发生的失败**。学生练习仍使用讲义 §四·5 的虚构案例，不直接修改本文件。

## 1. 本 trace 的六个教学点

1. **幻觉图谱因方向而异，核验流程的价值不在每次都抓到错**：MI trace 中 11 条记忆锚点 4 条 ID 张冠李戴；本次 12 条锚点 0 条 ID 错误，但抓到 1 条作者张冠李戴（A08 二作误记 Helmert，实为 Salamon）、2 条题名措辞误差、1 条载体误记（AlphaEvolve 误记为仅博客，实有 arXiv 版）。**如果因为"这个方向我记忆很好"就跳过核验，这些错误一条都不会被发现**——核验的完整性决定能不能发现错误，而不是错误是否存在（§6）。
2. **修复协议可以前置，但不能消除失败**：MI 第五阶段才建立的协议（双轨检索、元层分支、独立基准集自评、附件策略）本版全部作为起始协议执行，确实避免了 MI 走过的弯路（无新近窗口遗漏高引综述、基准集首轮即做）；但新的失败照样发生：arXiv API 批量查询静默丢弃 1/11 条目、S2 限流、Zotero 字段格式两次报错（§9.3）。协议是累积资产，不是免错符。
3. **小命中域的覆盖风险与 MI 不同**：核心短语 "recursive self-improvement" 全库仅命中 56 条（MI 为 688），不存在 200 条取样窗口截断问题；但核心短语本身覆盖不足——近年实证自改进文献（STaR、Self-Rewarding 等）题名不含该短语，分支检索式必须用扩展家族词承担覆盖责任（§3）。
4. **来源冲突不裁决**：Self-Rewarding LM 的 "ICML 2024" 发表信息为综述引文单源主张，dblp 与 OpenAlex 均只有 arXiv 记录；并列记录、保持 pending，不以多数票或权威来源主张自动解决（§8）。
5. **基准集自评本轮抓到两条真缺口**：以综述 2607.07663 核心引文 [1]-[11] 建立基准集，池内命中 8/10；漏检 FunSearch（Nature 2024）与 AlphaEvolve 的 arXiv 正式版（执行者此前记忆为"仅机构博客"）。缺口补齐依赖综述 PDF 原文的参考文献——**元层文献是指向漏网之鱼的索引**（§10）。
6. **同一流程第二方向复现本身就是验证**：第 3 课的检索纪律不是为 MI 定制的一次性脚本。换一个命中规模、发表生态、文献年代跨度都不同的方向重跑全流程，协议成立、失败形态变化、记录结构不变——这是"方法可迁移"的最直接证据。

## 2. 检索记录

| 字段 | 宽泛检索（双轨） | 分支检索（B1-B9） | 非 arXiv 发现与核验 |
| --- | --- | --- | --- |
| 库 | arXiv API | arXiv API | OpenAlex / Crossref / dblp / Semantic Scholar |
| 检索式 | `all:"recursive self-improvement"`（新近轮 `sortBy=submittedDate` 降序全量 56 条；相关性轮 `sortBy=relevance` 取前 20） | 见 §4 | 按锚点逐库检索式见 §6、§8 各节存档 |
| 检索日期 | 2026-08-11T14:22Z | 2026-08-11T14:23Z | 2026-08-11T14:25–14:32Z |
| 时间范围 | 无限制（命中集 56 < 窗口 200，全量取回） | 相关度排序各取前 200 条内样本 | 按锚点需要 |
| 命中数 | 56（总命中＝取样数） | B1 726 / B2 15 / B3 853 / B4 176 / B5 36 / B6 585 / B7 80 / B8 31 / B9 26 | 逐查询命中数见存档 summary.json |
| 纳入/排除标准 | 题名全量用于词频分支校验（§3），不做论文级纳入 | 锚点选取后逐条身份核验（§5） | 论文池外材料按外部线索处置（§7） |
| 纳入数 | — | 检索阶段 33 条线索入池（28 arXiv + 5 非 arXiv）；基准集/缺口轮补 7 条（含 FunSearch 与 AlphaEvolve arXiv 版）；安全分支代表补 SAHOO 1 条；另计外部线索 W01，终池 42 条 | 同左（非 arXiv 逐条来源见 §5 caveat 列） |

> 双轨轮因 skill 脚本的 arXiv 请求不带排序参数而改用等价公开 API（curl），实际请求 URL 逐轮存档（`broad-recent/request.txt`、`broad-relevance/request.txt`）；分支检索用 skill 脚本执行（每次执行一个空目录，含 request.json/summary.json/results.jsonl/raw.xml）。

## 3. 分支如何确定：词频信号 + 命中数校验（与 MI 的方法差异留档）

MI trace 的分支先由 Agent 凭记忆预设、再用数据校验；本版核心短语命中仅 56 条，直接以**命中集全体题名词频**与词网提出分支，再以分支检索命中数与样本题名校验。方法差异如实记录，不套用 MI 的"记忆预设→数据纠错"叙事。

56 条题名词频信号（≥2 次，去停用词）：agents/agentic 12、self-improving 6、coding 4、research 4、evolution/evolving 7、singularity 3、benchmarking/foundations 4、bounded 2、self-play 2、governance 2、mathematical/formal 4。据此提出 8 条对象级分支 + 1 条元层分支（B9，直接继承 MI §10.5 的 B10 设计）：

| 分支 | 词频/词网依据 | 校验结果 |
| --- | --- | --- |
| B1 Agent 自改进/自进化 | agents/agentic 12 | 命中 726，样本含自进化 Agent 综述与框架，成立 |
| B2 Gödel machine/形式化自修改 | 词网预设 | 命中仅 15，但全部高相关（Gödel machine 家族全体在列），成立——小分支≠弱分支 |
| B3 实证 LLM 自改进（self-rewarding/training） | 词网预设 | 命中 853，样本全部自奖励/自训练方向，成立；词本身是通用 ML 词汇，池外噪声靠后续筛选承担 |
| B4 自动化科研/AI Scientist | research 4 | 命中 176，样本含 AI Scientist 系列与评测，成立 |
| B5 智能爆炸/奇点/安全 | singularity 3、governance 2 | 命中 36，核心命中集内混入少量社会哲学语境的 singularity 条目（样本留档），成立但需人工筛 |
| B6 RSI 基准与评测 | benchmarking 2 + foundations 2 | 命中 585，样本含 PAST-Bench/RSIBench-Data 与自改进评测，成立 |
| B7 算法发现 | algorithms/discovery 4 | 命中 80，样本为 LLM 驱动算法发现，成立 |
| B8 自博弈自改进 | self-play 2 | 命中 31，成立 |
| B9 元层（survey/review/open problems） | 继承 MI B10 设计 | 命中 26，直接浮现 4 篇相关综述（含基准集来源 2607.07663），成立 |

B2 的小命中数是本次与 MI 最不同的数据形态：**领域术语专门化程度高的分支命中数可以很小，不能用命中数阈值否决分支**；B3/B6 的大命中数则提示词族过宽，筛选压力在人工环节，两向的边界都留档。

## 4. 分支检索式（可复盘）

| 分支 | arXiv 检索式 | 命中 |
| --- | --- | ---: |
| 宽泛（双轨共用） | `all:"recursive self-improvement"` | 56 |
| B1 Agent 自进化 | `(all:"self-improving agents" OR all:"self-improving AI" OR all:"self-evolving") AND (cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.MA)` | 726 |
| B2 Gödel machine | `(all:"Godel machine" OR all:"Gödel machine" OR all:"self-referential" AND all:"self-improvement") AND (cat:cs.AI OR cat:cs.LG OR cat:cs.NE OR cat:cs.LO)` | 15 |
| B3 实证自改进 | `(all:"self-rewarding" OR all:"self-training" OR all:"self-taught" OR all:"bootstrapping reasoning") AND (cat:cs.LG OR cat:cs.CL)` | 853 |
| B4 自动化科研 | `(all:"AI scientist" OR all:"automated scientific discovery") AND (cat:cs.AI OR cat:cs.CL OR cat:cs.SE OR cat:cs.LG)` | 176 |
| B5 智能爆炸/奇点 | `all:"intelligence explosion" OR all:"technological singularity"`（跨学科，不加类目过滤） | 36 |
| B6 基准评测 | `(all:"self-improvement" OR all:"self-improving") AND (all:benchmark OR all:evaluation)` | 585 |
| B7 算法发现 | `(all:"algorithm discovery" OR all:"improve themselves" OR all:"self-evolving algorithms") AND (cat:cs.LG OR cat:cs.AI OR cat:cs.NE)` | 80 |
| B8 自博弈 | `all:"self-play" AND (all:"self-improving" OR all:"self-improvement") AND (cat:cs.AI OR cat:cs.LG)` | 31 |
| B9 元层 | `(ti:survey OR ti:review OR ti:"open problems" OR ti:roadmap) AND (all:"recursive self-improvement" OR all:"self-improving" OR all:"intelligence explosion")` | 26 |

检索式修正留档：B2 同时收录带变音符与不带变音符两种写法（`Gödel`/`Godel`），实测 arXiv 对两种写法分别命中，缺一漏检；B5 不加类目过滤后混入少量非 AI 语境的 singularity 条目，样本保留供课堂讨论"为什么这个词需要人工筛"。

## 5. 待筛选线索表（全部 `pending`-身份已核；拟用主张待核）

身份核验方式：arXiv 锚点经 `id_list` 精确查询对齐 ID/题名/作者/首发日期（两批批量 + 两条单查）；非 arXiv 锚点经 Crossref DOI 或 OpenAlex/Semantic Scholar 题录核验（逐条来源见 caveat 列）。本表使用讲义 §五 十字段表头；尚无收敛研究问题与拟用主张，"对应问题/拟用主张"统一标"待问题收敛"，人工筛选决定统一标 `awaiting-human`。本表是线索区，不是候选文献表。

| 编号 | 题名（核验后） | 作者 | 年份 | 稳定来源 | 对应问题/拟用主张 | 预期证据角色 | 纳入理由 | 核验状态 | caveat/允许主张 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RSI-C01 | Speculations Concerning the First Ultraintelligent Machine | I. J. Good | 1966 | DOI 10.1016/S0065-2458(08)60418-0（Advances in Computers 6:31-88） | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | Crossref+OpenAlex 双源；RSI 概念奠基文献 |
| RSI-C02 | Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements | Schmidhuber | 2003 | arXiv:cs/0309048 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 记忆锚点 A01；ID 低置信猜中 |
| RSI-C03 | Machine Superintelligence（博士论文） | Legg | 2008 | 无稳定标识符（四源未解析） | 待问题收敛 | 探索线索 | awaiting-human | pending（身份未核完；拟用主张待核） | OpenAlex/dblp/Crossref/S2 均未命中；恢复路径：作者主页论文 PDF |
| RSI-C04 | The Singularity: a Philosophical Analysis | Chalmers | 2010 | S2 题录 + DOI 10.1002/9781118922590.CH16（Wiley 重印章节，2016） | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 原发期刊刊名两源均未给出（S2 venue 为空），待第二来源；A10 首轮 S2 429，重试命中 |
| RSI-C05 | Intelligence Explosion: Evidence and Import | Muehlhauser, Salamon | 2012 | DOI 10.1007/978-3-642-32560-1_2（The Frontiers Collection） | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | Crossref+OpenAlex 双源更正作者（记忆误记二作 Helmert，§6） |
| RSI-C06 | Bounded Recursive Self-Improvement | Nivel et al. | 2013 | arXiv:1312.6764 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C07 | Intelligence Explosion Microeconomics | Yudkowsky | 2013 | OpenAlex 记录（无 DOI；MIRI 技术报告） | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | OpenAlex 单源（CiteSeerX 镜像链），载体为机构报告 |
| RSI-C08 | From Seed AI to Technological Singularity via Recursively Self-Improving Software | Yampolskiy et al. | 2015 | arXiv:1502.06512 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C09 | A Model of Pathways to Artificial Superintelligence Catastrophe for Risk and Decision Analysis | Barrett et al. | 2016 | arXiv:1607.07730 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C10 | Self-Regulating Artificial General Intelligence | Gans | 2017 | arXiv:1711.04309 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C11 | A Formulation of Recursive Self-Improvement and Its Possible Efficiency | W. Wang et al. | 2018 | arXiv:1805.06610 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C12 | A Finite-Time Technological Singularity Model With Artificial Intelligence Self-Improvement | Kendiukhov | 2020 | arXiv:2010.01961 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C13 | STaR: Bootstrapping Reasoning With Reasoning | Zelikman et al. | 2022 | arXiv:2203.14465 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 记忆锚点 A03 题名措辞修正；已发表 NeurIPS 2022（dblp 单源） |
| RSI-C14 | Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | arXiv:2303.11366 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 综述相邻经典；已发表 NeurIPS 2023（dblp 单源） |
| RSI-C15 | Self-Refine: Iterative Refinement with Self-Feedback | Madaan et al. | 2023 | arXiv:2303.17651 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 已发表 NeurIPS 2023（dblp 单源） |
| RSI-C16 | Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution | Fernando et al. | 2023 | arXiv:2309.16797 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C17 | Large Language Models Cannot Self-Correct Reasoning Yet | J. Huang et al. | 2023 | arXiv:2310.01798 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 综述引文标 ICLR 2024（单源，索引库待核）；**对比证据候选** |
| RSI-C18 | Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation | Zelikman et al. | 2023 | arXiv:2310.02304 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C19 | Self-Rewarding Language Models | Yuan et al. | 2024 | arXiv:2401.10020 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | **发表状态冲突**：综述引文称 ICML 2024（单源），dblp/OpenAlex 仅见 arXiv 记录，不裁决（§8） |
| RSI-C20 | Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | Snell et al. | 2024 | arXiv:2408.03314 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 综述相邻经典 |
| RSI-C21 | The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | C. Lu et al. | 2024 | arXiv:2408.06292 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 记忆锚点 A06 |
| RSI-C22 | Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement | Yin et al. | 2024 | arXiv:2410.04444 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 记忆锚点 A07；已发表 ACL 2025（dblp 单源） |
| RSI-C23 | Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement | Ishibashi et al. | 2024 | arXiv:2410.15639 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 批量 id_list 曾被静默丢弃，单查恢复（§9.3） |
| RSI-C24 | A Survey on LLM Inference-Time Self-Improvement | Dong et al. | 2024 | arXiv:2412.14352 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 元层 |
| RSI-C25 | SiriuS: Self-improving Multi-agent Systems via Bootstrapped Reasoning | W. Zhao et al. | 2025 | arXiv:2502.04780 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C26 | Absolute Zero: Reinforced Self-play Reasoning with Zero Data | A. Zhao et al. | 2025 | arXiv:2505.03335 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C27 | Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents | J. Zhang et al. | 2025 | arXiv:2505.22954 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 记忆锚点 A05 题名措辞修正（"AI Agents"→"Agents"）；OpenAlex 另见期刊版 DOI 10.70777/si.v2i3.15063（arXiv 版与期刊版并存，引用指认版本） |
| RSI-C28 | AlphaEvolve: A coding agent for scientific and algorithmic discovery | Novikov et al. | 2025 | arXiv:2506.13131 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 基准集缺口轮入池：记忆误记为"仅机构博客"（A12），综述 ref [4] 指认 arXiv 版 |
| RSI-C29 | Will Compute Bottlenecks Prevent an Intelligence Explosion? | Whitfill et al. | 2025 | arXiv:2507.23181 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C30 | R-Zero: Self-Evolving Reasoning LLM from Zero Data | C. Huang et al. | 2025 | arXiv:2508.05004 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 综述引文标 ICLR 2026（单源，索引库待核） |
| RSI-C31 | A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Learning | Fang et al. | 2025 | arXiv:2508.07407 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 元层 |
| RSI-C32 | SGM: A Statistical Godel Machine for Risk-Controlled Recursive Self-Modification | X. Wu et al. | 2025 | arXiv:2510.10232 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C33 | Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improvement Loop | W. Wang et al. | 2025 | arXiv:2510.21614 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C34 | The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development? | X. Lu et al. | 2026 | arXiv:2606.04455 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C35 | Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | M. Chen et al. | 2026 | arXiv:2607.07663 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 元层；**本 trace 基准集来源**（§10） |
| RSI-C36 | Self-Improvements in Modern Agentic Systems: A Survey | Ren et al. | 2026 | arXiv:2607.13104 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 元层 |
| RSI-C37 | RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement | Meng et al. | 2026 | arXiv:2607.25886 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C38 | PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents | Xue et al. | 2026 | arXiv:2608.04003 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C39 | Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution | Liu et al. | 2026 | arXiv:2608.07645 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | |
| RSI-C40 | SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement | Sahoo et al. | 2026 | arXiv:2603.06333 | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 安全/对齐分支代表（后补） |
| RSI-C41 | Mathematical discoveries from program search with large language models | Romera-Paredes et al. | 2024 | DOI 10.1038/s41586-023-06924-6（Nature 625:468-475） | 待问题收敛 | 探索线索 | awaiting-human | pending（身份已核；拟用主张待核） | 基准集缺口轮入池（综述 ref [3]，FunSearch）；Crossref 出版年登记 2023（在线首发）与期刊卷年 2024 并存 |
| RSI-W01 | Recursive Self-Improvement（Anthropic Institute blog，2026-05） | Anthropic | 2026 | https://www.anthropic.com/institute/recursive-self-improvement | 待问题收敛 | 外部线索 | awaiting-human | pending（存在已核；内容未核） | URL 出自综述 ref [5]，HTTP 200 存活核实（2026-08-11）；外部线索不入论文池 |

## 6. 教学点一：记忆锚点幻觉审计（12 条先行留档，逐条核验）

执行规则与 MI trace 相同：任何检索请求发出**之前**，Agent 凭训练记忆写下 12 条锚点（含 ID 猜测与自报置信度），原始记录冻结于 `.work/rsi-search/01-memory-anchors.md`；核验只允许改审计结果列，不允许改记忆原文。核验结果：

| 记忆条目 | 记忆置信 | 核验结果 | 处置 |
| --- | --- | --- | --- |
| A01 Gödel Machines＝cs/0309048 | ID 低 | ID 正确（猜中），题名/作者一致 | 身份通过 |
| A02 Intelligence Explosion Microeconomics＝MIRI 报告 | 载体中 | OpenAlex 证实 Yudkowsky 2013，无 DOI | 身份通过（单源） |
| A03 STaR＝2203.14465 | ID 中 | ID 正确；**题名记忆有误**（记"Self-Taught Reasoner"，实为 "STaR: Bootstrapping Reasoning With Reasoning"） | 身份通过，题名修正 |
| A04 Self-Rewarding LM＝2401.10020 | ID 中 | ID 正确，题录一致 | 身份通过 |
| A05 Darwin Gödel Machine＝2505.22954 | ID 低 | ID 正确（猜中）；**题名措辞误差**（记"AI Agents"，官方 "Agents"） | 身份通过，题名修正 |
| A06 AI Scientist＝2408.06292 | ID 中 | 一致 | 身份通过 |
| A07 Gödel Agent＝2410.04444 | ID 低 | 一致（宽泛检索新近轮直接命中） | 身份通过 |
| A08 Intelligence Explosion: Evidence and Import＝Muehlhauser & **Helmert** | 作者记忆 | **作者张冠李戴**：Crossref+OpenAlex 双源证实二作为 Anna Salamon；载体系 Springer 书章节（非 arXiv） | 作者更正，来源登记 |
| A09 Machine Superintelligence＝Legg 博士论文 | 载体中 | OpenAlex/dblp/Crossref/S2 四源均未命中 | 保持 pending，恢复路径留档 |
| A10 Singularity: A Philosophical Analysis＝Chalmers 2010 | 载体中 | S2 首轮 429，重试命中；Wiley 重印章节 DOI 经 Crossref 核验；原发期刊刊名两源均为空 | 身份通过，刊名待第二来源 |
| A11 Self-Refine＝2303.17651 | ID 中 | 一致 | 身份通过 |
| A12 AlphaEvolve＝仅 DeepMind 博客 | 载体中 | **载体误记**：综述 ref [4] 指认 arXiv 正式版 2506.13131，id_list 核验通过 | 更正，arXiv 版入池（RSI-C28） |

**与 MI trace 的对照是本 trace 的核心教材**：MI 的 11 条锚点中 4 条 ID 张冠李戴；RSI 的 12 条锚点 0 条 ID 错误，但幻觉转移到了作者（A08）、题名措辞（A03/A05）与载体（A12）字段。两个方向合起来说明：**幻觉没有固定的形态分布，任何一类字段都可能出错；跳过核验的代价不是"可能漏掉错误"而是"必然漏掉错误"**。与讲义 §四·5 虚构表对照：虚构表练习状态判断，本表与 MI §6 展示真实审计的形态差异。

## 7. 非 arXiv 锚点与外部线索

| 条目 | 来源类型 | 状态 |
| --- | --- | --- |
| Good 1966（Advances in Computers） | 书章节，Crossref DOI | verified（身份层）：Crossref+OpenAlex 双源 |
| Muehlhauser & Salamon 2012（Springer Frontiers Collection 书章节） | 书章节，Crossref DOI | verified（身份层）：Crossref+OpenAlex 双源；作者更正见 §6 |
| Yudkowsky 2013（MIRI 技术报告） | 机构报告，无 DOI | pending：OpenAlex 单源 |
| Legg 2008（博士论文） | 学位论文 | pending：四源未解析（§6 A09） |
| Chalmers 2010 | 期刊论文 + Wiley 重印章节 | pending：S2 题录 + 重印 DOI（Crossref），原发刊名待第二来源 |
| AlphaEvolve DeepMind 博客（2025） | 机构博客 | 外部线索；其 arXiv 正式版已入池（RSI-C28），博客本身不重复入池 |
| Anthropic "Recursive Self-Improvement"（2026-05） | 机构博客 | 外部线索 RSI-W01：URL 存活核实，内容未核 |

## 8. 跨源核验与来源冲突（如实留档，不裁决）

1. **发表状态抽查**（dblp 题名检索）：STaR → NeurIPS 2022；Self-Refine → NeurIPS 2023；Reflexion → NeurIPS 2023；Gödel Agent → ACL 2025。以上均为 dblp 单源，待第二来源升级；Gödel Agent 的 dblp 条目题名（"Recursively Self-Improvement"）与 arXiv 官方题名（"Recursive Self-Improvement"）措辞不同，以 arXiv 元数据为身份锚。
2. **来源冲突（不裁决实例）**：RSI-C19 Self-Rewarding LM——综述 2607.07663 ref [8] 标 "In ICML, 2024"，dblp 三轮题名检索与 OpenAlex 2024 年过滤检索均只返回 arXiv/CoRR 记录。处置：两说并列记录，条目保持 pending，引用时按 arXiv 预印本对待并注明争议。与 MI §8 的单源局限记录同理：索引库查无≠未发表，索引库有记录≠完整，冲突交人工。
3. **OpenAlex 引文数据缺口**：基准集综述（2607.07663）在 OpenAlex 的 `referenced_works` 为空（新近预印本未建立引文索引），改走 PDF 原文取参考文献（§10）；前向滚雪球的 OpenAlex 引用数同样系统性低估 arXiv 预印本（DGM 被引 3、Gödel Agent 被引 2、STOP 被引 2），与 MI §10.3 的"记录分裂碎片条目"结论一致。
4. **Semantic Scholar 限流与恢复**：A10 首轮 429（与 MI §8 失败记录 2 同型），改词重试命中；无 key 情况下限流是常态而非例外，两 trace 合并观察：S2 只宜作补充源。

## 9. Zotero 入藏（群组库终局口径）

**正位**：GraduateCourse 群组库（groupID 6634461）集合 `DCNSRSZ2`（Recursive Self-Improvement），42 条顶层条目（RSI-C01–C41 + RSI-W01），全部 tag `rsi-trace`，Extra 登记 `trace-id`；trace-id → 群组 key 映射存档 `.work/rsi-search/zotero/group-keys.json`。

**附件策略**：延续 MI trace §10.7 终局口径（群组库 fileEditing 关闭 + Zotero 云配额 413 教训前置），41 条论文各挂 1 条 linked_url 附件（arXiv PDF 直链或 DOI 官链，40/40 成功；RSI-C03 无 OA 链接不挂附件）；RSI-W01 网页条目本身即 URL。不做真实文件上传，不重蹈附件假成功。

### 9.1 本阶段工具失败记录（真实发生，全部留档）

1. **skill 脚本 arXiv 请求不带排序参数**：双轨轮改用等价公开 API（curl），实际请求 URL 逐轮存档；脚本用于分支检索（其产物含 request.json/summary.json/results.jsonl，满足复盘要求）。
2. **http→https 重定向未跟随**：首次探测请求空响应，改 `https` + 跟随重定向后成功；请求层配置错误也是查询级失败，不记为文献级状态。
3. **arXiv API 批量 id_list 静默丢条**：11 条一批的批量查询只返回 10 条（2410.15639 缺失，无错误回报），单条重查恢复。**批量成功回报也要数条目**，与 MI §9.3 附件假成功同源。
4. **Semantic Scholar 429**：见 §8 第 4 条。
5. **Zotero 条目字段格式两次报错**：机构作者条目先后触发 "'firstName' creator field must be set" 与 "Invalid creator property 'fieldMode'"，第三次按单字段作者格式成功；每次失败回报与实际状态均留档。
6. **Zotero API SSL 瞬断**：批次写入成功后回查请求 SSL EOF 失败，重试后回查通过（顶层 42、附件 40）；**写入成功与回查成功是两件事，回查失败要重试而不是当作写入失败**。
7. **OpenAlex 引文索引对最新预印本为空**：见 §8 第 3 条，PDF 原文为兜底路径。

## 10. 检索质量自评（讲义 §六，本轮首次即执行）

### 10.1 基准集切片（独立于筛选结果建立）

基准集来源：B9 元层分支直接发现的综述 RSI-C35（Chen et al. 2026，arXiv:2607.07663，PDF 下载存档 `baseline/survey-2607.07663v1.pdf`）。取其参考文献 [1]–[11]（综述的核心谱系引文）为基准集切片；[5] Anthropic 博客按外部线索排除（排除理由记档），分母 10 条论文。

命中分析（对照 §5 线索池）：**8/10 命中**，两条缺口：

| 基准集条目 | 池内状态 |
| --- | --- |
| [1] Good 1966 | ✓ RSI-C01 |
| [2] Gödel Machines | ✓ RSI-C02 |
| [3] FunSearch（Nature） | ✗ 缺口 → 补验入池 RSI-C41 |
| [4] AlphaEvolve | ✗ 缺口（记忆误记仅博客）→ 补验入池 RSI-C28 |
| [6] Self-Refine | ✓ RSI-C15 |
| [7] STaR | ✓ RSI-C13 |
| [8] Self-Rewarding LM | ✓ RSI-C19 |
| [9] Gödel Agent | ✓ RSI-C22 |
| [10] Darwin Gödel Machine | ✓ RSI-C27 |
| [11] AI Scientist | ✓ RSI-C21 |

**切片自身局限**（与 MI §10.4 同口径）：基准集来自本次检索范围内发现的综述，独立性弱于 MI 第五阶段的用户 Scholar 快照；若用户后续提供 RSI 方向的 Scholar 快照或其他外部反例，按 MI §10.3 流程增补命中分析。8/10 是必要条件证据，不是充分性证明。

### 10.2 滚雪球

前向滚雪球两轮（OpenAlex cited_by，已知低估，记录在案）：DGM 被引 3、Gödel Agent 被引 2（第一轮）；STOP 被引 2（第二轮）。两轮均未出现池外核心相关文献——对象级被引论文多为应用类（材料设计、系统工程、多模态综述），记"当前策略下（OpenAlex 引用键）趋于饱和"。后向滚雪球由基准集切片承担（综述参考文献即核心论文的后向汇集）。

### 10.3 问题要素 × 分支覆盖矩阵（无空格）

问题初稿三要素：(a) 实现方案与理论论证；(b) 实证与经典构想的关系；(c) 验证与安全含义。

| 问题要素 | 对应分支 | 命中数 | 池内代表（编号） |
| --- | --- | --- | --- |
| (a) 形式化/理论自修改 | B2 | 15 | C02、C22、C27、C32、C33、C39、C16 |
| (a) 实证自改进方法 | B3、B8 | 853、31 | C13、C14、C15、C19、C26、C30 |
| (a) Agent 自进化 | B1 | 726 | C25、C31 |
| (a) 自动化科研/算法发现 | B4、B7 | 176、80 | C21、C23、C28、C34、C41 |
| (b) 实证与经典关系 | 宽泛双轨 + B9 | 56、26 | C35（综述题目即此问题）、C01、C08 |
| (c) 智能爆炸/安全/治理 | B5 | 36 | C05、C09、C10、C12、C29、C40 |
| (c) 基准与评测 | B6 | 585 | C37、C38 |

无零命中分支（B2 命中 15 为最小，样本全相关，非死路）。

### 10.4 代表性检查

- 方法族分组各 ≥1 代表：形式化（C02 系）、训练循环自改进（C13/C15/C19）、推理时自改进（C14/C15/C20）、自动化科研（C21/C28）、评测（C37/C38）、元层综述（C24/C31/C35/C36）✓
- 对比证据：RSI-C17（"LLM 尚不能自我纠错"）与自改进有效性主张构成对照，已在池 ✓
- 年份：1966–2026 连续覆盖，经典层与 2025–2026 新近层均在池 ✓
- 来源：arXiv 主源 + Nature（C41）+ Springer（C05）+ Wiley（C04 重印）+ Elsevier（C01），非 arXiv 单源结构缺口已由基准集轮暴露并部分修复 ✓
- 机构独立性：DeepMind 关联文献（C21/C28）与学术文献并存，利益相关标注待角色指认时处理 ✓
- 红旗项：**RSI-C03（Legg 论文）四源不可解析**——领域奠基文档在标准索引中长期不可见，本身是关于"来源覆盖≠领域覆盖"的证据；**发表状态冲突一例（C19）未裁决**，引用时按保守口径。

## 11. 复盘方式

宽泛检索新近轮可复盘：

```text
https://export.arxiv.org/api/query?search_query=all:%22recursive+self-improvement%22&start=0&max_results=56&sortBy=submittedDate&sortOrder=descending
```

分支复盘示例（B2）经 skill 脚本：

```bash
python3 .agents/skills/research-question-to-search/scripts/search_public_sources.py \
  --source arxiv \
  --raw-query '(all:"Godel machine" OR all:"Gödel machine" OR all:"self-referential" AND all:"self-improvement") AND (cat:cs.AI OR cat:cs.LG OR cat:cs.NE OR cat:cs.LO)' \
  --limit 200 --output-dir .work/rsi-search/replay-b2
```

单条身份核验：`http://export.arxiv.org/api/query?id_list=2410.04444`。命中数随时间变化属正常差异；复盘记录自己的检索日期与命中数，与原记录对照。教师生产 trace 原始材料存档于 `.work/rsi-search/`（不发布）：问题初稿与记忆锚点 `00-problem-draft.md`、`01-memory-anchors.md`；宽泛双轨 `broad-recent/`、`broad-relevance/`；分支 `branch-b1/`–`branch-b9/`；幻觉审计 `anchor-audit/`；基准集 `baseline/`（含综述 PDF 与引文核对）；滚雪球 `snowball/`；跨源 `cross-source/`；Zotero `zotero/`（group-keys.json、verify.json）。Zotero 断网备份以群组库集合 `DCNSRSZ2` 元数据为准。

## 12. 与课程的连接

- 讲义 §四 四态与进入规则：本文件全部条目按该口径标注（41 条论文 `pending`-身份已核 + 1 条外部线索）；
- 讲义 §五 三类记录：§2 对应检索记录，§6/§8 对应来源审计记录，§5 是线索区而非正式候选表；
- 讲义 §六 检索质量自评：§10 给出基准集切片（8/10）、滚雪球两轮、覆盖矩阵与代表性检查的完整实例——与 MI §10 合并构成"自评先评自己"的两方向样本；
- 讲义 §七 常见错误 3（AI 报告当证据）与错误 5（检索过程不可复盘）：§6 提供两方向幻觉形态对照，§2/§4/§11 给出可复盘记录；
- 与 [mi-search-trace-demo.md](./mi-search-trace-demo.md) 的对照关系：**同一方法、两个方向、不同的失败形态与命中生态**——MI 演示协议缺失时的代价与五阶段补救，本篇演示协议前置后仍会出新失败；两篇合用可破除"这套流程是为 MI 定制的"误解；
- 与 [source-audit-demo.md](./source-audit-demo.md)：Keshav trace 演示单篇主张级核验，本篇 §6 A08/A10 的作者与刊名核验与之呼应；
- 课程 2.0 批次 0 验收项"≥1 条真实科研失败演示"：本篇新增 1 条作者张冠李戴（A08）、1 条载体误记（A12）、1 条来源冲突不裁决（C19）与 7 条工具失败记录（§9.1）；
- 方向收敛段（从宽泛主题到具体研究问题）待博士生真实方向指认后补入本文件并升版。
