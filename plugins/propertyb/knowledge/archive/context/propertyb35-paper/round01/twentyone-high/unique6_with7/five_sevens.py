"""Complete shared inclusions of center6 plus five actual degree7 neighbours; no unit assumption."""
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
 return {m:v for m,v in enumerate(ns)} if min(ns)>=0 else None

def main():
 st=time.time();src=json.loads((HERE/'FOUR7_DP.json').read_text())['cases'];jj={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'FOUR7_JOINT.json').read_text())['results']};rem={r['id'] for r in src if jj.get(r['id'],Q(r['bound']))>=1};base=[moments(r['counts']) for r in json.loads((HERE/'FOUR7_DOMAIN.json').read_text())['labelled'] if r['orbit'] in rem];views=[(0,)+S for S in combinations(range(1,6),4)];options=[[lift(r,S) for r in base] for S in views];known=set();ks=[];buckets=[]
 for opt in options:
  shared=tuple(sorted(known&set(opt[0])));ks.append(shared);b={}
  for r in opt:b.setdefault(tuple(r[k] for k in shared),[]).append(r)
  buckets.append(b);known|=set(opt[0])
 joins=0;seen={};orbits=[];labels=[]
 def go(i,inc):
  if i==len(options):yield inc;return
  for r in buckets[i].get(tuple(inc[k] for k in ks[i]),[]):yield from go(i+1,inc|r)
 for inc in go(0,{}):
  joins+=1;assert set(inc)==set(range(1,64))-{62,63}
  assert all(inc[62^(1<<i)]==0 for i in range(1,6))
  ns=recover({0:35}|inc|{62:0,63:0})
  if ns is None:continue
  k=tuple(ns[m] for m in range(64))
  if k not in seen:
   oid=len(orbits);orbits.append(dict(id=oid,degrees=[6]+[7]*5,counts=ns))
   for perm in permutations(range(5)):
    def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(5) if m>>(i+1)&1)
    moved={move(m):v for m,v in ns.items()};seen[tuple(moved[m] for m in range(64))]=(oid,perm)
  oid,perm=seen[k];labels.append(dict(counts=ns,orbit=oid,from_representative_seven_permutation=perm))
 (HERE/'FIVE7_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,precompletion_joins=joins,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),'joins',joins,flush=True)
 if len(orbits)>1500:return
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 print('tested',len(out),'strict',sum(r['strict'] for r in out),'max',max((r['bound'] for r in out),default=None),flush=True)
 (HERE/'FIVE7_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
