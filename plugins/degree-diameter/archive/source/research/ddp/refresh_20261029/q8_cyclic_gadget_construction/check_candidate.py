#!/usr/bin/env python3
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
HERE=Path(__file__).resolve().parent
START=time.process_time()
pi=[l^(3 if l.bit_count()%2==0 else 5) for l in range(8)]
delta=[1,3,2,6,2,6,1,3]
sigma=[8*((a+delta[l])%8)+pi[l] for a in range(8) for l in range(8)]
assert sorted(sigma)==list(range(64))
inverse=[0]*64
for u,v in enumerate(sigma):inverse[v]=u
assert all(sigma[u]!=u and sigma[sigma[u]]!=u for u in range(64))
G=[{u^1,u^2,u^4,sigma[u],inverse[u]} for u in range(64)]
assert all(len(row)==5 and u not in row for u,row in enumerate(G))
assert all(u in G[v] for u,row in enumerate(G) for v in row)
rows=[]
for root in range(64):
    distance=[-1]*64;distance[root]=0;queue=[root]
    for u in queue:
        if distance[u]==3:continue
        for v in G[u]:
            if distance[v]<0:distance[v]=distance[u]+1;queue.append(v)
    phase_sets={str(l):[a for a in range(8) if distance[8*a+l]>=0] for l in range(8)}
    rows.append(dict(root=root,reached=len(queue),missing=[u for u,d in enumerate(distance) if d<0],phase_sets=phase_sets))
hit=all(row['reached']==64 for row in rows)
out=dict(status='K64_D3_HIT' if hit else 'SINGLE_ANALYTIC_VOLTAGE_CANDIDATE_REFUTED',n=64,m=160,degree=5,
         pi=pi,delta=delta,roots_checked=64,full_D3=hit,
         failing_root_count=sum(row['reached']<64 for row in rows),
         root0_reached=rows[0]['reached'],root0_missing=rows[0]['missing'],
         all_antipode_phases_covered=all(len(row['phase_sets'][str((row['root']%8)^7)])==8 for row in rows),
         candidate_count=1,main1088_graphs=0,CPU_seconds=time.process_time()-START)
(HERE/'PARAMETERS.json').write_text(json.dumps(dict(pi=pi,delta=delta,sigma=sigma,inverse=inverse),indent=2)+'\n')
(HERE/'ROOT_RESULTS.json').write_text(json.dumps(rows,indent=2)+'\n')
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
if hit:
    (HERE/'K64_ADJACENCY.json').write_text(json.dumps([sorted(row) for row in G])+'\n')
    with (HERE/'K64.edges').open('w') as f:
        f.write('64 160\n')
        for u,row in enumerate(G):
            for v in sorted(row):
                if u<v:f.write(f'{u} {v}\n')
print(json.dumps(out))
