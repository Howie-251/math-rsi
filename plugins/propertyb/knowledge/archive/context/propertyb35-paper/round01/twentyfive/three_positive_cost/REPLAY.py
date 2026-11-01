"""Independent integer-count replay: enumerate all seven Venn counts directly;
mark F by actual vertex subsets; generate minimal transversals from A1 x A2 x A3.
Use only a top-gain counting inequality, no cover recursion or optimization source.
"""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();families=0;simple=0;cases=0;feasible_budgets=0;table=Counter();maxslack=None
for cells in product(range(5),repeat=7):
 if sum(cells)<7:continue
 if any(sum(cells[mask-1] for mask in range(1,8) if mask>>j&1)!=4 for j in range(3)):continue
 families+=1;A=[set() for _ in range(3)];v=0
 for mask,size in enumerate(cells,1):
  points=set(range(v,v+size));v+=size
  for j in range(3):
   if mask>>j&1:A[j].update(points)
 if len({frozenset(a) for a in A})<3:continue
 simple+=1
 for q in range(3):
  for Ftuple in combinations(range(v),q):
   F=set(Ftuple);AA=[a-F for a in A];cases+=1
   raw={frozenset([x,y,z]) for x,y,z in product(*AA)};mins=[z for z in raw if not any(w<z for w in raw)]
   if any(len(z)==1 for z in mins):continue
   pp=[z for z in mins if len(z)==2];tt=[z for z in mins if len(z)==3];P0=len(pp)
   maxp=min((24-9*q)//4,(12-3*q)//2)
   if P0>maxp:continue
   X=[AA[i]&AA[j] for i,j in [(0,1),(0,2),(1,2)]]
   if q==0:assert sum(map(len,X))<=1 and P0 in [0,4]
   if q==1:assert sum(map(len,X))<=1 and P0 in [0,3]
   if q==2:assert not any(X) and P0==0
   K=max((sum(set(pair)<=z for z in tt) for pair in combinations(sorted(set.union(*AA)),2)),default=0)
   table[q,P0,len(tt),K]+=1
   for p in range(P0,maxp+1):
    tmax=min(24-9*q-4*p,12-3*q-2*p)
    gap=len(tt)-(p-P0)*K-tmax
    assert gap>0
    maxslack=gap if maxslack is None else min(maxslack,gap)
    feasible_budgets+=1
assert families==65 and simple==59
result=dict(passed=True,scope=__doc__,raw_Venn_families=families,simple_families=simple,actual_vertex_F_cases=cases,budget_comparisons=feasible_budgets,minimum_positive_gap=maxslack,count_table=[dict(q=q,forced_pairs=p,triples=t,max_pair_gain=k,multiplicity=m) for (q,p,t,k),m in sorted(table.items())],elapsed_seconds=time.perf_counter()-st)
(P/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='count_table'},indent=2))
