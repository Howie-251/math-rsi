from pathlib import Path
from collections import Counter
import json,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
P=Path(__file__).resolve().parent;started=time.process_time();S=P.parent.parent/'breadth_20261027_wave2/sources';source=S/'bhakar104.edges';old=json.loads((S/'bhakar104_check.json').read_text())
data=[list(map(int,line.split())) for line in source.read_text().splitlines() if line.strip() and not line.startswith('#')];n,m=data[0];edges=[tuple(x) for x in data[1:]];assert (n,m)==(104,208) and len(edges)==m
adj=[[] for _ in range(n)]
for u,v in edges:adj[u].append(v);adj[v].append(u)
for row in adj:row.sort()
assert all(len(set(row))==4 for row in adj)
nb2=[[0]*n for _ in range(n)];nb4=[[0]*n for _ in range(n)];all_counts=[[[0]*n for _ in range(n)] for _ in range(5)];cycles=set()
def canonical(cycle):
 return min(tuple(a[i:]+a[:i]) for a in (cycle,list(reversed(cycle))) for i in range(5))
for root in range(n):
 all_counts[0][root][root]=1
 for depth in range(1,5):
  prev=all_counts[depth-1][root];row=all_counts[depth][root]
  for u,count in enumerate(prev):
   if count:
    for v in adj[u]:row[v]+=count
 def rec(walk):
  u=walk[-1];depth=len(walk)-1
  if depth==2:nb2[root][u]+=1
  if depth==4:
   nb4[root][u]+=1
   if u in adj[root] and len(set(walk))==5:cycles.add(canonical(walk))
   return
  for v in adj[u]:
   if depth and v==walk[-2]:continue
   rec(walk+[v])
 rec([root])
assert all(sum(row)==108 for row in nb4)
bad=[(u,v) for u in range(n) for v in range(n) if u!=v and not nb2[u][v] and not nb4[u][v]]
edge5=Counter()
for cycle in cycles:
 for u,v in zip(cycle,cycle[1:]+cycle[:1]):edge5[tuple(sorted((u,v)))]+=1
def bound(pair):
 u,v=pair;return sum(3**depth*all_counts[depth][u][v] for depth in range(5))
witness=min(bad,key=lambda p:(bound(p),p)) if bad else None
wr=None
if witness:
 u,v=witness;walks=[]
 def enumerate_all(walk):
  if walk[-1]==v:walks.append(walk)
  if len(walk)==5:return
  for x in adj[walk[-1]]:enumerate_all(walk+[x])
 enumerate_all([u]);wr=dict(source=u,target=v,identity=u==v,NB2=nb2[u][v],NB4=nb4[u][v],all_walk_counts_length0_through4=[all_counts[d][u][v] for d in range(5)],all_walks_length_at_most4=walks,union_reachability_upper_bound=sum(3**d*all_counts[d][u][v] for d in range(5)),target_fiber_size=81,true_fixed_projection_capacity_obstruction=bound(witness)<81)
out=dict(status='RAW_NECESSARY_COVERAGE_FAIL_STOP' if bad else 'RAW_NECESSARY_COVERAGE_PASS_NEXT_LABEL_SCREEN_REQUIRED',source_file=str(source),source_url=old['source_url'],source_ordinary_check_reused=True,ordinary_BFS_repeated=False,n=n,m=m,controller_degree=4,criterion='identity OR NB2 OR all NB4, before excluding8bad chart words',ordered_pairs=n*n,raw_missing_ordered_pairs=len(bad),raw_missing_unordered_pairs=sum(u<v for u,v in bad),raw_missing_adjacent_ordered_pairs=sum(v in adj[u] for u,v in bad),raw_missing_nonadjacent_ordered_pairs=sum(v not in adj[u] for u,v in bad),five_cycles=len(cycles),edges_in_five_cycle=sum(edge5[tuple(sorted(e))]>0 for e in edges),edges_not_in_five_cycle=[list(e) for e in edges if not edge5[tuple(sorted(e))]],witness=wr,raw_gap_alone_scope='Only excludes this wide100word/pencil sufficient certificate; the supplied full-walk witness may independently exclude the fixed projection.',twofactor_or_label_search_started=False,graph_modified=False,CPU_seconds=time.process_time()-started)
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');(P/'raw_missing_pairs.json').write_text(json.dumps(bad)+'\n');(P/'five_cycle_edge_counts.json').write_text(json.dumps([dict(edge=list(e),five_cycles=edge5[tuple(sorted(e))]) for e in edges],indent=2)+'\n');(P/'NB2_NB4_counts.json').write_text(json.dumps(dict(NB2=nb2,NB4=nb4),separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in out.items() if k!='edges_not_in_five_cycle'},indent=2))
