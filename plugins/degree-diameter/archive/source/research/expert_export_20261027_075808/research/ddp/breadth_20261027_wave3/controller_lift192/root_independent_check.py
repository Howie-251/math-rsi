from pathlib import Path
from collections import Counter, deque
import json, time

P=Path(__file__).resolve().parent
out=P/'best.independent_check.json'
assert not out.exists(), 'Reuse the final saved-graph check.'
started=time.process_time(); n=192
raw=[tuple(map(int,s.split())) for s in (P/'best.edges').read_text().splitlines() if s.strip()]
assert len(raw)==384 and all(0<=u<n and 0<=v<n and u!=v for u,v in raw)
edges={tuple(sorted(e)) for e in raw}
assert len(edges)==384
adj=[set() for _ in range(n)]
for u,v in edges: adj[u].add(v); adj[v].add(u)
assert all(len(a)==4 for a in adj)
labels=json.loads((P/'best.labels.json').read_text())
assert labels['vertices']==n and labels['inverse']==[1,0,3,2]
for u,row in enumerate(labels['out']):
    assert len(row)==len(set(row))==4 and set(row)==adj[u]
    for a,v in enumerate(row): assert labels['out'][v][labels['inverse'][a]]==u

# Integer recurrence, independent of the production voltage-word support.
previous=[[int(v in adj[u]) for v in range(n)] for u in range(n)]
current=[[len(adj[u]&adj[v])-4*int(u==v) for v in range(n)] for u in range(n)]
for length in range(3,6):
    nxt=[[sum(current[w][v] for w in adj[u])-3*previous[u][v] for v in range(n)] for u in range(n)]
    assert all(x>=0 for row in nxt for x in row)
    assert all(sum(row)==4*3**(length-1) for row in nxt)
    previous,current=current,nxt
missing=[(u,v) for u in range(n) for v in range(n) if current[u][v]==0]
assert len(missing)==2752
hist=Counter(); diameter=0; bad=0
for root in range(n):
    dist=[-1]*n; dist[root]=0; queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if dist[v]<0: dist[v]=dist[u]+1; queue.append(v)
    assert -1 not in dist
    hist.update(dist); diameter=max(diameter,max(dist)); bad+=sum(x>5 for x in dist)
assert bad%2==0
report=dict(status='COMPLETE',n=n,edges=len(edges),simple=True,minimum_degree=4,maximum_degree=4,connected=True,ordinary_BFS_roots=n,ordinary_diameter=diameter,ordinary_bad_unordered_pairs_gt5=bad//2,ordered_distance_histogram=dict(sorted(hist.items())),exact_NB5_missing_ordered_pairs=len(missing),exact_NB5_witnesses=missing[:30],inverse_consistent_labels_verified=True,all_root_NB5_walk_counts=324,method='Read only saved edge list and labels. All-source ordinary BFS; separate integer recurrence N2=A2-4I, Nk=A*N(k-1)-3*N(k-2). No production support or symmetry reduction.',CPU_seconds=time.process_time()-started,pending=[],large_lift_generated=False)
out.write_text(json.dumps(report,indent=2)+'\n')
terminal=P/'terminal.json'; t=json.loads(terminal.read_text())
t['independent_full_best_check']='COMPLETE: best.independent_check.json'
t['ordinary_diameter']=diameter; t['ordinary_bad_unordered_pairs_gt5']=bad//2
terminal.write_text(json.dumps(t,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['n','ordinary_diameter','ordinary_bad_unordered_pairs_gt5','exact_NB5_missing_ordered_pairs','CPU_seconds']}))
