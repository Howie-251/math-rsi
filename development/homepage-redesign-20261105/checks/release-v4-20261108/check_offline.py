from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent
ROOT=OUT/'extracted/MathRSI_homepage_v4_20261108'
r={'checks':[],'errors':[],'network':[]}
def check(n,v,e=None):r['checks'].append({'name':n,'pass':bool(v),'evidence':e})
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True)
 p=b.new_page(viewport={'width':1440,'height':1000},reduced_motion='reduce');p.on('pageerror',lambda e:r['errors'].append(str(e)));p.on('request',lambda x:r['network'].append(x.url) if x.url.startswith(('http:','https:')) else None)
 p.goto((ROOT/'START_HERE.html').as_uri());p.wait_for_timeout(250)
 check('ZIP entry redirects to homepage',p.url.endswith('/site/index.html'))
 p.locator('[data-goto="4"]').click();check('ZIP v4 Current','Current' in p.locator('[data-goto="4"]').inner_text())
 links=p.locator('#results .meta a').evaluate_all('es=>es.map(x=>({label:x.textContent,url:x.href}))')
 for i,x in enumerate(links):
  if not x['url'].startswith('file:'):continue
  q=Path(unquote(urlsplit(x['url']).path));check(f'local result link {i} exists',q.is_file(),x)
  if q.suffix=='.html':
   tab=b.new_page();tab.goto(x['url']);check(f'local reader {i} opens',bool(tab.locator('body').inner_text().strip()),tab.title());tab.close()
 p.goto((ROOT/'development/homepage-redesign-20261105/site/dd-10-4.html').as_uri());check('ZIP DD released plugin and original run','current release' in p.locator('body').inner_text() and 'v2 + DD' in p.locator('body').inner_text())
 refs=p.locator('a[href],img[src],link[href]').evaluate_all('es=>es.map(e=>e.href||e.src)');missing=[x for x in refs if x.startswith('file:') and not Path(unquote(urlsplit(x).path)).is_file()];check('ZIP DD local source receipts and assets',not missing,missing)
 check('ZIP no network rendering',not r['network'],r['network']);p.screenshot(path=str(OUT/'offline-dd-1440.png'),full_page=True);b.close()
r['all_pass']=all(x['pass'] for x in r['checks']) and not r['errors'];(OUT/'OFFLINE_RESULT.json').write_text(json.dumps(r,indent=2));print(json.dumps({'checks':len(r['checks']),'all_pass':r['all_pass'],'errors':r['errors']}))
