"""18 spread samples of330 shared five-unit8 inventories, center7/n21/M35."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();rs=json.loads((HERE/'DOMAIN.json').read_text())['orbits'];ids={round(i*(len(rs)-1)/17) for i in range(18)};out=[]
for i in sorted(ids):
 r=rs[i];en=SubsetEngine(21,6,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1;out.append(z);print(i,z['bound'],z['strict'],flush=True)
(HERE/'PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,domain_count=len(rs),sample_count=len(out),fixed_strict=sum(z['strict'] for z in out),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('strict',sum(z['strict'] for z in out),'of',len(out),'seconds',time.time()-st)
