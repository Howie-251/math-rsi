"""All actual degree6+three degree7 inputs after every shared complete677 strict gate; seven points need not be unit."""
from pathlib import Path
from itertools import product,combinations,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def main():
 st=time.time();prev=json.loads((HERE/'ALL677_DP.json').read_text())['cases'];allow={}
 for r in prev:
  if not r['strict']:allow.setdefault(tuple(r['codegrees']),set()).add(r['triple'])
 prs=list(combinations(range(4),2));trs=list(combinations(range(4),3));labels=[];orbits=[];seen={}
 for ps in product((1,2),repeat=6):
  pair=dict(zip(prs,ps));opts=[allow.get((*sorted((pair[0,i],pair[0,j])),pair[i,j]),()) for i,j in combinations(range(1,4),2)]+[range(min(pair[i,j] for i,j in combinations(range(1,4),2))+1)]
  if any(not v for v in opts):continue
  for ts in product(*opts):
   for q in range(min(ts)+1):
    inc={0:35,1:6,2:7,4:7,8:7}|{sum(1<<i for i in S):v for S,v in pair.items()}|{sum(1<<i for i in S):v for S,v in zip(trs,ts)}|{15:q};ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(16)}
    if min(ns.values())<0:continue
    k=tuple(ns[m] for m in range(16))
    if k not in seen:
     oid=len(orbits);orbits.append(dict(id=oid,degrees=[6,7,7,7],codegrees=ps,triples=ts,four=q,counts=ns))
     for perm in permutations(range(3)):
      def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(3) if m>>(i+1)&1)
      moved={move(m):v for m,v in ns.items()};seen[tuple(moved[m] for m in range(16))]=(oid,perm)
    oid,perm=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_seven_permutation=perm))
 (HERE/'THREE7_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),flush=True)
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('strict',sum(r['strict'] for r in out),'of',len(out),'max',max(r['bound'] for r in out),flush=True)
 (HERE/'THREE7_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
