#!/usr/bin/env python3
"""Render the case README with bundled ARIS, embedding its one local figure."""

import base64
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
CASE = ROOT / "case-studies/property-b"
RENDER = ROOT / "base/skills/skills-codex/render-html/scripts/render_html.py"


def main():
    subprocess.run([
        sys.executable, str(RENDER), "case-studies/property-b/README.md",
        "--out", "case-studies/property-b/index.html", "--offline", "--lang", "en",
        "--eyebrow", "MathRSI · Research Case", "--title", "Property B",
        "--subtitle", "Stronger lower bounds, reusable proof methods",
    ], cwd=ROOT, check=True)
    output = CASE / "index.html"
    page = output.read_text(encoding="utf-8")
    figure = base64.b64encode((CASE / "assets/delta.png").read_bytes()).decode("ascii")
    page = page.replace('src="assets/delta.png"', f'src="data:image/png;base64,{figure}"')
    # Keep the upstream snapshot intact. These case-specific presentation rules
    # constrain the embedded figure and allow wide evidence tables to scroll.
    page = page.replace("</style>", """
main img { display: block; width: 100%; height: auto; margin: 24px 0; }
main { min-width: 0; }
.case-table { overflow-x: auto; margin: 16px 0; }
.case-table table { min-width: 680px; margin: 0; }
.case-table th:first-child, .case-table td:first-child { white-space: nowrap; }
main p, main li, td { overflow-wrap: anywhere; }
</style>""", 1)
    page = page.replace("<table>", '<div class="case-table"><table>')
    page = page.replace("</table>", "</table></div>")
    output.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
