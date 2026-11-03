"""Compile the new group implementation and save the two authorized preflight graphs."""
import json
import math
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();runs=[];limit=60.0
def run(args,log):
    remaining=max(1,math.ceil(limit-(cpu()-start)))
    def cap(): resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining))
    before=cpu();wall=time.monotonic()
    with (HERE/log).open('w') as output:
        result=subprocess.run(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
    runs.append({'command':list(map(str,args)),'log':log,'returncode':result.returncode,
                 'cpu_seconds':cpu()-before,'wall_seconds':time.monotonic()-wall})
    if result.returncode: raise RuntimeError(f'{log}: exit {result.returncode}')
run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],'compile.log')
samples=[[(1,1,0),(2,0,1),(3,3,1)],[(1,7,1),(0,1,0),(2,5,1)]]
completed=[];found=False
for j,sample in enumerate(samples):
    ids=[x+64*(a+21*e) for x,a,e in sample]
    run([str(HERE/'search'),'check',*map(str,ids),str(HERE/f'preflight_{j}')],f'preflight_{j}.log')
    data=json.loads((HERE/f'preflight_{j}.json').read_text())
    completed.append({'sample_index':j,'inverse_pair_representatives':sample,
                      'parameters_file':f'preflight_{j}.json','edges_file':f'preflight_{j}.edges',
                      'three_root_bad_pairs':data['bad_unordered_pairs']})
    if data['bad_unordered_pairs']==0:
        found=True
        break
result={'status':'PREFLIGHT_D5_CANDIDATE' if found else 'PREFLIGHT_GRAPHS_READY_FOR_INDEPENDENT_CHECK',
        'cumulative_cpu_seconds':cpu()-start,'cumulative_cpu_limit_seconds':limit,
        'worker_count':1,'runs':runs,'samples':completed,'profile_started':False}
(HERE/'prepare.terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
