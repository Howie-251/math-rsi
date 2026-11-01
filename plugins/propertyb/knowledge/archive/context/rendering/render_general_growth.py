#!/usr/bin/env python3
"""Render the complete general-growth Lean report with the existing offline SVG reader."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit

from render_propertyb_general import (
    ROOT, aris, embed_math, math_inputs, normalized_math_counter,
    prepare_reader_source, reader_template as general_reader_template,
)

SOURCES = (ROOT / "context/propertyb-general/bridge-12-16-20261021/LEAN_READER.md",)
DEFAULT_TRACE = ROOT / ".aris/traces/render-html/2026-10-21_general-growth-lean-k12"


def normalize_math(text):
    text = re.sub(r"(?<!\\)\\\[(.*?)\\\]", lambda m: "$$" + m[1].strip() + "$$", text, flags=re.S)
    return re.sub(r"(?<!\\)\\\((.*?)\\\)", lambda m: "$" + m[1].strip() + "$", text, flags=re.S)


def source_math_inputs(text):
    # Shell variables inside preserved code fences are not mathematical input.
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$", "", text)
    text = re.sub(r"(?<!`)`[^`\n]+`(?!`)", "", text)
    return math_inputs(text)


def reader_links(text, source):
    def target(href):
        if re.match(r"(?:https?:|mailto:|#)", href):
            return href
        path = unquote(urlsplit(href).path)
        for candidate in (source.parent / path, ROOT / path):
            if candidate.exists():
                return candidate.resolve().relative_to(ROOT).as_posix()
        return href

    text = re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)",
                  lambda m: f"[{m[1]}]({target(m[2])})", text)

    def code_link(match):
        label = match[1]
        if any(c in label for c in " \n\t"):
            return match[0]
        for candidate in (ROOT / label, source.parent / label,
                          ROOT / "formal/Aris4Math/General/RS" / label,
                          ROOT / "proofs/propertyb-general" / label):
            if candidate.is_file() or (candidate.is_dir() and "/" in label):
                return f"[{label}]({candidate.resolve().relative_to(ROOT).as_posix()})"
        return match[0]

    return re.sub(r"(?<!`)`([^`\n]+)`(?!`)", code_link, text)


def compose(snapshot):
    return reader_links(normalize_math(snapshot[SOURCES[0].name]), SOURCES[0]).rstrip() + "\n"


def reader_template(name):
    template = general_reader_template(name)
    template = re.sub(r'<footer class="aris-footer">[\s\S]*?</footer>',
        '<footer class="aris-footer">阅读稿：<a href="PROPERTY_B_GENERAL_LEAN.md">Markdown</a>'
        ' · <a href="context/propertyb-general/bridge-12-16-20261021/LEAN_READER.md">完整形式证明报告</a>'
        ' · <a href="formal/Aris4Math/General/Growth/Twelve.lean">Lean主入口</a></footer>',
        template, count=1)
    return template.replace('</style>', '''
main :not(pre) > code { white-space:normal; overflow-wrap:anywhere; }
main mjx-container:not([display="true"]) { overflow:visible; }
main h2 { border-top:1px solid var(--border); padding-top:25px; }
main .table-scroll { margin:22px 0; }
@media(max-width:700px) {
  main table { min-width:560px; }
  main table th,main table td { overflow-wrap:anywhere; }
  nav.toc ol { white-space:normal; display:block; }
  nav.toc ol li { margin:7px 0; }
}
</style>''', 1)


def browser_check(output, trace, source, expected_math):
    from playwright.sync_api import sync_playwright
    result = {}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for label, width, height in (("desktop", 1440, 1000), ("phone", 390, 844)):
            page = browser.new_page(viewport={"width": width, "height": height})
            requests, errors = [], []
            page.route("http://**/*", lambda route: route.abort())
            page.route("https://**/*", lambda route: route.abort())
            page.on("request", lambda request: requests.append(request.url)
                    if request.url.startswith(("http:", "https:")) else None)
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(output.as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            checks = page.evaluate(r'''() => {
              const ids=new Set([...document.querySelectorAll('[id]')].map(n=>n.id));
              const clone=document.querySelector('main').cloneNode(true);
              clone.querySelectorAll('mjx-container,pre,code').forEach(n=>n.remove());
              return {
                formulaCount:document.querySelectorAll('mjx-container').length,
                svgCount:document.querySelectorAll('mjx-container > svg').length,
                texInputs:[...document.querySelectorAll('mjx-container')].map(n=>n.dataset.tex),
                mathErrors:[...document.querySelectorAll('[data-mml-node="merror"],mjx-merror')].map(n=>n.textContent),
                scripts:document.scripts.length,
                externalAssets:[...document.querySelectorAll('script[src],link[href],img[src]')]
                  .map(n=>n.src||n.href).filter(x=>/^https?:/.test(x)),
                horizontalPageOverflow:document.documentElement.scrollWidth>innerWidth+1,
                brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].map(n=>n.getAttribute('href'))
                  .filter(h=>h.length>1&&!ids.has(decodeURIComponent(h.slice(1)))),
                localLinks:[...document.querySelectorAll('a[href]')].map(n=>n.getAttribute('href'))
                  .filter(h=>!/^https?:|^mailto:|^#/.test(h)),
                sourceHash:document.querySelector('meta[name="aris:source-sha256"]')?.content||null,
                sourceMathDelimiters:/\\\[|\\\]|\\\(|\\\)|\$\$/.test(clone.textContent),
                headings:[...document.querySelectorAll('main h2,main h3')].map(n=>n.textContent),
                tables:document.querySelectorAll('main table').length,
                bodyHeight:document.documentElement.scrollHeight
              };
            }''')
            page.screenshot(path=str(trace / f"{label}-top.png"), full_page=False)
            for name, index in (("theorem", 1), ("proof", 2), ("verification", 3), ("reproduction", 4)):
                headings = page.locator("main h2")
                if headings.count() > index:
                    headings.nth(index).scroll_into_view_if_needed()
                    page.screenshot(path=str(trace / f"{label}-{name}.png"), full_page=False)
            tex = checks.pop("texInputs")
            checks.update(networkRequests=requests, pageErrors=errors,
                          sourceMathCount=len(expected_math),
                          mathInputsMatch=normalized_math_counter(tex)==normalized_math_counter(expected_math),
                          mathInputOrderMatches=[re.sub(r"\s+", "", t) for t in tex] ==
                            [re.sub(r"\s+", "", t) for t in expected_math])
            checks["missingLocalLinks"]=[href for href in checks["localLinks"]
                if not (output.parent / unquote(urlsplit(href).path)).exists()]
            checks["missingSourceMath"]=list((normalized_math_counter(expected_math)-
                                              normalized_math_counter(tex)).elements())
            result[label]=checks
            assert not checks["horizontalPageOverflow"], (label, "page overflow")
            assert not (checks["scripts"] or checks["externalAssets"] or requests or errors or
                        checks["mathErrors"] or checks["brokenAnchors"] or checks["sourceMathDelimiters"]), checks
            assert checks["formulaCount"]==checks["svgCount"]==len(expected_math)>0, checks
            assert checks["mathInputsMatch"] and checks["mathInputOrderMatches"], checks
            assert not checks["missingLocalLinks"], checks["missingLocalLinks"]
            assert checks["sourceHash"]==aris.sha256_of(source.read_text())
            page.close()
        browser.close()
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--trace-dir", type=Path, default=DEFAULT_TRACE)
    args=parser.parse_args()
    trace=args.trace_dir.resolve()
    trace.mkdir(parents=True, exist_ok=True)
    snapshot={p.name:p.read_text() for p in SOURCES}
    composed=compose(snapshot)
    expected=[tex for path in SOURCES for tex in source_math_inputs(normalize_math(snapshot[path.name]))]
    assert normalized_math_counter(expected)==normalized_math_counter(source_math_inputs(composed))
    source=ROOT / "PROPERTY_B_GENERAL_LEAN.md"
    output=ROOT / "PROPERTY_B_GENERAL_LEAN.html"
    source.write_text(composed)
    aris.load_template=reader_template
    aris.strip_frontmatter=prepare_reader_source
    with tempfile.TemporaryDirectory(prefix="propertyb-general-growth-", dir=ROOT) as temporary:
        stage=Path(temporary) / "reader.html"
        aris.main([str(source), "--out", str(stage), "--template", "academic",
                   "--title", "一般增长下界的完整Lean证明",
                   "--eyebrow", "PROPERTY B · FORMAL VERIFICATION",
                   "--subtitle", "全部k≥12 · 最大RS预算与整数增益Δ≥2 · 原Bool染色 · 可复现证据",
                   "--lang", "zh-CN"])
        math_report=embed_math(stage, output, source)
    (trace / "math-build.json").write_text(json.dumps(math_report, ensure_ascii=False, indent=2)+"\n")
    (trace / "canonical-sources.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2)+"\n")
    report=browser_check(output, trace, source, source_math_inputs(composed))
    report.update(generatedAt=datetime.now(timezone.utc).isoformat(),
                  canonicalSources=[str(p.relative_to(ROOT)) for p in SOURCES],
                  markdown=source.name, html=output.name)
    (trace / "browser-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(f"Rendered {output.name}; {math_report['math']} embedded SVG formulas; offline desktop/phone checks passed.")


if __name__ == "__main__":
    main()
