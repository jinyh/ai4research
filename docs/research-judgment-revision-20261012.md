# 全课程研究判断与负荷修订记录

日期：2026-10-12。范围：16课及现行课程材料。状态：课程修订已提交推送，学生网站已发布；教师内容复核、助教计时试做与现场教学验证独立登记，不沿用历史 PASS。修订时仅完成本地检查；2026-10-12用户随后明确授权提交、推送和学生网站发布，执行状态见[网站部署记录](../web/README.md)。

## 审阅入口

- [课程逐课输入—判断—验证—输出—下课去向—课外预算总表](../course/judgment-path.md)
- [个人微型项目实际运行入口](../course/micro-project.md)
- [公开文献起始池](../course/source-starter-pool.md)
- [课程讲义、教案、逐页稿与课件入口](../lessons/README.md)
- [评分](../course/assessment.md)、[四次提交](../course/assignments.md)、[阅读边界](../course/reading-list.md)

## 变更与保留

每课新增一份学生共同判断任务和一份教师依据。普通课统一为入口确认、方法、独立判断、同伴比较、揭示校准、两段个人迁移、中点点评、反查及收束，合计90分钟；个人实践每段15分钟。L8/L15/L16保留学生主导结构。先判断后揭示，已有公开答案只作方法参考。

16套讲义、教案、逐页母稿及PPT同步。保留交大母版、原生图表、有效方法说明及历史版本记录。L1实际36页与原35页母稿冲突已修复；L3/L4保持21/18页，全课程319页。讲述备注写入判断依据、动作、课堂安排和来源。

课外预算包含全部必做事项：普通课15分钟阅读、10分钟准备、35分钟补全；门课15分钟整理、45分钟修订提交。三张精读卡分别在L4/L5/L6课堂完成，候选池可从公开起始材料独立筛选。报告与展示从同一项目累计材料整理。安装排障超时使用备用路径，工程证据最终仍须实际运行。

保留16课、32学时、八阶段链路、个人项目、L6/9/13/16四次正式提交和25%/30%/25%/20%评分。课堂质量尺度映射原等级，不增加每周成绩、工件数、失败数或工具数。

## 技术证据与边界

旧工作树及319页原课件已完整留存于本地工作记录；基线文件指纹、原有未提交差异与本轮验证日志分开保存。每套课件未修改的ZIP部件与基线逐字节比较，母版、主题和未涉及的原生对象保留。新增教师答案未列入网站或学生下载允许清单。

- 阅读卡原包：5项测试通过；RSI原包：8项测试通过。
- 新微型项目：7项行为测试通过，覆盖输入改变、缺失、分母完整、实际修改、中断恢复、不重复处理、公开评价隔离及边界。执行和评价分接口，普通Python实现仍有进程权限，不声称操作系统沙箱。
- 检索包：5项查询语义与空条件检查通过；固定保存结果中的错误供学生诊断。标题查询 `read AND paper` 仅命中S1，S3的paper只在keywords中。
- 个人路径桌面走查：实际执行baseline、修改版、中断和恢复，保留事件及散列。公开开发样本中正常输入均保留2/2；无效输入误接收从2/6变为0/6。此结果仅证明构造开发样本上的输入校验改变，不证明模型能力或真实总体改善。学生须独立选择其修改与验证。
- 网站：学生视图与下载边界17项测试通过；严格本地构建通过。最终链接、课件和视口检查见下方终检记录。

## 典型学生路径与时间核验

| 阶段 | 同一项目如何累计 | 课堂落点 |
| --- | --- | --- |
| L1–2 | 选择阅读卡中值得验证的小问题；设定读写和评价范围 | 比较取舍、核查trace、有限diff |
| L3–6 | 用查询与起始池形成候选表；三张卡逐课完成；受限综合后定义可证伪的小问题 | 不是三个案例各做一个项目；问题门主要检查在课堂完成 |
| L7–9 | 区分内容改善与测量变化，诊所修订；在现成CPU起点运行公平baseline | 同伴实际复查运行步骤和输入身份 |
| L10–13 | 本人修改实质校验环节，保留失败，验证恢复；比较基线与修改版 | 独立评价不读取学生输出后改标准，公共开发用例不充当盲测 |
| L14–16 | 把已有比较写成受限论证；真实同伴评审，现场修改和逆向抽查 | 最终报告、展示与运行说明均整理累计材料 |

这是材料及执行路径的桌面推演，不是实际学生计时。25人按7个3–4人固定组，专用课的换场与参与覆盖以当前教案为准；人数改变时重算。助教试做记录总耗时、提示次数、卡点，超出预算先缩小材料或问题，再复测，不能把超时转为新增课后任务。

## 终检记录与逐课入口

- 16套课件共319页，均完成文件重导入、全页渲染和联系表检查；60个屏显修改页按全尺寸检查，319页讲述备注与本轮母稿逐页匹配。每套文件结构、布局和字体策略检查通过，最终文件指纹与检查回执一致。
- 全部教案合计90分钟；普通课采用规定的10段结构，两段本人迁移各15分钟。特殊课保留学生主导组织结构。
- 课程一致性12项通过；225份纳入范围的Markdown内部链接通过；网站严格构建及91个HTML的链接、锚点、16个课堂入口和发布边界检查通过。
- 网站已检查1280像素桌面视口与390像素窄屏；课堂入口及共同任务可读，窄屏没有页面横向溢出。
- L2配套PDF同步为27页高清屏显版，保留课件视觉；常规导出发生字体替换，改用已核验的课件渲染生成PDF。PDF用于查看，文字不可直接选择；修改和复制使用可编辑PPTX。PDF重新打开、全页渲染及修改页全尺寸检查通过。
- Microsoft PowerPoint原生打开检查尚未完成；当前通过的是文件重导入与渲染检查。教师内容复核、学生实际计时和教室投影不计入上述技术通过记录。

下表列出当前文件。页面数字为本轮修改的屏显页；其余页面保留有效讲解，备注已同步。完整SHA256、逐部件保留记录、渲染和运行日志保存在本机工作记录中，表中提供指纹前12位方便识别。

| 课次 | 学生任务 | 教师依据 | 可编辑课件 | 页数 | 屏显修改页 | SHA256前12位 |
| --- | --- | --- | --- | ---: | --- | --- |
| L1 | [任务](../lessons/lesson-01/judgment-task.md) | [依据](../lessons/lesson-01/judgment-teacher.md) | [PPT](../lessons/lesson-01/lesson-01.pptx) | 36 | 7, 31, 36 | `795b43a5dfd8` |
| L2 | [任务](../lessons/lesson-02/judgment-task.md) | [依据](../lessons/lesson-02/judgment-teacher.md) | [PPT](../lessons/lesson-02/lesson-02.pptx) | 27 | 4, 24, 27 | `d6b0b64294c7` |
| L3 | [任务](../lessons/lesson-03/judgment-task.md) | [依据](../lessons/lesson-03/judgment-teacher.md) | [PPT](../lessons/lesson-03/lesson-03.pptx) | 21 | 1, 3, 6, 13, 14, 16, 17, 18, 21 | `4ecadbabf71b` |
| L4 | [任务](../lessons/lesson-04/judgment-task.md) | [依据](../lessons/lesson-04/judgment-teacher.md) | [PPT](../lessons/lesson-04/lesson-04.pptx) | 18 | 2, 3, 9, 11, 12, 14, 15, 17, 18 | `fb4775e9bc00` |
| L5 | [任务](../lessons/lesson-05/judgment-task.md) | [依据](../lessons/lesson-05/judgment-teacher.md) | [PPT](../lessons/lesson-05/lesson-05.pptx) | 21 | 3, 17, 21 | `05ccf732969f` |
| L6 | [任务](../lessons/lesson-06/judgment-task.md) | [依据](../lessons/lesson-06/judgment-teacher.md) | [PPT](../lessons/lesson-06/lesson-06.pptx) | 22 | 3, 17, 22 | `b1615ad9eaa3` |
| L7 | [任务](../lessons/lesson-07/judgment-task.md) | [依据](../lessons/lesson-07/judgment-teacher.md) | [PPT](../lessons/lesson-07/lesson-07.pptx) | 17 | 3, 14, 17 | `1bfacfda4c4c` |
| L8 | [任务](../lessons/lesson-08/judgment-task.md) | [依据](../lessons/lesson-08/judgment-teacher.md) | [PPT](../lessons/lesson-08/lesson-08.pptx) | 15 | 2, 13, 15 | `12c247605d22` |
| L9 | [任务](../lessons/lesson-09/judgment-task.md) | [依据](../lessons/lesson-09/judgment-teacher.md) | [PPT](../lessons/lesson-09/lesson-09.pptx) | 21 | 3, 17, 21 | `4ed522a61f3d` |
| L10 | [任务](../lessons/lesson-10/judgment-task.md) | [依据](../lessons/lesson-10/judgment-teacher.md) | [PPT](../lessons/lesson-10/lesson-10.pptx) | 17 | 3, 13, 17 | `4858f29a1a96` |
| L11 | [任务](../lessons/lesson-11/judgment-task.md) | [依据](../lessons/lesson-11/judgment-teacher.md) | [PPT](../lessons/lesson-11/lesson-11.pptx) | 20 | 3, 16, 20 | `2c68dc8b688a` |
| L12 | [任务](../lessons/lesson-12/judgment-task.md) | [依据](../lessons/lesson-12/judgment-teacher.md) | [PPT](../lessons/lesson-12/lesson-12.pptx) | 21 | 2, 17, 21 | `dcc1b0ebe8a6` |
| L13 | [任务](../lessons/lesson-13/judgment-task.md) | [依据](../lessons/lesson-13/judgment-teacher.md) | [PPT](../lessons/lesson-13/lesson-13.pptx) | 20 | 3, 17, 20 | `3ae42c8c6eaa` |
| L14 | [任务](../lessons/lesson-14/judgment-task.md) | [依据](../lessons/lesson-14/judgment-teacher.md) | [PPT](../lessons/lesson-14/lesson-14.pptx) | 16 | 3, 8, 16 | `4875714db659` |
| L15 | [任务](../lessons/lesson-15/judgment-task.md) | [依据](../lessons/lesson-15/judgment-teacher.md) | [PPT](../lessons/lesson-15/lesson-15.pptx) | 15 | 4, 10, 15 | `ec4ed1d7fa0b` |
| L16 | [任务](../lessons/lesson-16/judgment-task.md) | [依据](../lessons/lesson-16/judgment-teacher.md) | [PPT](../lessons/lesson-16/lesson-16.pptx) | 12 | 6, 7, 12 | `0c967472c86e` |

## 待独立登记

| 检查 | 当前状态 | 通过依据 |
| --- | --- | --- |
| 教师内容复核 | 待进行 | 对本轮任务、不同可接受答案与评分锚点签核 |
| 助教计时试做 | 待进行 | 逐课时间、提示次数、卡点及收缩复测记录 |
| 教室投影与实际教学效果 | 待进行 | 授课电脑、投影可读性、学生判断与迁移表现 |
| 线上发布 | 已完成 | GitHub Actions成功；62项线上文件与验收快照一致，教师答案入口404，详见[部署记录](../web/README.md) |
