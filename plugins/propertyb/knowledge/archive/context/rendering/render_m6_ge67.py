#!/usr/bin/env python3
"""Single-volume M6>=67 proof reader with offline SVG formulae."""
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit
from render_general_growth import (
    ROOT, aris, embed_math, normalize_math, source_math_inputs,
    reader_links, prepare_reader_source, general_reader_template,
)
from render_propertyb_general import normalized_math_counter

BASE=ROOT/'context/propertyb-m6-67-progress-20261029'
TRACE=BASE/'render'
MAIN=BASE/'PROOF_M6_GE67.md'
OUTPUT=ROOT/'M6_GE67.html'
APPENDICES=[
 ('a1','31–33点：完整分流与组件配额',BASE/'small31_33/REPORT.md',None),
 ('a2','34点：最小度九',BASE/'34_min9/REPORT.md',None),
 ('a3','34点：最小度十',BASE/'34_min10/PROOF.md',None),
 ('a4','34点：最小度十一',BASE/'34_min11/REPORT.md',None),
 ('a5','35点：最小度九',BASE/'root/PROOF35_MIN9.md',None),
 ('a6','35点：最小度十',BASE/'mid34_38/PROOF35_MIN10.md',None),
 ('a7','35点：最小度十一',BASE/'mid34_38/STATUS35.md','minimum-eleven'),
 ('a8','36–38点：完整实际分支',BASE/'mid34_38/PROOF36_38.md',None),
 ('a9','39点：弱四锁分支',BASE/'tail39_41/PROOF39.md',None),
 ('a10','40–41点：重选锁与完整分流',BASE/'tail39_41/PROOF40_41.md',None),
 ('a11','42–44点：尾部锁选择及完整迹',ROOT/'context/propertyb-m6-67-diagnosis-20261029/integer-lock/TAIL_SELECTION_REVIEW.md',None),
]
INTERNAL={p.resolve():f'#appendix-{key}' for key,_,p,_ in APPENDICES}
INTERNAL[MAIN.resolve()]='#main-proof'

def selection(path,scope):
    raw=path.read_text()
    if scope=='minimum-eleven':
        begin=raw.index('## The minimum-eleven case is complete')
        end=raw.index('\n## Two unit arms',begin)
        return raw[begin:end].strip()+'\n'
    return raw

def tex_plain(expression):
    expression=expression.strip().rstrip('。')
    expression=expression.replace(r'R⊆S\{j}',r'R\subseteq S\setminus\{j\}').replace('L={x:d(x)≤10}',r'L=\{x:d(x)\le10\}').replace('max_R',r'\max_R')
    expression=re.sub(r'λ([a-zA-Z][a-zA-Z0-9]*)',r'\\lambda_{\1}',expression)
    expression=re.sub(r'\bx([0-3])\b',r'x_{\1}',expression)
    for old,new in [('Σ',r'\sum'),('λ',r'\lambda'),('≥',r'\ge '),('≤',r'\le '),('−','-'),('·',r'\cdot '),('∈',r'\in '),('∉',r'\notin '),('∅',r'\varnothing'),('…',r'\ldots '),('，',r',\quad ')]:
        expression=expression.replace(old,new)
    expression=re.sub(r'\b(floor|ceil)\(',lambda m:r'\operatorname{'+m[1]+'}(',expression)
    return expression

def plain_math(text,path):
    # These three branch drafts use Unicode/plain-text mathematical notation.
    # Only typographical delimiters and equivalent TeX symbols are added here.
    if path.name not in ('PROOF35_MIN9.md','PROOF39.md','PROOF40_41.md'):
        return text
    text=re.sub(r'(?m)^    ([^\n]+)$',lambda m:'$$'+tex_plain(m[1])+'$$' if re.search(r'[=≥≤]|floor\(',m[1]) else m[0],text)
    standalone=[
      'E(t)=5t−114，p(t)=36−floor(E(t)/2)，D(t)=8+floor((108−t)/p(t))。',
      'Σ_{y∉S}e_y=5t−2·3−3·36=5t−114=E(t)。',
      '5f_R≤v−1−|R|+4B_R，',
      '2ceil((t−3)/2)>5t−200。',
    ]
    for expression in standalone:
        text=text.replace(expression,'$$'+tex_plain(expression.rstrip('，'))+'$$')
    snippets=[
      'v=35, M=66','v=39','v=40','v=41',
      'L={x:d(x)≤10}','Σ_{L}(11−d(x))≥11v−396',
      'q_R=max(0,ceil((5f_R−v+1+|R|)/4))≤B_R',
      'D_j=max_R D_{j,R}','Σ_h min(A_h,B_h,Q_h−D_h)',
      'R⊆S\\{j}','(T∪U)∩R=∅',
    ]
    parts=re.split(r'(\$\$.*?\$\$|\$(?!\$).*?\$|`[^`\n]+`)',text,flags=re.S)
    for i in range(0,len(parts),2):
        item=parts[i]
        for expression in snippets:
            item=item.replace(expression,'$'+tex_plain(expression)+'$')
        item=re.sub(r'λ[a-zA-Z][a-zA-Z0-9]*(?:[=≤≥][0-9]+)?',lambda m:'$'+tex_plain(m[0])+'$',item)
        parts[i]=item
    return ''.join(parts)

def source_links(text,path):
    text=reader_links(text,path)
    def replace(m):
        target=m[2]
        if target.startswith(('https:','http:','mailto:','#')):return m[0]
        filepart=unquote(urlsplit(target).path)
        candidate=(ROOT/filepart).resolve()
        if not candidate.exists() and (path.parent/filepart).resolve().is_relative_to(ROOT):
            candidate=(path.parent/filepart).resolve()
            target=candidate.relative_to(ROOT).as_posix()
        if candidate in INTERNAL:return f'[{m[1]}]({INTERNAL[candidate]})'
        return f'[{m[1]}]({target})'
    return re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',replace,text)

def compose():
    main=MAIN.read_text()
    pieces=[r'''<div class="result-strip"><div><span>六元超图下界</span><strong>64 → 67</strong><small>相对 64 增加 3</small></div><div><span>原始染色结论</span><strong>66 条边必可染</strong><small>任意有限简单六元超图</small></div><div><span>验证范围</span><strong>独立数值复算</strong><small>完整计算机辅助证明 · 尚未 Lean</small></div></div>

<p class="proof-status">完整计算机辅助证明 · 独立数值复算 · 尚未 Lean</p>

<a id="main-proof"></a>
''',source_links(normalize_math(main),MAIN).strip(),
'''## 分支证明全文

下列附录在本页内收入各实际分支的完整证明，不需跳转 Markdown 才能阅读。附录保留各稿形成时的状态说明；当前完整原题与验收范围以本卷首部及正文第9节为准。
''']
    manifest=[dict(path=MAIN.relative_to(ROOT).as_posix(),scope='full canonical text',formulaCount=len(source_math_inputs(normalize_math(main))),readerFormulaCount=len(source_math_inputs(normalize_math(main))),originalFormulaePreserved=True)]
    for key,label,path,scope in APPENDICES:
        raw=selection(path,scope)
        body=source_links(normalize_math(plain_math(raw,path)),path)
        assert not (normalized_math_counter(source_math_inputs(normalize_math(raw)))-normalized_math_counter(source_math_inputs(body))),path
        # Give every appendix its own heading namespace without changing its prose.
        body=re.sub(r'(?m)^(#{1,5}) (.*)$',lambda m:'#'*min(6,len(m[1])+2)+' '+key.upper()+' · '+m[2],body)
        pieces.append(f'<details class="proof-appendix" id="appendix-{key}">\n<summary>{key.upper()} · {label}</summary>\n\n'+body.strip()+'\n\n</details>')
        manifest.append(dict(path=path.relative_to(ROOT).as_posix(),scope=scope or 'full proof source',appendix=key,formulaCount=len(source_math_inputs(normalize_math(raw))),readerFormulaCount=len(source_math_inputs(body)),originalFormulaePreserved=True))
    return '\n\n'.join(pieces).strip()+'\n',manifest

def template(name):
    text=general_reader_template(name)
    # The caller explicitly requests no new fingerprints; source names suffice.
    text=re.sub(r'<meta name="aris:source-sha256"[^>]*>\s*','',text)
    text=re.sub(r'<details class="source-info">[\s\S]*?</details>','',text)
    text=re.sub(r'<div class="meta">[\s\S]*?</div>','',text,count=1)
    text=re.sub(r'<footer class="aris-footer">[\s\S]*?</footer>',
        '<footer class="aris-footer"><a href="'+MAIN.relative_to(ROOT).as_posix()+'">规范总证明</a> · 本卷包含全部分支证明全文</footer>',text,count=1)
    text=text.replace('</header>','</header><details class="mobile-toc"><summary>目录 · 九节正文与分支证明</summary>{{TOC_HTML}}</details>',1)
    return text.replace('</style>',r'''
.mobile-toc{display:none}
.result-strip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:28px 0 20px;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif}
.result-strip>div{padding:18px;background:#edf1eb;border-top:3px solid #245b60}
.result-strip>div:first-child{background:#f5ece3;border-color:#a44724}
.result-strip span,.result-strip strong,.result-strip small{display:block}
.result-strip span{font-size:12px;color:#52625c}.result-strip strong{font-size:23px;line-height:1.55;margin:6px 0;color:#245b60}.result-strip>div:first-child strong{color:#a44724}.result-strip small{font-size:12px;line-height:1.6;color:#52625c}
.proof-appendix{margin:18px 0;background:#fbfaf6;border:1px solid #ced6cc;border-radius:4px}
.proof-appendix>summary{font:600 16px/1.7 -apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;color:#245b60;padding:15px 17px;cursor:pointer}
.proof-appendix[open]{padding:0 18px 18px}.proof-appendix[open]>summary{margin:0 -18px 18px;border-bottom:1px solid #ced6cc}
.proof-appendix h3{font-size:23px}.proof-appendix h4{font-size:20px}.proof-appendix h5{font-size:18px}
main mjx-container:not([display="true"]){display:inline-block;max-width:100%;overflow-x:auto;overflow-y:hidden;vertical-align:middle}
main :not(pre)>code{white-space:normal;overflow-wrap:anywhere}
main p,main li{overflow-wrap:anywhere}main table{min-width:620px;font-size:14px}main .table-scroll{margin:20px 0}
nav.toc ol{white-space:normal;display:block}nav.toc ol li{margin:8px 0}
header.hero{margin-bottom:16px}header.hero h1{font-size:40px}
@media(max-width:700px){nav.toc{display:none}.mobile-toc{display:block;background:transparent;margin:12px 0 18px;border-color:#d4d8cc}.mobile-toc>summary{font-size:14px;padding:10px 12px}.mobile-toc ol{padding-left:27px;font-size:14px}.result-strip{grid-template-columns:1fr;gap:8px;margin:20px 0}.result-strip>div{padding:11px 15px}.result-strip strong{font-size:21px;margin:2px 0}.result-strip span,.result-strip small{font-size:12px}header.hero h1{font-size:29px}.proof-appendix[open]{padding:0 10px 14px}.proof-appendix[open]>summary{margin:0 -10px 14px}.proof-appendix>summary{font-size:15px;padding:12px 10px}main table{min-width:600px}}
</style>''',1)

def check_offline(expected):
    from playwright.sync_api import sync_playwright
    results={}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        for name,width,height in [('desktop',1440,1000),('phone',390,844)]:
            page=browser.new_page(viewport={'width':width,'height':height})
            requests=[];errors=[]
            page.route('http://**/*',lambda r:r.abort());page.route('https://**/*',lambda r:r.abort())
            page.on('request',lambda req:requests.append(req.url) if req.url.startswith(('http:','https:')) else None)
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.goto(OUTPUT.as_uri(),wait_until='load');page.evaluate('document.fonts.ready')
            page.screenshot(path=str(TRACE/f'{name}-top.png'))
            for label,index in [('probability',2),('assembly',7),('evidence',8)]:
                headings=page.locator('main > h2')
                if headings.count()>index:
                    headings.nth(index).scroll_into_view_if_needed();page.screenshot(path=str(TRACE/f'{name}-{label}.png'))
            page.locator('#appendix-a6').evaluate('(e)=>e.open=true');page.locator('#appendix-a6').scroll_into_view_if_needed();page.screenshot(path=str(TRACE/f'{name}-appendix-min10.png'))
            page.locator('details').evaluate_all('es=>es.forEach(e=>e.open=true)')
            r=page.evaluate(r'''()=>{
              const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);const idset=new Set(ids);
              const clone=document.querySelector('main').cloneNode(true);clone.querySelectorAll('mjx-container,pre,code').forEach(e=>e.remove());
              return {formulaCount:document.querySelectorAll('mjx-container').length,svgCount:document.querySelectorAll('mjx-container>svg').length,
                tex:[...document.querySelectorAll('mjx-container')].map(e=>e.dataset.tex),
                mathErrors:[...document.querySelectorAll('[data-mml-node="merror"],mjx-merror')].map(e=>e.textContent),
                scripts:document.scripts.length,externalAssets:[...document.querySelectorAll('script[src],link[href],img[src]')].map(e=>e.src||e.href).filter(s=>/^https?:/.test(s)),
                pageOverflow:document.documentElement.scrollWidth>innerWidth+1,
                brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].map(e=>e.getAttribute('href')).filter(s=>s.length>1&&!idset.has(decodeURIComponent(s.slice(1)))),
                localLinks:[...document.querySelectorAll('a[href]')].map(e=>e.getAttribute('href')).filter(s=>!/^https?:|^mailto:|^#/.test(s)),
                sourceMathDelimiters:/\\\[|\\\]|\\\(|\\\)|\$\$/.test(clone.textContent),
                appendixCount:document.querySelectorAll('details.proof-appendix').length,
                appendixFormulaCounts:[...document.querySelectorAll('details.proof-appendix')].map(e=>({id:e.id,count:e.querySelectorAll('mjx-container').length})),
                subscriptNodes:document.querySelectorAll('[data-mml-node="msub"],[data-mml-node="msubsup"]').length,
                placeholderLeak:/\{\{[A-Z_]+\}\}|\uE000|\uE001/.test(document.body.textContent),
                fingerprints:document.querySelectorAll('meta[name="aris:source-sha256"]').length,
                duplicateIds:ids.filter((s,i)=>ids.indexOf(s)!==i)
              };
            }''')
            tex=r.pop('tex');r['expectedFormulaCount']=len(expected)
            r['mathInputsMatch']=normalized_math_counter(tex)==normalized_math_counter(expected)
            r['mathOrderMatches']=[re.sub(r'\s+','',t) for t in tex]==[re.sub(r'\s+','',t) for t in expected]
            r['missingMath']=list((normalized_math_counter(expected)-normalized_math_counter(tex)).elements())
            r['networkRequests']=requests;r['pageErrors']=errors
            r['missingLocalLinks']=[s for s in r['localLinks'] if not (OUTPUT.parent/unquote(urlsplit(s).path)).exists()]
            r['pendingFinalReviewLinks']=[s for s in r['missingLocalLinks'] if s==str((BASE/'reviews/DISPOSITION.md').relative_to(ROOT))]
            r['unexpectedMissingLinks']=[s for s in r['missingLocalLinks'] if s not in r['pendingFinalReviewLinks']]
            results[name]=r
            assert r['formulaCount']==r['svgCount']==len(expected)>0,r
            assert r['mathInputsMatch'] and r['mathOrderMatches'],r
            assert not (r['mathErrors'] or r['scripts'] or r['externalAssets'] or requests or errors or r['pageOverflow'] or r['brokenAnchors'] or r['sourceMathDelimiters'] or r['placeholderLeak'] or r['fingerprints'] or r['unexpectedMissingLinks']),r
            assert r['appendixCount']==11 and r['subscriptNodes']>0,r
            page.close()
        browser.close()
    return results

def main():
    TRACE.mkdir(parents=True,exist_ok=True)
    body,manifest=compose();expected=source_math_inputs(body)
    source=TRACE/'reader-source.md';source.write_text(body)
    (TRACE/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    # Do not add an unnecessary source fingerprint for this reader.
    aris.sha256_of=lambda _:''
    aris.load_template=template;aris.strip_frontmatter=prepare_reader_source
    with tempfile.TemporaryDirectory(prefix='m6-ge67-',dir=ROOT) as tmp:
        stage=Path(tmp)/'reader.html'
        aris.main([str(source),'--out',str(stage),'--template','academic','--title','六元超图的 Property B：m(6) ≥ 67','--eyebrow','PROPERTY B · SIX-UNIFORM HYPERGRAPHS','--subtitle','任意有限简单六元超图，至多 66 条边必可二染色','--lang','zh-CN'])
        math_report=embed_math(stage,OUTPUT,MAIN)
    assert normalized_math_counter(math_report['mathInputs'])==normalized_math_counter(expected)
    # Repeated local equation numbers in different appendices need unique HTML ids.
    from itertools import count
    equation_ids=count(1)
    OUTPUT.write_text(re.sub(r'id="mjx-eqn:[^"]+"',lambda _:f'id="equation-{next(equation_ids)}"',OUTPUT.read_text()))
    (TRACE/'math-build.json').write_text(json.dumps(math_report,ensure_ascii=False,indent=2)+'\n')
    report=check_offline(expected)
    report.update(generatedAt=datetime.now(timezone.utc).isoformat(),output=OUTPUT.name,sources=manifest,formulaCount=math_report['math'])
    (TRACE/'browser-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'Rendered {OUTPUT.name}: {math_report["math"]} offline SVG formulae; {len(manifest)} sources; desktop/phone checked.')
if __name__=='__main__':main()
