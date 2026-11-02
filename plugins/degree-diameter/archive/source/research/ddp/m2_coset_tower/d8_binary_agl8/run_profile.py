"""Execute the authorized 2000 HH-coloured samples once, not a production scope."""
from pathlib import Path
import json
import math
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
prep=json.loads((HERE/'prepare.terminal.json').read_text())
preflight=json.loads((HERE/'preflight.terminal.json').read_text())
assert preflight['status']=='SAMPLE_COMPLETE'
assert not (HERE/'profile.terminal.json').exists(), 'Do not repeat this completed profile.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
prior=prep['cpu_seconds']+preflight['cpu_seconds']
remaining=60-prior-1
def cap():
    hard=max(1,math.ceil(remaining));resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
args=[str(HERE/'profile'),'profile',str(remaining),str(HERE)]
wall=time.monotonic()
with (HERE/'profile.log').open('w') as output:
    result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
elapsed=time.monotonic()-wall
assert result.returncode==0
terminal=json.loads((HERE/'profile.terminal.json').read_text())
total=prior+cpu()-start
summary={'status':terminal['status'],'worker_count':1,'CPU_limit_seconds':60,
 'prepare_and_compile_CPU_seconds':prep['cpu_seconds'],
 'preflight_CPU_seconds':preflight['cpu_seconds'],
 'profile_and_driver_CPU_seconds':cpu()-start,'cumulative_CPU_seconds':total,
 'profile_wall_seconds':elapsed,'profile_command':args,'profile':terminal,
 'independent_preflight':'parent-owned; pending','full_production_started':False}
(HERE/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
metadata={'scope':'Exactly 2000 deterministic HH-coloured tuples, no symmetry reductions or complete-family claim.',
 'component_order':['allones invol','plane4 invol','weight6 invol','weight2 inverse pair','nonplane4 inverse pair'],
 'component_list_order':'generator_lists.json: increasing involution code, increasing minimum inverse-pair code',
 'indices_at_cursor_j':['j mod8','(13j+7) mod56','(23j+19) mod56','(17j+31) mod756','(37j+5) mod1540'],
 'cursor_range':[0,2000],'all_2000_generator_sets_distinct':True,
 'only_patterns_tested':'two inverse pairs and three involutions, with the named fixed colour allocation',
 'all_candidates_legal_and_HH_verified_before_BFS':True,
 'scoring':'actual graph construction followed by three exact depth-five BFS roots, one per proven left-G orbit',
 'roots':[0,7168,8192],'root_weights':[7168,1024,128],
 'bad_pair_formula':'(7168*miss_leaf+1024*miss_block+128*miss_head)/2',
 'BB_optimization_used':False,'normal_H_formula_used':False,
 'full_production_started':False,'next_cursor':terminal['next_cursor']}
(HERE/'profile_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps(summary,indent=2))
