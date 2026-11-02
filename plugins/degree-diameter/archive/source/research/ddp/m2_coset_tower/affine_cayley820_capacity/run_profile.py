#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import subprocess

base=Path(__file__).resolve().parent
assert not (base/'profile.terminal.json').exists(), 'Do not restart this fixed profile.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();rows=json.loads((base/'symbolic_survivors.json').read_text());assert len(rows)==2139
with (base/'profile.patterns.txt').open('w') as stream:
    stream.write('2139\n')
    for row in rows:stream.write(' '.join(map(str,[row['id'],row['pairs'],row['involutions'],row['anchor_slot']]+row['pair_phases']))+'\n')
with (base/'profile.compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','profile.cpp','-o','profile'],cwd=base,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=120-prep-1;assert remaining>0
run={'status':'RUNNING','running':True,'worker_count':1,'CPU_budget_seconds':120,'preparation_CPU_seconds':prep,'production_limit_CPU_seconds':remaining,'fixed_seed':2026102622,'stage1_graph_scope':34224,'stage2_seed_scope':16,'prior_capacity_task_CPU_accounted_separately':True}
(base/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
with (base/'profile.log').open('w') as log:
    process=subprocess.Popen([str(base/'profile'),str(base),str(remaining)],cwd=base,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(base/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n');code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start)
if code==0:
    terminal=json.loads((base/'profile.terminal.json').read_text());run.update(status=terminal['status'],profile_actual_graphs=terminal['profile_actual_graphs'],descent_actual_neighbor_graphs=terminal['descent_actual_neighbor_graphs'])
else:run['status']='PROCESS_ERROR'
(base/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
