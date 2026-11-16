"""Capture the real homepage replay, ending at its live Current release.

Only the browser presentation is isolated/styled. Product files and application
state are never patched. Requires Python Playwright/Chromium and ffmpeg/ffprobe.
"""
from datetime import datetime, timedelta, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import json
import math
import subprocess
import threading
import traceback

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SITE = ROOT / 'development/homepage-redesign-20261105/site'
CACHE = ROOT / '.local/evolution-media-v5-dd-20261116'
FPS = 20
CLOCK_RATE = 0.25  # Browser-clock milliseconds per encoded-video millisecond.
OPENING_SECONDS = 1
FINAL_SECONDS = 6
VIEWPORT_WIDTH = 1900
GIF_WIDTH = 1400
GIF_FPS = 12
CAPTURE_CSS = '''
html {scroll-behavior:auto!important; overflow:hidden;}
body {background:white; overflow:hidden;}
#evolution {max-width:none; width:100%; padding:20px 24px;}
#evolution .evo-title {margin-top:0;}
#evolution .scroller {overflow:clip!important;}
#evolution .fig-foot, #evolution #panel, #evolution .row-b,
#evolution .row-p, .scroll-hint {display:none!important;}
#evolution button:focus {outline:none!important;}
#evolution .row-v {padding:12px 8px 14px;}
#evolution .vtag {font-size:24px;}
#evolution .vstate {font-size:18px;}
#evolution .vname {font-size:18px; line-height:1.25;}
#evolution .delta-tag[data-v="5"] .delta-value {font-size:20px;}
'''


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def ffmpeg(*args):
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *map(str, args)], check=True)


def probe(path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-count_frames',
        '-select_streams', 'v:0', '-show_entries',
        'stream=codec_name,width,height,r_frame_rate,nb_read_frames:format=duration',
        '-of', 'json', str(path)], capture_output=True, text=True, check=True)
    data = json.loads(result.stdout)
    return {**data['streams'][0], 'duration_seconds': float(data['format']['duration']),
            'bytes': path.stat().st_size}


def log(event, **fields):
    with (CACHE / 'attempts.jsonl').open('a') as file:
        file.write(json.dumps({'time': datetime.now(timezone.utc).isoformat(),
                               'event': event, **fields}, ensure_ascii=False) + '\n')


def capture(preview=False):
    CACHE.mkdir(parents=True, exist_ok=True)
    log('start', preview=preview, viewport_width=VIEWPORT_WIDTH, clock_rate=CLOCK_RATE)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    proc = None
    try:
        errors, failed_requests = [], []
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': VIEWPORT_WIDTH, 'height': 1500},
                                    device_scale_factor=1, reduced_motion='no-preference')
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.on('requestfailed', lambda r: failed_requests.append({'url': r.url, 'error': r.failure}))
            fixed = datetime(2026, 11, 16, tzinfo=timezone.utc)
            page.clock.install(time=fixed)
            page.clock.pause_at(fixed + timedelta(seconds=1))
            page.goto(f'http://127.0.0.1:{server.server_port}/development/homepage-redesign-20261105/site/index.html')
            page.evaluate('document.fonts.ready')
            expected = page.locator('.row-v:not(.fut) .vtag').all_text_contents()
            current_index = page.locator('.row-v.current').get_attribute('data-v')
            current = page.locator('.row-v.current .vtag').inner_text()
            page.evaluate('''() => {
                const evo = document.querySelector('#evolution');
                document.body.append(evo);
                for (const el of document.body.children) if (el !== evo) el.style.display = 'none';
                scrollTo(0, 0);
            }''')
            page.add_style_tag(content=CAPTURE_CSS)
            geometry = page.evaluate('''() => {
                const sc = document.querySelector('#scroller');
                return {scrollLeft:sc.scrollLeft, clientWidth:sc.clientWidth,
                    stageWidth:document.querySelector('#stage').getBoundingClientRect().width,
                    viewport:innerWidth,
                    versionRowBottom:Math.max(...[...document.querySelectorAll('.row-v,.lane-axis')].map(e=>e.getBoundingClientRect().bottom))};
            }''')
            height = math.ceil((geometry['versionRowBottom'] + 20) / 2) * 2
            page.set_viewport_size({'width': VIEWPORT_WIDTH, 'height': height})
            clip = {'x': 0, 'y': 0, 'width': VIEWPORT_WIDTH, 'height': height}
            assert geometry['stageWidth'] <= geometry['clientWidth'] and geometry['scrollLeft'] == 0, geometry

            def shot(name=None):
                frame = page.screenshot(type='png', clip=clip, animations='allow')
                if name:
                    (CACHE / name).write_bytes(frame)
                return frame

            def final_geometry():
                return page.evaluate('''() => {
                    const rect=e=>{const r=e.getBoundingClientRect();return {left:r.left,top:r.top,right:r.right,bottom:r.bottom}};
                    const q=document.querySelector('.delta-tag[data-c="q6"][data-v="5"]');
                    const d=document.querySelector('.delta-tag[data-c="dd"][data-v="5"]');
                    return {scrollLeft:document.querySelector('#scroller').scrollLeft,
                        currentVersion:document.querySelector('.row-v.current').innerText,
                        currentRow:rect(document.querySelector('.row-v.current')),
                        futureRow:rect(document.querySelector('.row-v.fut')),
                        dd:{text:d.textContent,visible:d.getAttribute('aria-hidden')==='false',opacity:getComputedStyle(d).opacity,box:rect(d)},
                        q7:{text:q.textContent,visible:q.getAttribute('aria-hidden')==='false',opacity:getComputedStyle(q).opacity,box:rect(q)}};
                }''')

            if preview:
                page.locator(f'[data-goto="{current_index}"]').first.evaluate('(e)=>e.click()')
                page.clock.run_for(3000)
                page.wait_for_timeout(350)
                shot('preview-poster.png')
                (CACHE / 'preview-geometry.json').write_text(json.dumps({
                    'resolution': [VIEWPORT_WIDTH, height], 'geometry': geometry,
                    'final': final_geometry()}, ensure_ascii=False, indent=2) + '\n')
                browser.close()
                ffmpeg('-i', CACHE / 'preview-poster.png', '-vf', 'scale=900:-2:flags=lanczos',
                       CACHE / 'preview-github-900.png')
                log('preview_complete', resolution=[VIEWPORT_WIDTH, height])
                return

            # Consume the original entry timeout, then use the real Replay control.
            page.locator('#replay').evaluate('(e)=>e.click()')
            page.clock.run_for(300)
            page.locator('#replay').evaluate('(e)=>e.click()')
            source_video = CACHE / 'capture-source.mp4'
            proc = subprocess.Popen(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                '-f', 'image2pipe', '-framerate', str(FPS), '-vcodec', 'png', '-i', 'pipe:0',
                '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-pix_fmt', 'yuv420p',
                '-movflags', '+faststart', str(source_video)], stdin=subprocess.PIPE)
            def put(frame, count=1):
                for _ in range(count):
                    proc.stdin.write(frame)

            start_state = page.locator('#readout').inner_text()
            assert start_state.startswith('v0'), start_state
            put(shot('start-v0.png'), FPS * OPENING_SECONDS)
            states = [{'frame': 0, 'video_seconds': 0, 'state': start_state}]
            last_state = start_state
            animation_frames = 0
            for i in range(FPS * 60):
                before = round(i * 1000 / FPS * CLOCK_RATE)
                after = round((i + 1) * 1000 / FPS * CLOCK_RATE)
                page.clock.run_for(after - before)
                frame = shot()
                put(frame)
                animation_frames += 1
                state = page.locator('#readout').inner_text()
                if state != last_state:
                    item = {'frame': FPS * OPENING_SECONDS + animation_frames - 1,
                            'video_seconds': OPENING_SECONDS + animation_frames / FPS,
                            'browser_clock_ms': after, 'state': state}
                    states.append(item)
                    (CACHE / f'state-{state.split()[0]}.png').write_bytes(frame)
                    print(json.dumps(item), flush=True)
                    last_state = state
                if page.locator('#play').get_attribute('data-s') == 'play':
                    break
            else:
                raise RuntimeError('The real player did not finish within 60 encoded seconds')
            page.wait_for_timeout(350)  # Let compositor-only opacity transitions settle too.
            status = page.locator('#readout').inner_text()
            final = final_geometry()
            assert current in status and 'Current' in status, status
            assert [x['state'].split('Origins')[0].split('Release')[0].split('Current')[0] for x in states] == expected, states
            assert all(final[k]['visible'] and float(final[k]['opacity']) == 1 for k in ['q7','dd']), final
            for rect in [final['q7']['box'], final['dd']['box'], final['currentRow'], final['futureRow']]:
                assert 0 <= rect['left'] < rect['right'] <= VIEWPORT_WIDTH and 0 <= rect['top'] < rect['bottom'] <= height, rect
            assert final['scrollLeft'] == 0 and not errors and not failed_requests, (final, errors, failed_requests)
            final_frame = shot('settled-current.png')
            put(final_frame, FPS * FINAL_SECONDS)
            proc.stdin.close()
            if proc.wait() != 0:
                raise RuntimeError('ffmpeg encoding failed')
            browser.close()
        # No fixed 580px crop: the encoded source already uses the measured bounds.
        mp4, gif, poster = CACHE/'evolution.mp4', CACHE/'evolution.gif', CACHE/'poster.png'
        ffmpeg('-i', source_video, '-c', 'copy', '-movflags', '+faststart', mp4)
        ffmpeg('-i', mp4, '-filter_complex',
            f'[0:v]fps={GIF_FPS},scale={GIF_WIDTH}:-2:flags=lanczos,split[a][b];'
            '[a]palettegen=max_colors=128:stats_mode=diff[p];'
            '[b][p]paletteuse=dither=bayer:bayer_scale=3', '-loop', '0', gif)
        ffmpeg('-sseof', '-0.08', '-i', mp4, '-frames:v', '1', poster)
        metadata = {'mp4': probe(mp4), 'gif': probe(gif)}
        gif_last = int(metadata['gif']['nb_read_frames']) - 1
        ffmpeg('-i', gif, '-vf', f'select=eq(n\\,{gif_last})', '-frames:v', '1', CACHE/'gif-last-decoded.png')
        ffmpeg('-i', poster, '-vf', 'scale=900:-2:flags=lanczos', CACHE/'github-900.png')
        for path in [mp4, gif, poster]:
            (OUT / path.name).write_bytes(path.read_bytes())
        receipt = {
            'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
            'source': str((SITE/'index.html').relative_to(ROOT)),
            'source_commit': subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'], text=True).strip(),
            'source_working_tree_changes': subprocess.check_output(['git','-C',str(ROOT),'diff','--name-only','HEAD','--',str(SITE)], text=True).splitlines(),
            'source_revision_note': 'Recorded the named HEAD with the listed presentation edits; the handoff commit contains the exact source used.',
            'current_version': current, 'expected_versions': expected,
            'capture': 'Actual Chromium Replay animation; deterministic browser clock; PNG frames to H.264',
            'recording_only_changes': 'Isolate evolution; hide detailed Base/Plugins rows and panel; enlarge version labels and Q7/DD headlines; preserve all seven columns. Product JS/CSS/data unchanged.',
            'capture_css': CAPTURE_CSS.strip(),
            'resolution': [VIEWPORT_WIDTH, height], 'fps': FPS, 'browser_clock_rate': CLOCK_RATE,
            'opening_hold_seconds': OPENING_SECONDS, 'final_hold_seconds': FINAL_SECONDS,
            'animation_frames': animation_frames,
            'duration_seconds': OPENING_SECONDS + animation_frames / FPS + FINAL_SECONDS,
            'completion': 'Wait for native play control to stop at Current; no hard-coded timeline end',
            'states': states, 'final_state': status, 'geometry': geometry, 'final_geometry': final,
            'page_errors': errors, 'failed_requests': failed_requests,
            'exports': metadata, 'poster_resolution': [VIEWPORT_WIDTH, height],
            'intermediates': str(CACHE.relative_to(ROOT)),
            'verification': 'MP4 final frame decoded as poster; last GIF frame decoded separately; 900px README preview rendered. Visual inspection is a separate human/agent step.'
        }
        (OUT/'RECORDING.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
        log('complete', duration_seconds=receipt['duration_seconds'], exports=metadata)
        print(json.dumps({'final_state':status,'resolution':receipt['resolution'],
                          'duration_seconds':receipt['duration_seconds'],'exports':metadata}), flush=True)
    except Exception:
        log('failure', traceback=traceback.format_exc())
        raise
    finally:
        if proc and proc.poll() is None:
            if proc.stdin and not proc.stdin.closed:
                proc.stdin.close()
            proc.terminate()
            proc.wait()
        server.shutdown()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview', action='store_true', help='Inspect measured final-state crop before recording')
    capture(preview=parser.parse_args().preview)
