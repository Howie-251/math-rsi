"""Complete tiny auxiliary catalog for HS59 t=7..11, after max deleted degree<=6."""
from pathlib import Path
import itertools,json,math,time
import networkx as nx
start=time.process_time()
components=[]
for G in nx.graph_atlas_g():
 n=G.number_of_nodes();m=G.number_of_edges()
 if 2<=n<=5 and 1<=m<=4 and nx.is_connected(G):
  components.append(G)
components.sort(key=lambda G:(G.number_of_edges(),G.number_of_nodes(),sorted(dict(G.degree()).values())))
assert len(components)==10

def multisets(rem,lo=0):
 if rem==0:yield [];return
 for i in range(lo,len(components)):
  e=components[i].number_of_edges()
  if e>rem:continue
  for tail in multisets(rem-e,i):yield [i]+tail

def name(G):
 e=G.number_of_edges();n=len(G);d=max(dict(G.degree()).values())
 if e==1:return 'K2'
 if e==2:return 'P3'
 if e==3:return 'K3' if n==3 else ('K1,3' if d==3 else 'P4')
 if n==4:return 'C4' if d==2 else 'triangle_with_pendant'
 return {2:'P5',3:'five_vertex_fork',4:'K1,4'}[d]

results=[]
for t in range(7,12):
 m=11-t
 deleted_degree_bounds={d:min(t*(d-1),math.comb(d,2)+math.comb(t-d,2)+(t-d)) for d in range(1,7)}
 bound=max(deleted_degree_bounds.values());entries=[]
 for ids in multisets(m):
  G=nx.Graph();offset=0;names=[]
  for i in ids:
   C=components[i];G.add_edges_from((a+offset,b+offset) for a,b in C.edges());offset+=len(C);names.append(name(C))
  assert offset<=9
  G.add_nodes_from(range(9));adj=[set(G[v]) for v in range(9)]
  bad=[list(e) for e in itertools.combinations(range(9),2) if e[1] not in adj[e[0]] and not adj[e[0]]&adj[e[1]]]
  need=len(bad)-2*t
  entries.append(dict(nontrivial_components=names,isolates=9-offset,edges=sorted([list(sorted(e)) for e in G.edges()]),bad_pairs=bad,bad_pair_count=len(bad),necessary_deleted_wedges=need,passes_deleted_wedge_bound=need<=bound))
 results.append(dict(t=t,H_edges=m,deleted_degree_at_most=6,deleted_wedge_bounds_by_max_degree=deleted_degree_bounds,deleted_wedge_upper_bound=bound,auxiliary_count=len(entries),remaining_auxiliary_count=sum(e['passes_deleted_wedge_bound'] for e in entries),auxiliaries=entries))
assert [r['auxiliary_count'] for r in results]==[11,5,2,1,1]
assert [r['remaining_auxiliary_count'] for r in results]==[8,5,2,1,1]
out=dict(status='EXACT_AUXILIARY_CATALOG_NOT_FAMILY_EXCLUSION',cpu_seconds=time.process_time()-start,networkx_version=nx.__version__,scope='All simple H on9 vertices with0..4 edges, up to isomorphism; wedge-bound survivors remain unproved.',targets=results)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cpu_seconds':out['cpu_seconds'],'summary':[{k:r[k] for k in ['t','H_edges','auxiliary_count','remaining_auxiliary_count','deleted_wedge_upper_bound']} for r in results]}))
