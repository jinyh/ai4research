# 个人微型项目运行起点

输入与参考判定：公开教学构造。执行：本机实际运行指定 Python 实现，不调用模型。需要 Python 3 标准库。

## 第一次执行

把本目录复制到个人项目。保留 baseline.py，只在副本 changed.py 实施本人决定的修改。以下命令均在本目录运行：

```bash
python3 run.py execute --implementation baseline.py --out runs/baseline
python3 run.py evaluate --out runs/baseline
```

原实现有已知输入缺口。看到错误输入被接收，正是需要分析的现象；不要改参考判定让它通过。先预测，再查 events.jsonl。

## 本人修改后的比较

```bash
python3 run.py execute --implementation changed.py --out runs/changed
python3 run.py evaluate --out runs/changed
```

changed.py 必须定义 normalize_record(record)。有效输入返回规范化记录，无效输入抛出有理由的异常。返回空对象会被记录为“接受了该输入”，不能靠下游跳过掩盖。评价同时报告 normal_preserved、normal_errors、invalid_rejected、invalid_admitted，分母保留全部 8 项。

## 中断与恢复

```bash
python3 run.py execute --implementation changed.py --out runs/recovery --fault-once
python3 run.py execute --implementation changed.py --out runs/recovery --fault-once
python3 run.py evaluate --out runs/recovery
```

首次预期退出码 2；第二次为 0。受控中断发生在第三项处理前；成功项不重复。输入或实现变更后必须使用新目录；技术失败和正常记录校验失败分别记录。所有执行尝试最多为输入条数加一。把停止理由写入本人判断记录。

执行端不读 reference.json；评价端才读取。此区分是接口约束，导入的 Python 实现仍有普通本机进程权限，不是操作系统沙箱。公开参考判定已经可见，不能当作未见过的最终测试。

identity.json 保存输入、实现和执行器散列；events.jsonl 保存每项处理和失败；state.json 保存恢复位置；评价报告按参考判定和事件散列命名，保留不同评价版本。耗时只计本次处理函数调用，不含准备、导入与评价，不用于稳定性能结论。

```bash
python3 test_runner.py
```

测试检查执行、恢复、输入冻结、完整分母和拒绝所有记录等失败路径；测试结果不代替学生自己的研究结论。
