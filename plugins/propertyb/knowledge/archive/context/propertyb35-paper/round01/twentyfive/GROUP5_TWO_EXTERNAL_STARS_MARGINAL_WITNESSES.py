"""Exact replay of two positive 20-partition marginal certificates.
These satisfy the new seven-lock residual supports and elementary multiplicity
caps, but are not claimed to satisfy all joint pair or edge-realization data.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json
P=Path(__file__).resolve().parent
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text())
replay=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_REPLAY.json').read_text())
w={1:[([1,2,4,24],1),([1,10,20],3),([2,12,17],3),([3,4,24],3),([4,9,18],1),([4,10,17],3),([7,24],2),([9,22],2),([13,18],2)],9:[([1,6,8,16],4),([2,4,9,16],4),([3,12,16],1),([3,28],2),([5,10,16],1),([5,26],2),([6,9,16],2),([10,21],2),([12,19],2)]}
out=[]
for ident,ww in w.items():
 mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};nu={t:(5-t.bit_count())*c for t,c in mu.items() if t};allowed={tuple(p) for r in replay['arc_pruning'] if r['id']==ident for p in r['remaining_partitions']};cc=Counter();parts=[]
 for pp,n in ww:
  assert tuple(pp) in allowed and n>=1
  assert n<=min(nu[t] for t in pp)
  assert n<=1 or sum(mu[t]==1 for t in pp)<3
  for t in pp:cc[t]+=n
  parts.extend([set(pp) for _ in range(n)])
 assert len(parts)==20 and dict(cc)==nu
 unique={t for t,c in mu.items() if t and c==1};parent=list(range(20))
 def find(x):
  while parent[x]!=x:x=parent[x]
  return x
 for x,y in combinations(range(20),2):
  common=parts[x]&parts[y]&unique;assert len(common)<=2
  if len(common)==2:parent[find(x)]=find(y)
 comps={}
 for x in range(20):comps.setdefault(find(x),[]).append(x)
 sizes=sorted([len(c) for c in comps.values()],reverse=True)
 bins=[0]*4;assignment=[[] for _ in range(4)]
 def pack(k):
  if k==len(sizes):return bins==[5]*4
  seen=set()
  for j in range(4):
   if bins[j] in seen or bins[j]+sizes[k]>5:continue
   seen.add(bins[j]);bins[j]+=sizes[k];assignment[j].append(k)
   if pack(k+1):return True
   bins[j]-=sizes[k];assignment[j].pop()
  return False
 assert pack(0)
 out.append(dict(id=ident,partition_multiset=[dict(blocks=p,multiplicity=n) for p,n in ww],nu=nu,component_sizes=sizes,component_packing=assignment,twenty_and_marginals_verified=True,elementary_caps_and_forced_group_packing_verified=True))
result=dict(scope=__doc__,passed=True,source='A bounded scipy.optimize.milp call proposed the integer vectors; this script certifies all stated properties with integer arithmetic only.',results=out,full_hypergraph_realizability_claimed=False)
(P/'GROUP5_TWO_EXTERNAL_STARS_MARGINAL_WITNESSES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(passed=True,ids=list(w),component_sizes=[r['component_sizes'] for r in out]),indent=2))
