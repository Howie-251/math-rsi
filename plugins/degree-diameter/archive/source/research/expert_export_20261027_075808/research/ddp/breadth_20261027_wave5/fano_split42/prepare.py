from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
triples=sorted(sum(1<<v for v in row) for row in combinations(range(7),3))
lines=[sum(1<<((i+x)%7) for x in [0,1,3]) for i in range(7)]
assert len(set(lines))==7
edges=[(u,v) for j,u in enumerate(triples) for v in triples[j+1:] if not u&v]
adj={u:sorted(v for v in triples if not u&v) for u in triples}
assert len(triples)==35 and len(edges)==70 and all(len(row)==4 for row in adj.values())
assert not any(u in lines and v in lines for u,v in edges)
B=sorted(set(triples)-set(lines));bi={u:i for i,u in enumerate(B)}
assert len(B)==28 and all(sum(v in lines for v in adj[u])==1 for u in B)
bb=[(bi[u],bi[v]) for u,v in edges if u in bi and v in bi]
assert len(bb)==42 and Counter(x for e in bb for x in e)==Counter({u:3 for u in range(28)})
neighbors=[[bi[v] for v in adj[u]] for u in lines]
assert all(len(row)==4 and row==sorted(row) for row in neighbors)
for u in triples:
 reach={u}
 for _ in range(3):reach |= {w for v in reach for w in adj[v]}
 assert len(reach)==35
with (P/'source.edges').open('w') as f:
 print(35,len(edges),file=f)
 ids={u:i for i,u in enumerate(triples)}
 for u,v in edges:print(ids[u],ids[v],file=f)
with (P/'input.txt').open('w') as f:
 print(len(bb),file=f)
 for u,v in bb:print(u,v,file=f)
 for row in neighbors:print(*row,file=f)
data=dict(source='Odd graph O4 = KG(7,3)',encoding='integer bitmask; bit v represents point v in Z7',
          source_vertices=35,source_edges=70,source_degree_histogram={4:35},source_all_roots_D3_reachability=True,
          masks_in_source_order=triples,Fano_line_masks_in_i_order=lines,B_masks_in_final_order=B,
          line_B_neighbor_ids=neighbors,B_vertices=28,B_edges=42,B_degree_histogram={3:28},
          A_independent=True,B_unique_A_neighbor=True,
          final_A_endpoint_labels='A_i0=28+2i, A_i1=29+2i',
          partition_choices='choice k in {0,1,2}: sorted neighbor positions {0,k+1} go to half0; other two to half1',
          matching='A_i0--A_(i+t mod 7)1, i=0..6; t=1..6',
          candidate_count=3**7*6,final_vertices=42,final_edges=84,target_degree=4,target_diameter=3,
          CPU_seconds=time.process_time()-t)
(P/'source_structure.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k not in ['masks_in_source_order','Fano_line_masks_in_i_order','B_masks_in_final_order','line_B_neighbor_ids']},indent=2))
