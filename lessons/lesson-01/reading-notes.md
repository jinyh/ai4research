---
版本：v1.0.5
最后更新：2026-09-22
适用课次：第 1 课
文档类型：教师文献精读卡集
状态：原文定位已完成；待教师复核与定稿
变更记录：
- v1.0.5 (2026-09-22): 同步 Pi Agent 主平台、OpenCode 等备选及人工应用建议路径。
- v1.0.4 (2026-09-22): 补现行页序索引及 Hao 统计口径复核；早期精读卡的课堂映射保留为历史建议。
- v1.0.3 (2026-08-07): 将 Lu et al. 2026 AI Scientist 精读卡的课堂引用由旧页号 P03 同步到现行 P04
- v1.0.2 (2026-08-05): 更新项目重组后的本地参考资料路径
- v1.0.1 (2026-07-30): 区分自动文本定位与教师人工复核，删除与授课无关的模型整合过程说明
- v1.0.0 (2026-07-30): 按 reading-list.md「AI 辅助经典阅读协议」生成第 1 课涉及 8 份文献的精读卡（Simon Ch.5、Hamming「You and Your Research」、Wang 2023、Lu 2026、Gottweis 2026、Ghareeb 2026、Hao 2026、Tao ICM 2026）。
---

# 第 1 课文献精读卡集

> 本笔记按 [reading-list.md](../../course/reading-list.md)「AI 辅助经典阅读协议」（AI 导航→原文核验→AI 质疑→偏差审计→人工定稿）生成，字段模板见 [starter-template.md](../../course/starter-template.md) 第 5 节。
>
> **核对说明**：每张卡的「关键证据及原文位置」均由 `pdftotext -layout` 从本地 PDF 提取并定位，页码可复查；「AI 初始阅读地图」标「未核验」；「偏差审计」记录已发现偏差或已检查风险点。自动文本定位不等于教师人工审读，课堂引用前仍须由教师回到原文复核。所有 PDF 仅在本地提取，未发送至外部服务。
>
> **授课前必修**：时效性信息（First Proof 数据、会议接收率、外链状态、模型版本）授课前须回源核验；书籍页码基于本地 PDF 版本，改引他版须重核。
>
---

## 现行引用索引（2026-09-22）

当前主平台为 Pi Agent，OpenCode 等为备选；平台操作见 [Pi Agent 最小启动说明](../../course/pi-setup.md)。

本轮以实际 31 页 PPT 为准：Lu et al. 的论文案例在 **P05**；Nature 评论与社论在 **P06**；Hao et al. 的个人产出、被引优势与集体探索在 **P07**；八阶段地图与阅读卡示意在 **P14–P16**；同一项目的助教操作在 **P19–P24**。Gottweis、Ghareeb、Tao 等精读卡供教师拓展阅读，不视为本轮屏显必讲内容。

Hao 的 3.02 倍对应研究者年均论文数，4.84 倍对应研究者被引量，比较对象均为样本中的 AI 采用者与非采用者；不是单篇论文被引比率，也不是因果增益。样本约 4,130 万篇、六个自然科学学科。Figure 3b 的知识空间集中及探索范围收缩，不直接等同于创新水平下降；课堂以“怎样利用 AI 探索有价值的新问题”引出研究判断。已对照 [Nature 原文](https://www.nature.com/articles/s41586-025-09922-y) 的摘要、个人影响与知识范围段落复核。

**下方卡片中的旧 PPT 页号及“可用于/对应”描述是早期设计建议和核验记录，均为历史映射，不是现行授课索引。** 论文自身页码与原文证据定位不变；现行课堂文案与边界以 [slides.md](./slides.md) 和 [handout.md](./handout.md) 为准。

## 文献清单与第 1 课角色

| # | 文献 | 本地原件 | 第 1 课角色 |
|---|---|---|---|
| 1 | Simon《人工科学》3rd ed. Ch.5 | `references/library/books/Simon_...3rd_ed.pdf` | 核心阅读：问题—目标—约束—评价 |
| 2 | Hamming「You and Your Research」(Ch.30) | `references/library/books/Hamming_1997_...pdf` | 任选：重要问题/研究品味 |
| 3 | Wang et al. 2023 综述 | `references/library/papers/s41586-023-06221-2.pdf` | 任选：AI 介入科学发现环节 |
| 4 | Lu et al. 2026 AI Scientist | `references/library/papers/s41586-026-10265-5.pdf` | P05 论文案例 |
| 5 | Gottweis et al. 2026 Co-Scientist | `references/library/papers/s41586-026-10644-y.pdf` | 教师拓展阅读 |
| 6 | Ghareeb et al. 2026 Robin | `references/library/papers/s41586-026-10652-y.pdf` | 教师拓展阅读 |
| 7 | Hao et al. 2026 影响与收缩 | `references/library/papers/s41586-025-09922-y.pdf` | P07 个人影响与集体探索 |
| 8 | Tao, Mathematics in the Age of AI (ICM 2026) | `references/library/talk/age-of-ai-icm-2026.pdf` | 教师拓展阅读 |

---

## 精读卡 1：Simon《人工科学》Ch.5「The Science of Design」

**(1) 完整书目信息**
Herbert A. Simon. *The Sciences of the Artificial*, 3rd ed. MIT Press, 1996（2019 reissue）. 选读 Chapter 5 "The Science of Design: Creating the Artificial". 出版社链接 https://mitpress.mit.edu/9780262537537/（与 reading-list 第 57 行一致）. 本书无 DOI；ISBN-13: 978-0-262-53753-7. 本地 PDF 全 241 页，Ch.5 跨印刷页 p.111–138（对应 PDF 物理页 p.123–150，物理页 = 印刷页 + 12）。

**(2) 来源类型与证据角色**
学术专著核心章节（经典理论文献）。在本课程属「核心阅读」，用于建立概念框架而非经验证据；定位为「方法论与概念来源」，不作为可单独支撑经验结论的稳定证据。

**(3) 本文试图回答的问题**
人工物的研究能否成为一门「科学」？设计过程是否可教、可形式化、可检验？设计推理是否需要独立于陈述逻辑的命令式逻辑？设计科学课程应包含哪些主题？计算资源有限、解空间巨大时理性设计如何可能？

**(4) 作者的中心主张**
存在一门「设计科学」，「intellectually tough, analytic, partly formalizable, partly empirical, teachable」（p.113），自 1970 年代中期起正在形成。设计关注「事物应当如何」，但其逻辑可在标准陈述逻辑内通过「可能世界 + 约束 + 效用函数最大化」归约，无需独立命令式逻辑（p.115–118）。面对真实复杂世界，设计通常是 satisficing（满意解）而非 optimizing（最优解），通过层级分解、生成—测试循环、手段—目的分析与表征转换推进。

**(5) 关键证据及原文位置**（印刷页码，可复查）
1. p.111：「Everyone designs who devises courses of action aimed at changing existing situations into preferred ones. Design ... is the principal mark that distinguishes the professions from the sciences.」
2. p.113：「The artificial world is centered precisely on this interface between the inner and outer environments.」
3. p.113：「It is the thesis of this chapter that such a science of design not only is possible but also has been emerging since the mid-1970s.」
4. p.116：优化范式——内环境＝备选行动集/命令变量，外环境＝参数，目标＝效用函数加约束，优化即在约束下最大化效用（概率情形为期望效用）。
5. p.116–117：饮食问题与 Figure 6 "The paradigm for imperative logic"，命令变量＝食物数量，约束＝热量上限、维生素下限。
6. p.117–118：命令式逻辑归约论证——把目标约束与最大化要求作为「自然律」并入环境条件，所用逻辑与谓词演算一致。
7. p.119：引入「satisficing」术语；明言「no one will satisfice if he can equally well optimize」。
8. p.120：旅行商问题反例——路径数 N!，「no algorithm ... sufficiently powerful ... for ... fifty cities」。
9. p.121–123：GPS 与手段—目的分析，依赖「additive/factorable」假设（p.123 明示为强假设）。
10. p.128–129：层级分解与生成—测试循环；不同分解对应「风格」差异（p.130）。
11. p.131–132：表征转换示例（number scrabble 重表征为 tic-tac-toe）。
12. p.134：设计科学课程七大主题（评估理论、最优/满意算法、形式逻辑、启发式搜索、搜索资源配置、层级结构、表征）。
13. p.138：「the proper study of mankind is the science of design ... a core discipline for every liberally educated person.」

**(6) 数据、实验设置或论证前提**
理论论证而非实证研究。前提：设计问题可形式化为约束下最大化效用或满意搜索；解空间巨大但可经分解、层级、启发式处理；世界近似「additive/factorable」（强假设，p.123）。经验素材包括 GPS、MATER 国际象棋程序、Manheim 公路选线、Sutherland SKETCHPAD 等可运行程序，作为「可被完整检视的设计过程」（p.135）。

**(7) 适用范围、局限与可能反例**
- satisficing 依赖计算可行性；小规模或凸问题最优仍首选（p.119）。
- 手段—目的分析的「可分解性」是强假设，现实系统常耦合、路径依赖（p.123–124 自陈「real worlds ... seldom completely additive」）。
- 命令式逻辑归约在优化/满意场景成立，对含规范性义务、不可通约价值的设计场景未充分覆盖。
- 七大主题反映 1996 年前状态，未涉数据驱动设计、LLM 辅助设计。
- 「设计是跨学科共同语言」（p.136–138）带倡导性，缺乏可证伪指标。

**(8) 与第 1 课教学的关联**
- 八阶段·阶段 1 问题定义 / 阶段 2 第一性原理：Simon 的「内环境—外环境—目标—约束—效用/满意」直接对应 slides P21–P22「先问清楚，再检查必要条件」。
- 「问题—目标—约束—评价」四元结构（slides P09、P22–P25）：Simon 的形式化是经典学理来源。
- 可追溯/可审计交互（slides P17、P19）：Simon 用「running computer programs」作为可被「full inspection and analysis」的设计过程记录（p.135），与 OpenCode 把 Task/Context/Tool/Diff/Review/Log 置于同一工作空间同构。
- 科研伦理（slides P18）：把设计判断从黑箱显式化到程序与约束，支持「AI 输出核验前只能是线索」。
- 四研究门：与第 6 课问题门关联最强——「先定义问题、再检查必要条件」对应问题门。
- 界限：Simon 谈人工物设计，课程八阶段是研究动作链路；教学时须说明「研究也是一种改变现状为偏好状态的设计活动」这一类比及其局限。

**(9) AI 初始阅读地图（未核验）**
Ch.5 主题为「设计科学」合法性与课程框架；区分自然科学与人工科学；引入 satisficing；提出七大主题；以饮食问题、旅行商、GPS、魔方阵为例。以上在人工核验前不作引用依据。

**(10) 本地原文定位与文本核对**
用 `pdftotext -layout` 本地提取全 241 页，按 form feed 分页定位 Ch.5 边界（印刷 p.111–138，PDF 物理页 p.123–150）。逐节复查 13 处引文与页码，措辞与 PDF 一致。七大主题汇总（p.134）与正文各节标题逐一对应。比对 reading-list 第 57 行书目、版次、章节、链接一致。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
未发现虚构引文或页码错误。已检查风险点：
- a. 「Simon 否定命令式逻辑」易被误读为「规范逻辑无用」——原文 p.115 用「unnecessary」非「impossible」，并承认模态逻辑可存在。
- b. 「satisficing」易被泛化为「不要追求最优」——p.119 明言能最优则最优。
- c. 1996 年七大主题易被误当作当前设计研究全貌——已标需补现代来源。
- d. 页码体系混淆风险——全卡统一印刷页码并给换算（物理页 = 印刷页 + 12）。
- e. Simon「设计」与课程「研究链路」易被直接等同——已显式说明类比与界限。
- f. AI 初始地图可能遗漏「表征转换」一节——已补入关键证据第 11 项。
- 未经独立核验：出版社链接有效性、ISBN 未联网核验（仅与 reading-list 比对一致），授课前应回 mitpress 验证。

**(12) 最终人工判断（草稿，待教师定稿）**
本章适合作为第 1 课「问题—目标—约束—评价」四元结构与「可审计研究过程」两个要点的核心学理来源，建议在 slides P09、P17、P21–P22 引用，引文限 p.111 定义句、p.113 界面句、p.135「程序为可检视记录」句三处。教学界限三点：(1) Simon 谈人工物设计非研究方法，类比须声明；(2) satisficing 仅在计算不可行时成立；(3) 1996 文本不覆盖数据驱动与 LLM 辅助设计，须另配现代来源并标「待核验」。

---

## 精读卡 2：Hamming「You and Your Research」

**(1) 完整书目信息**
Richard W. Hamming. *The Art of Doing Science and Engineering: Learning to Learn*. Chapter 30 "You and Your Research"（原书 pp.209–215）. 原版 CRC Press, 1997；Stripe Press 2020 再版（https://press.stripe.com/the-art-of-doing-science-and-engineering）. 本地 PDF 为 1997 版，227 页。与 reading-list 一致（任选经典，第 1 课引导阅读）。

**(2) 来源类型与证据角色**
经典演讲扩写为书末总结章（作者自述为「前 29 章的总结」），一手经验性方法论文献，非实证研究、非同行评议论文。用作第 1 课任选经典，提供研究品味、选题勇气与长期工作方式的叙事性参考；不作规范性结论直接证据。

**(3) 本文试图回答的问题**
一个人如何在仅有的一次科研生涯中做出重要工作？「做重要工作」主要靠运气、天赋，还是可培养的能力？怎样选择问题、安排时间、塑造 style，让长期积累朝同一方向？

**(4) 作者的中心主张**
做出第一流研究主要不靠运气或高 IQ，而靠：主动选择重要问题、培养自信/勇气、以长期 style 统一努力方向（复利累积）、容忍信念与怀疑并存的模糊性、定期抽身思考大问题。核心命题：「如果你不在重要问题上工作，就不可能做出重要工作。」（p.210）

**(5) 关键证据及原文位置**（1997 版页码）
1. p.209–210：开宗明义「it is better to do significant things than to just get through life」；用 Pasteur「Luck favors the prepared mind」反驳全凭运气说。
2. p.210：Shannon 与作者同期在 Bell Labs 分别创立信息论与编码论——「we were more prepared to find, work on, and create the corresponding theories」；化学桌故事，结论「If you do not work on important problems then it is obvious you have little chance of doing important things.」
3. p.211：「Confidence in yourself ... you can call it 'courage'. Shannon had courage.」；醉酒水手比喻——无方向 ∝ √N，有卓越愿景 ∝ N。
4. p.212：「intellectual investment is like compound interest」；「Friday afternoons—great thoughts」。
5. p.213：「Great people can tolerate ambiguity, they can both believe and disbelieve at the same time」；伟人常持 10–20 个尚不知如何解决的重要问题。
6. p.214–215：收束于「the essence of the book is 'style'」（p.214）与 Socrates「The unexamined life is not worth living」（p.214）；末句醉酒水手复现（p.215）。

**(6) 论证前提与例证**
前提：每人仅一次生涯；重复做出重要工作者（Shannon、Einstein）说明非纯运气。例证：Shannon/信息论、Einstein 12–14 岁追光思想实验、Newton「若他人同样努力」、Edison「99% perspiration」、Bill Pfann 区熔法、John Tukey 努力程度。论证形式：自传轶事 + 反例排除 + 类比（复利、随机游走）归纳，经验性归纳非演绎。

**(7) 适用范围、局限与可能反例**
- 证据为叙事轶事，无对照或统计，选择性突出幸存者。
- 「年龄」段称理论物理/数学最佳工作多在早期，泛化观察，反例不少。
- Bell Labs 中世纪环境（稳定资助、跨学科餐厅文化）未必复现于当今短期考核。
- 「open door vs closed door」作者自陈仅观察到相关、未证因果（p.211「I cannot prove the cause and effect relationship, I only observed the correlation」）。
- 反例：大科学团队突破（LIGO）不完全由 lone wolf 风格产生；AI 辅助时代问题选择与人机分工更复杂。

**(8) 与第 1 课教学的关联**
- 八阶段·阶段 1 问题定义：Hamming 核心「选择重要问题」是 slides P21、P22 的元方法依据。
- slides P01「研究责任仍由人承担」：选题、判断与 style 是人的责任，AI 不替代「在什么问题上工作」的决策。
- slides P36「优先使用真实兴趣」：与「work on important problems」相通。
- 第 6 课问题门：此章是问题门的价值前置——研究品味与勇气是问题门评估的隐性前提。
- 可追溯性：本章非实证证据，引用时标注「经验性方法论参考」，不作 stable 结论单证支撑。

**(9) AI 初始阅读地图（未核验）**
中心问题：如何在科研生涯做出重要工作；论证结构：运气反驳→勇气→选题→复利/style→模糊性→销售表达；关键术语：important problems、courage、style、compound interest、tolerance of ambiguity、open door；预期证据：Shannon、Einstein、Pfann、Tukey、Pasteur、醉酒水手；待追问：Friday afternoons、Socrates 引语、页码 pp.209–215。

**(10) 本地原文定位与文本核对**
用 `pdftotext -layout` 提取 pp.209–227，grep 定位「You and Your Research」为第 30 章（章标题页 p.209，正文止 p.215，后为 Index）。逐条核对第 (9) 步预设：中心问题（p.209）、论证顺序、术语（important problems p.210、courage p.211、style p.214、compound interest p.212、ambiguity p.213、open door p.211）、人物（Shannon p.209–210、Einstein p.209–210、Pfann p.210、Tukey p.212、Pasteur p.209、醉酒水手 p.211/215）、Friday afternoons（p.212）、Socrates（p.214）均核验通过。页码范围 pp.209–215 确认。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
未发现编造式错误（(9) 已先标「未核验」并核对）。已检查风险：
- 版次页码风险：本地为 1997 CRC 版，Stripe Press 2020 再版排版不同页码不通用，引用须注「1997 版 pp.209–215」。
- 「演讲 vs 章节」混淆风险：Hamming 有 1986 年同名演讲，流传讲稿与本章文字不同；AI 易混入讲稿段落。本次只引本章 PDF 原文。
- 「Chapter 30」归属风险：AI 可能误称第 28 章或附录；实际第 28 章是 Systems Engineering（pp.200–201），本卡为第 30 章（页眉「210 CHAPTER 30」等）。
- 泛化风险：「年龄」段为观察性泛化非定论。
- 因果越界风险：「open door」仅相关非因果（p.211），AI 复述易说成「开门导致做对问题」。
- 「努力复利 >6%」等启发式数值属比喻非实证，不作课程定量结论。

**(12) 最终人工判断（草稿，待教师定稿）**
本章可作第 1 课任选经典有效使用，定位为经验性方法论参考而非实证证据；与「研究责任由人承担」「阶段 1 问题定义」「问题门价值前置」一致。引用须注「Hamming 1997 版，第 30 章，pp.209–215」，改引 2020 再版须重核页码。可用关键句（附页码）：p.210 选题句、p.211 勇气句、p.212 复利句、p.213 模糊性句、p.214 style 句。不得据本章单独得出 stable 结论。

---

## 精读卡 3：Wang et al. 2023 综述

**(1) 完整书目信息**
Wang, H. et al.（30 位作者）. "Scientific discovery in the age of artificial intelligence." *Nature* 620, 47–60 (2023). Published online 2 August 2023. DOI: 10.1038/s41586-023-06221-2. 类型：Review（综述）。本地 PDF 14 页（Nature 页 47–60）。

**(2) 来源类型与证据角色**
同行评议综述论文（Nature Review 类）。课程任选阅读。框架性来源——用于定位 AI 介入科学发现链路的环节、机会与限制，不作单一稳定结论支撑。其概括性论断需回其所引原始文献或更新研究核验。

**(3) 本文试图回答的问题**
AI 在哪些环节介入科学研究、用什么方法、解决什么问题、剩余哪些根本性挑战。

**(4) 作者的中心主张**
AI 已成为跨学科科学发现全过程（数据→表示→假设→实验→模拟→解释）的增强与加速工具；其价值来自将科学知识以归纳偏置注入模型；AI4Science 成功取决于整合进常规科研实践并理解潜力与局限，核心障碍是分布外泛化、数据标注与质量、黑箱可解释性、可复现性、跨学科协作与负责任部署，而非单纯模型规模。

**(5) 关键证据及原文位置**（Nature 页码）
1. Fig.1 总览图，p.48：把科学发现画成 Observations→Hypotheses→Experiments 多阶段循环，外围列 weather forecasting、battery design、tokamak 磁控、合成路径规划、神经 PDE 求解器等案例。
2. Box 1 Glossary，p.49：定义 active learning、autoencoder、distribution shift、geometric deep learning、inductive bias、physics-informed AI、reinforcement learning、representation learning、self-supervised learning、surrogate models、transformer 等。
3. Fig.3，p.51：「AI-guided generation of scientific hypotheses」三路——AI predictor 高通量筛选、AI navigator 强化学习+Occam's razor 符号回归（示例推断牛顿引力律）、AI differentiator 自编码器潜空间优化。
4. Fig.4，p.53：「Integration of AI with scientific experiments and simulation」——tokamak 磁控 RL、构象跃迁采样、物理信息神经网络求解 PDE。
5. Grand challenges 节，p.55–56：practical considerations（数据标准化、model cards、联邦学习）、algorithmic innovations（out-of-distribution、causality、transfer learning、可解释性）、conduct of science（团队构成、算力集中、industry–academia、dual-use）。
6. Conclusion，p.56：「To use AI responsibly in scientific research, we need to measure the levels of uncertainty, error, and utility of AI systems.」
7. 分布外与因果，p.55–56：「A neural network trained on data from a specific regime may discover regularities that do not generalize in a different regime」；「Incorporating causality in AI is still a young field」。
8. 可复现性，p.55：「AI approaches can suffer from reproducibility due to the stochastic nature of model training ... Standardized benchmarks and experimental design can alleviate such issues.」

**(6) 数据、实验设置或论证前提**
综述不作单一实验。前提：深度学习因大数据、GPU、新算法而兴；科学数据具几何/对称/序列/图结构可注入归纳偏置；假设空间巨大（约 10^60 类药分子，p.48/52）穷举不可行；标注稀缺（不足 1% 已测序蛋白有功能注释，p.49）。所引证据来自 AlphaFold2、RoseTTAFold、Degrave tokamak、Wagner 神经网络反驳数学猜想、Davies 引导直觉、Coley 机器人合成等原始文献。

**(7) 适用范围、局限与可能反例**
- 综述概括性强，具体能力声明需回所引原始论文核验。
- 截至 2023 年 8 月，未覆盖 2024–2026 多 Agent 系统、AI Scientist、Co-Scientist（本课 P04 钩子补充）。
- 「autonomous discovery」「self-driving labs」表述偏乐观，原文同时强调 human supervision，易被过度概括为「AI 已能独立发现」。
- 对失败实验、负面结果、可复现危机讨论篇幅有限（p.55–56），不及课程「失败不得选择性删除」力度。
- 未深入 Agent 权限、工件追踪、AI 使用披露等治理议题，需第 2 课材料补足。

**(8) 与第 1 课教学的关联**
- slides P05：本文 Fig.1（p.48）为第一列“2023 综述”提供全流程框架；Grand challenges（p.55–56）支持“综述性框架、具体能力须回原始研究”的证据边界。
- 八阶段（P21–P25）：Fig.1 的 Observations/Hypotheses/Experiments 与八阶段粗略对应（Observations↔阶段 4/5，Hypotheses↔阶段 3/6，Experiments↔阶段 7），但本文不区分问题定义与第一性原理（阶段 1-2），不强调回写与表达（阶段 8），只能作环节定位，不替代八阶段语言。
- 可追溯性：p.56「measure uncertainty, error, utility」与 P08「真实问题→可核验证据→可复现实验→可追溯论证」一致。
- 科研伦理：p.55–56 的 dual-use、misuse、responsible deployment 对应第 2 课伦理底线，但本文不提供操作级清单。

**(9) AI 初始阅读地图（未核验）**
中心问题：AI 如何改变科学发现；论证结构：数据采集→表示→假设生成→实验与模拟→挑战展望；关键术语：geometric deep learning、self-supervised learning、inductive bias、neural operator、symbolic regression、PINN；预期证据：总览图、AlphaFold、tokamak；待追问：是否把 autonomous 说成已实现、哪些带量化、哪些是展望。

**(10) 本地原文定位与文本核对**
用 `pdftotext -layout` 本地提取全文，按页脚「Nature | Vol 620 | 3 August 2023」逐页确认 PDF 第 1 页=p.47…第 14 页=p.60。复查：Fig.1 题名与案例清单在 p.48；Fig.3 三子图与牛顿引力律示例在 p.51；Fig.4 tokamak/构象采样/PINN 在 p.53；Grand challenges 节首段与 out-of-distribution 原句在 p.55；Conclusion 原句在 p.56。术语清单经 Box 1（p.49）核对一致。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
未发现严重事实错误。已检查风险：
- 过度概括：易把「AI operate under human supervision」（p.48）和「self-driving labs」（p.55）读成「AI 已能自主完成科研」——原文处处强调 human-in-the-loop、uncertainty、limitations。
- 遗漏：许多声明无量化指标（如「near-experimental accuracy」「up to six orders of magnitude faster」p.51/52 未给实验设置），本卡未作稳定结论。
- 时效：2023 年 8 月，2024–2026 后续工作不在范围，授课时用 P04 钩子补充。
- 八阶段映射为本课程人为对应，非原文框架，已标「粗略对应」。

**(12) 最终人工判断（草稿，待教师定稿）**
本文是定位 AI4Science 全景与挑战的合格入门综述，适合第 1 课任选阅读，用作 Fig.1（p.48）环节定位与 Grand challenges（p.55–56）限制清单的图证来源。建议课堂只要求精读引言（p.47–48）、Fig.1（p.48）与 Grand challenges（p.55–56）三处，并按方向任选「AI-based generation of scientific hypotheses」（p.51–52）或「AI-driven experimentation and simulation」（p.53–54）一节。引用论断须回所引原始文献，不得把综述性概括当稳定证据；对「autonomous」「self-driving」须按原文 human supervision 语境限定。

---

## 精读卡 4：Lu et al. 2026 AI Scientist

**(1) 完整书目信息**
Lu, C. et al. "Towards end-to-end automation of AI research." *Nature* **651**, 914–919 (2026). DOI: 10.1038/s41586-026-10265-5. Received 8 July 2025；Accepted 11 February 2026；Published online 25 March 2026. Open Access (CC BY 4.0). 机构：Sakana AI（东京）、Oxford FLAIR、UBC、Vector Institute。本地 PDF 9 页。

> 卷期核验：PDF 页眉逐页显示「Nature | Vol 651 | 26 March 2026」，页码 914–919，与 slides P04、`references/README.md` 一致。Wang 2023 为卷 620，本篇为卷 651，二者不同。

**(2) 来源类型与证据角色**
同行评审 Nature 研究论文（Open Access），附 Supplementary Information、代码/数据可用性声明与 IRB 审批（H24-02652）。第 1 课 slides P04 课堂钩子——端到端 AI 科研自动化管线案例，对应八阶段「原型验证→回写与表达」自动化一极，同时作科研伦理与可追溯性反向锚点。

**(3) 本文试图回答的问题**
能否用基于基础模型的智能体系统，自主完成 ML 研究从构思、编码、实验、分析、写作到同行评审的全生命周期，并在人类同行评审流程下产生可被接受稿件？

**(4) 作者的中心主张**
The AI Scientist 管线（ideation→experimentation→write-up→review）已在 ML 这一可计算实验领域实现端到端自动化；生成稿件中 1 篇在顶级 ML 会议（ICLR）workshop（ICBINB）首轮同行评审中获超该 workshop 平均接收阈值评分（6.33；评审分 6/7/6）。作者明确：这是 workshop（非主会）首轮评审、仅 1/3 通过、不代表顶级主会水平或通用自主科研能力。

**(5) 关键证据及原文位置**（Nature 页码）
1. 摘要（p.914）：「The workshop had an acceptance rate of 70%.」「manuscript generated by this AI system passed the first round of peer review for a workshop of a top-tier machine learning conference.」——slides P04「workshop 首轮评审，接受率约 70%」出处。
2. Human evaluation（p.916）：「One of the three AI-generated manuscripts received an average score of 6.33 ... (individual scores were 6, 7 and 6)」「would have been accepted in all likelihood were it not withdrawn ... due to being AI-generated.」
3. Limitations（p.917）：「workshops have much higher acceptance rates than main conferences (for example, 70% for the ICLR 2025 ICBINB workshop versus 32% for the ICLR 2025 main conference). Therefore, The AI Scientist cannot yet meet the standards of top-tier publications」「none met the higher bar for a main ICLR conference publication.」
4. Table 1（p.915）：自动评审器在 NeurIPS 2021 consistency 基准 balanced accuracy 0.69±0.04（cutoff 前）/0.66±0.03（cutoff 后），与人类 0.66 相当；两样本 z 检验 P=0.319/0.921 无显著差异。
5. Fig.1a（p.914）：四阶段管线可视化（Ideation / Experimentation 含 4 阶段树搜索 / Write-up / AI review），slides P04 钩子图示原始来源。
6. Methods（p.919 起）：Template-free 版用 OpenAI o3 构思与代码评审、Claude Sonnet 4 写代码、GPT-4o 视觉语言、o4-mini 评审推理——「特定 ML 设置、特定模型后端」口径技术依据。

**(6) 数据、实验设置或论证前提**
领域限定 ML（实验全在计算机上）。两种模式：Template-based（人类提供起始脚手架）与 Template-free（系统自生成初始代码，agentic tree search）。模型后端 OpenAI、Anthropic、Google 系列。评审实验：向 ICLR 2025 ICBINB workshop 提交 3 篇 AI 稿件（混入 43 篇被评审稿件），评审者被告知存在 AI 稿件但不知具体哪篇；IRB H24-02652；预约定稿无论结果评审后撤回。自动评审基准以 OpenReview ICLR 决策为 ground truth。

**(7) 适用范围、局限与可能反例**
- 仅限 ML 可全自动实验领域；化学等需实体验领域为未来扩展。
- 通过的是 workshop 首轮评审，非顶级主会正式接收；3 篇中仅 1 篇过线、且未达主会标准。
- 失败模式（p.917 自列）：naive 想法、主想法实现错误、方法严谨性不足、实验实现错误、图表重复、各类幻觉（如不准确引用）。
- 数据污染风险：cutoff 后 balanced accuracy 由 69% 降至 66%，提示训练数据泄漏可能。
- 人工筛选环节：从 template-free 输出中人工挑选 3 篇提交（主题契合、代码正确运行、格式正确），「端到端全自动」表述须附此人工过滤脚注。
- 反例：仅 1/3 过线、3 篇均未达主会标准、workshop 接收率 70%（远高于主会 32%）——本身即「不可外推为通用自主科研能力」的反例支撑。

**(8) 与第 1 课教学的关联**
- slides P04 钩子：Fig.1a 四阶段管线展示「AI 科研自动化长链路」，与八阶段同构对照，引出「自动化能把哪些动作放大、哪些必须人保留」。
- 可追溯性：每个评分（6.33、70%、Table 1）可回溯原文位置与实验设置，作「结论必须可追溯证据」正例。
- 科研伦理：作者主动声明 IRB、workshop 主办方与 ICLR leadership 同意、评审后撤回、披露 AI 身份——「AI 使用披露、人工核验、安全边界」正面示范。
- 证据标准：单系统、单领域、单次会议、1/3 通过——按课程证据标准属「单一证据，须记录支持强度与适用边界，不得标 stable」。

**(9) AI 初始阅读地图（未核验）**
系统构成：AI Scientist（生成）+ Automated Reviewer（评审）；管线 Ideation→Experimentation→Write-up→Review；关键结果 1/3 过线、自动评审达人类相当、scaling 带来质量提升；伦理动作 IRB、主办方同意、评审后撤回。未核验：70% 与 32% 接收率是否与 ICLR 2025 官方一致（引用 [38][39] 指向 OpenReview 与 ICLR Fact Sheet，未另行核验）。

**(10) 本地原文定位与文本核对**
仅用本地 `pdftotext` 提取，未联网。核对：卷期页码 PDF 页眉「Nature | Vol 651 | 26 March 2026」，914–919 连续——**与 slides P04 一致（651）**；70% 接收率口径（p.914 摘要、p.917 Limitations）成立；「首轮评审」口径（p.914 first round、p.916 would have been accepted）成立；非「顶级会议正式接收」（p.917 明确 cannot yet meet standards、3 篇均未达主会）成立；6.33 分（p.916）一致。结论：slides P04 关键口径均有原文支撑。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
1. 媒体式过度概括：易被转述为「AI 已具备独立科研能力」或「AI 论文被顶级会议接收」——原文不支持（workshop、首轮、1/3、未达主会）。
2. 自动化程度过度概括：存在「人工筛选 3 篇提交」环节，表述为「全自主无人工」则构成遗漏。
3. 评审能力过度概括：Table 1 仅说明 NeurIPS 2021 consistency 上与人类相当，不能外推为「自动评审可替代人类评审」。
4. **AI 自身偏差实例（卷号混淆）**：本卡生成 Agent 在偏差审计初稿中误判「reading-list/slides 所写卷号为 620、应更正为 651」。经整合者核对，slides P04 实际写「Nature 651, 914-919」、`references/README.md` 与 PDF 页眉均为 651——Agent 将 Wang 2023（卷 620）与 Lu 2026（卷 651）混淆，把不存在的 slides 错误当成了真实错误。此为 AI 偏差的典型实例（记忆混淆 + 误报来源错误），已就地修正，保留作教学案例：AI 不仅会过度概括，还可能虚构「需要更正的错误」。
5. 证据强度：1 篇过线、单次、单领域——不构成 stable，仅作存在性证据。
- 未核验项：70%/32% 两接收率官方来源（引用 [38][39]）授课前应另行核验，本卡如实标「未核验」。

**(12) 最终人工判断（草稿，待教师定稿）**
可用于 slides P04 课堂钩子，必须保留口径：workshop 首轮评审（非主会正式接收）、接受率约 70%（ICBINB，对应主会 32%）、1/3 篇过线（6.33，评审分 6/7/6）、特定 ML 设置、不表述为通用自主科研能力。引用信息：Lu, C. et al. Nature 651, 914–919 (2026). DOI: 10.1038/s41586-026-10265-5（与 slides 一致，无需更正）。授课前核验项：ICLR 2025 ICBINB 70% 与主会 32% 接收率官方来源。证据分级：存在性证据，不标 stable。

---

## 精读卡 5：Gottweis et al. 2026 Co-Scientist

**(1) 完整书目信息**
Gottweis, J. et al.（约 70 位作者）. "Accelerating scientific discovery with Co-Scientist." *Nature* 655, 487–496 (2026). DOI: 10.1038/s41586-026-10644-y. Received 2025-03-20；Accepted 2026-05-11；Published online 2026-05-19；print issue 9 July 2026. Open access. 通讯作者 Gottweis、Weng、Kohli、Pawlosky、Karthikesalingam、Natarajan。单位：Google Cloud AI Research (Zurich)、Google DeepMind、Google Research、Stanford Medicine、Houston Methodist、Imperial College London。本地 PDF 28 页（含 Methods、参考文献、扩展数据）。

**(2) 来源类型与证据角色**
同行评审 Nature 研究论文（Open Access）。第 1 课 slides P04 钩子——展示「AI 从单点辅助走向连接多步研究行动（假设→方案→体外验证→临床分析）」范例。不作通用自主科学家证据，只作「具体生物医学任务下多智能体系统可行性」证据。

**(3) 本文试图回答的问题**
能否构建多智能体 AI 系统，在科学家给定目标后自主生成既有新颖性又可实验验证的假设，并在真实生物医学问题中端到端验证？测试时计算扩展是否随计算时间持续提升假设质量？能否在药物重定位、新靶点、抗药机制三类递进复杂度任务中产出可被体外实验或独立研究印证的结果？

**(4) 作者的中心主张**
Co-Scientist——基于 Gemini 的多智能体系统，通过「生成—辩论—进化」范式与锦标赛式自评，能作为科学家协作者加速科学发现。核心贡献：异步任务执行的多智能体架构（支持测试时计算扩展）+ 锦标赛进化实现自改进假设生成。在三类生物医学任务（AML 药物重定位、肝纤维化新靶点、AMR 基因转移机制）端到端验证。作者明确定位为「augment scientists」而非自主科学家，反复强调验证初步、局限于具体任务与体外条件。

**(5) 关键证据及原文位置**（Nature 页码）
1. 架构与锦标赛（p.488–489，Fig.1b）：Supervisor agent 解析目标并分配给 Generation、Reflection、Ranking、Evolution、Proximity、Meta-review worker agents；caption「red arrows represent the information feedback loop」，形成 self-improving loop。摘要（p.487）两贡献：「multi-agent architecture with asynchronous task execution」「tournament evolution process for self-improving hypotheses」。
2. 测试时计算扩展（p.490–491，Fig.2a,b）：203 个目标按时序分 10 桶，Elo 评分随计算时间上升；15 个专家策划难题上超过 Gemini 2.0 Pro、OpenAI o1/o3-mini、DeepSeek R1。
3. AML binimetinib（p.492，Fig.3a）：MOLM-13 细胞 IC50 = 0.01 μM（0.003–0.025），除 NOMO-1 外所有 AML 细胞系低至 2 nM，非 AML TK6 显著更高。
4. KIRA6 选择性（p.492–493，Fig.3d–h）：KG-1a IC50 = 10 nM，TK6 IC50 = 180 nM，caption「18-fold separation establishes a promising in vitro therapeutic window」。
5. 肝纤维化（p.494）：识别三个表观遗传修饰因子及靶向药物，两个在肝类器官显抗纤维化活性无毒性；vorinostat 已获 FDA 批准用于另一癌种。
6. AMR cf-PICI 独立复现（p.494–495）：「Co-Scientist independently and accurately proposed the top-ranked hypothesis ... in just 2 days, precisely matched the primary discovery of an independent, co-timed genomic and experimental study」（引用 He et al., Cell 188, 6636–6653 (2025)）。
7. 消融（p.490/491 后 Methods）：Reflection agent 获外部搜索工具可防幻觉——无搜索时对已知非新颖想法给 6.14/10 高新颖分，有搜索降至 2.38/10。
8. 局限与风险（p.494 Discussion 起）：依赖开放获取文献可能遗漏付费墙研究与负面结果；「there is a risk of propagating erroneous or irreproducible findings」；「validation ... remains preliminary」；不当使用可能加剧可复现性危机。

**(6) 数据、实验设置或论证前提**
基础模型 Gemini 2.0 系列（Methods「we used Gemini 2.0 models as the base foundational LLM」），架构自称 model-agnostic。评估：203 个研究目标（时序扩展）、15 个专家策划目标（对比基线）、11 个目标（盲法专家评估）。体外：4 种 AML 细胞系 + 非 AML 对照 TK6；n=3 生物学独立重复；IC50 非线性回归。论证前提：Elo 评分为假设质量代理指标（引文献 32 承认局限）；体外为 viability check 不替代临床验证；专家评估为主观评分非 objective ground truth。样本量未经统计预设（Statistics「No statistical methods were used to predetermine sample sizes」）。

**(7) 适用范围、局限与可能反例**
- 适用：验证集中于三个具体生物医学任务；作者反复声明「Although Co-Scientist is general purpose ... here we validate it in three impactful areas of biomedicine」（p.489）。
- 局限：依赖开放文献可能遗漏付费墙与负面结果；可能传播不可重复文献错误；继承模型事实性缺陷与幻觉；Elo 非直接优化目标；体外不保证体内/临床；盲法专家样本小（n=11）「further studies are necessary」。
- 反例/边界：nanvuranlat 与 leflunomide 在 MOLM-13 效果有限（Extended Data Fig.4）；KG-1a 对联合方案呈混合协同与拮抗（TP53 背景）；KIRA6 在 MOLM-13/HL-60 中 IC50 显著更高（1,750/870 nM），效果高度依赖亚型。作者如实呈现，未选择性删除。
- 不外推：不得表述为「通用自主科学家」或「已解决科学发现」。

**(8) 与第 1 课教学的关联**
- slides P04 钩子：展示 AI 从单点辅助走向连接多步研究行动（假设→方案→体外验证→临床分析），映射八阶段「机制假设→外部输入摄取→证据整理→原型验证」。
- 可追溯性：Co-Scientist 自身强调引文溯源、Reflection agent 搜索核验、deep verification 分解子假设，可作「AI 输出只是线索需回原文/实验核验」正反教材。
- 科研伦理：显式讨论幻觉风险、不可重复性危机、scientist-in-the-loop、安全与伦理（Supplementary Note 7），与第 1 课「AI 使用记录、人工核验、署名与披露」一致。
- 口径：只称「具体生物医学任务中验证过的多智能体假设生成系统」，失败与冲突证据（nanvuranlat/leflunomide 有限、KG-1a 拮抗）须一并呈现。

**(9) AI 初始阅读地图（未核验）**
系统多智能体含 Supervisor 与 6 类 agent；验证 AML、肝纤维化、AMR（均体外或文献复现非临床）；测试时计算扩展带来质量提升未见饱和；关键候选 binimetinib、KIRA6、vorinostat；局限集中文献覆盖、幻觉、样本量、临床转化。未核验：卷期页码、KIRA6 IC50 与 18 倍、通用性与验证范围措辞、是否提及 Gemini 3。

**(10) 本地原文定位与文本核对**
用 `pdftotext` 本地提取。卷期页码：首页页眉「NATURE | Vol 655 | 9 July 2026 | 487」，末页 496，正文跨 487–496 ✓。binimetinib IC50（p.492）✓。KIRA6 18 倍（p.493）✓。肝纤维化 vorinostat FDA（p.494）✓。AMR 2 天（p.494）✓。通用性 vs 验证范围措辞（p.489/摘要）✓。Gemini 3 提及（Methods 第 849 页段「such as Gemini 3」；本研究用 Gemini 2.0）✓。局限措辞（p.494）✓。第 (9) 步初始地图均与原文一致，无偏差。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
- 过度概括（已避免）：AI 易将「general-purpose system」误读为「已通用验证」——原文明确架构通用但验证只覆盖三任务，本卡严格区分。
- 数值（已核验）：IC50、18 倍、2 天均来自原文真实页码。
- 遗漏（已补）：Methods 中 Reflection agent 搜索使新颖评分 6.14→2.38 的量化消融、样本量未经统计预设声明，已补入。
- 引文（已注明）：参考文献 21（He et al., Cell 2025）为 cf-PICI 同期独立研究，AMR 复现关键对照。
- 未发现虚构引文、页码或数据。

**(12) 最终人工判断（草稿，待教师定稿）**
可作第 1 课 slides P04 钩子，口径须严格限定：在 AML 药物重定位、肝纤维化新靶点、AMR 机制复现三类具体生物医学任务上，对基于 Gemini 2.0 的多智能体系统的端到端初步验证。教学价值在展示 AI 串联多步研究行动的可能性与 AI 输出需人工/实验核验的伦理。不得表述为「通用自主科学家已实现」或「科学发现已被 AI 解决」。建议 PPT 同时呈现成功与失败候选（KIRA6 有效而 nanvuranlat/leflunomide 有限、KG-1a 拮抗）。证据强度：单一 Nature 论文，不标 stable，标「单证据，支持强度中等，适用边界=具体生物医学任务与体外条件，缺失=体内/临床、其他学科泛化，待验证=可重复性与独立团队复现」。授课前重新确认作者列表、单位、页码、DOI 是否与最新版本一致（Nature 可能存在 correction）。

---

## 精读卡 6：Ghareeb et al. 2026 Robin

**(1) 完整书目信息**
Ghareeb, A. E. et al.（14 位作者）. "A multi-agent system for automating scientific discovery." *Nature* 655, 497–505 (2026). DOI: 10.1038/s41586-026-10652-y. Published online 19 May 2026；print issue 9 July 2026. Received 23 May 2025；Accepted 12 May 2026. Open access. 通讯作者 Andrew D. White、Michaela M. Hinks、Samuel G. Rodriques。第一单位 FutureHouse（旧金山）。本地 PDF 23 页。

**(2) 来源类型与证据角色**
同行评审 Nature 原始研究（Open Access）。第 1 课 slides P04 钩子——展示多 agent 系统如何连接研究动作（文献检索→假设→实验→数据分析→假设更新），不作方法论规范结论或临床疗效证据。八阶段映射「外部输入摄取—证据整理—研究判断—原型验证」闭环。

**(3) 本文试图回答的问题**
能否用多 agent 系统，在实验生物学场景同时自动化「假设生成」与「实验数据分析」两个关键智力步骤，并在 lab-in-the-loop 框架内迭代产出可实验检验的候选治疗药物？在干性年龄相关性黄斑变性（dAMD）上能否提出并初步验证此前未被提出过的候选药？

**(4) 作者的中心主张**
Robin——集成文献检索 agent（Crow、Falcon，基于 PaperQA2）与数据分析 agent（Finch）的多 agent 系统，可在科学家只提供疾病名称、人工执行实验前提下，半自动完成「假设生成—实验设计建议—数据自主分析—假设更新」发现循环。以 dAMD 为概念验证识别 ripasudil（已在日本获批用于青光眼的 ROCK 抑制剂）和 KL001 为 RPE 细胞吞噬增强剂，其中 ripasudil 用于 dAMD 据作者所知此前未被提出。作者明确定位「semi-autonomous」「lab-in-the-loop」，非完全自主科学家。

**(5) 关键证据及原文位置**（Nature 页码）
1. 架构（p.498，Fig.1 及正文）：「Robin integrates multiple language agents in a structured workflow ... Crow and Falcon are literature search agents based on PaperQA2 ... Finch is a scientific data analysis agent」；摘要（p.497）「semi-autonomous approach to scientific discovery」。
2. 时间对比（p.498 Table 1、p.499）：人工 359–424 h vs Robin 不到 2 h；「551 papers in 30 min compared with ... 294 h for a human ... 200-fold reduction」。注意：人工时间为外部调研估计值，非直接实测。
3. dAMD 关键实验（p.501 右栏）：ripasudil「outperformed Y-27632 and increased RPE cell phagocytosis 1.89-fold compared with DMSO controls (Fig. 4b; human analysis showed a 1.75-fold increase)」；KL001 在 RPE-SC 中为 hit（p.502）。
4. ABCA1 机制（p.501 右栏）：「threefold upregulation (adjusted P = 2.13 × 10⁻³³) of ABCA1」，在 RPE-SC 用 ripasudil 复现（Supplementary Fig.17）。
5. 消融与基线（p.503）：移除 Falcon 或同时移除 Crow+Falcon 大幅增加幻觉引用；Finch 在 BixBench 22.8±1.7% vs Sonnet 3.7 单独 1.6±1.2%；OpenAI Deep Research 生成 17 个候选在该吞噬实验「None ... were hits ... did not suggest ROCK inhibition」（Extended Data Fig.6）。
6. 护栏与边界（p.503 右栏 guardrails 段）：优先选已有安全 profile 候选、lab-in-the-loop 输出须经标准临床前验证、用经 red-teaming 与 RLHF 对齐的现成 LLM、查询经 LLM 分类器过滤不安全主题。opportunities 段：「Robin does not yet produce precise, executable protocols」「Finch ... reliant on prompt engineering by domain experts」。
7. 临床效力边界（p.503 左栏 Discussion）：「would of course require validation in a suitable disease model and ultimately in a randomized, placebo-controlled trial to confirm clinical validity」（p.502「in vivo validation ... would be necessary for definitive comparison」）。

**(6) 数据、实验设置或论证前提**
疾病 dAMD；细胞模型 ARPE-19 及 Eye-Bank for Sight Restoration 老年患者原代 RPE-SC。实验由人工执行：药物孵育 1 h、pHrodo beads 或牛 ROS 孵育 3 h、流式测吞噬（Fig.2b）。Finch 分析：8 条独立 trajectory 元分析达成共识；流式与 RNA-seq 各 n=3 runs，rubric 评分 RNA-seq 86±0%、流式 100±0%（p.503）。统计 Dunnett 检验、n=3/4 孔、s.e.m.。论证前提：人工时间来自 von Hippel 等、Sboner 等及 Anaconda 调研（Table 1 脚注），即对比基线为外部估计非本项目实测；「200-fold」基于该估计。

**(7) 适用范围、局限与可能反例**
- 仅在 dAMD 的 RPE 吞噬体外模型验证，未做体内，不构成临床有效证据。
- Robin 不自动生成可执行实验方案，实验设计与执行仍由人类完成——「半自主 + lab-in-the-loop」，不能表述为「自主科学家」。
- Finch 在 BixBench 总体 22.8%、多步生物信息 15.3%，多步流水线任务仍弱；可靠性强依赖领域专家 prompt 工程。
- 成本时间对比用外部调研估计作人工基线，存在估计口径偏差；「200 倍」应作量级非精确实测。
- 单一适应证、单一实验室、单批细胞供体，泛化到其他疾病与材料科学仅为作者推断（p.503 提及 materials science）。
- 已知风险：ROCK 抑制剂此前已被提出用于湿性 AMD 等新生血管视网膜疾病（p.503 Discussion 自述），Robin 新颖性集中在「dAMD + 吞噬增强机制」组合，而非 ROCK 抑制本身。
- 引用幻觉在仅移除 Crow 时被 Falcon 掩盖（44.5±6.37% 引用为幻觉，p.503），提示文献检索栈可靠性依赖双层 agent。

**(8) 与第 1 课教学的关联**
- slides P04 钩子：把研究动作显式拆解为可命名 agent 职责（Crow/Falcon=外部输入摄取与证据整理；Finch=证据整理与研究判断；Robin 整体=原型验证后回写），直接呼应八阶段链路。
- 可追溯性：摘要（p.497）「All hypotheses, experimental directions, data analyses and data figures in the main text ... were produced by Robin」作「结论必须可追溯证据与上游决策」正向案例；同时人工实验、人工核验流式与 RNA-seq 分析体现人工核验点。
- 科研伦理：显式讨论 guardrails、安全对齐、临床前验证与 RCT 门槛，与第 2 课「Agent 权限、研究工件、伦理与披露」衔接。
- 口径：验证集中于「dAMD 的 RPE 吞噬体外实验」具体任务与条件，不得表述为「通用自主科学家」或「AI 发现了 AMD 新药」——后者超出原文证据强度。

**(9) AI 初始阅读地图（未核验）**
中心问题：AI 多 agent 能否端到端自动完成科学发现；论证结构：引言—系统设计—dAMD 案例验证—消融与对比—讨论局限；关键术语：multi-agent、lab-in-the-loop、hypothesis generation、RPE phagocytosis、ROCK inhibitor、ABCA1、PaperQA2；预期证据：架构图、时间对比表、体外药效图、RNA-seq 差异表达、消融；待追问：是否体内验证、人工时间基线如何得出、是否与通用 LLM agent 对照、安全护栏。

**(10) 本地原文定位与文本核对**
用 `pdftotext` 本地提取，逐页定位至少 7 处可复查位置。书目与 DOI 经首页与正文逐字核对，卷期 655, 497–505 与 PDF 页眉一致 ✓。「semi-autonomous」「lab-in-the-loop」为原文用词 ✓。ripasudil 1.89 倍、ABCA1 adjusted P=2.13×10⁻³³、Finch 22.8%、Deep Research 0 hits 均为原文数字 ✓。「200-fold」出自正文但人工基线为外部估计已标注 ✓。局限与 guardrails 段为原文所列 ✓。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
1. 过度概括为「自主科学家」：原文明确 semi-autonomous（摘要、p.498）且实验由人工执行（Table 1 脚注 c「Performed by a human scientist ... lab-in-the-loop」），已据原文纠正。
2. 把体外效力表述为临床有效：原文 p.503 明确要求「randomized, placebo-controlled trial」，已保留。
3. 混淆「新药」与「新适应证」：ripasudil 是已上市药，新颖性在 dAMD+吞噬增强组合（p.501/503），已纠正。
4. 把「200 倍」当精确实测：人工时间为外部调研估计（Table 1 脚注），已标量级非实测。
5. 遗漏 Finch 弱项与 prompt 依赖：已补 BixBench 22.8%、多步 15.3%、领域专家 prompt 依赖。
6. 遗漏引用幻觉风险：已补移除 Crow 时 44.5% 幻觉、Falcon 掩盖。
7. 未发现虚构错误：书目、页码、作者单位、数字经逐项核验一致。

**(12) 最终人工判断（草稿，待教师定稿）**
Robin 适合作第 1 课「多 agent 系统连接研究动作」课堂钩子：(1) 把文献检索、假设生成、数据分析、假设更新显式映射为可命名 agent 职责，与八阶段对应；(2) 显式承认半自主、lab-in-the-loop、不可生成可执行方案、依赖人工 prompt、需 RCT 验证等边界，是讨论人工核验点与证据强度的好素材；(3) 消融与 Deep Research 对照为「agent harness 相对裸 LLM 的增量」提供同任务弱证据。课堂口径：本卡结论仅支持「在 dAMD 的 RPE 吞噬体外模型及特定配置下，Robin 半自动产出经初步体外验证的候选药 ripasudil 与 KL001 及 ABCA1 这一可能新靶点」；不得表述为「通用自主科学家」或「AI 发现 AMD 新药/治愈 AMD」。建议 slides P04 仅展示 Fig.1 架构与摘要定位句，旁注「体外验证 + 人工执行实验」。证据强度：单一适应证、单一实验室、体外单批次、n=3/4，按课程标准属「单一证据 + 部分消融对照」，不标 stable，标 review。

---

## 精读卡 7：Hao et al. 2026 影响与收缩

**(1) 完整书目信息**
Hao, Q., Xu, F., Li, Y., Evans, J. "Artificial intelligence tools expand scientists' impact but contract science's focus." *Nature* 649, 1237–1243 (2026). 29 January 2026. DOI: 10.1038/s41586-025-09922-y. Received 2 January 2025；Accepted 14 November 2025；Published online 14 January 2026. 作者单位：清华电子工程系/BNRist、中关村学院、芝加哥大学 Knowledge Lab & 社会系、Santa Fe Institute。本地 PDF 24 页（正文 7 页 + Methods/EDD）。

**(2) 来源类型与证据角色**
同行评审 Nature 原创研究（Article），观察性大规模计量科学学研究（scientometric observational study）。第 1 课 slides P05 钩子——区分「个人效率提升」与「科学整体进步」两层次问题。**关联性证据，非因果证明**（作者自述）。按课程证据标准属「单一观察性研究」，可作线索与背景，不能作稳定结论单独成立。

**(3) 本文试图回答的问题**
AI 工具采用对个体科学家的产出、引用与职业发展有何影响？对整个科学领域的主题范围、后续参与与知识分布有何影响？个体「扩张」与集体「收缩」是否同时出现？

**(4) 作者的中心主张**
在自然科学领域，AI 工具采用与个体科学家影响力显著扩张（更多论文、更多引用、更早成为项目负责人）相关联，同时与集体科学探索范围收缩（主题覆盖变窄、后续参与下降、向数据丰富热门区域集中）相关联。作者概括为「个人影响扩张 vs. 集体科学范围收缩」张力，并指出 AI 当前更倾向自动化既有热门领域而非开拓新领域。

**(5) 关键证据及原文位置**（Nature 页码）
1. 摘要核心数字（p.1237）：「Scientists who engage in AI-augmented research publish **3.02 times** more papers, receive **4.84 times** more citations and become research project leaders **1.37 years** earlier」「AI adoption shrinks the collective volume of scientific topics studied by **4.63%** and decreases scientists' engagement with one another by **22%**」。
2. 识别模型与数据（p.1237–1238）：「41,298,433 research papers spanning from 1980 to 2025 in the OpenAlex dataset」（Web of Science 交叉验证）；BERT 模型「average F1-score of 0.875」（p.1238）；专家标注一致性「average Fleiss' κ of 0.964」（p.1238）；共识别「310,957 AI-augmented papers, comprising 0.75% of all selected papers」（p.1239）。
3. 个体影响（p.1239「AI expands scientists' impact」节）：「3.02 times more papers (t ≥ 47.18, P < 0.001)」「4.84 times more citations (t ≥ 30.32, P < 0.001)」；项目负责人晋升 AI 采用者 7.33 年（R²=0.995）vs 非采用者 8.70 年（R²=0.987），差 1.37 年（p.1240）。
4. 集体收缩（p.1240「AI contracts science's focus」节）：「4.63% contracted median collective knowledge extent across science, consistent across all six disciplines」；用 SPECTER 2.0 嵌入（768 维）定义 knowledge extent 为采样论文在向量空间的 diameter；「data availability seems to be a major impacting factor」（Supplementary Fig.25）。
5. 后续参与下降（p.1241「AI reduces scientific engagement」节）：「22% less follow-on engagement (t ≥ 8.10, P < 0.001)」；采样 590,325,130 对论文分析。
6. 局限自述（p.1242）：「we cannot fully identify the causal linkage between AI adoption and scientific impact」；识别方法「misses subtle and unmentioned forms of AI use」；聚焦自然科学未涵盖其他领域。

**(6) 数据、实验设置或论证前提**
数据：OpenAlex 41,298,433 篇自然科学论文（1980–2025），Web of Science 交叉验证。学科：生物、医学、化学、物理、材料、地质六学科。AI 时代划分：ML、DL、GAI 三阶段。AI 论文识别：两阶段微调 BERT（标题+摘要集成），F1=0.875，专家 Fleiss' κ=0.964。知识范围度量：SPECTER 2.0（110M 参数，768 维，max length 288 tokens），以采样批次论文 diameter 衡量 knowledge extent。因果识别：控制早期职业位置、考察数据可用性，但作者明确无法完全识别因果。统计：t 检验、χ²、中位数检验，99% CI。

**(7) 适用范围、局限与可能反例**
- 关联非因果：作者自述「cannot fully identify the causal linkage」。所有 3.02×、4.84×、-4.63%、-22% 均统计相关非因果效应。选择偏差（更优秀/资源丰富者更可能采用 AI）可能未完全控制。
- AI 使用识别不全：仅靠标题+摘要 BERT 识别，遗漏隐性、未明示 AI 使用，可能低估或错分。
- 学科范围有限：仅自然科学六学科，未涵盖人文社科、CS 本身；生成式 AI 时代数据较短，作者称 preliminary。
- 度量依赖嵌入模型：knowledge extent 依赖 SPECTER 2.0 嵌入空间，嵌入偏差影响收缩结论。
- 数据库偏差：OpenAlex 覆盖、引用归并等问题。
- 反例：论文也承认 AI 论文家族层面 knowledge extent 反而扩大 3.46%（p.1240–1241），与集体收缩并存。

**(8) 与第 1 课教学的关联**
- slides P05：作课堂钩子引出「AI 提升个人效率 ≠ 科学整体进步」核心张力，区分两层次问题。
- 八阶段：本文处于「问题定义→证据整理→研究判断」示范——把模糊争议（AI 是否促进科学）拆为两可测子问题（个人 vs 集体）并各配证据。
- 证据标准：本卡标「单一观察性研究、关联非因果」，符合「关键结论至少绑定一项可核验直接证据；稳定需两项独立证据；单一证据须记录支持强度与适用边界」。
- 科研伦理与 AI 使用披露：本文本身用 BERT/SPECTER 等 AI 完成研究，是「用 AI 研究科学」元案例，可引出「AI 输出不构成证据，须回原文/数据核验」。
- 第 1 课口径：不可将 3.02×、4.84× 讲成「AI 使科学家产出增加」的因果表述；必须说「在本文样本中，采用 AI 的研究者年均论文数是非采用者的 3.02 倍（相关，非因果）」。

**(9) AI 初始阅读地图（未核验）**
主题：AI 对科学的双面影响（个人 vs 集体）；核心数字 3.02×、4.84×、1.37 年、-4.63%、-22%；方法 BERT 识别、41.3M OpenAlex；结论 AI 扩张个人影响但收缩集体焦点；过度概括风险：把 associated with 讲成导致。均未核验。

**(10) 本地原文定位与文本核对**
用 `pdftotext` 本地提取，逐条比对摘要数字与正文/方法/图表对应位置。3.02×、4.84×、1.37 年、4.63%、22% 五数字在摘要（p.1237）与正文对应节（p.1239–1241）均可定位，文字一致未夸大。41,298,433（p.1237–1238）、F1=0.875（p.1238）、Fleiss' κ=0.964（p.1238）、AI 论文占比 0.75%（p.1239）均与正文一致。p.1242 自述「cannot fully identify the causal linkage」确认关联性。knowledge extent 定义于 p.1240，基于 SPECTER 2.0 嵌入 diameter，核验通过。22% 后续参与下降在 p.1241 节核验通过（n=590,325,130）。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
- 过度概括（高）：将 associated with 译述为「导致/使提升」是最大误读风险，第 1 课用此文献须显式声明「关联非因果」。原文 p.1242 明确否认完全因果识别。
- 数字脱离定义（中）：4.63% 主题范围收缩依赖 SPECTER 2.0 嵌入 diameter 定义，脱离定义讲会误导。定义位于 p.1240。
- 样本范围误植（中）：推广到「所有科学」或「所有 AI 使用」属过度概括。作者限定自然科学六学科，生成式 AI 部分为 preliminary。
- AI 识别不全（中）：仅靠标题/摘要识别，低估隐性 AI 使用。p.1242 自述。
- 个人 vs 集体张力被简化（低）：论文也发现 AI 论文家族层面 +3.46% 扩张与集体 -4.63% 收缩并存，只讲「集体收缩」会遗漏。
- AI 初始地图遗漏：初读未注意论文家族 +3.46% 扩张与集体 -4.63% 收缩并存，人工核验时补充。
- 未发现虚构数字、伪造引文或篡改统计量。

**(12) 最终人工判断（草稿，待教师定稿）**
本文适合作第 1 课 slides P05 课堂钩子，区分「个人效率提升」与「科学整体进步」两层次问题。使用口径：
1. 明确标注为观察性计量研究，关联非因果；引用数字须连同定义与样本一起呈现（41.3M、OpenAlex、BERT 识别、F1=0.875、六学科）。
2. 关键数字按原文口径：「采用 AI 的研究者年均论文数是非采用者的 3.02 倍（t≥47.18, P<0.001）」——不可说「AI 使论文产出增加 3.02 倍」；引用、1.37 年晋升、4.63% 知识范围收缩（须解释 knowledge extent）、22% 后续参与低，同上。
3. 呈现张力：同时给个人扩张与集体收缩，并提示论文家族 +3.46% 扩张与集体 -4.63% 收缩并存，避免简化。
4. 适用边界：自然科学六学科，1980–2025，识别仅基于标题/摘要，生成式 AI 时代为初步性。
5. 证据等级：单一观察性研究，作线索与课堂讨论钩子，不作「AI 是否促进科学」稳定结论。
- 建议教师使用前重新核验 Nature 原文页码与数字。

---

## 精读卡 8：Tao「Mathematics in the Age of AI」(ICM 2026)

**(1) 完整书目信息**
Terence Tao（陶哲轩，UCLA）. "Mathematics in the Age of AI". International Congress of Mathematicians 2026 (ICM 2026) 公开演讲，讲稿日期 2026 年 7 月 24 日。类型：公开演讲幻灯讲稿（slide transcript），非正式出版物。无 DOI、ISBN、期刊编号。本地存档 `references/library/talk/age-of-ai-icm-2026.pdf`（52 页）。在课程中为第 1 课课堂案例（非「已核验事实来源」）。

**(2) 来源类型与证据角色**
会议公开演讲，作者本人幻灯讲稿。未经同行评议、未经编辑出版流程，属「权威研究者个人观点陈述」。作课堂案例，用于分析 AI 使用层级、证明消化链、限制披露与演讲叙事结构。能力数据（First Proof 第二批结果、算力成本等）属易变信息，不作课程已核验结论。在课程证据标准中可作「线索」，不可作「稳定结论」直接证据。

**(3) 本文试图回答的问题**
顶层问题（演讲称「Community Response Question」，p.6）：数学界应如何回应现代 AI 技术及其声称的数学能力？作者将其定性为「元数学的、政治的、伦理的、文化的」问题而非数学问题本身（p.7）。演讲不试图回答 AI 能力是否成立，而回答一个正交补问题（p.13/15）：在假设 AI 具备一定研究级数学能力前提下，数学界的目标、价值与实践应如何重新审视。

**(4) 作者的中心主张**
- 数学界正进入「数学价值与实践基础的危机」（p.2 类比 1900–1930 基础危机）。
- 在 AI 能力假设（Working Hypothesis，p.15–16）成立前提下，单纯优化「解题数量」会触发 Goodhart 定律（p.21），使原本大体一致的多重数学目标分叉（p.23）。
- 应降低「证明生成」与「首次解决」权重，提升「证明消化」（表述、发表、经典化）权重（p.42/47）。
- 必须把 AI 使用的负责任披露常态化（p.46）。
- 上述分析应从问题求解推广到教学、指导、招聘、基金申请、公众外展等所有方面（p.49–50）。

**(5) 关键证据及原文位置**（PDF 物理页码）
1. Working Hypothesis（p.15–16）：「AI tools will, reasonably soon, become capable of performing a reasonable fraction of research-level mathematical tasks ...」；强调条件分析，p.16「I am not asking you to want, believe, or accept that this hypothesis is true」。
2. First Proof 第二批数据（p.14）：2026 年 5 月 28 日受控条件下测 4 个 AI harness；10 道研究级新题 7 道被至少一团队以可发表质量解决；单题算力成本 10–1000 美元；专家按正确性与表述评审。来源 1stproof.org（p.13）。注：演讲者引用的第三方评估，未附原始数据集与评审报告，属易变信息。
3. 证明消化链六阶段（p.24/26/29/37/43）：proof generation → verification → exposition → publication → digestion → canonicalization。每阶段对应一次目标修订（p.24 仅解决尽可能多未解问题；p.26 增验证为正确；p.29 增能清晰表述与理解；p.37 增被社区消化接受；p.43 增纳入权威理论）。
4. Goodhart 定律（p.21）：「When a measure becomes a target, it ceases to good measure. (1975)」；指出生成式 AI 非接地性与 AI 公司财务激励加剧该风险。
5. canonicalization 为最慢、最不易被 AI 优化却最有价值（p.42）：「the slowest stage of all ... least amenable to optimization by AI tools. But it is the most valuable part of the entire process.」
6. erdosproblems.com 上 AI 生成证明无人验证（p.28）：「Many are likely to be correct, but no human expert has yet volunteered to verify and vouch for them.」
7. AI 表述局限（p.30）：拼写语法近完美，但常「在琐事上长篇大论，对最有趣、最新颖部分一笔带过甚至遮蔽」，常不指明与既有文献联系。
8. AI 过程不透明（p.36）：「current AI tools are quite opaque about their problem-solving process ... particularly true for proprietary models whose inner workings remain a corporate secret.」
9. 负责任披露与脚注 7（p.46）：正文「Normalize the responsible disclosure of AI assistance」；脚注 7 自述本演讲幻灯「AI tools were used to autocomplete text and to generate diagrams in these slides」。
10. rule of thumb（p.48）：若作者无法令人信服地就结果做一场清晰、专家级、正确且规范署名的报告，则该结果不应发表。
11. Leiden declaration（p.45）：目标与价值讨论起点，链接 leidendeclaration.ai，指明 Jim Portegies 在 7 月 26 日另一演讲主题。
12. Thurston 引文（p.34）：引自 "On proof and progress in mathematics" (1994)——「The measure of our success is whether what we do enables people to understand and think more clearly and effectively about math.」

**(6) 论证前提与例证**
核心前提：Working Hypothesis（AI 将具备合理水平研究级数学能力），整个分析条件性，演讲者反复声明证据是否支持该假设与后续论证正交（p.16/18）。方法前提：借用数学精确语言澄清元数学问题（p.7），用 conjecture/hypothesis/orthogonal complement 做概念框架。例证策略：以「问题求解」为单一 case study（p.20），明确声明非数学职业全部。历史类比：将当下比作 1900–1930 基础危机（p.2–4）。价值前提：多重数学目标过去「大体正相关」因而可互为代理，是 Goodhart 风险论证基础。

**(7) 适用范围、局限与可能反例**
- 条件性结论，仅在 Working Hypothesis 成立时有意义；明确限于「问题求解」侧面（p.20），不直接覆盖理论建构、教学。
- 能力数据属易变：First Proof 第二批（7/10、10–1000 USD/题、4 harness，p.14）为 2026-05-28 单次评估，演讲未附完整数据集与评审报告，后续批次可能改变结论。课程中不作已核验结论。
- 未控科学条件：演讲者自承公开证据「多数未在受控科学条件下收集」，存在报道偏差与非科学激励（p.12）。
- 图示简化：目标分叉图自注「极度简化，实际应高维」（p.23 脚注 3）。
- 张力：演讲者主张提升 canonicalization 权重，但该阶段恰被描述为「最不易被 AI 优化」（p.42）——资源向其倾斜是否加剧社区人力瓶颈，演讲未给量化方案。
- proof abundance/indigestion（p.44）为预言性判断，证据为「征兆已现」，尚未稳定。
- rule of thumb（p.48）以「能否做专家级报告」为发表门槛，可能对非演讲型研究者不公，演讲未讨论。
- 时效：Leiden declaration、1stproof.org、mathlib.org 等链接与状态需授课前重新核验。

**(8) 与第 1 课教学的关联**
- 八阶段·阶段 8 回写与表达：Tao 证明消化链（exposition→publication→digestion→canonicalization，p.29–43）正是「回写与表达」在数学领域展开。可用于 slides P28–P29 说明：表达不是附录，而是结论能否被社区接受、能否进入权威理论的关口。
- 阶段 6 研究判断：Working Hypothesis 条件性分析（p.15–16）示范「现在怎么做」判断结构——把不可知能力问题悬置，转而分析可控价值与实践。对应 P24「证据回答支持到哪里，判断回答现在怎么做」。
- 阶段 4 外部输入摄取 / 阶段 5 证据整理：First Proof 数据（p.14）在课堂只作「外部输入候选」进入，对应 P23–P24 与 P20「一句流畅总结在核验前只能算线索」。
- 阶段 1 问题定义：Goodhart 定律与目标分叉（p.21/23）对应 P22「先问清楚，再检查必要条件」——AI 使度量与目标脱钩的风险是问题定义阶段必须显式化的内容。
- 可追溯/可审计交互：Tao 指 AI 过程不透明、专有模型内幕为公司机密（p.36），对应 P19「报告是产物，研究是可检查的过程」与 P17/P30–P35 OpenCode 演示。
- 科研伦理与 AI 使用披露：脚注 7 自述「AI 用于自动补全文本与生成图表」（p.46）是 P16「AI 使用底线」最佳实例——权威讲者也在做显式披露，且披露范围具体到「文本补全/图表生成」层级而非笼统「使用了 AI」。
- 演讲叙事结构本身作案例：Tao 用 conjecture→hypothesis→orthogonal complement 做元数学化框架，对应本课「把研究动作显式化」方法论；其「条件性分析不要求听众接受假设」的姿态，对应课程「结论必须可追溯到证据与上游判断，失败实验与冲突证据不得选择性删除」。

**(9) AI 初始阅读地图（未核验）**
演讲双层结构：(A) 能力问题（AI Capability Conjecture）被明确搁置；(B) 价值与实践问题（Goals and Values Question）作为正交补展开。核心模型：证明从生成到经典化六阶段流水线，每阶段一次目标修订，显示「优化单点度量触发 Goodhart」。演讲者立场：提升消化权重、常态化 AI 使用披露、条件性分析不预判能力。待核验：First Proof 数据是否如所述、canonicalization「最不易被 AI 优化」是否为判断而非实证、Leiden declaration 内容与状态。

**(10) 本地原文定位与文本核对**
用 `pdftotext` 本地提取 52 页（696 行），按 form feed 分页定位。复查（页码 = PDF 物理页码）：Community Response Question 提出于 p.6，元数学定性 p.7 ✓；AI Capability Conjecture 模板 p.8–11，弱/强形式 p.10–12 ✓；First Proof 与 1stproof.org p.13，第二批数据 p.14 ✓；Working Hypothesis p.15–16，条件性声明 p.16 ✓；Goals and Values Question p.17–18，目标清单 p.19，Goodhart p.21，目标分叉图 p.23 ✓；六阶段 p.24/26/29/37/43 ✓；erdosproblems.com 无人验证 p.28，AI 表述局限 p.30，过度优化移除自然摩擦 p.31，Bourgain 1991 批注图 p.33，Thurston 引文 p.34，AI 过程不透明 p.36 ✓；canonicalization slowest/least amenable/most valuable p.42 ✓；indigestion/proof abundance/impedance mismatch p.44–45，Leiden declaration p.45，responsible disclosure 与脚注 7 p.46，rule of thumb p.48，closing thoughts p.49–50，基础设施清单（Mathlib、Mathematical Discourse、Erdős problems、SAIR 等）p.52 ✓。本卡 (5) 字段所有页码与引文均与原文一致。

**(11) AI 的错误/过度概括/遗漏/已检查风险（偏差审计）**
- 过度概括（已检查）：易将 Tao 的「问题求解 case study」概括为「整个数学职业的结论」。原文 p.20 明确限定为单一侧面。
- 能力数据误用（已检查）：易将 First Proof 7/10、10–1000 USD 当已核验结论引用。原文 p.12 自承公开证据多未在受控条件下收集、存在报道偏差、部分成本未披露；p.14 数据为单批次。
- 条件性误读（已检查）：易将「Working Hypothesis 成立」误读为演讲者断言 AI 已具备该能力。原文 p.16 明确条件分析、不要求接受。
- canonicalization 论证张力（已检查）：初读易忽略「提升 canonicalization 权重」与「该阶段最不易被 AI 优化」的资源张力。
- 遗漏检查：本 AI 未发现演讲对「非英语数学社区」「非问题求解领域」的展开，原文确实未覆盖（p.20/49），属范围限制非遗漏。
- 链接时效（已检查）：leidendeclaration.ai、1stproof.org、mathlib.org、erdosproblems.com、mathematicaldiscourse.org、sair.foundation 等状态需授课前重核。
- 未发现明显事实性错误或内部矛盾（在演讲自述「极度简化」「条件性」前提下）。

**(12) 最终人工判断（草稿，待教师定稿）**
适合作第 1 课课堂案例，用途限定为：AI 使用层级披露（脚注 7）、证明消化链（六阶段流水线）、条件性研究判断（Working Hypothesis）、演讲叙事结构（元数学化框架）。**不适合**作课程已核验的能力结论来源；First Proof 等数据在课堂只作「外部输入候选」演示，必须现场标注「未核验/易变」。教学建议：与 slides P16（AI 使用底线）、P19（报告是产物研究是可检查的过程）、P21–P29（八阶段）、P28–P29（回写与表达）联合使用；课堂明确指出「本演讲是权威研究者个人观点陈述，非同行评议论文」以示范来源类型辨识。证据强度：作「叙事与框架案例」支持强度高；作「能力事实」支持强度为单源、易变，不得标 stable。授课前需重核所有外链状态与 First Proof 后续批次结果。

---

## 附：整合者核验与剩余风险

1. **8 份文献原文位置**：每张卡至少 2 个可复查位置（实际 6–13 处），均由 `pdftotext` 从本地 PDF 提取，页码与 PDF 对应。
2. **书目信息**：8 份 DOI/卷期/年份与 reading-list.md 逐项核对一致；Simon/Hamming 无 DOI 已注明，页码基于本地 PDF 版本（Simon 印刷页 p.111–138 / Hamming 1997 版 pp.209–215）。
3. **偏差审计**：8 张卡均如实记录，未虚构错误；Lu 卡额外记录了生成 Agent 的一处 AI 偏差实例（卷号混淆，见精读卡 4 字段 11 第 4 条）。
4. **课程锚点**：每张卡「与第 1 课教学关联」字段至少一个具体锚点（对应 slides 页码或八阶段阶段）。
5. **版权**：未复制大段版权全文，仅引关键句与页码位置。
6. **授课前必修核验**：First Proof 后续批次、ICLR 2025 ICBINB 70% 与主会 32% 接收率官方来源、所有外链状态、Simon/Hamming 页码（改引他版时）、Nature 论文可能存在的 correction。
7. **状态**：本卡集为草稿，待教师定稿；AI 导航部分标「未核验」，原文位置已从本地 PDF 提取。
