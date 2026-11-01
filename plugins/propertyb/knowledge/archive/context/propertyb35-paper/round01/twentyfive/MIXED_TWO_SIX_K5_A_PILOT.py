"""CaseA: degree spectrum6^2,9,7^22, one actual seven-degree K5 group.
Only forced positive-trace/special-pair inputs:42 new inputs. Every six-degree
point is globally unit, and7/9 codegree<=5 uses the seven-degree endpoint.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True;sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());st=time.perf_counter();cases=[]
def restore(ident,ds,p,r=None,q=None):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};x={t:1 for t in p};x[0]=ds[5]-len(p);ns={}
 if r is None:
  for t,n in mu.items():
   a=x.get(t,0);assert 0<=a<=n
   if n-a:ns[t]=n-a
   if a:ns[t+32]=a
 else:
  y={t:1 for t in r};y[0]=ds[6]-len(r);q=q or {}
  for t,n in mu.items():
   a=x.get(t,0);b=y.get(t,0);c=q.get(t,0);cells=[n-a-b+c,a-c,b-c,c]
   if min(cells)<0:return None
   for mask,v in enumerate(cells):
    if v:ns[t+32*mask]=v
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(ds))
 for i in range(len(ds)):
  for j in range(i+1,len(ds)):
   lam=sum(n for t,n in ns.items() if t>>i&1 and t>>j&1);assert lam==(sum(q.values()) if (i,j)==(5,6) else 2 if j<5 else 1)
   if ds[i]==6 or ds[j]==6:assert lam==1
 return ns
for d,e in [(6,6),(6,9)]:
 for p,r in [([5,26],[3,28]),([3,28],[5,26])]:
  ds=[7]*5+[d,e];q={0:1};cases.append(dict(id=12,degrees=ds,P=p,Q=r,joint=q,counts=restore(12,ds,p,r,q)))
ds=[7]*5+[9];cases.append(dict(id=25,degrees=ds,P=[1,30],counts=restore(25,ds,[1,30])))
ds=[7]*5+[6,6];cases.append(dict(id=26,degrees=ds,P=[1,8,22],Q=[1,8,22],joint={22:1},counts=restore(26,ds,[1,8,22],[1,8,22],{22:1})))
mu={int(t):n for t,n in cat['representatives'][24]['counts'].items()};parts=[(1,2,28),(3,28)]
for d,e in [(6,6),(6,9),(7,9)]:
 for pp,rr in product(parts,repeat=2):
  p={t:1 for t in pp};r={t:1 for t in rr};p[0]=d-len(pp);r[0]=e-len(rr);common=sorted(set(p)&set(r));ranges=[[1] if t==28 else range(max(0,p[t]+r[t]-mu[t]),min(p[t],r[t])+1) for t in common]
  for nums in product(*ranges):
   q={t:n for t,n in zip(common,nums) if n};lam=sum(q.values())
   if not (lam==1 if d==6 else 1<=lam<=5):continue
   ds=[7]*5+[d,e];ns=restore(24,ds,pp,rr,q)
   if ns is not None:cases.append(dict(id=24,degrees=ds,P=pp,Q=rr,joint=q,counts=ns))
assert len(cases)==42
out=[]
for z in cases:
 ns=z['counts'];s=len(z['degrees']);eng=SubsetEngine(25,s,ns);w=eng.verify(eng.solve());raw=sum(min(r['A'],r['B'],r['C']) for r in w['rows']);out.append(dict(**{k:v for k,v in z.items() if k!='counts'},raw_ABC_bound=raw,**w))
summary=dict(scope=__doc__,cases=len(out),raw_strict=sum(z['raw_ABC_bound']<1 for z in out),corrected_strict=sum(z['bound']<1 for z in out),maximum_raw=max(z['raw_ABC_bound'] for z in out),by_type=[dict(id=i,cases=sum(z['id']==i for z in out),maximum_raw=max(z['raw_ABC_bound'] for z in out if z['id']==i)) for i in [12,24,25,26]],elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_TWO_SIX_K5_A_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
