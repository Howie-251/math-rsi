from pathlib import Path
import json,subprocess,sys,time,resource
out=Path(__file__).resolve().parent;t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'prepare.log').open('w') as f:p=subprocess.run([sys.executable,str(out/'prepare_model.py')],stdout=f,stderr=subprocess.STDOUT,timeout=60)
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
if p.returncode==0:r=json.loads((out/'MODEL_STATS.json').read_text())
else:r={'status':'ERROR_OR_LIMIT_PREPARATION_INCOMPLETE','exit_code':p.returncode,'solver_calls':0,'matching_graphs_generated':0}
r['execution_receipt']={'exit_code':p.returncode,'worker_process_CPU_seconds':c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,'driver_CPU_seconds':time.process_time()-t,'worker_CPU_hard_seconds':18,'aggregate_preparation_CPU_budget_seconds':20,'workers':1,'live_handle':None}
(out/'PREPARATION_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
