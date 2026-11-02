"""One worker, bounded once; preserve checkpoint on a hard stop."""
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
started=time.process_time();wall=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
def save(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
env=os.environ.copy()
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):env[k]='1'
with (HERE/'worker.log').open('w') as log:
    proc=subprocess.Popen([sys.executable,str(HERE/'worker.py')],stdout=log,stderr=subprocess.STDOUT,env=env)
    save('RUN_HANDLE.json',{'status':'ACTUAL_FULL_STATIC_WORKER_RUNNING','running':True,'pid':proc.pid,
         'driver_pid':os.getpid(),'started_UTC':datetime.now(timezone.utc).isoformat(),
         'command':[sys.executable,str(HERE/'worker.py')],'aggregate_CPU_budget_seconds':130,
         'worker_CPU_hard_seconds':128,'preparation_CPU_limit_seconds':25,'solver_combined_seconds':95,
         'LP_calls_max':1,'MIP_calls_max':1,'workers':1,'threads':1,'wall_stop_seconds':200})
    print(json.dumps({'worker_pid':proc.pid,'driver_pid':os.getpid(),'status':'ACTUAL_FULL_STATIC_WORKER_RUNNING'}),flush=True)
    try:code=proc.wait(timeout=200)
    except subprocess.TimeoutExpired:
        proc.terminate()
        try:code=proc.wait(timeout=2)
        except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
r=resource.getrusage(resource.RUSAGE_CHILDREN)
child=r.ru_utime+r.ru_stime-r0.ru_utime-r0.ru_stime
receipt={'worker_exit_code':code,'worker_child_CPU_seconds':child,
         'driver_CPU_seconds':time.process_time()-started,'aggregate_CPU_seconds':child+time.process_time()-started,
         'wall_seconds':time.monotonic()-wall,'aggregate_CPU_budget_seconds':130,
         'compile_CPU_seconds':0,'workers':1,'threads':1,'retry_count':0}
if (HERE/'RESULT.json').exists(): result=json.loads((HERE/'RESULT.json').read_text())
else:
    checkpoint=json.loads((HERE/'checkpoint.json').read_text()) if (HERE/'checkpoint.json').exists() else None
    dims=json.loads((HERE/'MODEL_DIMENSIONS.json').read_text()) if (HERE/'MODEL_DIMENSIONS.json').exists() else None
    result={'status':'UNKNOWN_WORKER_LIMIT_OR_ERROR_NO_RETURN','target_Delta':15,'target_D':5,
            'source_n':102060,'source_m':765045,'hypothetical_n':102061,'actual_n':None,'actual_D':None,
            'ordinary_bad_unordered_pairs':None,'family_strictly_excluded':False,'last_checkpoint':checkpoint,
            'matrix_dimensions':dims,'full_model':bool(dims),'source_BFS':0,'ball_recomputation':0,
            'new_graphs_generated':0,'newroot_BFS':0,'hit':False}
result['execution_receipt']=receipt;save('RESULT.json',result)
save('terminal.json',{'status':result['status'],'execution_finished':True,'pending':[],
                      'hit':bool(result.get('hit')),'execution_receipt':receipt})
save('RUN_HANDLE.json',{'status':result['status'],'running':False,'execution_finished':True,
                         'pid':proc.pid,'execution_receipt':receipt})
print(json.dumps({'status':result['status'],'hit':bool(result.get('hit')),'execution_receipt':receipt}),flush=True)
