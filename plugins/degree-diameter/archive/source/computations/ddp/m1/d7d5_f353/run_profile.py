from pathlib import Path
import subprocess,json,time,resource,os
h=Path(__file__).resolve().parent
cmd=[str(h/'search'),'353','4','42','120','20261026',str(h/'profile')]
start=time.time();usage0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (h/'profile.log').open('w') as log:
 p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT)
 (h/'process.json').write_text(json.dumps(dict(pid=p.pid,wrapper_pid=os.getpid(),argv=cmd,start_unix=start),indent=2)+'\n')
 print(json.dumps(dict(status='RUNNING',pid=p.pid,argv=cmd)),flush=True)
 rc=p.wait()
usage1=resource.getrusage(resource.RUSAGE_CHILDREN)
result=dict(returncode=rc,wall_seconds=time.time()-start,cpu_seconds=usage1.ru_utime+usage1.ru_stime-usage0.ru_utime-usage0.ru_stime)
(h/'process_terminal.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
