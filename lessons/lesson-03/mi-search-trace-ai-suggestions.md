---
版本：v0.1.0
生成日期：2026-08-20
文档类型：MI 检索 trace 的 AI 建议叠加稿
状态：冻结审阅稿；全部建议待人工确认；不属现行课程材料
上游事实源：lessons/lesson-03/mi-search-trace-demo.md v0.5.1
上游 SHA-256：69fb6edb83654635949faf6fb79ef2bb6841c753705272720f557c66cab8458e
---

# MI 检索 trace：AI 建议叠加稿

> 本文件只给出 AI 建议，不修改也不替代[原 trace](./mi-search-trace-demo.md)。原 trace 仍是题名、作者、年份、稳定来源、检索过程与正式核验状态的唯一事实源。本文件冻结于原 trace v0.5.1 的所列 SHA-256 快照；本文件中的问题、角色、筛选动作、核验状态与允许主张全部保持 `awaiting-human`。研究负责人确认前，不得写回正式候选文献表、精读卡或证据地图。

## 一、建议边界与方法

1. 本轮只做第 3 课范围的入口核验：为每篇论文提出一条拟用主张，并回到一个原文位置核对；不代替第 4 课的多主张精读。
2. `原核验状态` 逐条镜像原 trace，全部保持 `pending（身份已核；拟用主张待核）`；`AI 建议核验状态` 只是建议，不产生状态升级。
3. `AI 建议筛选动作` 使用“建议纳入／建议仅留线索”，不是人工筛选决定。问题簇未被研究负责人选定时，相关条目仍只在线索区。
4. 原文定位优先使用本地 Zotero PDF；MI-C26 已换为 InterPLM `2412.12101v1`，MI-C30 已换为 PMLR 正式版 `adams25a`，MI-C36 已换为 ACM CSUR 正式版 `10.1145/3787104`。三份历史附件已移入 Zotero 回收站并在 `.work` 留存备份，其坚果云 WebDAV 对象已在用户确认后删除；后续仍应按题名与稳定标识复核文件身份。
5. 置信度只描述“当前允许主张能否由所列原文位置直接支持”，不评价论文整体质量，也不等于证据充分性。

## 二、AI 候选问题簇

| 编号 | 候选研究问题 | 建议用途 |
| --- | --- | --- |
| RQ-A | SAE 与其他特征发现方法在什么条件下能得到稳定、可解释且具有因果意义的表示单元？ | 表示单元、superposition、monosemanticity、SAE 与可解释训练 |
| RQ-B | 探针、patching、电路发现与因果抽象如何证明捕获的是机制，而不只是相关性或可操纵表象？ | 因果忠实性、机制定位、干预错觉、跨架构重复 |
| RQ-C | MI 方法应如何评价 fidelity、completeness、reconstruction、自动化与可扩展性？ | 评价指标、自动电路发现、SAE 规模化、训练进程指标 |
| RQ-D | MI 对控制、安全、幻觉检测、推理与训练失效分析提供了哪些直接证据，边界在哪里？ | 安全应用、RAG 幻觉、训练机制、行为控制 |
| RQ-E | MI 方法能否推广到视觉、多模态、world model 与蛋白质语言模型？ | 跨模态、跨领域、跨模型族迁移 |
| RQ-F | MI 领域当前有哪些开放问题、解释边界、概念分歧与治理含义？ | 综述、术语、理论边界、研究议程 |

这些问题是并列候选，不构成博士生问题定义。人工确认时应先选择或改写问题簇，再校准相应条目的角色和纳入决定。

## 三、逐条 AI 建议

### RQ-A｜表示单元、SAE 与可解释训练

| 编号 | AI 建议问题簇/拟用主张 | AI 建议预期证据角色 | AI 建议筛选动作 | AI 建议纳入理由 | 原核验状态 | AI 建议核验状态 | 原文定位 | AI 建议 caveat/允许主张 | 置信度 | 人工确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C01 · Toy Models of Superposition | RQ-A；稀疏特征可使玩具 ReLU 网络用 superposition 表示多于维度数的特征 | 主证据 | 建议纳入 RQ-A | 直接给出 superposition 的可分析生成机制 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要与导言 | 只允许主张“该现象在合成稀疏特征玩具模型中出现”；不能直接外推真实 LLM 的特征组织 | 高 | awaiting-human |
| MI-C02 · Sparse Autoencoders Find Highly Interpretable Features | RQ-A；SAE 在所测语言模型激活上提取了比替代分解更可解释、较单义的方向，并在 IOI 上定位因果相关特征 | 主证据 | 建议纳入 RQ-A | 同时连接特征提取、自动可解释性评价与局部因果任务 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 自动解释指标与单个 IOI 任务不足以证明已普遍“解决 superposition”；引用时指认 arXiv/ICLR 版本 | 中 | awaiting-human |
| MI-C03 · Gemma Scope | RQ-A、RQ-C；作者发布覆盖 Gemma 2 多层与多子层的 JumpReLU SAE 套件及标准指标 | 补充证据 | 建议纳入 RQ-A/RQ-C 的资源与规模化线 | 提供开放模型上的大规模 SAE 资源和跨层比较入口 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要 | 允许主张仅为“发布并评价该套件”；论文明确称 SAE 仍是不成熟技术，不能把资源规模当作方法有效性证明 | 高 | awaiting-human |
| MI-C14 · Engineering Monosemanticity in Toy Models | RQ-A；改变训练所到达的局部极小值与增加神经元，可在玩具模型中提高 monosemanticity | 补充证据 | 建议仅留 RQ-A 线索 | 提供“训练或架构可主动塑造可解释性”的替代路线 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要与 §1.1 | 初步结果且限于玩具模型；不能证明真实大模型可用同样方式获得单义表示 | 高 | awaiting-human |
| MI-C29 · Seeing is Believing / BIMT | RQ-A；加入几何连接代价的 BIMT 在若干简单任务中产生更模块化、可视化的网络 | 补充证据 | 建议仅留 RQ-A 线索 | 补充“从训练目标设计可解释结构”，区别于事后 SAE 分解 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要与导言 | 主要实验是小规模简单任务；“肉眼可见模块”不等于因果解释或对现代 LLM 有效 | 高 | awaiting-human |

### RQ-B｜因果忠实性与机制定位

| 编号 | AI 建议问题簇/拟用主张 | AI 建议预期证据角色 | AI 建议筛选动作 | AI 建议纳入理由 | 原核验状态 | AI 建议核验状态 | 原文定位 | AI 建议 caveat/允许主张 | 置信度 | 人工确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C05 · Sparse Feature Circuits | RQ-B；SAE 特征与因果电路搜索可组成可解释的 sparse feature circuits，并用于局部行为编辑 | 主证据 | 建议纳入 RQ-B | 直接把细粒度特征、因果子图与干预应用连接起来 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 允许主张限于论文所测行为和近似搜索流程；不能推成对任意模型行为的完整机制解释 | 高 | awaiting-human |
| MI-C06 · Tuned Lens | RQ-B、RQ-D；逐层 affine probes 比 logit lens 更可靠，并在所测模型上经因果实验显示使用与模型相似的特征 | 补充证据 | 建议纳入 RQ-B | 为“探针读出是否对应模型实际计算”提供实验线索 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | affine probe 仍可能改变或重编码表示；结论限于论文模型、任务与版本，不能把可预测性等同因果忠实性 | 中 | awaiting-human |
| MI-C07 · Emergent Linear Representations in World Models | RQ-B、RQ-E；OthelloGPT 的相对棋盘状态可由线性表示读出，并可通过向量运算控制行为 | 主证据 | 建议纳入 RQ-B | 同时给出线性读出和行为干预，比只报告 probing accuracy 更接近机制证据 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 结论来自 Othello 自监督序列模型；不能外推一般语言世界模型都采用同类线性表示 | 高 | awaiting-human |
| MI-C08 · IOI Circuit | RQ-B；GPT-2 small 的 IOI 行为可由 26 个注意力头组成的电路部分解释，并以 faithfulness、completeness、minimality 检查 | 主证据 | 建议纳入 RQ-B | 是端到端自然语言行为机制分析和多指标验证的核心案例 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 作者明确指出解释仍有缺口；只允许主张该电路解释所定义 IOI 设置，不能外推 GPT-2 全部语言行为 | 高 | awaiting-human |
| MI-C11 · Activation Patching Guide | RQ-B；activation patching 的证据强度取决于 corruption、patch 位置、metric 与结果解释 | 补充证据 | 建议纳入 RQ-B 的方法边界线 | 集中说明 patching 能回答什么及常见误读 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要与 §1 | 这是经验性方法指南，不是跨方法受控比较；允许主张仅为“总结实践建议与证据边界” | 高 | awaiting-human |
| MI-C12 · Successor Heads | RQ-B；successor heads 与 mod-10 特征在多个架构和规模中重复出现，并可用向量运算编辑其行为 | 主证据 | 建议纳入 RQ-B | 提供跨架构复现和干预证据，检验机制是否只存在于单一模型 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 机制围绕 succession 类任务，且相关 heads 仍具 polysemanticity；不能推成通用数值推理机制 | 高 | awaiting-human |
| MI-C13 · In-context Learning and Induction Heads | RQ-B、RQ-D；小型 attention-only 模型中 induction heads 与 in-context learning 有强因果证据，大模型证据主要相关性 | 主证据 | 建议纳入 RQ-B，并作证据强度分层示例 | 原文主动区分小模型因果证据与大模型相关证据 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 允许主张必须保留“小模型强因果／含 MLP 大模型相关性”的分层，不能写成已证明所有 ICL 由 induction heads 产生 | 高 | awaiting-human |
| MI-C22 · Causal Abstraction | RQ-B；causal abstraction 为多种 MI 方法提供统一的形式语言，并形式化 graded faithfulness 等概念 | 主证据 | 建议纳入 RQ-B 的理论基线 | 可用于明确“机制解释是低层系统的忠实高层简化”所需条件 | pending（身份已核；拟用主张待核） | `verified` | JMLR 正式版 p.1 摘要 | 这是理论统一框架，不直接证明某项经验解释真实或完整；引用须使用 JMLR 2025 正式版 | 高 | awaiting-human |
| MI-C24 · Boundless DAS | RQ-B；Boundless DAS 在 Alpaca 7B 的简单数值推理任务上找到两个可解释布尔变量的因果对齐 | 主证据 | 建议纳入 RQ-B | 展示 causal abstraction 方法向较大指令模型扩展的具体实例 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 单一简单任务与单一模型不足以证明复杂开放行为也可获得同等对齐 | 高 | awaiting-human |
| MI-C31 · Subspace Activation Patching Illusion | RQ-B；成功改变输出的 subspace intervention 不必定位到原模型实际使用的因果子空间 | 对比证据 | 建议纳入 RQ-B，作为强制反例 | 直接反驳“能控制行为即可解释机制”的推断，并给出成功案例所需附加证据 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 论文不主张 subspace patching 一概无效；允许主张是“存在可构造且在真实任务出现的解释错觉，需附加忠实性证据” | 高 | awaiting-human |

### RQ-C｜评价、自动化与可扩展性

| 编号 | AI 建议问题簇/拟用主张 | AI 建议预期证据角色 | AI 建议筛选动作 | AI 建议纳入理由 | 原核验状态 | AI 建议核验状态 | 原文定位 | AI 建议 caveat/允许主张 | 置信度 | 人工确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C04 · JumpReLU SAE | RQ-C；在 Gemma 2 9B 激活上，JumpReLU SAE 在给定稀疏度下改善重构 fidelity，且论文的人工与自动检查未发现相应可解释性代价 | 主证据 | 建议纳入 RQ-C | 直接研究 sparsity–reconstruction 张力和训练目标 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 只允许主张论文设置内的 Pareto 改善；“未付出可解释性代价”受所用人工/自动指标限制 | 高 | awaiting-human |
| MI-C09 · ACDC | RQ-C；ACDC 自动化了电路发现中的连接搜索，并在既有小型任务上重现部分人工电路 | 主证据 | 建议纳入 RQ-C | 提供可复盘的自动化对象、评价基准与恢复数量 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 自动化的是工作流中的一个步骤；对既有已知电路的恢复不等于能发现开放世界的新机制 | 高 | awaiting-human |
| MI-C10 · Attribution Patching | RQ-C；基于 attribution patching 的线性近似在论文任务平均 circuit-recovery AUC 上优于所比较方法，计算只需少量 passes | 主证据 | 建议纳入 RQ-C，并与 MI-C09 对照 | 直接比较自动电路发现的性能与计算代价 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 优势依赖线性近似、任务集合和 circuit-recovery 指标；不能写成在所有 MI 目标上普遍更优 | 高 | awaiting-human |
| MI-C16 · Principled SAE Evaluations | RQ-C、RQ-A；在 GPT-2 small IOI 上，SAE 特征虽可解释，但控制模型不如监督字典，并出现 feature occlusion 与 over-splitting | 对比证据 | 建议纳入 RQ-C | 为 SAE 评价提供 approximation、control、interpretability 三轴及明确失败模式 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 结果限于 IOI、GPT-2 small 与特定 SAE；监督字典也依赖任务标签，不能当普适 ground truth | 高 | awaiting-human |
| MI-C17 · Comparative Faithfulness Metrics | RQ-C；常用 faithfulness metrics 会给出冲突排序，sufficiency/comprehensiveness 在本文诊断性与计算代价指标上表现较好 | 对比证据 | 建议仅留 RQ-C 方法线索 | 提醒评价指标本身需要被评价，不能用单指标宣称解释忠实 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 研究对象主要是 NLP post-hoc explanations，不等同 MI 电路评价；指标结论不能直接迁移到 SAE 或 causal abstraction | 高 | awaiting-human |
| MI-C18 · Scaling and Evaluating SAEs | RQ-C；k-sparse SAE 改善 reconstruction–sparsity frontier，并报告随 autoencoder 规模变化的 scaling laws 与特征质量指标 | 主证据 | 建议纳入 RQ-C | 直接覆盖 SAE 训练规模、dead latents 与评价指标 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 最大规模实验使用 GPT-4 激活，部分模型与数据不可独立复现；代理指标改善不等于机制解释已验证 | 高 | awaiting-human |
| MI-C19 · Progress Measures for Grokking | RQ-C、RQ-D；对模加 grokking 的机制分解产生连续 progress measures，将训练分成 memorization、circuit formation 与 cleanup | 主证据 | 建议纳入 RQ-C | 展示 MI 不只解释终态，还能构造训练过程指标 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 完整逆向工程发生在小型 transformer 的模加任务；不能外推一般涌现能力都有同类三阶段机制 | 高 | awaiting-human |

### RQ-D｜安全、控制与失效分析

| 编号 | AI 建议问题簇/拟用主张 | AI 建议预期证据角色 | AI 建议筛选动作 | AI 建议纳入理由 | 原核验状态 | AI 建议核验状态 | 原文定位 | AI 建议 caveat/允许主张 | 置信度 | 人工确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C25 · ReDeEP | RQ-D；在论文 RAG 设置中，作者把幻觉与 Knowledge FFNs、Copying Heads 的相对作用联系起来，并据此提出检测与缓解方法 | 主证据 | 建议纳入 RQ-D | 是池中直接把 MI 机制假设用于幻觉检测和干预的核心实证论文 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 允许主张限于论文模型、数据集和 RAG 冲突场景；不能写成已建立所有幻觉的统一因果机制 | 高 | awaiting-human |
| MI-C28 · Repeated Data | RQ-D；少量高频重复数据可损害泛化，并伴随 copying/induction-head 相关结构受损，形成一个可能机制 | 补充证据 | 建议仅留 RQ-D 线索 | 展示 MI 如何分析训练数据失效，而非只解释静态任务 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 作者把 induction-head 损伤表述为“possible mechanism”；不能升级为唯一因果解释，也不是直接安全评测 | 高 | awaiting-human |

### RQ-E｜跨模态与跨领域迁移

| 编号 | AI 建议问题簇/拟用主张 | AI 建议预期证据角色 | AI 建议筛选动作 | AI 建议纳入理由 | 原核验状态 | AI 建议核验状态 | 原文定位 | AI 建议 caveat/允许主张 | 置信度 | 人工确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C26 · InterPLM | RQ-E、RQ-A；ESM-2 的 SAE features 与多类已知蛋白概念相关，并可用于缺失注释和定向生成实验 | 主证据 | 建议纳入 RQ-E | 将 SAE 特征发现从自然语言迁移到蛋白质模型，并提供已知概念对照 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | 正确 InterPLM PDF p.1 摘要 | 与已知注释的相关及模型 steering 不等于发现真实生物机制；“新 motif”需要独立生物实验验证 | 中 | awaiting-human |
| MI-C30 · Mechanistic Biology / InterProt | RQ-E、RQ-A；在 ESM-2 上训练的 SAE 得到 generic 与 family-specific features，并用线性 probing 连接部分已知蛋白性质 | 主证据 | 建议纳入 RQ-E，并与 MI-C26 对照 | 提供独立团队的蛋白质 SAE 方法、工具和假设生成路线 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PMLR 正式版 p.1 摘要 | 未知 feature 的功能是待实验检验的假设，不是已发现生物机制；引用应使用 ICML/PMLR 正式版 | 中 | awaiting-human |
| MI-C32 · BLIP Causal Tracing | RQ-E；作者把语言模型 causal tracing 工具适配到 BLIP，并在 VQA 中观察后层表示的因果相关性 | 主证据 | 建议纳入 RQ-E | 是从单模态语言模型向 vision-language 架构迁移的直接工具案例 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 仅展示 BLIP 与一个 VQA 设置，且主要是工具和初步结果；不能证明多模态 MI 已普遍可用 | 高 | awaiting-human |
| MI-C34 · Multimodal MI Survey | RQ-E、RQ-F；该综述整理 LLM 方法向多模态基础模型的适配、机制差异与研究缺口 | 补充证据 | 建议纳入 RQ-E 的导航层 | 可用于组织跨模态方法族和识别缺口，不承担单项效果主张 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要 | 这是综述分类，不是原始实验；其“gap”判断需回查所引一手论文 | 高 | awaiting-human |
| MI-C35 · Scale Alone Does Not Improve MI in Vision | RQ-E、RQ-C；在九个视觉模型及其 psychophysical 指标上，模型/数据规模增加未提高所测的一种机制可解释性 | 对比证据 | 建议纳入 RQ-E/RQ-C | 直接反驳“模型规模自然带来更可解释表示”的假设 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.1 摘要 | 只测一种以人类判断为核心的可解释性范式和九个视觉模型；不能概括所有 MI 方法或所有模态 | 高 | awaiting-human |

### RQ-F｜开放问题、概念边界与治理含义

| 编号 | AI 建议问题簇/拟用主张 | AI 建议预期证据角色 | AI 建议筛选动作 | AI 建议纳入理由 | 原核验状态 | AI 建议核验状态 | 原文定位 | AI 建议 caveat/允许主张 | 置信度 | 人工确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C15 · Faithfully Interpretable NLP Systems | RQ-F、RQ-C；论文主张 faithfulness 应与 plausibility 分开评价，并反对简单二元化定义 | 对比证据 | 建议仅留 RQ-F 概念线索 | 为“可读解释不等于忠实解释”提供早期概念框架 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要 | 这是 NLP interpretability 的 opinion piece，不是 MI 专属实证研究；允许主张仅为作者提出的区分与建议 | 高 | awaiting-human |
| MI-C20 · MI for AI Safety Review | RQ-F、RQ-D；综述将 MI 的安全潜力与 capability gain、dual use、scalability、automation 等风险和障碍并列讨论 | 补充证据 | 建议纳入 RQ-F 的安全议程层 | 能避免只讲安全收益而不呈现双用与规模化风险 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要 | 综述对安全潜力的讨论不是系统的效果验证；允许主张是“该文评述这些机会与风险” | 高 | awaiting-human |
| MI-C21 · Open Problems in MI | RQ-F；多作者前瞻综述把问题分为方法改进、目标应用与社会技术挑战 | 主证据 | 建议纳入 RQ-F | 直接回答“该领域认为哪些问题仍未解决”，并显式承认许多收益尚未实现 | pending（身份已核；拟用主张待核） | `verified-with-caveat` | PDF p.2 摘要 | 属观点综合和研究议程，不证明列出的优先级客观完备；作者观点也不必代表所属机构 | 高 | awaiting-human |
| MI-C23 · Practical Review | RQ-F；综述以任务为中心组织 MI 对象、技术、评价与挑战，并给出新手路线图 | 补充证据 | 建议纳入 RQ-F 的导航层 | 可作为问题簇与术语表的二级索引，帮助回到一手论文 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要 | 综述不承担被引方法的效果主张；其分类和未来方向是作者组织框架 | 高 | awaiting-human |
| MI-C27 · Mechanistic? | RQ-F；作者区分“mechanistic”的四种技术/文化用法，指出术语多义性 | 对比证据 | 建议纳入 RQ-F | 直接揭示“是否 mechanistic”可能混合因果标准与社群身份 | pending（身份已核；拟用主张待核） | `verified` | PDF p.1 摘要与 §2.1 | 这是术语史与概念分析，不评价具体方法效果；四分法是作者框架而非统一标准 | 高 | awaiting-human |
| MI-C33 · Explaining AI through MI | RQ-F；作者主张 MI 应借鉴生命科学的协调发现策略，以追求系统层面的功能理解 | 补充证据 | 建议纳入 RQ-F 的科学方法线 | 补充“MI 是怎样的科学发现实践”，而非仅是工具清单 | pending（身份已核；拟用主张待核） | `verified` | 正式期刊版 p.1 摘要 | 哲学论证不构成 MI 能提高安全性的实证证据；允许主张仅为作者提出的方法论立场 | 高 | awaiting-human |
| MI-C36 · Bridging the Black Box Survey | RQ-F、RQ-C；综述按 neurons、circuits、algorithms 三层及 behavioral、counterfactual、causal 三类评价视角组织领域 | 补充证据 | 建议纳入 RQ-F 的分类层 | 提供较新的正式综述和评价维度，可与 MI-C20/23 交叉审计 | pending（身份已核；拟用主张待核） | `verified` | ACM CSUR 正式版 p.1 摘要 | 综述框架不是领域共识或一手效果证据；引用应锁定 DOI `10.1145/3787104` 正式版 | 中 | awaiting-human |

## 四、AI 汇总建议

### 1. 各问题簇的优先入口

| 问题簇 | 建议先精读 | 必须同时保留的边界或对比证据 |
| --- | --- | --- |
| RQ-A | MI-C01、MI-C02、MI-C03 | MI-C14、MI-C16、MI-C29；区分玩具机制、代理指标与真实模型因果性 |
| RQ-B | MI-C08、MI-C22、MI-C24 | MI-C11、MI-C13、MI-C31；尤其保留 patching illusion 与证据强度分层 |
| RQ-C | MI-C04、MI-C09、MI-C18 | MI-C10、MI-C16、MI-C17；不要把单一 proxy 或 circuit-recovery AUC 当作完整评价 |
| RQ-D | MI-C25 | MI-C20、MI-C21、MI-C28；当前直接安全应用证据较少，安全收益多来自议程与综述 |
| RQ-E | MI-C26、MI-C30、MI-C32 | MI-C34、MI-C35；跨模态迁移需保留单任务、单指标和生物验证缺口 |
| RQ-F | MI-C21、MI-C27、MI-C36 | MI-C15、MI-C20、MI-C33；区分实证结果、综述分类、哲学立场与社群术语 |

### 2. 当前证据缺口

- RQ-A：缺少跨模型、跨任务、带独立人工或因果 ground truth 的 SAE 特征稳定性验证。
- RQ-B：少量机制案例具有较强干预证据，但尚不足以证明复杂开放行为可被完整、唯一地定位。
- RQ-C：评价指标分散且可能冲突；proxy 改善、重构改善与解释忠实性之间尚无统一转换规则。
- RQ-D：池中直接把 MI 用于安全结果的实证主要集中在 RAG 幻觉等有限场景；“MI 提高总体安全”仍是待验证主张。
- RQ-E：跨模态与蛋白质案例已出现，但领域 ground truth、外部实验验证和跨架构复现仍不足。
- RQ-F：综述和概念论文较多，不能用其数量替代一手实验证据。

### 3. 待人工确认块

```text
待确认：RQ-A–RQ-F 的保留、合并或改写；
MI-C01–MI-C36 → 建议纳入 / 建议仅留线索；
MI-C01–MI-C36 → AI 建议核验状态、预期证据角色与 caveat；
优先精读编号与所采用的正式版本。

未经确认：原 trace 的正式状态不变；不写正式候选表。
```

## 五、AI 使用记录

| 字段 | 记录 |
| --- | --- |
| 用途 | 为原 MI 线索表建立独立的 AI 建议叠加层 |
| Context | 原 trace v0.5.1、讲义 v1.4.0 的四态/角色规则、本地 Zotero MI 集合的 36 篇公开论文 PDF |
| AI 输出用途 | 候选问题、角色、筛选、核验状态与 caveat 建议；供研究负责人审阅 |
| 人工核验方式 | 逐条回 PDF 摘要或指定章节；核对题名、稳定标识、版本与允许主张；确认后另行写入正式工件 |
| 已发现问题 | Zotero 的 MI-C26、MI-C36 原挂历史错附件，MI-C30 原挂 bioRxiv 旧版；2026-08-20 已换为裁决后的正确版本，旧附件进入 Zotero 回收站并在 `.work` 留存备份，旧 WebDAV 对象已清除 |
