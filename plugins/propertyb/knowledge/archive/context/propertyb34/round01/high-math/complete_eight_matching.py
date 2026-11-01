"""Complete actual eighth-low extension after all seven-lock bounds finish.

All generated orbits retain a concrete strict projection or their own exact
eight-lock witness. Previous pilot arithmetic is reused by exact count equality.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from eighth_matching import extensions,canonical,graph,SubsetEngine,json_value

def drop(ns,i):
 out={}
 for t,n in ns.items():
  u=(t&((1<<i)-1))|((t>>(i+1))<<i);out[u]=out.get(u,0)+n
 return out

if __name__=='__main__':
 start=time.perf_counter();source=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING_BOUNDS.json').read_text());assert source['complete'] and source['low_count_limit']==3
 allseven=source['results'];good={tuple(sorted((int(t),n) for t,n in x['counts'].items())):dict(group=x['group'],bound=x['bound'],source='seven_direct') for x in allseven if Fraction(x['bound'])<1}
 for x in json.loads((HERE/'SEVEN_MATCHING_QMAX0_JOINT.json').read_text())['results']:
  if Fraction(x['bound'])<1:good[tuple(sorted((int(t),n) for t,n in x['counts'].items()))]=dict(group=x['group'],bound=x['bound'],source='q0_joint')
 bad=[x for x in allseven if Fraction(x['bound'])>=1 and x['low_count']>=1]
 seen={};raw=0;parents=[]
 for x in bad:
  ns={int(t):n for t,n in x['counts'].items()};degs=[sum(n for t,n in ns.items() if t&(1<<i)) for i in range(7)];matched={i for p in graph(ns,7) for i in p}
  for p in [None]+[i for i in range(7) if i not in matched and degs[i]==6]:
   nr=0
   for nc in extensions(ns,7,6,p):
    nr+=1;raw+=1;key=canonical(nc,8)
    if key not in seen:seen[key]=dict(counts=dict(key),source_group=x['group'],partner=p)
   parents.append(dict(group=x['group'],partner=p,raw=nr))
 print('GENERATED',len(bad),raw,len(seen),time.perf_counter()-start,flush=True)
 kept=[];covered=[]
 for j,x in enumerate(seen.values()):
  ns=x['counts'];witness=None
  for i in range(8):
   nd=drop(ns,i)
   if sum(sum(n for t,n in nd.items() if t&(1<<k))==6 for k in range(7))>3:continue
   key=canonical(nd,7)
   if key in good:witness=dict(dropped=i,**good[key]);break
  if witness is None:kept.append(dict(x,group=j))
  else:covered.append(dict(x,group=j,projection=witness))
 print('PROJECTED',len(covered),len(kept),time.perf_counter()-start,flush=True)
 catalogue=dict(complete=True,seven_count=len(allseven),seven_bad_groups=[x['group'] for x in bad],parents=parents,raw=raw,orbits=len(seen),covered=covered,residuals=kept,elapsed=time.perf_counter()-start)
 (HERE/'EIGHTH_LOW_COMPLETE_CATALOGUE.json').write_text(json.dumps(catalogue,indent=2)+'\n')
 cached={}
 pilot=HERE/'EIGHTH_LOW_PILOT_BOUNDS.json'
 if pilot.exists():
  for z in json.loads(pilot.read_text())['results']:cached[tuple(sorted((int(t),n) for t,n in z['counts'].items()))]=z
 out=[]
 for x in kept:
  key=tuple(sorted(x['counts'].items()))
  if key in cached:z=cached[key].copy();z['bound']=Fraction(z['bound']);z['reused_pilot']=True
  else:e=SubsetEngine(24,8,x['counts']);z=e.verify(e.solve())
  z.update(group=x['group'],source_group=x['source_group'],partner=x['partner']);out.append(z)
  if len(out)%50==0:print('BOUND',len(out),sum(z['bound']<1 for z in out),time.perf_counter()-start,flush=True)
  if len(out)%50==0 or len(out)==len(kept):
   result=dict(complete=len(out)==len(kept),scope=__doc__,orbits=len(seen),covered_by_projection=len(covered),residual_count=len(kept),elapsed=time.perf_counter()-start,results=out)
   (HERE/'EIGHTH_LOW_COMPLETE_BOUNDS.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
