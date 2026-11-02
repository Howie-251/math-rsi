from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
edges=[]
for line in (P/'source1620.author.edges.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'):continue
 u,v=map(int,line.split());edges.append((u,v))
n=1+max(max(e) for e in edges);adj=[set() for _ in range(n)]
for u,v in edges:
 assert u!=v and v not in adj[u]
 adj[u].add(v);adj[v].add(u)
assert n==1620 and len(edges)==12150
degrees=[len(a) for a in adj];free=[u for u,d in enumerate(degrees) if d<15]
sat=[sum(degrees[v]==15 for v in a) for a in adj]
blocks=[]
for b in range(60):
 rows=range(27*b,27*(b+1))
 inside=Counter(sum(v//27==b for v in adj[u]) for u in rows)
 dests={tuple(sorted(Counter(v//27 for v in adj[u]).items())) for u in rows}
 blocks.append({'block':b,'internal_degree_histogram':dict(inside),
 'external_neighbor_patterns':[[list(a) for a in z] for z in sorted(dests)]})
assert Counter(degrees)=={15:1620}
assert all(z['internal_degree_histogram']=={0:27} and len(z['external_neighbor_patterns'])==1 and len(z['external_neighbor_patterns'][0])==5 and all(m==3 for b,m in z['external_neighbor_patterns'][0]) for z in blocks)
construction=json.loads((P/'construction.author.json').read_text())
assert construction['order']==1620 and construction['degree']==15
res={'status':'ACTUAL1620_FULL15REGULAR_PRESERVE_OLD_EDGE_ENTRY_CLOSED','n':n,'m':len(edges),
 'source_bytes':(P/'source1620.author.edges.txt').stat().st_size,'Delta':max(degrees),
 'degree_histogram':dict(Counter(degrees)),'free_vertices':free,'free_count':len(free),
 'free_slots':sum(15-d for d in degrees),'saturated_neighbor_histogram':dict(Counter(sat)),
 'minSatN':min(sat),'zero_fault_prototypes':sum(x==0 for x in sat),'onefault_prototypes':sum(x==1 for x in sat),
 'fiber_blocks':60,'fiber_size':27,'blocks':blocks,'fiber_internal_edges':0,
 'block_degree':5,'edges_per_adjacent_block':81,'every_vertex_per_adjacent_block_degree':3,
 'reported_source_D':3,'actual_D':None,'ordinary_bad_unordered_pairs':None,
 'source_BFS':0,'radius2_cache':0,'solver_runs':0,'candidate_graphs':0,
 'prediction':'SUPPORTED_METADATA_BASED_REGULARITY','CPU_seconds':time.process_time()-start,
 'closure_scope':'This actual source, all old edges retained, maxdegree15: no nonempty connected append possible because all oldvertices saturated.',
 'unclosed_gap':'Does not exclude degree-releasing deletions, other source recipes or general larger(15,3)graphs.'}
(P/'SOURCE_PROFILE.json').write_text(json.dumps(res,indent=2)+'\n')
with (P/'source1620.header.edges').open('w') as f:
 f.write(f'{n} {len(edges)}\n')
 for u,v in sorted(tuple(sorted(e)) for e in edges):f.write(f'{u} {v}\n')
facts={'status':res['status'],'actual_source_n':n,'actual_source_m':len(edges),'actual_source_degree_histogram':res['degree_histogram'],
 'source_D_published':3,'source_D_reverified':False,'source_readme':'README.author.md','source_recipe':'construction.author.json',
 'source_literal':'source1620.author.edges.txt','primary_repo':'https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg15/dia3',
 'source_credit':'Nishant Bhakar public degree-diameter-graphs, current(15,3)1620',
 'construction':'route-chart lift,60controller vertices x F3^3,5external symbols each3neighbors; no within-cell edges',
 'controller':'Z20-lift of3base Schreier permutations, a=(1 2),b=(0 1 2),s=(0 1); va=(6,3,12),vb=0; s link voltage1 and semi-edge voltage10',
 'odd_fiber_resolution':'The symbol s is a fixedpoint-free involution on60controller vertices: its base semiedge atc2 shiftsg by10mod20. It is not an internal involution of an odd27cell; all15slots are external.',
 'free_count':0,'minSatN':15,'onefaultcount':0,'source_BFS':0,'R2_or_solver':0}
(P/'SOURCE_FACTS.json').write_text(json.dumps(facts,indent=2)+'\n')
for fn in ['RESULT.json','terminal.json']:
 (P/fn).write_text(json.dumps({k:v for k,v in res.items() if k!='blocks'}|{'pending':[]},indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='blocks'},indent=2))
