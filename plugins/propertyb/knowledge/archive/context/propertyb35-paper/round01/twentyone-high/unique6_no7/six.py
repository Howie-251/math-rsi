"""Six guaranteed nonexceptional unit8 neighbours: pair codegrees2, actual center partition a matching, all five projections shared."""
from pathlib import Path
from itertools import combinations,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def moments(ns,s):
 ns={int(m):v for m,v in ns.items()};return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,1<<s)}
def lift(inc,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in inc.items()}
def recover(inc):
 ns=[inc[m] for m in range(128)]
 for i in range(7):
  for m in range(128):
   if not m>>i&1:ns[m]-=ns[m|(1<<i)]
 return {m:n for m,n in enumerate(ns)} if min(ns)>=0 else None

def main():
 st=time.time();src=json.loads((HERE/'FIVE_DP.json').read_text())['cases'];jj={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'FIVE_JOINT.json').read_text())['results']};rem=[r for r in src if jj.get(r['id'],Q(r['bound']))>=1];keep=set()
 for r in rem:
  inc=moments(r['counts'],6);ones=[(i,j) for i,j in combinations(range(1,6),2) if inc[(1<<i)|(1<<j)]==1];assert all(inc[(1<<i)|(1<<j)] in (1,2) for i,j in combinations(range(1,6),2));assert not ones or any(set(ones)=={tuple(sorted((i,j))) for j in range(1,6) if j!=i} for i in range(1,6));assert inc[62]==0
  if not ones and max(B.bit_count() for B in r['center_partition'])<=2:keep.add(r['id'])
 base=[moments(r['counts'],6) for r in json.loads((HERE/'FIVE_DOMAIN.json').read_text())['labelled'] if r['orbit'] in keep];views=[(0,)+S for S in combinations(range(1,7),5)];options=[[lift(r,S) for r in base] for S in views];ks=[];buckets=[];known=set()
 for opt in options:
  shared=tuple(sorted(known&set(opt[0])));ks.append(shared);b={}
  for r in opt:b.setdefault(tuple(r[k] for k in shared),[]).append(r)
  buckets.append(b);known|=set(opt[0])
 joins=0;seen={};orbits=[];labels=[];complete=True
 def go(i,inc):
  if time.time()-st>55:raise TimeoutError('55-second domain budget')
  if i==len(options):yield inc;return
  for r in buckets[i].get(tuple(inc[k] for k in ks[i]),[]):yield from go(i+1,inc|r)
 try:
  for inc in go(0,{}):
   joins+=1;assert set(inc)==set(range(1,128))-{126,127}
   if joins>100000:raise TimeoutError('100000 join budget')
   ns=recover({0:35}|inc|{126:0,127:0})
   if ns is None:continue
   # Every source view is a matching partition; global equivalence remains so.
   groups=[];left=set(range(1,7))
   while left:
    i=min(left);B={j for j in left if i==j or inc[1|(1<<i)|(1<<j)]==1};groups.append(B);left-=B
   assert max(map(len,groups))<=2
   k=tuple(ns[m] for m in range(128))
   if k not in seen:
    oid=len(orbits);orbits.append(dict(id=oid,degrees=[6]+[8]*6,center_partition=[sum(1<<(i-1) for i in B) for B in groups],counts=ns))
    for perm in permutations(range(6)):
     def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(6) if m>>(i+1)&1)
     moved={move(m):v for m,v in ns.items() if v};seen[tuple(moved.get(m,0) for m in range(128))]=(oid,perm)
   oid,perm=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_neighbor_permutation=perm))
 except TimeoutError as e:complete=False;print(str(e),flush=True)
 (HERE/'SIX_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=complete,source_residuals=len(rem),source_kept_orbits=sorted(keep),source_labelled=len(base),precompletion_joins=joins,labelled=labels,orbits=orbits,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),'complete',complete,'joins',joins,flush=True)
 if not complete or len(orbits)>1500:return
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,7,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('tested',len(out),'strict',sum(r['strict'] for r in out),'max',max((r['bound'] for r in out),default=None),flush=True)
 (HERE/'SIX_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
