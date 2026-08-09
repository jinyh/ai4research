# 工具与 MCP 能力契约

> 本文件只记录项目备课所需的外部能力契约，不提交真实凭据或本机配置。MCP 配置保留在用户级环境，不在仓库内维护 `.mcp.json`。

## 能力契约

| 能力 | 建议状态 | 用途 |
| --- | --- | --- |
| Zotero | 已配置 | 检索本地文献库、导出引用、核对全文；涉及本地文献时优先于联网。Claude Code 与 OpenCode 均在用户级配置 zotero-mcp（本地模式）；依赖 Zotero 应用运行 |
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

截至 2026-08-05 的验证状态：Codex 已从项目 `.agents/skills/` 发现该 skill；`opencode agent list` 已列出 `prepare-course-lesson (subagent)`；Claude Code 的单向软链接已解析到同一 `SKILL.md`，实际触发行为仍应在相关备课任务中单独做 smoke test。该 skill 负责内容门、90 分钟教学门、逐页映射门、PPT 制作、三重检查与里程碑归档。当前备课流程见 [lessons/README.md](../lessons/README.md) 的"制作顺序"段。

`research-question-to-search` 检索流程 skill 于 2026-08-09 按同一三端模式注册（建设计划见 [research-question-to-search-skill-plan.md](./research-question-to-search-skill-plan.md)）：

- 单一事实源：`.agents/skills/research-question-to-search/SKILL.md`
- Claude Code：`.claude/skills/research-question-to-search`（软链接）
- OpenCode：`.opencode/agent/research-question-to-search.md`（薄封装，运行时读 SKILL.md）

该 skill 负责"问题→检索式→公开源检索→身份核验→候选文献表行"的受限流程：方法论源为 `lessons/lesson-03/handout.md` §一-§七 与 `references/material-contracts.md` §三；仅公开学术 API，订阅源不自动化，未发表素材不入查询；身份层/主张层双层核验，状态升级与纳入排除决策保留为人工审核点。首个使用场景为课程 2.0 批次 0 的 MI 检索 trace，回归基线为 Keshav 2007 既有 trace。
