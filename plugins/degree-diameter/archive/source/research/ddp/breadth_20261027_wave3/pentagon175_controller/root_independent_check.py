from pathlib import Path
from collections import deque, Counter
import json, time

P=Path(__file__).resolve().parent
out=P/'best.independent_check.json'
assert not out.exists(), 'Reuse the existing final check.'
t=time.process_time()
rows=[tuple(map(int,s.split())) for s in (P/'best.edges').read_text().splitlines() if s.strip() and not s.startswith('#')]
assert rows[0]==(175,350)
edges=rows[1:]
assert len(edges)==len(set(edges))==350
adj=[set() for _ in range(175)]
for u,v in edges:
    assert 0<=u<v<175
    adj[u].add(v);adj[v].add(u)
assert all(len(s)==4 for s in adj)
label_data=json.loads((P/'best.labels.json').read_text())
labels=label_data['neighbors_by_label'];inv=label_data['inverse_symbols']
assert inv==[1,0,3,2] and len(labels)==175
for u in range(175):
    assert len(labels[u])==len(set(labels[u]))==4 and set(labels[u])==adj[u]
    assert labels[u][0]==5*(u//5)+(u%5+1)%5
    for a,v in enumerate(labels[u]):
        assert labels[v][inv[a]]==u

# Independent integer nonbacktracking-count recurrence for a four-regular graph.
A=[[int(v in adj[u]) for v in range(175)] for u in range(175)]
N2=[[len(adj[u]&adj[v])-4*int(u==v) for v in range(175)] for u in range(175)]
previous,current=A,N2
for length in range(3,6):
    nxt=[[sum(current[w][v] for w in adj[u])-3*previous[u][v] for v in range(175)] for u in range(175)]
    assert all(x>=0 for row in nxt for x in row)
    assert all(sum(row)==4*3**(length-1) for row in nxt)
    previous,current=current,nxt
missing=[(u,v) for u in range(175) for v in range(175) if current[u][v]==0]
assert len(missing)==2696
assert all(current[u][u]>0 for u in range(175))
hist=Counter();diam=0;bad=0
for root in range(175):
    dist=[-1]*175;dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    assert -1 not in dist
    hist.update(dist);diam=max(diam,max(dist));bad+=sum(d>5 for d in dist)
assert bad%2==0
report=dict(status='COMPLETE',n=175,edges=350,simple=True,minimum_degree=4,maximum_degree=4,connected=True,ordinary_BFS_roots=175,ordinary_diameter=diam,ordinary_bad_unordered_pairs_gt5=bad//2,ordered_distance_histogram=dict(sorted(hist.items())),exact_NB5_missing_ordered_pairs=len(missing),exact_NB5_witnesses=missing[:20],inverse_consistent_labels_verified=True,all_root_NB5_walk_counts=324,method='Reconstruct from saved edges; integer N2=A2-4I, Nk=A*N(k-1)-3*N(k-2); ordinary deque BFS separately. No search bitset state reused.',CPU_seconds=time.process_time()-t,pending=[],large_lift_generated=False)
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['ordinary_diameter','ordinary_bad_unordered_pairs_gt5','exact_NB5_missing_ordered_pairs','CPU_seconds']}))
