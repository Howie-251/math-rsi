"""Exact all-order/all-position DP for the joined1469 five-neighbour star profiles.
Each visited fixed witness is replayed by independent labelled-injection A/B/C.
"""
from pathlib import Path
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
source=json.loads((HERE/'STAR_FIVE_DOMAIN.json').read_text())['cases'];start=time.time();out=[]
pilot=[0,7,44,45,90,170,171,300,700,len(source)-1];indices=pilot+[i for i in range(len(source)) if i not in pilot]
for n,idx in enumerate(indices):
 r=source[idx];one=time.time();eng=SubsetEngine(20,6,r['counts']);z=eng.solve();z=eng.verify(z);z.update(r);z.update(source_id=idx,strict=z['bound']<1,dp_seconds=time.time()-one);z.pop('rows',None);out.append(z)
 if n<10 or n%25==24:print(n,idx,r['neighbor_degrees'],z['bound'],z['dp_seconds'],'elapsed',time.time()-start,flush=True)
 stop=False
 if n==9:
  print('pilot_strict',sum(r['strict'] for r in out),'pilot_seconds',time.time()-start,flush=True)
  if sum(r['strict'] for r in out)<5:stop=True
 if (n+1)%100==0 or n==9 or len(out)==len(source) or time.time()-start>145 or stop:
  (HERE/'STAR_FIVE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(source),domain_size=len(source),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>145 or stop:break
print('done',len(out),'strict',sum(r['strict'] for r in out),'domain',len(source),'seconds',time.time()-start)
