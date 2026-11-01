"""Independent complete m4 replay.
Domain: separate quadruple/triple/pair Venn counts by surplus weight.
F: actual vertex subsets, quotient only by their seven/fifteen-cell multiplicities.
Candidates: enumerate free subsets and test their private hit bits.
No screen source import, no Cartesian-product candidate generation, no solver.
"""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();checkpoint=None
pairs=[m for m in range(1,16) if m.bit_count()==2];triples=[m for m in range(1,16) if m.bit_count()==3]
def compositions(total,length):
 if length==1:yield (total,);return
 for z in range(total+1):
  for tail in compositions(total-z,length-1):yield (z,)+tail
families=set();raw=0
for nquad in [0,1]:
 for nt in product(range(3),repeat=4):
  remaining=5-3*nquad-2*sum(nt)
  if remaining<0:continue
  for pair_total in range(remaining+1):
   for np in compositions(pair_total,6):
    d=dict(zip(pairs,np));d.update(zip(triples,nt));d[15]=nquad
    occ=[sum(size for m,size in d.items() if m>>j&1) for j in range(4)]
    if max(occ)>4:continue
    d.update({1<<j:4-occ[j] for j in range(4)});cc=tuple(d.get(m,0) for m in range(1,16));raw+=1
    support=[tuple(m for m in range(1,16) if m>>j&1 and cc[m-1]) for j in range(4)]
    if len(set(support))==4:families.add(cc)
assert raw==822 and len(families)==798
screen=json.loads((P/'FOUR_DEGREE_SCREEN.json').read_text());assert screen['summary']['complete'];assert families==set(map(tuple,screen['families']))
lookup={(tuple(screen['families'][r['family_id']]),tuple(r['Fcells'])):r for r in screen['records']}
compared=0;byq=Counter();budgets=0;degree_exclusions=0;count_exclusions=0;min_degree_gap=None;records=[]
for cc in sorted(families):
 membership=[]
 for m,num in enumerate(cc,1):membership.extend([m]*num)
 v=len(membership);representatives={}
 for q in range(3):
  for FF in combinations(range(v),q):
   signature=tuple(sorted(membership[x] for x in FF))
   if signature not in representatives:representatives[signature]=FF
 for signature,FF in representatives.items():
  F=set(FF);q=len(F);free=[x for x in range(v) if x not in F];T={k:[] for k in range(1,5)}
  for k in range(1,5):
   for vv in combinations(free,k):
    allbits=0;many=0
    for x in vv:many|=allbits&membership[x];allbits|=membership[x]
    if allbits!=15:continue
    private=allbits&~many
    if all(membership[x]&private for x in vv):T[k].append(vv)
  sizes=[len(T[k]) for k in range(1,5)];prior=lookup[cc,signature];assert prior['candidates']==sizes
  compared+=1;byq[q]+=1
  if T[1]:continue
  c23=Counter();c24=Counter();c34=Counter()
  for z in T[3]:c23.update(combinations(z,2))
  for z in T[4]:c24.update(combinations(z,2));c34.update(combinations(z,3))
  K23=max(c23.values(),default=0);K24=max(c24.values(),default=0);K34=max(c34.values(),default=0);assert prior['K']==[K23,K24,K34]
  p0=len(T[2]);u=len(free);a_occ=sum(membership[x].bit_count() for x in free);cap=7*u+7-a_occ;assert (prior['degree_capacity'],prior['free_points'],prior['positive_free_occ'])==(cap,u,a_occ)
  for p in range(p0,min((24-9*q)//4,(8-3*q)//2)+1):
   required3=max(0,len(T[3])-(p-p0)*K23)
   for t in range(required3,min(24-9*q-4*p,8-3*q-2*p)+1):
    budgets+=1;needed4=max(0,len(T[4])-(p-p0)*K24-(t-required3)*K34)
    if needed4>28-q-p-t:count_exclusions+=1;continue
    inc=2*p+3*t+4*needed4;assert inc>cap
    degree_exclusions+=1;gap=inc-cap;min_degree_gap=gap if min_degree_gap is None else min(min_degree_gap,gap)
  if checkpoint is None and time.perf_counter()-st>=10:
   checkpoint=dict(states=compared,elapsed_seconds=time.perf_counter()-st);print('10sec_profile',json.dumps(checkpoint),flush=True)
  if time.perf_counter()-st>110:raise RuntimeError('110 second bounded replay reached; no complete result')
assert compared==23393 and dict(byq)=={0:798,1:5206,2:17389} and compared==len(lookup)
result=dict(passed=True,scope=__doc__,raw_families=raw,distinct_positive_families=len(families),states=compared,by_q=dict(byq),candidate_and_cost_records_match=True,budget_comparisons=budgets,excluded_by_edge_count=count_exclusions,excluded_by_degree=degree_exclusions,minimum_degree_gap=min_degree_gap,ten_second_checkpoint=checkpoint,elapsed_seconds=time.perf_counter()-st)
(P/'FOUR_DEGREE_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
