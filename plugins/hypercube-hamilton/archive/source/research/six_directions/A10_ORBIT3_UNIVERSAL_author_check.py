"""Producer-side deterministic validation, separate from C++ rank search."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
pre='A10_ORBIT3_UNIVERSAL_rank'
rank=json.loads((R/(pre+'.json')).read_text())
indices=rank['selected_row_indices'];assert len(indices)==1024==len(set(indices))
allpairs=(R/'A10_ORBIT3_SPECTRUM_pairs.bin').read_bytes()
allforests=(R/'A10_ORBIT3_SPECTRUM_forests.bin').read_bytes()
selected=(R/(pre+'_selected_pairs.bin')).read_bytes()
forest=b''.join(allforests[40*i:40*(i+1)] for i in indices)
assert selected==b''.join(allpairs[22*i:22*(i+1)] for i in indices)
(R/(pre+'_selected_forests.bin')).write_bytes(forest)
H={0,1,2,4,8,15,23,27,29,30};K=set(range(32))-H
for i in range(1024):
 rec=forest[40*i:40*(i+1)];adj=[[] for _ in range(32)]
 edges=[tuple(rec[j:j+2]) for j in range(0,40,2)]
 assert len(set(edges))==20
 for a,b in edges:
  assert a<b and (a^b) in {1,2,4,8,16}
  adj[a].append(b);adj[b].append(a)
 assert not adj[0]
 assert all(len(adj[v])==(1 if v in K else 2) for v in range(1,32))
 visited=set();P=[]
 for root in sorted(K):
  if root in visited:continue
  visited.add(root);previous=root;current=adj[root][0]
  while current not in K:
   assert current not in visited
   visited.add(current)
   nxt=next(v for v in adj[current] if v!=previous)
   previous,current=current,nxt
  assert current not in visited;visited.add(current);P.append((root,current))
 assert visited==set(range(1,32))
 assert bytes(v for pair in sorted(P) for v in pair)==selected[22*i:22*(i+1)]

# Independently validate elimination evidence from saved integers.
def rows(name):
 raw=(R/(pre+name+'.bin')).read_bytes();assert len(raw)==1024*128
 return [int.from_bytes(raw[128*i:128*(i+1)],'little') for i in range(1024)]
matrix=rows('_matrix');tri=rows('_pivots');combo=rows('_combos')
for i in range(1024):
 assert tri[i].bit_length()==i+1
 actual=0;c=combo[i]
 while c:
  low=c&-c;actual^=matrix[low.bit_length()-1];c^=low
 assert actual==tri[i]
out=dict(status='PASS_PRODUCER_CHECK_NOT_FRESH_AUDIT',selected_forests=1024,
 selected_P_alignment=True,forest_degrees_and_shortness=True,
 forest_paths_and_exact_P=True,elimination_combinations_verified=True,
 rank_lower_bound=1024,external_rank_upper_bound_required=1024,
 fresh_independent_acceptance_pending=True)
(R/'A10_ORBIT3_UNIVERSAL_author_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
