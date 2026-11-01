"""Only near-saturated j3-middle cross inventories t14..16; no general q2 table."""
from pathlib import Path
from itertools import product,permutations
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(P.parent),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
CROSS=[5,9,6,10];RES=[1,2,4,8,3,12,7,11,13,14,15]
GROUP=[]
for p in permutations(range(4)):
 if {frozenset((p[0],p[1])),frozenset((p[2],p[3]))}!={frozenset((0,1)),frozenset((2,3))}:continue
 GROUP.append([sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)])
assert len(GROUP)==8
def degree(ns):return tuple(sum(n for m,n in enumerate(ns) if m>>i&1) for i in range(4))
def image(ns,mp):
 out=[0]*16
 for m,n in enumerate(ns):out[mp[m]]=n
 return tuple(out)
def canon(ns):return min((degree(q),q) for q in (image(ns,mp) for mp in GROUP))[1]
def extras(base,budget,i=0):
 if i==len(RES):yield base.copy();return
 m=RES[i];cap=min(budget//m.bit_count(),*(9-sum(n for q,n in enumerate(base) if q>>v&1) for v in range(4) if m>>v&1))
 for n in range(max(-1,cap)+1):
  base[m]+=n
  yield from extras(base,budget-n*m.bit_count(),i+1)
  base[m]-=n
st=time.process_time();keys=set()
for aa in product(range(5),repeat=4):
 t=sum(aa)
 if not 14<=t<=16:continue
 ns=[0]*16;ns[3]=ns[12]=1
 for m,n in zip(CROSS,aa):ns[m]=n
 for z in extras(ns,36-4-2*t):
  ds=degree(z)
  if min(ds)<7 or max(ds)>9 or ds.count(7)>1:continue
  if any(sum(n for m,n in enumerate(z) if m&p==p)>4 for p in (3,5,9,6,10,12)):continue
  z[0]=35-sum(z)
  if z[0]<0:continue
  keys.add(tuple(z))
reps={canon(k) for k in keys}
print('profile',len(keys),len(reps),dict(Counter(sum(k[m] for m in CROSS) for k in keys)),flush=True)
out=[]
for ns0 in sorted(reps,key=lambda n:(degree(n),n)):
 ns={m:n for m,n in enumerate(ns0) if n};e=SubsetEngine(21,4,ns);z=e.verify(e.solve())
 out.append(dict(degrees=degree(ns0),counts=ns,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
 assert time.process_time()-st<15,'bounded CPU pilot ceiling'
result={'scope':__doc__,'complete':True,'labeled_keys':[list(k) for k in sorted(keys)],'group_order':8,'representative_keys':[list(k) for k in sorted(reps)],'cases':out,'labels_by_cross_count':dict(Counter(sum(k[m] for m in CROSS) for k in keys)),'nonstrict_ids':[i for i,r in enumerate(out) if not r['strict']],'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print({'labels':len(keys),'orbits':len(reps),'strict':sum(r['strict'] for r in out),'max':str(max(r['bound'] for r in out)),'cpu_seconds':result['cpu_seconds']})
