#!/usr/bin/env python3
from pathlib import Path
import json
import resource
import subprocess

base=Path(__file__).resolve().parent
assert not (base/'run.json').exists(),'One authorized run only; do not restart.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();source=base.parent/'affine_cayley820_capacity'
best=json.loads((source/'profile.best.json').read_text())['candidate']
top=json.loads((source/'profile.top16.json').read_text());seen=set();seeds=[]
for name,c in [('best',best)]+[(f'top{i}',x) for i,x in enumerate(top)]:
    key=tuple(sorted(c['S']))
    if key in seen:continue
    seen.add(key);seeds.append({'source':name,'expected_root_missing':c['root_deficit'],'S':list(key),'pairs':c['pairs'],'involutions':c['involutions']})
assert len(seeds)==17
(base/'seeds.json').write_text(json.dumps(seeds,indent=2)+'\n')
with (base/'seeds.txt').open('w') as out:
    out.write(f'{len(seeds)}\n')
    for row in seeds:out.write(' '.join(map(str,[row['expected_root_missing']]+row['S']))+'\n')
phases=json.loads((source/'symbolic_survivors.json').read_text());assert len(phases)==2139
with (base/'allowed_phases.txt').open('w') as out:
    out.write(f'{len(phases)}\n')
    for row in phases:out.write(' '.join(map(str,[row['pairs']]+row['pair_phases']))+'\n')
powers=[pow(36,j,41) for j in range(20)]
def inv(g):
    x,j=g%41,g//41
    return (-powers[-j%20]*x)%41+41*(-j%20)
pool={'encoding':'x+41*j','action_root':36,'nonidentity_involutions':[a for a in range(1,820) if inv(a)==a],'noninvolution_inverse_pairs':[[a,inv(a)] for a in range(1,820) if a<inv(a)]}
assert len(pool['nonidentity_involutions'])==41 and len(pool['noninvolution_inverse_pairs'])==389
(base/'group_pools.json').write_text(json.dumps(pool,indent=2)+'\n')
with (base/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=base,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=180-prep-1;assert remaining>0
run={'status':'RUNNING','running':True,'worker_count':1,'CPU_budget_seconds':180,'preparation_CPU_seconds':prep,'production_CPU_limit_seconds':remaining,'conservative_shutdown_reserve_seconds':1,'fixed_seed_scope':17,'random_seeds':0}
(base/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (base/'production.log').open('w') as log:
    process=subprocess.Popen([str(base/'search'),str(base),str(remaining)],cwd=base,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(base/'run.json').write_text(json.dumps(run,indent=2)+'\n');code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start)
if code==0:
    terminal=json.loads((base/'terminal.json').read_text());run.update(status=terminal['status'],actual_full_root_BFS=terminal['actual_full_root_BFS'],best_root_missing=terminal['best_root_missing'])
else:run['status']='PROCESS_ERROR'
(base/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
