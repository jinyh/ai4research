---
版本：v1.0.0
最后更新：2026-09-15
状态：教学构造回放包；验证记录见课次本轮记录
---

# 阅读卡：从源文本到评价的可复演小包

服务 L09–L15，同一数据对象贯穿指标、队列、工作流、评价、写作和评审。全部源文本、两种输出和参考标注为教学构造，运行器只回放已保存输出，不调用模型；日志记录本次实际回放与人为注入故障。

统一命题、解释与边界见[课程案例口径](../../../../course/reading-card-case.md)。

## 文件与分工

| 文件 | 用途 | 谁看 |
| --- | --- | --- |
| sources.json | 3 份源文本 T01–T03 | 生成/回放端与评价者 |
| outputs.json | 两条件共 6 份构造输出 | 回放端与评价者 |
| gold.json | 8 项应保留限定条件及源文片段 | 评价者 |
| annotations.json | 16 项条件判断及输出片段 | 评价者；课堂由学生逐项复核 |
| config.json | 固定队列、尝试预算与接口访问表 | 教师与运行器 |
| run.py | 回放、恢复、汇总与接口拒绝演示 | 教师／助教 |
| test_workflow.py | 完整性、失败恢复、权限接口与错误标注验证 | 助教 |

程序检查标注身份、引用片段、漏项与汇总；不自动判断语义。保留/遗漏的判定需要学生对回源文本核查。

## 快速复演

以下从课程仓库根目录执行，需 Python 3，无第三方依赖。输出只写到 `.work/`。每次新课堂使用新的输出目录。

```bash
python3 lessons/lesson-11/assets/reading-card-workflow/run.py replay --out .work/reading-card-demo --fault-once
```

此步故意在 T02-card 注入一次技术失败，退出码 2。打开 `events.jsonl` 与 `state.json`，先说明失败发生在哪里、哪些任务已经完成，再经人工决定继续：

```bash
python3 lessons/lesson-11/assets/reading-card-workflow/run.py replay --out .work/reading-card-demo
python3 lessons/lesson-11/assets/reading-card-workflow/run.py evaluate --out .work/reading-card-demo
python3 lessons/lesson-11/assets/reading-card-workflow/run.py access-check --out .work/reading-card-demo --role executor --resource gold
```

最后一步按教学工具接口的访问表拒绝请求，退出码 3，并保留 `access_denied` 记录。这里演示的是指定接口的拒绝，不是操作系统沙箱隔离；直接修改 Python 或绕开接口不在这个控制模型内。

## 课堂如何演

1. **L09 指标**：打开 T01 的源文本、输出和三条参考标注；学生先指出一项遗漏，再看它如何进入分子/分母。原 L09 布尔记录包单独标为复算校准。
2. **L10 工程校准**：继续使用本课 normalize_record 修复例；说明字段检查只保证结构，语义遗漏由此包的人工标注协议判断。
3. **L11 队列**：第一次运行在 T02-card 暂停；保留旧失败，恢复产生新 run ID；完成后看 T01 改善、T02 无改善、T03 负例。
4. **L12 工作流**：指认输入、持久状态、预算、评价入口和人工决定；执行 access-check 展示真实接口拒绝。预制模型输出的回放身份始终可见。
5. **L13 评价**：学生先复核一条标注，再汇总。card 3/8=0.375，free 4/8=0.500，差 -0.125。保留 T03；不画误差条、不作机制确认。
6. **L14–L15 写作/评审**：从 evaluation.json 反查具体记录；把有限观察、机制未决和 T03 范围问题一起写入报告。

## 失败、无改善与负例的区别

- 技术失败：人为注入的 T02-card 超时，属于执行事件；恢复后同一任务获得输出，两个 run ID 都保留。
- 无改善：T02 两条件都遗漏 1/3，属于评价结果。
- 负例：T03 card 遗漏 2/2、free 遗漏 1/2，属于评价结果；不能通过恢复运行或移出原样本使它消失。
- 原因候选：图表条件提取不足，须用解析记录或对照进一步核查；本包不提供机制证实。

## 验收

```bash
python3 lessons/lesson-11/assets/reading-card-workflow/test_workflow.py
```

另一名助教应能从 T03 的一项源文本条件反查到输出、标注、分项结果和总体结果；解释技术失败与负例的区别；重放不会重复记六个成功任务；输入变化会要求新版本目录；缺标注或不存在的引文会阻止汇总。
