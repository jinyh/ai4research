# 阅读卡：下载、复演与核查

这套材料贯穿第 9–15 讲。3 份源文本、两条件共 6 份输出、8 项参考条件和 16 条条件标注均为**教学构造**。程序回放固定输出，不调用模型、不需要模型账户。

## 下载与运行

[下载完整回放包（ZIP）](../downloads/reading-card-workflow.zip)。解压后，在 `reading-card-workflow` 文件夹打开终端。需要 Python 3，无第三方依赖。

每次复演使用新的输出目录；以下使用 `runs/demo`：

```bash
python3 run.py replay --out runs/demo --fault-once
```

此步在 T02-card 注入受控技术失败，预期退出码 **2**。先打开 `runs/demo/events.jsonl` 与 `state.json`，检查哪些任务完成、哪里失败，再恢复：

```bash
python3 run.py replay --out runs/demo
python3 run.py evaluate --out runs/demo
python3 run.py access-check --out runs/demo --role executor --resource gold
```

后续预期退出码依次为 **0、0、3**。最后一步应拒绝 executor 读取 gold，并保存 `access_denied` 事件；这是指定接口的角色检查，不是操作系统沙箱。恢复保留旧失败，新执行产生新的 `run_id`，已完成任务不重复执行。

## 先核查，再看汇总

1. 在 `sources.json` 找到 T01 的一个限定条件。
2. 对回 `outputs.json` 的两份输出，判断是否保留了该条件。
3. 核对 `gold.json` 与 `annotations.json` 的原文、输出片段及保留/遗漏标记。
4. 打开运行生成的 `evaluation.json`，核对分项结果与总计。

| 材料 | 阅读卡遗漏 | 自由摘要遗漏 | 观察 |
| --- | ---: | ---: | --- |
| T01 | 0/3 | 2/3 | 阅读卡更少 |
| T02 | 1/3 | 1/3 | 无改善 |
| T03 | 2/2 | 1/2 | 阅读卡更差 |
| 逐项合并 | 3/8 = 0.375 | 4/8 = 0.500 | 差值 −0.125 |

技术失败、无改善和负例是不同对象。恢复运行可以补齐技术失败的输出，不能消除 T03 的负向结果。程序检查记录和汇总，语义由人核验。

## 怎样写入判断

本构造包的总遗漏率方向与 Q1 一致；H1 生成机制与 A2 测量解释仍未区分，其他质量未测，T03 限制外推范围。没有随机重复，不报告误差条或显著性；这些材料不能充当阅读卡真实科研效果的证据。

[命题与解释定义](../course/reading-card-case.md) · [评价报告样例](../lessons/lesson-13/evaluation-report-example.md) · [评审与修改练习](../lessons/lesson-15/calibration-pack.md)

## 单独查看文件

[源文本](../lessons/lesson-11/assets/reading-card-workflow/sources.json) · [预制输出](../lessons/lesson-11/assets/reading-card-workflow/outputs.json) · [参考条件](../lessons/lesson-11/assets/reading-card-workflow/gold.json) · [逐项标注](../lessons/lesson-11/assets/reading-card-workflow/annotations.json) · [固定配置](../lessons/lesson-11/assets/reading-card-workflow/config.json) · [运行器](../lessons/lesson-11/assets/reading-card-workflow/run.py) · [行为验证](../lessons/lesson-11/assets/reading-card-workflow/test_workflow.py)

可以运行 `python3 test_workflow.py` 核验包的关键行为。使用自己的项目材料时，重新定义评价协议与运行版本，保留原始记录和人工决定。
