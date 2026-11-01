"""One low/five high, one high nonunit pair: full actual-low-slot residual probe."""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
from math import comb
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from fast_position_dp import Engine
from mixed_six import trans
from multilock import Profile,rows,total_bound,pair_weight,json_value
from pure_quota import certificate
from independent_structure_bounds import independent_rows
start=time.perf_counter();eng=Engine(24,6);out=[];allperms=list(permutations(range(6)))
source=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low1_bad6.json').read_text());dp=json.loads(Path(__file__).with_name('ONE_LOW_ALL_ORDERS.json').read_text());res={x['group']:x for x in dp['results'] if Fraction(x['bound'])>=1}
for x in source['results']:
 if x['group'] not in res:continue
 ns={int(t):n for t,n in x['counts'].items()};key=tuple(sorted(ns.items()));ts=sorted(t for t in ns if t&1);slots=[]
 pure=max(0,(4*ns.get(1,0)-18+2)//3)
 for i,t in enumerate(ts):
  for u in ts[i:]:
   cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
   if cap and t&u==1 and (pure==0 or (t,u)==(1,1)):slots.append((t,u))
 auto=[p for p in allperms if tuple(sorted((trans(t,p),n) for t,n in ns.items()))==key];seen_slots=set()
 for slot in slots:
  canon=min(tuple(sorted(trans(t,p) for t in slot)) for p in auto)
  if canon in seen_slots:continue
  seen_slots.add(canon);seen=set();best=None
  priority=res[x['group']]['relabeling'];perms=[tuple(priority)]+allperms
  for perm in perms:
   counts={trans(t,perm):n for t,n in ns.items()};st=tuple(sorted(trans(t,perm) for t in slot));ky=tuple(sorted(counts.items())),st
   if ky in seen:continue
   seen.add(ky);z=eng.solve(counts,{perm[0]:st})
   if best is None or z['bound']<best['bound']:best=dict(relabeling=perm,counts=counts,center=perm[0],actual_slot=st,**z)
   if z['bound']<1:break
  pos=best['positions'];p=Profile(24,5,pos,best['counts']);cs=[certificate(p,i) for i in range(6)];losses={pos[i]:cs[i]['loss'] for i in range(6)};j=best['center'];t,u=best['actual_slot'];losses[pos[j]]=pair_weight(24,5,pos,t,u,pos[j])+pair_weight(24,5,pos,u,t,pos[j]);rs=rows(p,deductions=losses);assert total_bound(rs)==best['bound']
  stubs=[frozenset(i+1 for i in range(6) if t&(1<<i)) for t,n in p.counts.items() for _ in range(n)];ir=independent_rows(24,pos,stubs);assert all(all(a[k]==b[k] for k in ('A','B','C')) for a,b in zip(rs,ir))
  out.append(dict(group=x['group'],original_slot=slot,orders=len(seen),rows=rs,independent_ABC=True,**best));print(x['group'],slot,best['bound'],'orders',len(seen),'sec',time.perf_counter()-start,flush=True)
  Path(__file__).with_name('ONE_LOW_ACTUAL_ALL.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=False,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>180:print('BUDGET_STOP',flush=True);raise SystemExit
Path(__file__).with_name('ONE_LOW_ACTUAL_ALL.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
