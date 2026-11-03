#!/usr/bin/env python3
from collections import Counter,deque
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
assert not (HERE/'run.json').exists(), 'One complete574 batch, no automatic restart.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start,wall=cpu(),time.monotonic();Q,N=43,172
source_file=HERE.parent/'cyclic4_172_balanced/best.json'
source=json.loads(source_file.read_text());U,V,B=source['edge_u'],source['edge_v'],source['voltages']
assert source['n']==172 and source['m']==602 and source['degree']==7 and len(U)==len(V)==len(B)==14
assert all(0<=u<v<4 for u,v in zip(U,V))
assert all(B[e]!=B[f]for e in range(14)for f in range(e)if(U[e],V[e])==(U[f],V[f]))
(HERE/'source.json').write_text(json.dumps(source,indent=2)+'\n')
(HERE/'parameters.txt').write_text('14\n'+'\n'.join(f'{u} {v} {b}'for u,v,b in zip(U,V,B))+'\n')

# Formal candidate0 only: matching0 slope2, not the old flat graph.
calibration_start=cpu();edges=set();edge,slope=0,2
for e,(u,v,b)in enumerate(zip(U,V,B)):
    a=slope if e==edge else 1
    for x in range(Q):edges.add(tuple(sorted((Q*u+x,Q*v+(a*x+b)%Q))))
assert len(edges)==600 and all(u!=v for u,v in edges)
adj=[[]for _ in range(N)]
for u,v in edges:adj[u].append(v);adj[v].append(u)
degree=list(map(len,adj));assert min(degree)==6 and max(degree)==7 and degree.count(6)==4
distances=[];hist=Counter();bad=0;diameter=0
for root in range(N):
    d=[-1]*N;d[root]=0;queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;queue.append(v)
    distances.append(d);hist.update(d);bad+=sum(d[v]<0 or d[v]>3 for v in range(root+1,N))
    if -1 in d:diameter=-1
    elif diameter>=0:diameter=max(diameter,max(d))
(HERE/'first.expected_distances.txt').write_text('\n'.join(' '.join(map(str,d))for d in distances)+'\n')
(HERE/'first.python_check.json').write_text(json.dumps({'scope':'only first formal nonflat candidate, matching0 slope2; ordinary independent all172-root BFS','changed_edge':0,'slope':2,'n':N,'m':len(edges),'min_degree':min(degree),'max_degree':max(degree),'degree_histogram':dict(Counter(degree)),'diameter':diameter,'bad_unordered_pairs':bad,'ordered_distance_histogram':dict(sorted(hist.items())),'roots_checked':N,'source_flat_graph_scored':False,'CPU_seconds':cpu()-calibration_start},indent=2)+'\n')
with (HERE/'compile.log').open('w')as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=60-prep-2;assert remaining>0
metadata={'source_parameters':str(source_file),'source_cached_bad_pairs_for_reference_only':source['score']['bad_unordered_pairs'],'q':Q,'n':N,'max_degree_bound':7,'scope':'change one individual matching slope, preserve every intercept and all other slopes1','matching_indices':list(range(14)),'slope_values':list(range(2,43)),'candidate_count':574,'enumeration_order':'matching index0..13, then slope2..42','no_graph_discarded_for_nonregularity':True,'parallel_edge_duplicates':'merged into one undirected edge','expected_edges_by_class_size':{'3':600,'2':601},'expected_degree_range':[6,7],'scoring':'ordinary complete all172-root BFS for every formal candidate; no C43 symmetry reduction','first_formal_candidate':'independent Python all172-root distances, compared pointwise to C++ formal first evaluation and reused','old_flat_source_rescored':False,'cancelled_246_shared_class_slope_batch':'not executed; different scope','CPU_budget_seconds':60,'worker_count':1,'preparation_CPU_seconds':prep,'process_CPU_limit_seconds':remaining,'shutdown_reserve_seconds':2,'independent_final':'parent-owned, only the unique saved final new graph; regularity not required'}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
def cap():
    bound=math.ceil(remaining)+1;resource.setrlimit(resource.RLIMIT_CPU,(bound,bound))
with (HERE/'search.log').open('w')as log:
    process=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,preexec_fn=cap)
    run={'status':'RUNNING','running':True,'pid':process.pid,'driver_pid':os.getpid(),'worker_count':1,'CPU_budget_seconds':60,'preparation_CPU_seconds':prep,'process_CPU_limit_seconds':remaining}
    (HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run),flush=True);code=process.wait()
run.update(running=False,exit_code=code,total_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,restarts=0)
if code==0:
    terminal=json.loads((HERE/'search.terminal.json').read_text());terminal.update(preparation_CPU_seconds=prep,total_CPU_seconds=run['total_CPU_seconds'],wall_seconds=run['wall_seconds'],CPU_budget_seconds=60,worker_count=1,restarts=0,independent_final='parent-owned; sole saved best pending')
    (HERE/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n');run.update(status=terminal['status'],processed_candidates=terminal['processed_candidates'])
else:run['status']='PROCESS_ERROR'
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');print(json.dumps(run,indent=2),flush=True)
