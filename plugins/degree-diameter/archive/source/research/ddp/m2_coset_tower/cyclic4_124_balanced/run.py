#!/usr/bin/env python3
from collections import Counter, deque
from pathlib import Path
import json
import math
import os
import random
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
assert not (HERE/'run.json').exists(), 'One authorized run; no automatic restart.'
Q,N,E,D=31,124,12,6
U=[0,0,0,0,0,0,1,1,1,1,2,2]
V=[1,1,2,2,3,3,2,2,3,3,3,3]
TREE=[0,2,4];FREE=[e for e in range(E)if e not in TREE]
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
begin,wall=cpu(),time.monotonic()
degree=[0]*4
for a,b in zip(U,V):degree[a]+=1;degree[b]+=1
assert degree==[D]*4 and len(FREE)==9
topology={'q':Q,'n':N,'degree':D,'edge_u':U,'edge_v':V,'tree_edge_indices':TREE,'free_edge_indices':FREE,'K4_pair_multiplicity':2,'symbolic_capacity_from_completed_math_task':[[55,44,44,44],[44,55,44,44],[44,44,55,44],[44,44,44,55]],'capacity_recomputed_in_this_search':False,'source':'parent authorized d6 q31 double matching topology after complete47 base capacity task'}
(HERE/'topology.json').write_text(json.dumps(topology,indent=2)+'\n')
(HERE/'topology.txt').write_text('12 3\n'+'\n'.join(f'{a} {b}'for a,b in zip(U,V))+'\n'+' '.join(map(str,TREE))+'\n')
def legal(state):
    return all(0<=v<Q for v in state) and all(state[e]==0 for e in TREE) and all(state[e]!=state[f]for e in range(E)for f in range(e)if(U[e],V[e])==(U[f],V[f]))
start_seed,kick_seed=20261026460,20261026461
rng=random.Random(start_seed);starts=[]
while len(starts)<64:
    state=[0]*E;assigned=set(TREE)
    for e in FREE:
        unavailable={state[f]for f in assigned if(U[e],V[e])==(U[f],V[f])}
        state[e]=rng.choice([x for x in range(Q)if x not in unavailable]);assigned.add(e)
    assert legal(state)
    if state not in starts:starts.append(state)
(HERE/'starts.json').write_text(json.dumps({'fixed_random_count':64,'start_rng':'Python random.Random MT19937','start_seed':start_seed,'kick_rng':'C++ mt19937_64','kick_seed':kick_seed,'old172_seed_used':False,'states':starts},indent=2)+'\n')
(HERE/'starts.txt').write_text('64\n'+'\n'.join(' '.join(map(str,s))for s in starts)+'\n')

# One independent construction and four complete BFS for the first formal start.
calibration_start=cpu();edges=set()
for a,b,v in zip(U,V,starts[0]):
    for x in range(Q):edges.add(tuple(sorted((Q*a+x,Q*b+(x+v)%Q))))
assert len(edges)==372 and all(a!=b for a,b in edges)
adj=[[]for _ in range(N)]
for a,b in edges:adj[a].append(b);adj[b].append(a)
assert all(len(row)==D and len(set(row))==D for row in adj)
distances=[];histograms=[];misses=[]
for root in (0,31,62,93):
    dist=[-1]*N;dist[root]=0;queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
    distances.append(dist);histograms.append(dict(sorted(Counter(dist).items())));misses.append(sum(d<0 or d>3 for d in dist))
assert Q*sum(misses)%2==0
(HERE/'first.expected_distances.txt').write_text('\n'.join(' '.join(map(str,d))for d in distances)+'\n')
(HERE/'first.expected_adjacency.txt').write_text('\n'.join(' '.join(map(str,sorted(row)))for row in adj)+'\n')
(HERE/'first.python_check.json').write_text(json.dumps({'scope':'only first formal random start; independent Python edge set and4 complete roots; no all-source test','voltages':starts[0],'n':N,'m':len(edges),'degree':D,'root_misses':misses,'root_distance_histograms':histograms,'bad_unordered_pairs':Q*sum(misses)//2,'connected':all(-1 not in d for d in distances),'CPU_seconds':cpu()-calibration_start},indent=2)+'\n')
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-begin;source_prep=json.loads((HERE/'preparation.json').read_text())['CPU_seconds']
remaining=120-prep-source_prep-2;assert remaining>0
metadata={'mechanism':'C31 lift of K4 with two matchings on every pair','q':Q,'n':N,'degree':D,'target_diameter':3,'edge_u':U,'edge_v':V,'tree_edge_indices':TREE,'free_edge_indices':FREE,'free_voltage_dimension':9,'common_scalar_quotient_used':False,'fixed_random_starts':64,'start_seed':start_seed,'kick_seed':kick_seed,'old172_seed_used':False,'segments_per_start_maximum':9,'strict_full_coordinate_moves_per_segment_maximum':30,'neighbor_choice':'best strict improvement over complete legal single-coordinate neighborhood; two-coordinate legal kick between segments','legality':'different voltages on two edges of each fixed pair; tree3 fixed0','BFS_roots_per_legal_evaluation':4,'root_labels':[0,31,62,93],'score':'sum of four radius3 deficits; bad unordered pairs=31*sum/2','first_formal_start':'independent Python full edges and4distance rows; compare each adjacency/distance entry with C++ first evaluation and reuse','family_exhausted':False,'CPU_budget_seconds':120,'worker_count':1,'preparation_CPU_seconds':prep,'source_preparation_CPU_seconds':source_prep,'production_CPU_limit_seconds':remaining,'shutdown_reserve_seconds':2,'independent_final':'parent-owned, sole saved final best all124 roots'}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
def cap():
    ceiling=math.ceil(remaining)+1;resource.setrlimit(resource.RLIMIT_CPU,(ceiling,ceiling))
with (HERE/'search.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,preexec_fn=cap)
    run={'status':'RUNNING','running':True,'pid':process.pid,'driver_pid':os.getpid(),'worker_count':1,'preparation_CPU_seconds':prep,'source_preparation_CPU_seconds':source_prep,'process_CPU_limit_seconds':remaining,'CPU_budget_seconds':120}
    (HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run),flush=True);code=process.wait()
total=cpu()-begin+source_prep
run.update(running=False,exit_code=code,total_CPU_seconds=total,restarts=0)
if code==0:
    t=json.loads((HERE/'search.terminal.json').read_text());t.update(preparation_CPU_seconds=prep,source_preparation_CPU_seconds=source_prep,total_CPU_seconds=total,wall_seconds=time.monotonic()-wall,CPU_budget_seconds=120,worker_count=1,restarts=0,independent_final='parent-owned; sole saved best pending')
    (HERE/'terminal.json').write_text(json.dumps(t,indent=2)+'\n');run.update(status=t['status'],evaluations=t['legal_states_evaluated'])
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run,indent=2),flush=True)
