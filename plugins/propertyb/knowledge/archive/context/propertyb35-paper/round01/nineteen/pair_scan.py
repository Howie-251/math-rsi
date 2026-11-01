from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,double
from fractions import Fraction
out=[]
for a in [8,9]:
 for b in range(a,14):
  for c in range(1,a+1):
   ns=double(19,a,b,c)
   if min(ns.values())<0:continue
   poss=[(1,2),(1,11),(11,1),(7,8),(8,7),(8,9),(9,8),(9,10),(10,9),(10,11),(11,10),(1,10),(10,1)]
   z=min((evaluate(19,ns,p) for p in poss),key=lambda z:z['bound'])
   out.append(dict(d=[a,b],c=c,bound=str(z['bound']),pos=z['positions'],strict=z['bound']<1))
print(json.dumps(out,indent=2))
(ROOT/'context/propertyb35-paper/round01/nineteen/PAIR_SCAN.json').write_text(json.dumps(out,indent=2)+'\n')
