"""Build the concise seminar edition, preserving the earlier source collection."""
from pathlib import Path
import hashlib
import html
import json
import re
import shutil
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
R = HERE.parent
sys.path.insert(0, str(HERE / 'vendor'))
import markdown
from bs4 import BeautifulSoup
from latex2mathml.converter import convert

NAME = 'Ruskey-Savage_Q6_研究报告'
ARCHIVE = 'Ruskey-Savage_Q6_证明资料汇编'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

frozen = {name: sha(R/name) for name in (
    'P6_FULL_CLOSURE.md', 'P6_FULL_REVIEW.json', 'P6_FULL_REVIEW.md',
    'FOURTEEN_FINAL25_PROOF.md', 'SIXTEEN_SMALLCUT_PROOF.md')}
gate = json.loads((R/'P6_FULL_REVIEW.json').read_text(encoding='utf-8-sig'))
assert gate['verdict'] == 'PASS' and gate['details']['full_P6_proved']
assert gate['details']['remaining_full_p6_hole_levels'] == []
for ext in ('md', 'html'):
    archive = ROOT/f'{ARCHIVE}.{ext}'
    if not archive.exists():
        previous = ROOT/f'{NAME}.{ext}'
        assert previous.stat().st_size > 500_000, 'Archive the original collection before overwriting'
        shutil.copy2(previous, archive)

source = HERE/'seminar_zh.md'
md = source.read_text(encoding='utf-8')
math_count = 0
pattern = re.compile(r'\$\$([\s\S]*?)\$\$|(?<![\\$])\$(?!\$)([^\n$]+?)(?<!\\)\$(?!\$)')
def formula(m):
    global math_count
    tex = (m[1] if m[1] is not None else m[2]).strip()
    display = m[1] is not None
    # latex2mathml does not implement aligned; an equivalent two-column array
    # preserves both row breaks and the alignment at the equality sign.
    render_tex = tex.replace(r'\begin{aligned}', r'\begin{array}{rl}').replace(r'\end{aligned}', r'\end{array}')
    rendered = convert(render_tex, display='block' if display else 'inline')
    math_count += 1
    tag = 'div' if display else 'span'
    cls = 'math-block' if display else 'math-inline'
    # Literal pipes inside MathML must not be interpreted as Markdown table delimiters.
    return (f'<{tag} class="{cls}" title="{html.escape(tex, quote=True)}">'
            f'{rendered}</{tag}>').replace('|', '&#124;')

engine = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists'])
body = engine.convert(pattern.sub(formula, md))
soup = BeautifulSoup(body, 'html.parser')
assert len(soup.find_all('math')) == math_count
for matrix in soup.find_all('mtable'):
    row = matrix.find('mtr', recursive=False)
    if row:
        cells = row.find_all('mtd', recursive=False)
        if cells and all(cell.has_attr('columnalign') for cell in cells):
            matrix['columnalign'] = ' '.join(cell['columnalign'] for cell in cells)
broken = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if href.startswith('https://'):
        a['rel'] = 'noreferrer'
    elif href.startswith('#'):
        assert soup.find(id=href[1:])
    else:
        p = ROOT / unquote(href.split('#')[0])
        if not p.is_file():
            broken.append(href)
assert not broken, broken
for p in soup.find_all('p'):
    first = p.find('strong', recursive=False)
    if first and first.get_text().startswith(('猜想 ', '定理 ', '推论 ', '引理 ', '有限引理 ', '局部命题')):
        p['class'] = ['statement']
for table in soup.find_all('table'):
    table.wrap(soup.new_tag('div', attrs={'class':'table-scroll'}))
toc = '\n'.join(f'<a href="#{h["id"]}">{html.escape(h.get_text())}</a>' for h in soup.find_all('h2'))
css = '''
:root{color-scheme:light;--ink:#1b2834;--accent:#185c65;--line:#d7e0e3}
*{box-sizing:border-box}html{scroll-padding-top:28px}
body{margin:0;background:#f3f5f6;color:var(--ink);font-family:"Microsoft YaHei","Noto Sans CJK SC",sans-serif;font-size:17px;line-height:1.95}
aside{position:fixed;left:28px;top:42px;width:190px;font-size:14px}
.brand{font-size:12px;letter-spacing:2px;color:#57717b;margin-bottom:20px;font-weight:700}
nav a{display:block;color:#465c66;padding:9px 10px;text-decoration:none;border-left:2px solid transparent;line-height:1.6}
nav a:hover,nav a.active{background:#e5edef;color:var(--accent);border-color:var(--accent)}
.actions{display:flex;gap:14px;margin-top:25px;padding-left:10px;font-size:13px}
button{border:0;background:none;color:var(--accent);font:inherit;cursor:pointer;padding:0}
main{max-width:1130px;margin:32px 32px 60px 244px;padding:48px 56px 64px;background:white;border:1px solid var(--line)}
h1{font-size:34px;line-height:1.45;letter-spacing:1px;margin:0 0 38px;font-weight:650}
h2{font-size:23px;font-weight:650;line-height:1.5;margin:48px 0 20px;padding-top:9px;border-top:1px solid var(--line)}
h3{font-size:19px;margin:32px 0 18px;line-height:1.6}
p{margin:15px 0;text-align:justify}strong{font-weight:650}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px;overflow-wrap:anywhere}
.statement{background:#f4f8f8;border-left:3px solid #659394;padding:12px 17px;margin-top:24px}
.math-block{overflow-x:auto;overflow-y:hidden;text-align:center;padding:14px 3px;margin:18px 0;max-width:100%;font-size:1.08em}
math{font-family:"Cambria Math","STIX Two Math",math}.math-inline{white-space:nowrap}
mtd[columnalign="left"]{text-align:left}mtd[columnalign="right"]{text-align:right}
.table-scroll{overflow-x:auto;max-width:100%;margin:23px 0}
table{border-collapse:collapse;width:100%;min-width:650px;font-size:14px;line-height:1.75}
th{background:#eaf1f2;color:#294c56;text-align:left;font-weight:650}
td,th{padding:12px 13px;vertical-align:top;border-bottom:1px solid var(--line)}
tr:nth-child(even) td{background:#fafcfc}td:first-child{white-space:nowrap}
ol{padding-left:1.6em}li{margin:9px 0}h2,h3,.statement{break-after:avoid}
@media(min-width:1500px){main{margin-left:auto;margin-right:auto;width:1130px}aside{left:calc(50% - 795px)}}
@media(max-width:1100px){aside{left:16px;width:165px}main{margin-left:198px;margin-right:20px;padding:34px 30px}body{font-size:16px}h1{font-size:29px}}
@media(max-width:760px){aside{position:static;width:auto;margin:20px 18px 12px}.brand{margin-bottom:8px}nav{display:flex;gap:4px 12px;flex-wrap:wrap}nav a{padding:3px 0;border:0;font-size:12px}.actions{margin-top:10px;padding:0}main{margin:14px 12px 30px;padding:26px 20px;border:0}h1{font-size:27px;margin-bottom:28px}h2{font-size:21px;margin-top:34px}p{text-align:left}.math-block{font-size:1em}.statement{padding:10px 12px}}
@media print{@page{size:A4;margin:19mm 18mm}body{background:white;font-family:"SimSun",serif;font-size:11pt;line-height:1.7}aside{display:none}main{margin:0;padding:0;max-width:none;border:0}h1{font-size:22pt}h2{font-size:15pt;margin-top:24pt}h3{font-size:12pt}table{font-size:9pt;min-width:0}td,th{padding:6px}a{color:inherit;text-decoration:none}.statement{background:none}.math-block{overflow:visible;font-size:1em}.table-scroll{overflow:visible}tr{break-inside:avoid}}
'''
page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>超立方体匹配的 Hamilton 延拓 · 组会讲稿</title><style>{css}</style></head>
<body><aside><div class="brand">Q₆ · 组会讲稿</div><nav>{toc}</nav>
<div class="actions"><a href="{NAME}.md">Markdown</a><button onclick="window.print()">打印</button></div></aside>
<main>{soup}</main>
<script>
const links=[...document.querySelectorAll('nav a')];
const observer=new IntersectionObserver(entries=>{{for(const e of entries)if(e.isIntersecting){{for(const a of links)a.classList.toggle('active',a.hash==='#'+e.target.id)}}}},{{rootMargin:'0px 0px -65% 0px'}});
document.querySelectorAll('main h2').forEach(h=>observer.observe(h));
</script></body></html>'''
(ROOT/f'{NAME}.md').write_text(md, encoding='utf-8')
(ROOT/f'{NAME}.html').write_text(page, encoding='utf-8')
assert all(sha(R/n) == value for n,value in frozen.items())
assert len(soup.find_all('table')) == 2
manifest = {
    'edition':'concise seminar manuscript', 'source_sha256':sha(source),
    'math_count':math_count, 'section_count':len(soup.find_all('h2')),
    'tables':2, 'broken_local_links':broken, 'frozen_inputs_unchanged':frozen,
    'outputs':{f'{NAME}.{ext}':{'sha256':sha(ROOT/f'{NAME}.{ext}'),
                             'bytes':(ROOT/f'{NAME}.{ext}').stat().st_size} for ext in ('md','html')},
    'archives':{f'{ARCHIVE}.{ext}':sha(ROOT/f'{ARCHIVE}.{ext}') for ext in ('md','html')}
}
(HERE/'SEMINAR_BUILD_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'math':math_count,'tables':2,'local_links':'PASS','outputs':manifest['outputs']},ensure_ascii=False))
