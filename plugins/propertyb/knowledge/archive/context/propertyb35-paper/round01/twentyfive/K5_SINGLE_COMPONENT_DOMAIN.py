"""Single real K5 component only: two outside points on one trace edge.
For |T|=j<=3, a fixed outside point has another outside point of that edge
with pair codegree <= 1+floor(4/(4-j)). No outer five-group assumption.
"""
from pathlib import Path
from itertools import combinations_with_replacement,product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());six=json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text());ids=[1,5,7,8,9,10,18,23,24,26]
# Canonical unordered partitions, generated independently of all old scripts.
parts={()}
for i in range(5):
 new=set()
 for pp in parts:
  new.add(tuple(sorted(pp+(1<<i,))))
  for k,t in enumerate(pp):new.add(tuple(sorted(pp[:k]+pp[k+1:]+(t|(1<<i),))))
 parts=new
parts.remove((31,));assert len(parts)==51

def split(mu,p,r,q):
 ns=Counter()
 for t,c in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);v=q.get(t,0)
  cells=[c-a-b+v,a-v,b-v,v]
  if min(cells)<0:return None
  for mask,n in zip([t,t+32,t+64,t+96],cells):ns[mask]+=n
 ns={t:c for t,c in ns.items() if c}
 if any(t.bit_count()>5 for t in ns):return None
 assert sum(ns.values())==35 and all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(7))
 assert all(sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(5) for j in range(i+1,7))
 assert sum(c for t,c in ns.items() if t&96==96)==sum(q.values())
 return ns
out=[]
for ident in ids:
 mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};s=next((z for z in six['families'] if z['id']==ident),None)
 pp=sorted(tuple(sorted(p)) for p in s['residual_partitions']) if s else sorted(p for p in parts if all(mu.get(t,0) for t in p) and mu[0]>=7-len(p))
 byT=[];casesT={}
 for T in sorted(t for t,c in mu.items() if c and 1<=t.bit_count()<=3):
  L=1+4//(4-T.bit_count());eligible=[p for p in pp if T in p];cases=[]
  for p,r in combinations_with_replacement(eligible,2):
   other=sorted(set(p)&set(r)-{T})
   for bits in product([0,1],repeat=len(other)):
    for q0 in range(min(7-len(p),7-len(r))+1):
     q={T:1,**{t:v for t,v in zip(other,bits) if v}}
     if q0:q[0]=q0
     if sum(q.values())>L:continue
     ns=split(mu,p,r,q)
     if ns is not None:cases.append(dict(id=ident,T=T,codegree=sum(q.values()),P=p,Q=r,joint=q,counts=ns))
  byT.append(dict(T=T,size=T.bit_count(),pair_codegree_bound=L,eligible_partitions=len(eligible),cases=len(cases)));casesT[T]=cases
 # Three-point traces gave much stronger pilot bounds. The only inventory
 # without one is23; for it use the smallest remaining two-point domain.
 preferred=[z for z in byT if z['size']==3] or byT
 chosen=min(preferred,key=lambda z:(z['cases'],z['size'],z['T']))
 out.append(dict(id=ident,mu=mu,initial_partitions=pp,full_G_edge=bool(mu.get(31)),by_trace=byT,chosen_T=chosen['T'],cases=casesT[chosen['T']]))
summary=dict(scope=__doc__,inventories=ids,chosen_cases=sum(len(r['cases']) for r in out),all_trace_cases=sum(x['cases'] for r in out for x in r['by_trace']),elapsed_seconds=time.perf_counter()-st)
(P/'K5_SINGLE_COMPONENT_DOMAIN.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2));print([(r['id'],r['chosen_T'],len(r['cases']),[(x['T'],x['size'],x['cases']) for x in r['by_trace']]) for r in out])
