---
版本：v1.0.0
最后更新：2026-09-22
文档类型：课程算力指南
状态：现行
变更记录：
- v1.0.0 (2026-09-22): 新增沐曦课程算力入口，区分模型 API 与 GPU 实验；Pi Agent 为主要接入方式，OpenCode 为备选。
---

# 沐曦算力：申请与使用

本课程算力由沐曦支持，通过模力方舟使用模型服务与 GPU 资源。先按课程活动申请算力券，再根据自己的研究任务选择资源。领取资格、额度、有效期和可抵扣范围以课程活动通知及券面为准。

[申请课程算力](https://developer.metax-tech.com/activities/33){ .md-button .md-button--primary }
[打开模力方舟](https://ai.gitee.com/){ .md-button }

## 先选资源

| 你的任务 | 使用什么 | 从哪里开始 |
| --- | --- | --- |
| 在 Pi Agent 中辅助阅读、理解代码和分析结果 | 沐曦 Token 资源包提供的模型 API | [领取与兑换](#apply)，然后[连接 Pi](#pi) |
| 自己运行代码，开展训练、推理或对照实验 | 带“券”标识的沐曦 GPU 服务 | [租用与结束 GPU 实例](#gpu) |

只调用模型 API 无需另租 GPU。Pi Agent 是课程主平台，OpenCode 等是备选；平台与模型选择不作为评分项。

## 领取与兑换 {#apply}

1. 登录沐曦开发者社区，在[课程专属领取页](https://developer.metax-tech.com/activities/33)按活动要求申请。
2. 根据活动通知领取算力券，在[模力方舟](https://ai.gitee.com/)“费用中心 → 算力券”兑换。
3. 核对账户中的额度、有效期及适用服务，再选择 Token 资源包或 GPU。确认订单的抵扣与应付金额；资格、额度或抵扣不清楚时先联系助教。

本课程不要求学生自费购买额度。资源尚未到账或暂时不可用时，先使用[课前准备中的备用路径](./pi-setup.md#fallback)。

## 模型资源包与访问令牌 {#token}

在模型广场选择[沐曦 Token 资源包](https://ai.gitee.com/serverless-api/packages/1492)，确认套餐范围、有效期与算力券抵扣后购买。模型名称以当前套餐为准；公开模型列表中存在某个模型，不代表你的资源包已包含它。

在“工作台 → 设置 → 访问令牌”新建通用令牌，授权本次使用的沐曦资源包。个人资源与组织资源要使用对应工作台的令牌。操作细节见[官方访问令牌说明](https://ai.gitee.com/docs/account/access-token)。

API Key 仅保存在本机凭据或当前终端环境中，不放入作业、截图、聊天记录或公开仓库。首次连接使用公开或课堂构造材料。

## 在 Pi Agent 中连接模型 {#pi}

先按[Pi Agent 课前准备](./pi-setup.md)完成安装与个人项目准备。下面只补充模力方舟连接；已有配置请合并，保留其他服务商。

### 1. 设置当前终端的 API Key

在终端中输入以下命令，再按提示粘贴令牌；输入过程不显示令牌内容。

**macOS / Linux / WSL（Bash 或 Zsh）：**

```bash
printf '请输入模力方舟 API Key: '
read -rs MOARK_API_KEY
export MOARK_API_KEY
printf '\n'
```

**Windows PowerShell：**

```powershell
$moarkSecret = Read-Host "请输入模力方舟 API Key" -AsSecureString
$env:MOARK_API_KEY = [System.Net.NetworkCredential]::new("", $moarkSecret).Password
Remove-Variable moarkSecret
```

环境变量只在当前终端及其启动的程序中生效；后续在同一终端启动 Pi。

### 2. 添加模型配置

编辑本机用户目录中的 `models.json`：macOS / Linux / WSL 为 `~/.pi/agent/models.json`，Windows 为 `%USERPROFILE%\.pi\agent\models.json`。不存在时创建对应目录和文件。

将下面的 `REPLACE_WITH_AUTHORIZED_MODEL_ID` 换成套餐已授权、支持工具调用的文本模型 ID；模型 ID 按平台模型详情复制，不用展示名称代替。

```json
{
  "providers": {
    "moark": {
      "baseUrl": "https://ai.gitee.com/v1",
      "api": "openai-completions",
      "apiKey": "$MOARK_API_KEY",
      "authHeader": true,
      "models": [
        { "id": "REPLACE_WITH_AUTHORIZED_MODEL_ID" }
      ]
    }
  }
}
```

`$MOARK_API_KEY` 是环境变量引用，保留原样；不要改成真实密钥。配置依据为[模力方舟 Pi 指南](https://ai.gitee.com/docs/integrations/Development-Tools/pi)与 [Pi 自定义模型说明](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md)。

### 3. 检查连接，再开始课堂任务

进入已有个人项目目录，在设置令牌的终端启动：

```bash
pi --tools read --no-extensions
```

输入 `/model`，选择 `moark` 下已授权的模型，发送“请只回复：连接成功，不读取文件”。收到正常回复，并在平台调用记录中看到对应请求后，基本连接检查完成。记录 Pi 版本、模型 ID、日期与检查结果，不记录密钥。

随后按第 1 讲任务契约提出建议、人工判断、有限写回和核对 diff。Pi 默认没有逐次权限弹窗；写入与执行边界按[课程操作说明](./pi-setup.md#permissions)落实。问答成功不代表工具调用、写入限制或 GPU 实验已经验证。

??? note "OpenCode 备选接入"

    已准备 OpenCode 的同学可沿用同一个人项目，参照[课程备选平台说明](./opencode-setup.md)和[模力方舟 OpenCode 指南](https://ai.gitee.com/docs/integrations/Development-Tools/open_code)连接。仍使用套餐授权的模型与令牌，沿用相同的任务范围、人工核验和记录要求。

## 租用与结束 GPU 实例 {#gpu}

1. 先确定实验确实需要 GPU，并根据课程通知或与助教确认的方案选择型号、数量和镜像。确认代码及依赖适配所选沐曦环境，不直接假定原有 CUDA 环境可用。
2. 在[沐曦算力专区](https://ai.gitee.com/compute/metax)选择带“券”标识的服务，核对费用、抵扣与实例类型后创建。
3. 打开实例的 JupyterLab 与 Terminal，执行 `mx-smi` 检查设备；按本人的实验说明运行，代码、数据和结果放在 `/data`，保留环境、配置、命令和实验 ID。
4. 结束实验前，将代码、日志与结果下载或同步回个人项目；较大模型文件保存到自己的存储，在项目中记录位置。
5. 按实例类型结束使用，并在控制台确认状态。关闭浏览器不会停止服务。销毁会永久删除全部实例数据，包括 `/data`；关机是否停止计费及保留期限按当前实例规则确认。

按量实例的关机与自动销毁规则、目录保留方式及文件下载步骤见[官方容器使用指南](https://moark.com/docs/compute/container)。

## 回到同一个个人项目 {#project}

| 提交节点 | 资源服务什么任务 | 保存哪些材料 |
| --- | --- | --- |
| 问题门 · 第 6 课后 | 模型辅助梳理文献与问题，回原文核验 | 精读卡、证据地图、问题定义、AI 使用与人工核验记录 |
| 判断门 · 第 9 课后 | Pi 辅助理解代码、完善方案；按需用 GPU 跑 baseline | 实验规格、环境与配置、复现说明、实际失败记录 |
| 验证门 · 第 13 课后 | 按需调用模型或 GPU，执行与评价个人 Agent Workflow | 工作流、权限边界、运行记录、对照评价及失败分析 |
| 论证门 · 第 16 课 | 根据已有结果整理图表与报告，逐项核对结论 | 论文式报告、最终工作流与复盘、可追溯证据 |

第 1–8 课使用[早期脚手架](./starter-template.md)，第 9 课迁移到[完整项目模板](./project-template.md)。算力使用记录并入现有项目，不另设“算力作业”。第 8 课诊所、第 15 课评审不新增正式提交；完整条件见[项目要求](./assignments.md)与[考核细则](./assessment.md)。

## 遇到问题 {#help}

| 情况 | 先检查什么 |
| --- | --- |
| 申请或兑换未完成 | 活动资格、领取通知、登录账户与券有效期；联系助教 |
| 认证或资源未授权 | 当前终端变量、令牌所属工作台、资源包授权与余额 |
| 找不到模型 | `models.json` 位置和格式、模型 ID、套餐范围；重启 Pi 后检查 `/model` |
| 问答成功但工具调用失败 | 模型是否支持工具调用、版本与接口兼容；保留去除密钥后的错误信息交助教 |
| GPU 环境无法运行 | 设备状态、镜像、依赖适配与实验说明；先跑最小样例 |
| 平台暂时不可用 | 使用已有回放材料，标明实际执行、构造回放或未执行 |

本页依据课程提供的《沐曦算力申请与使用指南》及所链接的官方文档整理，更新于 2026-09-22。额度、模型、镜像及界面可能调整，以课程通知和账户实际授权为准。
