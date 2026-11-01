"""Only three genuinely new triple projections when joining {low1,low2,y,z} and {low1,low2,y,w}:
{low1,z,w},{low2,z,w},{y,z,w}. Canonicalize by actual permutations preserving degree labels.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();dom=json.loads((HERE/'R2_THREE_DOMAIN.json').read_text());seen={};projs=[];maps=[]
for r in dom['orbits']:
 ids=[]
 for i in range(3):
  old=(i,3,4);degrees=tuple(sorted(r['degrees'][j] for j in old));ns={int(t):n for t,n in r['counts'].items()};best=None;bestorder=None
  for order in permutations(old):
   if tuple(r['degrees'][j] for j in order)!=degrees:continue
   vv=[0]*8
   for t,n in ns.items():vv[sum(1<<j for j,k in enumerate(order) if t>>k&1)]+=n
   if best is None or tuple(vv)<best:best=tuple(vv);bestorder=order
  key=(degrees,best)
  if key not in seen:
   seen[key]=len(projs);projs.append(dict(id=len(projs),degrees=degrees,counts={t:n for t,n in enumerate(best) if n}))
  ids.append(dict(id=seen[key],new_order=bestorder))
 maps.append(dict(source_id=r['id'],projections=ids))
print('distinct new projections',len(projs),'seconds',time.time()-start,flush=True)
out=[];eng3=Engine(20,3)
for r in projs:
 eng=SubsetEngine(20,3,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1
 if not z['strict']:
  jj=solve_profile(eng3,dict(z,graph='r2newproj',group=r['id']),permutation_limit=6);z['joint']=jj;z['strict']=Q(jj.get('bound','2'))<1
 out.append(z)
(HERE/'R2_NEW_PROJECTIONS.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=out,maps=maps,elapsed_seconds=time.time()-start)),indent=2)+'\n');strict={r['id'] for r in out if r['strict']};keep={r['source_id'] for r in maps if not any(p['id'] in strict for p in r['projections'])};filtered=[r for r in dom['orbits'] if r['id'] in keep]
(HERE/'R2_THREE_FILTERED_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,unfiltered_orbits=len(dom['orbits']),projection_strict=len(strict),orbits=filtered,orbit_count=len(filtered),elapsed_seconds=time.time()-start)),indent=2)+'\n');print('projection strict',len(strict),'remaining',len(filtered),'seconds',time.time()-start,flush=True)
if len(filtered)>3000:print('remaining exceeds small pilot budget; no DP',flush=True);sys.exit(0)
vals=[]
for r in filtered:
 eng=SubsetEngine(20,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;vals.append(z)
 if time.time()-start>65:break
(HERE/'R2_THREE_FILTERED_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(vals)==len(filtered),cases=vals,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(vals),'strict',sum(r['strict'] for r in vals),'seconds',time.time()-start,flush=True)
joints=[];eng5=Engine(20,5)
for r in vals:
 if r['strict']:continue
 jj=solve_profile(eng5,dict(r,graph='r2filtered',group=r['id']),permutation_limit=120);jj['source_id']=r['id'];joints.append(jj)
 print('joint',r['id'],r['degrees'],r['bound'],'->',jj.get('bound',jj.get('status')),flush=True)
 if time.time()-start>80:break
(HERE/'R2_THREE_FILTERED_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
