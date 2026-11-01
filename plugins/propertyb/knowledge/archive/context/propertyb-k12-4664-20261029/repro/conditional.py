import sys,time,json,resource
from pathlib import Path
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
 if v>693:break
 cal=CachedFast(12,M);z=cal.unlocked(v)
 if z<S:rows.append({'v':v,'mode':'none','profiles':1,'worst_z':z,'worst_profile':[]});continue
 d0=CEIL(v-1,11);parts=[];n=0;worst=(-1,None);bad=None;counts={'one':0,'two':0,'three':0}
 for d in range(d0,12*M//v+1):
  z=cal.one(v,d)
  if z<S:
   parts.append({'d':d,'mode':'one','z':z});n+=1;counts['one']+=1
   if z>worst[0]:worst=(z,{'mode':'one','d':d})
   continue
  sd=2*(v-1)-11*d
  if sd<=0:bad={'d':d,'reason':'nonpositive-unit-pool','sd':sd};break
  B=d+(12*M-v*d)//sd;sub=[]
  for e in range(d,B+1):
   z=cal.two(v,d,e)
   if z<S:
    sub.append({'e':e,'mode':'two','z':z});n+=1;counts['two']+=1
    if z>worst[0]:worst=(z,{'mode':'two','d':d,'e':e})
    continue
   pool=v-2-(11*d-(v-1))-(11*e-(v-1))
   R=12*M-v*d-(e-d)
   if pool<=0:bad={'d':d,'e':e,'reason':'nonpositive-common-pool','pool':pool,'two_z':z};break
   F=d+R//pool;w=(-1,None)
   for f in range(d,F+1):
    ds=tuple(sorted([d,e,f]))
    for triple in [False,True]:
     z=cal.three(v,ds,triple);n+=1;counts['three']+=1
     if z>w[0]:w=(z,{'mode':'three','d':d,'e':e,'f':f,'sorted':ds,'triple':triple})
     if z>=S:bad={'d':d,'e':e,'reason':'conditional-third','pool':pool,'F':F,'failure':w};break
    if bad:break
   if bad:break
   sub.append({'e':e,'mode':'three','pool':pool,'R':R,'F':F,'profiles':2*(F-d+1),'worst_z':w[0],'worst_profile':w[1]})
   if w[0]>worst[0]:worst=w
  if bad:break
  parts.append({'d':d,'mode':'two-or-three','sd':sd,'B':B,'sub':sub})
 if bad:fail.append({'v':v,'failure':bad,'checked':n});break
 rows.append({'v':v,'mode':'hybrid123','profiles':n,'counts':counts,'parts':parts,'worst_z':worst[0],'worst_profile':worst[1]})
 if v%10==0:print('PASS',v,sum(r['profiles'] for r in rows),round(time.monotonic()-t,3),flush=True)
res={'M':M,'S':S,'candidate_v':vs,'rows':rows,'failures':fail,'complete':len(rows)==len(vs),'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-t,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(OUT/'CONDITIONAL.json').write_text(json.dumps(res,indent=2));print('DONE',res['complete'],len(rows),res['cpu_seconds'],fail,flush=True)
