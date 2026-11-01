"""c1 four actual unpaired common-unit Q=degree8/9 points; all same-star three-point residual projections."""
from pathlib import Path
from itertools import product,combinations,permutations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def partitions(n):
 for a in product(range(n),repeat=n):
  if a[0] or any(a[i]>max(a[:i])+1 for i in range(1,n)):continue
  yield tuple(sum(1<<i for i,v in enumerate(a) if v==j) for j in range(max(a)+1))
def restriction(P,S):return tuple(sorted(sum(1<<j for j,i in enumerate(S) if B>>i&1) for B in P if any(B>>i&1 for i in S)))
def main():
 st=time.time();src=json.loads((HERE/'UNPAIRED_THREE_DP.json').read_text())['cases'];joint={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'UNPAIRED_THREE_JOINT.json').read_text())['results']};resids={r['id'] for r in src if r['center_codegree']==1 and joint.get(r['id'],Q(r['bound']))>=1};labels=json.loads((HERE/'UNPAIRED_THREE_DOMAIN.json').read_text())['labelled'];allowed={}
 for r in labels:
  if r['orbit'] not in resids:continue
  ns={int(m):v for m,v in r['counts'].items()};parts=[tuple(sorted(m>>2 for m,v in ns.items() if v and m&3==i and m>>2)) for i in (1,2)];I3=sum(v for m,v in ns.items() if m&28==28);allowed.setdefault((tuple(r['neighbor_degrees']),*parts),set()).add(I3)
 seen={};orbits=[];labels=[];trs=list(combinations(range(4),3))
 for ds in [(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)]:
  perms=[p for p in permutations(range(4)) if all(ds[i]==ds[p[i]] for i in range(4))]
  for P,R in product(partitions(4),repeat=2):
   opts=[allowed.get((tuple(ds[i] for i in S),restriction(P,S),restriction(R,S)),()) for S in trs]
   if any(not v for v in opts):continue
   for ts in product(*opts):
    for q in range(min(ts)+1):
     inc={1<<i:ds[i] for i in range(4)}|{sum(1<<i for i in S):2 for S in combinations(range(4),2)}|{sum(1<<i for i in S):t for S,t in zip(trs,ts)}|{15:q};J={A:v-int(any(B&A==A for B in P))-int(any(B&A==A for B in R)) for A,v in inc.items()};outside={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,16)};outside[0]=24-sum(outside.values())
     if min(outside.values())<0:continue
     ns={A<<2:v for A,v in outside.items()};ns[3]=1;ns[1]=5-len(P);ns[2]=5-len(R)
     for B in P:ns[1|(B<<2)]=1
     for B in R:ns[2|(B<<2)]=1
     k=(ds,tuple(ns.get(m,0) for m in range(64)))
     if k not in seen:
      oid=len(orbits);orbits.append(dict(id=oid,degrees=[6,6]+list(ds),partitions=[P,R],high_triples=ts,high_four=q,counts=ns))
      for perm in perms:
       for swap in (0,1):
        def move(m):return ((((m&1)<<1)|((m&2)>>1)) if swap else m&3)|sum(1<<(perm[i]+2) for i in range(4) if m>>(i+2)&1)
        moved={move(m):v for m,v in ns.items()};seen[(ds,tuple(moved.get(m,0) for m in range(64)))]=(oid,perm,swap)
     oid,perm,swap=seen[k];labels.append(dict(neighbor_degrees=ds,counts=ns,orbit=oid,from_representative_high_permutation=perm,from_representative_center_swap=swap))
 (HERE/'C1_FOUR_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),flush=True)
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 for ds in [(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)]:
  rr=[r for r in out if tuple(r['degrees'][2:])==ds];print(ds,len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
 (HERE/'C1_FOUR_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
