"""Exact six-lock trace diagnosis for the seven residual v22 nonunit graphs."""
from pathlib import Path
from itertools import combinations,permutations
from functools import lru_cache
import sys,time,json
HERE=Path(__file__).resolve().parent;sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'high-math'))
from fast_position_dp import Engine
from position_dp import solve,json_value
start=time.perf_counter();s=6;v=22;perms=list(permutations(range(s)))
pairs=[sum(1<<i for i in ij) for ij in combinations(range(s),2)]
def trans(t,p):return sum(1<<p[i] for i in range(s) if t&(1<<i))
blocks=[t for t in range(1<<s) if 2<=t.bit_count()<=5]
content={t:tuple(j for j,b in enumerate(pairs) if t&b==b) for t in blocks}
def generate(bad):
 @lru_cache(None)
 def rec(rem):
  if time.perf_counter()-start>160:raise RuntimeError('160s generation budget')
  if not any(rem):return frozenset([()])
  j=next(j for j,n in enumerate(rem) if n);out=set()
  for t in blocks:
   inds=content[t]
   if j not in inds or any(rem[k]==0 for k in inds):continue
   nxt=list(rem)
   for k in inds:nxt[k]-=1
   for tail in rec(tuple(nxt)):out.add(tuple(sorted((t,)+tail)))
  return frozenset(out)
 return rec(tuple(1+int(t in bad) for t in pairs))
engine=Engine(v,s);out=[]
source=json.loads((HERE/'SIX_GRAPH_COVER.json').read_text())
for graph in source['residual_groups']:
 bad={sum(1<<i for i in p) for p in graph['pairs']};raw=generate(bad)
 auto=[p for p in perms if {trans(t,p) for t in bad}==bad];groups=[];orbit={}
 for bs in sorted(raw):
  ns={b:bs.count(b) for b in set(bs)}
  for i in range(s):ns[1<<i]=7-sum(bool(t&(1<<i)) for t in bs)
  ns[0]=34-sum(ns.values())
  if min(ns.values())<0:continue
  ns={t:n for t,n in ns.items() if n};key=tuple(sorted(ns.items()))
  if key not in orbit:
   gid=len(groups);groups.append(ns)
   for p in auto:orbit[tuple(sorted((trans(t,p),n) for t,n in ns.items()))]=gid
 print('generated',graph['graph'],len(raw),len(groups),'time',time.perf_counter()-start,flush=True)
 witnesses=[]
 for gid,ns in enumerate(groups):
  best=None;labels=set()
  for p in perms:
   c={trans(t,p):n for t,n in ns.items()};key=tuple(sorted(c.items()))
   if key in labels:continue
   labels.add(key);r=engine.solve(c)
   if best is None or r['bound']<best['bound']:best=dict(**r,counts=c)
   if r['bound']<1:break
  checked=solve(v,best['counts'],s);assert checked['bound']==best['bound']
  witnesses.append(dict(group=gid,label_orders_checked=len(labels),**checked))
  if best['bound']>=1:print('FAIL',graph['graph'],gid,best['bound'],flush=True)
  if time.perf_counter()-start>160:raise RuntimeError('160s total budget')
 rec=dict(graph=graph['graph'],pairs=graph['pairs'],raw=len(raw),valid=len(orbit),groups=len(groups),all_pass=all(x['bound']<1 for x in witnesses),witnesses=witnesses)
 out.append(rec);print('finished',graph['graph'],rec['all_pass'],'time',time.perf_counter()-start,flush=True)
 (HERE/'MIDDLE_SIX_RESIDUE_RESULTS.json').write_text(json.dumps(json_value(dict(scope=__doc__,graphs_completed=len(out),complete=len(out)==7,results=out,elapsed_seconds=time.perf_counter()-start)),indent=2)+'\n')
