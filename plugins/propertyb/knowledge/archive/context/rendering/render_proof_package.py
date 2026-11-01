#!/usr/bin/env python3
"""Compose the full proof and publish one HTML with embedded, offline SVG math."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import tempfile

from compose_proof_package import compose

ROOT = Path(__file__).resolve().parents[2]
repo = Path(os.environ.get("ARIS_REPO", "/Users/rfy_naiveai/Desktop/aris_main"))
candidates = [
    ROOT / ".agents/skills/render-html/scripts/render_html.py",
    ROOT / "skills/render-html/scripts/render_html.py",
    repo / "skills/render-html/scripts/render_html.py",
    Path.home() / ".codex/skills/render-html/scripts/render_html.py",
]
helper = next(p for p in candidates if p.is_file())
spec = importlib.util.spec_from_file_location("aris_render_html_proof", helper)
aris = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aris)

# Adapt unsupported delimiters in memory. The helper still reads/hashes the
# original source and the canonical Markdown remains untouched.
strip_frontmatter = aris.strip_frontmatter
def prepare_source(raw):
    text = strip_frontmatter(raw)
    text = re.sub(r"(?<!\\)\\\[(.*?)\\\]", lambda m: "$$" + m[1].strip() + "$$", text, flags=re.S)
    text = re.sub(r"(?<!\\)\\\((.*?)\\\)", lambda m: "$" + m[1] + "$", text, flags=re.S)
    return re.sub(r"(?m)^~~~([A-Za-z0-9_+.#-]*)\s*$", lambda m: chr(96) * 3 + m[1], text)
aris.strip_frontmatter = prepare_source

render_table = aris.render_table
def scrollable_table(header, divider, rows):
    return '<div class="table-scroll" role="region" aria-label="可横向滚动的数据表" tabindex="0">' + render_table(header, divider, rows) + '</div>'
aris.render_table = scrollable_table
render_toc = aris.render_toc
aris.render_toc = lambda toc: render_toc([entry for entry in toc if entry["level"] == 2])
aris.CDN_BLOCK_FULL = r"""
<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$']], displayMath: [['$$', '$$']], processEscapes: true},
  svg: {fontCache: 'local'},
  startup: {typeset: false},
  options: {skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"></script>
"""

load_template = aris.load_template
def readable_template(name):
    template = load_template(name)
    template = re.sub(
        r'(  <div class="meta">[\s\S]*?  </div>)(\n</header>)',
        r'  <details class="source-info"><summary>来源信息</summary>\n\1\n  </details>\2',
        template, count=1,
    )
    template = re.sub(
        r'<footer class="aris-footer">[\s\S]*?</footer>',
        '<footer class="aris-footer">源文档：<a href="{{SOURCE_PATH}}">{{SOURCE_PATH}}</a>'
        ' · <a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/render-html/SKILL.md">ARIS render-html</a></footer>',
        template, count=1,
    )
    css = """
/* Keep the canonical proof readable on desktop, phone, and paper. */
main { min-width: 0; }
.chapter-anchor { scroll-margin-top: 24px; }
main > h1:first-of-type { display: none; }
nav.toc > ol { list-style: none; padding-left: 0; }
nav.toc ol li::before { content: none; }
header.hero .subtitle { font-style: normal; }
header.hero .meta { overflow-wrap: anywhere; border-top: none; padding: 12px 0 0; }
header.hero details.source-info { background: transparent; border: none; margin: 12px 0 0; }
header.hero details.source-info summary { padding: 0; color: var(--ink-muted); font-size: 12px; }
header.hero details.source-info[open] summary { border-bottom: none; }
main a, footer code { overflow-wrap: anywhere; }
main .table-scroll { max-width: 100%; overflow-x: auto; margin: 16px 0; }
main table { width: 100%; min-width: 580px; margin: 0; }
main table th, main table td { vertical-align: top; }
main table td { overflow-wrap: anywhere; }
main .arithmetic-case table { font-size: 12px; font-variant-numeric: tabular-nums; }
main .arithmetic-case table:nth-child(n) { min-width: 720px; }
main .arithmetic-case summary { font-variant-numeric: tabular-nums; }
main pre { max-width: 100%; overflow-x: auto; font-size: 12px; }
main > p:first-of-type { font-size: 20px; line-height: 1.8; }
mjx-container:not([display="true"]) {
  max-width: 100%; overflow-x: auto; overflow-y: hidden;
}
mjx-container[display="true"] {
  min-width: 0 !important; max-width: 100%;
  overflow-x: auto; overflow-y: hidden; padding: 12px 0;
}
@media (max-width: 700px) {
  nav.toc { margin-bottom: 24px; padding-bottom: 8px; }
  nav.toc h3 { display: none; }
  nav.toc ol { display: flex; gap: 20px; overflow-x: auto; white-space: nowrap; }
  nav.toc ol li { flex: 0 0 auto; }
  header.hero h1 { font-size: 29px; line-height: 1.3; }
  main table { font-size: 14px; }
  main table th, main table td { min-width: 58px; }
}
@media print {
  nav.toc { display: none; }
  .layout { display: block; max-width: none; }
  details:not([open]) > :not(summary) { display: none; }
}
"""
    return template.replace("</style>", css + "</style>", 1).replace("{{TOC_LABEL}}", "目录")
aris.load_template = readable_template


def embed_math(stage, destination):
    """Typeset once; the final file makes no network requests when opened."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True, proxy={"server": "http://127.0.0.1:7890"})
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(stage.as_uri(), wait_until="networkidle", timeout=60000)
        page.evaluate("""async () => {
          await MathJax.startup.promise;
          document.querySelectorAll('details').forEach(d => d.open = true);
          await MathJax.typesetPromise();
          await document.fonts.ready;
        }""")
        report = page.evaluate("""() => {
          const items = Array.from(MathJax.startup.document.math);
          for (const item of items) {
            if (item.typesetRoot) item.typesetRoot.dataset.tex = item.math;
          }
          return {
            math: items.length,
            mathInputs: items.map(item => item.math),
            mathErrors: [...document.querySelectorAll('[data-mml-node="merror"],mjx-merror')]
              .map(node => node.textContent),
            tables: document.querySelectorAll('main table').length,
            arithmeticCases: document.querySelectorAll('details.arithmetic-case').length
          };
        }""")
        if errors or report["mathErrors"]:
            raise RuntimeError(f"Rendering errors: {errors}; {report['mathErrors']}")
        assert report["math"] > 500 and report["arithmeticCases"] == 23
        page.evaluate("""() => {
          document.querySelectorAll('script,link[rel="stylesheet"],.code-copy-btn,.copy-btn')
            .forEach(node => node.remove());
          document.querySelectorAll('details').forEach(d => d.open = false);
          document.querySelectorAll('mjx-container').forEach(node => {
            node.removeAttribute('tabindex');
          });
          const meta = document.createElement('meta');
          meta.name = 'aris:math-mode';
          meta.content = 'embedded-svg; no runtime network dependency';
          document.head.append(meta);
        }""")
        destination.write_text("<!DOCTYPE html>\n" + page.evaluate("document.documentElement.outerHTML") + "\n")
        browser.close()
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace-dir", type=Path)
    args = parser.parse_args()
    source = compose()
    destination = ROOT / "PROOF_PACKAGE.html"
    with tempfile.TemporaryDirectory(prefix="proof-reader-", dir=ROOT) as temporary:
        stage = Path(temporary) / "proof.html"
        # Relative evidence links target the final page's project-root location.
        aris.main([
            str(source), "--out", str(stage), "--template", "academic",
            "--title", "五元超图的32条边界：完整证明",
            "--eyebrow", "Property B · m(5) ≥ 33",
            "--subtitle", "数学规格 · 完整推导 · 精确算术 · Lean核验",
            "--lang", "zh-CN",
        ])
        report = embed_math(stage, destination)
    if args.trace_dir:
        args.trace_dir.mkdir(parents=True, exist_ok=True)
        (args.trace_dir / "math-build.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Published {destination.name}: {destination.stat().st_size:,} bytes; "
          f"{report['math']} embedded formulas; {report['arithmeticCases']} exact profiles.")
