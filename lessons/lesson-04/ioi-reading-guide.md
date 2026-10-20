# IOI 精读输入与代码定位

版本：v1.1.0；核验日期：2026-10-20。

本页提供原始输入与定位入口，供学生形成自己的判断。原文使用 Wang 等 *Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small*，[arXiv:2211.00593v1](https://arxiv.org/html/2211.00593v1)，预印本 2022 / ICLR 2023。L3 的检索记录见[上游输入](../lesson-03/ioi-retrieval-record.md)。

## 待判断问题

移除同一组组件后，候选电路与完整模型的表现为什么可能不同？先读 Fig.6(a) 的轴、点和对角线，回查 §2.1 与 §4.1 的操作与采样。自行形成解释，标出证据与推断，再提出下一项检查。本页供初判使用；作答后的完整解析在教师校准后发放的讲义中。

这是教师 MI Demo 的输入；本人精读卡使用与自己研究问题相关的材料，见[个人阅读输入](./personal-reading-inputs.md)。

本课代码比较限定为 `run.py` 的默认 residual 分支和 `policy-baseline.json`；新增注意力头分支另供后续教师实验，不混用其干预语义。

## 原文入口

| 原文位置 | 阅读任务 |
|---|---|
| §2 Task description | 找到任务对象、名字角色与指标定义 |
| §2.1 | 核对 knockout 的替换值、参考分布和模板条件 |
| §3.1 / Appendix B（另行代码比较） | 确认 path patching 改什么、保持什么 |
| §4 / §4.1 / Fig.6(a) | 读轴、点与比较基准，判断作者检查了哪种缺口 |
| §4.2 / §5 | 按本人主张需要补查组件作用与研究局限 |

至少两个位置应承担不同作用：支持结果、限定设置或检验解释。章节与图号优先于未实际核对的 PDF 页码。

## 代码入口

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

> 这是教师 GPT-2 small IOI 演示。请围绕“候选电路与完整模型在移除同组组件后的差异”建立阅读地图，列出需要核对的原文位置和理由，区分论文方法与我提供的课程代码。尚未读到的位置标待查；先列候选解释及区分它们所需的证据。

核对至少两个原文位置后，再让 AI 提出一个可检查的质疑。共同诊断先记录理由；个人精读卡随后回到本人论文完成。没有可用模型时先用人工提问完成阅读诊断，真实 AI 动作按课程安排补齐并保留身份。

## 离线入口

课前下载公开原文，保留版本信息。课堂可使用本课已保存的 [Fig.2](./assets/ioi-circuit-original.svg) 和 [Fig.6(a)](./assets/ioi-completeness-original.svg)；原图能支持读图动作，不能替代未检查的全文结论。离线原文由教师准备，已有阅读卡不冒充本人新执行。

Fig.6(a)的点型须结合[原论文共用图例](./assets/ioi-completeness-legend-original.svg)读取。该文件完整保留子图(b)，只用右侧图例核对颜色／形状；子图(b)的散点属于naive circuit，不能当作(a)的数据。
