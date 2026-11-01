from pathlib import Path
from fractions import Fraction
from itertools import permutations
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from average_actual_low import rawrows,average
from multilock import json_value
start=time.perf_counter();source=json.loads(Path(__file__).with_name('SEVEN_LOW_AVERAGE.json').read_text());s=7
tr=lambda t,p:sum(1<<p[i] for i in range(s) if t&(1<<i));allperm=list(permutations(range(s)));groups={}
for x in source['groups']:
 if Fraction(x['best']['bound'])<1:continue
 ns={int(t):n for t,n in x['counts'].items()};key=tuple(sorted(ns.items()));auto=[p for p in allperm if tuple(sorted((tr(t,p),n) for t,n in ns.items()))==key]
 groups[x['group']]=dict(source=x,counts=ns,auto=auto,best=None)
layouts=[tuple(range(9,16)),tuple(range(10,17)),(10,11,12,13,14,23,24),(9,10,11,12,13,14,16),(9,10,11,12,13,15,16)]
for pos in layouts:
 rs=rawrows(24,s,pos)
 for gid,g in groups.items():
  if g['best'] and g['best']['bound']<1:continue
  seen=set()
  for perm in allperm:
   counts={tr(t,perm):n for t,n in g['counts'].items()};key=tuple(sorted(counts.items()))
   if key in seen:continue
   seen.add(key);inv=tuple(perm.index(i) for i in range(s));auto=[tuple(perm[p[inv[i]]] for i in range(s)) for p in g['auto']]
   z=average(counts,24,s,pos,rs,perms=auto);z['source_relabeling']=perm;z['used_auto']=auto
   if g['best'] is None or z['bound']<g['best']['bound']:g['best']=z
   if z['bound']<1:break
  print(gid,pos,'best',g['best']['bound'],'auto',len(g['auto']),'orders',len(seen),'sec',time.perf_counter()-start,flush=True)
  out=[dict(group=h,**g['best']) for h,g in groups.items() if g['best']]
  Path(__file__).with_name('SEVEN_AUTO_AVERAGE.json').write_text(json.dumps(json_value(dict(elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>180:print('BUDGET_STOP',flush=True);raise SystemExit
