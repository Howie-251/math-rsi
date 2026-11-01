from pathlib import Path
import sys,itertools,json
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,triple
out=[]
for d in [(9,9,b) for b in range(10,14)]+[(8,8,b) for b in range(9,14)]+[(8,a,b) for a in [9,10] for b in [9,10]]:
 for ab in range(1,4):
  for ac in range(1,4):
   for bc in range(1,4):
    for t in range(min(ab,ac,bc)+1):
     ns=triple(19,d,(ab,ac,bc),t)
     if min(ns.values())<0:continue
     poss=set(tuple(range(k,k+3)) for k in range(1,18))
     poss|={(1,11,12),(11,1,12),(11,12,1),(1,2,11),(1,11,2),(11,1,2)}
     z=min((evaluate(19,ns,p) for p in poss),key=lambda z:z['bound'])
     out.append(dict(d=d,c=[ab,ac,bc],t=t,bound=str(z['bound']),pos=z['positions'],strict=z['bound']<1))
(ROOT/'context/propertyb35-paper/round01/nineteen/MIXED_SCAN.json').write_text(json.dumps(out,indent=2)+'\n')
for b in range(10,14):
 print('9 9',b)
 for c in itertools.product(range(1,4),range(2,4),range(2,4)):
  if c[1]>c[2]:continue
  rs=[r for r in out if r['d']==(9,9,b) and r['c']==list(c)]
  print(c,[(r['t'],r['bound']) for r in rs], 'allpass',all(r['strict'] for r in rs))
