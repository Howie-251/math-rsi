import sys,time,json,resource
from pathlib import Path
from itertools import combinations_with_replacement
sys.path.insert(0,str(Path(__file__).resolve().parent))
from scan import domain,getD,FastExact,CEIL,S
OUT=Path(__file__).resolve().parent
class CachedFast(FastExact):
 def __init__(self,k,m):
  super().__init__(k,m);self.saved_tables={}
 def table(self,v,s):
  if (v,s) not in self.saved_tables:self.saved_tables[v,s]=super().table(v,s)
  return self.saved_tables[v,s]
M=4663;t=time.monotonic();cpu=time.process_time();rows=[];fail=[]
vs=domain(M)
for v in vs:
 cal=CachedFast(12,M); z=cal.unlocked(v)
 if z<S:rows.append({'v':v,'mode':'none','profiles':1,'worst_z':z,'worst_profile':[]});continue
 # Try one/two locks with the same actual minimum-degree point, separately for every d.
 d0=CEIL(v-1,11);parts=[];n=0;worst=(-1,None);bad=None
 for d in range(d0,12*M//v+1):
  z=cal.one(v,d)
  if z<S:
   parts.append({'d':d,'mode':'one','z':z});n+=1
   if z>worst[0]:worst=(z,[d])
   continue
  sd=2*(v-1)-11*d
  if sd<=0:bad={'d':d,'reason':'nonpositive-unit-pool','sd':sd};break
  B=d+(12*M-v*d)//sd
  # Screen endpoint and diagonal first; enumerate all only after screen passes.
  zs=[(cal.two(v,d,e),e) for e in sorted(set([d,B]))]
  if max(zs)[0]>=S:
   bad={'d':d,'reason':'two-screen','B':B,'worst':max(zs)};break
  w=(-1,None)
  for e in range(d,B+1):
   z=cal.two(v,d,e);n+=1
   if z>w[0]:w=(z,e)
   if z>=S:bad={'d':d,'reason':'two-interior','B':B,'worst':w};break
  if bad:break
  parts.append({'d':d,'mode':'two','sd':sd,'B':B,'profiles':B-d+1,'worst_z':w[0],'worst_e':w[1]})
  if w[0]>worst[0]:worst=(w[0],[d,w[1]])
 if not bad:
  rows.append({'v':v,'mode':'hybrid12','profiles':n,'parts':parts,'worst_z':worst[0],'worst_profile':worst[1]})
 else:
  D=getD(M,v)
  if D is None:
   fail.append({'v':v,'hybrid_failure':bad,'three_D':None});break
  params=[(ds,f) for ds in combinations_with_replacement(range(d0,D+1),3) for f in (False,True)]
  w=(-1,None);ok=True;n=0
  for ds,f in params:
   z=cal.three(v,ds,f);n+=1
   if z>w[0]:w=(z,[ds,f])
   if z>=S:ok=False;break
  if not ok:fail.append({'v':v,'hybrid_failure':bad,'three_D':D,'three_failure':w,'checked':n});break
  rows.append({'v':v,'mode':'three','D':D,'profiles':n,'worst_z':w[0],'worst_profile':w[1]})
 if v%10==0:print('PASS',v,rows[-1]['mode'],sum(r['profiles'] for r in rows),round(time.monotonic()-t,3),flush=True)
 if time.process_time()-cpu>68:break
res={'M':M,'S':S,'candidate_v':vs,'rows':rows,'failures':fail,'complete':len(rows)==len(vs),'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-t,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(OUT/'HYBRID_FAST.json').write_text(json.dumps(res,indent=2));print('DONE',res['complete'],len(rows),res['cpu_seconds'],fail,flush=True)
