# 第 3 课共同诊断｜检索漏检与误纳诊断

## 先独立判断

**问题：查询的改动解决了哪种漏检，又引入什么误纳？**

输入：L2 的来源范围；独立种子 Keshav 2007。先记录判断和依据，再与同伴比较；课堂校准后可修订并写明改变原因。答案有分歧时回到具体记录。已有示例可作方法参考，不替代本人的初始判断。

## 原始材料与待比较选项

本地微型索引是教学构造的检索环境；S1/S2 的书目身份来自公开原文，S3–S5 是明显标记的构造条目。下表是已保存的固定查询结果，不是学术库命中数。

| ID | title 字段 | keywords 字段 |
| --- | --- | --- |
| S1 | How to Read a Paper | three-pass; research reading |
| S2 | Guidelines for Performing Systematic Literature Reviews in Software Engineering | search strategy; study selection |
| S3 | Teaching record: structured reading cards | paper reading; condition retention |
| S4 | Teaching record: reading memory cards | hardware; memory |
| S5 | Teaching record: paper card recycling | manufacturing; recycling |

查询均只搜 title，按大小写不敏感的子串匹配；括号为概念组。

- Q1：`paper AND reading AND card`，保存结果：S5。
- Q2：`(paper OR reading) AND (card OR review)`，保存结果：S2、S3、S4、S5。
- 独立种子：教师从上一课方法书目提供 S1；它不是从 Q1/Q2 命中里反向挑出的“已知相关项”。

原文入口：[S1 核验记录](./source-audit-demo.md)；[S2 机构索引](https://ebse.webspace.durham.ac.uk/ebse-bibliography/guidelines-for-performing-systematic-literature-reviews-in-software-engineering/)。S3–S5 不能进入真实文献表。

**待决定：**比较扩大同义词、改变检索字段、增加独立查询三种动作；写一条修订查询，再执行并保存结果。

把“初始判断—证据位置—仍缺什么—核验后决定”写在现有笔记中。允许回答“仍不能判断”，同时指出下一项能改变判断的证据。

本地执行入口：[Python 检索小包](./assets/search-diagnosis/README.md)。真实候选可从[公开起始池](../../course/source-starter-pool.md)独立筛选。

## 迁移到本人项目

先修复保存结果，再在本地索引或可用学术库执行自己的修订查询，记录字段/语义/结果。对两条真实线索做身份与一条拟用主张审计；两条均核验通过也合格。同题允许独立定位与判断。

**验证：**同伴按查询逐字重放一个命中和一个漏检；候选条目有原文位置与纳入理由。离线用 S1/S2 存档审计，网络故障条目保持 pending。

**保存位置与达标证据：**notes/literature-search.md：一条可重放查询、两条据实审计、一条候选的角色与决定。

**下课去向：**L4 精读其中一条关键主张；候选起始池可继续扩展。

## 完成标准

| 尺度 | 判断依据 |
| --- | --- |
| 需支持 | 完成操作，但理由、证据定位或验证仍有缺口。 |
| 达标 | 独立决定，证据可定位，完成相称验证，并更新本人项目。 |
| 优秀 | 识别替代解释或有效性威胁，以额外检查改变或加强判断。 |

课堂尺度对应课程的待改、达标、卓越；不新增每周成绩或提交。优秀依判断质量，不要求更多课外时长。

断网时保留同样的判断要求，使用包内文本、存档或本地工件。工程课纸面诊断仅作备用练习，最终仍须补本人实际执行、实质修改和对照评价。提前完成者可寻找一个使自己决定改变的反例；不增加课后任务。
