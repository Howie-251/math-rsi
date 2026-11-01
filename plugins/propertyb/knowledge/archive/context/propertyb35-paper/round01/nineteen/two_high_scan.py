from pathlib import Path
import sys,json,itertools
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,triple
out=[]
for ab,ac in [(2,2),(2,3),(3,3)]:
 for t in range(min(ab,ac,3)+1):
  d=[9,11,11];c=[ab,ac,3];ns=triple(19,d,c,t)
  if min(ns.values())<0:continue
  ps=set(itertools.permutations(range(1,20),3))
  z=min((evaluate(19,ns,p) for p in ps if p[1]<p[2]),key=lambda z:z['bound'])
  r=dict(d=d,c=c,t=t,bound=str(z['bound']),pos=z['positions'],strict=z['bound']<1)
  out.append(r);print(r,flush=True)
(ROOT/'context/propertyb35-paper/round01/nineteen/TWO_HIGH_SCAN.json').write_text(json.dumps(out,indent=2)+'\n')
