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
