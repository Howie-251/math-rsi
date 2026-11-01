"""Run one agent-authorized light probe, capped at 20 s / 4 GiB per process."""
from pathlib import Path
import json
import os
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
env = os.environ.copy()
env['ELAN_HOME'] = str(ROOT/'.tools/elan')
env['PATH'] = env['ELAN_HOME']+'/bin:'+env.get('PATH','')
source, output = sys.argv[1:]
path = Path(output)
start = time.monotonic()
peak = 0
reason = None
with path.open('w') as log:
    process = subprocess.Popen(['lake','env','lean',source],cwd=ROOT/'formal',env=env,
                               stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    while process.poll() is None:
        elapsed = time.monotonic()-start
        table = subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True)
        rows = [tuple(map(int,line.split())) for line in table.splitlines() if line.strip()]
        ours = {process.pid}
        for _ in range(4):
            ours.update(pid for pid,ppid,_ in rows if ppid in ours)
        maximum = max((rss for pid,_,rss in rows if pid in ours),default=0)
        peak = max(peak, maximum)
        if elapsed >= 20 or maximum >= 4*1024*1024:
            reason = 'wall_20s' if elapsed >=20 else 'process_rss_4GiB'
            os.killpg(process.pid,signal.SIGTERM)
            process.wait(timeout=5)
            break
        time.sleep(.15)
    result = dict(source=source,exit_code=process.wait(),wall_seconds=time.monotonic()-start,
                  peak_process_rss_kib=peak,stopped_because=reason)
    log.write('\n'+json.dumps(result)+'\n')
print(json.dumps(result))
sys.exit(0 if result['exit_code']==0 else 1)
