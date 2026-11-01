"""Complete four actual unit8-neighbour views of one degree6 center, shared actual partition and inclusions."""
from pathlib import Path
from itertools import product,combinations,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def parts(n):
 for a in product(range(n),repeat=n):
  if a[0] or any(a[i]>max(a[:i])+1 for i in range(1,n)):continue
  if max(a)>=6:continue
  P=tuple(sum(1<<i for i,v in enumerate(a) if v==j) for j in range(max(a)+1))
  if max(B.bit_count() for B in P)<=4:yield P

def restrict(P,S):return tuple(sorted(sum(1<<j for j,i in enumerate(S) if B>>i&1) for B in P if any(B>>i&1 for i in S)))
def recover(s,P,hi):
 J={A:v-int(any(B&A==A for B in P)) for A,v in hi.items()};outside={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,1<<s)};outside[0]=29-sum(outside.values())
 if min(outside.values())<0:return None
 ns={A<<1:v for A,v in outside.items()};ns[1]=6-len(P)
 for B in P:ns[1|(B<<1)]=1
 return ns

def main():
 st=time.time();src=json.loads((HERE/'THREE_DP.json').read_text())['cases'];jj={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'THREE_JOINT.json').read_text())['results']};rem={r['id'] for r in src if jj.get(r['id'],Q(r['bound']))>=1};allowed={}
 for r in json.loads((HERE/'THREE_DOMAIN.json').read_text())['labelled']:
  if r['orbit'] not in rem:continue
  ns={int(m):v for m,v in r['counts'].items()};P=tuple(sorted(m>>1 for m,v in ns.items() if v and m&1 and m>>1));I=lambda A:sum(v for m,v in ns.items() if m&(A<<1)==A<<1);cs=tuple(I(A) for A in (3,5,6));allowed.setdefault((P,cs),set()).add(I(7))
 trs=list(combinations(range(4),3));seen={};orbits=[];labels=[]
 for P in parts(4):
  for cs in product(range(1,4),repeat=6):
   pair=dict(zip(combinations(range(4),2),cs));opts=[allowed.get((restrict(P,S),tuple(pair[ij] for ij in combinations(S,2))),()) for S in trs]
   if any(not v for v in opts):continue
   for ts in product(*opts):
    for q in range(min(ts)+1):
     hi={1<<i:8 for i in range(4)}|{sum(1<<i for i in S):v for S,v in pair.items()}|{sum(1<<i for i in S):v for S,v in zip(trs,ts)}|{15:q};ns=recover(4,P,hi)
     if ns is None:continue
     k=tuple(ns.get(m,0) for m in range(32))
     if k not in seen:
      oid=len(orbits);orbits.append(dict(id=oid,degrees=[6]+[8]*4,center_partition=P,neighbor_codegrees=cs,triples=ts,four=q,counts=ns))
      for perm in permutations(range(4)):
       def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(4) if m>>(i+1)&1)
       moved={move(m):v for m,v in ns.items()};seen[tuple(moved.get(m,0) for m in range(32))]=(oid,perm)
     oid,perm=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_neighbor_permutation=perm))
 (HERE/'FOUR_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),flush=True)
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('strict',sum(r['strict'] for r in out),'of',len(out),'max',max((r['bound'] for r in out),default=None),flush=True)
 (HERE/'FOUR_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
