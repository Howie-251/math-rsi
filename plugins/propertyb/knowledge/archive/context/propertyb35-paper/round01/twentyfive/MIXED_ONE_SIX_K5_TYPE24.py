"""Only type24's unique real three-point trace edge, 36 new mixed inputs.
Degrees6/7 and6/8 have common degree1 because the six-point is globally unit.
Degrees7/8 have c<=5 from the seven-point's weighted row4; no8/8 case exists.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
mu={int(t):n for t,n in json.loads((P/'GROUP5_CATALOGUE.json').read_text())['representatives'][24]['counts'].items()};parts=[(1,2,28),(3,28)];st=time.perf_counter();out=[]
for d,e in [(6,7),(6,8),(7,8)]:
 for pp,rr in product(parts,repeat=2):
  p={t:1 for t in pp};r={t:1 for t in rr};p[0]=d-len(pp);r[0]=e-len(rr);common=sorted(set(p)&set(r));opts=[[1] if t==28 else range(max(0,p[t]+r[t]-mu[t]),min(p[t],r[t])+1) for t in common]
  for vv in product(*opts):
   q={t:n for t,n in zip(common,vv) if n};lam=sum(q.values())
   if not (lam==1 if d==6 else 1<=lam<=5):continue
   ns={};ok=True
   for t,n in mu.items():
    a=p.get(t,0);b=r.get(t,0);v=q.get(t,0);cells=[n-a-b+v,a-v,b-v,v]
    if min(cells)<0:ok=False;break
    for mask,z in enumerate(cells):
     if z:ns[t+32*mask]=z
   if not ok or any(t.bit_count()>5 for t in ns):continue
   assert sum(ns.values())==35 and all(sum(n for t,n in ns.items() if t>>i&1)==deg for i,deg in enumerate([7]*5+[d,e]))
   assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==(lam if (i,j)==(5,6) else 2 if j<5 else 1) for i in range(7) for j in range(i+1,7))
   eng=SubsetEngine(25,7,ns);w=eng.verify(eng.solve());raw=sum(min(z['A'],z['B'],z['C']) for z in w['rows']);out.append(dict(id=24,degrees=[7]*5+[d,e],P=pp,Q=rr,joint=q,codegree=lam,raw_ABC_bound=raw,**w))
 counts={f'{d}/{e}':sum(z['degrees'][-2:]==[d,e] for z in out) for d,e in [(6,7),(6,8),(7,8)]}
summary=dict(scope=__doc__,cases=len(out),by_degree_pair=counts,strict=sum(z['bound']<1 for z in out),raw_strict=sum(z['raw_ABC_bound']<1 for z in out),maximum_raw=max(z['raw_ABC_bound'] for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_K5_TYPE24.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
