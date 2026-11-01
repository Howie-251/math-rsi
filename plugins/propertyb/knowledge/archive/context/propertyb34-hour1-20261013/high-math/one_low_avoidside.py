"""Complete residual probe with one actual low bad-pair edge avoiding all high locks."""
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
start=time.perf_counter();eng=Engine(24,6);out=[];allperms=list(permutations(range(6)));base=[];infeasible=[]
for suffix in ('none','6','6_24'):
 path=Path(__file__).with_name('MIXED_SIX_v24_low1_bad'+suffix+'.json')
 if not path.exists():raise RuntimeError('missing '+str(path))
 source=json.loads(path.read_text())
 for x in source['results']:
  if Fraction(x['bound'])<1:base.append(dict(source=path.name,group=x['group'],bound=x['bound']));continue
  ns={int(t):n for t,n in x['counts'].items()};key=tuple(sorted(ns.items()));ts=sorted(t for t in ns if t&1);slots=[]
  pure=max(0,(4*ns.get(1,0)-18+2)//3)
  for t in ts:
   cap=comb(ns.get(1,0),2) if t==1 else ns.get(1,0)*ns[t]
   if cap and (pure==0 or t==1):slots.append((1,t))
  if not slots:infeasible.append(dict(source=path.name,group=x['group'],reason='No positive-capacity low slot with a pure member'));continue
  auto=[p for p in allperms if tuple(sorted((trans(t,p),n) for t,n in ns.items()))==key];seen_slots=set()
  for slot in slots:
   canon=min(tuple(sorted(trans(t,p) for t in slot)) for p in auto)
   if canon in seen_slots:continue
   seen_slots.add(canon);seen=set();best=None
   order=sorted(range(6),key=lambda i:x['positions'][i]);priority=tuple(order.index(i) for i in range(6));perms=[priority]+allperms
   for perm in perms:
    counts={trans(t,perm):n for t,n in ns.items()};st=tuple(sorted(trans(t,perm) for t in slot));ky=tuple(sorted(counts.items())),st
    if ky in seen:continue
    seen.add(ky);z=eng.solve(counts,{perm[0]:st})
    if best is None or z['bound']<best['bound']:best=dict(relabeling=perm,counts=counts,center=perm[0],actual_slot=st,**z)
    if z['bound']<1:break
   pos=best['positions'];p=Profile(24,5,pos,best['counts']);cs=[certificate(p,i) for i in range(6)];losses={pos[i]:cs[i]['loss'] for i in range(6)};j=best['center'];t,u=best['actual_slot'];losses[pos[j]]=pair_weight(24,5,pos,t,u,pos[j])+pair_weight(24,5,pos,u,t,pos[j]);rs=rows(p,deductions=losses);assert total_bound(rs)==best['bound']
   stubs=[frozenset(i+1 for i in range(6) if t&(1<<i)) for t,n in p.counts.items() for _ in range(n)];ir=independent_rows(24,pos,stubs);assert all(all(a[k]==b[k] for k in ('A','B','C')) for a,b in zip(rs,ir))
   out.append(dict(source=path.name,group=x['group'],original_slot=slot,orders=len(seen),rows=rs,independent_ABC=True,**best));print(suffix,x['group'],slot,best['bound'],'orders',len(seen),'sec',time.perf_counter()-start,flush=True)
   Path(__file__).with_name('ONE_LOW_AVOIDSIDE.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=False,elapsed=time.perf_counter()-start,base=base,infeasible=infeasible,results=out)),indent=2)+'\n')
   if time.perf_counter()-start>180:print('BUDGET_STOP',flush=True);raise SystemExit
Path(__file__).with_name('ONE_LOW_AVOIDSIDE.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,elapsed=time.perf_counter()-start,base=base,infeasible=infeasible,results=out)),indent=2)+'\n')
