#!/usr/bin/env python3
"""Compose the complete T34 prose proof and render a single offline volume."""
import argparse
import json
import re
import tempfile

from render_propertyb33 import ROOT, aris, embed_math

CHAPTERS = ROOT / "context/propertyb34-reader"
SOURCE = ROOT / "M5_GE35.md"
OUTPUT = ROOT / "M5_GE35.html"
TRACE = ROOT / ".aris/traces/render-html/2026-10-14_propertyb34-full"


def compose():
    intro = r'''# m(5) ≥ 35：完整自然语言证明

从任意有限五元超图出发，经过最小反例约化、真实局部结构与严格概率界，回到每条边都含两种颜色的染色。

<div class="proof-status"><strong>完整自然语言候选证明</strong><span>端到端 Lean 尚未完成；核验进度列于文末。</span></div>

本页完整展开原命题、公共引理和19—25点的全部证明分支。阅读正文无需跳转到其他 Markdown 文件；逐行算术证书与 Lean 源码作为补充资料保留。

<div class="proof-road"><a href="#reduction"><b>01 · 缩小反例</b><span>任意有限顶点集 → 19—25点</span></a><a href="#probability"><b>02 · 建立染色判据</b><span>真实迹、联合计数、坏对扣除</span></a><a href="#v19"><b>03 · 处理全部分支</b><span>实际选点、完整分类、共同约束</span></a><a href="#conclusion"><b>04 · 回到原命题</b><span>排除所有反例，得到染色</span></a></div>

快速定位：[19点](#v19) · [20点](#v20) · [21点](#v21) · [22点](#v22) · [23点](#v23) · [24点](#v24) · [25点](#v25) · [Lean状态](#lean-status)。
'''
    files = ["CHAPTER_FOUNDATIONS.md", "CHAPTER_19_21.md", "CHAPTER_22_23.md",
             "CHAPTER_24_25.md", "CHAPTER_CONCLUSION.md"]
    contents = [intro]
    for filename in files:
        text = (CHAPTERS / filename).read_text()
        # All authored chapter links intentionally use the final project-root base.
        contents.append(text)
    text = "\n\n".join(contents)
    anchors = {
        "## 第一步：": "reduction", "## 公共概率工具：": "probability",
        "## 公共结构工具：": "structure", "### 19点：": "v19",
        "### 20点：最小度五或六": "v20", "### 21点：两个可反复使用": "v21",
        "## 二十二点：": "v22", "## 二十三点：": "v23",
        "## 二十四点：": "v24", "## 二十五点：": "v25",
        "## 回到原命题：": "conclusion", "## Lean 核验状态": "lean-status",
    }
    for prefix, anchor in anchors.items():
        text, count = re.subn(r"(?m)^(" + re.escape(prefix) + r".*)$",
                             lambda m: f'<div id="{anchor}" class="chapter-anchor"></div>\n\n{m[1]}',
                             text, count=1)
        if count != 1:
            raise ValueError(f"Missing chapter anchor: {prefix}")
    # Give the concrete supplemental certificates clickable paths, without
    # making any mathematical paragraph depend on an external Markdown page.
    evidence_dirs = [ROOT / "context/propertyb34/round01/high-math",
                     ROOT / "context/propertyb34-hour1-20261013/high-math"]
    def certificate_link(match):
        name = match[1]
        found = next((directory / name for directory in evidence_dirs
                      if (directory / name).is_file()), None)
        return f"[{name}]({found.relative_to(ROOT)})" if found else match[0]
    text = re.sub(r"`([A-Z][A-Z0-9_]+\.json)`", certificate_link, text)
    SOURCE.write_text(text.rstrip() + "\n")
    return SOURCE


_base_template = aris.load_template


def proof_template(name):
    css = '''
:root { --bg:#f8f6ef; --ink:#1b3034; --primary:#245b60; --accent:#9a4829; --border:#d4d8cc; --border-soft:#e1e4db; }
body { font-family:Georgia,"Songti SC","STSong",serif; font-size:17px; line-height:1.9; }
.layout { max-width:1500px; grid-template-columns:225px minmax(0,1fr); gap:44px; padding:42px 36px; }
header.hero h1 { font-size:44px; line-height:1.28; letter-spacing:-.02em; }
header.hero .subtitle { font-size:18px; line-height:1.7; }
h2 { margin-top:64px; padding-top:20px; border-top:2px solid #b9cbc4; font-size:29px; }
h3 { margin-top:38px; font-size:23px; line-height:1.5; }
h4 { margin-top:28px; font-size:20px; }
main > p:first-of-type { font-size:22px; line-height:1.8; }
main strong { color:var(--ink); }
main table { font-size:15px; }
main code { font-size:12px; }
.proof-status { display:flex; flex-wrap:wrap; gap:6px 20px; border-left:4px solid #ad8750; background:#f2eddf; padding:14px 18px; margin:22px 0; font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; font-size:14px; }
.proof-status span { color:#655b47; }
.proof-road { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:26px 0; }
.proof-road a { display:block; background:#eaf0ea; padding:16px 20px; border:1px solid #cfdcd3; border-radius:4px; text-decoration:none; }
.proof-road b { display:block; color:var(--primary); font-size:16px; }
.proof-road span { display:block; color:var(--ink); font-size:14px; margin-top:5px; }
nav.toc { font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; font-size:13px; line-height:1.6; }
nav.toc ol li { margin:11px 0; }
nav.toc ol li a { white-space:normal; }
@media(max-width:1000px) { .layout { grid-template-columns:185px minmax(0,1fr); gap:26px; padding:30px 24px; } }
@media(max-width:700px) { .layout { display:block; padding:22px 18px; } header.hero h1 { font-size:31px; } main > p:first-of-type { font-size:20px; } h2 { font-size:25px; margin-top:46px; } h3 { font-size:21px; } .proof-road { grid-template-columns:1fr; gap:8px; } .proof-road a { padding:12px 16px; } nav.toc ol li a { white-space:nowrap; } }
@media print { .proof-road { grid-template-columns:repeat(2,minmax(0,1fr)); } h2,h3,h4 { break-after:avoid; } }
'''
    return _base_template(name).replace("</style>", css + "</style>", 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--compose-only", action="store_true")
    args = parser.parse_args()
    source = compose()
    if args.compose_only:
        print(f"Composed {source}: {len(source.read_text())} characters")
        return
    TRACE.mkdir(parents=True, exist_ok=True)
    aris.load_template = proof_template
    with tempfile.TemporaryDirectory(prefix="propertyb34-reader-", dir=ROOT) as tmp:
        stage = __import__("pathlib").Path(tmp) / "proof.html"
        aris.main([str(source), "--out", str(stage), "--template", "academic",
                   "--title", "m(5) ≥ 35：完整自然语言证明",
                   "--eyebrow", "PROPERTY B · 34 条边 · T34",
                   "--subtitle", "原命题 · 公共引理 · 19—25点全部分支 · 严格概率界",
                   "--lang", "zh-CN"])
        report = embed_math(stage, OUTPUT, source)
    report["sourceCharacters"] = len(source.read_text())
    report["sourceChapters"] = [p.name for p in CHAPTERS.glob("CHAPTER_*.md")]
    (TRACE / "math-build.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Rendered {OUTPUT}: {report['math']} embedded formulas, {report['tables']} tables.")


if __name__ == "__main__":
    main()
