"""Run the one authorized 120 CPU second diamond profile, then check its graph."""
from collections import deque
from pathlib import Path
import json, os, resource, subprocess, time

HERE=Path(__file__).resolve().parent
cpu=min(os.sched_getaffinity(0))
prefix=HERE/'control_diamond_n31'
command=[str(HERE/'control_diamond31'),'120','20261026',str(prefix)]
(HERE/'run.json').write_text(json.dumps(dict(command=command,cpu_affinity=[cpu],
    cpu_hard_limit_seconds=120,internal_stop_cpu_seconds=119.8,seed=20261026,profiles=1,
    schedule='up to ten 12-CPU-second initialization segments within one fixed profile',
    scope='32 fixed internal edges; 30 cross-block edges; no within-block additions'),indent=2)+'\n')

def limits():
    os.sched_setaffinity(0,{cpu})
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))

before=resource.getrusage(resource.RUSAGE_CHILDREN);started=time.monotonic()
with (HERE/'profile.log').open('w') as log:
    result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
assert result.returncode==0
metadata=json.loads(prefix.with_suffix('.json').read_text())
rows=[tuple(map(int,line.split())) for line in prefix.with_suffix('.edges').read_text().splitlines()]
assert rows[0]==(31,62)
n=31;edges={tuple(sorted(e)) for e in rows[1:]}
assert len(edges)==62 and all(u!=v for u,v in edges)
fixed={(0,1),(0,2),(0,3),(1,2),(1,3)}
block=[0]*4+[k for k in range(1,10) for _ in range(3)]
for a in range(4,31,3):fixed.update({(a,a+1),(a,a+2),(a+1,a+2)})
assert len(fixed)==32 and fixed<=edges
external=edges-fixed
assert len(external)==30 and all(block[u]!=block[v] for u,v in external)
A=[[0]*n for _ in range(n)]
for u,v in edges:A[u][v]=A[v][u]=1
assert all(sum(row)==4 for row in A)
A2=[[sum(A[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
A3=[[sum(A2[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
zeros=[[i,j] for i in range(n) for j in range(n) if not A3[i][j]]
assert len(zeros)==metadata['zero_entries_A3']
adj=[[j for j in range(n) if A[i][j]] for i in range(n)]
profiles=[];distances=[]
for root in range(n):
    distance=[-1]*n;distance[root]=0;queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if distance[v]<0:distance[v]=distance[u]+1;queue.append(v)
    assert -1 not in distance
    distances.append(distance)
    profiles.append(dict(root=root,eccentricity=max(distance),
                         layer_sizes=[distance.count(d) for d in range(max(distance)+1)]))
triangles=[[i,j,k] for i in range(n) for j in range(i+1,n) for k in range(j+1,n)
           if A[i][j] and A[j][k] and A[k][i]]
terminal=dict(status=metadata['status'],profiles_run=1,returncode=result.returncode,
    wall_seconds=time.monotonic()-started,
    child_cpu_seconds=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime),
    control_order=n,control_size=62,control_degree=4,simple=True,
    fixed_internal_edges=32,cross_block_edges=30,
    A3_zero_count=len(zeros),A3_zero_pairs=zeros,A3_zero_diagonal=[i for i in range(n) if not A3[i][i]],
    diameter=max(row['eccentricity'] for row in profiles),all_root_BFS=profiles,
    triangles=triangles,necessary_condition_passed=not zeros,
    unordered_zero_pair_details=[dict(pair=[u,v],distance=distances[u][v],
        two_walk_count=A2[u][v],common_neighbors=sorted(set(adj[u])&set(adj[v])))
        for u,v in zeros if u<v],
    proposed_lift_order=837,actual_lift_constructed=False,
    limitation='One bounded heuristic profile. Failure does not exclude this topology or general controllers.')
(HERE/'validation.json').write_text(json.dumps(terminal,indent=2)+'\n')
(HERE/'A3.json').write_text(json.dumps(A3)+'\n')
print(json.dumps({k:v for k,v in terminal.items() if k not in ('all_root_BFS','triangles')},indent=2))
