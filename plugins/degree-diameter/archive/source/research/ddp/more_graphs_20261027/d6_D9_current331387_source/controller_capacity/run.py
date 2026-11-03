from pathlib import Path
import json,resource,subprocess,time
out=Path(__file__).resolve().parent
child0=resource.getrusage(resource.RUSAGE_CHILDREN)
started=time.process_time()
with (out/'worker.log').open('w') as log:
 run=subprocess.run(['python',str(out/'count_dp.py')],stdout=log,stderr=subprocess.STDOUT,timeout=10)
child1=resource.getrusage(resource.RUSAGE_CHILDREN)
cpu=(child1.ru_utime+child1.ru_stime)-(child0.ru_utime+child0.ru_stime)
assert run.returncode==0
p=out/'RESULT.json';r=json.loads(p.read_text());r.update({'worker_process_CPU_seconds':cpu,'parent_CPU_seconds':time.process_time()-started,'worker_process_exit_code':0,'live_handle':None,'terminal':True});p.write_text(json.dumps(r,indent=2)+'\n')
terminal={k:r[k] for k in ['status','minimum_raw_count','first_minimum_phase','target_fiber_size','prediction_supported','exact_prefix_count','worker_process_CPU_seconds','worker_CPU_hard_limit_seconds','graphs','BFS']}
(out/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal),flush=True)
