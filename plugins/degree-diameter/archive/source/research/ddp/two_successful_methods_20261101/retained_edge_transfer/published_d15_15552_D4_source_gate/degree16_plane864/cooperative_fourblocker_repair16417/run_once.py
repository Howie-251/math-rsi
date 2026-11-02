#!/usr/bin/env python3
import time
START=time.process_time()
import json,os,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
PRIOR=35.491164489;PREP=1.;CAP=120.
def save(name,x):(HERE/name).write_text(json.dumps(x,indent=2)+'\n')
assert(HERE/'COOPERATIVE_BLOCKER_REPAIR_PAPER.md').is_file()
assert not(HERE/'ATTEMPT.json').exists(),'solefinitecase,noautomaticretry'
p=dict(status='STARTING',driver_pid=os.getpid(),prior_case_CPU_seconds=PRIOR,new_preparation_CPU_seconds=PREP,
 wholecase_CPU_cap_seconds=CAP,child_hard_CPU_seconds=80,single_worker=True)
save('ATTEMPT.json',p);save('HANDLE.json',p)
env=dict(os.environ)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:env[k]='1'
with(HERE/'STDOUT.log').open('w')as out,(HERE/'STDERR.log').open('w')as err:
 child=subprocess.Popen([sys.executable,'-u',str(HERE/'finite_child.py')],stdout=out,stderr=err,env=env)
 p.update(status='ACTUAL_CHILD_ACTIVE',child_pid=child.pid);save('HANDLE.json',p)
 _,status,usage=os.wait4(child.pid,0);child.returncode=os.waitstatus_to_exitcode(status)
childcpu=usage.ru_utime+usage.ru_stime;parentcpu=time.process_time()-START
r=json.loads((HERE/'CHILD_RESULT.json').read_text())if(HERE/'CHILD_RESULT.json').exists()else{}
if child.returncode!=0:r.update(status='UNKNOWN_CHILD_FAILURE_NO_RETRY',candidate_graphs_generated=0)
r.update(driver_pid=os.getpid(),child_pid=child.pid,child_exit_code=child.returncode,actual_all_child_CPU_seconds=childcpu,
 actual_driver_CPU_seconds=parentcpu,prior_case_CPU_seconds=PRIOR,new_preparation_CPU_seconds=PREP,
 wholecase_CPU_seconds=PRIOR+PREP+childcpu+parentcpu,wholecase_CPU_cap_seconds=CAP,terminal=True,active_processes=0)
save('RESULT.json',r);save('TERMINAL.json',r);save('HANDLE.json',r);print(json.dumps(r),flush=True)
