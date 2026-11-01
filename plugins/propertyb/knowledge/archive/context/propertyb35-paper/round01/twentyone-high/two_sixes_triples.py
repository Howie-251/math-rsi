"""Complete triples with two degree6 points and a degree7/8/9 partner after strong double exclusions."""
from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from pilot import triple,json_value
from subset_position_dp import SubsetEngine
st=time.time();out=[]
for d in [7,8,9]:
 for xy in [1,2,3]:
  for a in range(1,4):
   for b in range(a,4):
    if xy-1+max(a,b)-1>4:continue
    for t in range(min(xy,a,b)+1):
     ns=triple(21,[6,6,d],[xy,a,b],t)
     if min(ns.values())<0:continue
     eng=SubsetEngine(21,3,ns);z=eng.verify(eng.solve());z.update(degrees=[6,6,d],codegrees=[xy,a,b],triple=t,strict=z['bound']<1);out.append(z)
 rr=[z for z in out if z['degrees'][2]==d];print(d,'profiles',len(rr),'strict',sum(z['strict'] for z in rr),flush=True)
 for xy in [1,2,3]:print('xy',xy,'residual',[(z['codegrees'][1:],z['triple'],str(z['bound'])) for z in rr if z['codegrees'][0]==xy and not z['strict']],flush=True)
(HERE/'TWO_SIXES_TRIPLES.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
