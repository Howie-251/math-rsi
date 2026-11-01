"""Fifteen named four-positive states, integer necessary blocker bounds only.
A nonstrict bound would not be an actual signed-system witness.
"""
from pathlib import Path
from itertools import product,combinations
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
families={
'disjoint':[{0,1,2,3},{4,5,6,7},{8,9,10,11},{12,13,14,15}],
'common_all':[{0,1,2,3},{0,4,5,6},{0,7,8,9},{0,10,11,12}],
'common_all_plus_two_pairs':[{0,1,2,3},{0,1,4,5},{0,2,6,7},{0,8,9,10}],
'five_pair_intersections':[{0,1,2,5},{0,3,4,6},{1,3,7,8},{2,4,9,10}],
'overlap_three_plus_two':[{0,1,2,5},{0,1,2,6},{3,4,7,8},{3,4,9,10}]
}
results=[]
for name,A in families.items():
 excess=16-len(set.union(*A));assert excess<=5
 ranked=sorted(set.union(*A),key=lambda x:(-sum(x in a for a in A),x))
 for q in range(3):
  F=set(ranked[:q]);AA=[a-F for a in A];U=sorted(set.union(*AA));raw={frozenset(z) for z in product(*AA)};mins=[z for z in raw if not any(w<z for w in raw)];T={k:[z for z in mins if len(z)==k] for k in range(1,5)}
  row=dict(name=name,positive=[sorted(z) for z in A],repeat=excess,F=sorted(F),q=q,candidates={k:len(v) for k,v in T.items()})
  if T[1]:row['strict']=True;row['reason']='free_singleton';results.append(row);continue
  p0=len(T[2]);K23=max([sum(set(pair)<=z for z in T[3]) for pair in combinations(U,2)],default=0);K24=max([sum(set(pair)<=z for z in T[4]) for pair in combinations(U,2)],default=0);K34=max([sum(set(tri)<=z for z in T[4]) for tri in combinations(U,3)],default=0)
  row.update(forced_pairs=p0,K23=K23,K24=K24,K34=K34);possible=[];gaps=[]
  for p in range(p0,min((24-9*q)//4,(8-3*q)//2)+1):
   lower3=max(0,len(T[3])-(p-p0)*K23)
   for t in range(lower3,min(24-9*q-4*p,8-3*q-2*p)+1):
    upper4=(p-p0)*K24+(t-lower3)*K34+28-q-p-t;gap=len(T[4])-upper4;gaps.append(gap)
    if gap<=0:possible.append(dict(p=p,t=t,upper4=upper4))
  row.update(strict=not possible,min_gap=min(gaps,default=None),remaining_budget_options=possible);results.append(row)
out=dict(scope=__doc__,states=len(results),strict=sum(z['strict'] for z in results),elapsed_seconds=time.perf_counter()-st,results=results)
(P/'FOUR_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2));print([(z['name'],z['q'],z['strict'],z.get('min_gap')) for z in results])
