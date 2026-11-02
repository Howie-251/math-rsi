import json,os,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
env=os.environ.copy()
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:env[name]='1'
with (HERE/'worker.log').open('w') as log:
    worker=subprocess.Popen(['python',str(HERE/'worker.py')],stdout=log,stderr=subprocess.STDOUT,env=env)
    (HERE/'PARENT_HANDLE.json').write_text(json.dumps({'pid':worker.pid,'status':'WORKER_STARTED','wall_timeout_seconds':150},indent=2)+'\n')
    print('WORKER_PID',worker.pid,flush=True)
    wall_killed=False
    try:code=worker.wait(timeout=150)
    except subprocess.TimeoutExpired:
        wall_killed=True;worker.kill();code=worker.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
observed=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
receipt={'worker_exit_code':code,'worker_and_descendants_CPU_seconds':observed,'parent_elapsed_wall_seconds':time.monotonic()-start,'parent_wall_timeout_triggered':wall_killed,'wall_timeout_seconds':150}
(HERE/'PROCESS_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
if (HERE/'RESULT.json').exists():
    result=json.loads((HERE/'RESULT.json').read_text());result['process_receipt']=receipt
else:
    checkpoint=json.loads((HERE/'checkpoint.json').read_text()) if (HERE/'checkpoint.json').exists() else None
    result={'status':'UNKNOWN_PARENT_WALL_TIMEOUT' if wall_killed else 'UNKNOWN_PROCESS_TERMINATED','worker_exit_code':code,'checkpoint':checkpoint,'actual_n':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'hit':(HERE/'HIT.json').exists(),'family_strictly_excluded':False,'prediction':'UNKNOWN','process_receipt':receipt}
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['RUN_HANDLE.json','terminal.json','PARENT_HANDLE.json']:(HERE/name).write_text(json.dumps({'status':result['status'],'running':False,'execution_finished':True,'pending':[],'receipt':receipt},indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
