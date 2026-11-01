"""Actual24/M35/delta7 high cover P of size5; no all7 edge, and nonB forces the fullP edge.
Remaining trace excess exactly3: three pair traces WITH repetition, triple+pair, or one quadruple.
True label permutations preserve the fixed high-degree vector.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
import json,time
HERE=Path(__file__).parent

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(32))
def main():
 st=time.time();pairs=[sum(1<<i for i in S) for S in combinations(range(5),2)];trips=[sum(1<<i for i in S) for S in combinations(range(5),3)];quads=[sum(1<<i for i in S) for S in combinations(range(5),4)];patterns=[]
 patterns += [('three_pairs',dict(Counter(ts))) for ts in combinations_with_replacement(pairs,3)]
 patterns += [('triple_pair',{t:1,p:1}) for t in trips for p in pairs]
 patterns += [('quadruple',{q:1}) for q in quads]
 assert Counter(c for c,ns in patterns)=={'three_pairs':220,'triple_pair':100,'quadruple':5}
 seen={};orbits=[];labelled=[];stats=[]
 for ds in ((10,8,8,8,8),(9,9,8,8,8)):
  before=len(orbits);group=[p for p in permutations(range(5)) if all(ds[i]==ds[p[i]] for i in range(5))];labels=0
  for category,multi in patterns:
   ns={t:0 for t in range(32)};ns[31]=1;ns.update(multi)
   for i,d in enumerate(ds):ns[1<<i]=d-1-sum(n for t,n in multi.items() if t>>i&1)
   assert min(ns.values())>=0 and sum(ns.values())==35 and all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(ds));kk=(ds,key(ns))
   if kk not in seen:
    idx=len(orbits);orbits.append(dict(id=idx,degrees=ds,counts=ns,category=category,multi=multi))
    for p in group:
     move=lambda t:sum(1<<p[i] for i in range(5) if t>>i&1);seen[(ds,key({move(t):n for t,n in ns.items()}))]=(idx,p)
   idx,p=seen[kk];labelled.append(dict(degrees=ds,counts=ns,category=category,multi=multi,orbit=idx,from_representative_permutation=p));labels+=1
  stats.append(dict(degrees=ds,labelled_count=labels,group_order=len(group),orbit_count=len(orbits)-before))
 result=dict(scope=__doc__,complete=True,category_counts=dict(Counter(c for c,ns in patterns)),stats=stats,labelled_count=len(labelled),orbit_count=len(orbits),labelled=labelled,orbits=orbits,elapsed_seconds=time.time()-st);(HERE/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('labelled','orbits')})
if __name__=='__main__':main()
