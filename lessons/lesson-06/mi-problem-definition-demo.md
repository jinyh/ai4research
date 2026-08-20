---
版本：v1.0.0
最后更新：2026-08-20
适用课次：第 6 课教师演示；第 7-9 课接口
文档类型：公开材料问题定义与问题门示例
---

# MI 问题定义示例：从证据缺口到 SAE-vs-PCA baseline

> 案例边界：这是基于公开论文构造的课程示例，不是博士生未发表研究计划或实验结果。状态为 `review`，所有命题都等待 L7-L9 的设计与运行。

## 结构性研究问题

在固定的 Pythia-410M layer 11、IOI 样本和 activation-patching 协议下，SAE 特征能否比 PCA 方向以更少 patch 与更小 edit magnitude 达到相同目标 KL；若能，这一结果在控制重构误差、held-out 样本与 dormant-pathway 替代解释后，是否仍支持这些特征对模型正常计算具有因果忠实性？

## 范围与非例

- 包含：Pythia-410M、layer 11 residual stream、IOI、SAE 与 PCA 对照、KL/edit magnitude/patch 数、重构敏感性与效度检查。
- 暂不包含：跨模型普遍性、自动特征语义标注质量、端到端安全结论、博士生未发表数据。
- 非例 1：在不同模型或不同任务上 SAE feature circuit 成功，不能直接回答本问题。
- 非例 2：单个特征能被人命名，不能单独回答因果忠实性。
- 非例 3：训练重构损失更低，不能替代行为干预与效度证据。

## 可证伪命题与竞争假设

| 编号 | 命题 | 推翻条件 | 竞争解释 |
| --- | --- | --- | --- |
| H-eff | 固定目标 KL 下，SAE 所需 patch 数和 edit magnitude 均低于 PCA | 预注册区间内任一主要指标不优于 PCA，或优势只在 cherry-picked 样本出现 | 特征选择/排序使比较偏向 SAE |
| H-rob | SAE 优势对重构误差控制与 held-out IOI 样本稳健 | 加入误差控制或 held-out 后优势消失/反转 | 优势由 reconstruction residual 或过拟合驱动 |
| H-faith | 有额外机制证据表明 patching 沿模型正常使用的路径起效 | 随机/监督方向同样有效，或发现 dormant pathway 可解释输出变化 | patching 创造变量而非定位正常计算变量 |

## 第一性原理推导

若“SAE 更稀疏且因果忠实”成立，至少需要：

1. **表示条件**：SAE 方向捕获的任务相关变化不能主要落在 reconstruction residual 中。
2. **比较条件**：SAE 与 PCA 使用相同层、样本、目标输出、排序预算和停止规则。
3. **稳健条件**：结果在 held-out IOI 样本和预先固定的 KL 目标上保持。
4. **排他条件**：随机方向、监督字典或其他合理对照不能以同样代价达到相同效果。
5. **路径条件**：需要正常前向计算中的机制证据，排除 dormant pathway 或 intervention artifact。

上述条件是实验规格的来源，不是由逻辑自动证明的结论。

## 重要性与周期可行性

- So what：如果效率优势不能通过效度检查，MI 研究容易把“可干预”误写成“可解释机制”；若能通过，则为 SAE 特征的因果使用提供更强证据。
- Who cares：使用 SAE 做 circuit discovery、model editing 或安全解释的研究者需要知道结论能外推到什么程度。
- 课程周期：先复现 C02 的最小比较，再按预算加入一个重构敏感性对照和一个替代方向对照；跨模型泛化留作后续工作。

## 问题门失败记录

| ID | 失败/死路 | 原因与证据 | 处理 | 回写位置 |
| --- | --- | --- | --- | --- |
| F-MI-01 | 初版问题写成“SAE 是否因果忠实” | C02 只给 intervention efficiency；C31 表明 patching 可能有幻觉 | 拆成 H-eff/H-rob/H-faith，并将 `stable` 降为 `review` | 研究问题、证据地图、L9 对照 |

## 问题门九项自查

1. 候选文献/材料约 10 项且已标证据角色：由 L3 线索池提供，实际提交需学生本人筛选。
2. 至少 3 张完整精读卡：C02、C16、C31 示例已完成。
3. AI 导航、两个以上原文位置、偏差审计与人工判断：见三张精读卡。
4. 证据地图区分直接、补充、冲突和空白：见 L5 示例。
5. 研究问题含范围、非例与可证伪命题：本文件已写。
6. 第一性原理推导含必要条件与可检验前提：本文件五项条件。
7. 重要性和课程周期可行性：已写最小范围。
8. 至少一条失败/死路及原因、处理和回写：F-MI-01。
9. AI 辅助过程与正式来源核验：见 L3 trace、L4 cards 与 registry。

## L7-L9 接口

![从问题门到 baseline](assets/mi-question-to-baseline.svg)

*图注：课程自绘流程图，不代表实验已经运行。来源与许可见 [assets/README.md](./assets/README.md)。*

- L7：把 H-eff、H-rob、H-faith 分别映射到变量、指标、对照与停止条件。
- L8：用“问题—关键证据—可证伪命题—最小实验—最大风险”完成 3 分钟陈述。
- L9：运行 Pythia-410M layer 11 IOI 的 SAE-vs-PCA baseline；仓库接口固定到 `HoagyC/sparse_coding@69c5ae0...`，但仓库未声明 license，进入学生复现前先由教师核对依赖与使用边界。

上游证据地图见 [L5 MI evidence map](../lesson-05/mi-evidence-map-demo.md)；完整 claim-level 来源见 [L3 MI trace](../lesson-03/mi-search-trace-demo.md) §5。
