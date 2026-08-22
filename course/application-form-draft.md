---
版本：v1.4.2
最后更新：2026-08-22
文档类型：已批准课程的申请表口径底稿
状态：现行申报口径参考；不替代课程大纲或申请原件
变更记录：
- v1.4.2 (2026-08-22): 明确本文件为已批准课程的申报口径底稿而非待审批课程状态；不修改中英文申请内容
- v1.4.1 (2026-08-05): 更新课程申请原件的本地归档位置说明，不再引用迁移前的参考资料目录
- v1.4.0 (2026-07-29): 中英文同步更新课程实施设计：OpenCode 从第 1 课贯穿全程；不讲现成 Skills 用法而分析 Agent/Skill 逻辑；默认个人项目；新增第 8 课学生分享；正式提交调整为第 6/9/13/16 课四个研究门；学生需设计、实现并评价个人 Agent Workflow
- v1.3.4 (2026-05-14): 移除不可用文献检索入口的可用性表述，改用 AMiner、OpenAlex、Semantic Scholar、DBLP、arXiv 等入口
- v1.3.3 (2026-05-14): 统一中文申请材料中的英文术语口径，改为中文译名为主、首次括注英文或缩写
- v1.3.2 (2026-05-14): 将证据三角验证降级为多源证据核验与证据充分性检查，弱化工件状态硬门槛
- v1.3.1 (2026-05-13): 明确平台下拉字段建议口径，补充教学目标表述，弱化外部趋势过满表述，修正中文引号
- v1.3.0 (2026-05-13): 教学大纲压缩为 6 模块简版，详细 16 课安排指向 syllabus.md
- v1.2.0 (2026-05-13): 补充开课动机段落、工具与环境要求、数据隐私条款；先修要求增加 Git 和命令行；中文简介补充证据类型；第 9 课阶段标注补充"（实验规格）"；明确学生可用自己的研究课题
- v1.1.0 (2026-05-13): 第 12 课中英文大纲同步更新为"AutoResearch 与 Research Agent 工作流"，增加 AutoResearch 元模式和 AI Scientist v1/v2 对比内容
- v1.0.0 (2026-05-13): 初始版本
---

# 上海交通大学研究生课程开设申请表口径底稿

本文件按 `.local/applied/` 中的研究生课程开设申请表原件字段组织，保留课程获批时的申报口径并支持后续一致性检查。它不替代已提交原件或 [课程大纲](./syllabus.md)；行政信息和平台下拉选项仍由课程负责人按学院要求确认。

## 课程基本信息 Basic Information

| 字段 | 建议填写 |
| --- | --- |
| 课程名称（中文） | 智能科研方法 |
| Course Name | AI for Research: Methods and Practice |
| 学分 | 2 |
| 总学时 | 32 |
| 开课季节 | 建议选择：秋季；可按培养方案排课需要调整 |
| 是否跨学期 | 否 |
| 课程性质 | 专业选修课 |
| 课程分类 | 研究生课程 |
| 课程类别 | 建议选择：专业课程；如平台支持前沿交叉课程类别，可按学院口径确认 |
| 课程层次 | 建议选择：硕士生、博士生；如平台只能单选，按培养方案归属确认 |
| 授课语言 | 建议选择：中文；配套英文文献与英文资料。如申报中英文双语课程，需按学院双语课程要求另行确认 |
| 主要上课方式 | 建议选择：讲授；实际教学结合研讨、上机实践和项目指导 |
| 成绩记录方式 | 百分制 |
| 主要考试类型 | 课程项目 / 大作业 |
| 开课单位 | 计算机学院 |
| 所属一级学科 | 计算机科学与技术 |
| 负责教师 | 姓名、工号、单位、邮箱由课程负责人填写 |

## 课程简介（中文）

大模型和智能代理正在深刻改变科研中的文献检索、论文阅读、代码生成、实验迭代和论文写作方式。AutoResearch（自主研究）正在形成重要范式，国际一流高校已开设智能体式人工智能（Agentic AI）和面向科学研究的人工智能（AI for Scientific Research）等相关课程，但普遍侧重技术应用，缺乏系统的科研方法论框架。对研究生而言，关键能力不只是使用工具，而是判断哪些科研环节适合人工智能（AI）增强、哪些必须保留人工判断，并在可复现、可审查、符合学术规范的前提下提升科研效率。当前培养方案中尚无课程系统训练“如何用 AI 做研究”这一能力，本课程填补这一空白。

本课程面向计算机、人工智能、软件工程和数据科学等方向研究生，围绕“人工智能如何增强科研全过程”展开。课程不以单一工具教学为目标，而以八阶段研究链路（问题定义、第一性原理分析、机制假设、外部输入摄取、证据整理、研究判断、原型验证、回写与表达）为主线，训练学生使用大模型、智能代理和自动化实验方法支持科研闭环的每个阶段。OpenCode 从第 1 课起作为统一的课堂工作平台，但平台操作和现成技能（Skill）的安装不是学习目标；课程通过案例分析任务契约、上下文、工具与权限、状态与工件、执行循环、评价机制、人工审核点和失败恢复，引导每位学生为自己的真实科研动作设计、实现并评价一个可审计的科研智能体工作流（Agent Workflow）。课程目标是使学生能够用人工智能增强而非替代科研判断，完成从文献与问题到实验验证和论文表达的可追溯科研闭环，并掌握证据整理、研究判断、可复现实验、科研智能体工作流边界和科研伦理披露等基本能力。课程引入结构化研究方法论：研究工件有标准格式和轻量状态追踪，研究推进有门条件，证据分级与多源核验要求学生区分理论证据、实践证据、对比证据和补充线索等证据角色，说明关键结论的证据来源、支持强度和缺失风险，结论必须可追溯到证据和决策。机器学习（ML）实验自动化作为课程特色模块，重点覆盖实验配置、实验追踪、自动化参数探索、智能体式实验循环、失败实验复盘和人工审核边界。课程强调人工智能输出必须可追溯、可验证、可复盘，并将数据隐私、知情同意、版权许可、署名贡献、潜在误用和人工智能使用披露纳入项目要求。项目默认个人完成，固定同伴组仅用于方案分享、研究门互查和同行评审。学生需记录关键提示词、上下文来源、工具使用、人工核验方式和误导案例。先修要求为 Python 编程基础、机器学习基础、Git 基本操作、命令行环境使用和英文论文阅读能力。课程最终产出包括问题定义、研究计划、证据地图、实验规格、个人科研智能体工作流、评价报告、可运行原型、实验记录、科研伦理与合规说明、人工智能使用记录和论文式短文。

## Course Description

Large language models and AI agents are fundamentally transforming how researchers conduct literature search, paper reading, code generation, experiment iteration, and academic writing. AutoResearch is becoming an important paradigm, and leading international universities have launched related courses in Agentic AI and AI for Scientific Research, yet most focus on technology and applications without a systematic research methodology framework. For graduate students, the critical competency is not merely using tools but judging which research stages benefit from AI augmentation and which require human judgment, while maintaining reproducibility, auditability, and compliance with academic norms. No existing course in the current curriculum systematically trains this capability; this course fills that gap.

This graduate course is designed for students in computer science, artificial intelligence, software engineering, data science, and related areas. It focuses on how AI can augment the research workflow rather than on isolated tool usage. The course follows an eight-stage research chain: problem definition, first-principles analysis, mechanism hypothesis, external input intake, evidence organization, research judgment, prototype validation, and writeback and expression. OpenCode serves as the shared classroom work platform from the first session, but platform operation and the installation of existing Skills are not learning objectives. Through case analysis, students examine task contracts, context, tools and permissions, state and artifacts, execution loops, evaluation mechanisms, human review points, and failure recovery. Each student then designs, implements, and evaluates an auditable Agent Workflow for a real research action in their own project. The teaching objectives are to enable students to augment, rather than replace, research judgment with AI; complete a traceable research loop from literature review and problem formulation to experimental validation and paper-style communication; and master evidence organization, research judgment, reproducible experimentation, Research Agent workflow boundaries, and ethics and AI-use disclosure. The course introduces structured research methodology: research artifacts have standard formats and lightweight status tracking, project progression is governed by gate conditions, evidence classification and multi-source validation require students to distinguish theoretical evidence, practical evidence, comparative evidence, and supplementary leads, and to explain evidence sources, support strength, and missing-evidence risks for key conclusions. Conclusions must be traceable to evidence and decisions. Machine learning experiment automation is included as a distinctive module, covering configuration management, experiment tracking, automated parameter exploration, agentic experiment loops, failure analysis, and human review boundaries. AI-generated outputs must be traceable, verifiable, and auditable, and students must address data privacy, informed consent, copyright and licensing, authorship, potential misuse, and AI-use disclosure. Projects are individual by default; fixed peer groups are used only for proposal sharing, gate checks, and peer review. Students must record prompts, context sources, tool usage, human validation methods, and misleading outputs. Prerequisites include basic Python programming, fundamental machine learning knowledge, familiarity with Git and command-line environments, and the ability to read research papers in English. Final deliverables include a problem definition, a research proposal, an evidence map, an experiment spec, a personal Agent Workflow, an evaluation report, a runnable prototype, experiment records, an ethics and compliance statement, an AI usage log, and a short paper-style report.

## 教学大纲（中文）

课程按五个教学模块组织，共 32 学时。详细 16 次课安排见 [syllabus.md](./syllabus.md)。

| 模块 | 主要内容 | 课时 | 教学方式 | 课程思政内容 |
| --- | --- | ---: | --- | --- |
| 1. 导论、OpenCode 平台、科研伦理与研究工件 | 八阶段研究链路、个人项目工作区、工件状态追踪与门条件、Agent 权限矩阵、人工智能使用记录与伦理检查 | 4 | 讲授、演示、研讨 | 科技创新责任、科研诚信、负责任使用人工智能、数据隐私与知情同意 |
| 2. 文献、证据与问题定义 | 检索式设计、证据角色判断、人工智能辅助论文精读、相关工作矩阵、证据地图、空白识别、问题收敛、可证伪命题和第一性原理推导 | 8 | 演示、实践、研讨、工作坊 | 尊重知识来源、避免伪造引用、严谨求实学风、批判性思维与原创意识 |
| 3. 机制假设、方案分享与可复现基线 | 机制假设、研究判断、实验设计、个人方案分享与反馈、基线（baseline）复现、环境与配置管理、随机种子和实验规格 | 6 | 工作坊、学生分享、案例分析、上机实践 | 面向真实问题的科研责任、公平评价、诚实报告、开源合规与建设性反馈 |
| 4. 受限 Agent、实验自动化与自主工作流 | Agent 辅助编码与调试、实验队列、AutoResearch 循环、任务契约、上下文、工具权限、Skill/MCP、评估机制、个人工作流实现、结果分析与失败复盘 | 8 | 演示、上机实践、工作坊 | 人机协作责任边界、规范化实验记录、安全可控的智能代理使用 |
| 5. 论文表达与项目闭环 | 证据回写、证据充分性检查、论文式写作、同行评审、论证门预检、个人展示与最终提交 | 6 | 研讨、写作工作坊、答辩 | 实事求是、避免夸大结论、学术表达规范、建设性批评、科研责任与透明报告 |

## Syllabus

The course is organized into five teaching modules totaling 32 hours. For the detailed 16-session schedule, see [syllabus.md](./syllabus.md).

| Module | Main Contents | Hours | Teaching Style | Ideological and Ethical Elements |
| --- | --- | ---: | --- | --- |
| 1. Introduction, OpenCode Platform, Research Ethics, and Artifacts | Eight-stage research chain, individual project workspace, artifact tracking and gates, agent permission matrix, AI usage logs, and ethics checks | 4 | Lecture, demonstration, seminar | Responsibility in technological innovation, research integrity, responsible AI use, data privacy and informed consent |
| 2. Literature, Evidence, and Problem Definition | Search query design, evidence role assessment, AI-assisted paper reading, related-work matrices, evidence maps, gap identification, problem refinement, falsifiable propositions, and first-principles derivation | 8 | Demonstration, practice, seminar, workshop | Respect for knowledge sources, avoidance of fabricated citations, rigorous scholarship, critical thinking and originality |
| 3. Mechanism Hypotheses, Proposal Sharing, and Reproducible Baselines | Mechanism hypotheses, research judgment, experiment design, individual proposal sharing and feedback, baseline reproduction, environment and configuration management, random seeds, and experiment specs | 6 | Workshop, student sharing, case analysis, lab practice | Responsibility toward real research problems, fair evaluation, honest reporting, open-source compliance, and constructive feedback |
| 4. Bounded Agents, Experiment Automation, and Personal Workflows | Agent-assisted coding and debugging, experiment queues, AutoResearch loops, task contracts, context, tool permissions, Skills/MCP, evaluation, personal workflow implementation, result analysis, and failure analysis | 8 | Demonstration, lab practice, workshop | Human accountability, standardized experiment records, and safe and controllable AI agent use |
| 5. Paper Writing and Project Closure | Evidence writeback, evidence sufficiency review, paper-style writing, peer review, argumentation pre-check, individual presentation, and final submission | 6 | Seminar, writing workshop, defense | Truthfulness, avoidance of overstated claims, academic communication norms, constructive criticism, and transparent reporting |

## 课程要求（中文）

课程采用过程性评价与最终个人项目结合的方式，不设置每周独立作业分。每位学生围绕一个研究问题持续完成文献分析、问题定义、第一性原理推导、机制假设、证据地图、研究判断、实验规格、原型实现、个人科研智能体工作流、评价报告、结果分析和论文式表达。正式提交安排在第 6、9、13、16 课，分别对应问题门、判断门、验证门和论证门；第 8 课个人方案分享和第 15 课同行评审属于形成性活动。评分包括文献与问题定位 25%、实验设计与可复现性 30%、原型与科研智能体工作流实践 25%、表达、伦理与复盘 20%。所有项目必须提交人工智能使用记录和科研伦理与合规说明，并说明任务契约、上下文来源、工具权限、预算与停止条件、人工核验方式和失败记录。结论必须可追溯到证据和决策。学生不得将未发表的核心研究数据（如未公开的实验数据、未提交的论文全文）发送给外部商业应用程序接口（API），如需使用外部大语言模型（LLM）服务处理敏感数据，应使用学校或课题组部署的本地模型或已签署数据保护协议的服务。

## Requirements

Assessment combines process evaluation with a final individual project; there are no separate weekly-assignment points. Each student works on one research question and completes literature analysis, problem definition, first-principles derivation, mechanism hypotheses, evidence mapping, research judgments, experiment specs, prototype implementation, a personal Agent Workflow, evaluation, result analysis, and paper-style writing. Formal submissions occur after Sessions 6, 9, 13, and 16 for the Problem, Judgment, Validation, and Argumentation Gates. The Session 8 proposal sharing and Session 15 peer review are formative activities. Grading consists of literature and problem formulation (25%), experimental design and reproducibility (30%), prototype and Agent Workflow practice (25%), and communication, ethics, and reflection (20%). Every project must include an AI usage log, an ethics and compliance statement, and a description of the task contract, context sources, tool permissions, budgets and stopping conditions, human validation methods, and failure records. Conclusions must be traceable to evidence and decisions. Students must not send unpublished core research data (such as unreleased experimental data or unsubmitted full papers) to external commercial APIs; when processing sensitive data with LLMs, students should use locally deployed models or services covered by data protection agreements.

## 工具与环境要求（中文）

课程不绑定特定商业工具。OpenCode 作为从第 1 课贯穿全程的主要课堂工作平台，优先连接国内网络环境可直连、开源或学校已部署的模型后端。学生可以使用功能等价的其他 Agent 环境，但不因使用特定平台获得额外分数。

计算与模型资源：课程所需大语言模型（LLM）调用额度由开课单位统一提供或从教学经费中列支，学生无需自费购买应用程序接口调用凭证（API token）。如使用学校 GPU 集群部署开源模型（如 DeepSeek、Qwen、GLM-4），由课程统一配置访问权限。

国内优先工具栈：
- 大语言模型服务：DeepSeek API、通义千问 API、智谱 GLM-4 API、月之暗面 Kimi API（均支持国内直连）
- 统一课堂工作平台：OpenCode（开源，支持多模型后端）
- 可选编程智能体 / 科研智能体：Codex、Claude Code、Cursor、通义灵码或功能等价工具
- 文献检索：AMiner、OpenAlex、Semantic Scholar、DBLP、arXiv
- 实验追踪：MLflow（自部署）、SwanLab（国产）、Weights & Biases（国内可用但需注册）
- 代理框架：LangChain、Dify（国产，可视化编排）、AutoGen

网络要求分层：
- 必须可用（国内直连）：国产大语言模型服务、OpenCode + 国内模型后端、MLflow、Git
- 推荐使用（按当学期网络情况确认）：GitHub、Semantic Scholar、Weights & Biases
- 仅教师演示（不要求学生使用）：Claude Code、OpenAI API 等需要海外网络的服务

学生自备设备要求：能运行 Python 3.10+、Git 和命令行终端的笔记本电脑。无需本地 GPU——计算密集型任务使用学校集群或云端 API。

## Tool and Environment Requirements

The course is not tied to any specific commercial tool. OpenCode is the primary classroom work platform from the first session and should use model backends that are directly accessible within mainland China, open-source, or deployed by the university. Students may use functionally equivalent agent environments, but no platform receives preferential grading.

Computing and model resources: LLM API quotas required by the course are provided by the offering department or funded through teaching budgets. Students are not required to purchase API tokens at their own expense. If open-source models (e.g., DeepSeek, Qwen, GLM-4) are deployed on the university GPU cluster, access will be configured by the course.

Preferred tool stack for domestic access:
- LLM services: DeepSeek API, Tongyi Qianwen API, Zhipu GLM-4 API, Moonshot Kimi API (all directly accessible in China)
- Shared classroom platform: OpenCode (open-source and multi-backend)
- Optional Coding Agent / Research Agent environments: Codex, Claude Code, Cursor, Tongyi Lingma, or functionally equivalent tools
- Literature search: AMiner, OpenAlex, Semantic Scholar, DBLP, arXiv
- Experiment tracking: MLflow (self-hosted), SwanLab (domestic), Weights & Biases (accessible but requires registration)
- Agent frameworks: LangChain, Dify (domestic, visual orchestration), AutoGen

Network access tiers:
- Required (direct domestic access): domestic LLM APIs, OpenCode with domestic model backends, MLflow, Git
- Recommended (availability to be confirmed before each offering): GitHub, Semantic Scholar, Weights & Biases
- Instructor demo only (not required for students): Claude Code, OpenAI API, and other services requiring overseas network access

Student equipment: a laptop capable of running Python 3.10+, Git, and a command-line terminal. No local GPU is required—compute-intensive tasks use the university cluster or cloud APIs.

## 课程资源（中文）

- 课程自编讲义、案例和项目模板。
- 参考网站与项目：Karpathy AutoResearch、Sakana AI Scientist、AI Scientist-v2、Berkeley RDI LLM Agents / Agentic AI 课程、UNL Agentic AI for Workflow Automation、MIT AI Agents and Agentic Web、Johns Hopkins Agentic AI Certificate、eCornell Agentic AI Architecture、Coursera AI for Scientific Research。
- 工具资源：OpenCode 课堂环境、文献检索与管理工具、大语言模型辅助阅读工具、科研智能体与编程智能体工具、实验追踪与配置管理工具、智能体工作流框架、模型上下文协议（MCP）与评估工具。
- 教学案例：现成 Agent/Skill 的结构拆解，以及学生自主工作流的任务契约、权限、评价、失败恢复和人工审核案例。
- 论文和技术报告：课程每轮开课前根据最新研究进展更新。

## Resources

- Instructor-prepared lecture notes, cases, and project templates.
- Reference websites and projects: Karpathy AutoResearch, Sakana AI Scientist, AI Scientist-v2, Berkeley RDI LLM Agents / Agentic AI courses, UNL Agentic AI for Workflow Automation, MIT AI Agents and Agentic Web, Johns Hopkins Agentic AI Certificate, eCornell Agentic AI Architecture, and Coursera AI for Scientific Research.
- Tool resources: the OpenCode classroom environment, literature search and management tools, LLM-assisted reading tools, Research Agent and coding agent tools, experiment tracking and configuration management tools, agent workflow frameworks, MCP, and evaluation tools.
- Teaching cases: structural analysis of existing Agents/Skills and examples of task contracts, permissions, evaluation, failure recovery, and human review in student-designed workflows.
- Research papers and technical reports, updated before each offering according to recent developments.

## 对照检查表建议

| 检查项 | 建议 |
| --- | --- |
| 是否有适用本课程的马工程系列教材可选用 | 否 |
| 教材、教参选用符合国家、学校相关规定 | 是 |
| 课程教学内容是否涉及意识形态问题 | 否 |
| 课程教学内容是否已融入课程思政元素 | 是，融入科研伦理、科研诚信、负责任人工智能、数据安全、开源合规、科技创新责任 |
| 课程教学如涉及中国地图，是否已选用规范地图 | 不涉及 |
