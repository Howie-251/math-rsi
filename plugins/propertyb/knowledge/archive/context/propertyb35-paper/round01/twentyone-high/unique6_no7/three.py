"""Unique6/no7 branch: complete actual three-unit8 center-star domain for M35/v21, after n21 unit pair gates."""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction
import json,sys,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
sys.path.insert(0,str(BASE/'two_low_high_star'))
from unpaired_three import serial

def main():
 st=time.time();gate={(r['codegrees'][2],r['triple']):r['strict'] for r in json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees']==[6,8,8]};parts=[(7,),(1,6),(2,5),(4,3),(1,2,4)];pairs=list(combinations(range(3),2));seen={};orbits=[];labels=[]
 for P in parts:
  same=lambda A:int(any(B&A==A for B in P))
  for cs in product(range(1,4),repeat=3):
   if any(gate[(v,same(sum(1<<i for i in S)))] for S,v in zip(pairs,cs)):continue
   for t in range(min(cs)+1):
    inc={1:8,2:8,4:8,3:cs[0],5:cs[1],6:cs[2],7:t};J={A:v-same(A) for A,v in inc.items()};outside={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,8)};outside[0]=29-sum(outside.values())
    if min(outside.values())<0:continue
    ns={A<<1:v for A,v in outside.items()};ns[1]=6-len(P)
    for B in P:ns[1|(B<<1)]=1
    k=tuple(ns.get(m,0) for m in range(16))
    if k not in seen:
     oid=len(orbits);orbits.append(dict(id=oid,degrees=[6,8,8,8],center_partition=P,neighbor_codegrees=cs,neighbor_triple=t,counts=ns))
     for perm in permutations(range(3)):
      def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(3) if m>>(i+1)&1)
      moved={move(m):v for m,v in ns.items()};seen[tuple(moved.get(m,0) for m in range(16))]=(oid,perm)
    oid,perm=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_neighbor_permutation=perm))
 old=[r for r in json.loads((BASE/'STAR_THREE_DOMAIN.json').read_text())['cases'] if r['center_degree']==6 and r['neighbor_degrees']==[8,8,8]];assert {tuple(r['counts'].get(str(m),0) for m in range(16)) for r in old}=={tuple(r['counts'].get(m,0) for m in range(16)) for r in labels}
 (HERE/'THREE_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),flush=True)
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('strict',sum(r['strict'] for r in out),'of',len(out),'max',max(r['bound'] for r in out),flush=True)
 (HERE/'THREE_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n')
if __name__=='__main__':main()
