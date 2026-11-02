from pathlib import Path
from itertools import product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;started=time.process_time();d=json.loads((P/'construction.json').read_text());edges=d['base_edges'];inv=d['inverse_labels'];base=[[] for _ in range(8)];C=[[-1]*4 for _ in range(72)]
for e,x in enumerate(edges):
 u,v,t,z=x['tail'],x['head'],x['label'],x['voltage'];base[u].append((v,e,1));base[v].append((u,e,-1))
 for h in range(9):C[9*u+h][t]=9*v+(h+z)%9;C[9*v+(h+z)%9][inv[t]]=9*u+h
assert all(len(set(row))==4 for row in C)
assert all(C[v][inv[t]]==u for u,row in enumerate(C) for t,v in enumerate(row))
words=[w for w in product(range(4),repeat=4) if all(w[i+1]!=inv[w[i]] for i in range(3))]
def endpoint(u,w):
 for t in w:u=C[u][t]
 return u
counts=[[0]*72 for _ in range(72)]
for u in range(72):
 for w in words:counts[u][endpoint(u,w)]+=1
missing=[(u,v) for u in range(72) for v in range(72) if not counts[u][v]]
missinghist=Counter(sum(v==0 for v in row) for row in counts)
paths=[[[] for _ in range(8)] for _ in range(8)]
for root in range(8):
 def rec(u,prev,coeff,word):
  if len(word)==4:paths[root][u].append(coeff.copy());return
  for v,e,s in base[u]:
   if e==prev:continue
   coeff[e]+=s;word.append((e,s));rec(v,e,coeff,word);word.pop();coeff[e]-=s
 rec(root,-1,[0]*16,[])
assert all(sum(map(len,row))==108 for row in paths)
# Gauge the external C8 tree to zero, retaining edge3 as its one free voltage h.
# Internal factor: (e0,e1)=(a,a+5), (e4,e5)=(b,b+5),
# (e12,e13,e14,e15)=(c,d,e,d+e-c), forcing every internal component to C4.
coefs=[[0]*6 for _ in range(16)];const=[0]*16
for e,j in [(0,0),(1,0),(4,1),(5,1),(12,2),(13,3),(14,4),(3,5)]:coefs[e][j]=1
const[1]=const[5]=5;coefs[15][2]=-1;coefs[15][3]=coefs[15][4]=1
records=[]
for u in range(8):
 for v in range(8):
  funcs10=set();funcs5=set();unconstrained=set()
  for c in paths[u][v]:
   a=tuple(sum(c[e]*coefs[e][j] for e in range(16))%10 for j in range(6));k=sum(c[e]*const[e] for e in range(16))%10
   funcs10.add((a,k));funcs5.add(tuple(x%5 for x in a));unconstrained.add(tuple(x%10 for x in c))
  upper=min(len(funcs10),2*len(funcs5));records.append(dict(source=u,target=v,raw_NB4_paths=len(paths[u][v]),unconstrained_symbolic_mod10=len(unconstrained),C4_factor_symbolic_mod10=len(funcs10),C4_factor_symbolic_mod5=len(funcs5),upper_possible_states_mod10=upper,required10=10))
minimum=min(r['upper_possible_states_mod10'] for r in records);witness=next(r for r in records if r['upper_possible_states_mod10']==minimum)
result=dict(status='C4_FACTOR_Z10_CAPACITY_PASSES_NECESSARY_SCREEN' if minimum>=10 else 'C4_FACTOR_Z10_CAPACITY_OBSTRUCTION',source_controller_vertices=72,source_controller_edges=144,source_exact_NB4_missing_ordered_pairs=len(missing),source_exact_NB4_missing_per_root_histogram=dict(missinghist),source_diagonal_NB4_missing=sum(counts[u][u]==0 for u in range(72)),source_missing_pairs=missing,base_internal_factor_edge_ids=[0,1,4,5,12,13,14,15],base_external_C8_edge_ids=[2,3,6,7,8,9,10,11],proposed_controller_vertices=80,proposed_fiber_modulus=10,proposed_C4_factor_count=20,proposed_free_voltages=['a','b','c','d','e','h'],minimum_symbolic_capacity=minimum,capacity_witness=witness,records=records,actual80_graphs_generated=0,voltage_search_started=False,CPU_seconds=time.process_time()-started)
(P/'controller_and_capacity.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'controller72.edges').write_text('72 144\n'+''.join(f'{u} {v}\n' for u,row in enumerate(C) for v in row if u<v))
(P/'controller72.labels.json').write_text(json.dumps(dict(n=72,inverse=inv,out=C))+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['source_missing_pairs','records']},indent=2));print('raw counts',[ [records[8*u+v]['raw_NB4_paths'] for v in range(8)] for u in range(8)]);print('upper capacities',[[records[8*u+v]['upper_possible_states_mod10'] for v in range(8)] for u in range(8)])
