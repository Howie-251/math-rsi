"""Complete local 111/211 three-external-point domains for inventories 1,9.
Uses seven-lock residual crosspair graphs. No full H is enumerated.
"""
from pathlib import Path
from itertools import combinations_with_replacement,product
from collections import Counter
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());old=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_REPLAY.json').read_text())
def inventory(mu,ps,T,mode,U=None):
 ns=Counter()
 for t,c in mu.items():
  m=[c]+[int(t in pp) if t else 7-len(pp) for pp in ps]+[0]*4
  # bit masks 1,2,4 are the three external points. For mode211,
  # points0,1 share the additional edge in G-trace U.
  vals={0:c,1:m[1],2:m[2],4:m[3],3:int(t==T)+int(mode=='211' and t==U),5:int(t==T),6:int(t==T),7:int(t==T)}
  cells={s:sum((-1)**((r^s).bit_count())*v for r,v in vals.items() if r&s==s) for s in range(8)}
  if min(cells.values())<0:return None
  for s,n in cells.items():ns[t|(s<<5)]+=n
 ns={t:c for t,c in ns.items() if c}
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(8))
 for i in range(8):
  for j in range(i+1,8):
   target=2 if j<5 or (mode=='211' and (i,j)==(5,6)) else 1
   assert sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==target
 assert sum(c for t,c in ns.items() if t&224==224)==1 and ns.get(T|224)==1
 return ns
out=[]
for ident in [1,9]:
 mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};ps=[tuple(p) for r in old['arc_pruning'] if r['id']==ident for p in r['remaining_partitions']];zs=[z for z in old['results'] if z['id']==ident];Ts=sorted(t for t in [1,2,4,8,16] if mu.get(t,0));cases=[];stats=[]
 for T in Ts:
  pp=[p for p in ps if T in p];edges={frozenset((tuple(sorted(z['P'])),tuple(sorted(z['Q'])))) for z in zs if z['T']==T and Q(z['bound'])>=1};n111=n211=0
  for aa in combinations_with_replacement(pp,3):
   if not all(frozenset((aa[i],aa[j])) in edges for i,j in [(0,1),(0,2),(1,2)]):continue
   ns=inventory(mu,aa,T,'111')
   if ns is not None:cases.append(dict(id=ident,T=T,mode='111',partitions=aa,U=None,counts=ns));n111+=1
  for a,b in combinations_with_replacement(pp,2):
   for c in pp:
    if not all(frozenset((q,c)) in edges for q in [a,b]):continue
    for U in [0]+sorted(set(a)&set(b)-{T}):
     if U&T or U.bit_count()>3:continue
     ns=inventory(mu,[a,b,c],T,'211',U)
     if ns is not None:cases.append(dict(id=ident,T=T,mode='211',partitions=[a,b,c],U=U,counts=ns));n211+=1
  stats.append(dict(T=T,eligible_partitions=len(pp),mode111=n111,mode211=n211,total=n111+n211))
 out.append(dict(id=ident,mu=mu,by_trace=stats,cases=cases))
summary=dict(scope=__doc__,inventories=[1,9],cases=sum(len(r['cases']) for r in out),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_THREE_EXTERNAL_STARS_DOMAIN.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2));print([(r['id'],r['by_trace']) for r in out])
