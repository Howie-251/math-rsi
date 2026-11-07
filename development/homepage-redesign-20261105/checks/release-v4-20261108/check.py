from pathlib import Path
import importlib.util,json
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('prior',OUT.parent/'dd-v4-20261108/check.py')
# Reuse the prior geometry function without executing its old test suite.
source=(OUT.parent/'dd-v4-20261108/check.py').read_text();body=source[source.index('def geometry(p):'):source.index('\n\ndef visible_dd_results')]
exec(body)
r={'checks':[],'errors':[]}
def check(n,v,e=None):r['checks'].append({'name':n,'pass':bool(v),'evidence':e})
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True)
 for width in [1440,390]:
  p=b.new_page(viewport={'width':width,'height':1000 if width>400 else 844},reduced_motion='reduce');p.on('pageerror',lambda e:r['errors'].append(str(e)))
  response=p.goto('http://127.0.0.1:8768/development/homepage-redesign-20261105/site/index.html');check(f'{width}: HTTP ready',response.status==200)
  p.locator('[data-goto="4"]').click();p.wait_for_timeout(150)
  text=p.locator('body').inner_text();v=p.locator('[data-goto="4"]').inner_text()
  check(f'{width}: v4 current', 'Current' in v and 'Preview' not in v,v)
  check(f'{width}: no stale release prose',all(x not in text for x in ['not yet implemented','local v4','v4 Preview','Latest tagged release: v3']),text[:800])
  check(f'{width}: three base actions',all(x in text for x in ['Recover the equality chain','Make legal exchanges','Connect the same endpoints']))
  g=geometry(p);check(f'{width}: geometry',g['document']<=width and all(c['inBand'] and c['textInside'] for c in g['cards']) and not g['cardBlockOverlap'] and not g['cardCardOverlap'] and not g['cardCounterOverlap'],g)
  if width==390:p.evaluate('()=>{const s=document.querySelector("#scroller"),stage=document.querySelector("#stage");s.scrollLeft=(80+232*4+116)*stage.clientWidth/1472-s.clientWidth/2}')
  p.locator('#evolution').scroll_into_view_if_needed();p.screenshot(path=str(OUT/f'current-{width}.png'))
  p.locator('#chips [data-case="dd"]').click();check(f'{width}: DD run v2 retained','Run: v2' in p.locator('#sky').text_content())
  p.goto('http://127.0.0.1:8768/development/homepage-redesign-20261105/site/dd-10-4.html');text=p.locator('body').inner_text()
  check(f'{width}: detail released methods and original run','current release' in text and 'v2 + DD' in text and 'Not yet implemented' not in text)
  check(f'{width}: detail no horizontal overflow',p.evaluate('document.documentElement.scrollWidth<=innerWidth'))
  p.screenshot(path=str(OUT/f'detail-{width}.png'),full_page=True);p.close()
 b.close()
r['all_pass']=all(x['pass'] for x in r['checks']) and not r['errors'];(OUT/'RESULT.json').write_text(json.dumps(r,indent=2));print(json.dumps({'checks':len(r['checks']),'all_pass':r['all_pass'],'errors':r['errors']}))
