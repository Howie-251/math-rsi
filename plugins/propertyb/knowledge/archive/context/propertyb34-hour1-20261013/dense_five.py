"""Bounded local diagnosis: five seven-degree locks, all codegrees two."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations,permutations
from fractions import Fraction
import sys,time,json
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'high-math'))
from fast_position_dp import Engine
from position_dp import solve,json_value
start=time.perf_counter();s=5
pairs=[sum(1<<i for i in ij) for ij in combinations(range(s),2)]
blocks=[t for t in range(1<<s) if t.bit_count()>=2]
content={t:tuple(j for j,p in enumerate(pairs) if t&p==p) for t in blocks}
@lru_cache(None)
def rec(rem):
 if time.perf_counter()-start>90:raise RuntimeError('90s enumeration budget')
 if not any(rem):return frozenset([()])
 j=next(j for j,x in enumerate(rem) if x);out=set()
 for t in blocks:
  inds=content[t]
  if j not in inds or any(rem[k]==0 for k in inds):continue
  nxt=list(rem)
  for k in inds:nxt[k]-=1
  for tail in rec(tuple(nxt)):out.add(tuple(sorted((t,)+tail)))
 return frozenset(out)
raw=rec((2,)*len(pairs));groups={};orbit={}
def trans(t,p):return sum(1<<p[i] for i in range(s) if t&(1<<i))
for bs in sorted(raw):
 ns={b:bs.count(b) for b in set(bs)}
 for i in range(s):ns[1<<i]=7-sum(bool(t&(1<<i)) for t in bs)
 ns[0]=34-sum(ns.values())
 if min(ns.values())<0:continue
 ns={t:n for t,n in ns.items() if n};key=tuple(sorted(ns.items()))
 if key not in orbit:
  gid=len(groups);groups[gid]=ns
  for p in permutations(range(s)):orbit[tuple(sorted((trans(t,p),n) for t,n in ns.items()))]=gid
print('raw',len(raw),'valid',len(orbit),'groups',len(groups),'seconds',time.perf_counter()-start,flush=True)
out=[]
for v in (22,23):
 engine=Engine(v,s)
 for gid,ns in groups.items():
  best=None;seen=set()
  for perm in permutations(range(s)):
   c={trans(t,perm):n for t,n in ns.items()};key=tuple(sorted(c.items()))
   if key in seen:continue
   seen.add(key);r=engine.solve(c)
   if best is None or r['bound']<best['bound']:best=dict(**r,counts=c)
   if r['bound']<1:break
  checked=solve(v,best['counts'],s);assert checked['bound']==best['bound']
  out.append(dict(v=v,group=gid,label_orders_checked=len(seen),**checked))
  print(v,gid,best['bound'],len(seen),flush=True)
  if time.perf_counter()-start>150:raise RuntimeError('150s total budget')
(HERE/'DENSE_FIVE_RESULTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,raw=len(raw),valid=len(orbit),groups=len(groups),results=out,elapsed_seconds=time.perf_counter()-start)),indent=2)+'\n')
