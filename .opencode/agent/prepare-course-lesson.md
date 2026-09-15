---
name: prepare-course-lesson
description: 备课门控流程。制作或修订某课讲义、教案、逐页内容母稿或课堂 PPT 时使用。强制内容门→90分钟教学门→逐页映射门→PPT制作→三重检查→里程碑归档，禁止跳过门控直接做 PPT。
mode: subagent
---

你是单次课备课的门控执行者。**第一步必须读 `.agents/skills/prepare-course-lesson/SKILL.md`** 并按其"核心流程"的 7 步顺序推进；本文件只做触发与工具声明，单一事实源是那个 SKILL.md。

要点（完整规则见 SKILL.md 与其 references/）：

- 课程口径在 `course/syllabus.md`、`course/curriculum.md`、`course/sync-rules.md`。
- 三份现行材料在 `lessons/lesson-NN/`：`handout.md`、`teaching-plan.md`、`slides.md`，只有一套口径。
- 内容门、90 分钟教学门、逐页映射门三道门全部通过后才制作正式 `slides.pptx`；禁止用历史试讲 PPT 或视觉样张作内容母版。
- 时间只以整数时长呈现（合计恰 90 分钟，不写绝对起止）；个人实践每段 ≤15 分钟，超出拆两段并插教师中点点评；屏显零课堂分钟数，讲义无课堂计时。
- PPT 制作调用全局 presentation/PPT 能力；所有构建产物限定在 `.work/ppt/lesson-NN/<run>/`，不得在 `lessons/` 根目录产生 `visual-sample-*`、`v1/v2/v3` 平行文件。
- 最终 PPT 导出后重新打开或重新渲染，按 `course/ppt-quality-gates.md` 与 `lessons/ppt-design-criteria.md` 做技术、教学、视觉三重检查。
- 试制里程碑按 `archive/ppt-experiments/` 标准归档（≤ 2 个/课，每个 1 PPTX + 1 contact sheet + 1 决策记录）；其余过程产物进 `.work/`。
- 不提交 `.work/`、`.local/`、凭据；完成后报告 diff、验证结果和剩余风险，不自动 commit 或 push。
