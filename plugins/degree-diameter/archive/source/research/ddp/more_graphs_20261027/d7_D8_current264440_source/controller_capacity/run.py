from pathlib import Path
import resource,subprocess,json,time
out=Path(__file__).resolve().parent;started=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'worker.log').open('w') as log:
 run=subprocess.run(['python',str(out/'count_dp.py')],stdout=log,stderr=subprocess.STDOUT,timeout=10)
after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
assert run.returncode==0
p=out/'RESULT.json';r=json.loads(p.read_text());r.update({'worker_process_CPU_seconds':cpu,'parent_CPU_seconds':time.process_time()-started,'worker_process_exit_code':0,'live_handle':None,'terminal':True});p.write_text(json.dumps(r,indent=2)+'\n')
t={k:r[k] for k in ['status','minimum_raw_count','first_minimum_slot','first_minimum_phase','first_minimum_normal11','target_fiber_size','prefix_count','worker_process_CPU_seconds','worker_CPU_hard_limit_seconds','graphs','BFS']};(out/'terminal.json').write_text(json.dumps(t,indent=2)+'\n');print(json.dumps(t),flush=True)
