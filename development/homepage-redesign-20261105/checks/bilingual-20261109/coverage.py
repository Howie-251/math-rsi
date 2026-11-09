"""Exercise Chinese interactive states and report visible prose missing the catalog."""
import functools, http.server, threading, json
from pathlib import Path
from playwright.sync_api import sync_playwright
OUT=Path(__file__).resolve().parent
SITE=OUT.parents[1]/'site'
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(SITE)))
threading.Thread(target=server.serve_forever,daemon=True).start()
report=[]
with sync_playwright() as p:
    browser=p.chromium.launch()
    for width in [1440,390]:
        page=browser.new_page(viewport={'width':width,'height':1050},reduced_motion='reduce')
        page.goto(f'http://127.0.0.1:{server.server_port}/')
        page.evaluate("MathRSII18n.setLanguage('zh-CN')")
        missing=set(); bounds=[]
        def collect(state):
            data=page.evaluate('''() => {const out=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const p=n.parentElement;if(!p||p.closest('script,style,pre,code,math,.katex,[data-no-i18n]')||!p.getClientRects().length)continue;const s=n.nodeValue.replace(/\\s+/g,' ').trim();if(/[A-Za-z]{3}/.test(s)&&!/[\\u4e00-\\u9fff]/.test(s)&&!Object.prototype.hasOwnProperty.call(window.MATHRSI_ZH,s))out.push(s);}return [...new Set(out)]}''')
            missing.update(data)
            defects=page.evaluate('''() => [...document.querySelectorAll('svg:not([hidden]) text')].filter(e=>e.getClientRects().length).flatMap(e=>{const s=e.ownerSVGElement;const b=e.getBoundingClientRect(),r=s.getBoundingClientRect();return b.left<r.left-2||b.right>r.right+2?[{text:e.textContent,svg:s.id||s.classList.value,left:Math.round(b.left-r.left),right:Math.round(b.right-r.right)}]:[]})''')
            if defects: bounds.append({'state':state,'out_of_svg':defects})
        collect('initial')
        for case in ['pb','ecc','dd','e86','q6','he']:
            page.locator(f'#chips [data-case="{case}"]').click()
            page.wait_for_timeout(30)
            collect('case-'+case)
        for v in range(6):
            page.locator(f'[data-goto="{v}"]').click()
            page.wait_for_timeout(30)
            collect('version-'+str(v))
        for mode in ['problem','result']:
            for button in page.locator(f'[data-rv-mode="{mode}"]').all(): button.click()
            collect(mode)
        for step in page.locator('#rpSteps [data-step]').all():
            step.click(); collect('step-'+step.get_attribute('data-step'))
        page.locator('#overview').click()
        page.locator('#evolution').screenshot(path=str(OUT/f'actual-evolution-{width}.png'))
        page.locator('#results').screenshot(path=str(OUT/f'actual-results-{width}.png'))
        page.locator('#workflow').screenshot(path=str(OUT/f'actual-workflow-{width}.png'))
        report.append({'width':width,'unmapped_visible_latin':sorted(missing),'svg_bounds':bounds})
        page.close()
    browser.close()
server.shutdown()
(OUT/'actual-coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
