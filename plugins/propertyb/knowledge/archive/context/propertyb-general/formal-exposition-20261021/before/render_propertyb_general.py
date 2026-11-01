#!/usr/bin/env python3
"""Compose the general-bound sources and render one offline SVG reader.

The mathematical Markdown files remain canonical.  This script changes only
reader framing/heading levels and omits dated workflow-status paragraphs.
"""
import argparse
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

对每个整数 $k\ge17$，相对于指定的 Radhakrishnan–Srinivasan 精确判据所接受的最大边数 $B_{\rm RS}(k)$，可增加

$$
\Delta(k)=\left\lfloor
\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}
\right\rfloor
$$

条边，同时保持任意有限简单 $k$ 元超图均可二染。对应下界为

$$
\boxed{m(k)\ge B_{\rm RS}(k)+1+\Delta(k).}
$$

<p class="proof-status">完整自然语言证明 · 2026年10月21日</p>

## 结果说了什么

$k$ 是每条边包含的顶点数；$m(k)$ 是不可二染色的有限简单 $k$ 元超图的最少边数。这里二染色要求每条边同时含红、蓝两色，顶点集可以是任意有限集。$\log$ 均为自然对数。

$B_{\rm RS}(k)$ 是下文指定的旧 RS–FKG–精确积分判据接受的最大**边数预算**。旧判据给 $m(k)\ge B_{\rm RS}(k)+1$；本卷的结构加强允许预算增加 $\Delta(k)$，故下界也增加同样的整数。该函数通过严格不等式定义，不依赖浮点求根或逐个 $k$ 的实验外推。

对 $k\ge32$，第四部分给出由主要一般数值判据组成的明确参考包络 $L_{\rm ref}(k)$，并证明 $L_{\rm ref}(k)=B_{\rm RS}(k)+1$。因此，同一增益也提高这一参考包络。另有 $k\ge256$ 时针对一个有限必要数据松弛方案的补充比较，其测试范围在定理处完整定义。

{{GAIN_EXAMPLES}}

### 从小参数经验到统一结构

小参数研究中，保留同一张超图的真实坏边对，比把各个局部最坏值独立相加更有效。这里把这一经验变成一般结构：在最小顶点反例中，顶点对必须被边覆盖；真实边的关联矩阵又限制单交图中的团。公共点二分进一步加强团界，于是随机重染中的责备边对总数获得统一削减。

<div class="proof-route"><div><b>原始超图</b><span>任意有限顶点集</span></div><i>→</i><div><b>最小反例</b><span>覆盖点对，限制点数</span></div><i>→</i><div><b>真实单交图</b><span>Gram与公共点团界</span></div><i>→</i><div><b>同一重染算法</b><span>削减吸收新增边数</span></div></div>

下面完整给出原超图到染色的概率与结构论证、旧预算的有限性、加一余量、随预算增长的整数增益，以及准确参考界的比较。全部证明均在本页展开。
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
    body += "|$k$|比旧下界 $B_{\\rm RS}(k)+1$ 至少增加|\n|---:|---:|\n"
    body += "\n".join(f"|{row['k']}|{row['certified_increment_lower']:,}|" for row in rows)
    body += "\n\n这些数字采用整数与有理数保守估计，帮助理解增益规模；整个参数范围的证明在下文，不由这些例子外推。\n"
    return body


def mathematical_body(text):
    """Drop only the original title and dated status paragraph."""
    return text[text.index("\n## ") + 1 :].strip()


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
        path, sep, fragment = target.partition("#")
        relative = os.path.relpath((source.parent / path).resolve(), ROOT)
        return f"[{label}]({relative}{sep}{fragment})"
    return re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)", link, text)


def compose(snapshot, illustration):
    core = mathematical_body(snapshot[SOURCES[0].name])
    core = core.split("\n## 与原始来源及研究目标的关系", 1)[0]
    gain = mathematical_body(snapshot[SOURCES[1].name])
    gain = gain.replace(
        "本定理精确比较的是 (1) 指定的RS–FKG–精确积分整数界。其他文献中的离散位置、度数或共度加强，必须另行比较；不能因 (2) 已有候选证明就宣称超过它们或完成整个Goal。",
        "上述加一结论比较的是 (1) 指定的RS–FKG–精确积分整数界。",
    )
    clique = mathematical_body(snapshot[SOURCES[2].name])
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
    pieces = [INTRO.replace("{{GAIN_EXAMPLES}}", illustration),
              "## 一、一般二染色判据与完整原图连接\n\n" + subordinate(core),
              "## 二、旧预算的有限性与统一加一余量\n\n" + subordinate(gain),
              "## 三、公共点二分与增长的整数增益\n\n" + subordinate(clique),
              "## 四、参考界与有限测试方案的完整比较\n\n" + subordinate(baseline),
              r"""## 来源与比较对象

概率工具继承 Radhakrishnan–Srinivasan 的延迟重染分析及其附录正关联估计，保留精确积分与实际有向单交对；没有把这些工具或公共点二分的标准论证记作首创。原始来源为 [RS作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)，本地亦保存[原始PDF](ref/radhakrishnan_srinivasan_2000_two_coloring.pdf)。

本卷组合的四个规范来源是[一般充分判据](proofs/propertyb-general/CORE_THEOREM.md)、[统一整数加一](proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)、[团界加强与增长增益](proofs/propertyb-general/CLIQUE_REFINEMENT.md)、[参考界完整比较](proofs/propertyb-general/BASELINE_COMPARISON.md)。它们保持规范地位；本页与[Markdown阅读稿](PROPERTY_B_GENERAL_BOUND.md)提供完整合并阅读。原始文献的阅读范围另见[来源核对](context/propertyb-general/round01/literature/BASELINE.md)。

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
main p,main li { overflow-wrap:break-word; }
main mjx-container[display="true"] { margin:20px 0; background:#f0f1e9; border-left:3px solid #aabdb5; padding:18px 14px; border-radius:3px; }
main mjx-container:not([display="true"]) { overflow:visible; }
.proof-status { border-left:3px solid #ad8054; color:#71532f; font:14px/1.7 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif; padding:10px 14px; background:#f2eadc; }
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
            target = page.locator("main h2").nth(1)
            target.scroll_into_view_if_needed()
            page.screenshot(path=str(trace / f"{label}-proof.png"), full_page=False)
            comparison = page.get_by_role("heading", name="四、参考界与有限测试方案的完整比较", exact=True)
            if comparison.count():
                comparison.scroll_into_view_if_needed()
                page.screenshot(path=str(trace / f"{label}-comparison.png"), full_page=False)
                relaxation = page.get_by_role("heading", name="5. 补充定理：明确的零锁有限测试方案", exact=True)
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
    snapshot = {p.name: p.read_text() for p in SOURCES}
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
                   "--eyebrow", "PROPERTY B · k ≥ 17",
                   "--subtitle", "从真实坏边对到全超图下界：完整论证与明确的整数比较",
                   "--lang", "zh-CN"])
        math_report = embed_math(stage, output, source)
    (trace / "math-build.json").write_text(json.dumps(math_report, ensure_ascii=False, indent=2) + "\n")
    (trace / "source-snapshots.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
    report = browser_check(output, trace, source, math_inputs(composed))
    report["generatedAt"] = datetime.now(timezone.utc).isoformat()
    report["canonicalSources"] = [str(p.relative_to(ROOT)) for p in SOURCES]
    report["markdown"] = str(source.relative_to(ROOT))
    report["html"] = str(output.relative_to(ROOT))
    (trace / "browser-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Rendered {output}; {math_report['math']} offline SVG formulas; desktop/phone checks passed.")


if __name__ == "__main__":
    main()
