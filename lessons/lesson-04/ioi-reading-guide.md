# IOI 精读输入与代码定位

版本：v1.2.0；核验日期：2026-10-21。

本页提供原始输入与定位入口，供学生形成自己的判断。原文使用 Wang 等 *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small*，[arXiv:2211.00593v1](https://arxiv.org/html/2211.00593v1)，预印本 2022 / ICLR 2023。L3 的检索记录见[上游输入](../lesson-03/ioi-retrieval-record.md)。

## 阅读起点

先读摘要与 §1，说明作者要解释 GPT-2 small 的哪项行为，以及用什么方法建立和检验解释。随后读 §2 的 IOI 输入：John 和 Mary 同行，John 给东西给……，目标为 Mary；John 是重复主语 S，Mary 是 IO。此句是任务说明，不是新的模型运行。

**读图所需定义：**M 是完整模型，C 是候选电路，K 是从 C 中选出的节点集合。F 是 IOI 样本上的平均 logit(IO)−logit(S)。C∖K 与 M∖K 都移除同组 K，但前者还消融 C 外节点。“移除”按 §2.1 用 p_ABC 同模板样本的平均激活替换，p_ABC 使用三个不同名字；不删除参数。F 衡量两名字间偏好，不是准确率。

§4 的评价从保留任务表现，继续追问解释是否遗漏、组件是否有作用。以上术语先提供；Fig.6(a) 中哪些结果支持或限制解释，由你读原文判断。

## 待判断问题

移除同一组组件后，候选电路与完整模型的表现为什么可能不同？先读 Fig.6(a) 的轴、点和对角线，回查 §2.1 与 §4.1 的操作与采样。自行形成解释，标出证据与推断，再提出下一项检查。本页供初判使用；作答后的完整解析在教师校准后发放的讲义中。

这是教师 MI Demo 的输入；本人精读卡使用与自己研究问题相关的材料，见[个人阅读输入](./personal-reading-inputs.md)。

本课代码比较限定为 `run.py` 的默认 residual 分支和 `policy-baseline.json`；新增注意力头分支另供后续教师实验，不混用其干预语义。

## 原文入口

| 原文位置 | 阅读任务 |
|---|---|
| 摘要 / §1 | 用自己的话概括问题、贡献与检验路线 |
| §2 Task description | 找到任务对象、名字角色与指标定义 |
| §2.1 | 核对 knockout 的替换值、参考分布和模板条件 |
| §3.1 / Appendix B（另行代码比较） | 确认 path patching 改什么、保持什么 |
| §4 / §4.1 / Fig.6(a) | 读轴、点与比较基准，判断作者检查了哪种缺口 |
| §4.2 / §5 | 按本人主张需要补查组件作用与研究局限 |

至少两个位置应承担不同作用：支持结果、限定设置或检验解释。章节与图号优先于未实际核对的 PDF 页码。

## 代码入口（按需，不占共同诊断任务）

课程代码：[run.py](../lesson-09/assets/mi-ioi/run.py)，关注 `capture`、`hook`、`forward` 和生成 `row` 的位置。参数见 [policy-baseline.json](../lesson-09/assets/mi-ioi/policy-baseline.json)，指标与控制见 [protocol.json](../lesson-09/assets/mi-ioi/protocol.json)。

以下代码为本地文件中的实际语句摘录，中间省略初始化；不是独立可运行程序：

```python
layer = model.transformer.h[policy['layer']]
changed[:, pos, :] = replacement
return float(logits[target[0]] - logits[subject[0]])
```

解释每句分别选择了什么对象、替换了什么范围、如何计算输出。接着回到 `row` 查看 clean、corrupt、noop、random、patch 的输入区别。代码阅读不要求加载模型，实际效果应来自另行保存的真实运行记录。

## AI 导航输入

将以下任务连同允许使用的公开原文交给本人使用的 AI，记录工具或模型身份、实际输入与相关输出：

> 请只根据提供的 IOI 原文，概括研究问题、主要贡献及方法和评价的关系，给出候选章节与定位理由。请定位任务与指标、节点移除定义、完整性检验。没有读到的内容标待查；区分作者主张与自己的推断。此轮先建立阅读路线，不预判 Fig.6(a) 的结果或归因。

教师先展示一次实际输入和原始输出，打开摘要／§1核验其中一项问题或贡献描述，记录采用、修订或维持的理由。模型不可用时用本页原文入口导航，明确标为人工替代。核对至少两个原文位置后，再让 AI 提出一个可检查的质疑。共同诊断先记录理由；个人精读卡随后回到本人论文完成。没有可用模型时先用人工提问完成阅读诊断，真实 AI 动作按课程安排补齐并保留身份。

## 离线入口

课前下载公开原文，保留版本信息。课堂可使用本课已保存的 [Fig.2](./assets/ioi-circuit-original.svg) 和 [Fig.6(a)](./assets/ioi-completeness-original.svg)；原图能支持读图动作，不能替代未检查的全文结论。离线原文由教师准备，已有阅读卡不冒充本人新执行。

Fig.6(a)的点型须结合[原论文共用图例](./assets/ioi-completeness-legend-original.svg)读取。该文件完整保留子图(b)，只用右侧图例核对颜色／形状；子图(b)的散点属于naive circuit，不能当作(a)的数据。
