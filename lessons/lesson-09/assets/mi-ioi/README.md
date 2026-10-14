# GPT-2 small IOI 激活干预教学包

版本：v1.0.0
最后更新：2026-10-14

本包进行真实模型推理。研究对象、输入和适用范围见[个人微型项目](../../../../course/micro-project.md)。输入为课程自行构造，依据 [IOI 原始研究](https://arxiv.org/abs/2211.00593) 的任务形式；不是原论文数据或完整回路复现。模型来自 [openai-community/gpt2](https://huggingface.co/openai-community/gpt2)，MIT 许可，固定修订见 protocol.json。GPT-2 被研究模型与协助研究的 Agent 是两个不同角色。

## 准备与运行

教师在课前分发固定版本模型目录，包含 config.json、model.safetensors、tokenizer.json、tokenizer_config.json、vocab.json、merges.txt 和模型许可。依赖使用 Python 3.12 与 requirements.txt；不要求学生付费或本地 GPU。安装排障计入每课总预算，不能把课堂未完任务整体转移到课后。

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python test_runner.py
.venv/bin/python run.py --model-dir /path/to/pinned-gpt2 --split dev --out runs/baseline-dev
```

保持 baseline，复制 policy-baseline.json 为自己的 policy.json，只改授权的层、位置及理由。实际修改后使用新目录：

```sh
.venv/bin/python run.py --model-dir /path/to/pinned-gpt2 --policy policy.json --split dev --out runs/revised-dev
```

在开发材料上确定选择、冻结协议与候选策略之后，才能执行保留评价：

```sh
.venv/bin/python run.py --model-dir /path/to/pinned-gpt2 --policy policy.json --split heldout --out runs/revised-heldout
```

本地文件可读范围只是课堂协议，不声称实现了操作系统隔离。真实未见评价可由助教保管保留材料或在单独执行环境运行；查看结果后若继续改进，需新评价材料或降低结论范围。

## 输入与对照

cases.jsonl 共 24 条，store／park 为开发模板族，office／party 为保留模板族，各族 6 组名称方向。划分单位是模板族，不把同一句换名字当作独立模板迁移。

指标为最后位置的 `logit(原句间接宾语) - logit(原句主语)`。每条输入保存原句 clean、扰动 corrupt、扰动自替换 noop、原句激活维度打乱 random 和指定 patch。random 保持向量元素及范数但破坏维度对应，只是一种负对照。noop 应与 corrupt 在浮点误差内一致；偏离时先查实现。

layer 使用 0–11；position 为第二次主语所在 token 的 subject 或句尾 last。对整条 residual 向量做干预不能直接定位单一注意力头。随机对照按输入 ID 固定种子，恢复运行不改变它。

## 记录与故障恢复

每次运行生成 manifest.json、逐条 results.jsonl、events.jsonl 和完成后的 summary.json。保留模型／依赖版本、输入与实现指纹、运行时间、前向次数及失败。输出目录非空时默认拒绝覆盖。

```sh
.venv/bin/python run.py --model-dir /path/to/pinned-gpt2 --out runs/recovery --fault-after 2
.venv/bin/python run.py --model-dir /path/to/pinned-gpt2 --out runs/recovery --resume
```

首次受控中断退出码为 2，恢复跳过已完成记录；输入、协议、实现或策略改变时拒绝恢复，应新建运行目录。普通模型加载失败同样要保存实际错误与修复，不伪造成功记录。

## AI 研究工作流

[WORKFLOW.md](./WORKFLOW.md)给出可交给当前 Agent 环境执行的真实任务。Agent 在开发反馈上提出策略，实验运行器负责测量，评价协议保持冻结，学生解释采用决定。Agent 输出与工具记录写入个人项目，不能拿教师示例或运行器前向推理冒充自己的 AI 研究动作。
