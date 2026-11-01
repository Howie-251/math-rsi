"""Migrate the specified five 4-lock clique-graph families to 34 edges."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from math import factorial,comb
import runpy,sys,time,json
ROOT=Path(__file__).resolve().parents[2]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from twentytwo_four_scan import pattern_family
from four_wide_positions import weight_rows
from multilock import Profile,rows,total_bound,json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows

start=time.perf_counter();v=22;D=factorial(18)
families={ss:pattern_family(ss) for ss in [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]}
for best,patterns in families.values():
 for _,ns in patterns:ns[0]=ns.get(0,0)+1
for pos in combinations(range(8,16),4):
 raw=weight_rows(v,pos)
 for sizes,(best,patterns) in families.items():
  for gid,ns in patterns:
   total=0
   for aa,bb,cc,bit in raw:
    A=sum(n*aa[t] for t,n in ns.items());B=sum(n*bb[t] for t,n in ns.items());C=sum(ns.get(t,0)*(ns.get(u,0)-(t==u))*w for (t,u),w in cc.items())
    if bit:
     pure=max(0,(4*ns.get(bit,0)-18+2)//3);remaining=max(0,3-pure);loss=2*pure*cc.get((bit,bit),0)
     ts=sorted(t for t in ns if t&bit);slots=[]
     for j,t in enumerate(ts):
      for u in ts[j:]:
       cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
       if t==u==bit:cap-=pure
       assert cap>=0
       if cap:slots.append((cc.get((t,u),0)+cc.get((u,t),0),cap))
     for w,cap in sorted(slots):
      take=min(remaining,cap);remaining-=take;loss+=take*w
     assert not remaining;C-=loss
    total+=min(A,B,C)
   if best[gid]['best'] is None or total<best[gid]['best']:best[gid]=dict(best=total,bound=Fraction(total,D),positions=pos,counts=ns)
 if time.perf_counter()-start>180:raise RuntimeError('180 second profile budget')
out=[]
for sizes,(best,patterns) in families.items():
 for gid,r in best.items():
  p=Profile(v,5,r['positions'],r['counts']);cs=[certificate(p,i) for i in range(4)];rr=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(4)})
  assert total_bound(rr)==r['bound']
  stubs=[frozenset(i+1 for i in range(4) if b&(1<<i)) for b,n in p.counts.items() for _ in range(n)]
  for a,b in zip(rr,independent_rows(v,p.positions,stubs)):assert all(a[k]==b[k] for k in ['A','B','C'])
  out.append(dict(sizes=sizes,group=gid,**r,rows=rr,certificates=cs,independent_ABC=True))
 print(sizes,len(best),sum(r['bound']<1 for r in best.values()),max(r['bound'] for r in best.values()),flush=True)
Path(__file__).with_name('MIDDLE_FOUR_RESULTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.perf_counter()-start,profiles=out)),indent=2)+'\n')
