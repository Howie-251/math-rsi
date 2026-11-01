"""Finish modest385 actual four-eight orbit domain, reusing all23 pilot fixed and joint results."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();dom=json.loads((HERE/'DOMAIN.json').read_text());pilot={r['id']:r for r in json.loads((HERE/'PILOT.json').read_text())['cases']};out=[]
for r in dom['orbits']:
 if r['id'] in pilot:z=pilot[r['id']];z['bound']=Q(z['bound']);z['strict']=z['bound']<1
 else:eng=SubsetEngine(20,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1
 out.append(z)
(HERE/'FOUR_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,pilot_fixed_reused=len(pilot),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
joints=[];eng4=Engine(20,4)
for r in out:
 if r['strict']:continue
 if r.get('joint'):jj=r['joint']
 else:jj=solve_profile(eng4,dict(r,graph='four8all',group=r['id']),permutation_limit=24)
 jj['source_id']=r['id'];joints.append(jj)
 print('joint',r['id'],jj.get('bound',jj.get('status')),flush=True)
(HERE/'FOUR_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');strictjoint={r['source_id'] for r in joints if Q(r.get('bound','2'))<1};res=[r for r in out if not r['strict'] and r['id'] not in strictjoint]
(HERE/'FOUR_REMAINDERS.json').write_text(json.dumps(json_value(dict(scope='Actual four-eight profiles not yet strict after complete fixed DP and one bounded joint.',count=len(res),cases=res,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',len(strictjoint),'of',len(joints),'residual',len(res),'seconds',time.time()-start)
