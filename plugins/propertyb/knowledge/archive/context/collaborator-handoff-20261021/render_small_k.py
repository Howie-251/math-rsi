#!/usr/bin/env python3
"""Compose four unchanged collaborator proofs and embed their SVG math offline."""
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "context/rendering"))
from render_propertyb33 import aris, embed_math

SOURCES = [
    ("k6", "k=6：m(6)≥65", ROOT / "propertyB_small_k/propertyB_m6_proof.md"),
    ("k7", "k=7：m(7)≥130", ROOT / "propertyB_small_k/propertyB_m7_proof.md"),
    ("k8-9", "k=8,9：m(8)≥266、m(9)≥542", ROOT / "propertyB_small_k/propertyB_k8_k9_proof.md"),
    ("k10-11", "k=10,11：m(10)≥1112、m(11)≥2275", ROOT / "propertyB_small_k/propertyB_k10_k11_research.md"),
]
SOURCE = ROOT / "PROPERTY_B_SMALL_K_6_11.md"
OUTPUT = ROOT / "PROPERTY_B_SMALL_K_6_11.html"

INTRO = """# Property B：合作者 k=6…11 原稿合卷

本卷完整收入合作者提供的四份证明 Markdown，依原次序逐字保留，未改写原定理、证明、公式或作者的状态说明。方法与原始证明保留合作者归属；本项目此前完成了源码阅读和原算术证书重放，本次只制作离线阅读视图。

四稿都面向任意有限简单 k 元超图；点对覆盖、点数窗口和选锁条件由证明内部推出。数值分别为 m(6)≥65、m(7)≥130、m(8)≥266、m(9)≥542、m(10)≥1112、m(11)≥2275。它们是纸面归约加精确有限局部算术的计算机辅助证明候选，原证书合计103190型已在本机重放通过；本卷不新增全链独立验收、跨家族审阅、Lean证明或公开纪录认证。两份k10/11最紧双锁型另有独立Fraction复算，其余全量第二实现未完成。

| 参数 | 原证书重放型数 | 完整原稿 |
|---|---:|---|
| k=6 | 200 | [propertyB_m6_proof.md](propertyB_small_k/propertyB_m6_proof.md) |
| k=7 | 115 | [propertyB_m7_proof.md](propertyB_small_k/propertyB_m7_proof.md) |
| k=8、9 | 1290、2568 | [propertyB_k8_k9_proof.md](propertyB_small_k/propertyB_k8_k9_proof.md) |
| k=10、11 | 28545、70472 | [propertyB_k10_k11_research.md](propertyB_small_k/propertyB_k10_k11_research.md) |

[复算与状态说明](context/collaborator-handoff-20261021/SMALL_K_GUIDE.md)给出可移植命令、完整依赖和各项核验边界；[既有阅读与重放总览](research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)连接实际日志。k10/11验证器须与certified模块一起运行，已解包副本随材料提供。原稿中的日期、待审阅说明与探索段保持原貌。

本页公式为内嵌SVG，打开阅读无需联网。导航：[k6](#original-k6) · [k7](#original-k7) · [k8/9](#original-k8-9) · [k10/11](#original-k10-11)。

"""


def main():
    snapshots = {str(path): path.read_text() for _, _, path in SOURCES}
    pieces = [INTRO]
    for key, title, path in SOURCES:
        original = snapshots[str(path)]
        pieces += [
            f'<div id="original-{key}" class="chapter-anchor"></div>\n\n',
            f"## 合作者原稿：{title}\n\n",
            f"来源：[{path.name}]({path.relative_to(ROOT).as_posix()})。以下为原稿全文。\n\n",
            original,
            "\n\n",
        ]
    combined = "".join(pieces)
    for original in snapshots.values():
        assert original in combined
    SOURCE.write_text(combined)
    with tempfile.TemporaryDirectory(prefix="small-k-reader-", dir=ROOT) as temporary:
        stage = Path(temporary) / "proof.html"
        aris.main([
            str(SOURCE), "--out", str(stage), "--template", "academic",
            "--title", "Property B：合作者 k=6…11 原稿合卷",
            "--eyebrow", "PROPERTY B · COLLABORATOR PROOFS",
            "--subtitle", "四份完整原稿 · 精确证书重放范围 · 离线公式",
            "--lang", "zh-CN",
        ])
        report = embed_math(stage, OUTPUT, SOURCE)
    for _, _, path in SOURCES:
        assert path.read_text() == snapshots[str(path)]
    report.update(
        source=str(SOURCE.relative_to(ROOT)),
        output=str(OUTPUT.relative_to(ROOT)),
        source_blocks=[dict(path=str(path.relative_to(ROOT)), bytes=path.stat().st_size,
                            preserved_verbatim=True) for _, _, path in SOURCES],
        original_files_unchanged=True,
        scope="Rendering and unchanged source composition only; fresh fidelity review arranged separately.",
    )
    (HERE / "small_k_render.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(OUTPUT), "math": report["math"],
                      "bytes": OUTPUT.stat().st_size, "all_originals_verbatim": True}, ensure_ascii=False))


if __name__ == "__main__":
    main()
