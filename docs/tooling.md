# 工具与 MCP 能力契约

> 本文件只记录项目备课所需的外部能力契约，不提交真实凭据或本机配置。MCP 配置保留在用户级环境，不在仓库内维护 `.mcp.json`。

## 能力契约

| 能力 | 建议状态 | 用途 |
| --- | --- | --- |
| Zotero | 可选、推荐 | 检索本地文献库、导出引用、核对全文；涉及本地文献时优先于联网。具体客户端连接属于用户级环境，不作为仓库事实 |
| GitHub | 按需 | 只有需要 issue、PR 或远端仓库操作时启用；连接失败的实例应及时修复或禁用 |
| Context7 | 非项目依赖 | 核对易变的软件文档；不参与课程事实来源管理 |
| PPT/Office 本地工具 | 必需 | 渲染、重新打开和视觉检查；不需要 MCP |

## 凭据安全

- 不在命令参数中放置 API key；迁移到环境注入、Keychain 或客户端支持的凭据存储。
- 轮换已经通过命令参数暴露的现有凭据。
- 不把用户级 MCP 配置、插件缓存或绝对路径复制进本仓库。
- 若以后为课堂演示提供 MCP 配置，应放在独立示例目录，只提交使用环境变量占位符的示例，不提交真实值。

## 项目 skill

`prepare-course-lesson` 备课门控 skill 已按三端入口注册：
- Claude Code：`.claude/skills/prepare-course-lesson`（软链接到 `.agents/skills/prepare-course-lesson/`）
- OpenCode：`.opencode/agent/prepare-course-lesson.md`（薄封装，运行时读 SKILL.md）
- 单一事实源：`.agents/skills/prepare-course-lesson/SKILL.md`

该 skill 负责内容门、90 分钟教学门、逐页映射门、PPT 制作、三重检查与里程碑归档。发现与运行状态应在实际使用的客户端中做 smoke test，不在本文件固化某次个人环境结果。当前备课流程见 [lessons/README.md](../lessons/README.md) 的“制作顺序”段。

`research-question-to-search` 检索流程 skill 按同一三端模式注册；历史建设与 forward test 记录已移入[被替代文档归档](../archive/superseded-docs/research-question-to-search-skill-plan-v1.1.2.md)：

- 单一事实源：`.agents/skills/research-question-to-search/SKILL.md`
- Claude Code：`.claude/skills/research-question-to-search`（软链接）
- OpenCode：`.opencode/agent/research-question-to-search.md`（薄封装，运行时读 SKILL.md）
- Codex 元数据：`.agents/skills/research-question-to-search/agents/openai.yaml`
- 公开源执行脚本：`.agents/skills/research-question-to-search/scripts/search_public_sources.py`

该 skill 负责“问题初稿→每库实际检索式→公开源检索→入口核验→筛选/审计/候选表”的受限流程。v1 只自动处理论文、预印本和正式学术出版物；其他来源仅登记为外部线索。它分开记录查询运行状态、预期证据角色、四态核验状态、筛选建议和人工决定，状态升级与最终筛选保留为人工审核点。当前实现包含确定性公开源脚本与 Codex 元数据；Keshav 回归和独立 forward test 聚焦复测均已通过。
