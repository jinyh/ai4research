---
版本：v1.1.0
最后更新：2026-09-22
文档类型：课前环境指南
状态：现行；Pi Agent 主平台课前准备入口
变更记录：
- v1.1.0 (2026-09-22): 增加沐曦课程资源与模力方舟接入入口。
- v1.0.0 (2026-09-22): 确立 Pi Agent 主路径，说明安装、模型连接、项目准备、人工确认、实际限制与备用路径。
---

# Pi Agent 最小启动说明

## 一、课堂定位

Pi Agent 是从第 1 课贯穿全程的主要课堂演示与实践平台。OpenCode、Claude Code、Codex 等为备选；需要 OpenCode 时见[备选平台说明](./opencode-setup.md)。平台与模型选择不构成评分项，课程评价研究判断、可验证产出和个人 Agent Workflow。

安装、模型连接和项目准备在课前完成。学生不必自费购买 API 额度；优先使用学校允许、网络可达且成本可控的后端。首次交互只用公开或课堂构造材料。

## 二、安装与启动

先准备 Git、终端及符合 Pi 当前要求的 Node.js（本次核验为 ≥22.19.0）。安装命令与版本要求分别见 [Pi 官方快速开始](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#quick-start)和[软件包声明](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/package.json)。

```bash
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pi --version
```

进入个人项目目录后启动。第 1 课先只向模型开放读取工具，并关闭扩展自动发现：

```bash
pi --tools read --no-extensions
```

这限制本次可用工具，不等于目录沙箱，也不阻止向模型后端发送输入。课堂契约中的 `NETWORK off` 指不进行额外联网检索或外部操作；模型服务连接仍按已批准的数据规则使用。启动时核对加载的项目说明与配置，只使用自己建立的课堂项目。工具选项见[官方 CLI 说明](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#cli-reference)。

## 三、连接模型

本课程由沐曦提供算力支持。使用课程资源时，先[申请算力券并准备模型资源包](./metax-compute.md#apply)，再按[Pi 接入步骤](./metax-compute.md#pi)配置模力方舟；仅调用模型 API 无需另租 GPU。

使用已有订阅时通过 `/login` 选择提供方；API 后端按提供方文档配置凭据，再用 `/model` 选择模型。凭据放在本机凭据配置或环境中，不写入项目、截图或使用日志。学校与自定义兼容端点的设置见 [Providers](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/providers.md)和 [Models](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md)。

助教课前登记可用后端、Pi 版本及一次最小问答结果。课程阅读材料中的旧 commit 只用于结构分析，不是本学期安装版本锁定。连接失败时转 §五，不在课堂逐台排障。

## 四、人工确认与执行限制 {#permissions}

Pi 默认不提供逐次权限弹窗，`AGENTS.md` 和任务契约用于声明边界；真正的路径、命令和网络限制须由经过检查的扩展或隔离环境落实。参见[官方设计说明](https://github.com/earendil-works/pi/tree/main/packages/coding-agent#philosophy)。

课堂按以下顺序操作：

1. Pi 读取指定材料，提出建议及其理由；人判断采用哪条。
2. 人明确本次允许修改的文件与段落。Lesson 01 只改 `problem-definition.md` 的“当前问题”。
3. 已通过复演的限制配置可用于 Agent 写回；没有该配置时，继续保持读取工具，由人将批准的文本应用到目标段。日志如实区分“Agent 写入”和“人工应用建议”。
4. 人查看 `git diff -- problem-definition.md`，再查看 `git status --short` 核对全部变化；通过后填写修改记录和 AI 使用日志。Git 用于核对与恢复，不提供权限隔离。

后续需要命令、写入或实验执行的课次，助教须提前验证相应执行限制与停止条件；不能用一句“最小权限”代替实际配置。第 1 课的人工应用路径完成问题修订，不算执行了效果实验。

## 五、备用路径 {#fallback}

主平台不可用时，可使用已准备好的 OpenCode 等备选环境；沿用同一任务契约、文件、人工审核点和验收标准。所有平台均须核对其实际限制配置，不能假定功能与默认值相同。

模型也不可用时，使用课堂材料包的构造回放和备用 diff，人工完成判断、修改与记录，标明“构造回放”，不记为模型实际运行。临时共用设备时，每位学生仍维护自己的项目和记录。卡点课前报告助教。

## 六、项目目录与 AGENTS.md

从[早期研究脚手架](./starter-template.md)创建个人项目，按模板准备 `AGENTS.md`、`problem-definition.md`、`artifact-tracking.md`、`ai-usage-log.md`、`agent-permissions.md` 与 `notes/`。仅在新建的个人课堂目录中执行初始化：

```bash
mkdir my-research-project
cd my-research-project
git init
# 在此按脚手架创建文件，检查内容后建立基线
git add AGENTS.md problem-definition.md artifact-tracking.md ai-usage-log.md agent-permissions.md notes/
git commit -m "baseline: 个人项目起点"
```

已有仓库先检查状态；不要重新初始化或覆盖已有材料。基线让后续 diff 能显示已跟踪文件的变化，新文件同时通过状态清单核对。`AGENTS.md` 课前自取，课堂只核对任务范围。

## 七、课前自查与复演记录

- [ ] Pi 可启动；登记版本、操作系统、模型名称及后端，日志不含凭据。
- [ ] 个人项目文件齐全，已建立基线，能查看差异与完整文件状态。
- [ ] 读取模式能完成一次建议生成；记录实际加载的工具与配置。
- [ ] 涉及 Agent 写入或命令执行时，已验证允许、拒绝与停止路径；未通过则采用人工应用或备用环境。
- [ ] 已演练一次建议取舍、目标段修改、diff 核对及人工记录。
- [ ] 已准备无模型回放，明确实际运行、构造回放和预期结果的区别。

## 八、核验状态

2026-09-22 对照官方文档核验安装入口、Node 要求、模型选择、工具选项及权限行为。本次为文档核验，未代替授课电脑上的安装、后端连接、限制配置和课堂复演；现场结果填入助教复演记录。课程时段、个人产出、评分及四次正式提交保持不变。
