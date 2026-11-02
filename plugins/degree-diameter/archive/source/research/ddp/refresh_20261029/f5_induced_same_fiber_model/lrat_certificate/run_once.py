#!/usr/bin/env python3
"""One LRAT reproduction and one independent check, without changing the CNF."""
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[4]
CNF=HERE.parent/'model.cnf'
SOLVER=PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'
CHECKER=PROJECT/'.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'
assert not (HERE/'HANDLE.json').exists(), 'This unique certificate attempt has already started.'
assert not (HERE/'TERMINAL.json').exists(), 'This certificate attempt already terminated.'
start=time.process_time();wall_start=time.monotonic()
c0=resource.getrusage(resource.RUSAGE_CHILDREN);child0=c0.ru_utime+c0.ru_stime
def child_cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return c.ru_utime+c.ru_stime
def used():return time.process_time()-start+child_cpu()-child0
def save(name,value):(HERE/name).write_text(json.dumps(value,indent=2)+'\n')
def source_info():
    s=CNF.stat()
    with CNF.open() as f:header=f.readline().strip()
    return {'path':str(CNF),'header':header,'bytes':s.st_size,'mtime_ns':s.st_mtime_ns,'inode':s.st_ino}
source_before=source_info()
assert source_before['header']=='p cnf 333551 2316695'
prior=json.loads((HERE.parent/'CEGIS_TERMINAL.json').read_text())
assert prior['status']=='RAW_UNSAT_UNCERTIFIED' and prior['actual_solver_calls']==1
old_solver_cpu=prior['solver_CPU_seconds']
old_whole_cpu=prior['total_CPU_seconds_including_prior_preparation']
assert old_solver_cpu+121<300 and old_whole_cpu+220<360
save('INPUT_AND_BUDGET.json',{'CNF':source_before,'original_raw_solver_CPU_seconds':old_solver_cpu,
    'original_whole_CPU_seconds':old_whole_cpu,'certificate_whole_CPU_limit':220,
    'solver_window':120,'solver_CPU_hard_limit':121,'checker_CPU_limit':90,
    'combined_whole_CPU_limit':360,'combined_solver_CPU_limit':300,
    'solver_version':'2.1.2','checker_version':'0.2.0',
    'proof_format':'binary LRAT, CaDiCaL default binary encoding',
    'checker_success_rule':'exit20 and s VERIFIED; CNF explicitly supplied'})

def run_stage(name,command,limit_seconds):
    before=child_cpu();wall=time.monotonic()
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(limit_seconds,limit_seconds))
    with (HERE/(name+'.stdout')).open('w') as out:
        proc=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
        handle={'status':'RUNNING_'+name.upper(),'driver_pid':os.getpid(),'pid':proc.pid,
            'command':command,'CPU_hard_limit_seconds':limit_seconds,
            'certificate_CPU_before':used(),'running':True}
        save('HANDLE.json',handle);save(name+'.HANDLE.json',handle)
        print(json.dumps(handle),flush=True)
        observations=0
        while True:
            try:code=proc.wait(timeout=5);break
            except subprocess.TimeoutExpired:observations+=1
    result={'name':name,'pid':proc.pid,'command':command,'returncode':code,
        'CPU_hard_limit_seconds':limit_seconds,'CPU_seconds':child_cpu()-before,
        'wall_seconds':time.monotonic()-wall,'observation_timeouts':observations,
        'same_PID_waited_to_exit':True}
    save(name+'.RESULT.json',result)
    print(json.dumps({'event':name+'_FINISHED',**result}),flush=True)
    return result

status='NOT_STARTED';solver=None;checker=None;verified=False;error=None
try:
    command=[str(SOLVER),'-q','-t','120','--lrat',str(CNF),str(HERE/'certificate.lrat')]
    solver=run_stage('solver',command,121)
    if source_info()!=source_before:
        status='INPUT_FILE_CHANGED_NO_CERTIFICATION'
    elif solver['returncode']!=20:
        status='CERTIFICATE_SOLVER_NOT_UNSAT_KEEP_PRIOR_RAW_RESULT'
    elif not (HERE/'certificate.lrat').is_file() or (HERE/'certificate.lrat').stat().st_size==0:
        status='NO_LRAT_CERTIFICATE_KEEP_PRIOR_RAW_RESULT'
    else:
        remaining=min(90,math.floor(220-used()-2),math.floor(360-old_whole_cpu-used()-2))
        if remaining<1:
            status='CERTIFICATE_BUDGET_BEFORE_CHECK_KEEP_PRIOR_RAW_RESULT'
        else:
            command=[str(CHECKER),str(CNF),str(HERE/'certificate.lrat')]
            checker=run_stage('checker',command,remaining)
            verified_line=any(line.strip()=='s VERIFIED' for line in (HERE/'checker.stdout').read_text().splitlines())
            if source_info()!=source_before:
                status='INPUT_FILE_CHANGED_NO_CERTIFICATION'
            elif checker['returncode']==20 and verified_line:
                verified=True;status='LRAT_VERIFIED_UNSAT_EXACT_CNF'
            else:
                status='LRAT_NOT_VERIFIED_KEEP_PRIOR_RAW_RESULT'
except Exception as exc:
    error={'type':type(exc).__name__,'message':str(exc)}
    status='ERROR_STOP_NO_RETRY_KEEP_PRIOR_RAW_RESULT'
result={'status':status,'verified_UNSAT_of_exact_CNF':verified,'input':source_before,
    'solver':solver,'checker':checker,
    'certificate_whole_CPU_seconds':used(),'certificate_whole_CPU_limit':220,
    'combined_whole_CPU_seconds':old_whole_cpu+used(),
    'combined_solver_CPU_seconds':old_solver_cpu+(solver['CPU_seconds'] if solver else 0),
    'wall_seconds':time.monotonic()-wall_start,'proof_bytes':(HERE/'certificate.lrat').stat().st_size if (HERE/'certificate.lrat').exists() else 0,
    'error':error,'running':False,'automatic_retry':False,'source_CNF_modified_by_this_run':False,
    'old_terminal_modified':False,'new_graphs':0,'BFS_runs':0,
    'mathematical_encoding_scope':'CNF certificate only; H65 and graph-to-CNF preservation remain separate review obligations'}
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:save(name,result)
print(json.dumps(result),flush=True)
