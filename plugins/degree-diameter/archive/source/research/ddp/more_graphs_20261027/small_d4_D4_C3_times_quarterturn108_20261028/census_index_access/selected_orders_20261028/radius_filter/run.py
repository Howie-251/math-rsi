from pathlib import Path
import subprocess,sys,json,time,resource
out=Path(__file__).resolve().parent;begin=time.process_time();cpu0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'worker.log').open('w') as log:
 p=subprocess.run([sys.executable,str(out/'filter.py')],stdout=log,stderr=subprocess.STDOUT,timeout=150)
cpu1=resource.getrusage(resource.RUSAGE_CHILDREN)
if p.returncode==0:
 r=json.loads((out/'WORKER_RESULT.json').read_text())
else:
 r={'status':'UNKNOWN_INCOMPLETE_PROCESS_TERMINATED','exit_code':p.returncode,'ordinary_bad_unordered_pairs':None,'actual_global_D':None}
 if (out/'checkpoint.json').exists():r['last_checkpoint']=json.loads((out/'checkpoint.json').read_text())
 if (out/'WORKER_ERROR.json').exists():r['error']=json.loads((out/'WORKER_ERROR.json').read_text())
r['execution_receipt']={'worker_process_CPU_seconds':cpu1.ru_utime+cpu1.ru_stime-cpu0.ru_utime-cpu0.ru_stime,'driver_CPU_seconds':time.process_time()-begin,'worker_CPU_hard_seconds':42,'aggregate_CPU_budget_seconds':45,'compile_CPU_seconds':0,'workers':1,'exit_code':p.returncode,'live_handle':None}
for name in ['RESULT.json','terminal.json']:(out/name).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)
