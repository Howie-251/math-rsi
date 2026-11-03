from pathlib import Path
import json,time,resource,subprocess,sys
out=Path(__file__).resolve().parent;t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'binding.log').open('w') as f:p=subprocess.run([sys.executable,str(out/'bind_source.py')],stdout=f,stderr=subprocess.STDOUT,timeout=30)
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
if p.returncode==0:r=json.loads((out/'WORKER_RESULT.json').read_text())
else:
 r={'status':'UNKNOWN_SINGLE_BINDING_PROCESS_LIMIT_OR_ERROR','exit_code':p.returncode,'isomorphic':None,'retry_count':0,'matching_graphs':0,'source_BFS':0}
 if (out/'checkpoint.json').exists():r['last_checkpoint']=json.loads((out/'checkpoint.json').read_text())
r['execution_receipt']={'worker_process_CPU_seconds':c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,'driver_CPU_seconds':time.process_time()-t,'worker_CPU_hard_seconds':8,'aggregate_CPU_budget_seconds':10,'compile_CPU_seconds':0,'workers':1,'exit_code':p.returncode,'live_handle':None}
for n in ['BINDING_RESULT.json','binding_terminal.json']:(out/n).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)
