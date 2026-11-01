from pathlib import Path
from collections import Counter
from playwright.sync_api import sync_playwright
import json,re
ROOT=Path('/Users/rfy_naiveai/Desktop/aris4math')
OUT=ROOT/'context/propertyb-general/comparison-table-20261021'
TRACE=ROOT/'.aris/traces/render-html/2026-10-21_general-literature-comparison'
old=json.loads((ROOT/'.aris/traces/render-html/2026-10-21_general-growth-lean/fresh-browser-check.json').read_text())['PROPERTY_B_GENERAL_BOUND']['desktop']['formulas']
prior=json.loads((ROOT/'.aris/traces/render-html/2026-10-21_general-formal-exposition-lean-update/source-snapshots.json').read_text())
source_unchanged={name:(ROOT/'proofs/propertyb-general'/name).read_text()==text for name,text in prior.items()}
result={'verdict':'PASS','scope':'New literature-summary tables and display only; no re-audit of existing proofs or Lean.','review_independence':'same-family','acceptance_status':'provisional','source_text_unchanged':source_unchanged,'views':{}}
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True)
 for label,width,height in [('desktop',1440,1000),('phone',390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},offline=True)
  page.goto((ROOT/'PROPERTY_B_GENERAL_BOUND.html').as_uri(),wait_until='load')
  page.evaluate('document.fonts.ready')
  stats=page.evaluate(r'''() => {
   const tables=[...document.querySelectorAll('main table')].slice(0,2);
   return {formulaCount:document.querySelectorAll('mjx-container').length,
     svgCount:document.querySelectorAll('mjx-container > svg').length,
     formulas:[...document.querySelectorAll('mjx-container')].map(n=>n.dataset.tex),
     mathErrors:[...document.querySelectorAll('[data-mml-node="merror"]')].map(n=>n.textContent),
     documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,
     pageOverflow:document.documentElement.scrollWidth>innerWidth+1,
     tables:tables.map(t=>{
      const wrap=t.parentElement, old=wrap.scrollLeft;
      wrap.scrollLeft=wrap.scrollWidth;
      const reached=wrap.scrollLeft;
      wrap.scrollLeft=old;
      return {rowColumns:[...t.rows].map(r=>r.cells.length),
       cells:[...t.rows].map(r=>[...r.cells].map(c=>{
         const clone=c.cloneNode(true);clone.querySelectorAll('mjx-container').forEach(n=>n.replaceWith(document.createTextNode(n.dataset.tex)));return clone.textContent;
       })),
       tableWidth:t.getBoundingClientRect().width,wrapperWidth:wrap.clientWidth,
       wrapperScrollWidth:wrap.scrollWidth,wrapperOverflowX:getComputedStyle(wrap).overflowX,
       horizontalReachable:reached>0,
       fontSize:getComputedStyle(t).fontSize,
       formulaCount:t.querySelectorAll('mjx-container').length,
       svgCount:t.querySelectorAll('mjx-container > svg').length};
     })};
  }''')
  norm=lambda v:re.sub(r'\s+','',v)
  old_c=Counter(map(norm,old)); new_c=Counter(map(norm,stats.pop('formulas')))
  stats['oldFormulaCount']=len(old)
  stats['oldFormulaMissing']=list((old_c-new_c).elements())
  screenshots=[]
  for i in range(2):
   table=page.locator('main table').nth(i)
   wrap=table.locator('..')
   wrap.evaluate('(e)=>e.scrollLeft=0')
   path=TRACE/f'fresh-{label}-literature-table-{i+1}-left.png'
   wrap.screenshot(path=str(path));screenshots.append(str(path.relative_to(ROOT)))
   if label=='phone':
    wrap.evaluate('(e)=>e.scrollLeft=e.scrollWidth')
    path=TRACE/f'fresh-{label}-literature-table-{i+1}-right.png'
    wrap.screenshot(path=str(path));screenshots.append(str(path.relative_to(ROOT)))
  stats['screenshots']=screenshots
  result['views'][label]=stats
  page.close()
 browser.close()
(OUT/'TABLE_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({**{k:v for k,v in result.items() if k!='views'},'views':{label:{k:v for k,v in stats.items() if k not in ['tables']}|{'tables':[{k:v for k,v in t.items() if k!='cells'}for t in stats['tables']]} for label,stats in result['views'].items()}},ensure_ascii=False,indent=2))
