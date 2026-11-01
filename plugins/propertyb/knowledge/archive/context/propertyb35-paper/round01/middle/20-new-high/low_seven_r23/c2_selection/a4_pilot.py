"""Actual A>=4: select four degree8 unpaired double-unit neighbors of the same two7 centers, center codegree2.
Both star coincidence graphs form one matching; every high pair has inclusive count2.
Three-high inclusive count is0 for triples containing a star pair, otherwise0/1; four-high0..min triple.
"""
from pathlib import Path
from itertools import combinations,product,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[6];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();pairs=[(1<<i)|(1<<j) for i,j in combinations(range(4),2)];triples=[sum(1<<i for i in S) for S in combinations(range(4),3)];matchings=[()]
for k in (1,2):
 for es in combinations(pairs,k):
  if sum(e.bit_count() for e in es)!=(sum(es)).bit_count():continue
  matchings.append(es)
assert len(matchings)==10
seen={};orbits=[];labelled=[]
for matching in matchings:
 for colors in product((0,1),repeat=len(matching)):
  P=[]
  for center in (0,1):
   blocks=[e for e,c in zip(matching,colors) if c==center];covered=0
   for B in blocks:covered|=B
   blocks.extend(1<<i for i in range(4) if not covered>>i&1);P.append(blocks)
  ranges=[(0,) if any(T&e==e for e in matching) else (0,1) for T in triples]
  for ts in product(*ranges):
   for quad in range(min(ts)+1):
    J={1<<i:6 for i in range(4)}
    J.update({e:2-int(e in matching) for e in pairs});J.update(dict(zip(triples,ts)));J[15]=quad
    nn={T:sum((-1)**(A.bit_count()-T.bit_count())*v for A,v in J.items() if A&T==T) for T in range(1,16)};nn[0]=23-sum(nn.values())
    if min(nn.values())<0:continue
    ns={T<<2:v for T,v in nn.items() if v};ns[3]=2
    for a in (0,1):
     ns[1<<a]=5-len(P[a])
     for B in P[a]:ns[(1<<a)|(B<<2)]=1
    assert sum(ns.values())==35 and [sum(v for t,v in ns.items() if t>>i&1) for i in range(6)]==[7,7,8,8,8,8]
    key=tuple(ns.get(t,0) for t in range(64))
    if key in seen:idx,perm,swap=seen[key]
    else:
     idx=len(orbits);orbits.append(dict(id=idx,degrees=[7,7,8,8,8,8],counts=ns,partitions=P,high_triples=ts,high_quad=quad,labelled_count=0))
     for perm in permutations(range(4)):
      for swap in (0,1):
       def move(t):return ((((t&1)<<1)|((t&2)>>1)) if swap else(t&3))|sum(1<<(perm[i]+2) for i in range(4) if t>>(i+2)&1)
       moved={move(t):v for t,v in ns.items()};seen[tuple(moved.get(t,0) for t in range(64))]=(idx,perm,swap)
     idx,perm,swap=seen[key]
    orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_high_permutation=perm,from_representative_low_swap=swap))
(HERE/'A4_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
out=[]
for r in orbits:
 eng=SubsetEngine(20,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z);print('dp',r['id'],z['bound'],flush=True)
(HERE/'A4_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp strict',sum(z['strict'] for z in out),'seconds',time.time()-start,flush=True)
joints=[];eng6=Engine(20,6)
for r in out:
 if r['strict']:continue
 z=solve_profile(eng6,dict(r,graph='c2a4',group=r['id']),permutation_limit=720);z['source_id']=r['id'];joints.append(z);print('joint',r['id'],z.get('bound',z.get('status')),flush=True)
 if time.time()-start>60:break
(HERE/'A4_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
