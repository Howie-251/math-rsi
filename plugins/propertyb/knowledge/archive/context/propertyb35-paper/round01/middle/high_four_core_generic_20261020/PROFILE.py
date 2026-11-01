from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent
PM=[sum(1<<i for i in p) for p in combinations(range(4),2)];TM=[7,11,13,14]
perms=list(permutations(range(4)));maps=[[sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)] for p in perms]
def canon(ns):
 return min(tuple(ns[mp[m]] for m in range(16)) for mp in maps)
def domain():
 for q in range(2,5):
  for tt in product(range(3),repeat=4):
   rem=[4-q-sum(v for m,v in zip(TM,tt) if m&p==p) for p in PM]
   if min(rem)<0:continue
   for pp in product(*(range(r+1) for r in rem)):
    ns={15:q,**dict(zip(TM,tt)),**dict(zip(PM,pp))}
    singles=[8-sum(v for m,v in ns.items() if m>>i&1) for i in range(4)]
    if min(singles)<0:continue
    cij=[q+sum(v for m,v in zip(TM,tt) if m&p==p)+v for p,v in zip(PM,pp)]
    if any(sum(c-1 for p,c in zip(PM,cij) if p>>i&1)>12 for i in range(4)):continue
    ns.update({1<<i:v for i,v in enumerate(singles)});ns[0]=35-sum(ns.values())
    if ns[0]<0:continue
    yield tuple(ns.get(i,0) for i in range(16))
st=time.process_time();allkeys=set(domain());reps={canon(ns) for ns in allkeys}
out={'scope':'complete necessary four8 core; muK>=2, all inclusive pairs<=4, degree8,rowexcess<=12,nonnegative35 inventories','labels':len(allkeys),'S4_orbits':len(reps),'q_counts':dict(Counter(ns[15] for ns in allkeys)),'cpu_seconds':time.process_time()-st,'representatives':[list(x) for x in sorted(reps)]}
(P/'PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='representatives'})
