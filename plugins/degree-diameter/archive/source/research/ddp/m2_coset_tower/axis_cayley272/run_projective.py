#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import subprocess

base=Path(__file__).resolve().parent
assert not (base/'production.terminal.json').exists(), 'Do not restart completed finite batch.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
prior=json.loads((base/'capacity_cpu.json').read_text())['process_CPU_seconds']
data=json.loads((base/'QUOTIENT_CAPACITY.json').read_text())
survivors=data['survivors'];assert len(survivors)==158 and data['projective_input_bound']==254852
rows=['158']
for row in survivors:
    rows.append(' '.join(map(str,[row['id'],row['pair_count'],row['involution_count']]+row['pair_phases'])))
(base/'survivor_patterns.txt').write_text('\n'.join(rows)+'\n')
with (base/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','search_projective.cpp','-o','search_projective'],cwd=base,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start
remaining=60-prior-prep-1
assert remaining>0
run={'status':'RUNNING','worker_count':1,'running':True,'scope':254852,'CPU_budget_seconds':60,'earlier_capacity_process_CPU_seconds':prior,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':remaining}
(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
with (base/'production.log').open('w') as log:
    process=subprocess.Popen([str(base/'search_projective'),str(base),str(remaining)],cwd=base,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid
    (base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
    code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=prior+cpu()-start)
if code==0:
    terminal=json.loads((base/'production.terminal.json').read_text())
    run.update(status=terminal['status'],next_cursor=terminal['next_cursor'])
else:
    run['status']='PROCESS_ERROR'
(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
