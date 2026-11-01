"""Selected exclusive2+2 original outeredges; exactcross14, degrees7..13, high-excess4."""
from pathlib import Path
from itertools import product,permutations
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();CROSS=(5,6,9,10);TM=(7,11,13,14)
perms=[p for p in permutations(range(4)) if {frozenset(p[:2]),frozenset(p[2:])}=={frozenset((0,1)),frozenset((2,3))}]
maps=[tuple(sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)) for p in perms]
def image(ns,p):
 out=[0]*16
 for m,v in enumerate(ns):out[p[m]]=v
 return tuple(out)
def deg(ns):return tuple(sum(v for m,v in enumerate(ns) if m>>i&1) for i in range(4))
keys=set();high_shapes=set()
for aa in product(range(5),repeat=4):
 if sum(aa)!=14:continue
 for t in (0,*TM):
  if any(a+int(t&p==p and t!=0)>4 for p,a in zip(CROSS,aa)):continue
  for A,B in product(range(1,5),repeat=2):
   if A+int(t&3==3 and t!=0)>4 or B+int(t&12==12 and t!=0)>4:continue
   base=[0]*16;base[3]=A;base[12]=B
   for m,v in zip(CROSS,aa):base[m]=v
   if t:base[t]=1
   dd=deg(base);high_shapes.add(tuple(base))
   for ss in product(*(range(max(0,7-d),14-d) for d in dd)):
    d=tuple(x+y for x,y in zip(dd,ss))
    if sum(max(x-9,0) for x in d)>4:continue
    ns=base.copy()
    for i,s in enumerate(ss):ns[1<<i]=s
    ns[0]=35-sum(ns)
    if min(ns)<0:continue
    keys.add(tuple(ns))
reps=sorted({min(image(ns,p) for p in maps) for ns in keys})
profile=dict(labels=len(keys),orbits=len(reps),high_shapes=len(high_shapes),by_maxdegree=dict(Counter(max(deg(k)) for k in reps)),generation_cpu=time.process_time()-st)
(P/'DOMAIN.json').write_text(json.dumps(dict(profile=profile,labeled_keys=sorted(keys),representative_keys=reps),indent=2)+'\n');print('DOMAIN',profile,flush=True)
cases=[]
for ns in sorted(reps,key=lambda k:(max(deg(k)),sum(max(d-9,0) for d in deg(k)),deg(k),k)):
 e=SubsetEngine(21,4,{m:v for m,v in enumerate(ns) if v});orig=e.inv.copy();e.inv={p:(0,0,[]) for p in orig};z=e.solve();mode='zero'
 if z['bound']>=1:e.inv=orig;z=e.solve();mode='nested_total_pure'
 cases.append(dict(degrees=deg(ns),counts=ns,positions=z['positions'],mode=mode,bound=z['bound'],strict=z['bound']<1))
 if z['bound']>=1:print('FIRST_NONSTRICT',deg(ns),str(z['bound']),ns,flush=True);break
 if time.process_time()-st>15:print('CPU_STOP',flush=True);break
out=dict(scope=__doc__,profile=profile,complete=len(cases)==len(reps),case_count=len(cases),cases=cases,nonstrict=[c for c in cases if not c['strict']],mode_counts=dict(Counter(c['mode'] for c in cases)),cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print('RESULT',len(cases),len(reps),'cpu',out['cpu_seconds'],out['mode_counts'],flush=True)
