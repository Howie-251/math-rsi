import importlib.util,json,time,itertools,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('cert',ROOT/'propertyB_small_k/propertyB_m6_certificate.py'); c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.M=65
OUT=Path(__file__).resolve().parent
start=time.process_time()
def unlocked(v):
 q=c.ceilings(65*15-c.C(v,2),10);gamma=65*64-2*q
 return sum(min(F(390,v)*F(c.C(h-1,5),c.C(v-1,5)),F(390,v)*F(c.C(v-h,5),c.C(v-1,5)),gamma*F(c.C(h-1,5)*c.C(v-h,5),v*c.C(v-1,5)*c.C(v-6,5))) for h in range(1,v+1))
rows=[]
def record(v,kind,ds,tri,u,pos):
 rows.append(dict(v=v,kind=kind,degrees=ds,tri=tri,positions=pos,U=str(u),approx=float(u),pass_strict=u<1))
# Complete structural domain for the declared partition below.
for v in range(27,34):record(v,'zero',[],None,unlocked(v),[])
for v in (34,35,36):
 for d in range(c.ceilings(v-1,5),min(9 if v!=34 else 11,390//v)+1):record(v,'one',[d],None,c.one(v,d),[v//2])
for v in (35,36):
 for d in range(10,390//v+1):
  excess=5*d-(v-1)
  # Smallest t for which all codegree-one neighbors degree>=t+1 contradict total budget.
  t=next(t for t in range(d,66) if d+(v-1-excess)*(t+1)+excess*d>390)
  assert d+(v-1-excess)*(t+1)+excess*d>390
  for e in range(d,t+1):record(v,'two',[d,e],None,c.two(v,d,e),[v//2,v//2+1])
for v in (37,):
 for d in range(c.ceilings(v-1,5),390//v+1):
  excess=5*d-(v-1)
  t=next(t for t in range(d,66) if d+(v-1-excess)*(t+1)+excess*d>390)
  for e in range(d,t+1):record(v,'two',[d,e],None,c.two(v,d,e),[v//2,v//2+1])
for v in range(38,42):
 d0=c.ceilings(v-1,5);rmin=c.ceilings(12*v-390,12-d0)
 for r in range(rmin,v+1):
  u2e=(61-v)*r+1950-60*v
  assert u2e>=0 and r*r>2*(r+u2e),(v,r,u2e)
 for ds in itertools.combinations_with_replacement(range(d0,12),3):
  for tri in (0,1):record(v,'three',list(ds),tri,c.three(v,ds,tri),[v//2-1,v//2,v//2+1])
for v in (42,43):
 nine= v-(390-9*v); excess=45-(v-1)
 assert c.ceilings(nine,excess+1)>=3
 for tri in (0,1):record(v,'three',[9]*3,tri,c.three(v,[9]*3,tri),[v//2-1,v//2,v//2+1])
assert 43*c.ceilings(42,5)<=390<44*c.ceilings(43,5)
assert all(65*F(c.C(v//2,6)+c.C(v-v//2,6),c.C(v,6))<1 for v in range(11,27))
result=dict(M=65,domain='complete necessary profile domain for stated 0-3-lock partition',profiles=len(rows),failures=[r for r in rows if not r['pass_strict']],rows=rows,cpu_seconds=time.process_time()-start)
(OUT/'baseline.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
