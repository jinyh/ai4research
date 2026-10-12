# 第 11 课教学资产

| 资产 | 角色与来源 | 发布与范围 |
| --- | --- | --- |
| `reading-card-workflow/` | 课程原有阅读卡构造包，见该目录 README | 学生发布沿用现有逐文件清单；不是外部模型实测 |
| [RSI 案例](rsi-selection-case/README.md) | 公开材料审计＋课程自行编写、实际运行的合成 Bernoulli 实验 | 不代表 Dream-RSI 或工业任务实测；不含未公开计划和学生资料 |
| [选优诊断图](rsi-selection-case/figures/selection-diagnosis.png) | 自建图表，由冻结 `summary.json` 生成，500 重复、95% bootstrap 区间 | 课程自建资产，可随教学案例分发；图中结果仅适用于冻结模拟设置 |
| `rsi-selection-case/teacher-notes.md` | 教师诊断答案与检查提示 | 教师材料，不进入学生网站或下载包 |

公开事实版本、来源链接与指纹见案例 `source-audit.json`。网站只按 `web/scripts/link_content.py` 白名单发布学生文件，不递归收集目录。外部原始资料只读保留于本机过程目录，未整体复制进教学包。
