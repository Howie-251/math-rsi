"""Five K6-top edges: bounded six-lock pilot and exact packing-domain census."""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction
import sys,time,json
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();CPU_LIMIT=14
vertices=range(5)
blocks=[tuple(t) for size in [2,3,4] for t in combinations(vertices,size)]
covered=[frozenset(combinations(t,2)) for t in blocks]
packings=[]
def rec(k,used,chosen):
 if k==len(blocks):packings.append(tuple(chosen));return
 rec(k+1,used,chosen)
 if not used&covered[k]:rec(k+1,used|covered[k],chosen+[k])
rec(0,frozenset(),[])
assert len(packings)==2624

def inventory(ds,pp):
 ns={63^(1<<(i+1)):1 for i in range(5)};ns[1]=4
 h=[0]*5
 for j in pp:
  mask=sum(1<<(i+1) for i in blocks[j]);assert mask not in ns
  ns[mask]=1
  for i in blocks[j]:h[i]+=1
 for i,d in enumerate(ds):ns[1<<(i+1)]=d-4-h[i]
 ns[0]=35-sum(ns.values());assert min(ns.values())>=0
 assert sum(ns.values())==35
 assert [sum(n for t,n in ns.items() if t>>i&1) for i in range(6)]==[9]+list(ds)
 return ns
# Canonical under true degree-class permutations, no permutation of q0 with yi.
def canon(ds,pp):
 masks=[sum(1<<i for i in blocks[j]) for j in pp]
 out=[]
 for perm in permutations(range(5)):
  if any(ds[i]!=ds[perm[i]] for i in range(5)):continue
  out.append(tuple(sorted(sum(1<<perm[i] for i in range(5) if m>>i&1) for m in masks)))
 return min(out)
census=[];domains=[]
for n8 in range(6):
 ds=tuple([8]*n8+[9]*(5-n8));dd=[];reps={}
 for pp in packings:
  w=[sum(len(blocks[j])-1 for j in pp if i in blocks[j]) for i in range(5)]
  if any(w[i]>4*ds[i]-31 for i in range(5)):continue
  dd.append(pp);reps.setdefault(canon(ds,pp),pp)
 domains.append((ds,dd,reps));census.append(dict(eight_count=n8,labelled=len(dd),orbits=len(reps)))
# Most symmetric degree-nine case, including empty and nontrivial maximal packings.
first=[(),tuple(i for i,b in enumerate(blocks) if len(b)==2),
       tuple(blocks.index(b) for b in [(0,1,2,3),(0,4),(1,4),(2,4),(3,4)]),
       tuple(blocks.index(b) for b in [(0,1,2),(0,3,4),(1,3),(1,4),(2,3),(2,4)])]
out=[]
for pp in first:
 ds=(9,)*5;ns=inventory(ds,pp);e=SubsetEngine(21,6,ns);z=e.verify(e.solve())
 out.append(dict(kind='symmetric_max_degree_pilot',degrees=[9]+list(ds),blocks=[blocks[j] for j in pp],counts=ns,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
 if time.process_time()-st>=CPU_LIMIT:break
result=dict(scope=__doc__,all_packings=len(packings),census=census,pilot_cases=out,pilot_complete=len(out)==len(first),all_inventory_bounds_evaluated=False,cpu_seconds=time.process_time()-st)
(P/'PILOT.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
print(json.dumps({k:v for k,v in json_value(result).items() if k!='pilot_cases'},indent=2))
for z in out:print(z['blocks'],str(z['bound']),z['positions'])
