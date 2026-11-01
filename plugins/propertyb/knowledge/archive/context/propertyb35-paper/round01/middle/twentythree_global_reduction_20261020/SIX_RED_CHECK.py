#!/usr/bin/env python3
"""Tiny exact check of constants and the exhaustive graph forms in SIX_RED_PROOF.md."""
from math import comb
from itertools import product, combinations
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
C=lambda n,k:comb(n,k) if 0<=k<=n else 0
R=C(14,7);w=[C(10+j,3+j) for j in range(4)]
assert R==3432 and w==[120,330,792,1716]
triple_rows=[]
for a,b,c,z in product(range(3),repeat=4):
 if z>min(a,b,c) or any(4-x-y+z<0 for x,y in [(a,b),(a,c),(b,c)]):continue
 u=12-a-b-c+z;num=C(18-u,11-u);m2=sum(x==2 for x in [a,b,c]);m1=sum(x==1 for x in [a,b,c])
 if m2==0:assert num<=12*m1
 if m2==1:assert num<=96+12*m1 and num<=8+56*m1
 if m2==2 and m1==0:assert num<=192
 if m2==2 and m1==1:assert num<=2*96+12+126
 if m2==3:assert num<=3*96+504
 triple_rows.append([a,b,c,z,u,num])
# Graph forms on six labeled indices, classified independently by component sizes.
pairs=list(combinations(range(6),2));forms={}
for mask in range(1<<15):
 parent=list(range(6));edges=[]
 def f(i):
  while parent[i]!=i:i=parent[i]
  return i
 for k,(i,j) in enumerate(pairs):
  if mask>>k&1:parent[f(i)]=f(j);edges.append((i,j))
 comps={}
 for i in range(6):comps.setdefault(f(i),[]).append(i)
 rank=6-len(comps)
 if rank>2:continue
 sizes=sorted(len(x) for x in comps.values() if len(x)>1)
 key=(tuple(sizes),len(edges));forms[key]=forms.get(key,0)+1
assert forms=={((),0):1,((2,),1):15,((3,),2):60,((2,2),2):45,((3,),3):20}
values={
 'three_heavy_forest':3*w[2]+2*w[0],
 'triple_pair_plus_second_heavy':w[3]+w[2]+3*w[0],
 'triple_pair_rank3_forest':w[3]+2*w[1]+2*w[0],
 'all_linear':1800+162*6,
 'one_heavy':1800+288+162*4,
 'disjoint_two_heavy':1800+576+162*2,
 'path_three_linear':1800+576+162*3-126,
 'path_two_linear':3564-(330+6*36+13*8),
 'triangle_all_linear_counts':min(2952-14*m for m in range(13))}
assert min(values.values())==2616
out={'status':'PASS_TINY_EXACT_CHECK','R':R,'D':C(18,11),'pair_intersection_counts':w,'feasible_three_set_Venn_parameter_rows':len(triple_rows),'rank_at_most_two_graphs':sum(forms.values()),'heavy_graph_forms':[{'nontrivial_component_sizes':list(s),'edges':e,'labeled_graphs':n} for (s,e),n in forms.items()],'case_deductions':values,'minimum_deduction':min(values.values()),'scope':'Checks constants, feasible triple-event inequalities, all rank<=2 heavy graph forms, and the proof case arithmetic. Analytic support arguments and forest/Bonferroni directions are supplied in SIX_RED_PROOF.md; no H or four-set family enumeration.','cpu_seconds':time.process_time()-st}
(P/'SIX_RED_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
