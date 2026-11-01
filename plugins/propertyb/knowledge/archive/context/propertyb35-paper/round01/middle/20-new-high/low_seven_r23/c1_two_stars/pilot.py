"""c1 unique-small-Q rigid spectrum. Select three actual unpaired degree10 vertices.
Two real unit-center partitions over the same three highs; common center edge contains none.
Noncenter inclusive J=I-p1-p2 and exact Mobius, keeping simultaneous same-block on both sides.
"""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[6];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time()
def partitions3():
 return [(7,),(1,6),(2,5),(4,3),(1,2,4)]
def inc(P,A):return int(any(B&A==A for B in P))
seen={};orbits=[];labelled=[]
for P1,P2 in product(partitions3(),repeat=2):
 for cs in product(range(1,5),repeat=3):
  for tt in range(min(cs)+1):
   I={1:10,2:10,4:10,3:cs[0],5:cs[1],6:cs[2],7:tt};J={A:v-inc(P1,A)-inc(P2,A) for A,v in I.items()}
   ns0={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,8)};ns0[0]=22-sum(ns0.values())
   if min(ns0.values())<0:continue
   ns={A<<2:v for A,v in ns0.items() if v};ns[3]=1;ns[1]=6-len(P1);ns[2]=6-len(P2)
   for B in P1:ns[1|(B<<2)]=1
   for B in P2:ns[2|(B<<2)]=1
   assert sum(ns.values())==35 and [sum(v for t,v in ns.items() if t>>i&1) for i in range(5)]==[7,7,10,10,10]
   key=tuple(ns.get(t,0) for t in range(32))
   if key in seen:idx,perm,swap=seen[key]
   else:
    idx=len(orbits);orbits.append(dict(id=idx,degrees=[7,7,10,10,10],counts=ns,partitions=[P1,P2],high_pairs=cs,high_triple=tt,noncenter_inclusive=J,labelled_count=0))
    for perm in permutations(range(3)):
     for swap in (0,1):
      def move(t):return ((((t&1)<<1)|((t&2)>>1)) if swap else(t&3))|sum(1<<(perm[i]+2) for i in range(3) if t>>(i+2)&1)
      moved={move(t):v for t,v in ns.items()};seen[tuple(moved.get(t,0) for t in range(32))]=(idx,perm,swap)
    idx,perm,swap=seen[key]
   orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_high_permutation=perm,from_representative_low_swap=swap))
(HERE/'DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
out=[]
for r in orbits:
 eng=SubsetEngine(20,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 if len(out) in (10,100,500):print('dp progress',len(out),'strict',sum(x['strict'] for x in out),'seconds',time.time()-start,flush=True)
 if len(out)==10 and (len(orbits)>2500 or time.time()-start>2):break
 if time.time()-start>55:break
(HERE/'DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(orbits),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
joints=[];eng5=Engine(20,5)
for r in out:
 if r['strict']:continue
 z=solve_profile(eng5,dict(r,graph='twostars',group=r['id']),permutation_limit=120);z['source_id']=r['id'];joints.append(z)
 print('joint',r['id'],r['bound'],'->',z.get('bound',z.get('status')),flush=True)
 if time.time()-start>75:break
(HERE/'JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
