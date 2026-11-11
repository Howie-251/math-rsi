"""Render the existing browser animation into a shareable MP4; no site files change."""
from datetime import datetime, timedelta, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import math
import subprocess
import threading

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SITE = ROOT / 'development/homepage-redesign-20261105/site'
CACHE = OUT / '.local'
CACHE.mkdir(exist_ok=True)
FPS = 20
SPEED = 0.60

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
threading.Thread(target=server.serve_forever, daemon=True).start()
errors = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1600,'height':1300}, device_scale_factor=1,
                            reduced_motion='no-preference')
    page.on('pageerror', lambda e: errors.append(str(e)))
    fixed = datetime(2026, 11, 11, tzinfo=timezone.utc)
    page.clock.install(time=fixed)
    page.clock.pause_at(fixed + timedelta(seconds=1))
    page.goto(f'http://127.0.0.1:{server.server_port}/development/homepage-redesign-20261105/site/index.html')
    page.evaluate('document.fonts.ready')
    page.evaluate('''() => {
      const evo = document.querySelector('#evolution');
      document.body.append(evo);
      for (const el of document.body.children) if (el !== evo) el.style.display = 'none';
      window.scrollTo(0,0);
    }''')
    page.add_style_tag(content='''
      html {scroll-behavior:auto!important; overflow:hidden;}
      body {background:white; overflow:hidden;}
      #evolution {padding-top:24px; padding-bottom:24px;}
      #evolution .scroller {overflow:clip!important;}
      #evolution .fig-foot, #evolution #panel, .scroll-hint {display:none!important;}
      #evolution button:focus {outline:none!important;}
    ''')
    page.locator('#replay').evaluate('(el) => el.click()')
    # Satisfy the original entry timeout without letting it restart the timeline.
    page.clock.run_for(300)
    page.locator('#replay').evaluate('(el) => el.click()')
    box = page.locator('#evolution').bounding_box()
    css_height = math.ceil(box['height']/4)*4
    page.set_viewport_size({'width':1600,'height':css_height})
    width, height = 1600, css_height
    assert height % 2 == 0
    dest = CACHE/'MathRSI_evolution_v0-v4.mp4'
    cmd = ['ffmpeg','-hide_banner','-loglevel','error','-y','-f','image2pipe',
           '-framerate',str(FPS),'-vcodec','png','-i','pipe:0','-an','-c:v','libx264',
           '-preset','fast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(dest)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    def shot(name=None):
        frame = page.screenshot(type='png', animations='allow')
        if name: (CACHE/name).write_bytes(frame)
        return frame
    def put(frame, n=1):
        for _ in range(n): proc.stdin.write(frame)
    put(shot('frame-start.png'), FPS)
    states=[]
    frames=math.ceil((7400/SPEED + 500)/1000*FPS)
    print(json.dumps({'resolution':[width,height], 'animation_frames':frames, 'output':str(dest)}),flush=True)
    for i in range(frames):
        page.clock.run_for(round((i+1)*1000/FPS*SPEED/2.15)-round(i*1000/FPS*SPEED/2.15))
        frame=shot('frame-middle.png' if i==frames//2 else None)
        put(frame)
        if i%60==0:
            state=page.locator('#readout').inner_text()
            states.append({'frame':i,'state':state})
            print(f'frame {i}/{frames}: {state}',flush=True)
    final=shot('MathRSI_evolution_poster.png')
    put(final, FPS*5)
    proc.stdin.close()
    if proc.wait()!=0: raise RuntimeError('ffmpeg encoding failed')
    status=page.locator('#readout').inner_text()
    assert 'v4' in status and 'Current' in status, status
    assert not errors, errors
    geometry=page.evaluate('''() => {
      const sc=document.querySelector('#scroller'), st=document.querySelector('#stage');
      return {scrollLeft:sc.scrollLeft, clientWidth:sc.clientWidth,
        stageWidth:st.getBoundingClientRect().width, viewport:innerWidth};
    }''')
    assert geometry['scrollLeft']==0, geometry
    (OUT/'RECORDING.json').write_text(json.dumps({
      'source':str((SITE/'index.html').relative_to(ROOT)),'resolution':[width,height], 'fps':FPS,
      'duration_seconds':(FPS+frames+FPS*5)/FPS,
      'capture':'Actual Chromium rendering, deterministic browser clock, PNG frames to H.264',
      'recording_only_changes':'Isolated evolution section; browser time replayed at 0.60/2.15 speed; no JavaScript or product source edits',
      'states':states,'final_state':status,'page_errors':errors,'geometry':geometry,
      'file':str(dest.relative_to(ROOT))},indent=2)+'\n')
    browser.close()
server.shutdown()
print('DONE',flush=True)
# README exports retain the complete result bubbles, axis and harness-version row.
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(dest),
 '-vf','crop=1600:580:0:0','-c:v','libx264','-crf','19','-pix_fmt','yuv420p',
 '-movflags','+faststart',str(OUT/'evolution.mp4')],check=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(OUT/'evolution.mp4'),
 '-filter_complex','[0:v]fps=12,scale=1000:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3',
 '-loop','0',str(OUT/'evolution.gif')],check=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-sseof','-1',
 '-i',str(OUT/'evolution.mp4'),'-frames:v','1',str(OUT/'poster.png')],check=True)
