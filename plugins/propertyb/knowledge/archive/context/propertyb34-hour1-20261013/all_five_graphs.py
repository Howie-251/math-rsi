"""T34 v22: all codegree-one/two graphs on five degree-seven locks, bounded pilot."""
from pathlib import Path
from itertools import combinations,permutations
from functools import lru_cache
from fractions import Fraction
import sys,json,time
HERE=Path(__file__).resolve().parent;sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'high-math'))
from fast_position_dp import Engine
from position_dp import solve,json_value
start=time.perf_counter();s=5;v=22;perms=list(permutations(range(s)))
pairs=[sum(1<<i for i in ij) for ij in combinations(range(s),2)]
def trans(t,p):return sum(1<<p[i] for i in range(s) if t&(1<<i))
def graphtrans(g,p):return sum(1<<pairs.index(trans(t,p)) for j,t in enumerate(pairs) if g&(1<<j))
graphs=[];seen=set()
for g in range(1<<len(pairs)):
 if g in seen:continue
 graphs.append(g);seen.update(graphtrans(g,p) for p in perms)
blocks=[t for t in range(1<<s) if t.bit_count()>=2]
content={t:tuple(j for j,b in enumerate(pairs) if t&b==b) for t in blocks}
@lru_cache(None)
def rec(rem):
 if time.perf_counter()-start>150:raise RuntimeError('150s generation budget')
 if not any(rem):return frozenset([()])
 j=next(j for j,n in enumerate(rem) if n);out=set()
 for t in blocks:
  inds=content[t]
  if j not in inds or any(rem[k]==0 for k in inds):continue
  nxt=list(rem)
  for k in inds:nxt[k]-=1
  for tail in rec(tuple(nxt)):out.add(tuple(sorted((t,)+tail)))
 return frozenset(out)
engine=Engine(v,s);output=[]
for g in graphs:
 raw=rec(tuple(1+bool(g&(1<<j)) for j in range(len(pairs))))
 auto=[p for p in perms if graphtrans(g,p)==g];groups=[];orbit={}
 for bs in sorted(raw):
  ns={b:bs.count(b) for b in set(bs)}
  for i in range(s):ns[1<<i]=7-sum(bool(t&(1<<i)) for t in bs)
  ns[0]=34-sum(ns.values())
  if min(ns.values())<0:continue
  ns={t:n for t,n in ns.items() if n};key=tuple(sorted(ns.items()))
  if key not in orbit:
   gid=len(groups);groups.append(ns)
   for p in auto:orbit[tuple(sorted((trans(t,p),n) for t,n in ns.items()))]=gid
 witnesses=[];bad=None
 for gid,ns in enumerate(groups):
  best=None;labels=set()
  for p in perms:
   c={trans(t,p):n for t,n in ns.items()};key=tuple(sorted(c.items()))
   if key in labels:continue
   labels.add(key);r=engine.solve(c)
   if best is None or r['bound']<best['bound']:best=dict(**r,counts=c)
   if r['bound']<1:break
  check=solve(v,best['counts'],s);assert check['bound']==best['bound']
  witnesses.append(dict(group=gid,label_orders_checked=len(labels),**check))
  if best['bound']>=1:
   bad=gid;break
 result=dict(graph=g,nonunit_pairs=[pairs[j] for j in range(len(pairs)) if g&(1<<j)],raw=len(raw),valid=len(orbit),groups=len(groups),all_pass=bad is None,witnesses=witnesses)
 output.append(result);print(g,len(groups),'pass',bad is None,'checked',len(witnesses),'last',witnesses[-1]['bound'],'time',time.perf_counter()-start,flush=True)
 if time.perf_counter()-start>150:break
(HERE/'ALL_FIVE_GRAPH_RESULTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,graph_count=len(graphs),graphs_checked=len(output),all_graphs_complete=len(output)==len(graphs),results=output,elapsed_seconds=time.perf_counter()-start)),indent=2)+'\n')
