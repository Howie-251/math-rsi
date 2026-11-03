from pathlib import Path
import subprocess,sys,json,resource,time
H=Path(__file__).resolve().parent;t=time.perf_counter();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (H/'production.log').open('w') as out:
 p=subprocess.Popen([sys.executable,str(H/'run.py')],stdout=out,stderr=subprocess.STDOUT)
 try:rc=p.wait(timeout=130)
 except subprocess.TimeoutExpired:p.kill();rc=p.wait()
r=resource.getrusage(resource.RUSAGE_CHILDREN);f=H/'terminal.json';d=json.loads(f.read_text()) if f.exists() else {}
if rc:d.update(status='PROCESS_LIMIT_OR_EXIT_NO_RETURNED_INCUMBENT',incumbent=False,pending=[])
d.update(process_returncode=rc,measured_process_CPU_seconds=r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime,driver_wall_seconds=time.perf_counter()-t)
f.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
