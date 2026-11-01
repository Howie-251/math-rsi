from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
old=json.loads((P.parent/'tau_shared_capacities_20261020/FINAL_LAMBDA4_VERIFY.json').read_text())
def squares(d,t):
 q,r=divmod(2*t,d)
 return (d-r)*q*q+r*(q+1)**2

def oldP(n1):
 q,r=divmod(2*n1,30);a,b=divmod(r,5)
 return 360*q+(r*r-((5-b)*a*a+b*(a+1)**2))//2

def weighted(c,P):
 ans=0
 for k,w in reversed(list(enumerate((36,120,330,792,1716)))):
  use=min(c[k],P);ans+=use*w;P-=use
 return ans
jobs=[]
for j in old['jobs']:
 if j['strict']:continue
 ds=j['degrees'];caps=[comb(d,2)-max(0,(4*d-20+2)//3) for d in ds]
 marg=sorted(squares(d,t)-squares(d,t-1) for d,c in zip(ds,caps) for t in range(1,c+1));prefix=[0]
 for x in marg:prefix.append(prefix[-1]+x)
 res=[]
 for k in j['survivors']:
  n1=k['n'][1];q,r=divmod(2*n1,30)
  if n1>len(marg):p=-1;v=-1
  else:
   p=min(oldP(n1),(900*q+r*r-prefix[n1])//2)
   v=6864*n1+weighted(k['caps'],p)
  res.append({**k,'newP':p,'oldP':oldP(n1),'new_twice_L':v,'strict':v<5445440})
 jobs.append({'spectrum_id':j['spectrum_id'],'degrees':ds,'lambda4_subcase_only':j['lambda4_subcase_only'],'keys':res,'strict':all(k['strict'] for k in res)})
out={'status':'PILOT','lemma':'actual vertex singleton incidence square bound with link-overlap quota','jobs':jobs,'new_strict':[j['spectrum_id'] for j in jobs if j['strict']],'remaining':sum(not k['strict'] for j in jobs for k in j['keys']),'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print('NEWSTRICT',out['new_strict'],'REMAIN',out['remaining'],'CPU',out['cpu_seconds'])
for j in jobs:
 print(j['spectrum_id'],'strict',j['strict'],'remain',sum(not k['strict'] for k in j['keys']),'max',max(k['new_twice_L'] for k in j['keys']),'Pdrop',min(k['oldP']-k['newP'] for k in j['keys']))
