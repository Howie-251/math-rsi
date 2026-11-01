from pathlib import Path
from itertools import combinations
import json
P=Path(__file__).resolve().parent
src=json.loads((P/'PROFILE.json').read_text());bad=[];tested=0
for row in src['records']:
 c=row['cells'];ff=row['forbidden_cells'];q=row['q'];A=[set() for _ in range(3)];x=0;F=set()
 for mask,(sz,fsz) in enumerate(zip(c,ff),1):
  vv=set(range(x,x+sz));F.update(range(x,x+fsz));x+=sz
  for j in range(3):
   if mask>>j&1:A[j].update(vv)
 A=[aa-F for aa in A];U=sorted(set.union(*A));mins=[]
 for k in [1,2,3]:
  for z in combinations(U,k):
   if all(set(z)&aa for aa in A) and not any(set(w)<=set(z) for w in mins):mins.append(z)
 if any(len(z)==1 for z in mins):continue
 forced=[z for z in mins if len(z)==2];T=[set(z) for z in mins if len(z)==3];gains=sorted([sum(set(pair)<=z for z in T) for pair in combinations(U,2)],reverse=True)
 exceptions=[]
 for p in range(len(forced),min((24-9*q)//4,(12-3*q)//2)+1):
  t=min(24-9*q-4*p,12-3*q-2*p);tested+=1
  deficit=len(T)-sum(gains[:p-len(forced)])-t
  if deficit<=0:exceptions.append(dict(p=p,t=t,T=len(T),gains=gains[:p-len(forced)],deficit=deficit))
 if exceptions:bad.append(dict(cells=c,Fcells=ff,q=q,P=len(forced),exceptions=exceptions))
out=dict(tested_budgets=tested,coarse_bound_exceptions=len(bad),exceptions=bad)
(P/'COARSE_BOUND.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
