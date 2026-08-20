# 逐课参考阅读清单

版本：v2.2.0
最后更新：2026-08-12

变更记录：

- v2.2.0 (2026-08-12)：第 11 课新增课堂案例"Prime Agent 自我改进研究 Agent 案例簇"（钉 commit，附两篇预印本，仅分析对象）；第 12 课新增课堂案例"Pi Coding Agent 最小 harness 拆解案例"（钉 commit）；两课各达 5 项上限；正式书目与课时结构不变。
- v2.1.0 (2026-08-10)：G3 选题训练配套——第 5 课 Qian 课堂案例扩为六种构思模式（填空/扩展/造锤找钉/小处泛化/复现前作/外部来源，已对本地转载副本核验）；第 6 课新增课堂案例霍强《创新研究到底怎么做？》（四维选题标准卡的兴趣与意义参照）。
- v2.0.4 (2026-08-05)：修正项目重组后的历史归档路径标签。
- v2.0.3 (2026-07-30)：修正第 2 课诚信提醒发布机构名为“中国科学院科研道德委员会”，与官方页面及 lesson-02 handout/slides 一致。
- v2.0.2 (2026-07-30)：区分作者团队工作稿与正式同行评议稿；将未公开论文的绝对禁令调整为授权、规则、环境与最小披露条件。
- v2.0.1 (2026-07-30)：修正第 1 课 Tao ICM 2026 本地讲稿路径。
- v2.0.0 (2026-07-29)：改为“正式书目 + 课堂案例”双层结构；以经典书籍选章、同行评议论文、正式规范和原始论文为主干；加入 AI 导航—原文核验—偏差审计阅读法。
- v1.0.0 (2026-07-29)：初版逐课阅读清单，已归档至 [archive/superseded-docs/reading-list-v1.0.0.md](../archive/superseded-docs/reading-list-v1.0.0.md)。

本清单面向 16 次正式课程。每课共 3-4 项，不超过 5 项；通常只要求 1 项核心阅读，其他正式文献按项目需要选读，系统、项目、演讲和本地讲义只作为课堂案例或中文辅助材料。书籍只指定章节，不布置整本阅读。

## 一、书目层级与使用规则

### 正式书目

只收录以下材料：

- 经典或公认基础性学术书籍的指定章节；
- 同行评议论文、正式技术报告和共识报告；
- 政府、学术组织、出版社或标准组织发布的正式规范；
- 快速演进领域中无法由经典文献替代的原始研究论文。

正式书目优先链接 DOI、出版社、期刊、会议或作者机构页面。付费书籍通过学校图书馆或正版渠道获取，不在课程仓库复制受版权保护的全文。

### 课堂案例

GitHub 仓库、厂商工程文章、协议文档、大学课程讲义、演讲稿、转载讲义和真实审稿回复可以用于拆解设计与失败，但不作为经典文献，也不单独支撑课程的规范性结论。案例必须标明版本或核验日期。

### 中文导读

英文原典保留原文。教师提供中文阅读范围、术语和以下三个固定问题，不制作未经授权的全文翻译：

1. 作者的中心主张和论证结构是什么？
2. 最强证据位于何处，支持到什么范围？
3. 哪些假设、限制或反例影响它在本人项目中的适用性？

## 二、AI 辅助经典阅读协议

课程明确鼓励使用 AI 快速建立阅读地图，但 AI 摘要不等于完成阅读。每篇核心阅读采用以下流程：

1. **AI 导航**：让 AI 给出中心问题、论证结构、关键术语、预期证据和待追问问题；全部标记为“未核验”。
2. **原文核验**：人工阅读指定章节，至少记录两个可复查的章节、页码、图表、公式或实验位置。
3. **AI 质疑**：让 AI 根据已核验内容提出反例、遗漏和适用边界，与个人笔记比较。
4. **偏差审计**：记录至少一处 AI 的错误、过度概括、遗漏或高风险判断。如果未发现明显错误，记录检查过的风险点及核验依据，不虚构错误。
5. **人工定稿**：由学生写出最终阅读卡，区分作者主张、原文证据、个人判断和 AI 建议。

核心阅读的轻量记录持续保存在个人项目中，不逐周正式提交。第 6 课问题门只统一检查至少 3 张与个人研究项目直接相关的完整精读卡。

保密评审材料、敏感数据和许可不允许处理的全文，不得上传到未经授权的外部模型。作者团队自己的未公开工作稿不作一刀切处理：全文进入个人消费级外部服务时默认拒绝；只有在共同作者或材料权利人同意、项目与机构规则允许、处理环境获认可、披露范围最小且保留人工核验与使用记录时，才可转为有条件允许。优先使用公开版本、必要片段、抽象化问题、本地或机构环境。正式同行评议稿遵守期刊或评议组织者的保密与 AI 使用政策。

AI 生成的作者、题名、年份、页码、DOI 和引文必须回到正式来源逐项核验。

## 第 1 课：AI 辅助科研导论、OpenCode 与八阶段研究链路

### 正式书目

1. **核心｜经典书籍选章｜约 30 分钟**
   Herbert A. Simon. *The Sciences of the Artificial*, 3rd ed. MIT Press, 1996（2019 reissue）. 选读 Chapter 5, “The Science of Design: Creating the Artificial”。[出版社页面](https://mitpress.mit.edu/9780262537537/the-sciences-of-the-artificial/)
   用途：区分自然现象研究与人工物设计，理解 CS/AI 研究中“问题—目标—约束—评价”的基本结构。

2. **任选｜经典演讲/书籍章节｜约 20 分钟**
   Richard W. Hamming. *The Art of Doing Science and Engineering: Learning to Learn*. Stripe Press, 2020 reissue. 选读 “You and Your Research”。[出版社页面](https://press.stripe.com/the-art-of-doing-science-and-engineering)
   用途：讨论重要问题、研究品味、勇气和长期工作方式。

3. **任选｜原始综述论文｜约 25 分钟**
   Wang, H. et al. “Scientific discovery in the age of artificial intelligence.” *Nature* 620, 47–60 (2023). DOI: [10.1038/s41586-023-06221-2](https://www.nature.com/articles/s41586-023-06221-2)。选读引言、总览图和与本人方向相关的一节。本地正式版见 [PDF](../references/library/papers/s41586-023-06221-2.pdf)。
   用途：定位 AI 介入科学发现链路的环节、机会与限制。

### 课堂案例

4. **演讲案例**
   Terence Tao. *Mathematics in the Age of AI* (ICM 2026 public lecture). [本地讲稿](../references/library/talk/age-of-ai-icm-2026.pdf)。只分析 AI 使用层级、证明消化链、限制披露和演讲叙事，不把其中的能力数据视为课程已核验结论。

## 第 2 课：科研伦理、Agent 权限、研究工件与追踪

### 正式书目

1. **核心｜正式规范｜约 15 分钟**
   中国科学院科研道德委员会：《关于在科研活动中规范使用人工智能技术的诚信提醒》（2024）。[官方页面](https://www.cas.cn/sygz/202409/t20240910_5031186.shtml)
   用途：建立 AI 辅助检索、生成内容披露、数据真实性、评审保密和责任归属的国内底线。

2. **任选｜共识报告选章｜约 25 分钟**
   National Academies of Sciences, Engineering, and Medicine. *Fostering Integrity in Research*. National Academies Press, 2017. 选读 Chapter 2, “Foundations of Integrity in Research: Core Values and Guiding Norms”, pp. 27–38. DOI: [10.17226/21896](https://nap.nationalacademies.org/catalog/21896/fostering-integrity-in-research)。
   用途：从客观、诚实、开放、公平、问责和守护责任理解科研诚信，而不只记忆禁止事项。

3. **任选｜经典论文选段｜约 20 分钟**
   Saltzer, J. H., & Schroeder, M. D. “The Protection of Information in Computer Systems.” *Proceedings of the IEEE* 63(9), 1278–1308 (1975). DOI: [10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939)。只读 fail-safe defaults、complete mediation、separation of privilege 和 least privilege。
   用途：为 Agent 权限矩阵提供经典安全原则，而不是依赖某个平台的权限界面。

### 课堂案例

4. **工程文章案例**
   Anthropic. [*Building Effective Agents*](https://www.anthropic.com/engineering/building-effective-agents) (2024)。只分析工具接口、人工检查点、停止条件和沙箱测试；不作为科研伦理规范或产品使用教程。

## 第 3 课：文献检索与证据角色判断

### 正式书目

1. **核心｜经典研究方法书选章｜约 30 分钟**
   Booth, W. C. et al. *The Craft of Research*, 5th ed. University of Chicago Press, 2024. 选读 Chapter 3, “Finding and Evaluating Sources”，含 “Using Generative Artificial Intelligence” quick tip。[出版社页面](https://press.uchicago.edu/ucp/books/book/chicago/C/bo215874008)
   用途：区分来源类型、相关性、可靠性和来源在论证中的角色。

2. **任选｜正式技术报告选段｜约 25 分钟**
   Kitchenham, B., & Charters, S. *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. EBSE-2007-01, 2007. 选读 protocol、search strategy 和 study selection。[机构索引](https://ebse.webspace.durham.ac.uk/ebse-bibliography/guidelines-for-performing-systematic-literature-reviews-in-software-engineering/)
   用途：把检索、纳入和排除过程变成可复核方法。

3. **任选｜正式报告规范｜约 15 分钟**
   Page, M. J. et al. “The PRISMA 2020 statement: an updated guideline for reporting systematic reviews.” *BMJ* 372:n71 (2021). DOI: [10.1136/bmj.n71](https://www.bmj.com/content/372/bmj.n71)。只读 checklist 和 flow diagram。[PRISMA 官方入口](https://www.prisma-statement.org/prisma-2020-statement)
   用途：学习透明报告逻辑，不要求 CS/AI 项目机械套用医学综述格式。

## 第 4 课：AI 辅助论文精读与深度分析

### 正式书目

1. **核心｜经典论文｜约 20 分钟**
   Keshav, S. “How to Read a Paper.” *ACM SIGCOMM Computer Communication Review* 37(3), 83–84 (2007). DOI: [10.1145/1273445.1273458](https://doi.org/10.1145/1273445.1273458)。[作者课程 PDF](https://cs.uwaterloo.ca/~brecht/courses/854-http-video-2012/readings/keshav-paper-reading.pdf)
   用途：以三遍阅读法控制阅读深度，并建立实验论文的检查问题。

2. **任选｜经典研究方法书选章｜约 25 分钟**
   Booth et al. *The Craft of Research*, 5th ed. 选读 Chapter 4, “Engaging Sources”，重点为 reading for a problem、argument、data and support。
   用途：防止把作者主张、数据、证据和个人推断混为一谈。

### 课堂案例

3. **中文检查表案例**
   沈向洋、华刚：《读科研论文的三个层次、四个阶段与十个问题》。[本地转载副本](<../references/library/research-method/how to search/沈向洋、华刚：读科研论文的三个层次、四个阶段与十个问题 - 知乎.pdf>)。只作为中文提问清单；正式分发前须确认原始出处与许可。

## 第 5 课：综述、证据地图与研究空白识别

### 正式书目

1. **核心｜正式技术报告选段｜约 30 分钟**
   Kitchenham & Charters. *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. 选读 study quality assessment、data extraction 和 synthesis。
   用途：从“列举文献”转向质量判断、结构化提取与证据综合。

2. **任选｜经典研究方法书选段｜约 20 分钟**
   Booth et al. *The Craft of Research*, 5th ed. 选读 4.3–4.5：reading for a problem、arguments、data and support。
   用途：从来源中提取问题、论证与证据角色。

3. **任选｜同行评议方法论文｜约 20 分钟**
   Pautasso, M. “Ten Simple Rules for Writing a Literature Review.” *PLOS Computational Biology* 9(7):e1003149 (2013). DOI: [10.1371/journal.pcbi.1003149](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003149)。
   用途：检查综述的范围、批判性、结构和迭代。

### 课堂案例

4. **问题生成与研究空白案例**
   Qian, Z. *How to Look for Ideas in Computer Science Research*. [本地转载副本](<../references/library/research-method/how to think/How to Look for Ideas in Computer Science Research _ by Zhiyun Qian _ Jan, 2021 _ Medium.pdf>)。分析其六种构思模式（填空、扩展、造锤找钉、小处泛化、复现前作、外部来源）与 gap 候选生成；“表格空位”只是问题来源之一，不能自动证明问题重要或真实。

## 第 6 课：研究问题、问题定义与第一性原理

### 正式书目

1. **核心｜经典研究方法书选章｜约 35 分钟**
   Booth et al. *The Craft of Research*, 5th ed. 选读 Chapter 1, “From Topics to Questions” 和 Chapter 2, “From Questions to a Problem”。
   用途：把兴趣收敛为研究问题，并用 “So what?”、实际后果和知识后果检查重要性。

2. **任选｜经典论文｜约 25 分钟**
   Platt, J. R. “Strong Inference.” *Science* 146(3642), 347–353 (1964). DOI: [10.1126/science.146.3642.347](https://pubmed.ncbi.nlm.nih.gov/17739513/)。
   用途：用竞争假设、关键实验和排除逻辑形成可证伪命题。

3. **任选｜经典演讲/书籍章节｜约 15 分钟**
   Hamming. “You and Your Research.” 本课只读“重要问题”和研究品味部分。
   用途：区分“可做”“新颖”和“值得投入”的问题。

### 课堂案例

4. **中文问题审校案例**
   胡晓峰：《浅谈科研课题中的“科学问题”》。[本地副本](<../references/library/research-method/how to think/胡晓峰：浅谈科研课题中的“科学问题”.pdf>)。用于识别把背景、意义、工程任务或“怎么做”误写成科学问题的情况。

5. **选题标准参照案例**
   霍强：《讲堂 | 霍强：创新研究到底怎么做？》。[本地副本](<../references/library/research-method/how to think/讲堂 _ 霍强：创新研究到底怎么做？.pdf>)。任选，约 15 分钟。用“Start with why”与 Passion/Excellence/Impact 三标准作四维选题标准卡（意义/新颖性/可行性/兴趣）的兴趣与意义维度参照；不替代论证链位置的重要性检查。

## 第 7 课：机制假设、研究判断与实验设计

### 正式书目

1. **核心｜经典书籍选章｜约 35 分钟**
   Box, G. E. P., Hunter, J. S., & Hunter, W. G. *Statistics for Experimenters: Design, Innovation, and Discovery*, 2nd ed. Wiley, 2005. ISBN: 978-0-471-71813-0. 选读 Chapter 1, “Catalyzing the Generation of Knowledge” 和 3.4, “Comparison, Replication, Randomization, and Blocking in Simple Experiments”。[出版社配套页](https://bcs.wiley.com/he-bcs/Books?action=index&bcsId=9686&itemId=0471718130)
   用途：把实验理解为模型—推论—数据—修正的迭代学习过程。

2. **任选｜经典论文重读｜约 15 分钟**
   Platt. “Strong Inference.” 本课只读替代假设、关键实验与结果区分力部分。
   用途：为主假设设计竞争解释和反驳条件。

3. **任选｜正式统计手册选段｜约 20 分钟**
   NIST/SEMATECH. [*e-Handbook of Statistical Methods: Process Improvement—Experimental Design*](https://www.itl.nist.gov/div898/handbook/pri/pri.htm)。选读 objectives、factors、responses、randomization、replication 和 blocking。
   用途：检查变量、对照、测量和混杂因素。

### 课堂案例

4. **构思策略案例**
   Raskar, R. *Coming up with New Ideas in Imaging*. [本地 PPT](<../references/library/research-method/how to think/Coming up with New Ideas in Imaging.ppt>)。用于生成机制候选，不作为假设成立的证据。

## 第 8 课：学生研究方案分享与设计诊所

### 正式书目

1. **核心｜经典研究方法书选段｜约 20 分钟**
   Booth et al. *The Craft of Research*, 5th ed. 选读 5.5, “Planning Your Research Argument” 和 10.2, “Planning Your Paper”。
   用途：检查问题、理由、证据与预期反对意见是否构成完整论证。

2. **任选｜经典论文｜约 15 分钟**
   Whitesides, G. M. “Whitesides’ Group: Writing a Paper.” *Advanced Materials* 16, 1375–1377 (2004). DOI: [10.1002/adma.200400767](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.200400767)。
   用途：理解“好的论文提纲也是好的研究计划”，先组织数据和论证再写文字。

### 课堂案例

3. **经典研究提案讲义案例**
   Peyton Jones, S. [*Writing a Great Research Proposal*](https://simon.peytonjones.org/assets/pdfs/great-research-proposal.pdf)。选读 problem、idea、evidence、success criteria 和 work plan，用于准备可被质询的研究方案；该材料是经典教学讲义，不作为研究结论的学术证据。

## 第 9 课：Baseline、实验规格与可复现实验工程

### 正式书目

1. **核心｜同行评议方法论文｜约 25 分钟**
   Wilson, G. et al. “Good Enough Practices in Scientific Computing.” *PLOS Computational Biology* 13(6):e1005510 (2017). DOI: [10.1371/journal.pcbi.1005510](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)。
   用途：建立项目组织、数据管理、版本记录、脚本和协作的最低可靠实践。

2. **任选｜原始研究论文｜约 25 分钟**
   Pineau, J. et al. “Improving Reproducibility in Machine Learning Research.” *Journal of Machine Learning Research* 22(164), 1–20 (2021). [JMLR 正式页面](https://www.jmlr.org/papers/v22/20-303.html)。
   用途：将 ML reproducibility checklist 转化为 baseline、环境和实验报告要求。

3. **任选｜正式政策｜约 15 分钟**
   ACM. [*Artifact Review and Badging, Version 1.1*](https://www.acm.org/publications/policies/artifact-review-and-badging-current) (2020)。选读 documented、consistent、complete、exercisable、available 和 results validated 的定义。
   用途：区分“代码可下载”“工件可运行”和“结果得到独立验证”。

4. **任选｜原始研究论文｜约 20 分钟**
   Bouthillier, X. et al. “Accounting for Variance in Machine Learning Benchmarks.” *Proceedings of Machine Learning and Systems* 3 (2021). [MLSys 正式页面](https://proceedings.mlsys.org/paper_files/paper/2021/hash/0184b0cd3cfb185989f858a1d9f5c1eb-Abstract.html)。
   用途：检查随机性、方差来源和不公平 benchmark 比较。

## 第 10 课：AI 辅助编码、调试与受限 Agent 执行

### 正式书目

1. **核心｜经典教材选章｜约 30 分钟**
   Russell, S., & Norvig, P. *Artificial Intelligence: A Modern Approach*, 4th ed. Pearson, 2020. 选读 Chapter 2, “Intelligent Agents”：agents and environments、rationality、environment properties、agent structure。[出版社页面](https://www.pearson.com/en-us/subject-catalog/p/artificial-intelligence-a-modern-approach/P200000003500/9780134610993)
   用途：先用经典 Agent 概念理解环境、目标、观察和行动，再分析 LLM coding agent。

2. **任选｜基础性 Agent 论文｜约 25 分钟**
   Yao, S. et al. “ReAct: Synergizing Reasoning and Acting in Language Models.” *ICLR 2023*. [会议页面](https://iclr.cc/virtual/2023/poster/11003)。
   用途：分析 reasoning—action—observation 循环及其错误传播。

3. **任选｜同行评议 HCI 论文｜约 20 分钟**
   Amershi, S. et al. “Guidelines for Human-AI Interaction.” *CHI 2019*. DOI: [10.1145/3290605.3300233](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)。选读人工纠错、控制、反馈和失败处理相关准则。
   用途：设计人工确认点和可恢复交互，而不是假设 Agent 始终正确。

### 课堂案例

4. **基准案例**
   Jimenez, C. E. et al. [*SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*](https://www.swebench.com/original.html), ICLR 2024。只分析任务构造、执行环境、测试判定及 benchmark 局限。

## 第 11 课：实验自动化、AutoResearch 循环与结果追踪

### 正式书目

1. **核心｜经典可复现论文｜约 25 分钟**
   Sandve, G. K. et al. “Ten Simple Rules for Reproducible Computational Research.” *PLOS Computational Biology* 9(10):e1003285 (2013). DOI: [10.1371/journal.pcbi.1003285](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)。
   用途：建立结果—脚本—参数—输入—随机种子的可执行追踪链。

2. **任选｜原始研究论文｜约 25 分钟**
   Huang, Q. et al. “MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation.” *ICML 2024*, PMLR 235, 20271–20309. [PMLR 正式页面](https://proceedings.mlr.press/v235/huang24y.html)。
   用途：用任务、成功标准、轨迹和失败类型评价 ML 实验 Agent。

3. **任选｜前沿原始论文｜约 25 分钟**
   Lu, C. et al. “Towards end-to-end automation of AI research.” *Nature* (2026). DOI: [10.1038/s41586-026-10265-5](https://www.nature.com/articles/s41586-026-10265-5)。本地正式版见 [PDF](../references/library/papers/s41586-026-10265-5.pdf)。
   用途：分析端到端自动化的任务范围、评价证据和仍需人工判断的边界。

### 课堂案例

4. **上游项目案例**
   Karpathy. [*AutoResearch*](https://github.com/karpathy/autoresearch)。只读 README、`program.md` 和核心循环，分析固定预算、固定指标、保留/丢弃和日志；授课前固定 commit 并复核。

5. **自我改进研究 Agent 案例簇（预印本，仅分析对象）**
   PrimeIntellect. [*Prime Agent*（commit `965941c7`）](https://github.com/PrimeIntellect-ai/prime-agent/tree/965941c750ff816cc4d68d18a5fcea5e0b4c120b)，配 Karten et al. “Continual Harness: Online Adaptation for Self-Improving Foundation Agents.” [arXiv:2605.09998](https://arxiv.org/abs/2605.09998)（预印本）与 Zhang, A. L., Kraska, T. & Khattab, O. “Recursive Language Models.” [arXiv:2512.24601](https://arxiv.org/abs/2512.24601)（预印本）。只分析 `/autonomous` 的预算与质量门设计、harness 状态持久化与回退自述，对照本课四约束；项目发布仅数日、论文未经同行评议，不外推为能力结论，不进学生安装清单；授课前复核。

## 第 12 课：Agent/Skill 逻辑与自主 Research Workflow 设计

### 正式书目

1. **核心｜经典 Agent 论文｜约 30 分钟**
   Wooldridge, M., & Jennings, N. R. “Intelligent Agents: Theory and Practice.” *The Knowledge Engineering Review* 10(2), 115–152 (1995). DOI: [10.1017/S0269888900008122](https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/intelligent-agents-theory-and-practice/CF2A6AAEEA1DBD486EF019F6217F1597)。选读 agent properties、abstract architectures 和 reflection 部分。
   用途：区分 autonomy、reactivity、pro-activeness 和 social ability，不把“调用 LLM”自动等同于 Agent。

2. **任选｜经典工作流论文｜约 25 分钟**
   van der Aalst, W. M. P. et al. “Workflow Patterns.” *Distributed and Parallel Databases* 14, 5–51 (2003). DOI: [10.1023/A:1022883727209](https://research.tue.nl/files/2053121/613310.pdf)。选读 sequence、parallel split、synchronization、exclusive choice、simple merge 和 iteration。
   用途：用可复用控制流模式分析 Skill 和 Agent Workflow，而不是按产品术语分类。

### 课堂案例

3. **工程模式案例**
   Anthropic. [*Building Effective Agents*](https://www.anthropic.com/engineering/building-effective-agents)。比较 prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer 与 autonomous agent；它是工程经验，不是经典理论。

4. **协议架构案例**
   Model Context Protocol. [*Architecture Overview*](https://modelcontextprotocol.io/docs/learn/architecture)。只分析 host、client、server、tools、resources、prompts 和权限边界；授课前复核当前协议版本。现成 Skill 仓库保留在 [resources.md](./resources.md) 案例池，不列为正式阅读。

5. **最小 harness 拆解案例**
   [*Pi Coding Agent*（commit `9795d602`）](https://github.com/earendil-works/pi/tree/9795d602306ef68a97585909e8e79f92a389057b)（pi.dev，`@earendil-works/pi-coding-agent`）。只读该版本 README 与默认工具清单，分析"默认仅 read/write/edit/bash 四工具、权限与计划/子 Agent 刻意移出核心"的设计决定；作为八要素拆解的最小对照组，与 OpenCode 显性 harness 对照，不进学生安装清单；授课前复核。

## 第 13 课：工作流评价、结果分析与失败复盘

### 正式书目

1. **核心｜经典 ML 系统论文｜约 25 分钟**
   Sculley, D. et al. “Hidden Technical Debt in Machine Learning Systems.” *NeurIPS 2015*, 2503–2511. [Google Research 正式页面](https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/)。
   用途：从纠缠、反馈回路、隐性消费者、数据依赖和配置债建立失败分类。

2. **任选｜原始研究论文重读｜约 20 分钟**
   Bouthillier et al. “Accounting for Variance in Machine Learning Benchmarks.” 本课只读比较协议、不确定性和结论强度部分。
   用途：让工作流前后对照报告方差和不确定性，而不是只比较单次分数。

3. **任选｜系统评价论文｜约 20 分钟**
   Breck, E. et al. “The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction.” *IEEE Big Data 2017*. [Google Research 正式页面](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)。
   用途：学习用可检查 rubric 评价数据、模型、基础设施和监控，而不是用功能清单代替质量。

### 课堂案例

4. **失败轨迹案例**
   MLAgentBench 的 evaluation、trajectory 和 failure sections。要求把失败回写为研究判断、限制或下一轮修改，不只汇报成功率。

## 第 14 课：论文式表达与回写

### 正式书目

1. **核心｜经典研究方法书选章｜约 35 分钟**
   Booth et al. *The Craft of Research*, 5th ed. 选读 Chapter 5 “Making Good Arguments”、Chapter 7 “Assembling Reasons and Evidence” 和 10.2 “Planning Your Paper”。
   用途：把 claim、reason、evidence、warrant 和 anticipated objection 组织为可追溯论证。

2. **任选｜经典论文｜约 15 分钟**
   Whitesides. “Whitesides’ Group: Writing a Paper.” *Advanced Materials* 16, 1375–1377 (2004). DOI: [10.1002/adma.200400767](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.200400767)。
   用途：用 outline、图表和数据组织驱动写作。

3. **任选｜经典科学写作论文｜约 25 分钟**
   Gopen, G. D., & Swan, J. A. “The Science of Scientific Writing.” *American Scientist* 78(6), 550–558 (1990). [期刊页面](https://www.americanscientist.org/article/the-importance-of-context-in-genetics)。本地副本见 [PDF](<../references/library/research-method/how to write/science-of-writing.pdf>)。
   用途：理解主题位、重音位、旧信息—新信息和读者预期。

### 课堂案例

4. **CS 写作讲座案例**
   Simon Peyton Jones. *How to Write a Great Research Paper*. [本地讲稿](<../references/library/research-method/how to write/How to write a great research paper.pdf>)。只分析贡献列表、示例先行和反馈驱动修改。

## 第 15 课：同行评审、论证门预检与修改工作坊

### 正式书目

1. **核心｜经典 CS 评审论文｜约 25 分钟**
   Smith, A. J. “The Task of the Referee.” *Computer* 23(4), 65–71 (1990)；早期技术报告 UCB/CSD-89-511。[UC Berkeley 正式存档](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1989/6154.html)
   用途：从正确性、新颖性、重要性、表达质量和出版物定位评价论文。

2. **任选｜经典研究方法书选章｜约 25 分钟**
   Booth et al. *The Craft of Research*, 5th ed. 选读 Chapter 9 “Acknowledgments and Responses” 和 Chapter 11 “Revising and Organizing”。
   用途：把反对意见转化为子论证，并区分接受、澄清、补证和保留异议。

### 课堂案例

3. **大学课程讲义案例**
   Stanford Scientific Writing. Unit 8, “How to Do a Peer Review.” [本地课程材料](<../references/library/research-method/how to write/Stanford-科学写作课件/Unit_PDFs-Unit8.pdf>)。用于训练具体、建设性、针对工作而非作者的评审语言；正式分发前确认课程材料许可。

4. **真实回复案例**
   *Responses to Referee #2 Comments*. [本地案例](<../references/library/research-method/how to use template/response letter/Responses to Referee %232 Comments.pdf>)。只分析接受、补证、澄清和保留异议四类回应。魏秀参、施柏鑫等转载材料降为教师备课线索，不进入正式学生书目。

## 第 16 课：最终分享、论证门与项目提交

### 正式书目

1. **核心｜经典书籍选章｜约 30 分钟**
   Alley, M. *The Craft of Scientific Presentations: Critical Steps to Succeed and Critical Errors to Avoid*, 2nd ed. Springer, 2013. DOI: [10.1007/978-1-4419-8279-7](https://link.springer.com/book/10.1007/978-1-4419-8279-7)。选读 Chapter 3 “Structure”、Chapter 4 “Visual Aids”，以及 Critical Errors 3、4、7。
   用途：控制内容范围、建立叙事路径，并让幻灯片承载可辨认的证据而非默认模板。

### 课堂案例

2. **经典 CS 演讲讲义案例**
   Peyton Jones, S. [*How to Give a Good Research Talk*](https://www.microsoft.com/en-us/research/publication/how-to-give-a-good-research-talk/)。选读 audience、story、slides 和 delivery，用于把项目压缩为听众能够复述和检查的研究论证；该材料不作为表达效果的实证研究。

3. **演讲逆向分析**
   Tao. *Mathematics in the Age of AI*. 本课只分析开场、问题推进、案例选择、限制披露和结尾回扣，不重复第 1 课内容。过时的 Oral/Spotlight Video 软件操作指南不再列入学生书目。

## 三、不纳入正式书目的材料

- 知乎、Medium、博客和转载 PDF：可作中文辅助或课堂案例，不标为经典或正式证据。
- GitHub README、厂商文章、协议文档：用于系统拆解和版本化案例，不作为稳定方法论。
- 标题与内容错配、抽取失败、正文损坏或来源不明的文件。
- 重复度高的 SCI 写作口诀、套话模板、投稿信模板和励志类读博文章。
- 旧投稿系统、会议历史规则、工具界面和只展示效果而无评价协议的宣传材料。

## 四、维护与版权

本清单由 [research-method 选目分析](../references/notes/research-method-选目分析.md) 和 [库外补充推荐](../references/notes/research-method-补充推荐.md) 提供候选，再回到出版社、期刊、会议、政府、学术组织或作者机构页面核验。

每轮开课前应：

1. 复核 Agent、MCP、基准和上游仓库的版本、commit 与链接；
2. 核对论文题名、作者、年份、刊物、页码和 DOI；
3. 确认本地 PDF 的来源与课堂分发许可；
4. 通过学校图书馆提供付费书籍和论文的合法访问方式；
5. 检查指定章节、阅读时间与课程任务是否仍匹配；
6. 用更高质量的正式来源替换当前二手案例时，保留变更记录。
