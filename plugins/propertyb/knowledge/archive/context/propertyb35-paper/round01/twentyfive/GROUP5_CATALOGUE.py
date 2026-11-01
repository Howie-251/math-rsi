"""Actual a5 group trace domain: K5 pair multiplicity2, trace size2..5.
Every block has multiplicity<=2; the five-element trace has multiplicity<=1.
Degree7 singleton and M35 empty counts are recovered, never freely chosen.
"""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();budget=15
pairs=[(1<<i)|(1<<j) for i,j in combinations(range(5),2)]
blocks=[t for t in range(1,32) if t.bit_count()>=2]
content={t:[j for j,p in enumerate(pairs) if p&t==p] for t in blocks}
by_pair={j:[t for t in blocks if j in content[t]] for j in range(10)}
perms=list(permutations(range(5)))
transforms=[[sum(1<<p[i] for i in range(5) if t>>i&1) for t in range(32)] for p in perms]
raw=feasible=nodes=0;orbits={};representatives=[];complete=True
class Budget(Exception):pass

def visit(rem,picked,start=0):
 global raw,feasible,nodes
 nodes+=1
 if nodes%10000==0 and time.perf_counter()-st>budget:raise Budget
 if not any(rem):
  raw+=1;multi=dict(Counter(picked));singles=[7-sum(c for t,c in multi.items() if t>>i&1) for i in range(5)]
  empty=35-sum(multi.values())-sum(singles)
  if min(singles+[empty])<0:return
  feasible+=1;ns={**multi,**{1<<i:a for i,a in enumerate(singles) if a},0:empty};key=tuple(sorted(ns.items()))
  if key not in orbits:
   keys=[tuple(sorted((tr[t],c) for t,c in ns.items())) for tr in transforms]
   canonical=min(keys);idx=len(representatives)
   representatives.append(dict(id=idx,counts=dict(canonical),orbit_size=len(set(keys))))
   for key in keys:orbits[key]=idx
  return
 j=next(j for j,r in enumerate(rem) if r)
 for t in by_pair[j]:
  if t<start or (t==31 and t in picked):continue
  inds=content[t]
  if any(rem[k]==0 for k in inds):continue
  rr=list(rem)
  for k in inds:rr[k]-=1
  # When the same pivot still needs one copy, its chosen blocks are sorted.
  newstart=t if rr[j] else 0
  visit(tuple(rr),picked+[t],newstart)
try:visit((2,)*10,[])
except Budget:complete=False
out=dict(scope=__doc__,complete=complete,labelled_multicovers=raw,degree7_M35_feasible_labelled=feasible,orbits=len(representatives),orbit_sizes_sum=sum(r['orbit_size'] for r in representatives),recursion_nodes=nodes,elapsed_seconds=time.perf_counter()-st,representatives=representatives)
assert not complete or sum(r['orbit_size'] for r in representatives)==feasible
(P/'GROUP5_CATALOGUE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='representatives'},indent=2))
