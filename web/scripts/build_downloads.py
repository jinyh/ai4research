"""将明确发布的阅读卡文件打包，下载后可独立运行。"""

from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from mkdocs.exceptions import PluginError

REPO = Path(__file__).resolve().parents[2]
PACKAGE = "lessons/lesson-11/assets/reading-card-workflow"
FILES = ("sources.json", "outputs.json", "gold.json", "annotations.json",
         "config.json", "run.py", "test_workflow.py")
README = """# 阅读卡回放包

源文本、输出和参考标注均为教学构造，不调用模型。
需要 Python 3，无第三方依赖。在解压后的本目录打开终端：

    python3 run.py replay --out runs/demo --fault-once
    python3 run.py replay --out runs/demo
    python3 run.py evaluate --out runs/demo
    python3 run.py access-check --out runs/demo --role executor --resource gold

预期退出码依次为 2、0、0、3。首次受控失败与末步权限拒绝均为预设分支。
每次新复演使用新的输出目录；不要覆盖以前的记录。
阅读卡遗漏 3/8=0.375，自由摘要 4/8=0.500；T02 无改善、T03 负向。
接口角色检查不等于操作系统沙箱。语义由人核验，程序只核查记录与汇总。

运行 python3 test_workflow.py 可验证包的关键行为。
完整说明：https://jinyh.github.io/ai4research/materials/reading-card/
"""


def on_pre_build(config, **_kwargs):
    # 清单是发布边界：不得递归收集目录、运行产物或本机文件。
    from importlib.util import spec_from_file_location, module_from_spec
    spec = spec_from_file_location("site_publish_list", REPO / "web/scripts/link_content.py")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    output = Path(config["docs_dir"]) / "downloads/reading-card-workflow.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    content = {"README.md": README.encode("utf-8")}
    for name in FILES:
        relative = f"{PACKAGE}/{name}"
        if relative not in module.PUBLISH:
            raise PluginError(f"下载包文件未获发布清单登记：{relative}")
        content[name] = (REPO / relative).read_bytes()
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for name, data in sorted(content.items()):
            info = ZipInfo(f"reading-card-workflow/{name}", date_time=(2026, 9, 16, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    build_rsi_download(config, module.PUBLISH)
    build_judgment_downloads(config, module.PUBLISH)


RSI_PACKAGE = "lessons/lesson-11/assets/rsi-selection-case"
RSI_FILES = ("README.md", "config.json", "run.py", "test_case.py", "plot.py", "source-audit.json",
             "figures/selection-diagnosis.png", "recorded/config.json", "recorded/raw-counts.csv",
             "recorded/results.csv", "recorded/summary.json", "recorded/manifest.json")


def build_rsi_download(config, publish):
    """Only explicit student files; never collect teacher notes or run folders."""
    output = Path(config["docs_dir"]) / "downloads/rsi-selection-case.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for name in RSI_FILES:
            relative = f"{RSI_PACKAGE}/{name}"
            if relative not in publish:
                raise PluginError(f"RSI 下载文件未获发布清单登记：{relative}")
            info = ZipInfo(f"rsi-selection-case/{name}", date_time=(2026, 10, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            data = (REPO / relative).read_bytes()
            if name == "README.md":
                # Repository links become web links in the standalone student package.
                base = config.get("site_url", "https://jinyh.github.io/ai4research/").rstrip("/")
                text = data.decode("utf-8").replace("../../../lesson-13/evaluation-report-template.md", base + "/lessons/lesson-13/evaluation-report-template/")
                data = text.replace("../../../../course/assessment.md", base + "/course/assessment/").encode("utf-8")
            archive.writestr(info, data)


# Explicit files only: teacher judgments, notes and authoring material never enter a ZIP.
JUDGMENT_FILES = (
    "course/judgment-path.md",
    "course/source-starter-pool.md",
    "course/micro-project.md",
    "lessons/lesson-01/judgment-task.md",
    "lessons/lesson-02/judgment-task.md",
    "lessons/lesson-03/judgment-task.md",
    "lessons/lesson-04/judgment-task.md",
    "lessons/lesson-05/judgment-task.md",
    "lessons/lesson-06/judgment-task.md",
    "lessons/lesson-07/judgment-task.md",
    "lessons/lesson-08/judgment-task.md",
    "lessons/lesson-09/judgment-task.md",
    "lessons/lesson-10/judgment-task.md",
    "lessons/lesson-11/judgment-task.md",
    "lessons/lesson-12/judgment-task.md",
    "lessons/lesson-13/judgment-task.md",
    "lessons/lesson-14/judgment-task.md",
    "lessons/lesson-15/judgment-task.md",
    "lessons/lesson-16/judgment-task.md",
    "lessons/lesson-03/assets/search-diagnosis/README.md",
    "lessons/lesson-03/assets/search-diagnosis/index.json",
    "lessons/lesson-03/assets/search-diagnosis/search.py",
    "lessons/lesson-10/assets/micro-project/README.md",
    "lessons/lesson-10/assets/micro-project/baseline.py",
    "lessons/lesson-10/assets/micro-project/inputs.json",
    "lessons/lesson-10/assets/micro-project/reference.json",
    "lessons/lesson-10/assets/micro-project/run.py",
    "lessons/lesson-10/assets/micro-project/test_runner.py",
)
MICRO_PREFIX = "lessons/lesson-10/assets/micro-project/"
SEARCH_PREFIX = "lessons/lesson-03/assets/search-diagnosis/"


def build_judgment_downloads(config, publish):
    import re
    import posixpath
    output = Path(config["docs_dir"]) / "downloads"
    output.mkdir(parents=True, exist_ok=True)
    bundles = {
        "judgment-tasks.zip": ("", JUDGMENT_FILES),
        "micro-project.zip": (MICRO_PREFIX, tuple(p for p in JUDGMENT_FILES if p.startswith(MICRO_PREFIX))),
        "search-diagnosis.zip": (SEARCH_PREFIX, tuple(p for p in JUDGMENT_FILES if p.startswith(SEARCH_PREFIX))),
    }
    for filename, (prefix, files) in bundles.items():
        with ZipFile(output / filename, "w", compression=ZIP_DEFLATED) as archive:
            for relative in files:
                if relative not in publish:
                    raise PluginError(f"判断任务下载未获发布清单登记：{relative}")
                data = (REPO / relative).read_bytes()
                if relative.endswith(".md"):
                    def resolve_link(match):
                        label, target = match.groups()
                        if re.match(r"(?:[a-z]+:|#)", target):
                            return match.group(0)
                        clean, sep, fragment = target.partition("#")
                        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(relative), clean))
                        if resolved in files:
                            return match.group(0)
                        if resolved in publish:
                            base = config.get("site_url", "https://jinyh.github.io/ai4research/").rstrip("/")
                            urlpath = publish[resolved].removesuffix(".md") + ("/" if resolved.endswith(".md") else "")
                            return f"[{label}]({base}/{urlpath}{sep}{fragment})"
                        raise PluginError(f"任务下载含未登记相对链接：{relative} -> {target}")
                    data = re.sub(r"\[([^]\n]+)\]\(([^)\n]+)\)", resolve_link, data.decode("utf-8")).encode("utf-8")
                name = relative[len(prefix):] if prefix else relative
                info = ZipInfo(name, date_time=(2026, 10, 12, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
