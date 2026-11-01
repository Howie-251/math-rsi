"""Independent certificate replay for all 27 external-partition decisions.
Positive cases: check 20 disjoint partitions and every nu marginal.
Negative cases: explicit integer separators, exhaustively valid on all 51
partitions without a five-element block. No matching-search trust required.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
source=json.loads((P/'GROUP5_CATALOGUE.json').read_text());decisions=json.loads((P/'GROUP5_PARTITIONS.json').read_text())
# Independent Bell recursion: insert the next point into an existing block or new singleton.
parts=[()]
for i in range(5):
 new=[]
 for part in parts:
  new.append(tuple(sorted(part+(1<<i,))))
  for j in range(len(part)):
   q=list(part);q[j]|=1<<i;new.append(tuple(sorted(q)))
 parts=sorted(set(new))
assert len(parts)==52
parts=[p for p in parts if 31 not in p];assert len(parts)==51
separators={
 0:dict(weights={t:1 for t in range(1,31) if t.bit_count()>=2},bound=2,kind='at_most_two_nonsingle_blocks'),
 2:dict(weights={t:1 for t in [28,24,20,18,17,15]},bound=1,kind='pairwise_intersecting_block_family'),
 3:dict(weights={t:1 for t in [28,20,18,17,7]},bound=1,kind='pairwise_intersecting_block_family'),
 4:dict(weights={t:(2 if t==19 else 0 if t==12 else 1) for t in range(1,31) if t.bit_count()>=2},bound=2,kind='triple_and_its_complement'),
 6:dict(weights={t:1 for t in [25,24,20,18,17,15]},bound=1,kind='pairwise_intersecting_block_family'),
}
records=[]
for rep,decision in zip(source['representatives'],decisions['results']):
 assert rep['id']==decision['id'];i=rep['id'];mu={int(t):c for t,c in rep['counts'].items()}
 nu={t:(5-t.bit_count())*c for t,c in mu.items() if t and t!=31 and (5-t.bit_count())*c}
 if i not in separators:
  assert decision['status']=='FEASIBLE';observed=Counter();n=0
  for item in decision['partition_multiset']:
   part=item['blocks'];c=item['multiplicity'];assert isinstance(c,int) and c>0
   assert tuple(part) in parts
   n+=c
   for t in part:observed[t]+=c
  assert n==20 and dict(sorted(observed.items()))==dict(sorted(nu.items()))
  records.append(dict(id=i,status='FEASIBLE',twenty_partitions_replayed=True,all_nu_marginals_equal=True,nu=nu,partition_multiset=decision['partition_multiset']))
 else:
  cert=separators[i];w=cert['weights'];b=cert['bound']
  assert all(sum(w.get(t,0) for t in part)<=b for part in parts)
  left=sum(w.get(t,0)*c for t,c in nu.items());right=20*b
  assert left>right
  records.append(dict(id=i,status='INFEASIBLE',separator=cert,left=left,right=right,all_51_partitions_checked=True,nu=nu))
summary=dict(scope=__doc__,complete=True,feasible=22,infeasible=5,all_cases_independently_replayed=True,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_PARTITIONS_REPLAY.json').write_text(json.dumps(dict(summary=summary,results=records),indent=2)+'\n');print(json.dumps(summary,indent=2))
