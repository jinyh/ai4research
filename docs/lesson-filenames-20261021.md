# 课堂课件文件命名调整

版本：v1.0.0；日期：2026-10-21。

用户认可交付目录按课次命名，并要求其他文件一并调整。16课现行PPT由 `slides.pptx` 统一为 `lesson-NN.pptx`，现有L02旧PDF由 `slides.pdf` 改为 `lesson-02.pdf`。文件仍在原课次目录；逐页母稿 `slides.md` 不改名。L01–L03交付副本继续位于 `deliverables/2026-fall/`，其他课不因改名自动成为正式交付。

本次仅重命名二进制文件，16份PPT与1份PDF逐字节保持原内容，前后SHA256一致；16份PPT容器完整。关联Markdown链接、交付清单、命名规范和课程检查入口同步更新，历史原始证据与本机归档保持原名，正文指向现行文件的链接已更新。第4课原文件已在PowerPoint关闭后改名，没有保存或覆盖其他演示文稿。

| 课次 | 现行文件 | SHA256（改名前后相同） |
| --- | --- | --- |
| L01 | [lesson-01.pptx](../lessons/lesson-01/lesson-01.pptx) | `a55f143a194b6597b9f91737d5974a9571d93de057b1dc3a6b66b69946f6eaf8` |
| L02 | [lesson-02.pptx](../lessons/lesson-02/lesson-02.pptx) | `4a4d24a284197acab63cd7e079b7d68d3402a30ab014b52b67cd0ab88070863d` |
| L02 | [lesson-02.pdf](../lessons/lesson-02/lesson-02.pdf) | `e6603bfb7739035e007946aa3e0dc7122c59a35325ed849cab5e418a94f0ef10` |
| L03 | [lesson-03.pptx](../lessons/lesson-03/lesson-03.pptx) | `def6d3fd3362a815947c263f92a5c704ad23cec20e6f4c815919288f06ed3030` |
| L04 | [lesson-04.pptx](../lessons/lesson-04/lesson-04.pptx) | `885487e6bbb1d5dbd517f1385e1bc3cf1f55b5ad36664af21bfa1d2fe5a9d226` |
| L05 | [lesson-05.pptx](../lessons/lesson-05/lesson-05.pptx) | `05ccf732969f24c6d896a3bb1b496baf9242bfca99ef4dbd10b9f00f1b7b8673` |
| L06 | [lesson-06.pptx](../lessons/lesson-06/lesson-06.pptx) | `b1615ad9eaa30dd065bf69ba35b7690f4cbabb0805801acc18dbc180b3617119` |
| L07 | [lesson-07.pptx](../lessons/lesson-07/lesson-07.pptx) | `1bfacfda4c4ce3f76c8094fa6307969edc7323df09ba5fc131618123707655ce` |
| L08 | [lesson-08.pptx](../lessons/lesson-08/lesson-08.pptx) | `12c247605d22c259dc56120055455dd603abb44ee11abf4929d966b8a4f6c09f` |
| L09 | [lesson-09.pptx](../lessons/lesson-09/lesson-09.pptx) | `4ed522a61f3dde2d645525e1bd1563437d920a82f93ed8e0f3ffa352521b1b97` |
| L10 | [lesson-10.pptx](../lessons/lesson-10/lesson-10.pptx) | `4858f29a1a96dd819536b933c8557b19200364357860292258834e2e09a8f02e` |
| L11 | [lesson-11.pptx](../lessons/lesson-11/lesson-11.pptx) | `2c68dc8b688ab6d9aef8dd688a8f7d0006edfbc760b95e5517ec33c3b93c8b90` |
| L12 | [lesson-12.pptx](../lessons/lesson-12/lesson-12.pptx) | `dcc1b0ebe8a6b154f7a5337da2a6f3fd3d48e3cb3612fa15a7afc5f5fea22edc` |
| L13 | [lesson-13.pptx](../lessons/lesson-13/lesson-13.pptx) | `3ae42c8c6eaa1cc394a869ef61904d3a8d453d604ff736ce350f299918fab834` |
| L14 | [lesson-14.pptx](../lessons/lesson-14/lesson-14.pptx) | `4875714db659063b943cb8f61a282e0e72a9fbfe86eef6d249d1b310bbc017fb` |
| L15 | [lesson-15.pptx](../lessons/lesson-15/lesson-15.pptx) | `ec4ed1d7fa0b7f8f56dcec862254897b74dce6e1f57241242c1e7835b8ab0276` |
| L16 | [lesson-16.pptx](../lessons/lesson-16/lesson-16.pptx) | `0c967472c86e95d6932018298a8dd28739393d062067694ed003cb8c748231f5` |

L02 PDF为原有历史版本，不是本轮L01–L03的配套PDF；各课README的验收状态继续有效，本次不新增内容或现场通过结论。

命名规则：`lessons/lesson-NN/lesson-NN.pptx`（现行工作文件）；`deliverables/<term>/lesson-NN.pptx`（经授权的交付副本）；两处同一课次交付时需核对文件指纹。本轮输入快照与逐文件核对保存在 `.work/lesson-filenames-20261021.json`。未提交、推送或发布网站。

复验结果：12项课程一致性、246份Markdown内部链接与44项现有测试均通过；Git差异空白检查通过。改名后17个二进制文件指纹均保持不变，L01–L03交付副本与现行课件仍字节一致。第4课已从新路径重新在PowerPoint打开，确认32页及首张备注；未执行新的内容编辑。清理旧文件名留下的15份自动inspection缓存，其他轮工作目录未动。
