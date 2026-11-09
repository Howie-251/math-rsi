"""Focused local browser checks; production scripts are instrumented in transit only."""
import functools
import http.server
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

SITE = Path(__file__).resolve().parents[2] / 'site'
OUT = Path(__file__).resolve().parent
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{server.server_port}/'
synthetic = not (SITE / 'zh-CN.js').exists()
results = {'catalog': 'synthetic' if synthetic else 'actual', 'viewports': []}
with sync_playwright() as p:
    browser = p.chromium.launch()
    for width in [1440, 390]:
        context = browser.new_context(viewport={'width': width, 'height': 1000})
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))
        if synthetic:
            page.route('**/zh-CN.js', lambda route: route.fulfill(content_type='text/javascript', body='window.MATHRSI_ZH={"Play":"播放","Pause":"暂停","Overview":"总览","Live English":"动态中文"};'))
        def instrument(route):
            source = (SITE / 'app.js').read_text()
            position = source.rfind('})();')
            source = source[:position] + 'window.__snapshot=()=>({t,mode,playing,target,targetSel,future,focus,hl,rp});\n' + source[position:]
            route.fulfill(content_type='text/javascript', body=source)
        page.route('**/app.js', instrument)
        page.goto(url)
        page.wait_for_timeout(450)
        assert page.locator('html').get_attribute('lang') == 'en'
        english_problems = page.locator('#results .vcap').all_text_contents()
        for button in page.locator('[data-rv-mode="problem"]').all(): button.click()
        english_problems = page.locator('#results .vcap').all_text_contents()
        for button in page.locator('[data-rv-mode="result"]').all(): button.click()
        # Pause initial animation so version/case interactions have a stable endpoint.
        page.locator('[data-goto="2"]').click()
        page.wait_for_timeout(700)
        page.locator('#chips [data-case="ecc"]').click()
        page.locator('#rpSteps [data-step="3"]').click()
        page.locator('#results details').first.evaluate('(el)=>el.open=true')
        page.locator('#rpNext').focus()
        baseline = page.evaluate('''() => ({state:__snapshot(),math:[...document.querySelectorAll('.katex')].map(e=>e.innerHTML),geometry:[...document.querySelectorAll('#results svg *')].map(e=>[e.tagName,...['x','y','x1','x2','y1','y2','width','height','cx','cy','r','d','points','transform'].map(a=>e.getAttribute(a))]), focus:document.activeElement.id})''')
        page.evaluate("MathRSII18n.setLanguage('zh-CN')")
        page.wait_for_timeout(30)
        assert page.locator('html').get_attribute('lang') == 'zh-CN'
        assert page.locator('[data-lang="zh-CN"]').get_attribute('aria-pressed') == 'true'
        after = page.evaluate('''() => ({state:__snapshot(),math:[...document.querySelectorAll('.katex')].map(e=>e.innerHTML),geometry:[...document.querySelectorAll('#results svg *')].map(e=>[e.tagName,...['x','y','x1','x2','y1','y2','width','height','cx','cy','r','d','points','transform'].map(a=>e.getAttribute(a))]), focus:document.activeElement.id})''')
        assert baseline == after, 'Language switch changed stable app state, focus, math or geometry'
        assert page.locator('#results details').first.evaluate('(el)=>el.open')
        page.evaluate("document.body.insertAdjacentHTML('beforeend','<p id=qa-dynamic>Overview</p>')")
        page.wait_for_function("document.querySelector('#qa-dynamic').textContent===MATHRSI_ZH['Overview']")
        page.evaluate("document.querySelector('#qa-dynamic').firstChild.data='Play'")
        page.wait_for_function("document.querySelector('#qa-dynamic').textContent===MATHRSI_ZH['Play']")
        page.evaluate("MathRSII18n.setLanguage('en')")
        assert page.locator('#overview').inner_text() == 'Overview'
        assert page.locator('#qa-dynamic').inner_text() == 'Play'
        # Switching during playback must leave the same running timeline at the same instant.
        page.locator('#replay').click()
        page.wait_for_timeout(160)
        live = page.evaluate("() => {const before=__snapshot();MathRSII18n.setLanguage('zh-CN');return {before,after:__snapshot()}}")
        assert live['before'] == live['after'] and live['after']['playing']
        page.wait_for_timeout(120)
        assert page.evaluate('__snapshot().t') > live['after']['t']
        page.reload()
        page.wait_for_timeout(400)
        assert page.locator('html').get_attribute('lang') == 'zh-CN'
        overflow = page.evaluate('document.documentElement.scrollWidth > innerWidth + 1')
        assert not overflow, 'Whole-page horizontal overflow'
        page.screenshot(path=str(OUT / f'{results["catalog"]}-{width}.png'), full_page=True)
        page.evaluate("MathRSII18n.setLanguage('en')")
        for button in page.locator('[data-rv-mode="problem"]').all(): button.click()
        page.wait_for_timeout(30)
        assert page.locator('#results .vcap').all_text_contents() == english_problems, 'Saved-ZH bootstrap captured Chinese problem captions as English'
        page.reload()
        assert page.locator('html').get_attribute('lang') == 'en'
        assert not errors, errors
        results['viewports'].append({'width':width,'state_math_geometry_focus_details':'pass','dynamic_reversal':'pass','live_playback':'pass','persistence_both_languages':'pass','saved_zh_reload_en_problem_captions':'pass','page_errors':errors,'horizontal_overflow':overflow})
        context.close()
    browser.close()
server.shutdown()
(OUT / f'{results["catalog"]}-report.json').write_text(json.dumps(results, indent=2))
print(json.dumps(results, indent=2))
