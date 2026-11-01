"""Bounded spread pilot over complete actual four-eight orbit domain. No old triple certificate re-search."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();dom=json.loads((HERE/'DOMAIN.json').read_text());rs=dom['orbits'];ids={round(i*(len(rs)-1)/19) for i in range(20)}
for f in (lambda r:r['counts']['0'],lambda r:sum(r['counts'].get(str(1<<i),0) for i in range(4)),lambda r:r['quadruple'],lambda r:r['pair_energy']):
 ids.add(min(rs,key=f)['id']);ids.add(max(rs,key=f)['id'])
out=[];eng4=Engine(20,4)
for i in sorted(ids):
 r=rs[i];eng=SubsetEngine(20,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1
 if not z['strict']:
  jj=solve_profile(eng4,dict(z,graph='four8pilot',group=i),permutation_limit=24);z['joint']=jj;z['strict']=Q(jj.get('bound','2'))<1
 out.append(z);print(i,z['bound'],z.get('joint',{}).get('bound'),'strict',z['strict'],flush=True)
result=dict(scope=__doc__,sample_count=len(out),fixed_strict=sum(Q(r['bound'])<1 for r in out),after_one_joint_strict=sum(r['strict'] for r in out),domain_orbits=len(rs),cases=out,elapsed_seconds=time.time()-start)
(HERE/'PILOT.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print('sample',len(out),'fixed',result['fixed_strict'],'afterjoint',result['after_one_joint_strict'],'seconds',time.time()-start)
