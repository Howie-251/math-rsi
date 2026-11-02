"""Hard wall guard for the one fixed selected-member network batch."""
from pathlib import Path
import json
import os
import signal
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'selected_orders_20261028'
OUT.mkdir(exist_ok=True)
start=time.perf_counter()
p=subprocess.Popen([sys.executable,str(HERE/'download_selected.py')],start_new_session=True)
try:
    rc=p.wait(timeout=119)
    killed=False
except subprocess.TimeoutExpired:
    os.killpg(p.pid,signal.SIGKILL)
    rc=p.wait()
    killed=True
path=OUT/'DOWNLOAD_RECEIPT.json'
data=json.loads(path.read_text()) if path.exists() else {}
if rc!=0:
    data.update(status='PARTIAL_DOWNLOAD_WALL_OR_PROCESS_STOP',error=f'worker exit {rc}',
                whole_archive_downloaded=False,graph_parsing=0,graph_BFS=0,solver_calls=0)
data.update(worker_exit_code=rc,parent_wall_guard_triggered=killed,
            parent_wall_seconds=time.perf_counter()-start,configured_parent_wall_seconds=120)
path.write_text(json.dumps(data,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps({k:v for k,v in data.items() if k not in ('member_records','requests')},indent=2)+'\n')
print(json.dumps({'final_status':data['status'],'completed_members':len(data.get('completed_orders',[])),
                  'failed_orders':data.get('failed_orders',[]),'pending_orders':data.get('pending_orders',[]),
                  'parent_wall_seconds':data['parent_wall_seconds'],'worker_exit_code':rc},indent=2),flush=True)
