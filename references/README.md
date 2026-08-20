# 参考资料索引

最后核验：2026-08-12（新增 pi-and-prime-agent.md：pi / Prime Agent 讲师参考对照笔记）

`references/notes/` 保存备课分析与核验记录，`references/library/` 保存默认不纳入 Git 的原始参考。课程结论不直接以本目录中的汇总文字为依据；引用前应回到原始论文、官方文档、课程主页或上游仓库核验。

## 来源分级

- A：官方文件、正式出版物、上游项目或课程主页，可作为相应类型事实的直接依据；A 只表示来源身份可靠，不表示所有材料都能承担研究证据。
- B：高质量二手整理，可帮助定位原始材料，关键结论仍需回源。
- C：社交媒体、博客、聚合列表或未复核笔记，只作为探索线索。

时效性字段：

- 稳定：方法或历史材料，短期内不易变化。
- 授课前复核：工具能力、课程页面、项目状态和安装方式可能变化。
- 原件待核：当前工作区缺少正式原件，不能据此作正式断言。

来源角色必须另行标注：研究论文用于研究主张，正式规范用于行为边界，News、Comment 与 Careers feature 用于背景、案例或线索，产品/项目文档用于经核验的功能与限制。期刊品牌、正式 PDF 或 A 级来源不能替代这一判断。

## 当前文件

| 文件 | 类型 | 主要用途 | 级别 | 时效性与核验说明 |
| --- | --- | --- | --- | --- |
| [material-contracts.md](./material-contracts.md) | 课程材料契约 | 规定讲义、教案、逐页母稿与正式 PPT 的内容门边界；统一文献核验四态 | 课程内部规则 | 2026-08-07 建立；不替代 `course/` 权威课程文件 |
| [AutoResearch.md](./notes/AutoResearch.md) | 链接与项目笔记 | AutoResearch、AI Scientist、课程与工作流案例入口 | B/C | 2026-07-29 已核对文件存在；具体项目描述和链接须授课前回源 |
| [skills_ref.md](./notes/skills_ref.md) | Skills / MCP 集合项目笔记 | 分析任务契约、上下文、权限、状态、循环和评价的案例池 | B/C | 2026-07-29 纳入索引，2026-08-08 增补新 skill 库与 MCP 条目；不作为 Skills 安装教程或项目质量背书 |
| [nature.md](./notes/nature.md) | Nature/Science 文献清单笔记 | AI for Research 代表性论文与系统工作入口 | B/C | 2026-07-29 纳入索引；二手整理，自称非完全穷尽，含具体 DOI/期号/日期（部分标注“约”）属易变，引用具体条目前须回期刊原站核验；不作为已核验事实 |
| [regulation.md](./notes/regulation.md) | 国内 AI 科研规范整理 | 人主智辅、AI 使用声明、责任归属与禁止事项的检索线索 | B/C | 2026-08-04 重申：二手整理不能作为正式政策证据；具体文件名、条款与发布日期须回学校、教育部、科技部或学会官网核验 |
| [research-method-选目分析.md](./notes/research-method-选目分析.md) | 全文通读与选目记录 | 对 `research-method/` 资料逐项分级、去重并映射课程课次 | B/C | 2026-07-29 纳入索引；是备课决策记录，不是学生阅读材料或直接证据 |
| [research-method-补充推荐.md](./notes/research-method-补充推荐.md) | 库外文献推荐线索 | 补足可复现、Agent、实验自动化和评价复盘等空白 | B/C | 2026-07-29 纳入索引；候选条目须回原始论文、官方文档或上游仓库核验后再采用 |
| [pi-and-prime-agent.md](./notes/pi-and-prime-agent.md) | Agent harness 对照笔记（讲师参考） | pi（极简 harness 底座）与 Prime Agent（自我改进研究型 Agent）的三方对照、八要素映射、钉死版本、安全摘录与待核验清单 | B/C | 2026-08-12 建立；两项目活跃迭代，功能宣称授课前回源；只作分析对象，不构成对学生安装或使用的建议 |
| [mi-case-registry.md](./notes/mi-case-registry.md) | MI 贯穿案例素材登记 | 课程 2.0 MI 素材元数据（素材 ID、许可、脱敏状态、教学可用性） | 课程内部规则 | 2026-08-08 建立骨架；只存元数据，不存原文与未发表内容；登记表待用户素材到位后填充 |
| [research-method/](./library/research-method/) | 外部克隆资料库（论文生命周期讲义/经验集） | 传统人工科研方法背景阅读池，按 think→search→write→submit→revise→present→template 组织 | B/C | 2026-07-29 克隆（来源 github.com/secdr/research-method）；多为知乎专栏/教授经验散文/高校讲座 PPT/经典英文写作指南，关键结论须回源；不作为课程证据；含易变条目（2021 基金统计、工具软广等），授课前复核；自带 .git，已加入 .gitignore 不纳入版本管理 |

## 克隆资料库 research-method/ 课次映射

来源 `github.com/secdr/research-method`，B/C 级背景阅读池。仅覆盖"通用科研"段，**不覆盖 AI/Agent 核心与可复现实验工程**；不得作为主干把课程拉回论文写作课定位。引用须回源核验作者与许可。

| 仓库分类 | 可对应课次 | 选用提示 |
| --- | --- | --- |
| how to think | 第6课问题定义/第一性原理、阶段3机制假设 | 经验类居多；"胡晓峰：科学问题""钱志云：CS 研究 idea"可作选题线索，缺可证伪命题训练 |
| how to search | 第3课文献检索、第4课论文精读 | "沈向洋/华刚：读论文三层次四阶段十问题"直接对应第4课；WoS/ScienceDirect 检索式对应第3课 |
| how to write | 第14课论文式表达 | "施柏鑫：审稿人视角写 CVPR 论文""Science Research Writing""Collected Advice"CS 契合度高 |
| how to revise | 第15课同行评审 | "国际期刊审稿流程与要点"、rebuttal 系列支撑"接受批评-证据回写"逻辑 |
| how to presentation | 第16课最终展示 | "Oral/Spotlight Video 指南"可作展示技巧补充 |
| how to submit / use template | 无直接对应 | 课程"提交"指研究门材料，非期刊投稿；不纳入主干 |

已评估不纳入主干引用的条目（易变或低相关）：

- `2021年度计算机科学学科基金项目申请资助情况及展望`：过时基金统计
- `模型评估指标可视化/自动画 Loss-Accuracy 曲线工具`：工具软广
- `王光辉_出国留学申请总结`、励志类读博心得：与课程方法论无关

| [unesco.md](./notes/unesco.md) | 国际机构立场整理 | 以人为本、透明披露、人工验证与 AI 素养的国际依据 | B/C | 2026-07-29 纳入索引；二手整理，UNESCO 指南持续更新，具体文件版本与条款须回 UNESCO 官网核验；原则共识可作导向，具体条款授课前回源 |

## 已下载论文与期刊材料（papers/）

本目录既含研究论文，也含期刊 News、Comment 与 Careers feature。原件可作为题名、作者、日期和原文表述的 A 级来源，但只有研究论文能按其研究设计支持研究主张；其他类型须按下表限定用途。核心论文的首页文本/内部标记已与 DOI 核对；重复副本与相同工作的 arXiv 预印本版已按既有记录处理。

### 核心论文（nature.md 清单）

| 文件 | 论文 | DOI | 核验说明 |
| --- | --- | --- | --- |
| [papers/s41586-023-06221-2.pdf](./library/papers/s41586-023-06221-2.pdf) | Wang et al. 2023, Scientific discovery in the age of AI（综述） | 10.1038/s41586-023-06221-2 | 用户下载，首页已核对 |
| [papers/Boiko2023-coscientist.pdf](./library/papers/Boiko2023-coscientist.pdf) | Boiko et al. 2023, Autonomous chemical research with LLMs（Coscientist） | 10.1038/s41586-023-06792-0 | 2026-07-29 下载（Nature OA），首页已核对 |
| [papers/s41586-025-09922-y.pdf](./library/papers/s41586-025-09922-y.pdf) | Hao et al. 2026, AI tools expand scientists’ impact but contract science’s focus | 10.1038/s41586-025-09922-y | 用户下载，首页已核对 |
| [papers/s41586-026-10265-5.pdf](./library/papers/s41586-026-10265-5.pdf) | Lu et al. 2026, Towards end-to-end automation of AI research | 10.1038/s41586-026-10265-5 | 2026-07-29 下载（Nature OA），首页已核对；已删去重复副本 |
| [papers/s41586-026-10644-y.pdf](./library/papers/s41586-026-10644-y.pdf) | Gottweis et al. 2026, Accelerating scientific discovery with Co-Scientist | 10.1038/s41586-026-10644-y | 用户下载 Nature 正式版（已删 arXiv 2502.18864 预印本版） |
| [papers/s41586-026-10652-y.pdf](./library/papers/s41586-026-10652-y.pdf) | Ghareeb et al. 2026, A multi-agent system for automating scientific discovery（Robin） | 10.1038/s41586-026-10652-y | 用户下载，首页已核对 |

已评估不纳入：

- Gao & Wang 2024, Quantifying the use and potential benefits of AI in scientific research（10.1038/s41562-024-02020-5, Nature Human Behaviour）— 与已下载的 Hao 2026（s41586-025-09922-y）主题/方法重叠，后者更新更尖锐（扩张+收缩），Gao 2024 偏单向 benefits，论点已被涵盖；如需同主题计量论文对比案例可再补

### 补充材料（nature.md 未列，用户补充）

| 文件 | 内容 | DOI/来源 | 核验说明 |
| --- | --- | --- | --- |
| [papers/s41567-025-03042-0.pdf](./library/papers/s41567-025-03042-0.pdf) | Naskręcki & Ono, Mathematical discovery in the age of AI（Nature Physics Comment） | 10.1038/s41567-025-03042-0 | 首页已核对；与陶哲轩 ICM 演讲主题呼应，第一课可用 |
| [papers/d41586-025-01069-0.pdf](./library/papers/d41586-025-01069-0.pdf) | Heidt, “Choosing the right AI tool for the job”（Nature Careers feature） | 10.1038/d41586-025-01069-0 | 2026-08-04 核对 3 页原件：*Nature* 640, 555–557 (2025)，栏目为 Advice, technology and tools / Work / Careers；只用作 2025 年工具生态快照和工具选择案例，不作同行评议研究证据或 2026 年工具推荐；授课前复核产品状态 |
| [papers/d41586-026-00934-w.pdf](./library/papers/d41586-026-00934-w.pdf) | Nature News “AI research assistants are changing science”（2026-03-26） | 10.1038/d41586-026-00934-w | 2 页社论/新闻，首页已核对 |
| [papers/s41598-026-63438-7_reference.pdf](./library/papers/s41598-026-63438-7_reference.pdf) | Bianchini, Geuna & Shermatov, Scientific discovery in the age of AI and supercomputing（Sci Rep, Article in Press） | 10.1038/s41598-026-63438-7 | 首页已核对；计量视角 |
| [papers/How-AI-slop-is-causing-a-crisis-in.md](./library/papers/How-AI-slop-is-causing-a-crisis-in.md) | Gibney, How AI slop is causing a crisis in science（Nature 新闻） | 10.1038/d41586-025-03967-9 | 网页存为 Markdown，配图存于 how-ai-slop/；与课程“生成报告≠研究”“防幻觉”相关 |

## 已收集书籍（books/）

课程涉及书籍的原件，按书名归档，与 papers/（论文）平级；不按课次分子目录，课次映射在本表"适用课次"列。级别 A 为正式出版物原件，授课前仍须核对版次与页码。

| 文件 | 书籍与章节 | 适用课次 | 来源 | 时效与核验说明 |
| --- | --- | --- | --- | --- |
| [books/Simon_Herbert_A_The_Sciences_of_the_Artificial_3rd_ed.pdf](./library/books/Simon_Herbert_A_The_Sciences_of_the_Artificial_3rd_ed.pdf) | Simon, H. A. *The Sciences of the Artificial*, 3rd ed., Ch. 5 | 第 1 课课后引导阅读（问题、目标、约束与评价） | [MIT Press](https://mitpress.mit.edu/9780262537537/the-sciences-of-the-artificial/) | 2026-07-29 原件已放入；章主题与 [lesson-01-slides.md](../lessons/lesson-01/slides.md) P39 引导阅读一致；授课前核对版次与章号 |
| [books/Hamming_1997_-_The_Art_of_Doing_Science_and_Engineering.pdf](./library/books/Hamming_1997_-_The_Art_of_Doing_Science_and_Engineering.pdf) | Hamming, R. W. *The Art of Doing Science and Engineering: Learning to Learn* (1997) | 第 1 课引导阅读（补充，与 Simon 并列；科研方法意识、品味与学会学习） | [Stripe Press](https://stripepress.com/)（2020 再版）；原版 CRC Press 1997 | 2026-07-29 原件已放入；出版方经联网核验；授课前核对所引版次与页码；具体书页 URL 因网络限制待回源补全 |

## 外部讲座与演讲素材（talk/）

他人讲座 PPT、演讲笔记、talk 录像整理稿的归处，与 papers/、books/ 平级。目录已建立。

收录边界：
- 收：他人讲座 PPT、演讲笔记、公开 talk 整理稿等外部参考素材。
- 不收：课程自己的正式授课 PPT 母稿（归 `lessons/lesson-NN/slides.*`）；试讲材料（归 `archive/trial-lecture/`）；学校视觉模板原件（归 `references/library/template/`）。
- 与 `research-method/` 的边界：`research-method/` 是整体克隆库（含 "how to presentation" 等），不拆入 `talk/`，靠本索引"克隆资料库课次映射"表定位。

| 文件 | 讲者/来源 | 主题 | 适用课次 | 级别 | 时效与核验说明 |
| --- | --- | --- | --- | --- | --- |
| [talk/age-of-ai-icm-2026.pdf](./library/talk/age-of-ai-icm-2026.pdf) | 陶哲轩，ICM 2026 公开演讲 | AI 时代数学研究价值与实践、多目标精化、证明消化链与 AI 使用披露案例 | 第 1 课 / 全程 AI 使用披露案例 | A | 2026-07-29 纳入索引；演讲文本稳定，但所引 First Proof（1stproof.org）、Leiden declaration（leidendeclaration.ai）、Mathlib 等能力声称与链接属易变信息，授课前须回源核验；能力数据作为报告观点引用，不作已核验事实 |

## 视觉模板（template/）

学校视觉模板与版式参考。

| 文件 | 内容 | 适用范围 | 级别 | 时效与核验说明 |
| --- | --- | --- | --- | --- |
| [template/交大模版.pptx](./library/template/交大模版.pptx) | 上海交大视觉样例 | 学校视觉元素与版式线索 | B | 仅含 2 页视觉样例，存在 `test1` 和空占位符；不能视为完整官方模板；正式授课 PPT 不以此代替制作 |

## 优先回源入口

### 正式规范与政策（A）

- [上海交通大学《关于在教育教学中使用 AI 的规范》](https://soo.sjtu.edu.cn/upload/file/20250217/20250217162021.pdf)：本课程最近的校级制度基线；授课前检查是否有修订或院系补充规定。
- [中国科学院科研活动原始记录中生成式人工智能使用提醒](https://www.cas.cn/sygz/202409/t20240910_5031186.shtml)：科研记录与责任边界的外部正式参照，不能替代学校与具体任务规则。
- [Nature Portfolio artificial intelligence policy](https://www.nature.com/nature-portfolio/editorial-policies/ai)：发表与同行评议场景参照；只适用于其覆盖的出版角色与材料。

### 上游项目与官方文档（A）

- [Karpathy AutoResearch](https://github.com/karpathy/autoresearch)
- [Sakana AI Scientist](https://github.com/sakanaai/AI-Scientist)
- [Sakana AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)
- [Orchestra Research AI Research Skills](https://github.com/Orchestra-Research/AI-research-SKILLs)
- [OpenCode Documentation](https://opencode.ai/docs/)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs/)
- [Pi Coding Agent（earendil-works/pi）](https://github.com/earendil-works/pi)（pi.dev；课堂只作分析对象）
- [Prime Agent（PrimeIntellect-ai/prime-agent）](https://github.com/PrimeIntellect-ai/prime-agent)（课堂只作分析对象）

### 工作流案例入口（上游仓库优先，A/B）

- [co-researcher](https://github.com/poemswe/co-researcher)
- [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar)
- [Wenyu Chiou AI Research Skills](https://github.com/WenyuChiou/ai-research-skills)
- [Deep Research Skills](https://github.com/Weizhena/Deep-Research-skills)
- [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)

### 同类课程主页（A）

- [Berkeley RDI LLM Agents, Fall 2024](https://rdi.berkeley.edu/llm-agents/f24)
- [Johns Hopkins Lifelong Learning](https://lifelonglearning.jhu.edu/indies/)
- [eCornell Agentic AI Architecture](https://ecornell.cornell.edu/certificates/ai/agentic-ai-architecture/)
- [UNL Agentic AI for Workflow Automation](https://newsroom.unl.edu/announce/unlcive/19549/104494)

## 使用规则

1. 先用本索引定位材料，再回到原始来源核验作者、版本、日期、许可和具体结论。
2. 不记录易过时的 Star 数、技能数量或“最新/首个”等宣传性表述；如课堂确需使用，授课前现场复核并标注日期。
3. AI 生成内容、README 宣传语和社媒帖子是线索，不单独构成课程证据。
4. 关键教学判断在 [reference-analysis.md](../course/reference-analysis.md) 中记录来源、适配方式和限制。
5. 新增参考时补充来源类型、用途、级别、核验日期和时效性；不要修改原始附件内容。
6. 遇到期刊 News、Comment、Careers feature 或品牌内容时，先登记栏目与文体，再决定能支持的主张；不得因 DOI 或期刊名把它升级为研究论文。
