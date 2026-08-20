---
版本：v1.0.0
最后更新：2026-08-20
适用课次：第 4 课教师演示；第 5-6 课可继续引用
文档类型：公开论文主张级精读卡示例
---

# MI 精读卡示例：SAE 的因果有效性

> 案例边界：以下内容只使用公开论文和公开仓库元数据，是课程教师演示线。它不包含博士生未发表问题、结果或失败日志；学生仍用自己的论文完成课堂练习。

## 共同研究问题

在 Pythia-410M 的 IOI 任务上，SAE 特征能否比 PCA 方向更稀疏地定位并干预模型行为；这种 patching 成功还需要哪些证据，才能支持“因果忠实”的解释？

## 卡 1｜MI-C02：正向主证据

- 完整书目信息：Cunningham et al. *Sparse Autoencoders Find Highly Interpretable Features in Language Models*. arXiv:2309.08600v3, 2023；ICLR 2024 版作者顺序不同，本卡固定 arXiv v3。
- 来源核验状态：`verified-with-caveat`。
- 证据角色：主证据（同任务直接比较）。
- 中心问题：任务无关训练的 SAE 特征是否比 PCA 更细粒度地定位 IOI 行为？
- 作者主张：在 Pythia-410M layer 11 的 IOI 设置中，稀疏字典以更少 patch 和更小 edit magnitude 达到给定目标 KL，优于 PCA 与非稀疏字典。
- 原文位置：p.5 §4 与 Fig.3；p.6 §4.1-4.2。
- 设置与证据：字典在 Pile 前 10,000 个元素上训练；ACDC 排序特征；50 个 IOI 测试点；比较 patched output 与 counterfactual target 的 KL divergence。
- 作者自述局限：p.6 指出更高 sparsity coefficient 会降低 reconstruction accuracy；p.9 §6.2 报告在 Pythia-70M layer 2 用重构替换激活时 perplexity 从 25 升至 40，并明确跨相似任务泛化仍需验证。
- 个人判断：可支持“该设置下 SAE patching 比 PCA 更稀疏有效”；不能直接支持“SAE 特征就是模型正常计算中的因果变量”。
- AI 初始阅读地图（未核验示例）：把 Fig.3 概括为“SAE 证明了因果忠实”。
- 偏差审计：`patching 更有效` 被过度概括成 `因果忠实`；原文比较的是 intervention efficiency，尚未排除替代路径与重构误差影响。
- 最终人工判断：纳入证据地图主格，状态保持 `verified-with-caveat`。

## 卡 2｜MI-C16：控制性限制证据

- 完整书目信息：Makelov, Lange, Nanda. *Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control*. arXiv:2405.08366v3, 2024。
- 来源核验状态：`verified-with-caveat`。
- 证据角色：对比/限制证据。
- 中心问题：SAE 学到的可解释特征，是否也能在特定任务上稀疏控制模型？
- 作者主张：在 GPT-2 Small IOI 上，任务特定和全分布 SAE 都能找到可解释特征，但控制能力弱于监督字典；论文还观察到 feature occlusion 与 feature over-splitting。
- 原文位置：pp.1-2 摘要与贡献；p.11 §5.2 随机特征对照；pp.13-14 §5.3-5.4 对 occlusion/over-splitting 的分析。
- 设置与证据：以监督字典提供近似、控制和解释的任务参照；冻结随机 decoder 的 SAE 作为非平凡控制对照。
- 局限：模型是 GPT-2 Small，SAE 与 C02 的实现、训练分布和控制协议不同。
- 个人判断：可反驳“可解释自动推出可控制”的一般化；不能写成对 C02 同设置结果的直接复现失败。
- AI 初始阅读地图（未核验示例）：把结论概括为“SAE 在 IOI 上无效”。
- 偏差审计：忽略了普通 SAE 优于冻结随机特征，并把“弱于监督字典”强化为“无效”。
- 最终人工判断：进入冲突/限制视图，要求 L9 增加监督或随机特征对照。

## 卡 3｜MI-C31：patching 效度威胁

- 完整书目信息：Makelov, Lange, Nanda. *Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching*. arXiv:2311.17030, ICLR 2024。
- 来源核验状态：`verified-with-caveat`。
- 证据角色：冲突/效度威胁证据。
- 中心问题：子空间 patching 的成功是否一定表示找到了模型正常使用的变量？
- 作者主张：子空间 intervention 可能通过 normally dormant pathway 创造出一个能改变输出的变量；论文同时给出 IOI 中的幻觉案例和经额外机制实验支持的成功案例。
- 原文位置：pp.1-4 摘要与 §1，尤其 Fig.1 的几何说明；pp.4-5 的贡献总结与相关工作。
- 设置与证据：理论构造、IOI 子空间案例、事实编辑案例，以及 residual-stream success case。
- 局限：论文研究一般子空间 patching，并未在 C02 的 SAE 字典、Pythia-410M layer 11 上做同设置实验。
- 个人判断：它要求把 `patching success` 与 `causal faithfulness` 分开评价；不支持“所有 patching 都无效”。
- AI 初始阅读地图（未核验示例）：把论文概括为“activation patching 不适合可解释性”。
- 偏差审计：删去了论文明确呈现的成功案例和“需要额外证据”的限定。
- 最终人工判断：进入证据地图冲突格，并转写为 L7-L9 的效度假设与对照。

## 两条补充卡索引

| 编号 | 作用 | 已核位置 | 允许主张 |
| --- | --- | --- | --- |
| MI-C18 | 评价框架 | p.1；p.8 §4.5 | 重构与稀疏度不是最终目标，应补 feature recovery、解释性和 downstream-effect sparsity；不单独证明因果忠实 |
| MI-C05 | 下游应用 | pp.1-2；p.6 §3.2；p.8 §4 | SAE feature circuits 可做 held-out faithfulness/completeness 与 SHIFT 干预；任务/模型不同，只作外部支持 |

## 从阅读卡到第 5 课

三张卡不按“论文 1/2/3”顺序写综述，而按一个判断组织：C02 支持 `SAE patching 更稀疏有效`；C16 限定 `可解释不等于可控制`；C31 限定 `patching 成功不等于因果忠实`。下一课把这三条关系重组为支持、限制、冲突与缺失证据。

来源边界与许可见 [MI registry](../../references/notes/mi-case-registry.md)；上游检索与升级记录见 [MI search trace](../lesson-03/mi-search-trace-demo.md) §5。
