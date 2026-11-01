#!/usr/bin/env python3
"""Compose the general-bound sources and render one offline SVG reader.

The mathematical Markdown files remain canonical.  This script changes only
reader framing/heading levels and omits dated workflow-status paragraphs.
"""
import argparse
import base64
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import json
from math import factorial, isqrt
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit

from render_propertyb33 import ROOT, aris, embed_math

SOURCES = (
    ROOT / "proofs/propertyb-general/CORE_THEOREM.md",
    ROOT / "proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md",
    ROOT / "proofs/propertyb-general/CLIQUE_REFINEMENT.md",
    ROOT / "proofs/propertyb-general/BASELINE_COMPARISON.md",
)
COMPARISON_SOURCE = ROOT / "proofs/propertyb-general/LITERATURE_COMPARISON_TABLE.md"
FIGURE_SOURCE = ROOT / "proofs/propertyb-general/RESULTS_FIGURE.md"
DEFAULT_TRACE = ROOT / ".aris/traces/render-html/2026-10-21_propertyb-general"
MATH_PATTERN = re.compile(r"(?<!\\)\$\$(.*?)\$\$|(?<!\\)\$(?!\$)(.*?)(?<!\\)\$(?!\$)", re.S)


def math_inputs(text):
    return [(display or inline).strip() for display, inline in MATH_PATTERN.findall(text)]


def normalized_math_counter(inputs):
    return Counter(re.sub(r"\s+", "", formula) for formula in inputs)


# Keep multiline TeX opaque to the Markdown block parser.  In particular, a
# strict inequality at the start of a formula line must not become a quote.
# This changes whitespace only in the parser input, never the saved Markdown.
BASE_PREPARE_SOURCE = aris.strip_frontmatter


def prepare_reader_source(raw):
    text = BASE_PREPARE_SOURCE(raw)
    return re.sub(r"(?<!\\)\$\$(.*?)\$\$", lambda m: "$$" +
                  re.sub(r"\s*\n\s*", " ", m[1]).strip() + "$$", text, flags=re.S)

INTRO = r"""# 单交结构带来的统一整数增益

本文证明：对每个整数 $k\ge12$，由指定 RS 重染判据得到的整数可染预算可以统一增加一个显式的正整数。所有染色结论均适用于任意有限简单 $k$ 元超图。

<p class="proof-status">定理、引理与完整证明 · 文献引用按所列版本标注</p>

{{RESULTS_FIGURE}}

## 基本定义与文献基线

**定义（超图与Property B）。** 有限简单 $k$ 元超图是 $H=(V,E)$，其中 $V$ 有限，$E\subseteq\binom Vk$。若存在 $c:V\to\{0,1\}$ 使每条边均含两色，则称 $H$ 具有 Property B。$m(k)$ 表示不具有 Property B 的此类超图的最少边数。全文 $\log$ 为自然对数。

**定义（RS组合判据的整数预算）。** 对整数 $k\ge12$，令

$$
d_k=2^{k-1},\qquad a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

并定义

$$
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d_k^2}J_k(p)<a_k(p)^{M/d_k}\right\}.
$$

这个判据组合了 [Radhakrishnan–Srinivasan，Claim A.1，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)的正关联端项，以及 [Claim 2.4的证明，第7页的未编号积分](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)，再使用有向单交边对数至多 $M(M-1)$。**最大整数预算 $B_{\rm RS}$ 是本文据此定义的函数，原文没有直接定义这一记号或最大化量。** 两项估计在同一算法中的组合见[引理1](#core-lemma-1)；最大值非空、有限及 $2^k\le B_{\rm RS}(k)<k2^k$ 的证明见[引理B.4](#gain-lemma-b4)。

## 主定理：增长的整数增益

**定理C。** 设整数 $k\ge12$，并令

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

则 $\Delta(k)\ge2$。对任意有限集合 $V$ 和任意 $E\subseteq\binom Vk$，若

$$|E|\le B_{\rm RS}(k)+\Delta(k),$$

则存在 $c:V\to\{0,1\}$，使每条 $e\in E$ 满足 $\{c(x):x\in e\}=\{0,1\}$。因此

$$\boxed{m(k)\ge B_{\rm RS}(k)+1+\Delta(k).}$$

**证明。** [引理B.4](#gain-lemma-b4)给出最大预算及其严格参数见证。[引理C.1](#clique-lemma-c1)与[推论C.2](#clique-corollary-c2)在同一最小顶点反例上削减有向单交对数；[引理B.1](#gain-lemma-b1)的参数控制保证该削减吸收新增的 $\Delta(k)$ 条边。全部不等式及原超图染色结论的推导见下文[定理C的完整证明](#clique-theorem-c)。∎

旧组合判据本身给出 $m(k)\ge B_{\rm RS}(k)+1$。定理C在整个 $k\ge12$ 范围将该下界增加 $\Delta(k)$；它不改变领先的渐近阶。对全部 $k\ge12$ 的五项明确参考包络比较见[定理D](#comparison-theorem-d)，对 $k\ge256$ 的指定零锁必要数据测试方案的比较见[定理E](#comparison-theorem-e)。

{{LITERATURE_COMPARISON}}

{{GAIN_EXAMPLES}}

## 证明依赖

以下依次证明概率引理、最小反例结构、最大预算的良定性和整数增益。图中每个结点均对应正文中的已编号结果；点对覆盖和团界是证明内部推出的结论，不是主定理对原超图的附加假设。

<div class="proof-route"><div><b>引理1</b><span>实际重染失败上界</span></div><i>＋</i><div><b>引理2、3、C.1</b><span>最小反例与单交团</span></div><i>→</i><div><b>推论C.2</b><span>结构加强的可染判据</span></div><i>＋</i><div><b>引理B.1、B.4</b><span>参数控制与最大预算</span></div><i>→</i><div><b>定理C</b><span>统一的正整数增益</span></div></div>
"""


def examples(trace):
    path = ROOT / "context/propertyb-general/round02/examples/CONSERVATIVE_GAIN_EXAMPLES.json"
    if not path.exists():
        return ""
    data = json.loads(path.read_text())
    rows = [row for row in data["rows"] if row["k"] in (17, 32, 64)]
    for row in rows:
        k, upper = row["k"], row["log_upper"]
        partial = sum((Fraction(upper) ** j / factorial(j)
                       for j in range(row["exp_partial_terms_through"] + 1)), Fraction(0))
        assert partial == Fraction(row["exp_partial_sum"]) > k
        assert row["floor_sqrt_2k"] == isqrt(2 ** k)
        assert row["certified_increment_lower"] == isqrt(2 ** k) // (8 * (1 + upper))
    (trace / "example-check.json").write_text(json.dumps(
        {"status": "PASS", "source": str(path.relative_to(ROOT)), "rows": rows},
        ensure_ascii=False, indent=2) + "\n")
    body = "### 三个保守的增益例子\n\n"
    body += "只用后文证明的 $B_{\\rm RS}(k)\\ge2^k$，便得到以下增益下限；这里没有计算 $B_{\\rm RS}(k)$ 本身。\n\n"
    body += "|$k$|比较基线|至少增加|\n|---:|---|---:|\n"
    body += "\n".join(f"|{row['k']}|" + ("$B_{\\rm RS}(k)+1$" if row['k'] == 17 else "$L_{\\rm ref}(k)=B_{\\rm RS}(k)+1$") + f"|{row['certified_increment_lower']:,}|" for row in rows)
    body += "\n\n这些数字采用整数与有理数保守估计，帮助理解增益规模；整个参数范围的证明在下文，不由这些例子外推。\n"
    return body


def mathematical_body(text):
    """Drop only the original title and dated status paragraph."""
    position = text.index("\n## ")
    anchors = re.findall(r'<a id="[^"]+"></a>', text[:position])
    return ("\n".join(anchors) + "\n" + text[position + 1:]).strip()


def subordinate(text):
    return re.sub(r"(?m)^(#{2,3}) ", lambda m: "#" + m[1] + " ", text)


def relocate_links(text, source):
    def link(match):
        label, target = match.groups()
        if target.startswith(("https:", "http:", "#", "mailto:")):
            return match[0]
        # TeX can contain [expression](expression).  Only relocate file links.
        if not (target.startswith(("../", "./"))
                or re.search(r"\.(?:md|pdf|html|json|txt)(?:#|$)", target)):
            return match[0]
        section_targets = {"CORE_THEOREM.md": "core-theorem-a", "UNIFORM_INTEGER_GAIN.md": "gain-definition-brs", "CLIQUE_REFINEMENT.md": "clique-theorem-c", "BASELINE_COMPARISON.md": "comparison-theorem-d"}
        path, sep, fragment = target.partition("#")
        if path in section_targets:
            destination = fragment if sep else section_targets[path]
            return f"[{label}](#{destination})"
        relative = os.path.relpath((source.parent / path).resolve(), ROOT)
        return f"[{label}]({relative}{sep}{fragment})"
    return re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)", link, text)


def compose(snapshot, illustration):
    core = relocate_links(mathematical_body(snapshot[SOURCES[0].name]), SOURCES[0])
    core = core.split("\n## 与原始来源及研究目标的关系", 1)[0]
    gain = relocate_links(mathematical_body(snapshot[SOURCES[1].name]), SOURCES[1])
    gain = gain.replace(
        "本定理精确比较的是 (1) 指定的RS–FKG–精确积分整数界。其他文献中的离散位置、度数或共度加强，必须另行比较；不能因 (2) 已有候选证明就宣称超过它们或完成整个Goal。",
        "上述加一结论比较的是 (1) 指定的RS–FKG–精确积分整数界。",
    )
    clique = relocate_links(mathematical_body(snapshot[SOURCES[2].name]), SOURCES[2])
    clique = clique.replace("## 相对指定RS判据的增益候选", "## 相对指定RS判据的增长增益")
    clique = clique.replace(
        "新充分判据在预算 $N$ 成立。若所有连接和常数通过审计，即得到",
        "新充分判据在预算 $N$ 成立。取 $M=B_{\\rm RS}(k)$，由前节的最大预算存在性及加强后的定理A，得到",
    )
    clique = clique.replace(
        "这仍是相对指定旧RS精确判据的数学比较，不预先声称超过全部适用文献界；也不声称公共点二分这一标准式论证首创。",
        "这一比较保留同一个旧判据见证 $p$，由结构削减吸收新增 $s$ 条边的成本。",
    )
    baseline = relocate_links(mathematical_body(snapshot[SOURCES[3].name]), SOURCES[3])
    comparison = relocate_links(snapshot[COMPARISON_SOURCE.name].strip(), COMPARISON_SOURCE)
    figure = relocate_links(snapshot[FIGURE_SOURCE.name].strip(), FIGURE_SOURCE)
    pieces = [INTRO.replace("{{GAIN_EXAMPLES}}", illustration).replace("{{LITERATURE_COMPARISON}}", comparison).replace("{{RESULTS_FIGURE}}", figure),
              "## 一、一般二染色判据与完整原图连接\n\n" + subordinate(core),
              "## 二、旧预算的有限性与统一加一余量\n\n" + subordinate(gain),
              "## 三、公共点二分与增长的整数增益\n\n" + subordinate(clique),
              "## 四、参考界与有限测试方案的完整比较\n\n" + subordinate(baseline),
              r"""## 参考文献与核验资料

[RS2000] J. Radhakrishnan and A. Srinivasan. *Improved bounds and algorithms for hypergraph 2-coloring*. Random Structures & Algorithms **16**(1), 4–32, 2000. [作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)；[本地PDF](ref/radhakrishnan_srinivasan_2000_two_coloring.pdf)。所引算法、Lemma 2.1、Claims 2.1–2.4、Claim A.1及页码均依27页作者稿，页码不冒作期刊排版页码。

[CK2015] D. D. Cherkashin and J. Kozik. *A note on random greedy coloring of uniform hypergraphs*. Random Structures & Algorithms **47**(3), 407–413, 2015. [DOI](https://doi.org/10.1002/rsa.20556)。本文引用刊版§2式(2.1)–(2.3)，第409–410页。

[P2009] A. Pluhár. *Greedy colorings of uniform hypergraphs*. Random Structures & Algorithms **35**(2), 216–221, 2009. [DOI](https://doi.org/10.1002/rsa.20267)。准确排列概率见§2.1的Claim 1证明，作者稿第2–3页。

[GL2024] K. Grill and D. Linzmayer. *Improved Lower Bounds for Property B*. [arXiv:2403.05674v3](https://arxiv.org/abs/2403.05674v3), 20 June 2024. 本文使用§1式(3)–(5)、§2式(6)–(8)以及式(9)之后两条未编号的单交对上界。

本卷组合的四个规范来源是[一般充分判据](proofs/propertyb-general/CORE_THEOREM.md)、[统一整数加一](proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)、[团界加强与增长增益](proofs/propertyb-general/CLIQUE_REFINEMENT.md)、[参考界完整比较](proofs/propertyb-general/BASELINE_COMPARISON.md)。它们保持规范地位；本页与[Markdown阅读稿](PROPERTY_B_GENERAL_BOUND.md)提供完整合并阅读。各具体引用、版本和页码的核对记录见[文献定位](context/propertyb-general/formal-exposition-20261021/SOURCE_MAP.md)。

本文全部整数k≥12的增长主定理C已完成[端到端Lean形式证明](PROPERTY_B_GENERAL_LEAN.html)：最大预算、至少二的统一增益、实际反例结构、概率判据和原Bool染色均已连接；[独立原命题及公理审计](context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)已通过。比较定理D、E仍为本文所给的纸面证明。原[RS核心与17元试点](PROPERTY_B_GENERAL_LEAN_PILOT.html)保留为前一阶段记录。

交接与验证补充：[人工交接](HANDOFF_PROPERTYB_GENERAL.md)、[合并数学审计](context/propertyb-general/round02/formal-audit/COMBINED_AUDIT.md)、[核心审阅处置](context/propertyb-general/round02/reviews/CORE_DISPOSITION.md)、[比较审阅处置](context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md)。
"""]
    return "\n\n".join(pieces).strip() + "\n"


def verify_math_preserved(snapshot, composed):
    def formulas(text):
        return Counter(math_inputs(text))
    expected = Counter()
    for index, path in enumerate(SOURCES):
        body = mathematical_body(snapshot[path.name])
        if index == 0:
            body = body.split("\n## 与原始来源及研究目标的关系", 1)[0]
        expected.update(formulas(body))
    expected.update(formulas(snapshot[COMPARISON_SOURCE.name]))
    expected.update(formulas(snapshot[FIGURE_SOURCE.name]))
    actual = formulas(composed)
    missing = expected - actual
    assert not missing, dict(missing)
    return {"status": "PASS", "canonicalMathSnippets": sum(expected.values()),
            "readerMathSnippets": sum(actual.values()), "missingSnippets": []}


BASE_TEMPLATE = aris.load_template


def reader_template(name):
    template = BASE_TEMPLATE(name)
    template = re.sub(
        r'<footer class="aris-footer">[\s\S]*?</footer>',
        '<footer class="aris-footer">阅读稿：<a href="PROPERTY_B_GENERAL_BOUND.md">Markdown</a>'
        ' · 数学规范：<a href="proofs/propertyb-general/CORE_THEOREM.md">一般判据</a>'
        ' · <a href="proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md">整数加一</a>'
        ' · <a href="proofs/propertyb-general/CLIQUE_REFINEMENT.md">增长增益</a>'
        ' · <a href="proofs/propertyb-general/BASELINE_COMPARISON.md">参考界比较</a></footer>',
        template, count=1,
    )
    css = """
:root { --bg:#f8f6ef; --ink:#193034; --primary:#245b60; --accent:#a44724; --border:#d4d8cc; }
body { font-family:Georgia,"Songti SC","STSong",serif; font-size:17px; line-height:1.9; }
.layout { max-width:1440px; grid-template-columns:200px minmax(0,1fr); gap:48px; padding:44px 38px; }
header.hero h1 { font-size:44px; line-height:1.3; letter-spacing:-.02em; }
header.hero .subtitle { max-width:850px; font-size:17px; }
main > p:first-of-type { font-size:21px; line-height:1.8; margin-top:0; }
main h2 { font-size:28px; margin-top:52px; }
main h3 { font-size:22px; margin-top:34px; }
main h4 { font-size:18px; margin-top:28px; }
main table { min-width:0; font-size:15px; }
main table.comparison-table { min-width:1000px; }
main table.comparison-table th:first-child, main table.comparison-table td:first-child { min-width:150px; }
main p,main li { overflow-wrap:break-word; }
main mjx-container[display="true"] { margin:20px 0; background:#f0f1e9; border-left:3px solid #aabdb5; padding:18px 14px; border-radius:3px; }
main mjx-container:not([display="true"]) { overflow:visible; }
.proof-status { border-left:3px solid #ad8054; color:#71532f; font:14px/1.7 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; padding:10px 14px; background:#f2eadc; }
.bound-summary { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px; margin:26px 0; font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; }
.bound-summary > div { border-top:3px solid #c34a36; background:#f5eee5; padding:20px 20px 18px; }
.bound-summary > div:nth-child(2) { border-color:#8052a0; background:#f1edf6; }
.bound-summary > div:nth-child(3) { border-color:#246d9c; background:#edf3f7; }
.bound-summary strong { color:#c34a36; }
.bound-summary > div:nth-child(2) strong { color:#8052a0; }
.bound-summary > div:nth-child(3) strong { color:#246d9c; }
.bound-summary span,.bound-summary strong,.bound-summary small { display:block; }
.bound-summary span { font-size:13px; color:#596863; }
.bound-summary strong { font-size:21px; line-height:1.7; margin:7px 0; }
.bound-summary small { font-size:12px; color:#596863; }
.bound-plot { overflow-x:auto; margin:24px 0 16px; padding:4px 0; background:#f8f6ef; }
.bound-plot img { display:block; width:100%; min-width:600px; max-width:none; height:auto; }
.bound-overview img { min-width:760px; }
.bound-delta img { min-width:840px; }
.figure-mobile-hint { display:none; }
@media(max-width:1000px) { .bound-summary { grid-template-columns:1fr; } }
@media(max-width:700px) { .bound-summary strong { font-size:20px; } .figure-mobile-hint { display:block; font:13px/1.7 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; color:#536963; } }
.proof-route { display:flex; align-items:center; gap:6px; margin:24px 0; }
.proof-route > div { flex:1; min-width:0; background:#e9eeea; border:1px solid #cedad3; border-radius:4px; padding:13px 7px; text-align:center; }
.proof-route b { display:block; font:600 14px/1.5 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; }
.proof-route span { display:block; font:11px/1.6 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; margin-top:4px; color:#536963; }
.proof-route i { color:#52746d; font-style:normal; }
nav.toc { font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; font-size:13px; line-height:1.7; }
nav.toc ol li { margin:12px 0; }
footer.aris-footer { margin-top:60px; }
@media(max-width:950px) { .layout { grid-template-columns:165px minmax(0,1fr); gap:26px; padding:30px 24px; } }
@media(max-width:700px) { .layout { display:block; padding:22px 18px; } header.hero h1 { font-size:30px; } main > p:first-of-type { font-size:18px; } main h2 { font-size:25px; } main h3 { font-size:21px; } .proof-route { display:grid; grid-template-columns:1fr; gap:4px; } .proof-route i { justify-self:center; transform:rotate(90deg); } .proof-route > div { text-align:left; padding:9px 14px; } .proof-route span { margin:0; } main mjx-container[display="true"] { padding:14px 8px; } }
@media print { .proof-status { background:none; } .proof-route > div { background:none; } main h2 { break-after:avoid; } }
"""
    return template.replace("</style>", css + "</style>", 1)


def browser_check(output, trace, source, expected_math):
    from playwright.sync_api import sync_playwright
    result = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for label, width, height in [("desktop", 1440, 1000), ("phone", 390, 844)]:
            page = browser.new_page(viewport={"width": width, "height": height},
                                    device_scale_factor=1)
            requests = []
            page.route("http://**/*", lambda route: route.abort())
            page.route("https://**/*", lambda route: route.abort())
            page.on("request", lambda req: requests.append(req.url)
                    if req.url.startswith(("http:", "https:")) else None)
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(output.as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            checks = page.evaluate("""() => {
              const ids = new Set([...document.querySelectorAll('[id]')].map(n=>n.id));
              return {
                formulaCount:document.querySelectorAll('mjx-container').length,
                svgCount:document.querySelectorAll('mjx-container > svg').length,
                texInputs:[...document.querySelectorAll('mjx-container')].map(n=>n.dataset.tex),
                mathErrors:[...document.querySelectorAll('[data-mml-node="merror"],mjx-merror')].map(n=>n.textContent),
                scripts:document.scripts.length,
                externalAssets:[...document.querySelectorAll('script[src],link[href],img[src]')].map(n=>n.src||n.href).filter(x=>/^https?:/.test(x)),
                horizontalPageOverflow:document.documentElement.scrollWidth>innerWidth+1,
                brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].map(n=>n.getAttribute('href')).filter(h=>h.length>1&&!ids.has(decodeURIComponent(h.slice(1)))),
                localLinks:[...document.querySelectorAll('a[href]')].map(n=>n.getAttribute('href')).filter(h=>!/^https?:|^mailto:|^#/.test(h)),
                sourceHash:document.querySelector('meta[name="aris:source-sha256"]')?.content || null,
                statusNotes:document.querySelectorAll('.proof-status').length,
                headings:[...document.querySelectorAll('main h2')].map(n=>n.textContent),
                bodyHeight:document.documentElement.scrollHeight
              };
            }""")
            page.screenshot(path=str(trace / f"{label}-top.png"), full_page=False)
            checks["boundPlots"] = page.locator('.bound-plot img').evaluate_all(
                "nodes=>nodes.map(n=>({alt:n.alt,loaded:n.complete&&n.naturalWidth>0,embedded:n.src.startsWith('data:image/svg+xml;base64,')}))")
            assert len(checks["boundPlots"]) == 3 and all(n["loaded"] and n["embedded"] for n in checks["boundPlots"])
            for plot_name in ("delta", "small", "overview"):
                plot = page.locator(f'.bound-plot[data-figure="{plot_name}"]')
                plot.evaluate("el => { for (let p=el.parentElement;p;p=p.parentElement) if(p.tagName==='DETAILS') p.open=true; }")
                plot.scroll_into_view_if_needed()
                page.screenshot(path=str(trace / f"{label}-figure-{plot_name}.png"), full_page=False)
            page.locator('details').evaluate_all('nodes=>nodes.forEach(n=>n.open=false)')
            target = page.locator("#core-lemma-1")
            target.scroll_into_view_if_needed()
            page.screenshot(path=str(trace / f"{label}-proof.png"), full_page=False)
            comparison = page.get_by_role("heading", name="四、参考界与有限测试方案的完整比较", exact=True)
            if comparison.count():
                comparison.scroll_into_view_if_needed()
                page.screenshot(path=str(trace / f"{label}-comparison.png"), full_page=False)
                relaxation = page.locator("#comparison-definition-d2")
                relaxation.scroll_into_view_if_needed()
                page.screenshot(path=str(trace / f"{label}-relaxation.png"), full_page=False)
            checks["networkRequests"] = requests
            checks["pageErrors"] = errors
            tex = checks.pop("texInputs")
            # Compare against the unparsed Markdown, rather than MathJax's
            # already-parsed inputs, so a lost display cannot pass this gate.
            checks["mathInputsMatch"] = normalized_math_counter(tex) == normalized_math_counter(expected_math)
            checks["mathInputOrderMatches"] = [re.sub(r"\s+", "", item) for item in tex] == [
                re.sub(r"\s+", "", item) for item in expected_math]
            checks["sourceMathCount"] = len(expected_math)
            checks["missingSourceMath"] = list((normalized_math_counter(expected_math) -
                                                normalized_math_counter(tex)).elements())
            checks["missingLocalLinks"] = [href for href in checks["localLinks"]
                if not (output.parent / unquote(urlsplit(href).path)).exists()]
            result[label] = checks
            assert not checks["horizontalPageOverflow"], (label, "page overflow")
            assert not (checks["scripts"] or checks["externalAssets"] or requests or errors
                        or checks["mathErrors"] or checks["brokenAnchors"]), checks
            assert checks["formulaCount"] == checks["svgCount"] > 0
            assert checks["mathInputsMatch"] and checks["mathInputOrderMatches"] and not checks["missingLocalLinks"]
            assert checks["sourceHash"] == aris.sha256_of(source.read_text())
            assert checks["statusNotes"] == 1
            page.close()
        browser.close()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace-dir", type=Path, default=DEFAULT_TRACE)
    args = parser.parse_args()
    trace = args.trace_dir.resolve()
    trace.mkdir(parents=True, exist_ok=True)
    snapshot = {p.name: p.read_text() for p in (*SOURCES, COMPARISON_SOURCE, FIGURE_SOURCE)}
    source = ROOT / "PROPERTY_B_GENERAL_BOUND.md"
    output = ROOT / "PROPERTY_B_GENERAL_BOUND.html"
    composed = compose(snapshot, examples(trace))
    fidelity = verify_math_preserved(snapshot, composed)
    source.write_text(composed)
    (trace / "canonical-math-check.json").write_text(json.dumps(fidelity, ensure_ascii=False, indent=2) + "\n")
    aris.load_template = reader_template
    aris.strip_frontmatter = prepare_reader_source
    with tempfile.TemporaryDirectory(prefix="propertyb-general-", dir=ROOT) as tmp:
        stage = Path(tmp) / "reader.html"
        aris.main([str(source), "--out", str(stage), "--template", "academic",
                   "--title", "单交结构带来的统一整数增益",
                   "--eyebrow", "PROPERTY B · k ≥ 12",
                   "--subtitle", "小参数的具体下界 · 一般参数的统一增益 · 完整数学证明",
                   "--lang", "zh-CN"])
        stage_html = stage.read_text()
        plot_alts = {
            "delta": "英文差值主图：共用Property B参数k横轴和已核参考界最大值L_ref。左线性轴显示红色k=5至12的锁点结果增益3、3、3、4、5、27、30、31，以及独立点型表示的我们的加强判据在k=12、13直接求值的增益14、25。紫色求值与蓝色统一公式来自同一加强判据。蓝色统一公式保证的增益Δ_cert=g_*读右侧对数轴，12、17、32、64处至少增加2、13、2346、152837269。对k≥12有L_ref=B_RS+1。左右轴尺度不同，视觉交点不表示数值反超。",
            "overview": "图A：从k=4的精确值23到k≥12的一般下界；k=5至12的锁点结果为35、67、131、267、543、1112、2275、4664，另显示本文C.2在k=12、13的下界4647、9564，灰点为同一已核参考包络。",
            "small": "图B：小参数下界除以2的k次幂，显示共同参考基线、锁点结果和本文C.2在k=12、13的精确求值4647、9564；各用独立点型，来源和证据范围在正文说明。",
        }
        for name, alt in plot_alts.items():
            encoded = base64.b64encode((ROOT / f"figures/propertyb_bounds/{name}.svg").read_bytes()).decode("ascii")
            extra_class = {"overview": " bound-overview", "delta": " bound-delta"}.get(name, "")
            marker = f'<div class="bound-plot{extra_class}" data-figure="{name}"></div>'
            assert stage_html.count(marker) == 1, (name, "missing figure placeholder")
            stage_html = stage_html.replace(marker, marker.replace('</div>', f'<img src="data:image/svg+xml;base64,{encoded}" alt="{alt}" /></div>'), 1)
        for header in ("论文／结果", "文献来源"):
            marker = f"<table><thead><tr><th>{header}</th>"
            assert stage_html.count(marker) == 1
            stage_html = stage_html.replace(marker, marker.replace("<table>", '<table class="comparison-table">'), 1)
        stage.write_text(stage_html)
        math_report = embed_math(stage, output, source)
    (trace / "math-build.json").write_text(json.dumps(math_report, ensure_ascii=False, indent=2) + "\n")
    (trace / "source-snapshots.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
    report = browser_check(output, trace, source, math_inputs(composed))
    report["generatedAt"] = datetime.now(timezone.utc).isoformat()
    report["canonicalSources"] = [str(p.relative_to(ROOT)) for p in SOURCES]
    report["comparisonTableSource"] = str(COMPARISON_SOURCE.relative_to(ROOT))
    report["figureSource"] = str(FIGURE_SOURCE.relative_to(ROOT))
    report["markdown"] = str(source.relative_to(ROOT))
    report["html"] = str(output.relative_to(ROOT))
    (trace / "browser-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Rendered {output}; {math_report['math']} offline SVG formulas; desktop/phone checks passed.")


if __name__ == "__main__":
    main()
