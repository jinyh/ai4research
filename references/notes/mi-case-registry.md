---
版本：v0.2.0
最后更新：2026-08-10
文档类型：MI 贯穿案例素材登记（元数据）
状态：L3 已用素材已登记；L4-L16 素材仍待博士生提供
变更记录：
- v0.2.0 (2026-08-10): 填充 L3 实际使用的 5 条素材（Keshav 2007 原文截图演示 + 幻觉审计四条被冒名论文的正确答案）；Zotero 便利层更新：正位改为 GraduateCourse 群组库（groupID 6634461）集合 I2GKJGNP（38 条，tag mi-trace，Extra trace-id），个人库原集合 V7XM4JF2 已移入回收站；登记素材 ID 与 trace 编号的映射说明
- v0.1.1 (2026-08-09): 登记 Zotero 检索便利层约定（课程案例 collection 已建，key V7XM4JF2，挂于 Teaching 下；tag 对应素材 ID）
- v0.1.0 (2026-08-08): 建立骨架——素材 ID 约定、登记表表头、L1-L16 身份映射表、填充流程；登记表内容留空待素材到位
---

# MI 贯穿案例素材登记（mi-case-registry）

本文件是课程 2.0 的 MI（Mechanistic Interpretability）贯穿案例素材元数据登记，**Git 跟踪，只存元数据**（DOI/arXiv/仓库链接、许可、脱敏状态、教学可用性），不存任何论文原文、代码或未发表内容。权威计划见 [docs/course-2.0-plan.md](../../docs/course-2.0-plan.md) §MI 逐课身份与§素材收集前置步骤。

**身份**：MI 是一位博士生的真实研究课题，已获教学授权；教师演示用真实脊椎，学生练习仍用虚构贯穿案例（每课使用处须有案例边界框声明）。

## 存放分区

| 内容 | 位置 | Git |
| --- | --- | --- |
| 公开原件（论文 PDF、仓库克隆） | `references/library/mi-case/` | 不跟踪 |
| 未发表原件（负结果、实验记录） | `.local/mi-case-unpublished/` | 绝不进跟踪路径 |
| 脱敏教学图件 | `lessons/*/assets/` | 跟踪 |
| 授权表述存档 | `.local/mi-case/authorization.md` | 不跟踪 |

处理未发表素材的任何环节（脱敏、制图、润色）不得送入外部 LLM/在线服务；脱敏由教师人工执行、用户复核后入库。

Zotero 检索便利层（非权威源）：教学素材集中存放于 GraduateCourse 群组库（groupID `6634461`）collection「Mechanistic Interpretability」（key `I2GKJGNP`，38 条，tag `mi-trace`，Extra 登记 `trace-id`），与个人 MI 阅读文献隔离；个人库原集合 `V7XM4JF2` 已于 2026-08-10 经确认移入回收站。条目对应关系：Zotero `trace-id`（MI-C01–C36 / MI-W01–W02）与 [mi-search-trace-demo.md](../../lessons/lesson-03/mi-search-trace-demo.md) 编号一致（映射存档 `.work/mi-search/stage5/group-keys.json`）；本文件素材 ID（MI-03-XX）按课次登记教学材料实际引用的素材，与 trace 编号不同维度，需要时在登记表注明对应 trace-id。附件策略为 linked_url 直链（Zotero 云配额耗尽，群组文件不经 WebDAV，见 trace §10.7）。许可、脱敏状态与教学可用性以本文件登记表为唯一权威，不在 Zotero 笔记中维护，避免两套口径漂移。

## 素材 ID 约定

格式：`MI-<课次>-<两位序号>`，如 `MI-03-01`。类型码：

| 码 | 类型 |
| --- | --- |
| PUB | 已发表论文 |
| PRE | 预印本 |
| REPO | 公开代码/数据/模型仓库（钉死 commit） |
| UNPUB | 未发表实验结果（含负结果；仅 PPT notes 与教案） |
| FIG | 脱敏教学图件（进 `lessons/*/assets/`） |

## 登记表

| 素材 ID | 课次身份 | 类型 | 来源（DOI/arXiv/仓库@commit） | 许可 | 脱敏状态 | 教学可用性 |
| --- | --- | --- | --- | --- | --- | --- |
| MI-03-01 | L3 演示 P13-P15：真实 Crossref—DOI—原文核对对象 | PUB | DOI 10.1145/1273445.1273458（Keshav, *How to Read a Paper*, ACM SIGCOMM CCR 37(3), 2007） | ACM；第 1 页截图仅作核验演示工件，不复用图中内容 | 公开，无需脱敏 | 教学可用（真实原文截图演示；对应 source-audit-demo.md） |
| MI-03-02 | L3 演示 P16：幻觉审计"Attribution Patching"正确答案 | PRE | arXiv:2310.10348（Syed et al.；trace 编号 MI-C10） | 仅元数据与 ID 演示，不复现图文 | 公开 | 教学可用（对应 trace §6 与 slides P16） |
| MI-03-03 | L3 演示 P16：幻觉审计"Tuned Lens"正确答案 | PRE | arXiv:2303.08112（Belrose et al.；trace 编号 MI-C06） | 仅元数据与 ID 演示 | 公开 | 教学可用 |
| MI-03-04 | L3 演示 P16：幻觉审计"Emergent Linear Representations"正确答案 | PRE | arXiv:2309.00941（Nanda, Lee, Wattenberg；trace 编号 MI-C07） | 仅元数据与 ID 演示 | 公开 | 教学可用 |
| MI-03-05 | L3 演示 P16：幻觉审计"Gemma Scope"正确答案 | PRE | arXiv:2408.05147（Lieberum et al.；trace 编号 MI-C03） | 仅元数据与 ID 演示 | 公开 | 教学可用 |

说明：P16 屏显的"错误记忆 ID"（2308.10939 / 2203.13787 / 2309.10655 / 2407.14400）指向不相关的真实论文，屏显只给 ID 与宽泛学科描述、不暴露被冒名论文身份，故不单独登记。trace 的 36 条完整锚点池登记在 trace 本身与 `.work/mi-search/stage5/group-keys.json`，进入后续课次教学材料时再逐条登记本表。

填充规则：每条素材登记许可与教学可用性后才能在课次材料中使用；UNPUB 条目的"教学可用性"须经用户复核脱敏件后标"教学可用（仅 PPT）"；REPO 必须钉死 commit（AutoResearch 先例）。

## L1-L16 课次身份映射

| 课 | 身份 | 课 | 身份 |
| --- | --- | --- | --- |
| L1 | 屏显实例（一张已发表图一句话带过） | L9 | 探针/消融 baseline、实验规格七字段示范（公开+脱敏） |
| L2 | 权限/风险卡对象（"未发表结果不发外部模型"元契合） | L10 | 探针训练小任务的受限 Agent 契约（公开代码） |
| L3 | 检索 trace 对象（试点），幻觉审计素材 | L11 | 消融批量队列改写受限循环 |
| L4 | 精读卡对象（L3 选定论文，与 Keshav 卡并列） | L12 | 探针 pipeline 八维拆解 |
| L5 | 证据地图对象（探针/因果干预/SAE 角色；负面证据首个实例） | L13 | 失败核心课：探针假阳性、控制集泄漏、假设被证伪（公开+脱敏） |
| L6 | 问题定义示范（门自查仍用虚构案例） | L14 | 负结果入文范文（结果段+讨论段） |
| L7 | 机制假设元契合（全课程契合度最高） | L15 | 评审校准样例（教师改写，标注教学样例） |
| L8 | 3 分钟陈述示范对象（Bouthillier 先例） | L16 | 负结果陈述示范（可选） |

## 填充流程

1. 用户提供素材清单：博士生论文/预印本（DOI/arXiv ID）+ 公开仓库/模型链接 + 未发表结果可用范围；可选：选题过程复盘与分层归因实例（供 G3/G4）。
2. 公开素材入 `references/library/mi-case/`，登记 PUB/PRE/REPO 条目并核验许可。
3. 未发表素材入 `.local/mi-case-unpublished/`；教师人工脱敏 → 用户复核 → 脱敏件入 `lessons/*/assets/`，登记 UNPUB/FIG 条目。
4. 各课改版时按身份映射引用素材 ID；课次 README 与登记双向核对一致。
