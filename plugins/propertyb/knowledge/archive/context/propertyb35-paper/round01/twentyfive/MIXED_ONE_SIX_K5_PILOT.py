"""Five genuinely forced mixed-degree inputs for one seven-degree K5 group.
Outside degree6 is globally unit; the other special point has degree8.
No full mixed-domain expansion and no assumption of an8/8 pair bound.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());st=time.perf_counter();cases=[]
def single(ident,d,pp):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};ns=Counter()
 for t,n in mu.items():
  p=int(t in pp) if t else d-len(pp);assert 0<=p<=n
  ns[t]+=n-p;ns[t+32]+=p
 return {t:n for t,n in ns.items() if n}
def pair(ident,d,e,pp,rr,q):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};ns=Counter()
 for t,n in mu.items():
  a=int(t in pp) if t else d-len(pp);b=int(t in rr) if t else e-len(rr);c=q.get(t,0);vv=[n-a-b+c,a-c,b-c,c];assert min(vv)>=0
  for mask,z in zip([t,t+32,t+64,t+96],vv):ns[mask]+=z
 return {t:n for t,n in ns.items() if n}
for d in [6,8]:cases.append(dict(label=f'25-four-trace-degree{d}',id=25,degrees=[7]*5+[d],partition=[1,30],counts=single(25,d,[1,30])))
for pp,rr in [([5,26],[3,28]),([3,28],[5,26])]:cases.append(dict(label=f'12-special-pair-{pp[0]}',id=12,degrees=[7]*5+[6,8],P=pp,Q=rr,joint={0:1},counts=pair(12,6,8,pp,rr,{0:1})))
cases.append(dict(label='26-triple-six-seven',id=26,degrees=[7]*5+[6,7],P=[1,8,22],Q=[1,8,22],joint={22:1},counts=pair(26,6,7,[1,8,22],[1,8,22],{22:1})))
out=[]
for z in cases:
 ns=z['counts'];s=len(z['degrees']);assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(z['degrees']))
 assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(s) for j in range(i+1,s))
 tm=time.perf_counter();eng=SubsetEngine(25,s,ns);w=eng.verify(eng.solve());raw=sum(min(rr['A'],rr['B'],rr['C']) for rr in w['rows']);out.append(dict(**{k:v for k,v in z.items() if k!='counts'},raw_ABC_bound=raw,seconds=time.perf_counter()-tm,**w));print(z['label'],w['bound'],raw,out[-1]['seconds'],flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),raw_strict=sum(z['raw_ABC_bound']<1 for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_K5_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(summary,indent=2))
