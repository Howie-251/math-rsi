"""Actual stronger r2 selection: c2 gives two Q points w<=1; c3 gives three.
Use all three overlapping four-views from R2_TWO before any five-lock DP.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();r=json.loads((HERE/'R2_THREE_FILTERED_DOMAIN.json').read_text())['orbits'];dom=json.loads((HERE/'R2_TWO_DOMAIN.json').read_text());dp=json.loads((HERE/'R2_TWO_DP.json').read_text())['cases'];jo={x['source_id']:x for x in json.loads((HERE/'R2_TWO_JOINT.json').read_text())['results']}
res={x['id'] for x in dp if not x['strict'] and Q(jo[x['id']].get('bound','2'))>=1}
keys={(tuple(x['degrees']),tuple(x['counts'].get(str(t),0) for t in range(16))) for x in dom['labelled'] if x['orbit'] in res};keep=[];maps=[]
for x in r:
 n={int(t):v for t,v in x['counts'].items()};c=sum(v for t,v in n.items() if t&3==3);w=[sum(v*((t&3).bit_count()) for t,v in n.items() if t&b)-2 for b in (4,8,16)]
 if c==2 and min(w[1:])>1:continue
 if c==3 and max(w)>1:continue
 if c>=2:
  found=None
  for pair in ((3,4),(4,3)):
   if w[pair[0]-2]>1:continue
   vv=[0]*16
   for t,v in n.items():vv[(t&3)|sum(1<<(j+2) for j,k in enumerate(pair) if t>>k&1)]+=v
   if (tuple([7,7]+[x['degrees'][k] for k in pair]),tuple(vv)) in keys:found=pair;break
  if found is None:continue
  maps.append(dict(source_id=x['id'],last_view_order=found))
 keep.append(x)
(HERE/'R2_THREE_STRONG_FILTER.json').write_text(json.dumps(json_value(dict(scope=__doc__,orbits=keep,orbit_count=len(keep),last_view_maps=maps,by_low_codegree=dict(Counter(sum(v for t,v in x['counts'].items() if int(t)&3==3) for x in keep)))),indent=2)+'\n')
selected=[x for x in keep if sum(v for t,v in x['counts'].items() if int(t)&3==3)>=2];print('c2/c3 selected',len(selected),'seconds',time.time()-start,flush=True)
out=[]
for x in selected:
 eng=SubsetEngine(20,5,x['counts']);z=eng.verify(eng.solve());z.update(x);z['strict']=z['bound']<1;out.append(z)
 if time.time()-start>60:break
(HERE/'R2_C23_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(selected),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(x['strict'] for x in out),'seconds',time.time()-start,flush=True)
joints=[];eng5=Engine(20,5)
for x in out:
 if x['strict']:continue
 jj=solve_profile(eng5,dict(x,graph='r2c23',group=x['id']),permutation_limit=120);jj['source_id']=x['id'];joints.append(jj)
 print('joint',x['id'],x['degrees'],x['bound'],'->',jj.get('bound',jj.get('status')),flush=True)
 if time.time()-start>80:break
(HERE/'R2_C23_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
