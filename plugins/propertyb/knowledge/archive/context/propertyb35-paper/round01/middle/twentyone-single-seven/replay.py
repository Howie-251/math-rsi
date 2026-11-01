"""Independent n21 unit8 domains and fixed/strict-dual replay; final547 domain fully processed, with64 residual inventories remaining.
RGS partitions and explicit Mobius replace the original recursive recovery.
"""
from pathlib import Path
from itertools import combinations,product,permutations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/middle-math'))
from audit21 import verify as rawfixed
import verify_joint_layout as joint

def fixed(r):return rawfixed(dict(r,quotas=r.get('certificates',r.get('quotas'))))
def check35(ns,s,v,expected_degrees=None):
 assert v==21 and sum(ns.values())==35 and all(n>=0 and t.bit_count()<=5 for t,n in ns.items());assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(expected_degrees));return [frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
joint.check_profile=check35

def parts(n):
 for a in product(range(n),repeat=n):
  if a[0] or any(a[i]>1+max(a[:i]) for i in range(1,n)):continue
  yield tuple(tuple(i for i in range(n) if a[i]==j) for j in range(max(a)+1))
def inventory(s,part,inc):
 J={0:28};J.update({A:inc[A]-int(any(all(i in B for i in range(s) if A>>i&1) for B in part)) for A in range(1,1<<s)});ns={1:7-len(part)}
 for B in part:ns[1|sum(1<<(i+1) for i in B)]=1
 for T in range(1<<s):ns[T<<1]=sum((-1)**((A^T).bit_count())*j for A,j in J.items() if A&T==T)
 return ns if min(ns.values())>=0 else None
def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<(s+1)))
def load(f):return json.loads((HERE/f).read_text())
def main():
 st=time.time();old=HERE.parents[1]/'twentyone-high';two=[r for r in json.loads((old/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees']==[7,8,8]];exp2=set()
 for p in parts(2):
  for c in range(1,9):
   ns=inventory(2,p,{1:8,2:8,3:c})
   if ns is not None:exp2.add(key(ns,2))
 assert len(two)==15 and exp2=={key(r['counts'],2) for r in two};assert all((fixed(r)<1)==(r['codegrees'][2]>=4) for r in two)
 exp3=set();metadata={}
 for p in parts(3):
  prs=list(combinations(range(3),2))
  for cs in product((1,2,3),repeat=3):
   for t in range(min(cs)+1):
    inc={1<<i:8 for i in range(3)};inc.update({(1<<i)|(1<<j):c for (i,j),c in zip(prs,cs)});inc[7]=t;ns=inventory(3,p,inc)
    if ns is not None:exp3.add(key(ns,3));metadata[key(ns,3)]=(p,cs,t)
 dp=load('THREE_DP.json');assert dp['complete'] and len(dp['cases'])==246 and exp3=={key(r['counts'],3) for r in dp['cases']};vs={r['id']:fixed(r) for r in dp['cases']};nf=sum(v<1 for v in vs.values());nj=0
 for z in load('THREE_JOINT.json')['results']:
  if Q(z.get('bound','2'))<1:
   assert key(z['counts'],3)==key(dp['cases'][z['source_id']]['counts'],3)
   vs[z['source_id']]=Q(joint.verify(z,v=21,s=4,expected_degrees=[7,8,8,8])['bound']);nj+=1
 res={metadata[key(r['counts'],3)] for r in dp['cases'] if vs[r['id']]>=1};assert len(res)==100
 exp4=set();pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3))
 for p in parts(4):
  for cs in product((1,2,3),repeat=6):
   cp=dict(zip(pairs,cs));opts=[]
   for S in triples:
    ren={i:j for j,i in enumerate(S)};pp=tuple(sorted(tuple(ren[i] for i in B if i in S) for B in p if any(i in S for i in B)));ccc=tuple(cp[ij] for ij in combinations(S,2));opts.append([t for part,cc,t in res if part==pp and cc==ccc])
   if any(not x for x in opts):continue
   for ts in product(*opts):
    for q in range(min(ts)+1):
     inc={1<<i:8 for i in range(4)};inc.update({(1<<i)|(1<<j):c for (i,j),c in zip(pairs,cs)});inc.update({sum(1<<i for i in S):t for S,t in zip(triples,ts)});inc[15]=q;ns=inventory(4,p,inc)
     if ns is not None:exp4.add(key(ns,4))
 dom=load('FOUR_DOMAIN.json');assert len(exp4)==7777 and dom['orbit_count']==547 and exp4=={key(r['counts'],4) for r in dom['labelled']}
 for r in dom['labelled']:
  ns=dom['orbits'][r['orbit']]['counts'];p=r['from_representative_neighbor_permutation'];move=lambda t:(t&1)|sum(1<<(p[i]+1) for i in range(4) if t>>(i+1)&1);assert key({move(int(t)):n for t,n in ns.items()},4)==key(r['counts'],4)
 maps=[[((t&1)|sum(1<<(p[i]+1) for i in range(4) if t>>(i+1)&1)) for t in range(32)] for p in permutations(range(4))]
 def canonical(ns):
  vv=key(ns,4);return min(tuple(vv[m.index(t)] for t in range(32)) for m in maps)
 assert len({canonical(r['counts']) for r in dom['orbits']})==547
 fd=load('FOUR_DP.json');assert fd['complete'] and len(fd['cases'])==547 and {key(r['counts'],4) for r in fd['cases']}=={key(r['counts'],4) for r in dom['orbits']};fv={r['id']:fixed(r) for r in fd['cases']};fn=sum(v<1 for v in fv.values());fj=0;js=load('FOUR_JOINT.json');assert js['complete']
 for z in js['results']:
  if Q(z.get('bound','2'))<1:
   assert key(z['counts'],4)==key(fd['cases'][z['source_id']]['counts'],4)
   fv[z['source_id']]=Q(joint.verify(z,v=21,s=5,expected_degrees=[7,8,8,8,8])['bound']);fj+=1
 resid={i for i,v in fv.items() if v>=1};assert len(resid)==64 and resid=={r['id'] for r in load('FOUR_REMAINDERS.json')['cases']}
 pilot=load('FOUR_PILOT.json')['cases'];pv=[Q(r['bound']) for r in pilot];assert len(pilot)==18 and sum(v<1 for v in pv)==13;assert all(key(r['counts'],4)==key(dom['orbits'][r['id']]['counts'],4) for r in pilot)
 result=dict(status='PASS',scope=__doc__,actual_pair_domain=15,independent_three_domain=246,three_fixed_strict=nf,three_joint_strict=nj,three_residual=100,independent_four_labelled=7777,four_stored_orbits=547,transport_checks=7777,final_domain_fully_processed=True,four_fixed_strict=fn,four_joint_strict=fj,four_remaining_count=len(resid),four_remaining_ids=sorted(resid),max_accepted_four_bound=str(max(v for v in fv.values() if v<1)),pilot_cases=18,pilot_strict=13,pilot_nonstrict_ids=[r['id'] for r,v in zip(pilot,pv) if v>=1],elapsed_seconds=time.time()-st);(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
