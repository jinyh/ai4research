---
name: prepare-course-lesson
description: 备课门控流程。当用户要制作或修订某课的讲义、教案、逐页内容母稿或课堂 PPT，或提到"备课""准备第 N 课""做课件""定稿 PPT"时使用。强制按内容门→90 分钟教学门→逐页映射门→PPT 制作→三重检查→里程碑归档的顺序推进，禁止跳过门控直接做 PPT。
---

# prepare-course-lesson

本 skill 是单次课备课的门控流程。它不替代内容创作，只在创作各阶段设通过条件，防止"未对齐口径就做 PPT""试制稿冒充正式课件""过程产物散落到工作区"。

## 触发条件

满足任一即进入本流程：

- 用户要求制作或修订某课的讲义、教师教案、逐页内容母稿（slides.md）或课堂 PPT。
- 用户说"备课""准备第 N 课""做课件""定稿 PPT""重新设计某页"。
- 已有课次材料需要对齐新的课程口径或 90 分钟结构。

## 核心流程

按下列顺序推进。每道门未通过不得进入下一道。

1. **确认课次目标**：在 `course/syllabus.md` 定位该课的目标与项目产出；在 `course/curriculum.md` 核对八阶段定位；在 `lessons/备课规划.md` 核对当前整改口径。明确该课不得引入的旧口径（见 `course/sync-rules.md`）。

2. **内容门**：对齐 `lessons/lesson-NN/handout.md`（学生讲义）、`teaching-plan.md`（教师教案）、`slides.md`（逐页内容母稿）。三份必须只有一套现行规则、案例与来源口径。通过条件见 `references/material-contracts.md`。

3. **90 分钟教学门**：做桌面推演，检查每段时间、第一次学生动手时间、最小课堂产出与备用路径。教师教案须含教学目标、时间分配、课堂活动、演示、形成性评价、课后复盘。

4. **逐页映射门**：每页写明页面任务、内容母稿位置、证据角色和学生动作。不以历史稿、试讲页或视觉样张为内容母版。

5. **PPT 制作**：前三道门通过后才制作正式 `slides.pptx`。调用已有 presentation/PPT 能力（全局 `ppt-master` skill 等）完成文件级工作。所有构建过程限定在 `.work/ppt/lesson-NN/<run>/`，不得在 `lessons/` 根目录产生 `visual-sample-*`、`v1/v2/v3` 平行文件。

6. **三重检查**：对最终 PPT 导出后重新打开或重新渲染，分别记录技术检查（图层遮挡、字体替换、裁切、换行、空 placeholder）、教学检查（页与母稿映射、学生动作）、视觉检查（视觉锚点、叙事关系、页型密度）。规则见 `course/ppt-quality-gates.md` 与 `lessons/ppt-design-criteria.md`。

7. **里程碑归档**：按 `archive/ppt-experiments/` 的标准（确立沿用视觉语言 / 记录重要取舍 / 正式版基线 / 不可由 Git 替代的证据）决定哪些试制结果归档。每个里程碑最多 1 PPTX + 1 contact sheet + 1 简短决策记录。不归档逐页 PNG、解包 XML、重复 PDF、inspection 文件。

## 修订已有课次

适用于已通过门控的课次做内容增改（加图、加案例、失败增补、文本清理、配套规范升版同步等，如 2.0 改版轮次）。在核心流程基础上按下列规则执行，并在课次 README 门控表新增"修订轮"登记（保留原门控记录不动）：

- **必须重走**：内容门（按 `references/material-contracts.md` 复核改动范围）；若动 `slides.md`，逐页映射门重走；若重建 `slides.pptx`，三重检查重走。
- **降级规则**：学习目标与时间结构不变 → 90 分钟教学门降级为复核（对照既有节奏表核对，不重做桌面推演）；不动 `slides.pptx` → PPT 制作与三重检查登记"未变更，原记录有效"；课次目标不变 → 课次目标门登记"复核通过"。
- **呈现增强**：handout 独增展示性结构图、出处块或清理表述口吻，且不改变三件套规则、案例与来源口径的，属呈现增强，内容门可带"推迟项清单"通过。
- **登记要求**：未到位的素材或未完成的改动（如待补的案例线）必须在课次 README 显式登记为"推迟项"，写明内容与补齐时机；不得静默遗漏。

## 资源路由

- 课程口径：`course/syllabus.md`、`course/curriculum.md`、`course/sync-rules.md`
- 备课元文档：`lessons/备课规划.md`、`lessons/备课教训.md`、`lessons/README.md`（含材料状态表与制作顺序）
- 材料契约：`references/material-contracts.md`
- PPT 规则：`course/ppt-quality-gates.md`（质量门）、`lessons/ppt-design-criteria.md`（正式课堂设计准则）
- 证据标准与安全边界：`AGENTS.md`
- 正式交付位置：`deliverables/<term>/`
- 临时产物位置：`.work/`（不纳入 Git）

## 边界

- 不用历史试讲 PPT 代替正式课堂 PPT。试讲材料在 `archive/trial-lecture/`，只用于评审与历史追踪。
- 不在 `lessons/` 或 `deliverables/` 产生名称含 `trial-lecture`、`visual-sample`、`pilot`、`v1/v2/v3`、`final` 的文件。
- 不提交 `.work/`、凭据或本机环境文件。
- 完成后先报告 diff、验证结果和剩余风险，不自动 commit 或 push。
