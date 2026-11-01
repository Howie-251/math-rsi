"""Bounded old981 marked-capacity profile for6mixed <=3small, shared T/B budget.
No newgraphclassification or negative layout. Force everythree-transversal as a negative triple, then count minimalfour-transversals with exact inclusion-exclusion.
"""
from pathlib import Path
from itertools import combinations,product
from math import comb
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
old=json.loads((HERE.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/CENSUS_PROFILE.json').read_text())['rows']
EDGES=list(combinations(range(6),2))
def matching(lst):
 if not lst:yield [];return
 a=lst[0]
 for b in lst[1:]:
  for tail in matching([v for v in lst if v not in (a,b)]):yield [(a,b)]+tail
MATCH=list(matching(list(range(6))));assert len(MATCH)==15
rows=[];stop=None
for source_i,r in enumerate(old):
 if r['M3']>3:continue
 g=r['vector'];deg=r['degrees'];E=r['E']
 edgepoints={};masks=[]
 for pair,m in zip(EDGES,g):
  edgepoints[pair]=list(range(len(masks),len(masks)+m));masks.extend([sum(1<<v for v in pair)]*m)
 triples=[frozenset(q) for match in MATCH for q in product(*(edgepoints[pair] for pair in match))]
 assert len(triples)==len(set(triples))==r['M3']
 for k in (0,1,2,3):
  for marked in combinations(range(6),k):
   if any(deg[v]>3 for v in marked) or 24-k-E>15:continue
   labels=masks.copy()
   for v in range(6):labels.extend([1<<v]*(4-int(v in marked)-deg[v]))
   N=len(labels);assert N==24-k-E
   C4=sum((-1)**s.bit_count()*comb(sum(not m&s for m in labels),4) for s in range(64) if sum(not m&s for m in labels)>=4)
   # C4 containing a member of triples: atmost4 triples, exact IE.
   contained=0
   for z in range(1,1<<len(triples)):
    union=set.union(set(),*[set(q) for i,q in enumerate(triples) if z>>i&1]);a=len(union)
    if a<=4:contained+=(-1)**(z.bit_count()+1)*comb(N-a,4-a)
   D4=C4-contained;bound=23-4*len(triples)
   rr={'old981_index':source_i,'graph':g,'marked_three_labels':marked,'capacities':[4-int(v in marked) for v in range(6)],'E':E,'U':N,'C3':len(triples),'C4':C4,'minimal_C4':D4,'block_bound':bound,'margin':D4-bound,'three_transversals':[sorted(q) for q in triples]}
   # Directsubset crosscheck for first100 rows and every boundfailure.
   if len(rows)<100 or D4<=bound:
    A=[{v for v,m in enumerate(labels) if m>>i&1} for i in range(6)]
    direct=[frozenset(q) for q in combinations(range(N),4) if all(set(q)&a for a in A)]
    assert len(direct)==C4 and sum(not any(t<=q for t in triples) for q in direct)==D4
    rr['sets']=[sorted(a) for a in A]
   rows.append(rr)
   if D4<=bound:
    stop=rr;break
   if time.process_time()-start>9:
    stop={'cpu_budget':'prefix_at9CPU','next_after_source':source_i,'marked':marked};break
  if stop:break
 if stop:break
out={'status':'FIRST_NONGATED_BOUND' if stop and 'graph'in stop else ('CPU_PREFIX' if stop else 'COMPLETE_ALL_MARKED_ROWS_STRICT'),
 'rows_done':len(rows),'rows':rows,'stop':stop,'domain':'Old981,E>=7,capacitymark0..3, U<=15, M3<=3; E6 separate.',
 'scope':__doc__,'cpu_seconds':time.process_time()-start}
(HERE/'HIGH_SHARED_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='rows'})
