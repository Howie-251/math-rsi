#!/usr/bin/env python3
from pathlib import Path
import collections
import itertools
import json
import math
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
assert not (HERE/'run.json').exists(), 'No automatic restart of this fixed trajectory.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();wall=time.monotonic();source=json.loads((HERE.parent/'best.json').read_text());meta=json.loads((HERE.parent/'metadata.json').read_text())
assert source['score']['score_sum']==12 and source['score']['root_misses']==[2,5,3,2]
eu=source['edge_u'];ev=source['edge_v'];seed=source['voltages'];free=meta['free_edge_indices']
assert meta['tree_edge_indices']==[0,6,10] and free==[1,2,3,4,5,7,8,9,11,12,13]
expected={tuple(sorted((43*a+x,43*b+(x+v)%43)))for a,b,v in zip(eu,ev,seed)for x in range(43)}
data=list(map(int,(HERE.parent/'best.edges').read_text().split()));assert data[:2]==[172,602]
saved={tuple(sorted(pair))for pair in zip(data[2::2],data[3::2])};assert expected==saved and len(saved)==602
(HERE/'seed.txt').write_text(' '.join(map(str,seed))+'\n')
(HERE/'seed_edges_check.json').write_text(json.dumps({'source':'../best.edges','voltages':seed,'all_602_edges_equal':True,'new_BFS_runs':0},indent=2)+'\n')
groups=list(zip(eu,ev));sizes=collections.Counter(groups)
def falling(n,k):return math.prod(n-j for j in range(k))
def legal_in_class(n,k):
    available=43-n+k
    return sum((-1)**i*math.comb(k,i)*falling(available-i,k-i)for i in range(k+1))
bytype=collections.Counter();count=0
for triple in itertools.combinations(free,3):
    multiplicities=collections.Counter(groups[e]for e in triple)
    number=math.prod(legal_in_class(sizes[g],k)for g,k in multiplicities.items())
    count+=number;bytype['+'.join(map(str,sorted(multiplicities.values(),reverse=True)))]+=number
assert count==11088102
(HERE/'neighborhood_counts.json').write_text(json.dumps({'raw':12224520,'legal':count,'illegal':12224520-count,'legal_by_coordinate_class_multiplicity':bytype},indent=2)+'\n')
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=300-prep-1;assert remaining>0
run={'status':'RUNNING','running':True,'worker_count':1,'CPU_budget_seconds':300,'preparation_CPU_seconds':prep,'process_CPU_limit_seconds':remaining,'conservative_shutdown_reserve_seconds':1,'fixed_start_count':1,'maximum_rounds':5,'raw_slots_per_complete_round':12224520,'legal_slots_per_complete_round':11088102,'illegal_slots_per_complete_round':1136418}
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (HERE/'search.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT)
    run['pid']=process.pid;(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall)
if code==0:
    terminal=json.loads((HERE/'terminal.json').read_text());run['status']=terminal['status'];run['best_score_sum']=terminal['best_score']['score_sum']
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
