> **核验状态（2026-08-12）**：本文件为讲师参考笔记，B/C 级。两个项目均活跃迭代、表述易变；钉死 commit 仅作课堂分析锚点，所有功能宣称授课前必须回源复核。本文件不构成对学生安装或使用的建议；课堂中两者只作**分析对象**，不作结论外推的依据。

# Pi Agent 与 Prime Agent 对照笔记（讲师参考）

## 1. 定位与结论

- **Pi Agent**（pi.dev，`@earendil-works/pi-coding-agent`）：极简终端 coding agent 底座，默认只给模型 4 个工具（read/write/edit/bash），刻意不内置权限弹窗、plan mode、sub-agents、MCP，复杂能力交给 extensions/skills/prompt templates/packages。
- **Prime Agent**（PrimeIntellect，MIT 许可）：约 2026-08-06 发布的自我改进研究型 Agent，面向长任务。**官方 README 明确声明构建于 pi 之上**（致谢 earendil-works/pi）——二者同一技术谱系：pi 是最小底座，Prime Agent 是在其上叠加的研究型长任务层。
- **课程结论**（对应 `course/reference-analysis.md` 采纳判断）：
  - pi 引入为第 12 课课堂拆解案例与讲师参考，作八要素框架的"最小对照组"；
  - Prime Agent 限制性引入为第 11 课课堂案例簇（钉 commit + 两篇预印本）与延伸阅读，讲师演示仅作备选；
  - **均不进入学生必装清单**。OpenCode 仍为唯一课堂统一基线（syllabus 口径）。

## 2. 谱系关系

```text
pi（极简 harness 底座，earendil-works/pi）
 └── Prime Agent（研究型长任务层，PrimeIntellect-ai/prime-agent，README 自述 built on top of pi）
旁置对照：OpenCode（完整工作台，课程统一基线，不随本笔记改变）
```

教学价值：三点一线演示"同一组八要素设计决定的不同取舍"——pi 把 harness 压到最小、把决定留给使用者；OpenCode 把权限、子 Agent、MCP、任务列表做成显性内置；Prime Agent 把 harness 本身变成可持久化、可被证据驱动精化的状态。这正对应课程"不绑定工具、教设计决定"的理念。

## 3. 三方对照表（按 harness 设计维度）

| 维度 | OpenCode（基线） | pi（commit `9795d602`） | Prime Agent（commit `965941c7`） |
| --- | --- | --- | --- |
| 核心定位 | 功能完整的开源终端 Agent 工作台 | 可拼装的极简 Agent 底座 | 自我改进的研究型长任务 Agent |
| 默认工具 | 内置工具较多（文件、命令、搜索、补丁、任务列表、网页、LSP 等） | 4 个：read/write/edit/bash；grep/find/ls 等只读工具需配置启用 | 一切经程序化：持久 IPython REPL 是内置模型工具，文件/shell/子 Agent 均通过代码调用 |
| 权限控制 | 细粒度权限（allow/ask/deny，按工具/命令/路径/agent） | 刻意不内置 permission popups，依赖 Git/容器/tmux/扩展控制风险 | 官方自述 worker/kernel 隔离**不是安全沙箱**，以用户权限执行模型生成的 Python |
| 计划与子 Agent | 内置 plan/build agent、todo、subagents | 刻意不内置 plan mode、to-dos、sub-agents | 内置程序化子 Agent（`rlm(...)` 生成子 Agent 并取回结果）；Agent 间可直接通信 |
| Skill 机制 | MCP servers、Agent Skills、自定义工具 | extensions、skills、prompt templates、packages | skills 为可导入 Python 包；内置 skill creator |
| 状态与 Memory | 会话 + 项目规则文件（AGENTS.md 等） | 启动读取 AGENTS.md/CLAUDE.md 与全局说明 | **Continual Harness**：supplemental prompts/memories/skill 描述/子 Agent 规格为持久状态，`/refine` 做证据支撑的小步更新，快照可回滚；不改不可变基础 system prompt |
| 执行循环 | 工具循环 + 计划模式 | 最小 agent loop | **RLM**：prompt-as-a-variable，持久 REPL 中程序化递归调用；`/autonomous` 有 turn/token/time 预算与质量门 |
| 长任务能力 | — | — | daemon 后台会话、detach/reattach、heartbeat、schedule、持久 goal |
| 安装方式 | npm/安装脚本，支持多 Provider 含国内供应商 | npm 包（@earendil-works/pi-coding-agent） | `curl -fsSL .../install.sh \| sh`；有 SHA-256 校验、无签名校验；可能触发 sudo 装 Node |
| 模型接入 | 多 Provider + OpenAI-compatible | 订阅登录 + API Key 多 Provider | 订阅登录（ChatGPT/Claude/Copilot）+ API Key（含 DeepSeek、MiniMax、Kimi 等）+ OpenAI-compatible 自定义端点（models.json）；Prime Inference 为可选自家服务 |
| 课堂角色 | 统一基线（不变） | 第 12 课源码级拆解案例（最小对照组） | 第 11 课案例簇 + 延伸阅读；讲师演示备选 |

## 4. Prime Agent 核心机制核验记录（2026-08-12）

来源以官方 README 与官方文档为准（A 级来源身份；功能描述属易变信息，授课前复核）。

| 机制 | 官方表述要点 | 来源 | 证据级别与限制 |
| --- | --- | --- | --- |
| RLM（Recursive Language Model） | 把 context 作为变量（prompt-as-a-variable），把工具与递归子 Agent 作为持久 REPL 中的函数调用 | README；上游论文 arXiv:2512.24601（Zhang, Kraska & Khattab，v1 2025-12-31） | 论文为预印本，未经同行评议；课程只引其设计思想作分析对象 |
| Continual Harness | `/refine` 回顾轨迹并对 supplemental harness 状态做小的、证据支撑的更新；不改不可变基础 system prompt；快照支持回滚 | README；论文 arXiv:2605.09998（Karten et al.，v1 2026-05-11） | 论文为预印本；实验对象（Pokémon/Gemini Plays Pokémon、ARC-AGI-3 公开集）与科研场景差异大，不外推到科研自动化能力 |
| Skills | skills 是可导入 Python 包；内置 skill creator 把重复工作流转为项目/个人 skill | README | 与第 12 课"Skill 是封装的任务说明+资源+执行方法"口径可对照 |
| 有界自主 | `/autonomous` 在 turn/token/time 预算内继续，可配用户定义质量门；官方自述"通过门只证明该门所验证的内容，到达上限不等于任务成功" | README | "通过门 ≠ 任务成功"是第 11 课停止条件教学的原文引证素材 |
| 长任务 | daemon 后台会话、detach/reattach、`/goal` 持久目标、heartbeat/schedule | README | 讲师演示备选功能，不进学生必做环节 |

## 5. 安全相关官方表述（摘录，课堂反面+正面两用）

README 警告原文要点（2026-08-12 核验）：

> Prime Agent executes model-generated Python and project commands with your user permissions. Its worker and kernel processes improve lifecycle isolation and recovery; they are **not** a security sandbox. Review changes and use trusted repositories, instructions, skills, and extensions only.

install.sh 审阅要点（2026-08-12 只读审阅，未执行）：下载来自可配置 base URL（默认官方发布端点）；对安装包与 Node.js 独立包做 SHA-256 校验，**无 GPG/签名校验**；可能经 apt/apk/Homebrew 安装 Node 并触发 sudo；可能把 PATH 写入 shell profile；下载源环境变量可被覆盖。

课堂用法：

- **反面**：`curl | sh` + 用户权限执行模型生成代码，直接对照第 2 课最小权限与第 10 课权限分层——课堂明确：个人确想试用必须使用容器或一次性隔离环境，并写入权限矩阵与 AI 使用记录。
- **正面**：官方主动披露"not a security sandbox"是"系统自我披露质量"的优质样例；`/autonomous` 的"passed gate 只证明该门"可作停止条件与质量门教学的原文引证。

## 6. 八要素教学映射

| 课程八要素 | pi 的观察点 | Prime Agent 的观察点 |
| --- | --- | --- |
| 任务契约 | 无内置计划模式，任务边界完全由使用者在 AGENTS.md/扩展中写明 | `/goal` 持久目标 + 任务在 REPL 中以代码表达 |
| Context | 默认工具极少，Context 由使用者显式组装 | prompt-as-a-variable：Context 是可编程操作的对象 |
| Memory / 状态 | 不内置持久记忆 | Continual Harness 持久状态（prompts/memories/skill 描述/subagent 规格） |
| 工具与权限 | 4 默认工具；权限外置给 Git/容器/扩展 | 以用户权限执行；官方声明非沙箱 |
| 执行循环 | 最小 agent loop | RLM 程序化递归 + `/autonomous` 预算与质量门 |
| 工件与追踪 | 依赖外部（Git 等） | 精炼历史、快照、会话日志 |
| Evals 与人工审核 | 由使用者自建 | 质量门可配；官方明示门不等于成功 |
| 失败恢复 | 由使用者自建 | 快照回滚（官方自述）vs 第三方批评（见证据冲突） |

## 7. 证据分级与不外推清单

- 级别：官方 README/文档与仓库 = A（来源身份可靠；功能描述易变，授课前复核）；两篇 arXiv = 预印本（未经同行评议，只作设计思想分析对象）；MarkTechPost 等报道 = B；Medium 批评文 = C（采用前回源）。
- 厂商基准与能力宣称（含 ARC-AGI-3 相关数字）按课程既有口径：**作为报告观点引用，不作已核验事实**，不进结论句；不记录 Star 数与"首个/超越"类宣传表述。
- 课堂表述不得外推为：
  - "Prime Agent 已能自主完成科研"；
  - "自我改进 harness 必然改善研究质量"（预印本实验场景为游戏/公开基准，非科研）；
  - "极简 harness 优于完整 harness"（pi 与 OpenCode 是不同取舍，不是高下）；
  - "官方快照回滚等于完整可审计性"（存在第三方批评，见下）。

## 8. 证据冲突记录

- **冲突**：官方自述 `/refine` 快照支持回滚、不改基础 system prompt；第三方批评文（Medium，C 级）指其日志只记录"发生了精化"而不记录"编辑波及范围"。
- **取舍**：两者都未经课程独立核验。课堂使用时按"冲突证据必须呈现冲突和取舍理由"处理——作为第 13 课"自我改进系统的可审计性"失败复盘素材，要求学生分别回源后再判断；采用任一表述前必须先回源核验。

## 9. 钉死版本与入口

| 对象 | 钉死版本 | 入口 |
| --- | --- | --- |
| prime-agent | commit `965941c750ff816cc4d68d18a5fcea5e0b4c120b`（2026-08-12 核验） | <https://github.com/PrimeIntellect-ai/prime-agent/tree/965941c750ff816cc4d68d18a5fcea5e0b4c120b> |
| pi | commit `9795d602306ef68a97585909e8e79f92a389057b`（2026-08-12 经 GitHub API 旧路径 badlogic/pi-mono 核验；项目已于 2026-05-07 迁至 earendil-works/pi，GitHub 对改名仓库自动重定向，授课前建议用新仓库路径复核该 SHA） | <https://github.com/earendil-works/pi/tree/9795d602306ef68a97585909e8e79f92a389057b> |
| Continual Harness 论文 | arXiv:2605.09998 v1（2026-05-11，预印本） | <https://arxiv.org/abs/2605.09998>；参考实现 <https://github.com/sethkarten/continual-harness> |
| RLM 论文 | arXiv:2512.24601 v1（2025-12-31，预印本） | <https://arxiv.org/abs/2512.24601>；参考实现 <https://github.com/alexzhang13/rlm> |
| pi 本地源码快照 | handsonlab 仓库内 `raw/框架/pi/`（2026-05-26 快照，pi-monorepo 结构，含 agent/ai/coding-agent/tui 四包） | 仅讲师本地参考；graduate 课程材料不建跨仓库相对链接 |

## 10. 待核验清单（授课前）

1. 用 `earendil-works/pi` 新仓库路径复核 pi 钉死 SHA（当前核验经旧路径重定向）；
2. PrimeIntellect 服务依赖：install.sh 取自 app.primeintellect.ai，`/login` 订阅路径是否强制经过 PrimeIntellect 端点未逐包核验；
3. 国内网络可达性与课堂网络环境（安装源、arXiv、GitHub）；
4. 两篇 arXiv 的后续版本与同行评议状态；
5. Prime Agent 对国内供应商的实际可用性：providers 文档列出 DeepSeek 内置、MiniMax/Kimi 条目与 OpenAI-compatible 自定义端点（阿里百炼未被点名，理论上可走自定义 Provider），未实测；
6. Medium 批评文的具体技术指控（采用前回源）；
7. arXiv PDF 课堂分发的许可边界（当前只发链接，不复制全文）。

## 11. 回退预案

- 若仓库结构剧变或项目停更：保留 arXiv 引用与钉死 commit 快照表述，删除"当前状态"类语句；
- 若国内可用性核验不过：讲师演示降级为纯文档/源码拆解（本笔记 §3 对照表 + §6 映射表可独立支撑）；
- 若第三方批评核验后与官方自述冲突扩大：按 §8 呈现冲突，不单方采信。

## 12. 课堂使用建议

- **第 11 课**：Prime Agent 案例簇只作分析对象——对照"固定指标/预算/停止条件/回退"四约束，分析 `/autonomous` 预算与质量门设计；引用"passed gate 只证明该门"原文。
- **第 12 课**：pi 作最小 harness 拆解案例——4 默认工具、权限外置、无内置计划/子 Agent，逐条对照八要素"拆解观察点"；与 OpenCode 的显性 harness 构成同谱系对照。
- **第 13 课（备选）**：证据冲突（§8）作自我改进系统可审计性的失败复盘素材。
- **演示隔离要求**：任何讲师实机演示必须在容器或一次性环境中进行，不在备课机直接安装；演示记录写入 AI 使用记录与权限矩阵。
- MBA 工作坊版对比（受众不同、结论限于工作坊）见 handsonlab 仓库 `materials/tool-comparison-opencode-pi.md`，本笔记为 graduate 独立重写，不互为链接依据。
