"""Bounded anchor-label and shared-group repair pilot on the saved actual H.
No hypergraphs are generated. Restricted colorings are checked both through the
five shared group variables and directly on each of the 35 input edges.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json,time
P=Path(__file__).resolve().parent
root=P.parents[3]
source=root/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json'
st=time.perf_counter(); H=json.loads(source.read_text()); E=[set(e) for e in H['edges']]
groups=[set(5*x+(x*x+c)%5 for x in range(5)) for c in range(5)]
owner={v:i for i,G in enumerate(groups) for v in G}
assert len(E)==35 and len({tuple(sorted(e)) for e in E})==35
assert all(len(e)==5 for e in E)
assert all(sum(v in e for e in E)==7 for v in range(25))
assert all(sum(u in e and v in e for e in E)==(2 if owner[u]==owner[v] else 1) for u,v in combinations(range(25),2))
x=0; G=groups[0]; gv=sorted(G); outside=set(range(25))-G
anchor=[j for j,e in enumerate(E) if x in e]
labels={v:[t for t,j in enumerate(anchor) if v in E[j]] for v in range(25) if v!=x}
assert all(len(labels[v])==1 for v in outside)
assert all(len(labels[v])==2 for v in G-{x})
label={v:labels[v][0] for v in outside}
# Actual obstruction to the TD assertion that every nonanchor block has distinct labels.
repeats=[]
for j,e in enumerate(E):
 if x in e:continue
 for t in range(7):
  vv=sorted(v for v in e-G if label[v]==t)
  if len(vv)>1:
   assert len({owner[v] for v in vv})==1
   repeats.append(dict(edge_index=j,anchor_edge_index=anchor[t],vertices=vv,group=owner[vv[0]]))
# General all-singleton-ray construction, then its actual two-axis instance.
ray=[j for j in anchor if E[j]&G=={x}]
assert ray==[0,5]
R=(G|set().union(*(E[j] for j in ray)))-{x}
red_counts=[len(e&R) for e in E]
assert all(0<c<5 for c in red_counts)
nonanchor_counts=[]
for j,e in enumerate(E):
 if x in e:continue
 k=len(e&G)+sum(len(e&E[a]) for a in ray)
 assert k==len(e&R)
 nonanchor_counts.append(dict(edge_index=j,group_trace=len(e&G),ray_intersections=[len(e&E[a]) for a in ray],red_count=k))
# Test the exact residual equivalence, not an independent choice for each trace.
counts=Counter(); good_labels=Counter(); scheme_count=0; good=0; first=None
for flip in [None,1,2,3,4]:
 for bm in range(128):
  fixed={v:((bm>>label[v])&1) ^ (owner[v]==flip) for v in outside}
  requirements=[]; impossible=False
  for e in E:
   T=e&G; O=e-G; colors={fixed[v] for v in O}
   if len(colors)==2:continue
   if not O:requirements.extend([(T,0),(T,1)])
   elif not T:impossible=True;break
   else:requirements.append((T,1-next(iter(colors))))
  n=0
  for gm in range(32):
   cG={v:(gm>>i)&1 for i,v in enumerate(gv)}
   residual=not impossible and all(any(cG[v]==color for v in T) for T,color in requirements)
   c={**fixed,**cG}
   direct=all(len({c[v] for v in e})==2 for e in E)
   assert residual==direct
   scheme_count+=1
   if direct:
    n+=1; good+=1; counts[str(flip)]+=1
    if first is None:first=dict(flip=flip,label_mask=bm,group_mask=gm,red=sorted(v for v in c if c[v]))
  if n:good_labels[str(flip)]+=1
# Interface diagnostic on the previously surviving 22 local trace representatives.
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text())
actual_mu=Counter(sum(1<<i for i,v in enumerate(gv) if v in e) for e in E)
assert actual_mu=={int(t):c for t,c in cat['representatives'][23]['counts'].items()}
parts=json.loads((P/'GROUP5_PARTITIONS.json').read_text())
alive={r['id'] for r in parts['results'] if r['status']=='FEASIBLE'}
local=[]
for r in cat['representatives']:
 if r['id'] not in alive:continue
 mu={int(t):c for t,c in r['counts'].items()}
 local.append(dict(id=r['id'],singleton_ray_counts=[mu.get(1<<i,0) for i in range(5)],empty_trace_count=mu.get(0,0),two_ray_anchor_count=sum(mu.get(1<<i,0)==2 for i in range(5))))
out=dict(scope=__doc__,actual_source=str(source.relative_to(root)),actual_group_representative_id=23,actual_group_trace_counts=dict(actual_mu),anchor=x,group=gv,anchor_edge_indices=anchor,external_labels={str(v):label[v] for v in sorted(outside)},double_labels_on_G={str(v):labels[v] for v in sorted(G-{x})},repeated_label_witnesses=repeats,two_ray_repair=dict(ray_edge_indices=ray,red=sorted(R),all_35_red_counts=red_counts,nonanchor_checks=nonanchor_counts),restricted_family=dict(label_masks=128,flip_choices=5,shared_group_masks=32,scheme_count=scheme_count,successful_schemes=good,successful_schemes_by_flip=dict(counts),successful_label_masks_by_flip=dict(good_labels),first_success=first,equivalence_checked_on_all_schemes=True,counts_are_parameter_schemes_not_distinct_colorings=True),local_22_trace_interface=local,elapsed_seconds=time.perf_counter()-st)
(P/'ANCHOR_TRANSFER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['anchor','group','anchor_edge_indices','two_ray_repair','restricted_family','elapsed_seconds']},indent=2))
