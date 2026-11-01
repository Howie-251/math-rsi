from pathlib import Path
from math import comb
from collections import Counter
from itertools import product
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();saved=json.loads((P/'CONDITIONAL_SCALAR_RESULT.json').read_text());assert saved['status']=='COMPLETE_CONDITIONAL_DIAGNOSTIC'
def F(s):
 groups=[s//5+int(j<s%5) for j in range(5)]
 return sum(groups[i]*groups[j] for i in range(5) for j in range(i))
verified=[]
for job in saved['jobs']:
 ds=job['degrees'];e=job['e'];W=sum(d*(d-1)//2 for d in ds)
 assert len(ds)==21 and sum(ds)==175 and all(d>=8 for d in ds) and ds.count(8)==14+e
 weights=sorted(d for d in ds for _ in range(comb(d,2)));cost=[0]
 for d in weights:cost.append(cost[-1]+d)
 budgets={}
 for n in range(397,526):
  a,b=divmod(2*n,30);slots=[30]*a+([b] if b else []);slots +=[0]*(35-len(slots));assert len(slots)==35 and sum(slots)==2*n
  budgets[n]=sum(F(s) for s in slots)
 result=[];domain=0;maximum=-1
 for tau in range(max(0,4*(max(ds)-10)),141):
  for t in range((140+tau)//6+1):
   lo=max(0,(397-W+280+2*tau-8*t+2)//3)
   hi=min((525-W+280+2*tau-8*t)//3,(140+tau-6*t)//3,735-W+tau-3*t)
   for m in range(lo,hi+1):
    n1=W-280-2*tau+3*m+8*t;n2=140+tau-3*m-6*t;n0=735-W+tau-m-3*t
    assert 397<=n1<=525 and min(n0,n2)>=0
    domain+=1;caps=[33*n0,35*n1-cost[n1],((sum(sorted(ds,reverse=True)[:6])-6)//2)*n2,13*m,4*t]
    rem=budgets[n1];v=6864*n1
    for j in range(4,-1,-1):
     take=min(caps[j],rem);v+=take*(36,120,330,792,1716)[j];rem-=take
    maximum=max(v,maximum)
    if v>=5445440:result.append((n0,n1,n2,m,t,tau,v))
 assert domain==job['complete_domain'] and maximum==job['maximum_L2'] and set(result)=={tuple(z) for z in job['survivors']}
 verified.append({'spectrum_id':job['spectrum_id'],'complete_domain':domain,'survivors':len(result),'maximum_L2':maximum})
 assert time.process_time()-st<10
out={'status':'PASS_CONDITIONAL_SCALAR_DOMAIN_AND_ALL_OBJECTIVES','scope':'Independent tau/n4/n3 moment generation versus original n1/n4/n3 parity generation. Explicit35-slot Pbox and expanded degree-flag prefix costs. Same stated conditional hypotheses, not new proof of them.','spectra':len(verified),'complete_moment_keys':sum(z['complete_domain'] for z in verified),'strict_spectra':sum(z['survivors']==0 for z in verified),'survivor_count':sum(z['survivors'] for z in verified),'all_survivor_keys_and_spectrum_maxima_equal':True,'jobs':verified,'cpu_seconds':time.process_time()-st}
(P/'CONDITIONAL_SCALAR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='jobs'}))
