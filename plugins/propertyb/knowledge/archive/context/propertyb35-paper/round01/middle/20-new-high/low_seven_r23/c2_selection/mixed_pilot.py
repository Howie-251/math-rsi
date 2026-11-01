"""Actual remaining eight type profiles: two real7 centers of codegree2 and three selected unit neighbors.
Modes:8,10,10/11 all unpaired;8,8,10/11 unpaired with A-pair star-separated and inclusive2;
or8,8,10 with paired10, all center stars discrete, exactly one common-center edge containing that10.
"""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[6];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math'),str(HERE.parent)]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
from replay_r3 import fixed
start=time.time();strong=[]
for a,b in ((8,11),(10,11)):
 for c in range(5,min(a,b)+1):
  ns={0:35-a-b+c,1:a-c,2:b-c,3:c};eng=SubsetEngine(20,2,ns);z=eng.verify(eng.solve());z.update(degrees=[a,b],codegree=c);assert z['bound']<1 and fixed(json_value(z))==z['bound'];strong.append(z)
(HERE/'MIXED_STRONG_PAIRS.json').write_text(json.dumps(json_value(dict(scope='All newly needed mixed degree11 high/high pairs with codegree>=5.',cases=strong,all_strict=True)),indent=2)+'\n')
Ps=[(7,),(1,6),(2,5),(4,3),(1,2,4)];inc=lambda P,A:int(any(B&A==A for B in P));modes=[('u8_10_10',[8,10,10],False,False),('u8_10_11',[8,10,11],False,False),('u8_8_10',[8,8,10],True,False),('u8_8_11',[8,8,11],True,False),('p8_8_10',[8,8,10],True,True)];results=[]
for name,degrees,separated,paired in modes:
 seen={};orbits=[];labelled=[]
 partitions=[(1,2,4)] if paired else [P for P in Ps if not separated or not inc(P,3)]
 for P1,P2 in product(partitions,repeat=2):
  for cs in product(*(((2,) if separated else range(1,5)),range(1,5),range(1,5))):
   for tt in range(min(cs)+1):
    high={1:degrees[0],2:degrees[1],4:degrees[2],3:cs[0],5:cs[1],6:cs[2],7:tt};I={}
    for t in range(1,32):
     low=t&3;A=t>>2
     if low==0:I[t]=high[A]
     elif low==1:I[t]=7 if A==0 else inc(P1,A)
     elif low==2:I[t]=7 if A==0 else inc(P2,A)
     else:I[t]=2 if A==0 else int(paired and A==4)
    ns={t:sum((-1)**(u.bit_count()-t.bit_count())*v for u,v in I.items() if u&t==t) for t in range(1,32)};ns[0]=35-sum(ns.values())
    if min(ns.values())<0:continue
    key=tuple(ns.get(t,0) for t in range(32))
    if key in seen:idx,perm,swap=seen[key]
    else:
     idx=len(orbits);orbits.append(dict(id=idx,degrees=[7,7,*degrees],counts=ns,partitions=[P1,P2],high_pairs=cs,high_triple=tt,paired_high=2 if paired else None,labelled_count=0))
     for perm in permutations(range(3)):
      if [degrees[i] for i in perm]!=degrees:continue
      # perm acts old label i -> perm[i], same-degree restriction equivalently checked above.
      for swap in (0,1):
       def move(t):return ((((t&1)<<1)|((t&2)>>1)) if swap else(t&3))|sum(1<<(perm[i]+2) for i in range(3) if t>>(i+2)&1)
       moved={move(t):v for t,v in ns.items()};seen[tuple(moved.get(t,0) for t in range(32))]=(idx,perm,swap)
     idx,perm,swap=seen[key]
    orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_high_permutation=perm,from_representative_low_swap=swap))
 domain=dict(scope=__doc__,mode=name,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled)
 (HERE/(name+'_DOMAIN.json')).write_text(json.dumps(json_value(domain),indent=2)+'\n');print(name,'domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
 if len(orbits)>1400:print(name,'too many orbits; no DP',flush=True);continue
 out=[]
 for r in orbits:
  eng=SubsetEngine(20,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
  if len(out)==10:print(name,'pilot10 strict',sum(z['strict'] for z in out),'seconds',time.time()-start,flush=True)
  if time.time()-start>105:break
 (HERE/(name+'_DP.json')).write_text(json.dumps(json_value(dict(scope=__doc__,mode=name,complete=len(out)==len(orbits),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print(name,'dp',len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-start,flush=True)
 joints=[];eng5=Engine(20,5)
 for r in out:
  if r['strict']:continue
  z=solve_profile(eng5,dict(r,graph=name,group=r['id']),permutation_limit=120);z['source_id']=r['id'];joints.append(z);print(name,'joint',r['id'],z.get('bound',z.get('status')),flush=True)
  if time.time()-start>115:break
 (HERE/(name+'_JOINT.json')).write_text(json.dumps(json_value(dict(scope=__doc__,mode=name,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print(name,'joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
 if time.time()-start>115:break
