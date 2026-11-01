"""Six chosen actual G-inventory + external-point partition cases.
All 18 no-full-G inventory partition domains are generated, but only six
nontrivial profiles receive six-lock DP. No H or outer-group identity is fixed.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;root=P.parents[3]
sys.dont_write_bytecode=True;sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());alive={r['id'] for r in json.loads((P/'GROUP5_PARTITIONS.json').read_text())['results'] if r['status']=='FEASIBLE'}
parts=[]
def rec(i,bs):
 if i==5:
  if bs!=[31]:parts.append(tuple(bs))
  return
 for j in range(len(bs)):
  bb=bs.copy();bb[j]|=1<<i;rec(i+1,bb)
 rec(i+1,bs+[1<<i])
rec(0,[]);assert len(parts)==51 and len(set(parts))==51

def extend(mu,part):
 ns=Counter(mu)
 for t in part:ns[t]-=1;ns[t|32]+=1
 ns[0]-=7-len(part);ns[32]+=7-len(part)
 ns={t:c for t,c in ns.items() if c};assert min(ns.values())>=0
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(6))
 assert all(sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(6) for j in range(i+1,6))
 projection=Counter()
 for t,c in ns.items():projection[t&31]+=c
 assert dict(projection)==dict(mu)
 return ns
families=[]
for r in cat['representatives']:
 if r['id'] not in alive or r['counts'].get('31',0):continue
 mu={int(t):c for t,c in r['counts'].items()};ps=[p for p in parts if all(mu.get(t,0) for t in p) and mu.get(0,0)>=7-len(p)]
 for p in ps:extend(mu,p)
 families.append(dict(id=r['id'],mu=mu,partitions=[list(p) for p in ps]))
assert len(families)==18
requests=[(1,2),(11,2),(17,2),(22,2),(16,3),(18,3)]
results=[]
for ident,k in requests:
 f=next(f for f in families if f['id']==ident);part=next(p for p in f['partitions'] if len(p)==k);ns=extend(f['mu'],part);start=time.perf_counter()
 eng=SubsetEngine(25,6,ns);z=eng.verify(eng.solve());row=z['rows'][z['positions'][5]-1]
 raw=sum(min(r['A'],r['B'],r['C']) for r in z['rows'])
 xgain=min(row['A'],row['B'],row['C'])-row['bound']
 results.append(dict(id=ident,partition=part,partition_size=k,dp_seconds=time.perf_counter()-start,x_singleton_count=ns.get(32,0),x_certificate=z['certificates'][5],no_quota_bound_at_same_layout=raw,x_quota_improvement_at_same_layout=xgain,x_row=row,**z))
 print(ident,part,'bound',z['bound'],'xq',z['certificates'][5],'xgain',xgain,'seconds',time.perf_counter()-start,flush=True)
summary=dict(scope=__doc__,no_full_G_families=18,total_admissible_partitions=sum(len(f['partitions']) for f in families),pilot_cases=len(results),strict=sum(z['bound']<1 for z in results),minimum=min(z['bound'] for z in results),maximum=max(z['bound'] for z in results),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_EXTERNAL_STAR_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,domain=families,results=results)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
