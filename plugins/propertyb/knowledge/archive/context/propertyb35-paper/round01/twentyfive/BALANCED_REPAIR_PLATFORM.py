"""Single known actual affine-plus-parabolas H: fixed quota coloring graph.
This diagnoses whether a unique bad edge can be a strict-descent trap.
It is unrelated to the old A5_SWAP pair-moment LP and enumerates no H family.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,deque
import json,time
P=Path(__file__).resolve().parent;root=P.parents[3];st=time.perf_counter()
H=json.loads((root/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json').read_text());E=[sum(1<<v for v in e) for e in H['edges']]
G=[sorted(5*x+(x*x+c)%5 for x in range(5)) for c in range(5)];quotas=[2,2,2,3,3]
owner={v:i for i,g in enumerate(G) for v in g}
assert len(E)==35 and len(set(E))==35 and all(e.bit_count()==5 for e in E)
assert all(sum(bool(e&(1<<v)) for e in E)==7 for v in range(25))
assert all(sum((e&(1<<u))!=0 and (e&(1<<v))!=0 for e in E)==(2 if owner[u]==owner[v] else 1) for u,v in combinations(range(25),2))
choices=[[sum(1<<v for v in s) for s in combinations(g,r)] for g,r in zip(G,quotas)]
def bad(red):return [j for j,e in enumerate(E) if red&e==0 or red&e==e]
def neighbors(red):
 for g in G:
  for v in g:
   if not(red>>v&1):continue
   for w in g:
    if red>>w&1:continue
    yield v,w,red^(1<<v)^(1<<w)
colors={sum(row):len(bad(sum(row))) for row in product(*choices)};assert len(colors)==100000
hist=Counter(colors.values());trap=None;checked=0
for red,c in colors.items():
 if c!=1:continue
 checked+=1
 nn=[(v,w,z,colors[z]) for v,w,z in neighbors(red)]
 if all(k>=1 for v,w,z,k in nn):trap=red;break
out=dict(scope=__doc__,source='context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json',groups=G,quotas=quotas,colorings=100000,bad_count_histogram={str(k):v for k,v in sorted(hist.items())},one_bad_colorings_checked_until_first_trap=checked,trap_found=trap is not None)
if trap is not None:
 critical=[j for j,e in enumerate(E) if (e&trap).bit_count() in (1,4)]
 repair_swaps=[]
 destroys=creates=0
 before_bad=set(bad(trap))
 for v,w,z in neighbors(trap):
  after_bad=set(bad(z));des=sorted(before_bad-after_bad);cre=sorted(after_bad-before_bad)
  destroys+=len(des);creates+=len(cre)
  if des:repair_swaps.append(dict(swap=[v,w],destroyed=des,created=cre))
 assert creates-destroys==sum(colors[z]-1 for v,w,z in neighbors(trap))
 q=deque([trap]);prev={trap:None};end=None
 while q and end is None:
  a=q.popleft()
  for v,w,z in neighbors(a):
   if colors[z]==0:prev[z]=(a,v,w);end=z;break
   if colors[z]==1 and z not in prev:prev[z]=(a,v,w);q.append(z)
 path=[]
 if end is not None:
  a=end
  while prev[a] is not None:
   b,v,w=prev[a];path.append(dict(swap=[v,w],before_red=[i for i in range(25) if b>>i&1],after_red=[i for i in range(25) if a>>i&1],before_bad_edges=bad(b),after_bad_edges=bad(a)));a=b
  path.reverse()
 out.update(trap_red=[v for v in range(25) if trap>>v&1],trap_bad_edges=bad(trap),critical_edges=critical,creation_multiplicity_sum=creates,destruction_multiplicity_sum=destroys,repair_swaps=repair_swaps,all_30_neighbor_counts=[dict(swap=[v,w],bad=colors[z]) for v,w,z in neighbors(trap)],zero_change_then_good_path=path,plateau_BFS_seen=len(prev),path_to_proper_found=end is not None)
out['elapsed_seconds']=time.perf_counter()-st
(P/'BALANCED_REPAIR_PLATFORM.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['all_30_neighbor_counts','zero_change_then_good_path']},indent=2))
