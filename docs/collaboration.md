# 双引擎协作规范

> 从 `AGENTS.md` 抽取。Claude Code、Codex、OpenCode 三端协作时遵循本规范。

- 每个任务指定一个主执行者，另一个引擎用于事实核验、教学逻辑审查或跨文档一致性复核。
- 不按"Claude 只写内容、Codex 只做技术"硬编码分工；根据任务和可验证性选择主执行者。
- **PPTX 制作（正式 PPT 构建、视觉调整、三重检查返工）由 Codex / Claude Code 执行；OpenCode / OpenChamber 不做 PPTX**。OpenCode/OpenChamber 在 PPT 环节的边界是内容母稿（slides.md）、门控登记材料与验证脚本/数据。
- 两个引擎不得同时修改同一文件。并行任务应按课次、材料包或文件边界切分。
- 主执行者负责整合，复核者只报告问题或提交边界清晰的修改建议，避免相互覆盖。
- 引擎特有的个人 skill、plugin 和凭据配置留在用户级环境，不复制到项目中。
