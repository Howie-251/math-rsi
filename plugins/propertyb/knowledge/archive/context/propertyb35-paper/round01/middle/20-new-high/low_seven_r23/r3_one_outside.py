"""r7=3 actual three-low inventory plus selected8/9 outsider of total low-excess<=3/2.
Old-trace capacity expansion, common projected low-low-outsider triples, true S3 orbits.
"""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();pr=json.loads((HERE/'PROJECTIONS.json').read_text())['cases'];lookup={(r['low_codegree'],r['degree'],*r['cross'],r['triple']):r['strict'] for r in pr}
base0=json.loads((HERE/'THREE_LOW_BASE.json').read_text())['cases'];bases={}
for r in base0:
 for perm in permutations(range(3)):
  ns={sum(1<<perm[i] for i in range(3) if t>>i&1):n for t,n in ((int(t),n) for t,n in r['counts'].items())}
  bases[tuple(ns.get(t,0) for t in range(8))]=ns
assert len(bases)==17
seen={};orbits=[];labelled=[];lowpairs=list(combinations(range(3),2))
for base_id,ns in enumerate(bases.values()):
 cs=[sum(n for t,n in ns.items() if t&m==m) for m in (3,5,6)];W=sum(c-1 for c in cs);budget=(27-2*W)//8;ts=[t for t,n in ns.items() if t and n]
 for ps in product(*(range(min(ns[t],3)+1) for t in ts)):
  promoted=dict(zip(ts,ps));lam=[sum(p for t,p in promoted.items() if t>>i&1) for i in range(3)]
  if any(c<1 or c>3 for c in lam) or sum(lam)-3>budget:continue
  taus=[sum(p for t,p in promoted.items() if t&m==m) for m in (3,5,6)]
  for d in (8,9):
   if any(lookup[(c,d,lam[i],lam[j],t)] for (i,j),c,t in zip(lowpairs,cs,taus)):continue
   p0=d-sum(ps)
   if not 0<=p0<=ns.get(0,0):continue
   new={0:ns[0]-p0,8:p0}
   for t,n in ns.items():
    if not t:continue
    p=promoted.get(t,0);new[t]=n-p;new[t|8]=p
   key=tuple(new.get(t,0) for t in range(16))
   if key in seen:idx,perm=seen[key]
   else:
    idx=len(orbits);orbits.append(dict(id=idx,degree=d,counts=new,base_counts=ns,codegrees=lam,total_excess=sum(lam)-3,excess_budget=budget,promoted=promoted,promoted_empty=p0,labelled_count=0))
    for perm in permutations(range(3)):
     move=lambda t:(t&8)|sum(1<<perm[i] for i in range(3) if t>>i&1)
     moved={move(t):n for t,n in new.items()};seen[tuple(moved.get(t,0) for t in range(16))]=(idx,perm)
    idx,perm=seen[key]
   orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=new,orbit=idx,from_representative_permutation=perm))
result=dict(scope=__doc__,base_labelled_count=17,orbit_count=len(orbits),labelled_count=len(labelled),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)
(HERE/'R3_ONE_DOMAIN.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
out=[]
for r in orbits:
 eng=SubsetEngine(20,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
(HERE/'R3_ONE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
joints=[];eng4=Engine(20,4)
for r in out:
 if r['strict']:continue
 z=solve_profile(eng4,dict(r,graph='r3one',group=r['id']),permutation_limit=24);z['source_id']=r['id'];joints.append(z)
 print('joint',r['id'],r['degree'],r['bound'],'->',z.get('bound',z.get('status')),flush=True)
 if time.time()-start>105:break
(HERE/'R3_ONE_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start)
