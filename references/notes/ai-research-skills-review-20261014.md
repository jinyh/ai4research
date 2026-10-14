# Research 与 academia Agent Skills 参考审阅

核验日期：2026-10-14
状态：教学设计参考；未安装、未运行这些外部工作流，不作为课程产出的实测证据。

## 审阅范围与发现

| 资料 | 截至核验日的版本／状态 | 可借鉴之处 | 适用边界与不直接采用的部分 |
| --- | --- | --- | --- |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | GitHub Releases 最新显示 v2.72.0（2026-10-01）；目录含 paper-lookup 等研究数据与方法工具 | 按研究动作组织技能；数据库和领域工具可组合；技能说明自身输入、输出、限制与验证 | 大型集合包含多领域能力、脚本和外部服务，不能整包安装或把可调用等同于证据成立。课程借鉴任务级选择、版本记录和审阅，不承诺已验证其效果。 |
| [Paper Search Pro](https://github.com/O0000-code/paper-search-pro) | 主分支 SKILL.md；页面未见稳定发行号，实施时应记录 commit | 多源检索、分层扩展、领域源路由、原始响应留存、来源覆盖说明和停止判断；OpenAlex 可作为默认主源，也可切换，另有语义及专题来源 | 其默认值与覆盖规则服务于该工具的报告流程，不是所有研究问题的最优流程；需要 API、领域适配和资源评估。课程不要求安装、不把 OpenAlex 设为唯一入口，也不直接复制 PRISMA 报告模板。 |
| [Karpathy autoresearch](https://github.com/karpathy/autoresearch) | 主分支；实施时记录 commit | 固定资源预算、明确指标、保留／丢弃、实验日志和有限改动范围，使自动实验可比较、可复查 | 主要面向单 GPU 语言模型训练优化；固定 5 分钟运行及单一 `val_bpb` 不能直接代表其他研究任务。借鉴预算与比较结构，不把其循环泛化为普适科研法。 |

## 教学处理

课程把“组织 AI 参与研究、评价其输出与改动”作为能力目标。L3 以研究问题和下一项信息价值最高的检索动作为主线，按需使用词法、语义、引文网络、数据库／Agent 路由；OpenAlex 是一个可替换数据源。学生保存真实请求、来源、筛选、调整依据和停止理由，并回到原文核验关键主张。L12–13 借鉴有界改进循环，区分任务纠错、可复用工作流改进和改进方法本身的变化，以未参与优化的评价材料检查迁移。

引用与版本信息不稳定时，在正式授课前重新核对仓库发布页、commit、依赖和接口。AI 或 skill 的自述能力、README 演示与本课程环境中的实际运行分别标注，不相互替代。

## 核验记录

- Scientific Agent Skills Releases：[发布页](https://github.com/K-Dense-AI/scientific-agent-skills/releases)；目录：[skills/](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills)。v2.72.0 发布说明列出 skill guides 扩展。
- Paper Search Pro：[仓库](https://github.com/O0000-code/paper-search-pro)；[SKILL.md](https://github.com/O0000-code/paper-search-pro/blob/main/SKILL.md)。当前说明包含 OpenAlex 主源、Semantic Scholar 回退及专题数据库分层；实际调用行为以固定 commit 与课堂运行记录为准。
- autoresearch：[仓库](https://github.com/karpathy/autoresearch)；[program.md](https://github.com/karpathy/autoresearch/blob/master/program.md)。当前 README 说明单 GPU、固定训练预算和 agent 修改范围；课程只借鉴实验治理结构。
