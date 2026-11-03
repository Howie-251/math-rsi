from pathlib import Path
import subprocess,sys,time,resource,json
here=Path(__file__).resolve().parent;before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.perf_counter()
with (here/'production.log').open('w') as out:
 proc=subprocess.Popen([sys.executable,str(here/'run.py')],stdout=out,stderr=subprocess.STDOUT)
 try:rc=proc.wait(timeout=145)
 except subprocess.TimeoutExpired:proc.kill();rc=proc.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
path=here/'terminal.json';r=json.loads(path.read_text()) if path.exists() else {}
if rc:r.update(status='PROCESS_EXIT_OR_LIMIT_WITH_PARTIAL_CASE_FILES',whole_family_excluded=False)
r.update(returncode=rc,measured_process_CPU_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,driver_wall_seconds=time.perf_counter()-start)
path.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='cases'},indent=2))
