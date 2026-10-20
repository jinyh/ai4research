# 全课备课 Harness

版本：v1.1.0；更新：2026-10-20。首轮使用 L4，其他课在修订时逐课接入。

本入口把现有备课检查与当前材料绑定。质量要求仍以[审校清单](../lessons/review-checklist.md)、[材料契约](../references/material-contracts.md)、[PPT 质量门](../course/ppt-quality-gates.md)及[设计准则](../lessons/ppt-design-criteria.md)为准。脚本检查结构与证据覆盖，内容、事实和视觉质量由实际审阅产生。教师确认、PowerPoint、投影和学生试做分别记录。

## 执行与阶段

```sh
python3 scripts/check_lesson.py --lesson 04 --stage source \
  --evidence .work/harness/lesson-04/<run>/evidence.json \
  --output .work/harness/lesson-04/<run>/source-check
```

呈现阶段将 `--stage` 改为 `presentation`，清单的 stage 同步修改。清单内所有路径相对仓库根目录；绝对路径仅接受仓库内部。每轮使用新报告目录，保留旧报告；脚本只向 `.work/` 写报告，不修改源稿。

- `source`：读取讲义、教案、母稿和学生任务作为上下文；检查内部链接、母稿页序与映射、现行流程总时长和本轮语义评审。只改讲义时 scope 可为 `["handout"]`，所需评审为 handout、alignment，不要求 PPT。
- `presentation`：另核对当前 PPTX 屏显、备注、全页渲染、联系表及技术／视觉评审。对整套候选检查，不以样页通过替代整稿；代表页可用于制作决策，但不单独取得本阶段通过。
- 输出 `report.md`、`result.json`。退出码 0=当前阶段通过，1=存在阻断，2=材料或评审证据不足，3=执行故障。阶段通过不等于正式交付。全课背景检查单列，不自动阻断本课。
- 生产者可据报告修复并复验。本入口不调用模型、不自动生成通过评审、不自动循环生产。

## 证据清单

JSON 的 `schema_version` 为 `graduate.lesson-evidence.v1`；`lesson` 是两位课次字符串；`stage` 与调用相同。`scope` 是本轮涉及的材料角色列表。`files` 的必需角色为 handout、teaching_plan、slides、task，分别指向本课的 handout.md、teaching-plan.md、slides.md、judgment-task.md；teacher、keystone 是可选上下文，纳入修改范围时必须登记。presentation 阶段增加 pptx，允许指向 `.work/` 中的预览。

每个文件引用为 `{"path":"仓库相对路径","sha256":"实际完整SHA-256"}`。哈希可用 Python `hashlib.sha256(Path(path).read_bytes()).hexdigest()` 获取。不得用占位值运行后宣称通过。

`rules` 将以下路径作为键，值仍为文件引用：

- `lessons/review-checklist.md`
- `references/material-contracts.md`
- `course/ppt-quality-gates.md`
- `lessons/ppt-design-criteria.md`
- `course/syllabus.md`
- `course/micro-project.md`

`sources` 可登记本轮依赖的阅读输入、代码、参数、原图及来源存档等文件引用，纳入版本绑定。

`reviews` 是评审 JSON 文件引用的列表。初次诊断可为空；结果会列出待评审项。`review_delta` 包含 keep、repeat、change 三个字符串数组，可为空，分别写保留项、重复项、需改变的表达。

presentation 增加：

- `renders`：按实际页序排列的完整数组。每条含文件引用、`page`（从 1 起）、`pptx_sha256`、实际 `renderer` 与 `renderer_version`。
- `contact_sheet`：文件引用及 `pptx_sha256`。

文件存在与哈希匹配只证明绑定有效，图像是否对应实际 PPT、是否可读仍须看实际渲染。模型或人工观察都不能凭文件名替代图像检查。

## 逐项评审

评审 JSON 包含 `reviewer`、`date`、`bindings`、`checks`。reviewer 如实填写 Agent 自检或具体人工身份，不能写作独立评审或教师通过。bindings 记录被评清单中所有文件角色及其 SHA-256，加上 `rule:<规则路径>` 和 `source:<来源数组索引>`；呈现阶段再加 `render:<页码>` 和 `contact_sheet`。与当前有效证据完全一致才接受评审。

checks 每项必须包含 group、criterion、location、observation、impact、status、blocking、action、recheck。location 定位实际章节、页码或对象；observation 写看到了什么；impact 解释对学生理解或操作的影响；action 写修改动作，无需修改则明写；recheck 写复验观察或待完成事项。

| group | criterion | 判断对象 |
|---|---|---|
| handout | readability / evidence | 独立阅读、概念解释；主张、证据与限定 |
| teaching | execution / independent_judgment | 教学执行、时间和备用；先独立判断、核验与回写 |
| alignment | research_thread / handoff | 同一研究主线与材料一致；上游输入和下游输出 |
| visual | objects / readability / sequence | 研究对象的解释作用；全尺寸阅读；整稿递进与揭示顺序 |
| technical | file / typography | 文件、备注与可编辑性；实际字号与布局检查 |

scope 包含 handout 时要求 handout；包含 teaching_plan、slides、task 或 teacher 时要求 teaching；alignment 始终要求；presentation 另要求 visual 和 technical。每个所需 criterion 恰好一项。visual 与 technical 每项必须给 `pages`，覆盖完整连续页码；观察可引用逐页日志，但应写明发现和处理。

status 为 pass、partial、fail、unverified 或 not_applicable；blocking 为布尔值。fail 总是阻断，unverified 总是缺证据；partial 必须写影响及是否阻断，未阻断的 partial 仍使总体状态为证据不足。not_applicable 需在观察中解释理由，不计为通过项。任何硬失败都不能被其他通过项抵消。

含“分钟”的屏显仅在明确课堂计时时自动阻断，其余列为语义待核。评审可在 `minute_dispositions` 中逐条记录与报告完全相同的 observation、kind（source_content 或 classroom_timing）、reason；原文实验耗时等可确认为 source_content。该接口不能撤销其他检查失败。

## 当前状态与人工记录

`confirmations` 可登记 teacher、powerpoint、projection、student_trial；缺失默认为 unverified。verified 必须附实际 evidence 文件引用、target_sha256，教师与试做绑定讲义，PowerPoint 与投影绑定 PPTX。确认须有真实人员／操作依据，Agent 不代签。阶段通过仍显示这些独立状态。

课次 README 顶部只维护当前轮入口和摘要；教师决定仍进[教师复核台账](../lessons/teacher-review-ledger.md)。每项新评审绑定新版本；保留旧问题、旧报告及复验差量。若生产范围变化，先更新本轮范围，不覆盖历史记录。

## 验证

```sh
python3 -m unittest discover -s scripts/tests -v
python3 scripts/check_course_consistency.py
python3 scripts/check_links.py
python3 scripts/check_slide_alignment.py lessons/lesson-03/slides.md lessons/lesson-03/slides.pptx
```

脚本结构检查不证明课件的学术质量和课堂效果。源稿自检完成、教师复核未完成时可生成明确标注的预览，按现行材料契约登记；正式交付仍遵循原有门控和发布边界。

## v1.1：个人项目迁移、独立评审与候选比较（2026-10-20）

MI 仅为教师 Demo，学生个人项目方向不限。新清单设置 `review_profile: personal-projects-v1`，要求 pedagogy.challenge（研究挑战性）与 pedagogy.transfer（跨项目迁移）逐项观察。旧 v1 清单保持兼容；规则版本变化仍使旧证据失效。

### 独立评审入口

```sh
python3 scripts/review_lesson.py --evidence .work/harness/lesson-04/run/source-evidence.json --output .work/harness/lesson-04/run/independent
```

入口使用已登录 Codex CLI，默认 gpt-6.1-sol/high，独立 ephemeral、read-only 会话；关闭工具执行、网络检索、应用与多代理能力。借鉴 AItalk `evaluate_course.py` 2026-10-20 的调用与留痕规则，代码独立维护，不依赖另一仓库。技术检查器不调用模型。

每项引用登记证据标签、一基行号及该行原文子串；图像使用实际 render 标签、空引文、line=0，观察中写具体对象。程序核对引用存在、位置、版本和必评项，不能保证解释正确。独立会话不等于独立模型或教师确认。记录请求模型与实际取得的用量；未知实际模型、账单成本保持 null。

源稿一次完整内容评审；呈现阶段每组最多四张全页图，另用联系表检查整稿。内容批次保留全部材料及研究文本来源；重复母稿的直接PPT技术抽取交技术／视觉批次，超过200000字符停止整理，不静默截断。视觉批次保留课程材料、规则和标注 `review_role: technical` 的直接技术证据；完整论文与代码不反复发送，所有来源仍参与版本绑定。图像行即使判为待核，也须引用实际附图并写明具体观察，不能仅引用母稿。每次最多600秒，仅临时故障或超时可重试一次；无效JSON、引文、认证或漏项不重试取悦评分。逐批有效结果落盘，后续失败保持 error；中断记录已用时间及未知token，不把部分完成放行。

内容批次先执行；互不依赖的图像批次最多三个并行，按页序校验并登记，不增加批次数。任一批次失败即取消尚未开始的批次，已开始的调用仍保留日志与实际用量；不能因结果未进入汇总而省略其成本。

评审开始与结束同时核对评审器、阶段检查器及屏显映射检查器的实现指纹；中途改变实现时，该轮不能作为完整有效结论。生成 review.json 和更新后的 evidence.json，再运行阶段检查。调用失败保留 error.json、日志和有效 progress.json。教师、助教、PowerPoint和投影仍使用独立确认字段。

### 候选隔离与采用

`check_lesson.py` 和 `review_lesson.py` 可使用 `--candidate-root .work/<实验>/<候选>`；目录内保持 lessons/lesson-NN 的材料角色结构。清单路径仍相对宿主仓库，规则引用固定在宿主权威源，候选源文件不能通过软链接冒充。准备相对链接依赖时复制所需公开材料；候选目录不承担规则权威身份。

路径验证只约束检查器读取。生产 Agent 必须在实际限制写入范围的执行环境中修改候选；不得将目录命名当作操作系统隔离。本轮未提供绕过沙箱的自动生产命令。现行源材料、验证器、最终评价和教师记录不由候选修改。执行前后检查指纹。

每任务最多两轮，每轮最多两个候选和一个组合。组合重新接受完整检查。所有运行先写 task、input_snapshot、sources、model、tools、evaluator、budget 条件以及总 calls/seconds/tokens 上限。原流程取得同总预算；记录生成、评审、修复和组合的全部实际成本，未知资源不得写0。

`scripts/compare_lesson_runs.py --experiment <清单> --output <.work新目录>` 只比较已经取得的运行记录。清单包含 limits（calls/seconds/tokens）、targets（如 pedagogy.transfer）、calibration（状态及教师依据引用）、runs。每条 run 包含 id、kind（baseline/candidate/composition）、round、conditions（上述七项）、usage（实际三项消耗，未知为null）、result（path/sha256）。先冻结该清单的条件与目标，再追加真实运行；不得事后改目标制造优势。

结果中的 candidate_for_teacher_review 仅表示有条件的候选，不自动写回源材料或记忆。同为通过时不按检查项计数选优；须增加预先声明的盲评或保留原方法。未校准、分歧、预算不足、条件变化或不稳定改善均保留原方法。模型评分是观察，课堂效果仍需实际试做。L4内容升级前后比较不能独自证明Harness改进。

### 校准与经验

首批样例见 `docs/harness-calibration.json`。expected为待教师校准的建议，不是已批准标签；开发和保留用途分开。教师确认后记录误报、漏报与定位准确性，明确阻断反例漏放时停止自动采用。小样本只支持当前覆盖。

每条经验保存触发条件、修改、运行证据、失败／不适用条件、验证任务和版本。先登记为本任务观察，经未参与优化的不同任务与非MI材料检验后再进入通用 skill。经验摘要受Git管理，原始日志留在.work。教师的备课Harness不成为学生必装工具。

## 借鉴来源与实现边界

- AItalk：本机HEAD `7f249718cacbf7a347aea6390ee9c6e334190900`；2026-10-20所读 `scripts/evaluate_course.py` SHA-256 `42206e1246ff36d0398136ec5fa9e72b99bfc4ce4278d1918ae522e51dc83d30`（记录文件指纹，工作区可能含未提交修改）。借鉴独立只读调用、结构化输出、分批图像和人工状态分离；未修改其生产入口。
- [Harness²](https://github.com/google-research/harness2)：2026-10-20读取main README，采用任务内提案／试跑／组合与跨任务经验两个层次。课程实现保留固定评价规则和有限预算，不沿用上游默认关闭沙箱的执行方式；没有直接安装其运行平台。本轮未获得可固定的上游commit，以上是日期标记的设计借鉴，不是代码依赖。
- [GEPA](https://github.com/gepa-ai/gepa)：2026-10-20读取README，参考用执行反馈改进提示与流程的思路。课程把反馈可用范围、未参与优化的评价和搜索总成本显式登记；尚未开展可证明收益的跨课对照。

本次经验：独立会话也会产生结构不合约的输出；实际引用和必评项检查必须先于采用。相同材料中的规则说明不能消除任务栏的旧要求，须走通具体输入、动作和产出。两条均为本次观察，未升级为普遍有效性结论。

校准数据中的reserved目前仅标记拟保留用途，样例已对开发者可见，不能宣称真正未参与优化。正式保留评价须由教师另行冻结并登记接触历史。本轮语义评审找到具体内容问题，也对缺助教实测保持阻断；尚无教师标签可计算误报／漏报率。

本轮适用条件、支持记录与反例边界见[经验登记](./harness-experience-20261020.md)，均保持任务级观察身份。

外置课堂图像可在 `sources` 中登记 `review_role: visual` 与 `review_pages`（实际对应的页码列表）；PNG/JPEG按相应批次附送，文本型视觉来源则进入视觉上下文。不能仅附文件名或哈希让评审者猜图像。图像引用须来自该批实际附件，每个视觉结论仍须引用实际幻灯片，不能用原图代替屏显观察。评审的材料缺陷与教师、助教、现场确认分别登记；后一类缺失不自动等于当前材料存在硬缺陷。此阶段解释尚待教师校准，保留旧轮分歧及原评级。
