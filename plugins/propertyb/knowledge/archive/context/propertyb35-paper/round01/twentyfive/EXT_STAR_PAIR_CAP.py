"""New multiplicity caps on id10's complete 21-partition residual domain.
Use LP/MIP only to propose a positive integer witness; exact checks and a
separate pure-Python replay certify what the witness actually satisfies.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction as Q
import json,time
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
P=Path(__file__).resolve().parent;st=time.perf_counter();ident=10
mu={int(t):c for t,c in json.loads((P/'GROUP5_CATALOGUE.json').read_text())['representatives'][ident]['counts'].items()}
parts=next(f['residual_partitions'] for f in json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text())['families'] if f['id']==ident)
nu={t:(5-t.bit_count())*c for t,c in mu.items() if t};ts=sorted(nu);single={t for t,c in mu.items() if t and c==1}
caps=[min(min(nu[t] for t in p),1 if len(set(p)&single)>=3 else 20) for p in parts]
A=np.array([[int(t in pp) for pp in parts] for t in ts]);rhs=np.array([nu[t] for t in ts]);n=len(parts)
conflicts=[(i,j) for i,j in combinations(range(n),2) if len(set(parts[i])&set(parts[j])&single)>=3]
assert not conflicts
lp=linprog(-np.ones(n),A_ub=A,b_ub=rhs,bounds=[(0,u) for u in caps],method='highs')
sol=milp(np.zeros(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),caps),constraints=LinearConstraint(A,rhs,rhs),options={'time_limit':10})
assert sol.success and sol.x is not None
vals=[int(round(float(x))) for x in sol.x];assert all(abs(v-float(x))<1e-8 for v,x in zip(vals,sol.x))
assert all(0<=v<=u for v,u in zip(vals,caps)) and sum(vals)==20
marg=Counter()
for pp,v in zip(parts,vals):
 for t in pp:marg[t]+=v
assert dict(marg)==nu
# Exact fractional packing upper certificate: y_T=|T|/5.
y={t:Q(t.bit_count(),5) for t in ts};assert all(sum(y[t] for t in pp)==1 for pp in parts)
upper=sum(y[t]*nu[t] for t in ts);assert upper==20
expanded=[set(pp) for pp,v in zip(parts,vals) for _ in range(v)];parent=list(range(20));forced=[];triple=[]
def find(i):
 while parent[i]!=i:i=parent[i]
 return i
for i,j in combinations(range(20),2):
 co=sorted(expanded[i]&expanded[j]&single)
 if len(co)>=2:parent[find(i)]=find(j);forced.append(dict(vertices=[i,j],shared_unique_blocks=co))
 if len(co)>=3:triple.append(dict(vertices=[i,j],shared_unique_blocks=co))
assert not triple
comps={}
for i in range(20):comps.setdefault(find(i),[]).append(i)
comps=sorted(comps.values(),key=lambda c:(-len(c),c));assert max(map(len,comps))<=5
# Additional necessary condition from the newly proved absence of four-point
# group traces: a unique singleton-G edge's four outside vertices cannot all
# be put in the same outer group.
forbidden={t:{i for i,pp in enumerate(expanded) if t in pp} for t in single if t.bit_count()==1}
assert all(len(ss)==4 for ss in forbidden.values())
bins=[set() for _ in range(4)];nodes=0
# Identical bins are symmetric; component membership is otherwise preserved.
def pack(i):
 global nodes
 nodes+=1
 if i==len(comps):return all(len(b)==5 for b in bins)
 seen=set();cc=set(comps[i])
 for j in range(4):
  key=frozenset(bins[j])
  if key in seen or len(bins[j])+len(cc)>5:continue
  seen.add(key);merged=bins[j]|cc
  if any(ss<=merged for ss in forbidden.values()):continue
  bins[j]=merged
  if pack(i+1):return True
  bins[j]-=cc
 return False
pack_ok=pack(0);assert pack_ok
assert all(len(b)==5 for b in bins) and set().union(*bins)==set(range(20))
assert all(not(ss<=b) for ss in forbidden.values() for b in bins)
out=dict(scope=__doc__,id=10,mu=mu,nu=nu,partition_domain=parts,single_capacity_traces=sorted(single),multiplicity_caps=caps,caps_sum=sum(caps),capped_partition_indices=[i for i,p in enumerate(parts) if len(set(p)&single)>=3],distinct_partition_three_unique_conflicts=conflicts,lp_status=dict(success=bool(lp.success),message=str(lp.message),packing_maximum_float=None if not lp.success else float(-lp.fun)),exact_LP_upper_certificate=dict(trace_weights={t:str(w) for t,w in y.items()},upper=str(upper)),solver_status=dict(success=bool(sol.success),message=str(sol.message)),integer_multiplicities=vals,partition_multiset=[dict(blocks=p,multiplicity=v) for p,v in zip(parts,vals) if v],twenty_partitions=[sorted(p) for p in expanded],forced_same_group_edges=forced,components=comps,outer_group_assignment=[sorted(b) for b in bins],unique_singleton_edge_outside_sets={t:sorted(ss) for t,ss in forbidden.items()},packing_nodes=nodes,no_four_trace_necessary_condition_satisfied=True,scope_of_positive_witness='partition marginals, unique-trace pair caps and one outer-group packing only; no complete H is constructed',elapsed_seconds=time.perf_counter()-st)
(P/'EXT_STAR_PAIR_CAP.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(id=10,partitions=n,cap_sum=sum(caps),cap1_count=len(out['capped_partition_indices']),integer_witness=True,component_sizes=list(map(len,comps)),packing_nodes=nodes,no_four_trace_check=True,elapsed_seconds=out['elapsed_seconds']),indent=2))
