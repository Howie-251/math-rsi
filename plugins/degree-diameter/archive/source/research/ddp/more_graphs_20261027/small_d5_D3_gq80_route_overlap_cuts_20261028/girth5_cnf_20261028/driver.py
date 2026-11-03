"""One45-second parent wall guard; no solver restart."""
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
cpu0,wall0=time.process_time(),time.perf_counter()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (HERE/'worker.log').open('w') as log:
    p=subprocess.Popen([sys.executable,str(HERE/'worker.py')],stdout=log,stderr=subprocess.STDOUT,
                       start_new_session=True)
    try:
        rc=p.wait(timeout=45);wall_kill=False
    except subprocess.TimeoutExpired:
        os.killpg(p.pid,signal.SIGKILL);rc=p.wait();wall_kill=True
after=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
path=HERE/'RESULT.json'
out=json.loads(path.read_text()) if path.exists() else {}
if rc!=0 or not path.exists():
    out.update(status='UNKNOWN_GIRTH5_WORKER_EXIT_NO_COMPLETED_RESULT',candidate_graphs=0,
               incumbent_exported=False,graph_BFS_calls=0,actual_D=None,
               ordinary_bad_unordered_pairs=None,prediction_status='UNKNOWN_NOT_REFUTED')
out.update(worker_exit_code=rc,parent_wall_guard_triggered=wall_kill,
           measured_worker_and_children_CPU_seconds=child_cpu,
           parent_CPU_seconds=time.process_time()-cpu0,
           aggregate_parent_children_CPU_seconds=child_cpu+time.process_time()-cpu0,
           observed_parent_wall_seconds=time.perf_counter()-wall0,configured_parent_wall_seconds=45)
for name in ('RESULT.json','terminal.json','RUN_HANDLE.json'):
    (HERE/name).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
