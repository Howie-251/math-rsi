"""All labelled orders/positions DP for the actual four-neighbour373-profile domain.
DP proposals are replayed by independent injection counts for saved witnesses.
"""
from pathlib import Path
import sys,json,time
from fractions import Fraction as Q
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
source=json.loads((HERE/'STAR_FOUR_DOMAIN.json').read_text())['cases'];start=time.time();out=[]
indices=list(range(len(source)))
# First10 span all currently nonempty degree patterns, then finish the same domain.
pilot=[0,1,7,13,14,40,100,181,182,300]
indices=pilot+[i for i in indices if i not in pilot]
for n,idx in enumerate(indices):
 r=source[idx];one=time.time();eng=SubsetEngine(20,5,r['counts']);z=eng.solve();z=eng.verify(z);z.update(r);z.update(source_id=idx,strict=z['bound']<1,dp_seconds=time.time()-one);out.append(z)
 print(n,idx,r['neighbor_degrees'],z['bound'],z['dp_seconds'],flush=True)
 (HERE/'STAR_FOUR_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(source),domain_size=len(source),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if n==9:
  print('pilot_strict',sum(r['strict'] for r in out),'pilot_seconds',time.time()-start,flush=True)
  if sum(r['strict'] for r in out)<5:break
 if time.time()-start>150:break
print('done',len(out),'strict',sum(r['strict'] for r in out),'domain',len(source),'seconds',time.time()-start)
