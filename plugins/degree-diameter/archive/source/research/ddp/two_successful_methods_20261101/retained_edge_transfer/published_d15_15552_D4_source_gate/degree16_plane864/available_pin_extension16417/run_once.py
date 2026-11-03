#!/usr/bin/env python3
"""Sole parent/child case with actual wait4 CPU accounting and hard50 child."""
import time
START=time.process_time()
import json,os,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
PREP=1.0;CAP=60.0
def save(name,x):(HERE/name).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
assert not(HERE/'ATTEMPT.json').exists(),'oneauthorizedattemptonly;noautomaticretry'
packet=dict(status='STARTING_SOLE_AVAILABLE_PIN_COVER_CASE',driver_pid=os.getpid(),
 new_preparation_reserve_CPU_seconds=PREP,wholecase_CPU_cap_seconds=CAP,child_hard_CPU_seconds=50,
 max_solver_window_seconds=30,single_worker=True,new_graph_parameter_Lean_counts=[0,0,0])
save('ATTEMPT.json',packet);save('HANDLE.json',packet)
env=dict(os.environ)
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:env[key]='1'
cmd=[sys.executable,'-u',str(HERE/'cover_child.py'),'--hard-cpu','50']
with(HERE/'STDOUT.log').open('w')as out,(HERE/'STDERR.log').open('w')as err:
 child=subprocess.Popen(cmd,stdout=out,stderr=err,env=env)
 packet.update(status='ACTUAL_CHILD_ACTIVE',child_pid=child.pid,command=cmd)
 save('HANDLE.json',packet)
 _,status,usage=os.wait4(child.pid,0);child.returncode=os.waitstatus_to_exitcode(status)
childcpu=usage.ru_utime+usage.ru_stime;parentcpu=time.process_time()-START
result=json.loads((HERE/'CHILD_RESULT.json').read_text())if(HERE/'CHILD_RESULT.json').exists()else{}
if child.returncode!=0:result.update(status='UNKNOWN_CHILD_FAILURE_NO_RETRY',child_failure_exit=child.returncode,new_graphs=0)
if not result:result=dict(status='UNKNOWN_NO_CHILD_RESULT_NO_RETRY',new_graphs=0)
result.update(driver_pid=os.getpid(),child_pid=child.pid,child_exit_code=child.returncode,actual_all_child_CPU_seconds=childcpu,actual_driver_CPU_seconds=parentcpu,
 new_preparation_reserve_CPU_seconds=PREP,wholecase_CPU_seconds=PREP+childcpu+parentcpu,wholecase_CPU_cap_seconds=CAP,
 terminal=True,active_processes=0,solver_retry_count=0)
save('RESULT.json',result);save('TERMINAL.json',result);save('HANDLE.json',result)
print(json.dumps(result),flush=True)
