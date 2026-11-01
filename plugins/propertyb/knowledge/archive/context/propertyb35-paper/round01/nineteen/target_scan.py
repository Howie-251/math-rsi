from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,double,triple
rs=[]
for a,b in [(10,10),(10,11),(10,12),(11,11)]:
 for c in range(1,min(a,b)+1):
  ns=double(19,a,b,c)
  p=[(1,2),(1,11),(11,1),(10,11),(11,10),(1,10),(10,1)]
  z=min((evaluate(19,ns,x) for x in p),key=lambda z:z['bound'])
  rs.append(dict(d=[a,b],c=c,bound=str(z['bound']),pos=z['positions'],strict=z['bound']<1))
print('pairs',[(r['d'],r['c'],r['bound']) for r in rs if r['strict']])
start=time.time()
for d,c,t in [([9,9,11],[1,2,3],0),([9,9,13],[1,3,3],0),([9,9,11],[2,2,2],0)]:
 ns=triple(19,d,c,t)
 z=min((evaluate(19,ns,p) for p in itertools.permutations(range(1,20),3) if p[0]<p[1]),key=lambda z:z['bound'])
 rs.append(dict(d=d,c=c,t=t,bound=str(z['bound']),pos=z['positions'],strict=z['bound']<1,full=True))
 print('full',rs[-1],time.time()-start,flush=True)
(ROOT/'context/propertyb35-paper/round01/nineteen/TARGET_SCAN.json').write_text(json.dumps(rs,indent=2)+'\n')
