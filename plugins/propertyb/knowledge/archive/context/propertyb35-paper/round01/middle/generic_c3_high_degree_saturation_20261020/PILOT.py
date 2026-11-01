"""Marked A/B near-saturation domain t>=15, selected positive excess above9 <=4."""
from pathlib import Path
from itertools import product, permutations
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent; ROOT=P.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
from independent_structure_bounds import independent_rows
from fractions import Fraction
st=time.process_time();CROSS=(5,9,6,10)
def ds(ns):return tuple(sum(v for m,v in enumerate(ns) if m>>i&1) for i in range(4))
perms=[p for p in permutations(range(4)) if {frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))}]
def image(ns,p):
 out=[0]*16
 for m,v in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=v
 return tuple(out)
def canonical(ns):return min(image(ns,p) for p in perms)
keys=set()
for aa in product(range(5),repeat=4):
 if sum(aa)<15:continue
 for A,B in product(range(1,5),repeat=2):
  base=[0]*16;base[3]=A;base[12]=B
  for m,v in zip(CROSS,aa):base[m]=v
  dd=ds(base)
  for ss in product(*(range(14-d) for d in dd)):
   degrees=tuple(d+s for d,s in zip(dd,ss))
   if sum(max(d-9,0) for d in degrees)>4:continue
   ns=base.copy()
   for i,s in enumerate(ss):ns[1<<i]=s
   ns[0]=35-sum(ns)
   if ns[0]<0:continue
   keys.add(tuple(ns))
reps=sorted({canonical(k) for k in keys})
profile={'labels':len(keys),'orbits':len(reps),'by_t':dict(Counter(sum(k[m] for m in CROSS) for k in keys)),'by_maxdegree':dict(Counter(max(ds(k)) for k in reps)),'generation_cpu':time.process_time()-st}
print(profile,flush=True)
(P/'PROFILE.json').write_text(json.dumps(profile,indent=2)+'\n')
cases=[]
# Pilot degree<=10 first, then all if bounded. Every solve explicitly zero quota.
for ns in sorted(reps,key=lambda k:(max(ds(k)),ds(k),k)):
 e=SubsetEngine(21,4,{m:v for m,v in enumerate(ns) if v})
 e.inv={p:(0,0,[]) for p in e.inv}
 z=e.solve()
 stubs=[frozenset(i+1 for i in range(4) if m>>i&1) for m,n in enumerate(ns) for _ in range(n)]
 ir=independent_rows(21,tuple(z['positions']),stubs)
 val=sum(min(r['A'],r['B'],r['C']) for r in ir)
 assert val==z['bound'] and len(stubs)==35
 cases.append({'counts':list(ns),'degrees':ds(ns),'positions':z['positions'],'bound':val,'strict':val<1})
 if val>=1:
  print('FIRST_NONSTRICT',ds(ns),str(val),z['positions'],flush=True)
  break
 if time.process_time()-st>40:break
out={'scope':__doc__,'profile':profile,'complete_probability':len(cases)==len(reps),'labeled_keys':[list(k) for k in sorted(keys)],'representative_keys':[list(k) for k in reps],'cases':cases,'max_bound':max(c['bound'] for c in cases),'nonstrict':[i for i,c in enumerate(cases) if not c['strict']],'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
print('RESULT',len(cases),len(reps),str(out['max_bound']),out['cpu_seconds'],flush=True)
