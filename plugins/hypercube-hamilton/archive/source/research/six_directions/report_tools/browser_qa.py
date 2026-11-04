"""Local Edge/CDP visual checks; no remote content or upload."""
from pathlib import Path
import base64
import json
import os
import subprocess
import time
import urllib.request
import websocket

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent.parent
os.environ['NO_PROXY']=os.environ.get('NO_PROXY','')+',127.0.0.1,localhost'
port=19366
edge=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
proc=subprocess.Popen([edge,'--headless=new','--disable-gpu','--no-first-run',
 '--no-default-browser-check','--disable-background-networking',
 '--remote-allow-origins=*',f'--remote-debugging-port={port}',
 f'--user-data-dir={HERE / "edge-profile-cdp"}','about:blank'],
 stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
ws=None
try:
 for _ in range(100):
  try:
   tabs=json.load(opener.open(f'http://127.0.0.1:{port}/json',timeout=1))
   tab=next(t for t in tabs if t['type']=='page')
   break
  except Exception:time.sleep(.1)
 else:raise RuntimeError('Edge debug endpoint unavailable')
 ws=websocket.create_connection(tab['webSocketDebuggerUrl'],timeout=30)
 ident=0
 def call(method,params=None):
  global ident
  ident+=1;wanted=ident
  ws.send(json.dumps({'id':wanted,'method':method,'params':params or {}}))
  while True:
   d=json.loads(ws.recv())
   if d.get('id')==wanted:
    assert 'error' not in d,d
    return d.get('result',{})
 def evaluate(code):
  r=call('Runtime.evaluate',{'expression':code,'returnByValue':True})
  assert not r.get('exceptionDetails'),r
  return r['result'].get('value')
 call('Page.enable')
 call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
 call('Page.navigate',{'url':(ROOT/'Ruskey-Savage_Q6_研究报告.html').as_uri()})
 for _ in range(100):
  if evaluate('document.readyState')=='complete' and evaluate('document.querySelectorAll("details.source-doc").length')==231:break
  time.sleep(.1)
 time.sleep(.4)
 result={'desktop':evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,math:document.querySelectorAll("math").length,docs:document.querySelectorAll("details.source-doc").length})')}
 def shot(name):
  d=call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
  (HERE/name).write_bytes(base64.b64decode(d['data']))
 shot('report-desktop.png')
 evaluate('document.getElementById("7").scrollIntoView({behavior:"instant",block:"start"})')
 time.sleep(.4)
 result['math_section']=evaluate('({scrollY:scrollY,top:document.getElementById("7").getBoundingClientRect().top})')
 shot('report-math.png')
 evaluate('location.hash="proof-fourteen-final25-proof"')
 time.sleep(.3)
 result['deep_link_opens_appendix']=evaluate('document.getElementById("proof-fourteen-final25-proof").open')
 evaluate('(()=>{const q=document.querySelector("#appendix-tools input");q.value="FOURTEEN_FINAL25";q.dispatchEvent(new Event("input"));})()')
 result['search_visible_documents']=evaluate('Array.from(document.querySelectorAll(".source-doc")).filter(x=>!x.hidden).length')
 evaluate('(()=>{const q=document.querySelector("#appendix-tools input");q.value="";q.dispatchEvent(new Event("input"));document.getElementById("collapse").click();history.replaceState(null,"",location.pathname);window.scrollTo(0,0)})()')
 call('Emulation.setDeviceMetricsOverride',{'width':420,'height':960,'deviceScaleFactor':1,'mobile':False})
 time.sleep(.4)
 result['mobile']=evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,mainWidth:document.querySelector("main").getBoundingClientRect().width})')
 shot('report-mobile.png')
 assert result['desktop']['scrollWidth']<=result['desktop']['width'],result
 assert result['mobile']['scrollWidth']<=result['mobile']['width'],result
 assert result['deep_link_opens_appendix'] and 0<result['search_visible_documents']<231,result
 (HERE/'REPORT_BROWSER_QA.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result))
finally:
 if ws:
  try:call('Browser.close')
  except Exception:pass
  ws.close()
 try:proc.wait(timeout=5)
 except subprocess.TimeoutExpired:proc.terminate()
