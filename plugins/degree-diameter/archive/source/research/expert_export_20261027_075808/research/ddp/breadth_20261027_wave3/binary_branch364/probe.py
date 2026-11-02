"""One finite necessary-condition test for a degree-five binary branching lift."""
from pathlib import Path
from collections import deque, Counter
import json, time, resource
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

P=Path(__file__).resolve().parent
terminal=P/'terminal.json'
assert not terminal.exists(), 'Do not restart the completed profile.'
started=time.process_time(); n=364
raw=[list(map(int,s.split())) for s in (P/'source364.adjlist').read_text().splitlines() if s.strip() and not s.startswith('#')]
assert len(raw)==n and sorted(row[0] for row in raw)==list(range(n))
edges=sorted({tuple(sorted((row[0],v))) for row in raw for v in row[1:]})
assert len(edges)==728 and all(0<=u<v<n for u,v in edges)
adj=[[] for _ in range(n)]
for e,(u,v) in enumerate(edges): adj[u].append((v,e)); adj[v].append((u,e))
assert all(len(a)==4 for a in adj)
distances=[]; constraints=[]; hist=Counter(); unique_pairs=0
for root in range(n):
    dist=[-1]*n; ways=[0]*n; parent=[None]*n
    dist[root]=0; ways[root]=1; queue=deque([root])
    while queue:
        u=queue.popleft()
        for v,e in adj[u]:
            if dist[v]<0: dist[v]=dist[u]+1; queue.append(v)
            if dist[v]==dist[u]+1:
                ways[v]+=ways[u]
                parent[v]=(u,e)
    assert -1 not in dist and max(dist)<=5
    hist.update(dist); distances.append(dist)
    for v in range(root+1,n):
        if dist[v]==5 and ways[v]==1:
            path=[]; w=v
            while w!=root: w,e=parent[w]; path.append(e)
            assert len(path)==5
            constraints.append(tuple(sorted(path))); unique_pairs+=1
constraints=sorted(set(constraints))
prep=time.process_time()-started
source=dict(n=n,edges=len(edges),degree=4,diameter=5,all_source_BFS=n,ordered_distance_histogram=dict(sorted(hist.items())),unique_distance5_unordered_pairs=unique_pairs,distinct_unique_path_constraints=len(constraints),source_URL='https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/Del364deg4D5_adjlist.txt',CPU_seconds=prep)
(P/'source_profile.json').write_text(json.dumps(source,indent=2)+'\n')
(P/'source_distances.json').write_text(json.dumps(distances)+'\n')
(P/'source.edges').write_text(f'{n} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges))
(P/'unique5_paths.json').write_text(json.dumps(constraints)+'\n')

# Upgrade M edges from one matching to K2,2. Max degree five forces M
# to be a matching in this four-regular core. Every unique geodesic of
# length five must meet M, whatever signs are used on the other edges.
ri=[]; ci=[]; va=[]; lower=[]; upper=[]
for u in range(n):
    for v,e in adj[u]: ri.append(u); ci.append(e); va.append(1.)
    lower.append(0.); upper.append(1.)
for path in constraints:
    r=len(lower)
    for e in path: ri.append(r); ci.append(e); va.append(1.)
    lower.append(1.); upper.append(np.inf)
a=coo_matrix((va,(ri,ci)),shape=(len(lower),len(edges))).tocsc()
solve_started=time.process_time()
res=milp(c=-np.ones(len(edges)),integrality=np.ones(len(edges)),bounds=Bounds(0,1),constraints=LinearConstraint(a,np.array(lower),np.array(upper)),options={'time_limit':25.,'threads':1,'mip_rel_gap':0.0})
solve_cpu=time.process_time()-solve_started
selected=[]
if res.x is not None:
    selected=[i for i,x in enumerate(res.x) if x>0.5]
    assert all(sum(i in selected for _,i in adj[u])<=1 for u in range(n))
    assert all(any(i in selected for i in path) for path in constraints)
    (P/'matching_candidate.json').write_text(json.dumps({'edge_ids':selected,'edges':[edges[i] for i in selected]},indent=2)+'\n')
out=dict(status=('NECESSARY_MATCHING_FOUND' if selected else 'NECESSARY_MATCHING_INFEASIBLE_UNCERTIFIED' if res.status==2 else 'NECESSARY_MATCHING_UNKNOWN'),solver_status=int(res.status),solver_message=res.message,matching_size=len(selected),unique_path_constraints=len(constraints),preprocess_CPU_seconds=prep,solver_CPU_seconds=solve_cpu,total_CPU_seconds=time.process_time()-started,new_lower_bounds=0,large_lift_generated=False,full_template_excluded=False,scope='Necessary matching hitting every unique length-five geodesic in the fixed364 core. Uniform binary edge relations: bijection or full K2,2; maximum degree5. Infeasible MIP is exploratory and not a certified universal exclusion.',pending=['build finite candidate only if a necessary matching is returned'] if selected else [])
terminal.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
