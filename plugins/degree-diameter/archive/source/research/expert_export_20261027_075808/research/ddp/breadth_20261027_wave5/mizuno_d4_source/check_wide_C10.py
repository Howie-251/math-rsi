from pathlib import Path
from itertools import product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;started=time.process_time();d=json.loads((P/'construction.json').read_text());A=d['matrices'];b=d['control_vectors'];inv=d['inverse_labels'];es=d['base_edges'];tree=[0,2,3,4,6,7,9];free=[e for e in range(16) if e not in tree]
def mv(T,x):return [sum(a*z for a,z in zip(row,x))%3 for row in T]
def rank(cs):
 m=[list(row) for row in zip(*cs)];r=0
 for j in range(len(cs)):
  p=next((i for i in range(r,4) if m[i][j]),None)
  if p is None:continue
  m[r],m[p]=m[p],m[r];z=1 if m[r][j]==1 else 2;m[r]=[z*x%3 for x in m[r]]
  for i in range(4):
   if i!=r:
    z=m[i][j];m[i]=[(x-z*y)%3 for x,y in zip(m[i],m[r])]
  r+=1
 return r
good=[];bad=[]
for w in product(range(4),repeat=4):
 if any(w[i+1]==inv[w[i]] for i in range(3)):continue
 cs=[]
 for t in w:cs=[mv(A[t],v) for v in cs]+[b[t]]
 (good if rank(cs)==4 else bad).append(w)
assert len(good)==100 and [''.join('ABCD'[t] for t in w) for w in bad]==['AABD','ACDD','BBAC','BDCC','CABB','CCDB','DBAA','DDCA']
short=[w for w in product(range(4),repeat=2) if w[1]!=inv[w[0]]];words=[()]+short+good
darts=[[None]*4 for _ in range(8)]
for e,x in enumerate(es):
 u,v,t=x['tail'],x['head'],x['label'];darts[u][t]=(v,e,1);darts[v][inv[t]]=(u,e,-1)
records=[];source9=[];transplant10=[];functions=[]
for root in range(8):
 target=[[] for _ in range(8)]
 for w in words:
  u=root;cc=[0]*16
  for t in w:
   u,e,s=darts[u][t];cc[e]+=s
  target[u].append((w,cc))
 rowfun=[]
 for v in range(8):
  funcs=sorted({tuple(cc[e]%10 for e in free) for w,cc in target[v]});rowfun.append(funcs)
  states9={sum(cc[e]*es[e]['voltage'] for e in range(16))%9 for w,cc in target[v]};states10={sum(cc[e]*es[e]['voltage'] for e in range(16))%10 for w,cc in target[v]}
  assert len(states9)==9;source9.append(len(states9));transplant10.append(10-len(states10));records.append(dict(source=root,target=v,raw_supported_words=len(target[v]),distinct_symbolic_C10_functions=len(funcs),required10=10,source_C9_reached=len(states9),source_integer_transplant_C10_reached=len(states10)))
 functions.append(rowfun)
# Gauge the original integer voltages after reinterpreting them modulo10.
potential=[None]*8;potential[0]=0
while any(v is None for v in potential):
 for e in tree:
  x=es[e];u,v,z=x['tail'],x['head'],x['voltage']
  if potential[u] is not None and potential[v] is None:potential[v]=(potential[u]+z)%10
  if potential[v] is not None and potential[u] is None:potential[u]=(potential[v]-z)%10
g=[(x['voltage']+potential[x['tail']]-potential[x['head']])%10 for x in es];assert all(g[e]==0 for e in tree) and g[1]!=0 and g[5]!=0
def support_orbits(gamma):
 rows=[]
 for root in range(8):
  reached=set()
  for w in words:
   u=root;h=0
   for t in w:u,e,s=darts[u][t];h=(h+s*gamma[e])%10
   reached.add(10*u+h)
  rows.append(sorted(reached))
 return rows
rep=support_orbits(g)
assert sum(80-len(x) for x in rep)==sum(transplant10)
minimum=min(x['distinct_symbolic_C10_functions'] for x in records)
out=dict(status='WIDE_C10_SYMBOLIC_CAPACITY_ALLOWS_FINITE_TRIAL' if minimum>=10 else 'WIDE_C10_SYMBOLIC_CAPACITY_OBSTRUCTION',certificate='identity OR reduced2 OR one of100 source rank-good reduced4 words',reduced2_words=12,rank_good4_words=100,total_supported_words_per_base_root=113,tree_edges=tree,free_edges=free,free_variables=9,parallel_nonzero_free_edges=[1,5],legal_normalized_assignments=9**2*10**7,controller_vertices=80,lift_q=3,lift_dimension=4,candidate_order=6480,candidate_degree=12,saved_record=5832,minimum_symbolic_capacity=minimum,records=records,source_C9_all64_base_pair_slots_covered=True,source_C9_controller_order=72,C10_integer_transplant_full_gauged_voltages=g,C10_integer_transplant_free_voltages=[g[e] for e in free],C10_integer_transplant_missing_representative_targets=sum(transplant10),C10_integer_transplant_missing_ordered_controller_pairs=10*sum(transplant10),C10_integer_transplant_reached_per_root=[len(x) for x in rep],C10_transplant_support=rep,no_C4_factor_constraint=True,actual80_graphs_generated=False,voltage_search_started=False,CPU_seconds=time.process_time()-started)
(P/'wide_C10_capacity.json').write_text(json.dumps(out,indent=2)+'\n');(P/'wide_C10_functions.json').write_text(json.dumps(dict(functions=functions,free_edges=free,good4_words=good,reduced2_words=short,tree_edges=tree),separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['records','C10_transplant_support']},indent=2));print('capacities',[[records[8*u+v]['distinct_symbolic_C10_functions'] for v in range(8)] for u in range(8)])
