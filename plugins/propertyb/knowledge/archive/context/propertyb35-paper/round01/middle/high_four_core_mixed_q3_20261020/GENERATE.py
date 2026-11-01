"""Four high-degree core spectra, exact full-core multiplicity3/4 only."""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(P.parent),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
PM=[sum(1<<i for i in p) for p in combinations(range(4),2)];TM=[7,11,13,14]
SPECTRA=[(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)]
def maps(ds):
 return [[sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)] for p in permutations(range(4)) if all(ds[p[i]]==ds[i] for i in range(4))]
def image(h,mp):
 z=[0]*16
 for m,v in enumerate(h):z[mp[m]]=v
 return tuple(z)
def domain(ds):
 for q in (3,4):
  for tt in product(range(2),repeat=4):
   rem=[4-q-sum(v for m,v in zip(TM,tt) if m&p==p) for p in PM]
   if min(rem)<0:continue
   for pp in product(*(range(r+1) for r in rem)):
    ns={15:q,**dict(zip(TM,tt)),**dict(zip(PM,pp))}
    for i in range(4):ns[1<<i]=ds[i]-sum(v for m,v in ns.items() if m>>i&1)
    ns[0]=35-sum(ns.values())
    if min(ns.values())<0:continue
    cc=[sum(v for m,v in ns.items() if m&p==p) for p in PM]
    if any(sum(v-1 for p,v in zip(PM,cc) if p>>i&1)>4*ds[i]-20 for i in range(4)):continue
    yield tuple(ns.get(m,0) for m in range(16))
st=time.process_time();jobs=[];cases=[]
for ds in SPECTRA:
 mm=maps(ds);keys=set(domain(ds));reps={min(image(k,mp) for mp in mm) for k in keys}
 jobs.append({'degrees':ds,'group_order':len(mm),'label_keys':[list(x) for x in sorted(keys)],'representative_keys':[list(x) for x in sorted(reps)]})
 for ns0 in sorted(reps):
  ns={m:v for m,v in enumerate(ns0) if v};e=SubsetEngine(21,4,ns);z=e.verify(e.solve())
  cases.append(dict(degrees=ds,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
  assert time.process_time()-st<20,'pilot CPU stop'
 print(ds,'labels',len(keys),'orbits',len(reps),'nonstrict',sum(not x['strict'] for x in cases if tuple(x['degrees'])==ds),flush=True)
out={'scope':__doc__,'complete':True,'jobs':jobs,'cases':cases,'nonstrict_ids':[i for i,r in enumerate(cases) if not r['strict']],'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print({'cases':len(cases),'nonstrict':len(out['nonstrict_ids']),'cpu_seconds':out['cpu_seconds']})
