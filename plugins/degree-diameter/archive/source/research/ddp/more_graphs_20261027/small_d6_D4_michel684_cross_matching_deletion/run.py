from pathlib import Path
import json,sys,subprocess,time,resource
out=Path(__file__).resolve().parent;t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'worker.log').open('w') as f:p=subprocess.run([sys.executable,str(out/'controls.py')],stdout=f,stderr=subprocess.STDOUT,timeout=60)
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
if p.returncode==0:r=json.loads((out/'WORKER_RESULT.json').read_text())
else:
 r={'status':'PROCESS_ERROR_OR_LIMIT_INCOMPLETE','exit_code':p.returncode,'actual_global_D':None}
 if (out/'checkpoint.json').exists():r['last_checkpoint']=json.loads((out/'checkpoint.json').read_text())
r['execution_receipt']={'worker_process_CPU_seconds':c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,'driver_CPU_seconds':time.process_time()-t,'worker_CPU_hard_seconds':13,'aggregate_CPU_budget_seconds':15,'compile_CPU_seconds':0,'workers':1,'exit_code':p.returncode,'live_handle':None}
for name in ['RESULT.json','terminal.json']:(out/name).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)
