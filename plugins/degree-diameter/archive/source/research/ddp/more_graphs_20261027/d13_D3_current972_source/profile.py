"""Structure only: no source ordinary-distance BFS."""
from collections import Counter
import json
from pathlib import Path
import resource
import time
P=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU,(3,4));start=time.process_time()
rows={}
for line in (P/'source972.author.adjlist.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    a=list(map(int,line.split()));rows[a[0]]=a[1:]
n=len(rows);assert n==972 and set(rows)==set(range(n))
adj=[set(rows[u]) for u in range(n)]
assert all(len(rows[u])==len(adj[u]) and u not in adj[u] for u in range(n))
assert all(u in adj[v] for u in range(n) for v in adj[u])
deg=[len(a) for a in adj];m=sum(deg)//2;free=[u for u in range(n) if deg[u]<13]
assert max(deg)<=13
sat=[sum(deg[v]==13 for v in a) for a in adj];minimum=min(sat)
blocks=[]
for b in range(36):
    vertices=range(27*b,27*(b+1));inside={u:[v for v in adj[u] if v//27==b] for u in vertices}
    external={u:[v for v in adj[u] if v//27!=b] for u in vertices}
    blocks.append(dict(block=b,internal_degree_histogram=dict(Counter(len(v) for v in inside.values())),external_degree_histogram=dict(Counter(len(v) for v in external.values())),internal_edges=sum(map(len,inside.values()))//2,internal_isolates=[u for u,v in inside.items() if not v],external_block_multiplicity_patterns=sorted(set(tuple(sorted(Counter(v//27 for v in external[u]).values())) for u in vertices))))
proxy=[]
for u in range(n):
    if deg[u]!=13:continue
    best=max((len(adj[u]&adj[w]) for w in free),default=0)
    parents=[w for w in free if len(adj[u]&adj[w])==best]
    proxy.append(dict(saturated_pin=u,max_free_neighbor_overlap=best,free_candidates=parents))
overall=max((x['max_free_neighbor_overlap'] for x in proxy),default=0)
examples=[]
for x in proxy:
    if x['max_free_neighbor_overlap']!=overall:continue
    u=x['saturated_pin'];w=x['free_candidates'][0]
    examples.append(dict(saturated_pin=u,free_proxy=w,shared_neighbors=sorted(adj[u]&adj[w]),only_saturated_pin=sorted(adj[u]-adj[w]),only_free_proxy=sorted(adj[w]-adj[u])))
    if len(examples)==5:break
result=dict(status='ACTUAL972_STRUCTURE_PROFILE_COMPLETE',n=n,m=m,Delta=max(deg),degree_histogram=dict(Counter(deg)),free_vertices=free,free_vertex_count=len(free),free_slots=sum(13-deg[u] for u in free),saturated_neighbor_histogram=dict(Counter(sat)),minSatN=minimum,minSatN_prototypes=[u for u in range(n) if sat[u]==minimum],zeroSatN_prototypes=[u for u in range(n) if sat[u]==0],onefault_prototypes=[u for u in range(n) if sat[u]==1],max_free_proxy_neighbor_overlap=overall,free_proxy_best_overlap_histogram=dict(Counter(x['max_free_neighbor_overlap'] for x in proxy)),proxy_examples=examples,contiguous27_blocks=blocks,source_allroot_BFS=0,source_single_root_BFS=0,candidate_graphs=0,ordinary_bad_unordered_pairs=None,source_reported_D=3,actual_D=None,CPU_seconds=time.process_time()-start)
(P/'SOURCE_PROFILE.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'source972.edges').write_text(f'{n} {m}\n'+''.join(f'{u} {v}\n' for u in range(n) for v in sorted(adj[u]) if u<v))
print(json.dumps({k:v for k,v in result.items() if k not in ['free_vertices','minSatN_prototypes','zeroSatN_prototypes','onefault_prototypes','contiguous27_blocks','proxy_examples']}))
print('free',free)
print('block0',blocks[0])
print('proxy_examples',examples)
