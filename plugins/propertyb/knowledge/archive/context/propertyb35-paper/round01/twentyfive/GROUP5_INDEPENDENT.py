"""Independent high-block-first enumeration: choose every size3..5 block count,
then all size2 multiplicities are forced by remaining pair capacities.
Compare all feasible labelled inventories to the union of 27 saved S5 orbits.
"""
from pathlib import Path
from itertools import combinations,permutations
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
pairs=[(1<<i)|(1<<j) for i,j in combinations(range(5),2)]
big=[t for t in range(32) if t.bit_count()>=3]
contents={t:[i for i,p in enumerate(pairs) if p&t==p] for t in big}
raw=feasible=nodes=0;keys=set()
def rec(k,rem,multi):
 global raw,feasible,nodes
 nodes+=1
 if k==len(big):
  ns={**multi,**{t:c for t,c in zip(pairs,rem) if c}}
  raw+=1;singles=[7-sum(c for t,c in ns.items() if t>>i&1) for i in range(5)]
  empty=35-sum(ns.values())-sum(singles)
  if min(singles+[empty])<0:return
  feasible+=1;ns.update({1<<i:c for i,c in enumerate(singles) if c});ns[0]=empty
  keys.add(tuple(sorted(ns.items())));return
 t=big[k];inds=contents[t];cap=min(rem[i] for i in inds)
 if t==31:cap=min(cap,1)
 for c in range(cap+1):
  rr=list(rem)
  for i in inds:rr[i]-=c
  mm=multi if c==0 else {**multi,t:c}
  rec(k+1,tuple(rr),mm)
rec(0,(2,)*10,{})
src=json.loads((P/'GROUP5_CATALOGUE.json').read_text());expected=set()
for rep in src['representatives']:
 ns={int(t):c for t,c in rep['counts'].items()}
 for perm in permutations(range(5)):
  tr=lambda t:sum(1<<perm[i] for i in range(5) if t>>i&1)
  expected.add(tuple(sorted((tr(t),c) for t,c in ns.items())))
assert raw==src['labelled_multicovers']==924
assert feasible==len(keys)==len(expected)==818
assert keys==expected
out=dict(scope=__doc__,complete=True,labelled_multicovers=raw,feasible_labelled=feasible,saved_orbits=27,all_labelled_inventories_equal=True,recursion_nodes=nodes,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
