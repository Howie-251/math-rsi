"""Run the one hard-budget process and record a terminal status on a budget kill."""
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
start=time.perf_counter()
before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (HERE/'production.log').open('w') as log:
    process=subprocess.Popen([sys.executable,str(HERE/'run.py')],stdout=log,stderr=subprocess.STDOUT)
    try:
        rc=process.wait(timeout=22)
    except subprocess.TimeoutExpired:
        process.kill();rc=process.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
path=HERE/'terminal.json'
d=json.loads(path.read_text()) if path.exists() else {}
if rc!=0:
    d.update(status='HARD_BUDGET_OR_PROCESS_EXIT_NO_EXPORTED_INCUMBENT',process_returncode=rc,
             incumbent_exported=False,graph_BFS_count=0,new_lower_bounds=0,pending=[])
d.update(process_returncode=rc,driver_wall_seconds=time.perf_counter()-start,
         measured_process_CPU_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
sys.path.insert(0,str(HERE.parents[3]/'aris_repo/tools'))
from capture_filter import screen
text=json.dumps(d,indent=2)+'\n'
assert not screen(text)
path.write_text(text)
print(text)
