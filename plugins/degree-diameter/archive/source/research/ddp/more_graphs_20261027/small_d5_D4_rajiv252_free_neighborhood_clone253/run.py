from pathlib import Path
import subprocess,sys,time,resource,json
out=Path(__file__).resolve().parent;t0=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'worker.log').open('w') as f:p=subprocess.run([sys.executable,str(out/'criticality.py')],stdout=f,stderr=subprocess.STDOUT,timeout=60)
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
if p.returncode==0:r=json.loads((out/'WORKER_RESULT.json').read_text())
else:r={'status':'ERROR_OR_LIMIT_NO_COMPLETE_SCOPE','exit_code':p.returncode,'target_actual_n':None,'target_actual_D':None}
r['execution_receipt']={'exit_code':p.returncode,'worker_process_CPU_seconds':c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,'driver_CPU_seconds':time.process_time()-t0,'worker_CPU_hard_seconds':13,'aggregate_CPU_budget_seconds':15,'compile_CPU_seconds':0,'workers':1,'live_handle':None}
for n in ['RESULT.json','terminal.json']:(out/n).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)
