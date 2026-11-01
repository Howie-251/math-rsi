"""Independent direct check of the first m4 count residual and its degree obstruction."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
P=Path(__file__).resolve().parent
A=[{0,1,2,10},{3,4,9,10},{5,6,9,10},{7,8,9,10}];F={9,10};U=set.union(*A)-F
R=[set(z) for z in combinations(sorted(U),4) if all(set(z)&aa for aa in A)]
assert len(R)==24 and len(U)==9 and 16-len(set.union(*A))==5
assert not any(all(set(z)&aa for aa in A) for size in [1,2,3] for z in combinations(sorted(U),size))
K2=max(sum(set(b)<=z for z in R) for b in combinations(sorted(U),2));K3=max(sum(set(b)<=z for z in R) for b in combinations(sorted(U),3));assert (K2,K3)==(6,3)
rows=[]
for p in range(5):
 for t in range(9):
  if 18+4*p+t<=24 and 6+2*p+t<=8:
   remaining=max(0,24-K2*p-K3*t);inc=2*p+3*t+4*remaining
   rows.append(dict(p=p,t=t,required_negative4=remaining,free_negative_incidence=inc,required_free_excess=max(0,inc+9-7*9)))
assert min(z['free_negative_incidence'] for z in rows)==74
assert min(z['required_free_excess'] for z in rows)==20
# A signed-set realization of the weak cost-only obstruction, not an H.
negative=[{9},{10}]+R+[R[0],R[0]]
assert len(negative)==28 and all(any(b<=z for b in negative) for z in R)
occ=Counter(x for b in negative for x in b)
positive=Counter(x for a in A for x in a)
assert sum(max(0,positive[x]+occ[x]-7) for x in U)>=42
out=dict(passed=True,scope=__doc__,A=[sorted(z) for z in A],F=sorted(F),free_points=sorted(U),candidate4_count=24,max_pair_coverage=K2,max_triple_coverage=K3,all_feasible_small_blocker_counts=rows,minimum_required_free_excess=20,actual_global_excess_upper_bound=7,cost_only_signed_model_negative=[sorted(z) for z in negative],signed_model_is_actual_H=False)
(P/'FOUR_RESIDUAL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['A','F','free_points','cost_only_signed_model_negative']},indent=2))
