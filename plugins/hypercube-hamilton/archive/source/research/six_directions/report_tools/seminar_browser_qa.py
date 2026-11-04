"""Render the local seminar manuscript with Edge and inspect offline MathML."""
from pathlib import Path
import base64
import json
import os
import subprocess
import time
import urllib.request
import websocket

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
os.environ['NO_PROXY'] = os.environ.get('NO_PROXY','')+',127.0.0.1,localhost'
port = 19367
proc = subprocess.Popen([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check',
    '--disable-background-networking','--remote-allow-origins=*',
    f'--remote-debugging-port={port}',f'--user-data-dir={HERE / "edge-profile-seminar"}',
    'about:blank'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW)
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
ws = None
try:
    for _ in range(100):
        try:
            tabs = json.load(opener.open(f'http://127.0.0.1:{port}/json',timeout=1))
            tab = next(t for t in tabs if t['type']=='page')
            break
        except Exception:
            time.sleep(.1)
    else:
        raise RuntimeError('Edge debug endpoint unavailable')
    ws = websocket.create_connection(tab['webSocketDebuggerUrl'],timeout=30)
    ident = 0
    def call(method, params=None):
        global ident
        ident += 1
        wanted = ident
        ws.send(json.dumps({'id':wanted,'method':method,'params':params or {}}))
        while True:
            data = json.loads(ws.recv())
            if data.get('id')==wanted:
                assert 'error' not in data, data
                return data.get('result',{})
    def evaluate(code):
        result = call('Runtime.evaluate',{'expression':code,'returnByValue':True})
        assert not result.get('exceptionDetails'), result
        return result['result'].get('value')
    def screenshot(name):
        result = call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
        (HERE/name).write_bytes(base64.b64decode(result['data']))
    def metrics(width,height):
        call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':False})
    def dimensions():
        return evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,mainWidth:document.querySelector("main").getBoundingClientRect().width,math:document.querySelectorAll("math").length})')
    call('Page.enable')
    metrics(1440,1100)
    call('Page.navigate',{'url':(ROOT/'Ruskey-Savage_Q6_研究报告.html').as_uri()})
    for _ in range(100):
        if evaluate('document.readyState')=='complete' and evaluate('document.querySelectorAll("main h2").length')==8:
            break
        time.sleep(.1)
    time.sleep(.3)
    results={'desktop':dimensions()}
    screenshot('seminar-desktop.png')
    evaluate('document.querySelectorAll("main h2")[1].scrollIntoView()')
    time.sleep(.2)
    screenshot('seminar-literature.png')
    evaluate('document.querySelectorAll("main h2")[2].scrollIntoView()')
    time.sleep(.2)
    screenshot('seminar-results.png')
    evaluate('Array.from(document.querySelectorAll("main h3")).find(h=>h.textContent.startsWith("3.4 ")).scrollIntoView()')
    time.sleep(.2)
    screenshot('seminar-results-logic.png')
    evaluate('document.querySelectorAll("main h2")[5].scrollIntoView()')
    time.sleep(.2)
    screenshot('seminar-proof.png')
    results['nonempty_formula_boxes'] = evaluate('Array.from(document.querySelectorAll("math")).every(m=>m.getBoundingClientRect().width>0 && m.getBoundingClientRect().height>0)')
    results['local_math_overflows'] = evaluate('Array.from(document.querySelectorAll(".math-block")).filter(x=>x.scrollWidth>x.clientWidth+2).length')
    results['remote_dependencies'] = evaluate('Array.from(document.querySelectorAll("script[src],link[rel=stylesheet],img")).map(x=>x.src||x.href).filter(x=>/^https?:/.test(x))')
    metrics(420,960)
    evaluate('window.scrollTo(0,0)')
    time.sleep(.2)
    results['mobile']=dimensions()
    screenshot('seminar-mobile.png')
    assert results['desktop']['scrollWidth']<=results['desktop']['width'],results
    assert results['mobile']['scrollWidth']<=results['mobile']['width'],results
    assert results['nonempty_formula_boxes'] and not results['remote_dependencies'],results
    expected = json.loads((HERE/'SEMINAR_BUILD_MANIFEST.json').read_text(encoding='utf-8'))['math_count']
    assert results['desktop']['math']==expected
    (HERE/'SEMINAR_BROWSER_QA.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print(json.dumps(results))
finally:
    if ws:
        try:
            call('Browser.close')
        except Exception:
            pass
        ws.close()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.terminate()
