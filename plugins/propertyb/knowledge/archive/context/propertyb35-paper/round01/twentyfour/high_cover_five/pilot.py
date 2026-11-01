"""Few fixed-DP witnesses on the complete81-orbit actual high-cover domain, n24/M35."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();rs=json.loads((HERE/'DOMAIN.json').read_text())['orbits'];ids=set()
for ds in ((10,8,8,8,8),(9,9,8,8,8)):
 ss=[r for r in rs if tuple(r['degrees'])==ds]
 ids.update(ss[round(i*(len(ss)-1)/5)]['id'] for i in range(6))
 for cat in ('three_pairs','triple_pair','quadruple'):ids.add(next(r['id'] for r in ss if r['category']==cat))
out=[]
for i in sorted(ids):
 r=rs[i];en=SubsetEngine(24,5,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1;out.append(z);print(i,r['degrees'],r['category'],z['bound'],z['strict'],flush=True)
(HERE/'PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,domain_orbits=len(rs),cases=out,fixed_strict=sum(r['strict'] for r in out),sample_count=len(out),elapsed_seconds=time.time()-st)),indent=2)+'\n');print('fixedstrict',sum(r['strict'] for r in out),'of',len(out),'seconds',time.time()-st)
