"""Complete seven-lock trace domains with codegree excess a matching.

An isolated matching vertex is appended to a complete six-lock domain. All
degree-six assignments of size <= qmax are included; all other degrees are 7.
Canonicalization is exact invariant refinement plus all remaining bijections.
"""
from pathlib import Path
from itertools import permutations, product, combinations
from functools import lru_cache
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;ROOT=HERE.resolve().parents[3]
sys.path[:0]=[str(HERE),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from mixed_six import profiles
from subset_position_dp import SubsetEngine
from multilock import json_value

def canonical(ns,n):
 blocks=[(t,c) for t,c in ns.items() if t and c]
 def normalize(sigs):
  d={v:i for i,v in enumerate(sorted(set(sigs)))}
  return [d[v] for v in sigs]
 colors=normalize([tuple(sum(c for t,c in blocks if t&(1<<i) and t.bit_count()==k) for k in range(1,6)) for i in range(n)])
 while True:
  signatures=[(colors[i],tuple(sorted((t.bit_count(),c,tuple(sorted(colors[j] for j in range(n) if j!=i and t&(1<<j)))) for t,c in blocks if t&(1<<i)))) for i in range(n)]
  nxt=normalize(signatures)
  if len(set(nxt))==len(set(colors)):colors=nxt;break
  colors=nxt
 cells=[tuple(i for i in range(n) if colors[i]==c) for c in sorted(set(colors))]
 dest=[];offset=0
 for cell in cells:dest.append(tuple(range(offset,offset+len(cell))));offset+=len(cell)
 best=None
 for orders in product(*(permutations(cell) for cell in cells)):
  p=[0]*n
  for order,ds in zip(orders,dest):
   for a,b in zip(order,ds):p[a]=b
  key=tuple(sorted((sum(1<<p[i] for i in range(n) if t&(1<<i)),c) for t,c in ns.items() if c))
  if best is None or key<best:best=key
 return best

def extend(ns,n=6):
 blocks=[t for t,c in ns.items() if t and c and t.bit_count()<=4]
 b=1<<n
 def visit(left,picked):
  if not left:
   nc=ns.copy()
   for t in picked:nc[t]-=1;nc[t|b]=nc.get(t|b,0)+1
   nc[b]=7-len(picked);nc[0]-=nc[b]
   yield {t:c for t,c in nc.items() if c};return
  bit=left&-left
  for t in blocks:
   if t&bit and t&left==t:yield from visit(left^t,picked+[t])
 yield from visit((1<<n)-1,[])

def generate(qmax,budget=600):
 start=time.perf_counter();out={};raw=colored=0;sources=[]
 for m in range(4):
  bad=[3<<(2*i) for i in range(m)];groups,nraw,valid=profiles([7]*6,bad);nr=0
  for g in groups.values():
   for ns in extend(g['counts']):
    nr+=1;raw+=1
    for q in range(qmax+1):
     for low in combinations(range(7),q):
      nc=ns.copy()
      for i in low:nc[1<<i]=nc.get(1<<i,0)-1
      nc[0]=nc.get(0,0)+q
      if min(nc.values())<0:continue
      colored+=1;key=canonical(nc,7)
      if key not in out:out[key]=dict(counts=dict(key),low_count=q,matching_size=m)
   if time.perf_counter()-start>budget:
    return dict(complete=False,qmax=qmax,raw=raw,colored=colored,sources=sources,elapsed=time.perf_counter()-start,profiles=list(out.values()))
  sources.append(dict(matching_size=m,six_orbits=len(groups),six_raw=nraw,raw_extensions=nr));print('generate',m,len(out),raw,colored,time.perf_counter()-start,flush=True)
 return dict(complete=True,qmax=qmax,raw=raw,colored=colored,sources=sources,elapsed=time.perf_counter()-start,profiles=list(out.values()))

if __name__=='__main__':
 qmax=int(sys.argv[1]) if len(sys.argv)>1 else 0
 target=HERE/f'SEVEN_MATCHING_QMAX{qmax}.json';start=time.perf_counter()
 if target.exists():g=json.loads(target.read_text());assert g['complete']
 else:g=generate(qmax);target.write_text(json.dumps(g,indent=2)+'\n')
 if not g['complete']:print('generation incomplete');raise SystemExit
 results=[]
 for j,p in enumerate(g['profiles']):
  e=SubsetEngine(24,7,p['counts']);z=e.solve()
  if z['bound']<1:e.verify(z)
  z.update(group=j,low_count=p['low_count'],matching_size=p['matching_size']);results.append(z)
  if len(results)%100==0:print('bound',len(results),sum(z['bound']<1 for z in results),time.perf_counter()-start,flush=True)
  if len(results)%100==0 or len(results)==len(g['profiles']):
   data=dict(complete=len(results)==len(g['profiles']),qmax=qmax,elapsed=time.perf_counter()-start,orbits=len(g['profiles']),strict=sum(z['bound']<1 for z in results),results=results)
   (HERE/f'SEVEN_MATCHING_QMAX{qmax}_BOUNDS.json').write_text(json.dumps(json_value(data),indent=2)+'\n')
