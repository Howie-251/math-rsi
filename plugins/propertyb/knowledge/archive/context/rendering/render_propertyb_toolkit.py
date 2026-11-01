#!/usr/bin/env python3
"""Compose the three canonical wiki guides into one offline reader."""
import html
import json
import os
from pathlib import Path
import re
import tempfile

from render_propertyb33 import ROOT, aris, embed_math

SOURCE = ROOT / "PROPERTY_B_TOOLKIT.md"
OUTPUT = ROOT / "PROPERTY_B_TOOLKIT.html"
TRACE = ROOT / ".aris/traces/render-html/2026-10-14_toolkit-inline-math"
WIKI = ROOT / "research-wiki"


def sections(filename):
    raw = (WIKI / filename).read_text()
    parts = re.split(r"(?m)^## (.+)\n", raw)
    return [(parts[i], parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def relocate(text):
    anchors = {
        "research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md": "#math",
        "research-wiki/PROPERTY_B_RESEARCH_LESSONS.md": "#verification",
        "research-wiki/PROPERTY_B_FAILURE_ATLAS.md": "#failures",
    }

    def link(match):
        label, target = match.groups()
        if target.startswith(("https:", "http:", "#", "mailto:")):
            return match[0]
        path, sep, fragment = target.partition("#")
        resolved = (WIKI / path).resolve()
        relative = os.path.relpath(resolved, ROOT)
        href = anchors.get(relative, relative + (sep + fragment if sep else ""))
        return f"[{label}]({href})"

    return re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)", link, text)


def chapter(anchor, title, text):
    return f'<div id="{anchor}" class="chapter-anchor"></div>\n\n## {title}\n\n{text.strip()}\n'


def detail(anchor, title, body, kind):
    return (f'<details id="{anchor}" class="reader-detail {kind}">\n'
            f'<summary>{html.escape(title)}</summary>\n\n'
            f'{relocate(body)}\n\n</details>\n')


def compose():
    math = sections("PROPERTY_B_REUSABLE_LEMMAS.md")
    lessons = sections("PROPERTY_B_RESEARCH_LESSONS.md")
    failures = sections("PROPERTY_B_FAILURE_ATLAS.md")
    assert len(math) == 14 and len(lessons) == 10 and len(failures) == 16
    chunks = ["# 从三个下界阶段，提炼可复用的方法\n"]
    chunks.append('''
同一张超图的各个局部视图，必须满足共同约束。把这些约束保留下来，往往比继续增加锁点、扩大分类表更有价值。

<div class="status-strip"><span class="accepted">m(5) ≥ 33 · 已验收</span><span class="accepted">m(5) ≥ 34 · 已验收</span><span class="candidate">m(5) ≥ 35 · 完整纸面候选，端到端 Lean 待闭合</span></div>

本页将数学工具、验证经验与效率方法汇成一卷。12组引理和15项失败记录均在页内，点开条目即可阅读完整推导或案例；源码与原始证据保留链接。
''')
    chunks.append(chapter("overview", "一屏看懂：积累了什么", '''
<div class="layer-grid"><div class="layer-card"><span class="card-kicker">01 · 数学</span><h3>12组可复用工具</h3><p>假设、证明、源码与推广边界一起保存，下一轮有据可用。</p><a href="#math">阅读引理目录 →</a></div><div class="layer-card"><span class="card-kicker">02 · 验证</span><h3>从原对象回到原结论</h3><p>局部表、数值界和条件定理，都要接到真实超图的染色。</p><a href="#verification">查看完整连接 →</a></div><div class="layer-card"><span class="card-kicker">03 · 效率</span><h3>把时间花在未闭合处</h3><p>复用重证书，单独修轻接口；用实际剩余义务判断进度。</p><a href="#efficiency">查看实测经验 →</a></div></div>

### 四个最值得继续使用的机制

|机制|直观含义|对应引理|
|---|---|---|
|真实迹的恢复与增锁|“迹”记录一条边经过哪些锁点。换视角或增加锁点时，始终追踪同一批实际边。|[L4–L5](#lemma-4)|
|避锁配额与重叠修复|证明某些子族里必有足够坏边对；多个配额重叠时，避免把同一坏对重复使用。|[L6–L7](#lemma-6)|
|共享坏对的多个布局|同一批坏对不能在每个布局里任意换成最坏位置，因此联合分析可能得到更强的界。|[L8](#lemma-8)|
|共同块族的计数守恒|各个局部视图都来自一个共同对象；双计数可以说明它们无法同时落入特定坏型。|[L10](#lemma-10)|

### 证明需要接通的整条链

<div class="proof-chain" aria-label="证明连接：任意原始超图到原染色"><div><b>任意原始超图</b><small>对象与量词不变</small></div><span>→</span><div><b>实际局部数据</b><small>从同一 H 提取</small></div><span>→</span><div><b>完整覆盖</b><small>合法输入没有遗漏</small></div><span>→</span><div><b>严格界</b><small>真实事件与精确计数</small></div><span>→</span><div><b>原染色</b><small>每条边都含两色</small></div></div>

一个值得记住的例子：度数预算能证明，至多36边的点对覆盖五元超图仍不超过25点；但到35边时，25点中“必有六度点”的旧保证已经消失。归约可以复用，选点结构却需要重新获得。这里的35边是参数 M=35，与下界 m(5)≥35 对应的34边任务不同。
'''))
    math_intro = relocate(math[0][1])
    # The table becomes a direct index into the full in-page statements.
    math_intro = re.sub(r"(?m)^\|L(\d+)\|", lambda m: f"|[L{m[1]}](#lemma-{m[1]})|", math_intro)
    chunks.append(chapter("math", "数学工具：12组定理与引理", math_intro))
    for i, (title, body) in enumerate(math[1:-1], 1):
        chunks.append(detail(f"lemma-{i}", title, body, "lemma"))

    verification = '''
完整分类不只要求“保存的代表都通过”，还要求每个实际超图一定进入该分类，并且证书中的数确实对应真实事件。Lean 最终核对的是指定命题及其依赖；页面和论文里的文字仍需与该命题对照。
'''
    for index in (6, 8):
        title, body = lessons[index]
        verification += f"\n### {title.split('、', 1)[1]}\n\n{relocate(body)}\n"
    chunks.append(chapter("verification", "验证：接回原命题，而非停在局部证书", verification))

    efficiency = '''
### 已经测到的组织收益

|实际工作|已记录结果|可复用的经验|
|---|---|---|
|21点四锁，同域674型／70代表|673条非默认键的关联查询；数据4.22秒，完整kernel87.75秒|先改变内核容易归约的表示，再扩大核验规模。|
|925项、3618项重证书|分别152秒、357秒；随后轻量分派及实际wrapper约1–2秒|把重证书和轻接口分开，接口修改复用已验依赖。|

这些是对应任务的实测。旧慢运行被终止，不能计算精确加速倍数；1–2秒指复用证书后的轻接口核验。
'''
    for index in (7, 9):
        title, body = lessons[index]
        efficiency += f"\n### {title.split('、', 1)[1]}\n\n{relocate(body)}\n"
    chunks.append(chapter("efficiency", "效率：减少重复归约与无效等待", efficiency))

    chunks.append(chapter("method", "研究方法：先定位损失，再增加数学", "下面六节保留三轮研究的方法推导、具体参数差分及成功经验。"))
    for i, (title, body) in enumerate(lessons[:6], 1):
        chunks.append(detail(f"method-{i}", title, body, "method"))

    chunks.append(chapter("failures", "失败地图：15项具体案例与重试条件", "每项保存发生了什么、实际排除了什么，以及什么新条件值得再试。它们既包含数学反模型，也包含表示和构建成本的实例。"))
    for i, (title, body) in enumerate(failures[:-1], 1):
        chunks.append(detail(f"failure-{i}", title, body, "failure"))

    next_use = relocate(math[-1][1]) + "\n\n" + relocate(failures[-1][1])
    next_use += '''

### 来源与讨论

正文分别来自[通用引理目录](research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md)、[研究经验](research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)、[失败地图](research-wiki/PROPERTY_B_FAILURE_ATLAS.md)。这些 Markdown 保持规范来源，本页提供合并阅读。

Grok 与 Gemini 已围绕具体数学条件、推广边界和效率经验完成讨论；有效补审与逐项纠正见[审阅记录](context/propertyb-unified-lessons-20261014/REVIEW_RECONCILIATION.md)。它们读取源码和已有记录，没有执行新的 Lean 构建。本页呈现既有积累，35的完整 Lean 状态保持未闭合。

研究恢复入口：[下一轮使用指南](research-wiki/PROPERTY_B_NEXT_BOUND_PLAYBOOK.md)。成果阅读：[已验收的 m(5)≥34](M5_GE34.html) · [m(5)≥35候选与形式化进度](M5_GE35.html)。
'''
    chunks.append(chapter("reuse", "下一轮怎样复用", next_use))
    SOURCE.write_text("\n\n".join(chunks).strip() + "\n")
    return SOURCE


_template = aris.load_template


def toolkit_template(name):
    css = '''
:root { --bg:#f8f6ef; --ink:#182e32; --primary:#245b60; --accent:#a44724; --border:#d4d8cc; --border-soft:#e0e3d9; }
body { font-family:"Georgia","Songti SC","STSong",serif; font-size:17px; line-height:1.85; }
.layout { max-width:1480px; grid-template-columns:210px minmax(0,1fr); gap:48px; padding:48px 40px; }
header.hero { padding-bottom:28px; margin-bottom:24px; }
header.hero h1 { font-size:46px; line-height:1.28; max-width:880px; letter-spacing:-.02em; }
header.hero .subtitle { font-size:18px; }
main > p:first-of-type { font-size:23px; line-height:1.75; margin-bottom:22px; }
h2 { font-size:29px; margin-top:52px; }
strong { color:var(--ink); font-weight:700; }
.status-strip { display:flex; gap:10px; flex-wrap:wrap; padding:10px 0; margin:12px 0; font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; font-size:13px; }
.status-strip span { padding:7px 12px; border-radius:4px; border:1px solid #cad8cd; }
.status-strip .accepted { background:#eaf0e8; color:#2a513b; }
.status-strip .candidate { background:#f6ecdc; color:#79501f; border-color:#e6d7bc; }
.layer-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px; margin:24px 0 34px; }
.layer-card { border-top:3px solid var(--primary); background:#efeee5; padding:20px; }
.card-kicker { font:12px -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; color:var(--accent); letter-spacing:.07em; }
.layer-card h3 { margin:14px 0 10px; color:var(--ink); font-size:20px; }
.layer-card p { font-size:15px; line-height:1.8; }
.layer-card a { font-size:14px; text-decoration:none; }
.proof-chain { display:flex; align-items:stretch; gap:6px; margin:24px 0; }
.proof-chain > div { flex:1; min-width:0; background:#e9eeea; border:1px solid #cddbd4; padding:14px 8px; text-align:center; border-radius:4px; }
.proof-chain > span { align-self:center; color:var(--primary); }
.proof-chain b { font-size:14px; display:block; }
.proof-chain small { display:block; font-size:11px; color:var(--ink-soft); margin-top:5px; }
details.reader-detail { background:#fffef9; border:1px solid var(--border); border-radius:5px; margin:12px 0; scroll-margin-top:24px; }
details.reader-detail summary { padding:18px 22px; font-weight:600; font-size:18px; color:var(--ink); cursor:pointer; }
details.reader-detail[open] { padding:0 24px 22px; }
details.reader-detail[open] > summary { margin:0 -24px 18px; border-bottom:1px solid var(--border-soft); background:#f0f2e9; }
details.reader-detail:target { border-color:var(--primary); box-shadow:0 0 0 2px #245b6020; }
details.failure > summary { border-left:3px solid #aa7355; }
main table { font-size:15px; min-width:580px; }
main code { font-size:12px; }
main .table-scroll { padding-bottom:4px; }
nav.toc { font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; font-size:13px; line-height:1.8; }
nav.toc ol li { margin:12px 0; }
@media (max-width:950px) { .layout { grid-template-columns:170px minmax(0,1fr); gap:26px; padding:30px 24px; } .layer-grid { grid-template-columns:1fr; } .layer-card { padding:16px 20px; } .proof-chain { flex-wrap:wrap; } .proof-chain > div { flex-basis:27%; } }
@media (max-width:700px) { .layout { display:block; padding:22px 18px; } header.hero h1 { font-size:31px; } main > p:first-of-type { font-size:20px; } h2 { font-size:25px; } .status-strip { gap:8px; } .status-strip span { font-size:12px; } .proof-chain { display:grid; grid-template-columns:1fr; gap:3px; } .proof-chain > div { text-align:left; padding:9px 15px; } .proof-chain b { font-size:15px; } .proof-chain small { margin:0; } .proof-chain > span { justify-self:center; transform:rotate(90deg); } details.reader-detail summary { padding:15px; font-size:16px; } details.reader-detail[open] { padding:0 16px 16px; } details.reader-detail[open] > summary { margin:0 -16px 14px; } }
'''
    return _template(name).replace("</style>", css + "</style>", 1)


def main():
    TRACE.mkdir(parents=True, exist_ok=True)
    source = compose()
    aris.load_template = toolkit_template
    with tempfile.TemporaryDirectory(prefix="propertyb-toolkit-", dir=ROOT) as tmp:
        stage = Path(tmp) / "reader.html"
        aris.main([str(source), "--out", str(stage), "--template", "academic",
                   "--title", "从三个下界阶段，提炼可复用的方法",
                   "--eyebrow", "PROPERTY B · 33 / 34 / 35 候选",
                   "--subtitle", "数学引理 · 证明验证 · Lean 与研究效率",
                   "--lang", "zh-CN"])
        report = embed_math(stage, OUTPUT, source)
    (TRACE / "math-build.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Rendered {OUTPUT}; {report['math']} embedded formulas; {report['tables']} tables.")


if __name__ == "__main__":
    main()
