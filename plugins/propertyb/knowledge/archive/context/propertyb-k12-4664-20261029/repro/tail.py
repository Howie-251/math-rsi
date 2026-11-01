import sys,time,json,resource
from pathlib import Path
from itertools import combinations_with_replacement
sys.path.insert(0,str(Path(__file__).resolve().parent))
from scan import domain,getD,FastExact,CEIL,S
OUT=Path(__file__).resolve().parent
M=4663;prefix=json.loads((OUT/'CONDITIONAL.json').read_text());start=prefix['rows'][-1]['v']+1;rows=[];failure=[];t=time.monotonic();cpu=time.process_time()
for v in domain(M):
 if v<start:continue
 D=getD(M,v);assert D is not None
 d0=CEIL(v-1,11);cal=FastExact(12,M);w=(-1,None);n=0
 for ds in combinations_with_replacement(range(d0,D+1),3):
  for flag in (False,True):
   z=cal.three(v,ds,flag);n+=1
   if z>w[0]:w=(z,[ds,flag])
   if z>=S:failure.append({'v':v,'profile':[ds,flag],'z':z});break
  if failure:break
 if failure:break
 rows.append({'v':v,'mode':'three-global','D':D,'d0':d0,'profiles':n,'worst_z':w[0],'worst_profile':w[1]})
 if v%10==0:print('PASS',v,sum(r['profiles'] for r in rows),round(time.monotonic()-t,3),flush=True)
res={'M':M,'S':S,'start_v':start,'rows':rows,'failures':failure,'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-t}
(OUT/'TAIL.json').write_text(json.dumps(res,indent=2))
combined={'M':M,'S':S,'candidate_v':domain(M),'rows':prefix['rows']+rows,'failures':prefix['failures']+failure,'cpu_seconds_accepted_drivers':prefix['cpu_seconds']+res['cpu_seconds'],'complete':len(prefix['rows']+rows)==len(domain(M))}
(OUT/'COMPLETE.json').write_text(json.dumps(combined,indent=2));print('DONE',combined['complete'],len(combined['rows']),res['cpu_seconds'],failure,flush=True)
