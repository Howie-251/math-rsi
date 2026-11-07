from pathlib import Path
import json, time
from playwright.sync_api import sync_playwright

OUT = Path(__file__).parent
URL = (OUT.parent.parent / 'site/index.html').as_uri()
REPORT = {'checks': [], 'errors': [], 'screenshots': []}

def check(name, condition, evidence=None):
    REPORT['checks'].append({'name': name, 'pass': bool(condition), 'evidence': evidence})

def state(p):
    return p.evaluate('''() => ({version:document.querySelector('.axis-hit').getAttribute('aria-valuenow'),
      selected:[...document.querySelectorAll('#chips [aria-pressed="true"]')].map(e=>e.dataset.case),
      line:document.querySelector('.focus-line').getAttribute('points'),
      stroke:document.querySelector('.focus-line').style.stroke,
      lines:document.querySelectorAll('.focus-line').length,
      leaders:[...document.querySelectorAll('.delta-leader')].filter(e=>getComputedStyle(e).visibility==='visible').length,
      overview:document.querySelector('#overview')?.getAttribute('aria-pressed'),
      playing:document.querySelector('#play').dataset.s,
      visibleTags:[...document.querySelectorAll('.delta-tag')].filter(e=>getComputedStyle(e).visibility==='visible').map(e=>({id:e.dataset.bubble||e.dataset.c+':'+e.dataset.m,c:e.dataset.c,kind:e.dataset.kind||null,origin:e.classList.contains('trace-origin'),text:e.textContent}))})''')

def snap(p, name):
    p.locator('#evolution').scroll_into_view_if_needed()
    p.screenshot(path=str(OUT / (name + '.png')))
    REPORT['screenshots'].append(name + '.png')

def scroll_column(p, col):
    p.evaluate('col=>{const s=document.querySelector("#scroller"),stage=document.querySelector("#stage");s.scrollLeft=(80+232*col+116)*stage.clientWidth/1472-s.clientWidth/2}',col)

def geometry(p):
    return p.evaluate('''() => {
      const box=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,right:r.right,bottom:r.bottom,width:r.width,height:r.height}};
      const overlaps=(a,b)=>Math.min(a.right,b.right)-Math.max(a.x,b.x)>.8 && Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>.8;
      const bands=[...document.querySelectorAll('#sky .band')].map(box);
      const tags=[...document.querySelectorAll('.delta-tag')].filter(e=>getComputedStyle(e).visibility==='visible');
      const cards=tags.map(e=>({c:e.dataset.c,origin:e.classList.contains('trace-origin'),box:box(e.querySelector('.delta-surface')),text:[...e.querySelectorAll('text')].map(x=>({text:x.textContent,box:box(x)}))}));
      const cardFits=cards.map(c=>({...c,inBand:bands.some(b=>c.box.x>=b.x-.8&&c.box.right<=b.right+.8),textInside:c.text.every(t=>t.box.x>=c.box.x-.8&&t.box.right<=c.box.right+.8&&t.box.y>=c.box.y-.8&&t.box.bottom<=c.box.bottom+.8)}));
      const blocks=[...document.querySelectorAll('#sky .bk > .anim')].filter(e=>+getComputedStyle(e).opacity>.1).map(box);
      const counters=[...document.querySelectorAll('.result-count')].filter(e=>getComputedStyle(e).visibility==='visible').map(e=>({text:e.textContent,box:box(e)}));
      return {viewport:innerWidth,document:document.documentElement.scrollWidth,cards:cardFits,cardCounterOverlap:cards.flatMap(c=>counters.filter(b=>overlaps(c.box,b.box)).map(b=>({card:c.c,cardBox:c.box,counter:b}))),cardBlockOverlap:cards.flatMap(c=>blocks.filter(b=>overlaps(c.box,b)).map(b=>({card:c.c,origin:c.origin,cardBox:c.box,block:b}))),cardCardOverlap:cards.flatMap((c,i)=>cards.slice(i+1).filter(d=>overlaps(c.box,d.box)).map(d=>[c.c,d.c]))};
    }''')


def visible_dd_results(p):
    return p.evaluate('''()=>{const a=[...document.querySelectorAll('#sky .bk[data-c="dd"]')].filter(e=>[...e.querySelectorAll('.anim')].some(a=>+getComputedStyle(a).opacity>.99));const right=Math.max(...a.map(e=>e.transform.baseVal.getItem(0).matrix.e));return a.filter(e=>e.transform.baseVal.getItem(0).matrix.e===right).map(e=>e.textContent)}''')

def fit(p,label):
    g=geometry(p)
    check(label,g['document']<=p.viewport_size['width'] and all(c['inBand'] and c['textInside'] for c in g['cards']) and not g['cardBlockOverlap'] and not g['cardCardOverlap'] and not g['cardCounterOverlap'],g)

def local_links(p,label):
    from urllib.parse import urlparse,unquote
    links=p.locator('a[href],img[src],script[src],link[href]').evaluate_all('es=>es.map(e=>e.href||e.src)')
    local=[unquote(urlparse(x).path) for x in links if x.startswith('file:')]
    missing=[x for x in local if not Path(x).exists()]
    check(label,not missing,missing)

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    for width in [1440,1024,390]:
        p=browser.new_page(viewport={'width':width,'height':1000 if width>400 else 844},reduced_motion='reduce')
        p.on('pageerror',lambda err:REPORT['errors'].append(str(err)))
        external=[]
        p.on('request',lambda req:external.append(req.url) if req.url.startswith(('http:','https:')) else None)
        p.goto(URL);p.wait_for_timeout(200)
        p.locator('[data-goto="4"]').click();s=state(p)
        check(f'{width}: v4 ten persistent bubbles',len(s['visibleTags'])==10,s)
        dd=[x for x in s['visibleTags'] if x['c']=='dd' and x['kind']=='delta']
        check(f'{width}: new DD bubble result and execution version',len(dd)==1 and all(x in dd[0]['text'] for x in ['2,566','2,567','Run: v2']),dd)
        fit(p,f'{width}: v4 all bubble geometry including DD and HE');snap(p,f'overview-{width}')
        if width==390:
            scroll_column(p,4);snap(p,'overview-390-v4')
        p.locator('#chips [data-case="dd"]').click();s=state(p)
        check(f'{width}: DD singleton trajectory',s['selected']==['dd'] and bool(s['line']) and s['lines']==1,s)
        fit(p,f'{width}: DD focus geometry');snap(p,f'dd-focus-{width}')
        check(f'{width}: v4 four reached DD result blocks',len(visible_dd_results(p))==4,visible_dd_results(p))
        check(f'{width}: v4 DD panel new totals','163' in p.locator('#panel').inner_text() and '2,567' in p.locator('#panel').inner_text(),p.locator('#panel').inner_text())
        for v in [3,2]:
            p.locator(f'[data-goto="{v}"]').click();p.wait_for_timeout(80);s=state(p)
            check(f'{width}: v{v} three DD blocks',len(visible_dd_results(p))==3,visible_dd_results(p))
            check(f'{width}: v{v} no new DD bubble',not any(x['c']=='dd' and x['kind']=='delta' for x in s['visibleTags']),s)
            quant=p.locator('#panel > div').first.locator('.p-quant').inner_text() if p.locator('#panel > div .p-quant').count() else p.locator('#panel > div').first.inner_text().split('Earlier research')[0]
            check(f'{width}: v{v} reached panel totals old',not any(x in quant.split('Mathematical results')[0] for x in ['163','2,567','2,566','49 concrete']),quant)
        p.locator('#overview').click();s=state(p)
        check(f'{width}: overview clears DD',not s['line'] and s['selected']==[],s)
        p.locator('[data-goto="4"]').click()
        results=p.locator('#results').inner_text()
        check(f'{width}: Results new DD summary',all(x in results for x in ['2,567','4']),results)
        local_links(p,f'{width}: homepage local resource links')
        check(f'{width}: no external rendering requests',not external,external)
        p.goto((OUT.parent.parent/'site/dd-10-4.html').as_uri());p.wait_for_timeout(150)
        local_links(p,f'{width}: DD detail local resource links')
        body=p.locator('body').inner_text()
        check(f'{width}: detail carries result and provenance',all(x in body for x in ['2,567','2,566','v2']),body[:1500])
        check(f'{width}: original construction SVG linked',p.locator('[href*="construction_d10_d4.svg"],[src*="construction_d10_d4.svg"]').count()>0)
        check(f'{width}: local original materials linked',p.locator('a[href*="assets/dd-2567/"]').count()>0)
        rows=p.locator('tr').all_inner_texts()
        check(f'{width}: detail four comparison rows',all(any(a in row and b in row for row in rows) for a,b in [('2,566','2,567'),('37,628','37,631'),('42,342','42,402'),('16,384','16,416')]),rows)
        check(f'{width}: detail no external rendering requests',not external,external)
        check(f'{width}: detail no horizontal document overflow',p.evaluate('document.documentElement.scrollWidth<=innerWidth'))
        p.screenshot(path=str(OUT/f'dd-detail-{width}.png'),full_page=True);REPORT['screenshots'].append(f'dd-detail-{width}.png')
        p.close()
    p=browser.new_page(viewport={'width':1440,'height':1000},reduced_motion='no-preference')
    p.on('pageerror',lambda err:REPORT['errors'].append(str(err)))
    p.goto(URL);p.locator('#replay').click();samples=[];deadline=time.monotonic()+12
    while time.monotonic()<deadline:
        samples.append(state(p));p.wait_for_timeout(45)
        if len(samples)>5 and samples[-1]['playing']=='play' and samples[-1]['version']=='4':break
    p.wait_for_timeout(300);samples.append(state(p))
    sets=[{t['id'] for t in s['visibleTags']} for s in samples]
    check('normal replay bubbles persist without flash',all(a<=b for a,b in zip(sets,sets[1:])),[sorted(x) for x in sets])
    check('normal replay ends with ten persistent bubbles',len(samples[-1]['visibleTags'])==10 and samples[-1]['version']=='4' and samples[-1]['playing']=='play',samples[-1])
    check('normal replay no unexpected trajectory',all(not s['line'] and s['selected']==[] for s in samples))
    (OUT/'animation-samples.json').write_text(json.dumps(samples,indent=2))
    snap(p,'normal-replay-final');browser.close()
REPORT['pass']=not REPORT['errors'] and all(c['pass'] for c in REPORT['checks'])
(OUT/'RESULTS.json').write_text(json.dumps(REPORT,indent=2))
print(json.dumps({'pass':REPORT['pass'],'checks':len(REPORT['checks']),'failures':[c for c in REPORT['checks'] if not c['pass']],'errors':REPORT['errors']},indent=2))
