from pathlib import Path
from fractions import Fraction
from itertools import permutations
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from average_actual_low import rawrows,average
from mixed_six import trans
from multilock import json_value
start=time.perf_counter();source=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low6_badnone.json').read_text());allperm=list(permutations(range(6)));groups={}
for x in source['results']:
 if Fraction(x['bound'])<1 or x['group']==0:continue
 ns={int(t):n for t,n in x['counts'].items()};key=tuple(sorted(ns.items()));auto=[p for p in allperm if tuple(sorted((trans(t,p),n) for t,n in ns.items()))==key]
 groups[x['group']]=dict(source=x,counts=ns,auto=auto,best=None)
layouts=[tuple(range(a,a+6)) for a in (10,9,8,7,11)]+[(10,11,12,13,14,24),(9,10,11,12,13,24),(10,11,12,13,23,24),(8,9,10,11,12,14)]
for pos in layouts:
 rs=rawrows(24,6,pos)
 for gid,g in groups.items():
  if g['best'] and g['best']['bound']<1:continue
  seen=set()
  for perm in allperm:
   moved=tuple(pos[perm[i]] for i in range(6));canon=min(tuple(moved[p[i]] for i in range(6)) for p in g['auto'])
   if canon in seen:continue
   seen.add(canon)
   counts={trans(t,perm):n for t,n in g['counts'].items()};inv=tuple(perm.index(i) for i in range(6));auto=[tuple(perm[p[inv[i]]] for i in range(6)) for p in g['auto']]
   z=average(counts,24,6,pos,rs,perms=auto);z['source_relabeling']=perm;z['used_auto']=auto
   if g['best'] is None or z['bound']<g['best']['bound']:g['best']=z
   if z['bound']<1:break
  print(gid,pos,'best',g['best']['bound'],'auto',len(g['auto']),'orders',len(seen),'sec',time.perf_counter()-start,flush=True)
  out=[dict(group=h,auto=g['auto'],**g['best']) for h,g in groups.items() if g['best']]
  Path(__file__).with_name('AUTOMORPHISM_AVERAGE.json').write_text(json.dumps(json_value(dict(elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>180:print('BUDGET_STOP',flush=True);raise SystemExit
