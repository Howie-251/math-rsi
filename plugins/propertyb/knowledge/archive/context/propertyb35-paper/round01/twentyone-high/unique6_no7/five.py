"""Bounded complete shared-four-view join for five actual unit8 neighbours of the same degree6 center."""
from pathlib import Path
from itertools import combinations,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def moments(ns):
 ns={int(m):v for m,v in ns.items()};return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,32)}
def lift(inc,S):return {sum(1<<S[i] for i in range(5) if m>>i&1):v for m,v in inc.items()}
def recover(inc):
 ns=[inc[m] for m in range(64)]
 for i in range(6):
  for m in range(64):
   if not m>>i&1:ns[m]-=ns[m|(1<<i)]
 return {m:n for m,n in enumerate(ns)} if min(ns)>=0 else None

def main():
 st=time.time();src=json.loads((HERE/'FOUR_DP.json').read_text())['cases'];j={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'FOUR_JOINT.json').read_text())['results']};rem={r['id'] for r in src if j.get(r['id'],Q(r['bound']))>=1};base=[moments(r['counts']) for r in json.loads((HERE/'FOUR_DOMAIN.json').read_text())['labelled'] if r['orbit'] in rem];views=[(0,)+S for S in combinations(range(1,6),4)];options=[[lift(r,S) for r in base] for S in views];ks=[];buckets=[];known=set()
 for opt in options:
  shared=tuple(sorted(known&set(opt[0])));ks.append(shared);b={}
  for r in opt:b.setdefault(tuple(r[k] for k in shared),[]).append(r)
  buckets.append(b);known|=set(opt[0])
 joins=0;rejected_partition=0;seen={};orbits=[];labels=[];complete=True
 def go(i,inc):
  if time.time()-st>55:raise TimeoutError('55-second domain budget')
  if i==len(options):yield inc;return
  for r in buckets[i].get(tuple(inc[k] for k in ks[i]),[]):yield from go(i+1,inc|r)
 try:
  for inc in go(0,{}):
   joins+=1;assert set(inc)==set(range(1,64))-{62,63}
   if joins>100000:raise TimeoutError('100000 join budget')
   blocks=[];remain=set(range(1,6))
   while remain:
    i=min(remain);B={j for j in remain if i==j or inc[1|(1<<i)|(1<<j)]==1};blocks.append(B);remain-=B
   if max(map(len,blocks))>4 or any(inc[1|(1<<i)|(1<<j)]!=int(any(i in B and j in B for B in blocks)) for i,j in combinations(range(1,6),2)):
    rejected_partition+=1;continue
   for t in range(min(1,min(inc[62^(1<<i)] for i in range(1,6)))+1):
    ns=recover({0:35}|inc|{62:t,63:0})
    if ns is None:continue
    k=tuple(ns[m] for m in range(64))
    if k not in seen:
     oid=len(orbits);P=tuple(sum(1<<(i-1) for i in B) for B in blocks);orbits.append(dict(id=oid,degrees=[6]+[8]*5,center_partition=P,neighbor_five=t,counts=ns))
     for perm in permutations(range(5)):
      def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(5) if m>>(i+1)&1)
      moved={move(m):v for m,v in ns.items()};seen[tuple(moved[m] for m in range(64))]=(oid,perm)
    oid,perm=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_neighbor_permutation=perm))
 except TimeoutError as e:complete=False;print(str(e),flush=True)
 (HERE/'FIVE_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=complete,precompletion_joins=joins,rejected_partition=rejected_partition,labelled=labels,orbits=orbits,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),'complete',complete,'joins',joins,flush=True)
 if not complete:return
 selected=list(range(len(orbits)));dp_complete=True
 if len(orbits)>1500:selected=sorted(set(round(i*(len(orbits)-1)/29) for i in range(30)));dp_complete=False
 out=[]
 for i in selected:
  r=orbits[i];eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('tested',len(out),'strict',sum(r['strict'] for r in out),'max',max((r['bound'] for r in out),default=None),flush=True)
 (HERE/'FIVE_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=dp_complete,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
