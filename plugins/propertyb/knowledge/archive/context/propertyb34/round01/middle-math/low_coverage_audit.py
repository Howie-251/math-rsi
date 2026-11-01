"""Independent pair-budget recursion for the complete four-low profile coverage."""
from pathlib import Path
from functools import lru_cache
from itertools import product,combinations,permutations
from time import perf_counter
import json
HERE=Path(__file__).resolve().parent
pairs=[sum(1<<i for i in ij) for ij in combinations(range(4),2)]
blocks=[t for t in range(16) if t.bit_count()>=2]
inds={t:[j for j,p in enumerate(pairs) if t&p==p] for t in blocks}
@lru_cache(None)
def rec(rem):
 if not any(rem):return frozenset([()])
 j=next(j for j,n in enumerate(rem) if n);out=set()
 for t in blocks:
  js=inds[t]
  if j not in js or any(rem[k]==0 for k in js):continue
  nxt=list(rem)
  for k in js:nxt[k]-=1
  for tail in rec(tuple(nxt)):out.add(tuple(sorted((t,)+tail)))
 return frozenset(out)
ps=list(permutations(range(4)))
def canon(ns):
 return min(tuple(sorted((sum(1<<p[i] for i in range(4) if t&(1<<i)),n) for t,n in ns.items() if n)) for p in ps)
def run(v):
 start=perf_counter();profiles=set();groups=set();budgets=0
 for ls in product(range(1,27-v),repeat=6):
  if any(sum(c-1 for t,c in zip(pairs,ls) if t&(1<<i))>25-v for i in range(4)):continue
  budgets+=1
  for bs in rec(ls):
   ns={t:bs.count(t) for t in set(bs)}
   for i in range(4):ns[1<<i]=6-sum(n for t,n in ns.items() if t.bit_count()>=2 and t&(1<<i))
   ns[0]=34-sum(ns.values())
   if min(ns.values())<0:continue
   profiles.add(tuple(sorted((t,n) for t,n in ns.items() if n)));groups.add(canon(ns))
 source=json.loads((HERE/f'FOUR_LOW_{v}.json').read_text())
 saved={tuple(sorted((int(t),n) for t,n in w['counts'].items())) for w in source['results']}
 assert groups==saved and len(profiles)==source['labelled'] and len(groups)==source['groups']
 out=dict(v=v,independent_first_pair_recursion=True,budgets=budgets,labelled_profiles=len(profiles),orbits=len(groups),exact_saved_domain_binding=True,elapsed_seconds=perf_counter()-start)
 (HERE/f'FOUR_LOW_{v}_COVERAGE.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':
 for v in [22,23]:run(v)
