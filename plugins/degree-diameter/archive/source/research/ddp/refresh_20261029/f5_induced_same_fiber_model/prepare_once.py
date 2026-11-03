#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import math
import os
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent/'f5_induced_shared_routes_model'
parser=argparse.ArgumentParser()
parser.add_argument('--prepare-only',action='store_true',required=True)
parser.parse_args()
assert not (HERE/'PREPARE_HANDLE.json').exists(), 'Once-only preparation has already started.'
assert sys.byteorder=='little'
start=time.process_time();child0=resource.getrusage(resource.RUSAGE_CHILDREN)
child0=child0.ru_utime+child0.ru_stime
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-child0
def save(name,value):(HERE/name).write_text(json.dumps(value,indent=2)+'\n')
def limit(seconds):
    def apply():resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    return apply
save('PREPARE_HANDLE.json',{'status':'PREPARING_ONLY','pid':os.getpid(),'CPU_budget':15,'solver_calls':0})
model=json.loads((PARENT/'MODEL.json').read_text())
assert (model['variables'],model['clauses'])==(315221,1290903)
flags=json.loads((PARENT/'RESTORED_OR_FLAGS.json').read_text())
flags=[f for f in flags if len(f['old_ids'])==5]
assert len(flags)==3000
with (HERE/'OR5_FLAGS.tsv').open('w') as out:
    for f in flags:out.write(str(f['flag'])+' '+' '.join(map(str,f['old_ids']))+'\n')
compile_command=['g++','-O3','-std=c++17',str(HERE/'prepare_native.cpp'),'-o',str(HERE/'prepare_native')]
compiled=subprocess.run(compile_command,capture_output=True,text=True,preexec_fn=limit(12))
(HERE/'compile.log').write_text(compiled.stdout+compiled.stderr)
if compiled.returncode!=0:
    save('TERMINAL.json',{'status':'COMPILE_FAILED_OR_BUDGET_STOP','code':compiled.returncode,'aggregate_CPU_seconds':cpu(),'solver_calls':0})
    raise SystemExit(2)
compile_and_prep_cpu=cpu()
remaining=math.floor(15-cpu()-0.5)
if remaining<1:
    save('TERMINAL.json',{'status':'PREPARE_CPU_BUDGET_STOP','aggregate_CPU_seconds':cpu(),'solver_calls':0})
    raise SystemExit(3)
command=[str(HERE/'prepare_native'),str(HERE.parent/'f5_induced_hyperplane3000/source_adjacency.u16.bin'),
         str(HERE/'OR5_FLAGS.tsv'),str(HERE),str(max(0.1,remaining-0.2))]
with (HERE/'native.log').open('w') as out:
    proc=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit(remaining))
    handle={'status':'ENUMERATING_LITERAL_SAME_FIBER_ROUTES','driver_pid':os.getpid(),'pid':proc.pid,
        'command':command,'compile_and_prep_CPU_seconds':compile_and_prep_cpu,
        'native_CPU_limit':remaining,'solver_calls':0}
    save('PREPARE_HANDLE.json',handle);print(json.dumps(handle),flush=True)
    code=proc.wait()
native=json.loads((HERE/'NATIVE_RESULT.json').read_text()) if (HERE/'NATIVE_RESULT.json').exists() else {'status':'NATIVE_TERMINATED'}
if code!=0 or native['status']!='COMPLETE_SAME_FIBER_ROUTE_CLAUSES':
    result=dict(native,returncode=code,aggregate_CPU_seconds=cpu(),solver_calls=0,running=False)
    save('TERMINAL.json',result);save('PREPARE_HANDLE.json',result)
    print(json.dumps(result),flush=True);raise SystemExit(code or 2)
assert native['additional_clauses']==930000 and native['additional_variables']==0
temporary=HERE/'model.cnf.preparing'
try:
    with temporary.open('w') as out,(PARENT/'model.cnf').open() as base:
        assert base.readline().split()==['p','cnf','315221','1290903']
        out.write('p cnf 315221 2220903\n')
        for filename,opened in [(PARENT/'model.cnf',base),(HERE/'same_fiber.added.cnf',None)]:
            inp=opened if opened is not None else filename.open()
            try:
                while True:
                    if cpu()>=14.8:raise TimeoutError('Preparation CPU budget while copying model')
                    chunk=inp.read(1024*1024)
                    if not chunk:break
                    out.write(chunk)
            finally:
                if opened is None:inp.close()
    temporary.rename(HERE/'model.cnf')
except TimeoutError as exc:
    result={'status':'COPY_CPU_BUDGET_STOP','error':str(exc),'native_complete':True,'aggregate_CPU_seconds':cpu(),'solver_calls':0,'running':False}
    save('TERMINAL.json',result);save('PREPARE_HANDLE.json',result)
    print(json.dumps(result),flush=True);raise SystemExit(3)
result=dict(native,status='PREPARED_NOT_SOLVED',variables=315221,clauses=2220903,
            parent_variables=315221,parent_clauses=1290903,parent_body_rebuilt=False,
            parent_CNF=str(PARENT/'model.cnf'),keep_variables=3750,n_at_least=1921,max_degree=16,
            full_same_fiber_distance_constraints=True,full_all_pair_D3_constraints=False,
            compile_and_prep_CPU_seconds=compile_and_prep_cpu,aggregate_CPU_seconds=cpu(),
            CPU_budget=15,solver_calls=0,new_graphs=0,runner_written=False,running=False,
            pending=['root mathematical scope and any future main budget decision'])
for name in ['MODEL.json','TERMINAL.json','PREPARE_HANDLE.json']:save(name,result)
print(json.dumps(result),flush=True)
