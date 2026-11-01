"""Actual c1 branch with >=2 Q points w<=1. Reuse the genuine common 3-view filtered domain, no repeated layout inputs."""
from pathlib import Path
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();refs=json.loads((HERE/'R2_C1_MULTIPLE_SMALL_DOMAIN.json').read_text())['references'];ids={x['source_id'] for x in refs};selected=[x for x in json.loads((HERE/'R2_THREE_DOMAIN.json').read_text())['orbits'] if x['id'] in ids];out=[]
for x in selected:
 eng=SubsetEngine(20,5,x['counts']);z=eng.verify(eng.solve());z.update(x);z['strict']=z['bound']<1;out.append(z)
(HERE/'R2_C1_MULTIPLE_SMALL_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(ids),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(x['strict'] for x in out),'seconds',time.time()-start,flush=True)
joints=[];eng5=Engine(20,5)
for x in out:
 if x['strict']:continue
 jj=solve_profile(eng5,dict(x,graph='r2c1multi',group=x['id']),permutation_limit=120);jj['source_id']=x['id'];joints.append(jj)
 print('joint',x['id'],x['degrees'],x['bound'],'->',jj.get('bound',jj.get('status')),flush=True)
 if time.time()-start>25:break
(HERE/'R2_C1_MULTIPLE_SMALL_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
