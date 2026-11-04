"""Build a self-contained Chinese reading edition without changing frozen proofs."""
from pathlib import Path
import hashlib
import html
import json
import re
import sys
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
R = HERE.parent
ROOT = R.parent.parent
sys.path.insert(0, str(HERE / 'vendor'))
import markdown
from bs4 import BeautifulSoup
from latex2mathml.converter import convert

NAME = 'Ruskey-Savage_Q6_研究报告'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return p.read_text(encoding='utf-8-sig')


def subchapter(s, chapter):
    lines = s.splitlines()[1:]
    out = []
    for line in lines:
        if line.startswith('## '):
            title = line[3:]
            title = re.sub(r'^(\d+)\.', lambda m: f'{chapter}.{m[1]}', title)
            line = '### ' + title
        elif line.startswith('### '):
            line = '#' + line
        out.append(line)
    return '\n'.join(out).strip()


final = json.loads(read(R / 'P6_FULL_REVIEW.json'))
assert final['verdict'] == 'PASS' and final['details']['full_P6_proved']
assert final['details']['remaining_full_p6_hole_levels'] == []
corollary = json.loads(read(R / 'SIX_DIRECTION_CYCLE_COROLLARIES_REVIEW.json'))
assert corollary['verdict'] == 'PASS'
for name, digest in corollary['audited_input_hashes'].items():
    assert sha(R / name) == digest.removeprefix('sha256:'), name

check = json.loads(read(R / 'P6_FULL_REVIEW_check.json'))
assert check['stage'] == 'final' and not check['errors']
nodes = check['review_nodes']
proofs = {'P6_FULL_CLOSURE.md', 'SIX_DIRECTION_CYCLE_COROLLARIES.md'}
reviews = {'P6_FULL_REVIEW.md', 'SIX_DIRECTION_CYCLE_COROLLARIES_REVIEW.md',
           'RUSKEY_SAVAGE_REPORT_SEMANTIC_REVIEW.md'}
owners = {}
for n in nodes:
    d = json.loads(read(R / n))
    for field in ('audited_input_hashes', 'imported_dependency_hashes'):
        for name in d.get(field, {}):
            p = (R / name).resolve()
            if not p.is_relative_to(R) or p.suffix != '.md' or not p.exists():
                continue
            rel = p.relative_to(R).as_posix()
            if 'REVIEW' in p.name:
                reviews.add(rel)
            else:
                proofs.add(rel)
                owners.setdefault(rel, set()).add(n)
    human = R / n.replace('.json', '.md')
    if human.exists():
        reviews.add(human.relative_to(R).as_posix())

ordered = ['P6_FULL_CLOSURE.md', 'ROOTED_MAXIMAL_18_HOLES.md',
           'GENERAL_NEAR_PERFECT.md', 'FOUR_HOLE_FULL.md', 'SIX_HOLE_CLOSED.md',
           'EIGHT_HOLE_FULL_CLOSURE.md', 'TEN_HOLE_FULL_CLOSURE.md',
           'TWELVE_HOLE_FULL_CLOSURE.md', 'FOURTEEN_HOLE_FULL_CLOSURE.md',
           'SIXTEEN_EIGHTEEN_FULL_CLOSURE.md', 'SIX_DIRECTION_CYCLE_COROLLARIES.md']
ordered += sorted(proofs - set(ordered))
review_order = ['P6_FULL_REVIEW.md', 'SIX_DIRECTION_CYCLE_COROLLARIES_REVIEW.md']
review_order += sorted(reviews - set(review_order))
ids = {n: 'proof-' + Path(n).stem.lower().replace('_', '-') for n in ordered}
ids.update({n: 'review-' + Path(n).stem.lower().replace('_', '-') for n in review_order})
assert len(ids.values()) == len(set(ids.values()))

seed = read(HERE / 'main_proof_zh.md')
main = seed.replace('<!-- HISTORY -->', subchapter(read(R / 'RUSKEY_SAVAGE_HISTORY_SOURCES.md'), 1))
main = main.replace('<!-- COROLLARIES -->', subchapter(read(R / 'SIX_DIRECTION_CYCLE_COROLLARIES.md'), 3))
main = main.replace('<!-- APPENDICES -->', '')
main += ('\n\n中文正文另经独立子任务作范围与推导核对，两处转述条件补齐后通过；'
         '该编辑语义审读不替代原数学证明的有限证书审计，见 '
         '`RUSKEY_SAVAGE_REPORT_SEMANTIC_REVIEW.md`。\n')
main += '\n\n## 15. 展开原始证明与审计附录\n\n'
main += (f'本阅读版嵌入 **{len(ordered)} 份数学说明**与 **{len(review_order)} 份审计原文**。'
         '点击标题展开。附录原文保持历史措辞，部分仍写着当时的待审状态；'
         '应结合最终接受报告理解其当前地位。原始文件未被此阅读版修改。'
         '这里纳入的是依赖图绑定的数学说明，其中的诊断性或局部材料仍只按关联审计实际使用的范围引用。\n\n')

appendix = []
html_documents = []
bindings = {}
for category, names in [('数学证明与局部构造', ordered), ('审计报告与接受范围', review_order)]:
    appendix.append(f'### {category}\n')
    for n in names:
        p = R / n
        original = read(p)
        bindings[n] = sha(p)
        title = original.splitlines()[0].lstrip('# ').strip()
        body = re.sub(r'^(#{1,6}) ', lambda m: '#' * min(6, len(m[1]) + 3) + ' ', original, flags=re.M)
        auditlinks = ', '.join(f'[{a}](research/six_directions/{quote(a)})' for a in sorted(owners.get(n, ())))
        provenance = f'原件：[打开文件](research/six_directions/{quote(n)})。SHA-256：`{bindings[n]}`。'
        if auditlinks:
            provenance += '\n\n关联审计（以其实际接受范围为准）：' + auditlinks + '。'
        html_documents.append((ids[n], n, title, provenance, body))
        appendix.append(f'<details id="{ids[n]}" class="source-doc" markdown="1">\n'
                        f'<summary>{html.escape(n)} — {html.escape(title)}</summary>\n\n'
                        f'{provenance}\n\n{body}\n\n</details>\n')

md = main + '\n\n' + '\n\n'.join(appendix)

# Link known inline file references; code blocks themselves remain verbatim.
def link_refs(s):
    def replace(m):
        label = m[1]
        if label in ids:
            return f'[{label}](#{ids[label]})'
        if (R / label).is_file() and not Path(label).is_absolute():
            return f'[{label}](research/six_directions/{quote(label)})'
        return m[0]
    chunks = re.split(r'(```[\s\S]*?```)', s)
    return ''.join(chunk if chunk.startswith('```') else re.sub(r'`([^`\n]+)`', replace, chunk)
                   for chunk in chunks)

md = link_refs(md)
(ROOT / (NAME + '.md')).write_text(md, encoding='utf-8')

math_errors = []
math_count = 0
math_pattern = re.compile(r'\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]|(?<![\\$])\$(?!\$)([^\n$]+?)(?<!\\)\$(?!\$)|\\\((.*?)\\\)')


def render_math(s):
    global math_count
    # Protect fenced/inline code from formula conversion.
    chunks = re.split(r'(```[\s\S]*?```|`[^`\n]+`)', s)
    def conv(m):
        global math_count
        tex = next(x for x in m.groups() if x is not None).strip()
        display = m[1] is not None or m[2] is not None
        try:
            rendered = convert(tex, display='block' if display else 'inline')
            math_count += 1
            wrapper = 'div' if display else 'span'
            cls = 'math-block' if display else 'math-inline'
            return f'<{wrapper} class="{cls}" title="{html.escape(tex, quote=True)}">{rendered}</{wrapper}>'.replace('|', '&#124;')
        except Exception as e:
            math_errors.append({'tex': tex, 'error': str(e)})
            return '<code class="math-fallback">' + html.escape(tex) + '</code>'
    return ''.join(chunk if chunk.startswith('`') else math_pattern.sub(conv, chunk) for chunk in chunks)


engine = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists'], extension_configs={
    'toc': {'permalink': False, 'toc_depth': '2-2'}})
content = engine.convert(render_math(link_refs(main)))
main_math_count = math_count
(HERE/'MAIN_RENDER_DEBUG.html').write_text(content, encoding='utf-8')
assert content.count('<math ') == main_math_count, ('Main-text formula lost during Markdown rendering', content.count('<math '), main_math_count)
formula_in_code = []
# Render each historical source separately: an unmatched raw HTML construct in
# a historical note must never consume later independent appendix documents.
for ident, name, title, provenance, body in html_documents:
    before = math_count
    local = markdown.markdown(render_math(link_refs(provenance + '\n\n' + body)),
                              extensions=['extra', 'sane_lists'])
    if local.count('<math ') != math_count-before:
        formula_in_code.append({'file': name, 'converted': math_count-before, 'raw_math_tags': local.count('<math ')})
    content += (f'<details id="{ident}" class="source-doc"><summary>'
                f'{html.escape(name)} — {html.escape(title)}</summary>{local}</details>')
soup = BeautifulSoup(content, 'html.parser')
assert len(soup.find_all('details', class_='source-doc')) == len(html_documents)
assert len(soup.find_all('math')) >= math_count-len(formula_in_code)
# Escaping raw mathematical less-than syntax in old plain-text notes is left to
# Markdown; all new formulas are converted above. Make local source links usable.
for a in soup.find_all('a', href=True):
    href = a['href']
    if not re.match(r'^(https?://|mailto:|#|research/)', href) and not re.match(r'^[A-Za-z]:', href):
        if (R / href).is_file():
            a['href'] = 'research/six_directions/' + quote(href)
    if href.startswith('https://'):
        a['rel'] = 'noreferrer'
for table in soup.find_all('table'):
    wrapper = soup.new_tag('div', attrs={'class': 'table-scroll'})
    table.wrap(wrapper)

toc = []
for h in soup.find_all('h2'):
    if h.get('id') and not h.find_parent('details'):
        toc.append(f'<a href="#{h["id"]}">{html.escape(h.get_text())}</a>')

css = '''
:root{--ink:#172c3a;--muted:#60717a;--paper:#fff;--line:#dde6e9;--accent:#087e83;--bg:#eef3f4}
*{box-sizing:border-box}html{scroll-padding-top:24px}body{margin:0;color:var(--ink);background:var(--bg);font:17px/1.85 "Segoe UI","Microsoft YaHei",sans-serif}
aside{position:fixed;inset:0 auto 0 0;width:274px;padding:32px 23px;background:#133541;color:#dcecef;overflow:auto}aside .brand{font-size:13px;letter-spacing:3px;color:#91c7cb}aside strong{display:block;font-size:24px;line-height:1.4;margin:12px 0 24px}nav a{display:block;color:#d7e5e7;text-decoration:none;font-size:13px;padding:8px 0;border-bottom:1px solid #ffffff12}nav a:hover{color:white}button,input{font:inherit}button{cursor:pointer;border:1px solid var(--line);border-radius:7px;padding:7px 12px;background:white;color:var(--ink);font-size:13px}aside button{margin-top:18px;background:#ffffff12;color:white;border-color:#ffffff40}
main{margin:35px 35px 65px 309px;background:var(--paper);max-width:1200px;padding:48px 58px;border:1px solid var(--line);border-radius:12px;box-shadow:0 8px 28px #0b293306}h1{font-size:36px;line-height:1.35;margin:12px 0 25px;letter-spacing:-.7px}h2{font-size:26px;border-top:1px solid var(--line);padding-top:34px;margin-top:46px;line-height:1.45}h3{font-size:20px;color:#12616a;margin-top:30px}h4,h5,h6{font-size:17px}p{margin:15px 0}a{color:#08777f;text-underline-offset:3px;overflow-wrap:anywhere}strong{font-weight:650}.kicker{font-size:12px;letter-spacing:2px;color:var(--accent);font-weight:700}.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:26px}.chips span{font-size:12px;background:#ecf6f5;color:#155e64;border:1px solid #cfe7e4;border-radius:20px;padding:3px 11px}.table-scroll{overflow:auto;margin:20px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.65}th,td{border:1px solid var(--line);padding:11px 13px;text-align:left;vertical-align:top}th{background:#eff7f7;color:#214c57}tr:nth-child(even){background:#fbfcfc}blockquote{border-left:4px solid var(--accent);margin:20px 0;padding:2px 20px;background:#f1f8f8}code{font:13px/1.6 Consolas,monospace;overflow-wrap:anywhere;background:#f0f4f5;padding:2px 4px;border-radius:3px}pre{overflow:auto;border:1px solid var(--line);background:#f5f8f9;padding:16px;border-radius:8px;white-space:pre-wrap}pre code{background:none;padding:0}.math-block{overflow-x:auto;padding:15px 0;max-width:100%}.math-inline math{font-size:1.03em}math{font-family:"Cambria Math","STIX Two Math",math}.math-fallback{background:#fff3d5}.source-doc{border:1px solid var(--line);border-radius:8px;margin:12px 0;padding:0 20px}.source-doc summary{cursor:pointer;list-style-position:outside;padding:15px 4px;font:14px/1.6 Consolas,"Microsoft YaHei",sans-serif;color:#25525c;overflow-wrap:anywhere}.source-doc[open]{padding-bottom:22px}.source-doc[open] summary{border-bottom:1px solid var(--line);margin-bottom:20px}.source-doc p,.source-doc li{font-size:15px}.source-doc h4{color:#185b65}.source-doc table{font-size:12px}.appendix-toolbar{background:#f1f7f7;padding:15px;border-radius:8px;display:flex;gap:9px;flex-wrap:wrap;margin-top:20px}.appendix-toolbar input{width:min(420px,100%);border:1px solid #c6d8dc;padding:8px 11px;border-radius:5px;font-size:14px}.appendix-toolbar small{display:block;flex-basis:100%;color:var(--muted)}footer{color:var(--muted);border-top:1px solid var(--line);margin-top:45px;padding-top:20px;font-size:12px}
@media(max-width:1100px){aside{width:225px;padding:25px 18px}main{margin-left:245px;padding:32px}}@media(max-width:760px){aside{position:static;width:auto;padding:22px}aside strong{font-size:22px;margin:8px 0}nav{display:none}aside button{margin-top:6px}main{margin:14px;padding:22px 18px}h1{font-size:28px}h2{font-size:23px}body{font-size:16px}}
@media print{body{background:white;font-size:11pt}aside,.appendix-toolbar,.source-doc,button{display:none!important}main{margin:0;padding:0;border:0;max-width:none;box-shadow:none}h1{font-size:24pt}h2{font-size:18pt;break-after:avoid}h3{break-after:avoid}a{color:inherit;text-decoration:none}table{font-size:9pt}pre{white-space:pre-wrap}.table-scroll{overflow:visible}.math-block{overflow:visible}}
'''
js = '''
const docs=[...document.querySelectorAll('.source-doc')];
const section=document.querySelector('#appendix-tools');
section.querySelector('input').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();let shown=0;for(const d of docs){const ok=!q||d.textContent.toLowerCase().includes(q);d.hidden=!ok;if(ok)shown++;}document.querySelector('#filter-count').textContent=`显示 ${shown} / ${docs.length} 份附录`;});
document.querySelector('#collapse').addEventListener('click',()=>docs.forEach(d=>d.open=false));
function revealHash(){const id=decodeURIComponent(location.hash.slice(1));const t=document.getElementById(id);if(!t)return;let p=t;while(p){if(p.tagName==='DETAILS'){p.open=true;p.hidden=false;}p=p.parentElement;}setTimeout(()=>t.scrollIntoView({block:'start'}),20);}
window.addEventListener('hashchange',revealHash);if(location.hash)revealHash();
document.querySelector('#print-main').addEventListener('click',()=>window.print());
'''
toolbar = f'''<div id="appendix-tools" class="appendix-toolbar"><input type="search" aria-label="搜索证明附录" placeholder="搜索附录文件名或正文，例如 FINAL25"><button id="collapse">折叠全部附录</button><small id="filter-count">显示 {len(ids)} / {len(ids)} 份附录 · 公式离线可读 · 打印功能只打印正文</small></div>'''
first_details = soup.find('details')
if first_details:
    first_details.insert_before(BeautifulSoup(toolbar, 'html.parser'))
page = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
page += '<title>Ruskey–Savage 猜想与 Q6 的计算辅助证明</title><style>' + css + '</style></head><body>'
page += '<aside><div class="brand">HYPERCUBE RESEARCH</div><strong>Ruskey–Savage<br>与六维核心证明</strong><nav>' + ''.join(toc) + '</nav><button id="print-main">打印正文 / 保存 PDF</button></aside>'
page += '<main><div class="kicker">研究阅读版 · 2026 / 11 / 02</div><div class="chips"><span>Q6 · 64 个顶点</span><span>完整 P6</span><span>确定性有限证书</span><span>同族模型审计</span></div>'
page += str(soup) + '<footer>本页为离线阅读版；正文、数学说明与审计原文内嵌，外部文献及二进制证书通过链接定位。阅读版不会改写冻结证明。MathML 公式由浏览器原生显示。</footer></main><script>' + js + '</script></body></html>'
out = ROOT / (NAME + '.html')
out.write_text(page, encoding='utf-8')
manifest = {
    'date': '2026-11-02', 'proof_documents': len(ordered), 'review_documents': len(review_order),
    'math_converted': math_count, 'math_conversion_errors': math_errors,
    'main_math_converted': main_math_count, 'appendix_formula_in_code': formula_in_code,
    'frozen_P6_review_sha256': sha(R / 'P6_FULL_REVIEW.json'),
    'main_source_sha256': sha(HERE / 'main_proof_zh.md'),
    'embedded_source_hashes': bindings,
    'outputs': {p.name: {'sha256': sha(p), 'bytes': p.stat().st_size} for p in [ROOT / (NAME + '.md'), out]},
}
(HERE / 'REPORT_BUILD_MANIFEST.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k:v for k,v in manifest.items() if k != 'embedded_source_hashes'}, ensure_ascii=True))
