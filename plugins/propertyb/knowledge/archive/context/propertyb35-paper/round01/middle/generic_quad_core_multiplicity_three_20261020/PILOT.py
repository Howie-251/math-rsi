"""Generic four-core multiplicity3/4, degrees7..13/excess4, true selected-L coverage."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations,product
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();PM=tuple(m for m in range(16) if m.bit_count()==2);TM=(7,11,13,14)
SPECTRA=[d for d in combinations_with_replacement(range(7,14),4) if sum(max(x-9,0) for x in d)<=4]

def maps(d):
 return [tuple(sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)) for p in permutations(range(4)) if all(d[p[i]]==d[i] for i in range(4))]
def image(ns,p):
 out=[0]*16
 for m,v in enumerate(ns):out[p[m]]=v
 return tuple(out)
def domain(d):
 for q in (3,4):
  if q==4 and min(d)<8:continue
  for t in (0,*TM) if q==3 else (0,):
   allowed=[m for m in PM if not t or m&t!=m]
   for subset in range(1<<len(allowed)) if q==3 else (0,):
    ns=[0]*16;ns[15]=q
    if t:ns[t]=1
    for j,m in enumerate(allowed):ns[m]=(subset>>j)&1
    if any(sum(v*(m.bit_count()-1) for m,v in enumerate(ns) if 2<=m.bit_count()<=3 and m>>i&1)>4*d[i]-26 for i in range(4)):continue
    for i in range(4):ns[1<<i]=d[i]-sum(v for m,v in enumerate(ns) if m>>i&1)
    ns[0]=35-sum(ns)
    if min(ns)<0:continue
    yield tuple(ns)
jobs=[]
for d in SPECTRA:
 keys=set(domain(d));mm=maps(d);reps=sorted({min(image(k,p) for p in mm) for k in keys})
 jobs.append(dict(degrees=d,group_order=len(mm),label_keys=sorted(keys),representative_keys=reps))
profile=dict(degree_spectra=len(jobs),labeled=sum(len(j['label_keys']) for j in jobs),orbits=sum(len(j['representative_keys']) for j in jobs),q4=sum(k[15]==4 for j in jobs for k in j['label_keys']),q3=sum(k[15]==3 for j in jobs for k in j['label_keys']),generation_cpu=time.process_time()-st)
(P/'DOMAIN.json').write_text(json.dumps(dict(profile=profile,jobs=jobs),indent=2)+'\n');print('DOMAIN',profile,flush=True)
# Mandatory small pilot: all q4 plus maxdegree<=9 q3, then first few10 cases.
queue=[(tuple(j['degrees']),tuple(ns)) for j in jobs for ns in j['representative_keys']]
queue.sort(key=lambda z:(z[1][15]!=4,max(z[0]),z[0],z[1]))
cases=[]
for d,ns in queue:
 e=SubsetEngine(21,4,{m:v for m,v in enumerate(ns) if v});original=e.inv.copy();e.inv={p:(0,0,[]) for p in original}
 z=e.solve();mode='zero'
 if z['bound']>=1:
  e.inv=original;z=e.solve();mode='nested_total_pure'
 cases.append(dict(degrees=d,counts=ns,mode=mode,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
 if z['bound']>=1:
  print('FIRST_NONSTRICT',d,str(z['bound']),mode,'counts',ns,flush=True);break
 if len(cases)%100==0:print('PROGRESS',len(cases),'cpu',time.process_time()-st,flush=True)
 if time.process_time()-st>45:print('CPU_STOP',flush=True);break
out=dict(profile=profile,cases=cases,complete=len(cases)==len(queue),case_count=len(cases),mode_counts=dict(Counter(c['mode'] for c in cases)),max_bound=max(c['bound'] for c in cases),cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print('RESULT',len(cases),len(queue),str(out['max_bound']),out['mode_counts'],out['cpu_seconds'],flush=True)
