---
版本：v1.1.2
最后更新：2026-08-09
文档类型：技能建设提案与实施记录
状态：已实施
变更记录：
- v1.1.2 (2026-08-09): 聚焦复测通过筛选门控、状态分层、原生查询和统一失败工件四项；修正未确认筛选决定的验证措辞，完成实施
- v1.1.1 (2026-08-09): 根据首轮 forward test 增加筛选建议/人工决定门控、独立检索运行状态、每库原生查询入口和统一失败工件，进入聚焦复测
- v1.1.0 (2026-08-09): 按 lesson 03 handout v1.2.0 校正范围与字段；限定为学术文献；拆分证据角色、核验状态和筛选决定；加入公开源脚本、OpenAI 元数据、验证与后续校准计划
- v1.0.0 (2026-08-09): 建立计划——目标、handout 逐节对照、边界、交付注册、执行顺序、验证清单与风险
---

# `research-question-to-search` skill 实施计划

## 一、目标与成功标准

把公开研究问题或宽泛主题转换为可复盘的学术文献检索，执行公开数据库查询，完成“书目身份 + 一条拟用主张”的入口核验，并产出课程兼容的检索、筛选、审计和候选文献记录。

成功标准：

1. 检索请求、时间、原始响应和规范化结果可追溯；动态数据库重跑允许说明性差异；
2. 预期证据角色、核验状态和筛选决定分别记录，不互相代替；
3. `rejected` 只留审计，网络/API/DOI 暂时失败不会自动变成 `rejected`；
4. 候选表严格使用 handout v1.2.0 的十字段；
5. Keshav DOI 回归、失败路径、三端发现和 skill 校验通过。

## 二、范围

**IN**：论文、预印本、正式学术出版物；问题初稿、词网、数据库实际检索式、公开 API 执行、筛选记录、入口核验、四态建议、十字段候选表和待精读移交项。

**OUT**：

- 代码仓库、数据集、规范、博客、issue 和机构网页的自动核验；这些只登记为外部线索；
- Scopus、Web of Science、CNKI 等订阅源自动化；
- 完整多主张精读、主张综合、综述报告和研究结论；
- 代替用户定稿研究问题、证据角色、核验升级或筛选决定；
- Zotero 导入、集合管理、提交、发布或推送。

## 三、与 lesson 03 的口径映射

| handout v1.2.0 | skill 实现 |
| --- | --- |
| §二 问题初稿与检索式 | 允许先用可修改问题启动；保留每库实际语法和迭代理由 |
| §三 证据角色 | 角色相对于问题/拟用主张判断，默认探索线索；与状态、决定分列 |
| §四·2 入口核验 | 执行身份层 + 一条拟用主张层；多主张与证据结构移交精读 |
| §四·3 四态 | 四态精确拼写；暂时失败为 `pending`，积极确认矛盾才 `rejected` |
| §四·4 Keshav trace | Crossref DOI 回归基线；演示已知题名身份核验，不冒充宽泛发现检索 |
| §五 三类记录 | 检索/筛选记录保留排除理由；审计保留 rejected；候选表只含纳入且非 rejected 条目 |
| §五 十字段 | 编号、题名、作者、年份、稳定来源、对应问题/拟用主张、预期角色、纳入理由、状态、caveat/允许主张 |

与第 4 课边界：本 skill 只保证一条拟用主张可安全进入候选表；多条主张、原文位置、指标、对照、样本、贡献和局限进入 `reading-cards.md` 的精读流程。

## 四、交付物与注册

| 交付物 | 状态 |
| --- | --- |
| `.agents/skills/research-question-to-search/SKILL.md` | 已实现，作为单一事实源 |
| `scripts/search_public_sources.py` | 本轮新增；确定性保存请求、原始响应和规范化 JSONL |
| `agents/openai.yaml` | 本轮新增；由 skill-creator 脚本生成并校验 |
| `.claude/skills/research-question-to-search` | 已注册软链接，需复核目标 |
| `.opencode/agent/research-question-to-search.md` | 已注册薄封装，本轮同步契约 |
| `docs/tooling.md` 与 lesson 03 README | 已登记，本轮同步实现状态 |

脚本支持 Crossref、OpenAlex、arXiv、dblp 和 Semantic Scholar；不输出核验状态或证据角色，避免把确定性抓取与人工判断混在一起。

## 五、实施与验证顺序

1. 完成 handout、L3 三件套、L4 衔接和工件路径校正；
2. 更新 SKILL.md，加入公开源脚本和 OpenAI 元数据，同步 Claude/OpenCode/tooling 注册；
3. 运行语法检查和 skill quick validation；
4. 用 Keshav DOI 重放身份链，核对题名、作者、年份、刊名和 DOI；
5. 运行 0 命中/API 失败用例，确认脚本只记录事实且不产生状态；
6. 运行课程 Markdown 链接与站点构建检查；
7. 交给独立 agent 做 forward test：输入一个新公开主题，检查其是否遵守范围、字段和人工审核点；
8. 根据 forward test 修订，完成后把本文状态改为“已实施”。

首轮 forward test 使用“LLM 辅助代码审查的缺陷发现与误报风险”，发现四项缺陷：人工确认前缺少筛选表示、查询级失败与文献四态混用、通用查询跨库语义不清、失败运行工件不统一。修订后以聚焦复测确认：筛选建议/人工决定双列、独立检索运行状态、`--raw-query`、所有运行统一输出 summary 与 JSONL 均按契约工作。测试记录保存在 `.work/forward-test-search-skill/` 与 `.work/forward-test-search-skill-retest/`。

## 六、风险与处理

| 风险 | 处理 |
| --- | --- |
| 动态 API 命中随时间变化 | 保存精确请求、时间和原始响应；不要求未来结果集完全相同 |
| Semantic Scholar 无 key 限流 | 记录 HTTP 失败并建议 OpenAlex/Crossref；不静默重试 |
| DOI 缺失或解析失败被误拒绝 | 保持 `pending`，尝试出版方、会议官网、arXiv 或其他正式身份源 |
| 把身份核验误当主张精读 | 强制拟用主张层与“待精读移交项”，并在 L4 明确深化边界 |
| 把已核验误当主证据 | 角色必须绑定当前问题；Keshav 回归应为“探索线索 + verified-with-caveat” |
| 非论文来源混入统一状态机 | v1 明确排除自动核验，只登记外部线索 |

## 七、后续校准

- MI trace 已有真实公开记录，但研究问题尚未由用户指认；当前只作为待筛选线索与失败审计，不为其补造角色或允许主张。
- 待真实研究问题确定后，用本 skill 运行新的端到端 trace，再决定是否把 MI 案例织入课堂演示。
- 第 12 课修订时可把本 skill 作为八要素拆解对象；本轮不提前修改第 12 课三件套。

## 关联文件

- `lessons/lesson-03/handout.md` v1.2.0
- `lessons/lesson-03/source-audit-demo.md` v1.1.0
- `lessons/lesson-04/handout.md` v0.4.0
- `references/material-contracts.md` §三
- `docs/tooling.md`
