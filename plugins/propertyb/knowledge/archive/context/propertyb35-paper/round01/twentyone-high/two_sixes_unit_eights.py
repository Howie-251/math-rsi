"""Two degree6 points codegree3, plus two actual degree8 common unit points; all xy+z triples zero."""
from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();out=[]
for c in range(1,5):
 for a,b in itertools.product((0,1),repeat=2):
  inc={0:35,1:6,2:6,4:8,8:8,3:3,5:1,9:1,6:1,10:1,12:c,7:0,11:0,13:a,14:b,15:0};ns={}
  for m in sorted(range(16),key=int.bit_count,reverse=True):ns[m]=inc[m]-sum(n for t,n in ns.items() if t&m==m)
  if min(ns.values())<0:continue
  eng=SubsetEngine(21,4,ns);z=eng.verify(eng.solve());z.update(degrees=[6,6,8,8],partner_codegree=c,triples=[0,0,a,b],four=0,strict=z['bound']<1);out.append(z)
(HERE/'TWO_SIXES_UNIT_EIGHTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-st)
for z in out:
 if not z['strict']:print('residual',z['partner_codegree'],z['triples'],z['bound'])
