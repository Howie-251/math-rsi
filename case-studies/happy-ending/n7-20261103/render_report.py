"""Render canonical Markdown as a self-contained, script-free HTML report."""

import argparse
import base64
import hashlib
import html
import importlib.util
import io
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from matplotlib import rc_context
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import MathTextParser, math_to_image


ROOT = Path(__file__).resolve().parent
HELPER = ROOT.parent.parent / '.agents/skills/render-html/scripts/render_html.py'
MATH = re.compile(r'(?P<display>\\\[.*?\\\]|(?<!\\)\$\$.*?\$\$)|(?P<inline>\\\([^\n]*?\\\)|(?<![\\$])\$(?!\$)[^\n$]+?\$(?!\$))', re.S)
CODE = re.compile(r'(```[\s\S]*?```|`[^`\n]+`)')
FIGURE = re.compile(r'^\s*\{\{figure:([a-z-]+)\}\}\s*$', re.M)
MATH_PARSER = MathTextParser('path')
FAMILY = 'Times New Roman'
FONT = FontProperties(family=FAMILY, size=14, math_fontfamily='custom')
MATH_FONT = {
    'mathtext.fontset': 'custom', 'mathtext.fallback': 'stix',
    **{f'mathtext.{style}': FAMILY for style in ('rm', 'cal', 'sf', 'tt')},
    'mathtext.it': FAMILY + ':style=italic',
    'mathtext.bf': FAMILY + ':weight=bold',
    'mathtext.bfit': FAMILY + ':style=italic:weight=bold',
}


def load_helper():
    packaged = ROOT / 'rendering/aris_render_html.py'
    spec = importlib.util.spec_from_file_location('aris_render_html', packaged if packaged.is_file() else HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def math_image(source, display, glyph_fonts):
    tex = re.sub(r'\\(le|ge|ne)(?![A-Za-z])', lambda match: '\\' + match.group(1) + 'q', source.strip())
    tex = re.sub(r'\\(?:big|Big|bigg|Bigg)[lrm]?(?![A-Za-z])', '', tex)
    tex = tex.replace(r'\coloneqq', ':=').replace(r'\implies', r'\Rightarrow').replace(r'\iff', r'\Leftrightarrow')
    tex = re.sub(r'\s+', ' ', tex)
    if re.search(r'[\u3400-\u9fff]', tex):
        raise ValueError(f'Move CJK explanatory text outside the math delimiters: {source!r}')
    expression = f'${tex}$'
    output = io.BytesIO()
    try:
        with rc_context({**MATH_FONT, 'svg.fonttype': 'path', 'svg.hashsalt': 'n7-math-20261103'}):
            bounds = MATH_PARSER.parse(expression, dpi=72, prop=FONT)
            for font, _, code, _, _ in bounds.glyphs:
                glyph_fonts[font.postscript_name] += 1
                if chr(code).isascii() and chr(code).isalnum() and font.family_name != FAMILY:
                    raise ValueError(f'Latin/digit glyph {chr(code)!r} used {font.family_name}')
            math_to_image(expression, output, prop=FONT, format='svg', color='#172535')
    except ValueError as error:
        raise ValueError(f'Unsupported mathematical expression: {source!r}\n{error}') from error
    svg = output.getvalue()
    encoded = base64.b64encode(svg[svg.index(b'<svg '):]).decode('ascii')
    width = bounds.width / 14
    height = bounds.height / 14
    alignment = -bounds.depth / 14
    image = (f'<img class="math-inline" alt="{html.escape(source, quote=True)}" '
             f'src="data:image/svg+xml;base64,{encoded}" '
             f'style="width:{width:.3f}em;height:{height:.3f}em;vertical-align:{alignment:.3f}em">')
    return f'<span class="math-display">{image}</span>' if display else image


def render(source_path, output_path, title, dek):
    helper = load_helper()
    source_bytes = source_path.read_bytes()
    source_hash = hashlib.sha256(source_bytes).hexdigest()
    raw = helper.strip_frontmatter(source_bytes.decode('utf-8-sig'))
    replacements = {}
    formulas = {}
    glyph_fonts = Counter()
    figures = json.loads((ROOT / 'figures/captions.json').read_text(encoding='utf-8'))
    figure_count = 0

    def stash(markup):
        token = f'N7REPORTTOKEN{len(replacements):05d}END'
        if token in raw:
            raise ValueError(f'Reserved token in Markdown: {token}')
        replacements[token] = markup
        return token

    def replace_math(match):
        display = match.lastgroup == 'display'
        raw_match = match.group()
        offset = 2 if raw_match.startswith(('\\', '$$')) else 1
        tex = raw_match[offset:-offset].strip()
        key = tex, display
        if key not in formulas:
            formulas[key] = math_image(tex, display, glyph_fonts)
        return stash(formulas[key])

    def replace_figure(match):
        nonlocal figure_count
        key = match.group(1)
        svg = (ROOT / 'figures' / f'{key}.svg').read_text(encoding='utf-8')
        caption = html.escape(figures[key])
        figure_count += 1
        return '\n\n' + stash(f'<figure>{svg}<figcaption>{caption}</figcaption></figure>') + '\n\n'

    raw = FIGURE.sub(replace_figure, raw)
    protected = ''.join(part if index % 2 else MATH.sub(replace_math, part) for index, part in enumerate(CODE.split(raw)))
    blocks = helper.parse_blocks(protected.splitlines())
    if blocks and blocks[0].get('type') == 'heading' and blocks[0].get('level') == 1:
        blocks = blocks[1:]
    body, toc = helper._render_blocks(blocks, collect_toc=True)
    body = re.sub(r'<table\b.*?</table>', lambda match: f'<div class="table-scroll" tabindex="0">{match.group()}</div>', body, flags=re.S)
    for token, markup in replacements.items():
        if markup.startswith('<figure>') or markup.startswith('<span class="math-display">'):
            body = body.replace(f'<p>{token}</p>', markup)
        body = body.replace(token, markup)
    if toc[0]['text'] != '当前上界' or toc[1]['level'] != 2:
        raise ValueError('Expected 当前上界 before the first numbered section')
    results, boundary, body = body.partition(f'<h2 id="{toc[1]["id"]}">')
    if not boundary or not results.startswith('<h2'):
        raise ValueError('Could not separate the results and numbered sections')
    body = boundary + body
    toc_html = helper.render_toc(toc[1:])
    for token, markup in replacements.items():
        toc_html = toc_html.replace(token, markup)
    source_name = source_path.relative_to(ROOT).as_posix()
    output = helper.substitute((ROOT / 'report-template.html').read_text(encoding='utf-8'), {
        'TITLE': html.escape(title), 'DEK': html.escape(dek), 'SOURCE_PATH': html.escape(source_name),
        'SOURCE_SHA256': source_hash,
        'GENERATED_AT': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'TOC': toc_html, 'BODY': body, 'RESULTS': results,
    })
    if re.search(r'N7REPORTTOKEN\d+END|\{\{[A-Z_]+\}\}', output):
        raise ValueError('Unresolved render placeholder')
    if re.search(r'<\s*(script|iframe|object|embed|link)\b|\son\w+\s*=', output, flags=re.I):
        raise ValueError('Unexpected active HTML markup')
    output_path.write_text(output, encoding='utf-8')
    return {'source_sha256': source_hash, 'html_sha256': hashlib.sha256(output_path.read_bytes()).hexdigest(), 'equations': len(formulas), 'figure_occurrences': figure_count, 'math_glyph_font_counts': dict(glyph_fonts)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / 'source/report.md')
    parser.add_argument('--out', type=Path, default=ROOT / 'n7-upper-bounds-20261103.html')
    parser.add_argument('--title')
    parser.add_argument('--dek')
    args = parser.parse_args()
    settings = json.loads((ROOT / 'source/report.json').read_text(encoding='utf-8'))
    receipt = render(args.source.resolve(), args.out.resolve(), args.title or settings['title'], args.dek or settings['subtitle'])
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
