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
assert not (HERE/'run.json').exists(), 'No automatic restart.'
assert (HERE/'topology.json').exists() and (HERE/'seed.json').exists(), 'Await the parent-selected single topology and source surgery seed.'
Q,N,E,D=43,172,14,7
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
begin,wall=cpu(),time.monotonic()
topology=json.loads((HERE/'topology.json').read_text())
seed=json.loads((HERE/'seed.json').read_text())
U,V,TREE=topology['edge_u'],topology['edge_v'],topology['tree_edge_indices']
assert len(U)==len(V)==E and len(TREE)==len(set(TREE))==3
assert all(0<=a<=b<4 for a,b in zip(U,V))
assert all(0<=e<E and U[e]!=V[e] for e in TREE)
FREE=[e for e in range(E)if e not in TREE]
degree=[0]*4
for a,b in zip(U,V):degree[a]+=1;degree[b]+=1
assert degree==[D]*4 and len(FREE)==11
tree_adj=[[]for _ in range(4)]
for e in TREE:tree_adj[U[e]].append((V[e],e,1));tree_adj[V[e]].append((U[e],e,-1))
seen={0};queue=deque([0])
while queue:
    for v,_,_ in tree_adj[queue.popleft()]:
        if v not in seen:seen.add(v);queue.append(v)
assert len(seen)==4
if 'edge_u'in seed:assert seed['edge_u']==U and seed['edge_v']==V
raw_seed=seed['voltages']
assert len(raw_seed)==E and all(isinstance(x,int) and 0<=x<Q for x in raw_seed)
# Gauge the one chosen source seed to the selected nonloop tree, with c0=0.
potential=[None]*4;potential[0]=0;queue=deque([0])
while queue:
    u=queue.popleft()
    for v,e,sign in tree_adj[u]:
        if potential[v]is None:potential[v]=(potential[u]-sign*raw_seed[e])%Q;queue.append(v)
seed_state=[(raw_seed[e]+potential[V[e]]-potential[U[e]])%Q for e in range(E)]
def legal(state):
    if len(state)!=E or any(not 0<=v<Q for v in state)or any(state[e]!=0 for e in TREE):return False
    for e in range(E):
        if U[e]==V[e] and state[e]==0:return False
        for f in range(e):
            if (U[e],V[e])==(U[f],V[f]):
                if state[e]==state[f]:return False
                if U[e]==V[e] and (state[e]+state[f])%Q==0:return False
    return True
assert legal(seed_state)
(HERE/'seed_gauge.json').write_text(json.dumps({'raw_voltages':raw_seed,'vertex_relabel_offsets':potential,'normalized_voltages':seed_state,'tree_edge_indices':TREE,'source_seed_legal':True},indent=2)+'\n')
(HERE/'topology.txt').write_text('14 3\n'+'\n'.join(f'{a} {b}'for a,b in zip(U,V))+'\n'+' '.join(map(str,TREE))+'\n')
start_seed,kick_seed=20261026440,20261026441
rng=random.Random(start_seed);starts=[seed_state]
while len(starts)<17:
    state=[0]*E;assigned=set(TREE)
    for e in FREE:
        unavailable={0}if U[e]==V[e]else set()
        for f in assigned:
            if (U[e],V[e])==(U[f],V[f]):
                unavailable.add(state[f])
                if U[e]==V[e]:unavailable.add((-state[f])%Q)
        state[e]=rng.choice([x for x in range(Q)if x not in unavailable]);assigned.add(e)
    assert legal(state)
    if state not in starts:starts.append(state)
(HERE/'starts.json').write_text(json.dumps({'source_seed_count':1,'fixed_random_count':16,'start_rng':'Python random.Random MT19937','start_seed':start_seed,'kick_rng':'C++ mt19937_64','kick_seed':kick_seed,'states':starts},indent=2)+'\n')
(HERE/'starts.txt').write_text('17\n'+'\n'.join(' '.join(map(str,s))for s in starts)+'\n')

# The first formal source seed is the sole independent preflight; no all-source BFS.
calibration_start=cpu();edges=set()
for a,b,v in zip(U,V,starts[0]):
    for x in range(Q):edges.add(tuple(sorted((Q*a+x,Q*b+(x+v)%Q))))
assert len(edges)==602 and all(a!=b for a,b in edges)
source_edges_file=(HERE/seed['source_edges_file']).resolve()
with source_edges_file.open()as handle:
    assert list(map(int,handle.readline().split()))==[N,602]
    old_edges={tuple(sorted(map(int,line.split())))for line in handle if line.strip()}
assert len(old_edges)==602
permutation=[Q*(v//Q)+(v%Q+potential[v//Q])%Q for v in range(N)]
assert len(set(permutation))==N
mapped_edges={tuple(sorted((permutation[a],permutation[b])))for a,b in old_edges}
assert mapped_edges==edges
(HERE/'source_relabel_check.json').write_text(json.dumps({'source_edges_file':str(source_edges_file),'source_independent_audit':seed.get('source_independent_audit'),'root_supplied_c':[(-c)%Q for c in potential],'mapping':'old (orbit,x) -> normalized (orbit,x-c_orbit); c=-potential modulo43','vertex_relabel_offsets':potential,'old_to_normalized_vertex_permutation':permutation,'all602_edges_match_after_relabel':True,'source_original_voltages':raw_seed,'normalized_voltages':seed_state,'additional_all_source_BFS':0},indent=2)+'\n')
adj=[[]for _ in range(N)]
for a,b in edges:adj[a].append(b);adj[b].append(a)
assert all(len(row)==D and len(set(row))==D for row in adj)
distances=[];histograms=[];misses=[]
for root in (0,43,86,129):
    dist=[-1]*N;dist[root]=0;queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
    distances.append(dist);histograms.append(dict(sorted(Counter(dist).items())));misses.append(sum(d<0 or d>3 for d in dist))
assert Q*sum(misses)%2==0
(HERE/'first.expected_distances.txt').write_text('\n'.join(' '.join(map(str,d))for d in distances)+'\n')
(HERE/'first.expected_adjacency.txt').write_text('\n'.join(' '.join(map(str,sorted(row)))for row in adj)+'\n')
(HERE/'first.python_check.json').write_text(json.dumps({'scope':'only first formal source surgery seed; independent Python full edge set and4 complete roots; no all-source test','voltages':starts[0],'n':N,'m':len(edges),'degree':D,'root_misses':misses,'root_distance_histograms':histograms,'bad_unordered_pairs':Q*sum(misses)//2,'connected':all(-1 not in d for d in distances),'CPU_seconds':cpu()-calibration_start},indent=2)+'\n')
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
preparation=cpu()-begin
source_prep=json.loads((HERE/'preparation.json').read_text())['CPU_seconds']
remaining=180-preparation-source_prep-2
assert remaining>0
metadata={'mechanism':'one selected 7regular four-node pseudograph lifted by C43, loops allowed','topology_source':topology,'n':N,'degree':D,'target_diameter':3,'edge_u':U,'edge_v':V,'tree_edge_indices':TREE,'free_edge_indices':FREE,'free_voltage_dimension':11,'common_scalar_or_loop_sign_quotient_used':False,'source_seed_count':1,'fixed_random_start_count':16,'total_start_count':17,'start_seed':start_seed,'kick_seed':kick_seed,'segments_per_start_maximum':9,'strict_full_coordinate_moves_per_segment_maximum':30,'legality':'loop v nonzero; loops on same vertex distinct up to sign; parallel cross edges have distinct voltages;3 nonloop tree voltages0','neighbor_choice':'best strict improvement over every legal single-coordinate value; legal2-coordinate kick between segments','BFS_roots_per_legal_evaluation':4,'root_labels':[0,43,86,129],'score':'sum of four radius3 deficits; exact bad unordered pairs=43*sum/2','first_formal_seed':'Python full edge set and4distance arrays; compare all adjacency rows and distance arrays with C++ first evaluation, then reuse evaluation','family_exhausted':False,'CPU_budget_seconds':180,'worker_count':1,'preparation_CPU_seconds':preparation,'source_preparation_CPU_seconds':source_prep,'production_CPU_limit_seconds':remaining,'shutdown_reserve_seconds':2,'independent_final':'parent-owned; one sole final best all172-root check'}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
def cap():
    ceiling=math.ceil(remaining)+1;resource.setrlimit(resource.RLIMIT_CPU,(ceiling,ceiling))
with (HERE/'search.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,preexec_fn=cap)
    run={'status':'RUNNING','running':True,'pid':process.pid,'driver_pid':os.getpid(),'worker_count':1,'preparation_CPU_seconds':preparation,'source_preparation_CPU_seconds':source_prep,'process_CPU_limit_seconds':remaining,'CPU_budget_seconds':180}
    (HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run),flush=True);code=process.wait()
total=cpu()-begin+source_prep
run.update(running=False,exit_code=code,total_CPU_seconds=total,restarts=0)
if code==0:
    terminal=json.loads((HERE/'search.terminal.json').read_text())
    terminal.update(preparation_CPU_seconds=preparation,source_preparation_CPU_seconds=source_prep,total_CPU_seconds=total,wall_seconds=time.monotonic()-wall,CPU_budget_seconds=180,worker_count=1,restarts=0,independent_final='parent-owned; pending sole final saved best')
    (HERE/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
    run.update(status=terminal['status'],evaluations=terminal['legal_states_evaluated'])
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run,indent=2),flush=True)
