#!/usr/bin/env python3
"""One small independent SAT attack on the six large proper supports."""
from pathlib import Path
import importlib.util
import json
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
OLD=HERE.parent/'f5_induced_retention_closure'
SUPPORT=HERE.parent/'f5_induced_support_closure'
assert not (HERE/'SUPPORT_CHECK_HANDLE.json').exists()
start=time.process_time();child0=resource.getrusage(resource.RUSAGE_CHILDREN)
child0=child0.ru_utime+child0.ru_stime
spec=importlib.util.spec_from_file_location('prior_exact_gate_definitions',OLD/'prepare.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
words=json.loads((OLD/'CONTROLLER_UNIQUE_WORDS.json').read_text())
supports=json.loads((SUPPORT/'LARGE_PROPER_SUPPORTS.json').read_text())['supports']
assert len(words)==258 and len(supports)==6
cnf=module.CNF(HERE/'support.body.tmp');cnf.nv=30
for word in words:
    u,a,b,v=word['vertices']
    cnf.add(-(u+1),-(v+1),a+1)
    cnf.add(-(u+1),-(v+1),b+1)
prev=[True]+[False]*16
for i in range(1,31):
    cur=[True]+[False]*16
    for j in range(1,min(i,16)+1):
        cur[j]=cnf.threshold_step(prev[j],prev[j-1],i)
    prev=cur
cnf.add(prev[16])
cnf.add(*[-i for i in range(1,31)])
blocked=[]
for record in supports:
    s=set(record['support'])
    assert 16<=len(s)<30
    clause=[-(v+1) if v in s else v+1 for v in range(30)]
    cnf.add(*clause);blocked.append(clause)
cnf.f.close()
with (HERE/'support_check.cnf').open('w') as out:
    out.write(f'p cnf {cnf.nv} {cnf.nc}\n')
    out.write((HERE/'support.body.tmp').read_text())
(HERE/'support.body.tmp').unlink()
model={'support_variables':30,'variables':cnf.nv,'clauses':cnf.nc,
       'ordered_words':258,'support_at_least':16,'proper':True,
       'blocked_exact_assignments':[r['support'] for r in supports],
       'blocking_clauses':blocked,'algorithm':'one SAT attack, no NextClosure enumeration'}
(HERE/'SUPPORT_CHECK_MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
command=[str(PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t','2',
         '-w',str(HERE/'support_check.sol'),str(HERE/'support_check.cnf')]
def limit():resource.setrlimit(resource.RLIMIT_CPU,(3,3))
wall=time.monotonic()
with (HERE/'support_check.stdout').open('w') as out:
    process=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit)
    handle={'status':'RUNNING_SMALL_SUPPORT_ATTACK','pid':process.pid,'driver_pid':os.getpid(),
            'command':command,'CPU_budget':3,'main_solver_started':False}
    (HERE/'SUPPORT_CHECK_HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
    print(json.dumps(handle),flush=True)
    observation_timeouts=0
    while True:
        try:code=process.wait(timeout=1);break
        except subprocess.TimeoutExpired:observation_timeouts+=1
child=resource.getrusage(resource.RUSAGE_CHILDREN)
solver_cpu=child.ru_utime+child.ru_stime-child0
result={'status':'RAW_UNSAT_COUNTEREXAMPLE_ATTACK_PASS' if code==20 else
        'NEW_PROPER_SUPPORT_FOUND_STOP_ALL30_CUT' if code==10 else 'UNKNOWN_STOP_ALL30_CUT',
        'solver_exit_code':code,'solver_calls':1,'solver_CPU_seconds':solver_cpu,
        'aggregate_CPU_seconds':time.process_time()-start+solver_cpu,
        'wall_seconds':time.monotonic()-wall,'observation_timeouts':observation_timeouts,
        'proof_log':False,'is_independent_complete_proof':False,
        'main_solver_calls':0,'BFS_runs':0,'source_graph_reads':0,'running':False}
if code==10:
    selected=[]
    for line in (HERE/'support_check.sol').read_text().splitlines():
        if line.startswith('v '):
            selected.extend(int(x)-1 for x in line[2:].split() if 1<=int(x)<=30)
    s=set(selected);assert 16<=len(s)<30
    assert all(not({w['vertices'][0],w['vertices'][3]}<=s) or set(w['vertices'][1:3])<=s for w in words)
    assert all(s!=set(r['support']) for r in supports)
    result['new_support']=sorted(s)
for name in ['SUPPORT_CHECK_RESULT.json','SUPPORT_CHECK_HANDLE.json']:
    (HERE/name).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
