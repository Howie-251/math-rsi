"""Render the maintenance diagram and its 900 CSS-pixel reading check."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

out = Path(__file__).resolve().parent
stem = 'research-to-capabilities'
svg = (out / f'{stem}.svg').read_text()
with sync_playwright() as p:
    browser = p.chromium.launch(channel='chromium', args=['--disable-gpu'])
    page = browser.new_page(viewport={'width': 1200, 'height': 650}, device_scale_factor=2)
    page.set_content('<html><body style="margin:0">' + svg + '</body></html>')
    bounds = page.locator('svg text').evaluate_all('''xs => xs.map(x => {
        const b = x.getBBox();
        return {text: x.textContent, x: b.x, y: b.y, w: b.width, h: b.height};
    })''')
    assert all(b['x'] >= 0 and b['y'] >= 0 and b['x'] + b['w'] <= 1200
               and b['y'] + b['h'] <= 650 for b in bounds), 'Text outside canvas'
    (out / f'{stem}-text-bounds.json').write_text(json.dumps(bounds, indent=2) + '\n')
    page.screenshot(path=str(out / f'{stem}.png'), full_page=True)
    page.set_viewport_size({'width': 900, 'height': 488})
    page.locator('svg').evaluate('x => {x.style.width="900px";x.style.height="auto";}')
    page.screenshot(path=str(out / f'{stem}-900px.png'), full_page=True)
    browser.close()
print('Rendered 2400×1300 PNG and 900 CSS-pixel preview; all text is inside canvas.')
