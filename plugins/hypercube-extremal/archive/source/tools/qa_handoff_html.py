"""Offline handoff QA with hidden Edge/CDP, package-link audit and viewport captures."""
from __future__ import annotations
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import socket
import os
import struct
import tempfile
import time
import urllib.parse
import urllib.request

class DevToolsSocket:
    """Minimal RFC6455 text client for local CDP; no third-party dependency."""
    def __init__(self,url):
        u=urllib.parse.urlsplit(url)
        self.sock=socket.create_connection((u.hostname,u.port),timeout=20)
        key=base64.b64encode(os.urandom(16)).decode()
        req=f'GET {u.path} HTTP/1.1\r\nHost: {u.netloc}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n'
        self.sock.sendall(req.encode());self.buf=b''
        while b'\r\n\r\n' not in self.buf:self.buf+=self.sock.recv(65536)
        headers,self.buf=self.buf.split(b'\r\n\r\n',1)
        if b' 101 ' not in headers.split(b'\r\n')[0]:raise RuntimeError(headers)
        self.fragment=b''
    def read(self,n):
        while len(self.buf)<n:
            more=self.sock.recv(max(65536,n-len(self.buf)))
            if not more:raise RuntimeError('CDP socket closed')
            self.buf+=more
        data,self.buf=self.buf[:n],self.buf[n:];return data
    def frame(self,data,opcode=1):
        mask=os.urandom(4);n=len(data)
        header=bytes([0x80|opcode,0x80|(n if n<126 else 126 if n<65536 else 127)])
        if n>=126:header+=struct.pack('!H' if n<65536 else '!Q',n)
        self.sock.sendall(header+mask+bytes(b^mask[i%4] for i,b in enumerate(data)))
    def send(self,text):self.frame(text.encode())
    def recv(self):
        while True:
            a,b=self.read(2);opcode=a&15;n=b&127
            if n==126:n=struct.unpack('!H',self.read(2))[0]
            elif n==127:n=struct.unpack('!Q',self.read(8))[0]
            mask=self.read(4) if b&128 else None
            data=self.read(n)
            if mask:data=bytes(v^mask[i%4] for i,v in enumerate(data))
            if opcode==8:raise RuntimeError('CDP close frame')
            if opcode==9:self.frame(data,10);continue
            if opcode not in (0,1):continue
            self.fragment+=data
            if a&128:
                text=self.fragment.decode();self.fragment=b'';return text
    def close(self):self.sock.close()

PACKAGE = Path(__file__).resolve().parents[1]
SOURCE = PACKAGE / 'START_HERE.html'
OUT = PACKAGE / 'validation/html_qa'
EDGE = Path('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.assets=[]; self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.append(a['id'])
        if tag=='a' and a.get('href'): self.links.append(a['href'])
        if tag in ['script','img','iframe'] and a.get('src'): self.assets.append(a['src'])
        if tag=='link' and a.get('href'): self.assets.append(a['href'])

def audit_links():
    parser=Links(); parser.feed(SOURCE.read_text('utf-8'))
    records=[]
    for href in parser.links:
        u=urllib.parse.urlsplit(href); rec={'href':href}
        if u.scheme and u.scheme not in ['file']:
            rec.update(kind='external',ok=False,reason='requires external target')
        else:
            path=urllib.parse.unquote(u.path)
            target=(SOURCE.parent/path).resolve() if path else SOURCE
            inside=target.is_relative_to(PACKAGE)
            exists=target.is_file()
            rec.update(kind='package' if inside else 'outside_package',target=str(target),ok=inside and exists)
            if u.fragment and inside and exists:
                frag=urllib.parse.unquote(u.fragment)
                if target.suffix.lower()=='.html':
                    t=Links();t.feed(target.read_text('utf-8'));rec['anchor_ok']=frag in t.ids
                    rec['ok']=rec['ok'] and rec['anchor_ok']
        records.append(rec)
    return {'links':records,'link_count':len(records),'broken_or_external_links':[r for r in records if not r['ok']],
      'declared_assets':parser.assets,'duplicate_ids':sorted({i for i in parser.ids if parser.ids.count(i)>1})}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    result={'input':str(SOURCE),'input_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),**audit_links()}
    with tempfile.TemporaryDirectory(prefix='q4-handoff-edge-',ignore_cleanup_errors=True) as profile:
        proc=subprocess.Popen([str(EDGE),'--headless=new','--disable-gpu','--no-first-run','--no-sandbox',
          '--disable-crash-reporter','--disable-breakpad','--no-default-browser-check','--disable-extensions',
          '--remote-debugging-port=0','--remote-allow-origins=*','--hide-scrollbars','--allow-file-access-from-files',
          '--user-data-dir='+profile,SOURCE.as_uri()],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,
          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        ws=None
        try:
            marker=Path(profile)/'DevToolsActivePort'
            for _ in range(120):
                if marker.exists():break
                time.sleep(.1)
            port=int(marker.read_text().splitlines()[0])
            for _ in range(100):
                with urllib.request.urlopen(f'http://127.0.0.1:{port}/json') as r: tabs=json.load(r)
                tab=next((t for t in tabs if t.get('type')=='page' and t.get('url')==SOURCE.as_uri()),None)
                if tab:break
                time.sleep(.1)
            ws=DevToolsSocket(tab['webSocketDebuggerUrl']);serial=0
            def call(method,params=None):
                nonlocal serial
                serial+=1;ws.send(json.dumps({'id':serial,'method':method,'params':params or {}}))
                while True:
                    e=json.loads(ws.recv())
                    if e.get('id')==serial:
                        if 'error' in e:raise RuntimeError(e['error'])
                        return e.get('result',{})
            def evaluate(js):
                r=call('Runtime.evaluate',{'expression':js,'returnByValue':True})
                if r.get('exceptionDetails'): raise RuntimeError(r['exceptionDetails'])
                return r['result'].get('value')
            call('Page.enable')
            for _ in range(100):
                if evaluate('document.readyState')=='complete':break
                time.sleep(.1)
            def viewport(width,height,mobile):
                call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':mobile})
                time.sleep(.2)
                return evaluate('''(() => ({viewportWidth:innerWidth,docWidth:document.documentElement.scrollWidth,
                  horizontalOverflow:document.documentElement.scrollWidth>innerWidth,
                  bodyHeight:document.body.scrollHeight,title:document.title,
                  headingText:[...document.querySelectorAll('h1,h2,h3')].map(e=>e.textContent),
                  replacementCharacters:document.body.innerText.includes('\\uFFFD'),
                  headingsWithReplacement:[...document.querySelectorAll('h1,h2,h3')].filter(e=>e.textContent.includes('\\uFFFD')).map(e=>e.textContent),
                  scriptSources:[...document.scripts].map(e=>e.src).filter(Boolean),
                  externalResources:performance.getEntriesByType('resource').filter(e=>/^https?:/.test(e.name)).map(e=>e.name),
                  overflowingElements:[...document.querySelectorAll('main,aside,section,header,.tablewrap,pre')].filter(e=>{
                    const r=e.getBoundingClientRect();return r.right>innerWidth+1||r.left < -1;
                  }).slice(0,20).map(e=>({tag:e.tagName,class:e.className,id:e.id,right:e.getBoundingClientRect().right}))}))()''')
            def screenshot(name,y):
                evaluate('window.scrollTo({top:'+str(y)+',behavior:"instant"})');time.sleep(.15)
                shot=call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
                (OUT/name).write_bytes(base64.b64decode(shot['data']))
            result['desktop']=viewport(1600,1100,False)
            screenshot('01_desktop_cover.png',0)
            y=evaluate("Math.max(0,document.querySelector('#trajectory').getBoundingClientRect().top+scrollY-20)")
            screenshot('02_desktop_middle.png',y)
            result['mobile']=viewport(430,900,True)
            screenshot('03_mobile_cover.png',0)
            y=evaluate("Math.max(0,document.querySelector('#trajectory').getBoundingClientRect().top+scrollY-20)")
            screenshot('04_mobile_middle.png',y)
            result['passed']=not(result['broken_or_external_links'] or result['duplicate_ids'] or
              result['desktop']['horizontalOverflow'] or result['mobile']['horizontalOverflow'] or
              result['desktop']['replacementCharacters'] or result['desktop']['scriptSources'] or
              result['desktop']['externalResources'])
            result['screenshots']=[p.name for p in sorted(OUT.glob('*.png'))]
            (OUT/'layout_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
            print(json.dumps({'passed':result['passed'],'links':result['link_count'],
              'bad_links':len(result['broken_or_external_links']),
              'desktop_overflow':result['desktop']['horizontalOverflow'],
              'mobile_overflow':result['mobile']['horizontalOverflow'],
              'external_scripts':result['desktop']['scriptSources'],
              'report':str(OUT/'layout_checks.json')},ensure_ascii=True))
        finally:
            if ws:
                try:call('Browser.close')
                except Exception:pass
                ws.close()
            try:proc.wait(timeout=8)
            except subprocess.TimeoutExpired:proc.terminate();proc.wait(timeout=8)

if __name__=='__main__':main()
