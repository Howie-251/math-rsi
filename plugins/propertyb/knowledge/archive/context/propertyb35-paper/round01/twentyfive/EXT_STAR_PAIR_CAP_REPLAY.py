"""Pure-Python exact replay of id10's newly capped positive witness.
Does not import NumPy, SciPy or the proposing program.
"""
from pathlib import Path
from collections import Counter,deque
from itertools import combinations
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();d=json.loads((P/'EXT_STAR_PAIR_CAP.json').read_text());mu={int(t):c for t,c in d['mu'].items()};nu={int(t):c for t,c in d['nu'].items()};single={t for t,c in mu.items() if t and c==1};parts=d['partition_domain'];v=d['integer_multiplicities']
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());assert mu=={int(t):c for t,c in cat['representatives'][10]['counts'].items()}
assert nu=={t:(5-t.bit_count())*c for t,c in mu.items() if t}
# Reconstruct the full local domain independently as exact covers of G.
allowed=[t for t,c in mu.items() if t and c];generated=[]
def covers(left,blocks):
 if not left:generated.append(frozenset(blocks));return
 pivot=left&-left
 for t in allowed:
  if t&pivot and t&left==t:covers(left^t,blocks+[t])
covers(31,[])
assert len(generated)==len(set(generated))==21
assert {frozenset(p) for p in parts}==set(generated)
assert all(isinstance(n,int) and n>=0 for n in v) and sum(v)==20
marg=Counter();expanded=[]
for i,(pp,n) in enumerate(zip(parts,v)):
 u=min(nu[t] for t in pp)
 if len(set(pp)&single)>=3:u=min(u,1)
 assert u==d['multiplicity_caps'][i] and n<=u
 for t in pp:marg[t]+=n
 expanded += [set(pp) for _ in range(n)]
assert dict(marg)==nu and [sorted(p) for p in expanded]==d['twenty_partitions']
y={int(t):Q(w) for t,w in d['exact_LP_upper_certificate']['trace_weights'].items()}
assert all(w>=0 for w in y.values()) and all(sum(y[t] for t in p)>=1 for p in parts)
assert sum(y[t]*nu[t] for t in nu)==20
# Directly check the full family of triple-of-unique-trace inequalities.
triple_checks=0
for tr in combinations(sorted(single),3):
 lhs=sum(n for pp,n in zip(parts,v) if set(tr)<=set(pp));assert lhs<=1;triple_checks+=1
adj={i:set() for i in range(20)};group_of={v:i for i,g in enumerate(d['outer_group_assignment']) for v in g}
assert len(group_of)==20 and all(len(g)==5 for g in d['outer_group_assignment']) and set(group_of)==set(range(20))
for i,j in combinations(range(20),2):
 co=expanded[i]&expanded[j]&single;assert len(co)<=2
 if len(co)==2:adj[i].add(j);adj[j].add(i);assert group_of[i]==group_of[j]
seen=set();components=[]
for i in range(20):
 if i in seen:continue
 q=deque([i]);seen.add(i);cc=[]
 while q:
  x=q.popleft();cc.append(x)
  for z in adj[x]-seen:seen.add(z);q.append(z)
 components.append(frozenset(cc))
assert {frozenset(c) for c in d['components']}==set(components)
for t in single:
 if t.bit_count()!=1:continue
 xx={i for i,p in enumerate(expanded) if t in p};assert len(xx)==4
 assert len({group_of[i] for i in xx})>=2
out=dict(scope=__doc__,passed=True,domain_partitions=21,partition_copies=20,all_trace_marginals=True,all_multiplicity_caps=True,triple_unique_trace_inequalities_checked=triple_checks,all_pair_common_unique_counts_at_most_two=True,component_sizes=sorted(map(len,components),reverse=True),four_outer_groups_size_five=True,no_four_trace_necessary_condition=True,exact_LP_optimum='20',full_H_constructed=False,elapsed_seconds=time.perf_counter()-st)
(P/'EXT_STAR_PAIR_CAP_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
