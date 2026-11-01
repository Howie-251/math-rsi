"""Three actual degree6 points have inclusive triple2; add two common unit neighbours of degree7/8."""
from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();out=[]
for d,e in [(7,7),(7,8),(8,8)]:
 for c in range(1,4 if d==7 else 5):
  for gs in itertools.product((0,1),repeat=3):
   ds=[6,6,6,d,e];inc={m:0 for m in range(32)};inc[0]=35
   for i,z in enumerate(ds):inc[1<<i]=z
   for i,j in itertools.combinations(range(5),2):inc[(1<<i)|(1<<j)]=2 if j<3 else c if i==3 else 1
   inc[7]=2
   for i,g in enumerate(gs):inc[(1<<i)|24]=g
   ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(32)}
   if min(ns.values())<0:continue
   eng=SubsetEngine(21,5,ns);z=eng.verify(eng.solve());z.update(degrees=ds,partner_codegree=c,single_low_triples=gs,strict=z['bound']<1);out.append(z)
 rr=[z for z in out if z['degrees'][3:]==[d,e]];print((d,e),'domain',len(rr),'strict',sum(z['strict'] for z in rr),'max',max(z['bound'] for z in rr),flush=True)
 for z in rr:
  if not z['strict']:print('residual',z['partner_codegree'],z['single_low_triples'],z['bound'])
(HERE/'THREE_SIXES_FIVE_T2.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
