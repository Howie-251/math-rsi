import json
import resource
import subprocess
import time
from pathlib import Path
D=Path(__file__).resolve().parent
start=time.process_time(); initial=resource.getrusage(resource.RUSAGE_CHILDREN); wall=time.time()
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
phases=[]
def call(args,name,cap):
 before=cpu()
 def limit(): resource.setrlimit(resource.RLIMIT_CPU,(cap,cap+1))
 with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
  p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=limit)
  (D/'HANDLE.json').write_text(json.dumps(dict(pid=p.pid,phase=name,single_worker=True,CPU_budget_seconds=20),indent=2)+'\n')
  rc=p.wait()
 phases.append(dict(phase=name,returncode=rc,CPU_seconds_including_driver=cpu()-before))
 return rc
rc=call(['g++','-std=c++17','-O2','pilot.cpp','-o','pilot'],'compile',10)
if rc==0:
 remaining=20-cpu()
 if remaining>2: rc=call(['./pilot',str(remaining-0.8)],'pilot',int(remaining))
 else: rc=3
result=json.loads((D/'RESULT.json').read_text()) if (D/'RESULT.json').exists() else None
terminal=dict(status='PASS' if rc==0 else ('UNKNOWN_CPU_CAP' if rc in [3,-24,-9] else 'FAILED'),returncode=rc,total_CPU_seconds_including_compile_all_new_field_geometry_checks_and_aggregation=cpu(),wall_seconds=time.time()-wall,CPU_budget_seconds=20,single_worker=True,all_children_terminal=True,phases=phases,result=result,measurement_boundary='One compiler and newq8 field/geometry executable batch. All tables/projections generated fresh. Interactive source authoring excluded. No old input or graph/field revalidation.')
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
(D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',all_children_terminal=True,returncode=rc),indent=2)+'\n')
print(json.dumps(terminal,indent=2));raise SystemExit(rc)
