from pathlib import Path
from collections import deque,Counter
import json,time
HERE=Path(__file__).resolve().parent
P=HERE
assert not (P/'best.independent_check.json').exists(), 'Final audit already exists; do not repeat.'
t=time.process_time()
best=json.loads((P/'best.json').read_text())
terminal=json.loads((P/'search.terminal.json').read_text())
assert terminal['running'] is False
assert best['group_name']=='Q64' and best['group_twist']==16
n=best['n']; assert n==256
pairs=[tuple(map(int,line.split())) for line in (P/'best.edges').read_text().splitlines() if line.strip()]
assert pairs[0]==(256,1024)
edges=pairs[1:]
assert len(edges)==1024 and len(set(edges))==1024
assert all(0<=u<v<n for u,v in edges)
expected=set()
for i,j,code in zip(best['edge_u'],best['edge_v'],best['voltages']):
 y,tphase=code%32,code//32
 for x in range(32):
  for s in range(2):
   # Independent direct tuple multiplication: (x,s)(y,t).
   z=(x+(-1)**s*y+16*s*tphase)%32
   a=64*i+x+32*s; b=64*j+z+32*((s+tphase)%2)
   expected.add(tuple(sorted((a,b))))
assert expected==set(edges)
adj=[[] for _ in range(n)]
for u,v in edges: adj[u].append(v); adj[v].append(u)
assert all(len(row)==len(set(row))==8 for row in adj)
rows=[];hist=Counter();ecc=[]
for root in range(n):
 d=[-1]*n;d[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if d[v]==-1: d[v]=d[u]+1;q.append(v)
 assert -1 not in d
 rows.append(d);hist.update(d);ecc.append(max(d))
bad=sum(c for d,c in hist.items() if d>3)//2
root_misses=[sum(d>3 for d in rows[64*i]) for i in range(4)]
assert bad==best['score']['bad_unordered_pairs']
assert root_misses==best['score']['root_misses']
assert 'diameter' not in best['score'] or max(ecc)==best['score']['diameter']
assert bad==32*terminal['minimum_score_in_scored_center_scope']
report={'status':'COMPLETE','n':n,'edges':len(edges),'simple':True,'minimum_degree':8,'maximum_degree':8,'connected':True,'roots_checked':n,'diameter':max(ecc),'bad_unordered_pairs':bad,'ordered_distance_histogram':dict(sorted(hist.items())),'four_root_misses':root_misses,'independent_parameter_expansion_matches_saved_edges':True,'method':'rebuild adjacency from saved explicit edge list; ordinary Python deque BFS from every vertex; compare independently expanded tuple group formula','CPU_seconds':time.process_time()-t,'running':False,'pending':[]}
(P/'best.independent_distances.json').write_text(json.dumps(rows)+'\n')
(P/'best.independent_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
