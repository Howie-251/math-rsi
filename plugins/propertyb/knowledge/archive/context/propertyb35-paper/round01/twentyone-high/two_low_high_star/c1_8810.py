"""c1 rigid |U_Q|=3: unpaired common-unit(8,8,10), eight-pair codegree2 and not in both center blocks."""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def main():
 st=time.time();gate={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees'][0]==6};parts=[(7,),(1,6),(2,5),(4,3),(1,2,4)];labels=[];orbits=[];seen={};ds=(8,8,10);pairs=list(combinations(range(3),2))
 for P,R in product(parts,repeat=2):
  same=lambda T,A:int(any(B&A==A for B in T))
  if same(P,3)+same(R,3)>1:continue
  for cs2,cs3 in product(range(1,4),repeat=2):
   cs=(2,cs2,cs3)
   if any(gate[(tuple(ds[i] for i in ij),v,same(T,sum(1<<i for i in ij)))] for T in (P,R) for ij,v in zip(pairs,cs)):continue
   for t in range(min(cs)+1):
    inc={1:8,2:8,4:10,3:2,5:cs2,6:cs3,7:t};J={A:v-same(P,A)-same(R,A) for A,v in inc.items()};outside={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,8)};outside[0]=24-sum(outside.values())
    if min(outside.values())<0:continue
    ns={A<<2:v for A,v in outside.items()};ns[3]=1;ns[1]=5-len(P);ns[2]=5-len(R)
    for B in P:ns[1|(B<<2)]=1
    for B in R:ns[2|(B<<2)]=1
    k=tuple(ns.get(m,0) for m in range(32))
    if k not in seen:
     oid=len(orbits);orbits.append(dict(id=oid,degrees=[6,6,8,8,10],partitions=[P,R],high_codegrees=cs,high_triple=t,counts=ns))
     for perm in [(0,1,2),(1,0,2)]:
      for swap in (0,1):
       def move(m):return ((((m&1)<<1)|((m&2)>>1)) if swap else m&3)|sum(1<<(perm[i]+2) for i in range(3) if m>>(i+2)&1)
       moved={move(m):v for m,v in ns.items()};seen[tuple(moved.get(m,0) for m in range(32))]=(oid,perm,swap)
    oid,perm,swap=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_high_permutation=perm,from_representative_center_swap=swap))
 (HERE/'C1_8810_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),flush=True)
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('cases',len(out),'strict',sum(r['strict'] for r in out),'max',max((r['bound'] for r in out),default=None),flush=True)
 (HERE/'C1_8810_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
