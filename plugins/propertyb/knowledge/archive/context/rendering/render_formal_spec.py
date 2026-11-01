#!/usr/bin/env python3
"""Render the canonical specification through ARIS, preserving its source metadata."""
import importlib.util
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
repo = Path(os.environ.get('ARIS_REPO', '/Users/rfy_naiveai/Desktop/aris_main'))
candidates = [
    ROOT / '.agents/skills/render-html/scripts/render_html.py',
    ROOT / 'skills/render-html/scripts/render_html.py',
    repo / 'skills/render-html/scripts/render_html.py',
    Path.home() / '.codex/skills/render-html/scripts/render_html.py',
]
helper = next(p for p in candidates if p.is_file())
spec = importlib.util.spec_from_file_location('aris_render_html', helper)
aris = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aris)

# The ARIS parser protects dollar-delimited TeX from Markdown emphasis.
# Normalize only the delimiters in memory; never rewrite the canonical MD.
strip_frontmatter = aris.strip_frontmatter
def prepare_math(raw):
    text = strip_frontmatter(raw)
    text = re.sub(r'\\\[(.*?)\\\]', lambda m: '$$' + m[1].strip() + '$$', text, flags=re.S)
    return re.sub(r'\\\((.*?)\\\)', lambda m: '$' + m[1] + '$', text, flags=re.S)
aris.strip_frontmatter = prepare_math

load_template = aris.load_template
def readable_template(name):
    template = load_template(name)
    template = re.sub(
        r'(  <div class="meta">[\s\S]*?  </div>)(\n</header>)',
        r'  <details class="source-info"><summary>来源信息</summary>\n\1\n  </details>\2',
        template, count=1,
    )
    css = '''
/* Long quantified formulas remain accessible on narrow screens. */
main { min-width: 0; }
header.hero details.source-info { background: transparent; border: none; margin: 12px 0 0; }
header.hero details.source-info summary { padding: 0; color: var(--ink-muted); font-size: 12px; }
header.hero .meta { overflow-wrap: anywhere; border-top: none; padding: 12px 0 0; }
nav.toc > ol { list-style: none; padding-left: 0; }
mjx-container:not([display="true"]) { max-width: 100%; overflow-x: auto; overflow-y: hidden; }
main table { display: block; max-width: 100%; overflow-x: auto; }
/* Keep the dependency-status column readable inside the scrollable table. */
main table:nth-of-type(2) th:nth-child(2),
main table:nth-of-type(2) td:nth-child(2) { min-width: 240px; }
main a, footer code { overflow-wrap: anywhere; }
main > h1:first-of-type { display: none; }
mjx-container[display="true"] { min-width: 0 !important; max-width: 100%; overflow-x: auto; overflow-y: hidden; padding: 12px 0; }
@media print { nav.toc { display:none; } .layout { display:block; max-width:none; } }
'''
    return template.replace('</style>', css + '</style>', 1).replace('{{TOC_LABEL}}', '目录')
aris.load_template = readable_template

if __name__ == '__main__':
    raise SystemExit(aris.main([
        str(ROOT / 'FORMAL_SPEC.md'), '--out', str(ROOT / 'FORMAL_SPEC.html'),
        '--template', 'academic', '--title', 'Property B：核心目标与数学规格',
        '--eyebrow', 'aris4math · 数学规格 v1.0',
        '--subtitle', '定义、等价模型与有限约化', '--lang', 'zh-CN',
    ]))
