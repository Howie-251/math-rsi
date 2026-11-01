#!/usr/bin/env python3
"""Offline reader for the complete new eight- and nine-uniform proofs."""
from datetime import datetime,timezone
import json,re,tempfile
from pathlib import Path
from urllib.parse import unquote,urlsplit
from render_general_growth import ROOT,aris,embed_math,normalize_math,source_math_inputs,reader_links,prepare_reader_source
from render_propertyb_general import normalized_math_counter
from render_m6_ge67 import template as six_template
BASE=ROOT/'context/propertyb-small-updates-20261029'
TRACE=BASE/'render-8-9'
OUT=ROOT/'M8_M9_IMPROVEMENTS.html'
EIGHT=ROOT/'context/propertyb-m8-267-20261029/PROOF_M8_GE267.md'
NINE=ROOT/'context/propertyb-m9-543-20261029/PROOF_M9_GE543.md'
GENERIC=ROOT/'propertyB_small_k/propertyB_k8_k9_proof.md'
REVIEW=BASE/'reviews-8-9/DISPOSITION.md'
ANCHORS={EIGHT.resolve():'#eight-proof',NINE.resolve():'#nine-proof',GENERIC.resolve():'#generic-probability'}

def pretty_nine(raw):
    expressions={
      '8d(x)=Σy≠xλxy≥v−1':r'8d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1',
      'v⌈(v−1)/8⌉≤4878':r'v\lceil(v-1)/8\rceil\le4878',
      '195⌈194/8⌉=4875≤4878':r'195\lceil194/8\rceil=4875\le4878',
      '196⌈195/8⌉=4900>4878':r'196\lceil195/8\rceil=4900>4878',
      'max542p(v)=6233/6307<1':r'\max542p(v)=6233/6307<1',
      'r+2e(G)≤Tr−8Z':r'r+2e(G)\le Tr-8Z',
      'α(G)≥r²/(Tr−8Z)':r'\alpha(G)\ge r^2/(Tr-8Z)',
    }
    chunks=re.split(r'(```[^\n]*\n.*?\n```|\$\$.*?\$\$|\$(?!\$).*?\$|`[^`\n]+`)',raw,flags=re.S)
    for i in range(0,len(chunks),2):
        text=chunks[i]
        for old,tex in expressions.items():text=text.replace(old,'$'+tex+'$')
        sub=re.split(r'(\$[^$]+\$)',text)
        for j in range(0,len(sub),2):
            t=sub[j]
            t=re.sub(r'λ([A-Za-z][A-Za-z0-9]*)',lambda m:r'$\lambda_{'+m[1]+'}$',t)
            t=re.sub(r'ℓ([A-Za-z0-9]+)',lambda m:r'$\ell_{'+m[1]+'}$',t)
            t=re.sub(r'(?<![A-Za-z0-9_])(e|f|w)h\((T(?:,U)?)\)',lambda m:'$'+m[1]+'_{h}('+m[2]+')$',t)
            t=re.sub(r'(?<![A-Za-z0-9_])(xj|pj|Dj|DR|qR|δ0)(?![A-Za-z0-9_])',lambda m:'$'+{'xj':'x_j','pj':'p_j','Dj':'D_j','DR':'D_R','qR':'q_R','δ0':r'\delta_0'}[m[1]]+'$',t)
            sub[j]=t.replace('$$','$ $')
        chunks[i]=''.join(sub)
    return ''.join(chunks)

def links(text,path):
    text=reader_links(text,path)
    def replacement(m):
        target=m[2]
        if target.startswith(('http:','https:','mailto:','#')):return m[0]
        candidate=(ROOT/unquote(urlsplit(target).path)).resolve()
        if candidate in ANCHORS:return f'[{m[1]}]({ANCHORS[candidate]})'
        if not candidate.exists() and (path.parent/target).resolve().is_relative_to(ROOT):target=(path.parent/target).resolve().relative_to(ROOT).as_posix()
        return f'[{m[1]}]({target})'
    return re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',replacement,text)

def section(raw,path,label):
    formatted=normalize_math(pretty_nine(raw) if path==NINE else raw)
    assert not (normalized_math_counter(source_math_inputs(normalize_math(raw)))-normalized_math_counter(source_math_inputs(formatted))),path
    formatted=links(formatted,path)
    return re.sub(r'(?m)^(#{1,5}) (.*)$',lambda m:'#'*min(6,max(3,len(m[1])+1))+' '+label+' · '+m[2],formatted)

def compose():
    general=GENERIC.read_text();begin=general.index('## 2. Generic conditioned greedy bound');end=general.index('\n## 3.',begin);general=general[begin:end].strip()+'\n'
    sources=[(GENERIC,general,'§2 only: generic conditional-permutation probability'),(EIGHT,EIGHT.read_text(),'full proof'),(NINE,NINE.read_text(),'full proof')]
    intro=r'''<div class="result-strip"><div><span>八元 · 相对基线 263</span><strong>m(8) ≥ 267 · 增加 4</strong><small>任意 266 条八元边均可二染色</small></div><div><span>九元 · 相对基线 538</span><strong>m(9) ≥ 543 · 增加 5</strong><small>任意 542 条九元边均可二染色</small></div></div>

<p class="proof-status">完整计算机辅助证明 · 独立全域重建与全概率复算 · 尚未 Lean</p>

本卷给出两项针对任意有限简单超图的完整证明：$m(8)\ge267$ 与 $m(9)\ge543$。点对覆盖、点数和度数条件均由同一实际最小反例内部推出；原始输入只要求有限、简单且每条边具有指定大小。

## 两项原始命题与验证范围

**八元定理。** 任意有限简单八元超图，若边数至多266，则存在使每条原边同时含红、蓝两色的染色。因此 $m(8)\ge267$。

**九元定理。** 任意有限简单九元超图，若边数至多542，则存在使每条原边同时含红、蓝两色的染色。因此 $m(9)\ge543$。

|结果|本卷固定参考基线|下界增益|全部独立概率复算|内部完整点数域|
|---|---:|---:|---:|---|
|$m(8)\ge267$|263|4|2094型，另299项组件配额|47–120|
|$m(9)\ge543$|538|5|3450型|57–195|

以下先收入通用条件排列的完整概率公式，再完整收入两份证明。两项均已完成独立全域重建和全概率复算，Grok与Gemini的整篇静态审阅均未发现实质缺口；准确范围见文末审阅记录，尚无 Lean 形式证明。
'''
    body=[intro,'<a id="generic-probability"></a>\n\n## 通用条件排列概率：完整公式\n\n'+section(general,GENERIC,'通用'),'<a id="eight-proof"></a>\n\n## 八元：完整证明\n\n'+section(sources[1][1],EIGHT,'八元'),'<a id="nine-proof"></a>\n\n## 九元：完整证明\n\n'+section(sources[2][1],NINE,'九元'),r'''## 独立核验、证书与复现

八元证明的47–120点完整实际参数域、全部2094型概率及299项七元链接组件配额已由另一套实现重建并精确复算；所有有理值与提交证书逐项相等，且均严格小于一。详见[八元独立审阅](context/propertyb-m8-267-20261029/independent/REVIEW.md)、[完整核验记录](context/propertyb-m8-267-20261029/independent/CHECK.json)和[原始精确证书](context/propertyb-m8-267-20261029/CERTIFICATE.json)。

九元证明的57–195点完整决策树已由不导入作者数值或域生成模块的实现独立重建，包括319次一锁分流测试、1702次二锁分流测试及73个实际条件三锁父型。全部3450个成功叶以具名自由顶点的下降阶乘注入计数复算，逐项精确相等且严格。详见[九元独立审阅](context/propertyb-m9-543-20261029/independent/REVIEW.md)、[完整核验记录](context/propertyb-m9-543-20261029/independent/CHECK.json)和[原始成功叶](context/propertyb-m9-543-20261029/CANDIDATE.json)。

这里的“独立”指不同概率实现与完整输入域重建，不表示第二台机器复现或形式化内核认证。两项仍使用所列条件贪心数学机制及普通精确整数／有理数软件信任；完整证明已在使用处写明实际选点、迹分类和合法扣除。联合静态终审的实际范围见[审阅处置](context/propertyb-small-updates-20261029/reviews-8-9/DISPOSITION.md)，原[审阅范围](context/propertyb-small-updates-20261029/reviews-8-9/REQUEST.md)一并保留。

复算命令：

```sh
python3 context/propertyb-m8-267-20261029/independent/check.py
python3 context/propertyb-m9-543-20261029/independent/check.py
```
''']
    manifest=[dict(path=p.relative_to(ROOT).as_posix(),scope=scope,originalFormulaCount=len(source_math_inputs(normalize_math(raw))),readerFormulaCount=len(source_math_inputs(section(raw,p,'记录'))),originalFormulaePreserved=True) for p,raw,scope in sources]
    return '\n\n'.join(body).strip()+'\n',manifest

def template(name):
    text=six_template(name).replace('目录 · 九节正文与分支证明','目录 · 两项完整证明与通用公式')
    text=re.sub(r'<footer class="aris-footer">[\s\S]*?</footer>','<footer class="aris-footer"><a href="'+EIGHT.relative_to(ROOT).as_posix()+'">八元规范证明</a> · <a href="'+NINE.relative_to(ROOT).as_posix()+'">九元规范证明</a></footer>',text,count=1)
    return text.replace('</style>','''
.result-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.result-strip strong{font-size:24px}.result-strip>div:nth-child(2){border-color:#245b60;background:#edf1eb}main h3{font-size:24px;margin-top:42px}main h4{font-size:20px}
@media(max-width:700px){.result-strip{grid-template-columns:1fr}.result-strip strong{font-size:21px}main h3{font-size:22px}header.hero h1{font-size:29px}}
</style>''',1)

def browser_check(expected):
    from playwright.sync_api import sync_playwright
    result={}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        for name,width,height in [('desktop',1440,1000),('phone',390,844)]:
            page=browser.new_page(viewport={'width':width,'height':height});requests=[];errors=[]
            page.route('http://**/*',lambda r:r.abort());page.route('https://**/*',lambda r:r.abort())
            page.on('request',lambda req:requests.append(req.url) if req.url.startswith(('http:','https:')) else None);page.on('pageerror',lambda e:errors.append(str(e)))
            page.goto(OUT.as_uri(),wait_until='load');page.evaluate('document.fonts.ready');page.screenshot(path=str(TRACE/f'{name}-top.png'))
            for anchor,label in [('#generic-probability','generic'),('#eight-proof','eight'),('#nine-proof','nine')]:
                page.locator(anchor).scroll_into_view_if_needed();page.screenshot(path=str(TRACE/f'{name}-{label}.png'))
            report=page.evaluate(r'''()=>{
              const ids=[...document.querySelectorAll('[id]')].map(e=>e.id),idset=new Set(ids),clone=document.querySelector('main').cloneNode(true);clone.querySelectorAll('mjx-container,pre,code').forEach(e=>e.remove());
              return {formulaCount:document.querySelectorAll('mjx-container').length,svgCount:document.querySelectorAll('mjx-container>svg').length,tex:[...document.querySelectorAll('mjx-container')].map(e=>e.dataset.tex),
              mathErrors:[...document.querySelectorAll('[data-mml-node="merror"],mjx-merror')].map(e=>e.textContent),scripts:document.scripts.length,
              externalAssets:[...document.querySelectorAll('script[src],link[href],img[src]')].map(e=>e.src||e.href).filter(s=>/^https?:/.test(s)),pageOverflow:document.documentElement.scrollWidth>innerWidth+1,
              brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].map(e=>e.getAttribute('href')).filter(s=>s.length>1&&!idset.has(decodeURIComponent(s.slice(1)))),
              localLinks:[...document.querySelectorAll('a[href]')].map(e=>e.getAttribute('href')).filter(s=>!/^https?:|^mailto:|^#/.test(s)),
              rawDisplayDelimiters:/\\\[|\\\]|\\\(|\\\)|\$\$/.test(clone.textContent),duplicateIds:ids.filter((s,i)=>ids.indexOf(s)!==i),
              subscriptNodes:document.querySelectorAll('[data-mml-node="msub"],[data-mml-node="msubsup"]').length,placeholderLeak:/\{\{[A-Z_]+\}\}|\uE000|\uE001/.test(document.body.textContent),sourceFingerprints:document.querySelectorAll('meta[name="aris:source-sha256"]').length};
            }''')
            tex=report.pop('tex');report.update(expectedFormulaCount=len(expected),mathInputsMatch=normalized_math_counter(tex)==normalized_math_counter(expected),mathOrderMatches=[re.sub(r'\s+','',t) for t in tex]==[re.sub(r'\s+','',t) for t in expected],networkRequests=requests,pageErrors=errors)
            report['missingLocalLinks']=[s for s in report['localLinks'] if not (OUT.parent/unquote(urlsplit(s).path)).exists()]
            report['pendingReviewLinks']=[s for s in report['missingLocalLinks'] if s==REVIEW.relative_to(ROOT).as_posix()]
            report['unexpectedMissingLinks']=[s for s in report['missingLocalLinks'] if s not in report['pendingReviewLinks']]
            assert report['formulaCount']==report['svgCount']==len(expected)>0 and report['mathInputsMatch'] and report['mathOrderMatches'],report
            assert not any(report[k] for k in ['mathErrors','scripts','externalAssets','pageOverflow','brokenAnchors','rawDisplayDelimiters','duplicateIds','placeholderLeak','sourceFingerprints','unexpectedMissingLinks','networkRequests','pageErrors']),report
            assert report['subscriptNodes']>0
            result[name]=report;page.close()
        browser.close()
    return result

def main():
    TRACE.mkdir(parents=True,exist_ok=True);body,manifest=compose();source=TRACE/'reader-source.md';source.write_text(body);expected=source_math_inputs(body)
    (TRACE/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    aris.sha256_of=lambda _:'';aris.load_template=template;aris.strip_frontmatter=prepare_reader_source
    with tempfile.TemporaryDirectory(prefix='m8-m9-reader-',dir=ROOT) as tmp:
        stage=Path(tmp)/'reader.html';aris.main([str(source),'--out',str(stage),'--template','academic','--title','八元与九元超图的 Property B 下界','--eyebrow','PROPERTY B · EIGHT- AND NINE-UNIFORM HYPERGRAPHS','--subtitle','m(8) ≥ 267，m(9) ≥ 543 · 两项完整证明与独立精确复算','--lang','zh-CN'])
        math=embed_math(stage,OUT,EIGHT)
    assert normalized_math_counter(math['mathInputs'])==normalized_math_counter(expected)
    from itertools import count
    ids=count(1);OUT.write_text(re.sub(r'id="mjx-eqn:[^"]+"',lambda _:f'id="equation-{next(ids)}"',OUT.read_text()))
    (TRACE/'math-build.json').write_text(json.dumps(math,ensure_ascii=False,indent=2)+'\n')
    report=browser_check(expected);report.update(generatedAt=datetime.now(timezone.utc).isoformat(),sources=manifest,formulaCount=math['math'],html=OUT.name)
    (TRACE/'browser-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f'Rendered {OUT.name}: {math["math"]} offline SVG formulae, three canonical sources, desktop/phone checks passed.')
if __name__=='__main__':main()
