# IOI 检索运行记录与课堂原始输入

版本：v1.0.0
记录日期：2026-10-15

## 记录身份

本记录来自课程备课时 Codex Agent 的实际 `web.run` 调用。原始工具响应由教师保存，课堂材料提供公开请求和可复查的结果元数据。本页保存可分发的请求与结果元数据节选，全文以原始来源为准。工具未提供搜索引擎身份、索引版本、相似度、搜索总命中数或计费数据，均记 N/A；没有测得可比较的时间或费用优势。

研究问题：GPT-2 small 的 IOI 干预及跨模板迁移与解释。给定种子：arXiv:2211.00593，来自课程，先于本轮查询。纳入建议标准：与任务、干预方法、评价或解释失效相关的原始学术研究；代码与教程另记线索。筛选建议由 AI 产生，正式纳入与状态由使用者回源确认。

## 输入 A：首轮搜索

接口：`web.run.search_query`。参数：

```json
{"q": "\"indirect object identification\" \"activation patching\" site:arxiv.org"}
```

实际使用的字符串是 `"indirect object identification" "activation patching" site:arxiv.org`。`response_length` 为 `long`。本次可见返回 4 条，按工具显示顺序如下；它们不是已确认纳入的候选表。

| 顺序 | arXiv ID | 返回题名 | 后续审计范围 |
| --- | --- | --- | --- |
| 1 | [2605.22462](https://arxiv.org/abs/2605.22462) | From Correlation to Cause: A Five-Stage Methodology for Feature Analysis in Transformer Language Models | 本课未核主张，pending |
| 2 | [2311.17030](https://arxiv.org/abs/2311.17030) | Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching | 打开原文，供入口核验 |
| 3 | [2608.03629](https://arxiv.org/abs/2608.03629) | Cross-Layer Interaction under Weight-Space Ablation: A Closed-Form Attention Jacobian Bound and a Test on a Real Pretrained Model | 本课未核主张，pending |
| 4 | [2508.21258](https://arxiv.org/abs/2508.21258) | RelP: Faithful and Efficient Circuit Discovery via Relevance Patching | 本课未核主张，pending |

## 输入 B：来源与可追踪关系

给定种子 [IOI v1](https://arxiv.org/html/2211.00593v1) 的 References 有 Geiger 等 (2021) 的 *Causal Abstractions of Neural Networks*，链接指向 [OpenReview](https://openreview.net/forum?id=RmuXDtjDhG)。本次沿链接访问返回浏览器验证页面，没有获得论文正文。记录为访问受阻，不给文献标 rejected。

后续题名查询：`"Causal Abstractions of Neural Networks" site:arxiv.org`。该请求返回 5 条可见结果，目标文献 [2106.02997](https://arxiv.org/abs/2106.02997) 列在首位，其余四条为 2403.07809、2403.00745、2307.02477、2307.09458，均未继续筛选。本轮只对目标文献打开摘要页，核对 Atticus Geiger、Hanson Lu、Thomas Icard、Christopher Potts，2021 年。目标摘要描述因果抽象与 interchange interventions，任务含 MQNLI。

这是从种子后向引文发现、再用题名恢复入口的一条分支。目标 Geiger 文献是相对首轮返回新增的 1 条方法线索；该数字只覆盖此选查分支。种子单列，另外四个恢复查询结果不计作新增相关文献。原始请求按实际工具接口可重做，未来排序和数量可能变化。

## 输入 C：两条原文审计入口

| 编号 | 身份入口 | 原文位置 | 供学生核对的拟用主张 |
| --- | --- | --- | --- |
| S1 | Wang 等，arXiv:2211.00593，2022 预印本／ICLR 2023 | [v1 摘要与 §4](https://arxiv.org/html/2211.00593v1) | 该研究分析 GPT-2 small 的 IOI 电路并检查解释的可靠性 |
| S2 | Makelov、Lange、Nanda，arXiv:2311.17030，2023 预印本 | [v2 摘要与 §4–5](https://arxiv.org/html/2311.17030v2) | 子空间干预有效仍可能出现解释幻觉，额外验证可以区分情形 |

学生应自行定位原文，记录状态、允许主张与处理决定。两个入口可以都通过，不要求制造错误。以上记录是历史运行输入，不代表学生本人已执行。

## 能力与覆盖

- 实际执行：通用搜索、原文后向引文选择、链接访问及失败恢复、身份与原文入口检查。
- 专门语义检索：未执行。自然语言表达 `Which interventions recover indirect-object predictions across prompt templates?` 仅为待运行输入，不附假想结果。
- 前向引文：检查 S2 引用 IOI 的关系可作为局部关系核验；本次未系统遍历所有引用 IOI 的工作。
- 完整性基准：只有给定 IOI 种子，未独立建立完整 must-find 集。
- 筛选尚待使用者确认。条目可以保留待核状态，来源排序不等于纳入依据。
