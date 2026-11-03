"""Score the authorized five head-triangle allocations; no production continuation."""
from pathlib import Path
import json
import math
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
prep=json.loads((HERE/'prepare.terminal.json').read_text())
pre=json.loads((HERE/'preflight.terminal.json').read_text())
assert pre['status']=='SAMPLE_COMPLETE'
assert not (HERE/'profile.terminal.json').exists(), 'Do not repeat a completed profile.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();prior=prep['cpu_seconds']+pre['cpu_seconds'];remaining=60-prior-1
def cap():
    n=max(1,math.ceil(remaining));resource.setrlimit(resource.RLIMIT_CPU,(n,n))
args=[str(HERE/'profile'),'profile',str(remaining),str(HERE)];wall=time.monotonic()
with (HERE/'profile.log').open('w') as f:
    proc=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT,preexec_fn=cap)
elapsed=time.monotonic()-wall
assert proc.returncode==0
t=json.loads((HERE/'profile.terminal.json').read_text())
rows=[json.loads(s) for s in (HERE/'profile.results.jsonl').read_text().splitlines()]
assert len(rows)==t['raw']
meta=json.loads((HERE/'profile_metadata.json').read_text());branches=[]
metrics={'LL':(0,0),'LB':(0,1),'LH':(0,2),'BL':(1,0),'BB':(1,1),'BH':(1,2),'HL':(2,0),'HB':(2,1),'HH':(2,2)}
for branch in meta['branches']:
    rr=[z for z in rows if z['branch']==branch['branch']]
    if not rr:continue
    out=dict(branch);out['actual']=len(rr)
    out['root_minimum_missing']=[min(z['root_missing'][i] for z in rr) for i in range(3)]
    out['root_zero_counts']=[sum(z['root_missing'][i]==0 for z in rr) for i in range(3)]
    out['layer_minimum_missing']={name:min(z['root_missing_by_target_layer'][i][j] for z in rr) for name,(i,j) in metrics.items()}
    out['layer_zero_counts']={name:sum(z['root_missing_by_target_layer'][i][j]==0 for z in rr) for name,(i,j) in metrics.items()}
    out['head_and_block_zero']=sum(z['root_missing'][1]==0 and z['root_missing'][2]==0 for z in rr)
    best=min(rr,key=lambda z:z['bad_unordered_pairs']);out['best']=best
    branches.append(out)
(HERE/'profile.branch_summary.json').write_text(json.dumps(branches,indent=2)+'\n')
summary={'status':t['status'],'worker_count':1,'CPU_limit_seconds':60,
 'prepare_compile_CPU_seconds':prep['cpu_seconds'],'preflight_CPU_seconds':pre['cpu_seconds'],
 'profile_driver_CPU_seconds':cpu()-start,'cumulative_CPU_seconds':prior+cpu()-start,
 'profile_wall_seconds':elapsed,'profile_command':args,'profile':t,
 'branch_summary':'profile.branch_summary.json','independent_preflight':'parent-owned; pending',
 'full_production_started':False,'no_extra_BFS_for_cursor_zero':True}
(HERE/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
for b in branches:print('branch',b['branch'],'min',b['root_minimum_missing'],'BBmin',b['layer_minimum_missing']['BB'],'BBzero',b['layer_zero_counts']['BB'],'best',b['best']['bad_unordered_pairs'])
