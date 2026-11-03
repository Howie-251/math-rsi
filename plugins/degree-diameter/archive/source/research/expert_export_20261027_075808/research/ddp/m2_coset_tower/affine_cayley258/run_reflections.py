#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import subprocess

base=Path(__file__).resolve().parent
assert not (base/'production.terminal.json').exists(), 'No restart of completed finite batch.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();prior=sum(json.loads((base/f).read_text())['process_CPU_seconds'] for f in ['capacity_cpu.json','orbit_cpu.json'])
cap=json.loads((base/'CAPACITY_RESULTS.json').read_text());orbit=json.loads((base/'REFLECTION_ORBITS.json').read_text())
assert orbit['affine_orbits']==74 and [r['pair_phases'] for r in cap['survivors']]==[[0,1],[0,2],[1,2]]
with (base/'surviving_patterns.txt').open('w') as stream:
    stream.write('3\n')
    for row in cap['survivors']:stream.write(' '.join(map(str,[row['id']]+row['pair_phases']))+'\n')
with (base/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','search_reflections.cpp','-o','search_reflections'],cwd=base,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=120-prior-prep-1;assert remaining>0
run={'status':'RUNNING','running':True,'worker_count':1,'CPU_budget_seconds':120,'prior_capacity_and_orbit_process_CPU_seconds':prior,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':remaining,'raw_scope':410478,'legal_scope':404114}
(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
with (base/'production.log').open('w') as log:
    process=subprocess.Popen([str(base/'search_reflections'),str(base),str(remaining)],cwd=base,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n');code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=prior+cpu()-start)
if code==0:
    terminal=json.loads((base/'production.terminal.json').read_text());run.update(status=terminal['status'],next_cursor=terminal['next_cursor'])
else:run['status']='PROCESS_ERROR'
(base/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
