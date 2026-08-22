# 项目重整建议

> 实施裁定（2026-08-05）：全部试讲版本及其内容源、讲述材料和判断记录进入 `archive/trial-lecture/`；逐页渲染、解包 XML 和完全重复缓存进入 `.work/`。该裁定取代下文对试讲内容“选取必要里程碑”的建议，PPT 视觉试制稿仍执行选择性归档。

## 1. 结论

建议采用“分阶段结构迁移”的方式整理仓库：先修复规则入口并停止产生新的散落中间文件，再重组课程设计、逐课材料、正式交付、参考资料和历史归档。

本次重整应遵循以下原则：

- `AGENTS.md` 是 Codex、Claude Code 和 OpenCode 共用的项目规则源。
- `CLAUDE.md` 只作为指向 `AGENTS.md` 的单向兼容入口，禁止双向软链接。
- 正式内容、当前工作稿、正式交付、历史里程碑和临时产物必须分区。
- PPT 只保留现行可编辑文件、正式交付和少量具有决策价值的试制里程碑。
- 项目级 skill 只承载本课程特有的重复工作流，不复制全局 presentation、PPT 或 Zotero 能力。
- MCP 配置和凭据保留在用户级环境，不把本机配置直接提交到项目。

## 2. 已验证的现状

截至 2026-08-05，仓库存在以下问题：

1. `AGENTS.md` 与 `CLAUDE.md` 当前互相指向，形成循环软链接，两份文件均不可正常读取。Git 中原有设计是 `AGENTS.md` 为普通文件、`CLAUDE.md` 单向指向它。
2. 根目录缺少 `README.md`，主要目录的职责只能从各子目录说明和 Agent 规则中推断。
3. `projects/` 同时放置正式逐课材料、历史文稿、视觉样张、PPT 试制稿、预览图以及两个完整试讲工程。
4. `projects/` 约 29 MB，包含 13 个 PPT/PPTX；其中还跟踪了大量 PPT 解包 XML、逐页渲染图和验证产物。
5. `ref/` 约 546 MB。多数外部原件已被 `.gitignore` 排除，但一次完整的 PPT 制作工作台被放入 `ref/ppt-master-ppt-1-lesson-01/`，它不属于参考资料。
6. 存在内容完全相同的 PPT 副本，例如部分试讲导出文件、视觉样张和源文件在多个目录重复保存。
7. `.tmp/` 已开始被忽略，但 `.ppt_master_inputs/`、各类 render、layout、XML inspection、QA 缓存和本地依赖尚未形成统一的产物边界。
8. 当前分支领先远端 11 个提交，且存在较多已修改和未跟踪文件。重组前必须先完成清单确认和安全检查点，不能直接批量移动或清理。
9. 仓库内没有项目级 skill 或 MCP 配置；相关能力均来自用户级安装。
10. Claude 侧当前有 GitHub、Zotero 和 Context7 等 MCP，其中一个 GitHub 连接异常；另有凭据通过命令参数传递，存在被进程列表、命令输出或日志暴露的风险。

## 3. 推荐的目标结构

```text
.
├── README.md
├── AGENTS.md
├── CLAUDE.md -> AGENTS.md
├── .agents/
│   └── skills/
│       └── prepare-course-lesson/
├── .claude/
│   └── skills/
│       └── prepare-course-lesson -> ../../../.agents/skills/prepare-course-lesson
├── course/
├── lessons/
│   ├── README.md
│   ├── lesson-01/
│   │   ├── handout.md
│   │   ├── teaching-plan.md
│   │   ├── slides.md
│   │   ├── slides.pptx
│   │   ├── reading-notes.md
│   │   └── assets/
│   └── lesson-02/
├── deliverables/
├── references/
│   ├── README.md
│   ├── notes/
│   └── library/
├── archive/
│   ├── trial-lecture/
│   ├── ppt-experiments/
│   └── superseded-docs/
├── docs/
├── scripts/
├── .work/       # 不纳入 Git
└── .local/      # 不纳入 Git
```

### 3.1 目录职责

| 目录 | 职责 | Git 策略 |
| --- | --- | --- |
| `course/` | 课程大纲、考核、阶段交付、申请表底稿和学生模板等跨课次权威源 | 跟踪 |
| `lessons/` | 按课次组织现行讲义、教案、逐页内容母稿、当前 PPT 和教学资产 | 跟踪 |
| `deliverables/` | 已通过内容、教学、技术和视觉检查的正式发布物 | 跟踪里程碑版本 |
| `references/notes/` | 可追踪的参考资料分析、选目和核验记录 | 跟踪 |
| `references/library/` | PDF、书籍、外部 PPT、克隆仓库等原始资料 | 默认不跟踪 |
| `archive/` | 全部试讲内容、被替代文稿和有决策价值的 PPT 试制里程碑 | 试讲内容完整跟踪；其他历史材料选择性跟踪 |
| `.work/` | 渲染、解包、layout、QA、临时脚本环境和缓存 | 不跟踪 |
| `.local/` | 申请原件、外部数据链接、凭据相关本机配置 | 不跟踪 |

## 4. 现有目录迁移映射

| 当前路径 | 推荐路径或处理方式 |
| --- | --- |
| `ai-research-workflow-course/` | 迁到 `course/` |
| `projects/lesson-NN-*` | 按课次迁到 `lessons/lesson-NN/`，使用稳定的短文件名 |
| `projects/assets/lesson-NN/` | 迁到对应 `lessons/lesson-NN/assets/` |
| `projects/trial_lecture_*` | 全部试讲版本、内容源、讲述材料和判断记录迁到 `archive/trial-lecture/`，可重建生成过程进入 `.work/` |
| `final/` | 当前内容均为试讲历史材料，迁到 `archive/trial-lecture/`；不要继续用 `final` 表示历史稿 |
| `ref/*.md` | 按主题迁到 `references/notes/` |
| `ref/papers/`、`books/`、`talk/`、`template/`、`research-method/` | 迁到 `references/library/` 并继续忽略原始附件 |
| `ref/ppt-master-ppt-1-lesson-01/` | 只保留选定里程碑，其余工作文件不进入 `references/` |
| `docs/archive/` | 合并到 `archive/superseded-docs/`，避免多个 archive 根目录 |
| `applied/`、`data/`、`raw/`、`results/` | 迁到 `.local/` 或由 `.local/` 中的软链接统一管理 |
| `.tmp/`、`.ppt_master_inputs/` | 统一替换为 `.work/` |

实际迁移应优先使用 `git mv`，随后集中修复 Markdown 相对链接。未跟踪文件需要先分类，不能假设都可删除。

## 5. PPT 生命周期和输出规则

### 5.1 五类状态

| 状态 | 保存位置 | 保留内容 |
| --- | --- | --- |
| 内容源 | `lessons/lesson-NN/*.md` | 讲义、教案、逐页内容和来源说明 |
| 当前课件 | `lessons/lesson-NN/slides.pptx` | 唯一现行可编辑 PPT |
| 正式交付 | `deliverables/<term>/` | 已通过检查的 PPTX、必要 PDF 和交付索引 |
| 试制里程碑 | `archive/ppt-experiments/lesson-NN/` | PPTX、contact sheet、简短决策记录 |
| 临时产物 | `.work/ppt/<lesson>/<run>/` | 渲染图、XML、layout、检查日志、缓存和依赖 |

### 5.2 命名和版本

- 现行文件使用稳定名称，例如 `slides.md` 和 `slides.pptx`。
- 日常版本历史交给 Git，不继续保留 `v1`、`v2`、`v3`、`final-final` 等平行副本。
- 正式学期交付可使用 `deliverables/2026-fall/lesson-01-slides.pptx`。
- 试制里程碑使用日期和目的命名，例如 `archive/ppt-experiments/lesson-01/2026-08-05-keystone-layout/`。
- 完全相同的二进制文件只保留一个规范副本，通过索引指向，不重复复制。

### 5.3 里程碑保留标准

只有满足以下至少一项的试制稿才进入归档：

- 确立了后来沿用的视觉语言或版式规则；
- 记录了一次重要设计取舍及其失败原因；
- 是正式版本所依赖的可编辑基线；
- 为审批、试讲或教学复盘提供了不可由 Git 历史替代的证据。

每个里程碑最多保留：

1. 一份可编辑 PPTX；
2. 一张 contact sheet 或对比图；
3. 一份简短 Markdown 决策记录。

不归档逐页 PNG、解包 XML、重复 PDF、`node_modules`、inspection NDJSON、layout JSON、LibreOffice 临时目录或自动备份文件。

## 6. `AGENTS.md` 与 `CLAUDE.md`

### 6.1 权威关系

- `AGENTS.md` 恢复为普通 Markdown 文件，并作为唯一项目规则源。
- `CLAUDE.md` 是指向 `AGENTS.md` 的单向软链接。
- 不再分别维护两份内容，也不建立相互指向的链接。
- OpenCode 和 Codex 直接读取 `AGENTS.md`；Claude Code 通过 `CLAUDE.md` 读取相同规则。

### 6.2 `AGENTS.md` 应保留的内容

- 项目目标和当前阶段的简短说明；
- 权威文件和目录职责；
- 内容修改的同步关系；
- 正式材料、试讲材料和过程稿的边界；
- 参考资料与证据标准；
- 敏感目录、凭据和外部操作边界；
- 当前任务完成后的最低验证入口。

### 6.3 应移出的内容

- 详细课程定位和完整 16 课结构：放入 `course/` 的权威课程文档；
- PPT 排版和证据框细则：放入独立的课件规范；
- 当前课次进度：放入 `lessons/README.md`；
- 冗长的逐项检查表：放入验证脚本或 skill reference；
- 特定工具的个人配置和安装说明：放入用户级环境或 `docs/tooling.md`。

## 7. 项目级 Skill

建议只建立一个项目 skill：`prepare-course-lesson`。

```text
.agents/skills/prepare-course-lesson/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── material-contracts.md
    └── ppt-quality-gates.md
```

该 skill 负责：

1. 确认课次目标和上游课程口径；
2. 对齐讲义、教师教案和逐页内容母稿；
3. 执行内容门、90 分钟教学门和逐页映射门；
4. 只有前三道门通过后才进入 PPT 制作；
5. 调用已有 presentation/PPT 能力完成文件级工作；
6. 把所有构建过程限定在 `.work/`；
7. 对最终 PPT 重新打开或重新渲染，记录技术、教学和视觉检查结果；
8. 按里程碑标准决定哪些试制结果可以归档。

设计要求：

- `SKILL.md` 保持精简，只包含触发条件、核心流程和资源路由；
- 详细材料契约和 PPT 检查规则放在 `references/`，避免与 `AGENTS.md` 重复；
- 不把学校模板、论文原图或正式 PPT 复制进 skill；这些仍属于项目资产或参考资料；
- 暂不放入构建脚本。确定出现稳定、重复且适合自动化的步骤后，再增加经过测试的脚本；
- 使用 `skill-creator` 提供的校验工具检查 frontmatter、目录名和 `agents/openai.yaml`；
- Codex 与 OpenCode直接读取 `.agents/skills/`，Claude Code 通过 `.claude/skills/` 的单向链接复用同一份 skill。

## 8. MCP 建议

### 8.1 项目策略

当前不建议在仓库根目录提交 `.mcp.json`：

- 备课的核心工作主要是本地文档、PPT、参考资料和 Git 操作，不依赖共享 MCP 服务；
- 三个 Agent 客户端的 MCP 配置格式和凭据处理不同，项目内同时维护容易漂移；
- 当前用户级配置已经覆盖 Zotero 等能力；
- MCP 配置很容易把绝对路径、账号信息或密钥带入仓库。

可以在 `docs/tooling.md` 中只记录能力契约：

| 能力 | 建议状态 | 用途 |
| --- | --- | --- |
| Zotero | 可选、推荐 | 检索本地文献库、导出引用和核对全文 |
| GitHub | 按需 | 只有需要 issue、PR 或远端仓库操作时启用 |
| Context7 | 非项目依赖 | 可用于核对易变的软件文档，但不参与课程事实来源管理 |
| PPT/Office 本地工具 | 必需 | 渲染、重新打开和视觉检查；不需要 MCP |

### 8.2 当前环境清理

- 修复或禁用当前连接失败的 GitHub MCP，避免同时保留两套用途重叠的 GitHub 服务。
- 不在命令参数中放置 API key；迁移到环境注入、Keychain 或客户端支持的凭据存储。
- 轮换已经通过命令参数暴露的现有凭据。
- 不把用户级 MCP 配置、插件缓存或绝对路径复制进本仓库。
- 若以后为课堂演示提供 MCP 配置，应放在独立示例目录，只提交使用环境变量占位符的示例，不提交真实值。

## 9. 分阶段迁移方案

### 阶段 0：建立安全基线

1. 导出现有 tracked、modified、untracked、ignored 文件清单。
2. 对所有 PPT/PPTX 计算哈希，标出完全重复文件。
3. 将文件分类为现行、正式交付、里程碑、历史文档、临时产物、外部原件和敏感本地文件。
4. 经人工确认后建立专用重整分支和安全检查点；不得自动提交敏感或本应忽略的文件。

### 阶段 1：先止血

1. 修复 `AGENTS.md` 与 `CLAUDE.md` 的循环链接。
2. 增加根 `README.md`，说明项目入口、权威文件、目录职责和当前状态。
3. 扩充 `.gitignore`，统一忽略 `.work/`、`.local/`、Office 临时文件、本地依赖和生成缓存。
4. 暂停产生新的根目录或 `projects/` 视觉试制文件。

### 阶段 2：迁移权威内容

1. 将课程设计迁到 `course/`。
2. 将第 1、2 课材料迁到各自课次目录。
3. 更新 `lessons/README.md` 的状态表。
4. 集中修复内部链接，并检查跨文档口径。

### 阶段 3：归档和去重

1. 将试讲材料迁到 `archive/trial-lecture/`。
2. 从现有 PPT 试制稿中选取少量里程碑。
3. 清除完全重复的规范副本之外的文件；非重复但无保留价值的过程稿依靠 Git 历史或本地归档恢复。
4. 将 PPT 工作台、渲染和解包结果移出 `references/`，后续统一写入 `.work/`。

### 阶段 4：Agent 工作流

1. 精简 `AGENTS.md`。
2. 创建并校验 `prepare-course-lesson` skill。
3. 增加最小的只读验证脚本。
4. 分别在 Codex、Claude Code 和 OpenCode 中做发现与触发测试。

## 10. 验收标准

完成重整后至少满足：

1. `AGENTS.md` 可直接读取，`CLAUDE.md` 只单向指向它，不存在软链接环。
2. 根 `README.md` 能在一分钟内说明项目目的、当前权威内容、正式交付位置和开始工作的入口。
3. 每次课只有一套现行讲义、教案、逐页内容母稿和当前 PPT。
4. `lessons/` 与 `deliverables/` 中不存在名称含 `trial-lecture`、试讲、`visual-sample`、`pilot` 或测试版本号的文件。
5. `.work/`、`.local/`、渲染目录、解包 XML、`node_modules` 和 inspection 文件不被 Git 跟踪。
6. 完全相同的 PPT/PPTX 不在多个目录重复保存。
7. 所有 Markdown 内部相对链接有效。
8. 课程大纲仍为 16 次课，正式提交仍只位于第 6、9、13、16 课，评分合计 100%，中英文课时均为 32。
9. 项目 skill 通过结构校验，并能在至少 Codex 和 Claude Code 中发现；OpenCode 在本机安装后补做运行时验证。
10. 仓库中不存在凭据、本机 MCP 配置、插件缓存或指向其他用户目录的绝对路径。

## 11. 风险与边界

- 当前工作区不是干净状态，任何实际迁移都必须保护现有用户改动。
- 目录重命名会产生大量链接修改，应分阶段提交，避免把内容修改和结构迁移混在同一提交。
- 二进制 PPT 的 Git 历史不适合逐页比较，因此归档前必须生成可快速审阅的 contact sheet 和决策记录。
- `ref/` 中的外部原件可能受许可或隐私约束，迁移时只改变本地组织方式，不擅自纳入 Git。
- 本机当前未发现可用的 OpenCode CLI；三端兼容设计已按其官方规则核验，但仍需要安装后的实际 smoke test。
- 本建议不授权删除、提交、推送或发布任何现有材料；这些操作应在清单确认后单独执行。
