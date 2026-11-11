"""Render maintained entries through GitHub's GFM API and inspect local previews.

Uses gh authentication, Python Playwright/Chromium and KaTeX 0.16.11 downloaded
into the ignored .local cache. CSS approximates GitHub's reading column; this
is not a screenshot of GitHub's full repository interface.
"""
from pathlib import Path
import json
import re
import subprocess
import urllib.request
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CACHE = ROOT / '.local/github-preview'
CHECKS = HERE / 'checks'
CACHE.mkdir(parents=True, exist_ok=True)
CHECKS.mkdir(exist_ok=True)
if not (CACHE / 'katex.min.js').exists():
    urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js', CACHE / 'katex.min.js')
DOCS = ['README.md', 'README.zh-CN.md', 'docs/README.md',
        'case-studies/README.md', 'figures/mathrsi/README.md']
CSS = '''
* {box-sizing:border-box} body {margin:0;background:#fff;color:#1f2328}
.markdown-body {max-width:964px;padding:32px;margin:0 auto;font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;overflow-wrap:break-word}
h1,h2,h3 {font-weight:600;line-height:1.25;margin:24px 0 16px} h1 {font-size:32px} h2 {font-size:24px} h3 {font-size:20px}
h1,h2 {padding-bottom:.3em;border-bottom:1px solid #d1d9e0} p,ul,ol,table,pre {margin:0 0 16px} li+li {margin-top:.5em}
a {color:#0969da;text-decoration:none} img {max-width:100%;height:auto} code {padding:.2em .4em;border-radius:6px;background:#818b981f;font-size:85%;font-family:ui-monospace,SFMono-Regular,Consolas,monospace}
pre {padding:16px;overflow:auto;border-radius:6px;background:#f6f8fa;font-size:85%;line-height:1.45} pre code {padding:0;background:transparent;font-size:100%}
markdown-accessiblity-table {display:block;max-width:100%;overflow-x:auto} table {border-collapse:collapse;width:100%} th,td {padding:6px 13px;border:1px solid #d1d9e0;text-align:left} tr:nth-child(2n) {background:#f6f8fa} summary {cursor:pointer;margin-bottom:16px}
@media(max-width:600px){.markdown-body{padding:16px}h1{font-size:28px}h2{font-size:22px}}
'''

for filename in DOCS:
    name = filename.replace('/', '__').removesuffix('.md')
    request = CACHE / (name + '.request.json')
    request.write_text(json.dumps({'text': (ROOT / filename).read_text(),
                                  'mode': 'gfm', 'context': 'lisresearchgroup/math-rsi'}))
    result = subprocess.run(['gh', 'api', '--method', 'POST', '/markdown',
                             '--input', str(request)], text=True, capture_output=True, check=True)
    page_html = ('<!doctype html><meta charset="utf-8"><base href="' +
                 (ROOT / filename).parent.as_uri() + '/">' +
                 '<link rel="stylesheet" href="' +
                 (ROOT / 'development/homepage-redesign-20261105/site/assets/math/katex.min.css').as_uri() +
                 '"><style>' + CSS + '</style><article class="markdown-body">' + result.stdout + '</article>')
    (CACHE / (name + '.html')).write_text(page_html)

results = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    for filename in DOCS:
        name = filename.replace('/', '__').removesuffix('.md')
        widths = [1280, 390] if filename.startswith('README') else [1280]
        for width in widths:
            page = browser.new_page(viewport={'width': width, 'height': 1000})
            page.goto((CACHE / (name + '.html')).as_uri())
            page.add_script_tag(path=str(CACHE / 'katex.min.js'))
            page.evaluate(r'''() => document.querySelectorAll('math-renderer').forEach(el => {
                const raw = el.textContent.replace(/^\$|\$$/g, '');
                katex.render(raw, el, {throwOnError:true});
            })''')
            page.evaluate('document.fonts.ready')
            page.wait_for_timeout(1700)
            metrics = page.evaluate('''() => ({
                width: innerWidth, bodyWidth: document.documentElement.scrollWidth,
                readingWidth: document.querySelector('article').clientWidth -
                  parseFloat(getComputedStyle(document.querySelector('article')).paddingLeft)*2,
                images: [...document.images].map(i => ({src:i.getAttribute('src'), loaded:i.complete && i.naturalWidth>0, renderedWidth:i.width})),
                math: document.querySelectorAll('math-renderer').length,
                tables: [...document.querySelectorAll('table')].map(t => ({headers:[...t.querySelectorAll('th')].map(x=>x.textContent), rows:t.querySelectorAll('tbody tr').length})),
                text: document.body.innerText
            })''')
            assert metrics['bodyWidth'] <= width, (filename, metrics)
            assert all(x['loaded'] for x in metrics['images']), (filename, metrics['images'])
            # Inline formulas missed by the GFM parser would be visible as raw dollar pairs.
            assert not re.search(r'\$[^\n$]+\$', metrics.pop('text')), filename
            if filename.startswith('README'):
                assert len(metrics['images']) == 3, metrics['images']
                assert metrics['tables'][0]['rows'] == 4, metrics['tables']
                assert len(metrics['tables'][0]['headers']) == 2
            shot = CHECKS / f'{name}-{width}.png'
            page.screenshot(path=str(shot), full_page=True)
            if filename.startswith('README'):
                page.screenshot(path=str(CHECKS / f'{name}-{width}-top.png'))
            results.append({'document': filename, 'viewport': width, 'screenshot': str(shot.relative_to(ROOT)), **metrics})
            page.close()
    page = browser.new_page(viewport={'width': 1280, 'height': 1000})
    page.goto((ROOT / 'development/homepage-redesign-20261105/site/index.html').as_uri())
    footer = page.locator('footer a[href$="docs/V4_CHANGES.md"]')
    assert footer.inner_text() == 'v4 changes ↗'
    page.locator('[data-lang="zh-CN"]').first.click()
    assert footer.inner_text() == 'v4 更新说明 ↗'
    page.reload()
    assert footer.inner_text() == 'v4 更新说明 ↗'
    page.locator('[data-lang="en"]').first.click()
    assert footer.inner_text() == 'v4 changes ↗'
    footer.scroll_into_view_if_needed()
    page.screenshot(path=str(CHECKS / 'homepage-footer-en.png'))
    results.append({'homepage_footer':'v4 EN → 中文 → remembered reload → EN passed',
                    'href': footer.get_attribute('href')})
    browser.close()
(CHECKS / 'BROWSER_RESULTS.json').write_text(json.dumps({
    'rendering': "GitHub GFM API HTML; local KaTeX 0.16.11 for math; approximate GitHub CSS and 900px/358px reading columns",
    'results':results}, indent=2, ensure_ascii=False)+'\n')
print(f'{len(results)} rendered entry/footer checks passed')
