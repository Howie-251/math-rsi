from pathlib import Path
import subprocess,sys,resource,time,json
p=Path(__file__).resolve().parent;t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with(p/'control.log').open('w') as f:r=subprocess.run([sys.executable,str(p/'control.py')],stdout=f,stderr=subprocess.STDOUT,timeout=8)
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
if r.returncode==0:x=json.loads((p/'WORKER_RESULT.json').read_text())
else:x={'status':'CONTROL_UNKNOWN_PROCESS_LIMIT_OR_ERROR','exit_code':r.returncode,'solver_calls':0,'actual_global_D':None}
x['execution_receipt']={'exit_code':r.returncode,'worker_process_CPU_seconds':c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,'driver_CPU_seconds':time.process_time()-t,'worker_CPU_hard_seconds':5,'wall_guard_seconds':8,'workers':1,'live_handle':None}
for name in ['RESULT.json','terminal.json']:(p/name).write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps(x))
