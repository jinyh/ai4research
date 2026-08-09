---
版本：v0.1.1
最后更新：2026-08-09
适用课次：第 3 课（教师演示与断网备用；第 12 课八要素拆解可引用）
文档类型：真实检索方法与失败演示包（MI 方向地图）
变更记录：
- v0.1.1 (2026-08-09): 将尚无研究问题、尚未筛选的 17 条记录改称“待筛选线索表”，避免与本课候选文献表进入规则混淆；事实记录不变
- v0.1.0 (2026-08-09): 首版——2026-08-09 MI 宽泛主题检索 trace：分支确定方法审计、待筛选线索 17 条（全部 pending-身份已核）、4 条真实幻觉引用 rejected 实例；方向收敛段待博士生真实方向指认后升 v1
---

# MI 方向地图：检索纪律与幻觉审计 trace

> 案例边界框：本文件是 **AI agent 与教师于 2026-08-09 对 Mechanistic Interpretability（MI）主题执行检索的真实 trace**，全部材料为公开 arXiv 元数据，不含任何未发表内容。它与 [source-audit-demo.md](./source-audit-demo.md)（Keshav 2007 单篇核验 trace）互为平行：那一篇演示单篇文献的身份核验，本篇演示领域级检索的框架审计与失败处理。学生练习仍使用讲义 §四·5 的虚构案例，不直接修改本文件。

## 1. 本 trace 的三个教学点

1. **检索框架本身也要审计**：检索分支不是先验给定的。Agent 凭记忆预设的分支划分只是线索，必须用领域数据校验（§3 的 v1→v2 修正表）。
2. **Agent 的记忆引用是幻觉高发区**：Agent 凭记忆给出的 11 个锚点论文 ID 中 6 个身份不符，其中 4 个是彻底的张冠李戴（§6）。全部按 `rejected` 处置并留下恢复路径——失败不重跑到无痕。
3. **四态口径全程生效**：未做主张层核验的条目一律 `pending`（注明身份已核）；`rejected` 永不入候选表，只留审计记录。状态名用精确拼写，无缩写。

## 2. 检索记录

| 字段 | 宽泛检索 | 分支检索（B1-B6） |
| --- | --- | --- |
| 库 | arXiv API | arXiv API |
| 检索式 | `all:"mechanistic interpretability" AND (cat:cs.LG OR cat:cs.CL)` | 见 §3 表 |
| 检索日期 | 2026-08-09 | 2026-08-09 |
| 时间范围 | 排序取最新 200 条（`submittedDate` 降序） | 相关度排序各取前 6 条 |
| 命中数 | 688（总命中；取样 200） | B1 664 / B2 377 / B3 226 / B4 86 / B5 104 / B6 532 |
| 纳入/排除标准 | 题名词频统计用于分支校验，不做论文级纳入 | 锚点选取后逐条做身份核验（§5） |
| 纳入数 | 分支修正 3 增 1 降级（§3） | 17 条身份已核候选（§5） |

## 3. 教学点一：分支如何确定——记忆先验 vs 数据校验

v1 六个分支由 Agent 凭记忆中 MI 子领域划分预设（SAE/探针/电路/induction heads/monosemanticity/忠实性）。按课程口径这是**探索线索**，不是领域结构证据。校验方法：宽泛检索最新 200 条题名做词频统计，与 v1 分支对照：

| 数据信号（200 条题名词频） | 对 v1 的修正 |
| --- | --- |
| causal 13、circuit 12、attribution 7、patching 3 | B3 电路方向成立 |
| sparse autoencoder/SAE/feature/superposition（B1 专查命中 664） | B1 成立；近期题名 SAE 词频下降系题名专门化，不是方向衰退 |
| evaluation 5 + faithfulness | B6 成立 |
| induction heads / in-context（B4 专查 86 条） | B4 成立 |
| monosemanticity（B5 专查 104 条） | B5 成立 |
| **steering 10、alignment 8、safety 2** | **v1 遗漏**：增 B7 表示引导/对齐 |
| **reasoning 9、chain-of-thought 3** | **v1 遗漏**：增 B8 推理与 CoT 机制解释 |
| **vision 4**（另有物理 jet-tagger、等变性等应用条目） | **v1 遗漏**：增 B9 非文本模态 MI 应用 |
| probing 在最新题名中仅 1 次 | B2 降级为方法基础线：历史锚点有效，但非近期前沿话语中心 |

B7-B9 锚点待研究问题收敛后按题名精确检索核验，不在指认前预造。

## 4. 分支检索式（可复盘）

| 分支 | arXiv 检索式 | 命中 |
| --- | --- | ---: |
| B1 SAE/特征提取 | `all:"sparse autoencoder" AND (cat:cs.LG OR cat:cs.CL)` | 664 |
| B2 探针/线性表示 | `(all:"linear probes" OR all:probing) AND all:"language model" AND (all:interpretability OR all:"mechanistic interpretability") AND (cat:cs.LG OR cat:cs.CL)` | 377 |
| B3 电路发现 | `all:"circuit discovery" OR all:"activation patching" AND (cat:cs.LG OR cat:cs.CL)` | 226 |
| B4 Induction heads | `all:"induction heads" AND (cat:cs.LG OR cat:cs.CL)` | 86 |
| B5 Monosemanticity | `all:monosemanticity OR all:"scaling monosemanticity"` | 104 |
| B6 忠实性/评价 | `all:interpretability AND (all:faithfulness OR all:fidelity) AND all:evaluation AND (cat:cs.LG OR cat:cs.CL)` | 532 |

## 5. 待筛选线索表（全部 `pending`-身份已核；主张层未做）

身份核验方式：arXiv `id_list` 精确查询，题名/作者/日期以 API 元数据为准。证据角色默认探索线索；纳入/排除待研究问题收敛后由教师确定。由于还没有可检索的问题初稿和拟用主张，本表不是讲义 §五 所定义的候选文献表。

| 编号 | 题名（核验后） | 作者 | 年份 | 来源 | 证据角色 | 纳入/排除 | 理由 | 核验状态 | caveat/允许主张 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MI-C01 | Toy Models of Superposition | Elhage et al. | 2022 | arXiv:2209.10652 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C02 | Sparse Autoencoders Find Highly Interpretable Features in Language Models | Cunningham et al. | 2023 | arXiv:2309.08600 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C03 | Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2 | Lieberum et al. | 2024 | arXiv:2408.05147 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C04 | Jumping Ahead: Improving Reconstruction Fidelity with JumpReLU Sparse Autoencoders | Rajamanoharan et al. | 2024 | arXiv:2407.14435 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C05 | Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models | Marks et al. | 2024 | arXiv:2403.19647 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C06 | Eliciting Latent Predictions from Transformers with the Tuned Lens | Belrose et al. | 2023 | arXiv:2303.08112 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C07 | Emergent Linear Representations in World Models of Self-Supervised Sequence Models | Belrose, Nanda et al. | 2023 | arXiv:2309.00941 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C08 | Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small | Wang et al. | 2022 | arXiv:2211.00593 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C09 | Towards Automated Circuit Discovery for Mechanistic Interpretability | Conmy et al. | 2023 | arXiv:2304.14997 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C10 | Attribution Patching Outperforms Automated Circuit Discovery | Syed et al. | 2023 | arXiv:2310.10348 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C11 | How to use and interpret activation patching | Heimersheim et al. | 2024 | arXiv:2404.15255 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C12 | Successor Heads: Recurring, Interpretable Attention Heads In The Wild | Gould et al. | 2023 | arXiv:2312.09230 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C13 | In-context Learning and Induction Heads | Olsson et al. | 2022 | arXiv:2209.11895 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C14 | Engineering Monosemanticity in Toy Models | Jermyn et al. | 2022 | arXiv:2211.09169 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C15 | Towards Faithfully Interpretable NLP Systems: How should we define and evaluate faithfulness? | Jacovi & Goldberg | 2020 | arXiv:2004.03685 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C16 | Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control | Makelov et al. | 2024 | arXiv:2405.08366 | 探索线索 | 待定 | | pending（身份已核） | |
| MI-C17 | A Comparative Study of Faithfulness Metrics for Model Interpretability Methods | Chan et al. | 2022 | arXiv:2204.05514 | 探索线索 | 待定 | | pending（身份已核） | |

## 6. 教学点二：审计失败实例（真实发生，本 trace 原生）

Agent 凭记忆提出 11 个锚点 ID，4 个张冠李戴（`rejected`），2 个 ID 正确但记忆题名有误（以 API 元数据修正），1 个题名记忆不全（精确题名检索无命中，关键词检索恢复）。失败全部保留，恢复路径留档：

| 记忆条目 | 核验结果 | 处置 | 恢复路径 |
| --- | --- | --- | --- |
| 2308.10939＝Attribution Patching | 实为凝聚态物理论文 | rejected（ID 记忆错误） | `ti:` 检索恢复 → 2310.10348 |
| 2203.13787＝Tuned Lens | 实为混合序列预测论文 | rejected（ID 记忆错误） | `ti:` 检索恢复 → 2303.08112 |
| 2309.10655＝Emergent Linear Representations | 实为路径规划论文 | rejected（ID 记忆错误） | `ti:` 检索恢复 → 2309.00941 |
| 2407.14400＝Gemma Scope | 实为 O-RAN 预测论文 | rejected（ID 记忆错误） | `ti:` 检索恢复 → 2408.05147 |
| 2312.09230＝Successor Heads（副标题记错） | ID 正确，题名以 arXiv 元数据为准 | 身份通过，题名修正 | 元数据修正 |
| 2405.08366＝SAE 评价（副标题记错） | ID 正确，题名以 arXiv 元数据为准 | 身份通过，题名修正 | 元数据修正 |
| "JumpReLU Autoencoders"（题名记忆不全） | 精确题名检索无命中 | 线索保留 | 关键词检索恢复 → 2407.14435 |

课堂用法：与讲义 §四·5 的虚构表（论文 A-E）对照——虚构表练习状态判断，本表展示真实审计中 `rejected` 的发生率与恢复动作。结论不是"AI 不可用"，而是：**记忆与模型输出只能作线索，身份核验必须回到正式来源**。

## 7. 非 arXiv 锚点（pending 线索，URL 待人工核验）

| 条目 | 来源类型 | 状态 |
| --- | --- | --- |
| Anthropic "Towards Monosemanticity"（2023-10） | 机构研究报告（transformer-circuits.pub） | pending：非 arXiv，URL 与身份待人工核验 |
| Anthropic "Scaling Monosemanticity"（2024-05） | 机构研究报告 | pending：同上 |
| OpenAI "Scaling and evaluating sparse autoencoders"（Gao et al., 2024） | 机构技术报告 | pending：无 arXiv 版本，URL 待人工核验 |

## 8. 复盘方式

任意一条检索式可在 arXiv API 复盘，例如分支 B1：

```text
http://export.arxiv.org/api/query?search_query=all:%22sparse+autoencoder%22+AND+(cat:cs.LG+OR+cat:cs.CL)&max_results=6
```

单条身份核验：

```text
http://export.arxiv.org/api/query?id_list=2209.10652
```

命中数随时间变化属正常差异；复盘时记录自己的检索日期与命中数，与原记录对照。教师生产 trace 的原始 JSON 存档于课程工作区 `.work/mi-search/`（不发布）。

## 9. 与课程的连接

- 讲义 §四 四态与进入规则：本文件全部条目按该口径标注；
- 讲义 §六 常见错误 5（检索过程不可复盘）：§2/§4/§8 给出可复盘记录的最小完整样式；
- 课程 2.0 批次 0 验收项"≥1 条真实科研失败演示"（见课程文档 `docs/course-2.0-plan.md`）：§6 提供 4 条；
- 方向收敛段（从宽泛主题到具体研究问题的第 1-4 步）待博士生真实方向指认后补入本文件并升版。
