#!/usr/bin/env python3
"""Single authorized finite run; compile/calibration/search CPU share 60 seconds."""
import json
from pathlib import Path
import resource
import subprocess
import time

base=Path(__file__).resolve().parent
assert not (base/'production.terminal.json').exists(), 'Do not restart completed finite batch.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF)
    b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
data=json.loads((base/'QUOTIENT_WORD_CAPACITY.json').read_text())
survivors=data['survivors']
assert len(survivors)==135
rows=['135']
for row in survivors:
    phase=row['pair_phase_classes']
    assert len(phase)==len(set(phase))==4 and 0 not in phase
    assert any(z%10 for z in phase)
    rows.append(' '.join(map(str,[row['id']]+phase)))
(base/'survivor_patterns.txt').write_text('\n'.join(rows)+'\n')
with (base/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','search_projective.cpp','-o','search_projective'],cwd=base,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start
remaining=60-prep-1
assert remaining>0
run={'status':'RUNNING','worker_count':1,'running':True,'scope':17955,'CPU_budget_seconds':60,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':remaining}
(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
with (base/'production.log').open('w') as log:
    process=subprocess.Popen([str(base/'search_projective'),str(base),str(remaining)],cwd=base,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid
    (base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
    code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start)
if code==0:
    terminal=json.loads((base/'production.terminal.json').read_text())
    run.update(status=terminal['status'],next_cursor=terminal['next_cursor'])
else:
    run['status']='PROCESS_ERROR'
(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
