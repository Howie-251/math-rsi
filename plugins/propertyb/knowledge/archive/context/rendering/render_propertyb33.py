#!/usr/bin/env python3
"""Render the T33 reader with the existing ARIS layout and embedded SVG math."""
import argparse
import json
import os
from pathlib import Path
import tempfile

from render_proof_package import ROOT, aris

_proof_template = aris.load_template


def reader_template(name):
    return _proof_template(name).replace("</style>", """
main p, main li { overflow-wrap: anywhere; }
main :not(pre) > code { white-space: normal; overflow-wrap: anywhere; }
</style>""", 1)


aris.load_template = reader_template


def embed_math(stage: Path, destination: Path, source: Path):
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
            headings: [...document.querySelectorAll('main h2')].map(n => n.textContent)
          };
        }""")
        if errors or report["mathErrors"] or not report["math"]:
            raise RuntimeError(f"Math rendering failed: {errors}; {report['mathErrors']}")
        page.evaluate("""() => {
          document.querySelectorAll('script,link[rel="stylesheet"],.code-copy-btn,.copy-btn')
            .forEach(node => node.remove());
          document.querySelectorAll('details').forEach(d => d.open = false);
          document.querySelectorAll('mjx-container').forEach(node => node.removeAttribute('tabindex'));
          const meta = document.createElement('meta');
          meta.name = 'aris:math-mode';
          meta.content = 'embedded-svg; no runtime network dependency';
          document.head.append(meta);
        }""")
        page.evaluate("""reference => {
          const link = document.querySelector('footer.aris-footer a');
          if (link) { link.href = reference; link.textContent = reference; }
        }""", os.path.relpath(source, destination.parent))
        destination.write_text("<!DOCTYPE html>\n" +
            page.evaluate("document.documentElement.outerHTML") + "\n")
        browser.close()
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path,
                        default=ROOT / "proofs/propertyb33/PROOF_PACKAGE.md")
    parser.add_argument("--out", type=Path, default=ROOT / "PROOF_PACKAGE_33.html")
    parser.add_argument("--trace-dir", type=Path, required=True)
    parser.add_argument("--candidate", action="store_true")
    args = parser.parse_args()
    title = "33条五元边：候选证明稿" if args.candidate else "33条五元边均可二染色：完整证明"
    eyebrow = "Property B · T33" if args.candidate else "Property B · m(5) ≥ 34"
    with tempfile.TemporaryDirectory(prefix="propertyb33-reader-", dir=ROOT) as temporary:
        stage = Path(temporary) / "proof.html"
        aris.main([
            str(args.source.resolve()), "--out", str(stage), "--template", "academic",
            "--title", title, "--eyebrow", eyebrow,
            "--subtitle", "原命题 · 完整推导 · 局部分类 · Lean形式证明", "--lang", "zh-CN",
        ])
        report = embed_math(stage, args.out.resolve(), args.source.resolve())
    args.trace_dir.mkdir(parents=True, exist_ok=True)
    (args.trace_dir / "math-build.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Rendered {args.out}: {report['math']} embedded formulas.")


if __name__ == "__main__":
    main()
