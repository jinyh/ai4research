# 课程网站（web/）

“智能科研方法”学生门户，沿用 MkDocs Material。五个入口：首页、16 讲课程、项目与考核、模板与资源、课程信息。

## 内容职责

- `docs/learn/01.md` 至 `16.md`：简短课堂入口，说明任务、输入、步骤、最低产出和样例；不是第二套讲义或研究门。
- `course/` 与 `lessons/`：课程规则和完整讲义的唯一内容源。通过白名单软链接引入，保留原网址。
- `docs/project.md`：提交入口。评分维度与比例、四个研究门完整条件由 `student_view.py` 构建时直接读取权威文件；不手抄门条件。
- `docs/index.md`、`teacher.md`、`templates.md`：首页、课程信息、模板与资源。
- `docs/stylesheets/course.css`：交大红、正文层级、窄屏表格与阅读宽度。

更新讲义的课堂最低产出或下一课输入时，同步复核对应 `docs/learn/NN.md`；网页入口不新增实践、必读或正式提交。

## 本地预览与验证

```sh
cd web
uv sync --frozen
uv run python scripts/link_content.py
uv run python -m unittest discover -s tests -v
uv run mkdocs build --strict
uv run python scripts/check_site.py
uv run mkdocs serve
```

预览地址由终端给出，默认为 http://127.0.0.1:8000 。构建输出在 `web/_build/`，不纳入 Git。依赖沿用锁文件，本轮未增加包。

仓库级检查：

```sh
web/.venv/bin/python scripts/check_course_consistency.py
web/.venv/bin/python scripts/check_links.py
```

## 发布边界

发布清单在 `scripts/link_content.py` 的 `PUBLISH` 字典，逐文件登记学生材料；`docs/course/` 与 `docs/lessons/` 为生成软链接，勿手改或整体加入 Git。

- 内部版本、变更记录和备课门控标签在网页中隐藏；正文中的虚构身份、证据状态、许可和风险说明保留。
- 讲义标题前仍标草稿、待教师复核或阻塞时，构建只输出待复核提示及任务链接，草稿正文不进入 HTML 或搜索。
- 当前第 16 讲详细讲义继续待复核，任务入口仅列已确认的展示与提交要求。教师确认后同步更新入口、导航状态与发布测试。
- 第 1 课材料包只展示学生内容，教师纸面验收节不发布。
- 已知内部资料链接显示“未公开；请查对应公开来源”；未发布的学生材料链接使构建失败，不再静默变成普通文字。
- 教案、逐页母稿、PPT、历史试讲、未公开原始资料和凭据不在发布清单内。

## 本轮验收（2026-09-12）

16 讲入口分别约 300–420 个非空白字符；第 1–15 讲完整讲义继续可查。首页正文由 751 减至 304 个非空白字符，课程信息由 1794 减至 405。90 分钟教案与 PPT 未改制；修正第 8 课任务权威文件遗漏的五段陈述口径，课堂计时仍由教师教案维护。

严格构建、12 项学生页回归测试、63 个 HTML 页面的实际内部链接与锚点检查、12 项课程一致性检查通过；188 个受管 Markdown 无断链，保留一条历史外部 PDF 缺失告警。网页短标题只用于入口导航，正式课名仍以课程大纲为准。

已检查桌面首屏、代表课次、中文搜索、研究门条件展开、草稿旧网址；窄屏通过本机 390 px 页面容器检查。真实手机、Safari/Windows 与上线后的路径仍需发布前复核。本轮不将这些未覆盖环境登记为通过。

## 部署

现有 `.github/workflows/deploy-web.yml` 在 `main` 推送或手动触发时构建并部署 GitHub Pages。流程在上传前运行严格构建、学生页回归测试与生成站点检查。

本地修改不会自动上线；没有明确发布授权时，不提交、推送或触发部署。
