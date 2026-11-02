"""Launch the single authorized bounded worker and recover a terminal on kill."""
import json
import resource
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
cpu0, wall0 = time.process_time(), time.perf_counter()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
with (HERE / 'production.log').open('w') as log:
    p = subprocess.Popen([sys.executable, str(HERE / 'worker.py')], stdout=log, stderr=subprocess.STDOUT)
    try:
        rc = p.wait(timeout=75)
        wall_kill = False
    except subprocess.TimeoutExpired:
        p.kill()
        rc = p.wait()
        wall_kill = True
after = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime
stats = json.loads((HERE / 'MODEL_STATS.json').read_text())
result_path = HERE / 'RESULT.json'
out = json.loads(result_path.read_text()) if result_path.exists() else {}
if rc != 0 or not result_path.exists():
    out.update(status='UNKNOWN_PROCESS_TERMINATED_NO_RETURNED_SOLVER_RESULT',
               incumbent_reported=False, candidate_graphs=0, graph_BFS_calls=0,
               actual_D=None, ordinary_bad_unordered_pairs=None, solver_calls=1)
out.update(process_returncode=rc, wall_fallback_triggered=wall_kill,
           measured_worker_CPU_seconds=child_cpu, driver_CPU_seconds=time.process_time()-cpu0,
           inherited_preparation_CPU_seconds=stats['preparation_CPU_seconds'],
           total_measured_CPU_seconds=child_cpu+time.process_time()-cpu0+stats['preparation_CPU_seconds'],
           driver_wall_seconds=time.perf_counter()-wall0, configured_solver_seconds=45,
           configured_aggregate_CPU_hard_seconds=55)
for name in ('RESULT.json', 'terminal.json', 'RUN_HANDLE.json'):
    (HERE / name).write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2), flush=True)
