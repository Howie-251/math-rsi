"""M35 v20 exactly4 seven-degree points: actual unique four-lock residue + one8/9 outsider.
Chosen outsider has all four codegrees1..3 and total excess<=5. Genuine old-trace
capacity extension; all low-low-outsider projections are checked first.
"""
from pathlib import Path
from itertools import combinations,product,permutations
import sys,json,time
from fractions import Fraction as Q
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(HERE.parent),str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from pilot import triple
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();projections=[];lookup={};eng3=Engine(20,3)
for d in (8,9):
 for a,b in product(range(1,4),repeat=2):
  for t in (0,1):
   ns=triple(20,[7,7,d],(1,a,b),t)
   if min(ns.values())<0:continue
   eng=SubsetEngine(20,3,ns);z=eng.verify(eng.solve());z.update(degree=d,cross=(a,b),triple=t,source_id=len(projections),strict=z['bound']<1)
   if not z['strict']:
    j=solve_profile(eng3,dict(z,graph='r4proj',group=z['source_id']),permutation_limit=6);z['joint']=j
    z['strict']=Q(j.get('bound','2'))<1
   projections.append(z);lookup[(d,a,b,t)]=z['strict']
(HERE/'R4_PROJECTIONS.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=projections,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('projections',len(projections),'strict',sum(r['strict'] for r in projections),flush=True)
pairs=list(combinations(range(4),2));perms=list(permutations(range(4)));seen={};domain=[];labelled=[]
for d in (8,9):
 for p2 in product((0,1),repeat=6):
  incidents=[sum(c for S,c in zip(pairs,p2) if i in S) for i in range(4)]
  for p1 in product(range(4),repeat=4):
   lam=[p1[i]+incidents[i] for i in range(4)]
   if any(c<1 or c>3 for c in lam) or sum(lam)>9:continue
   if any(lookup[(d,lam[i],lam[j],pij)] for (i,j),pij in zip(pairs,p2)):continue
   p0=d-sum(p2)-sum(p1)
   if not 0<=p0<=13:continue
   ns={0:13-p0,16:p0}
   for i,p in enumerate(p1):ns[1<<i]=4-p;ns[(1<<i)|16]=p
   for S,p in zip(pairs,p2):
    m=sum(1<<i for i in S);ns[m]=1-p;ns[m|16]=p
   key=tuple(ns.get(t,0) for t in range(32))
   if key in seen:idx,perm=seen[key]
   else:
    idx=len(domain);domain.append(dict(id=idx,degree=d,counts=ns,codegrees=lam,promoted_pairs=p2,promoted_singletons=p1,promoted_empty=p0,labelled_count=0))
    for perm in perms:
     move=lambda t:(t&16)|sum(1<<perm[i] for i in range(4) if t>>i&1)
     moved={move(t):n for t,n in ns.items()};seen[tuple(moved.get(t,0) for t in range(32))]=(idx,perm)
    idx,perm=seen[key]
   domain[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_permutation=perm))
(HERE/'R4_OUTSIDE_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,orbits=domain,labelled=labelled,orbit_count=len(domain),labelled_count=len(labelled),elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('extension domain',len(labelled),'orbits',len(domain),'seconds',time.time()-start,flush=True)
out=[]
for r in domain:
 eng=SubsetEngine(20,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('dp',r['id'],r['degree'],z['bound'],flush=True)
(HERE/'R4_OUTSIDE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('dp strict',sum(z['strict'] for z in out),'of',len(out),'seconds',time.time()-start,flush=True)
joints=[];eng5=Engine(20,5)
for r in out:
 if r['strict']:continue
 z=solve_profile(eng5,dict(r,graph='r4outside',group=r['id']),permutation_limit=120);z['source_id']=r['id'];joints.append(z)
 print('joint',r['id'],r['degree'],z.get('bound',z.get('status')),len(z.get('layouts',[])),flush=True)
 if time.time()-start>110:break
(HERE/'R4_OUTSIDE_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start)
