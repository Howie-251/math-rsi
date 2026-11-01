"""Independent n1-first full-domain verification of all nine tau-sensitive scalar runs."""
from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();r=json.loads((P/'TAU_SENSITIVE_RESULT.json').read_text())
results=[]
for j in r['jobs']:
 ds=j['degrees'];W=sum(d*(d-1)//2 for d in ds);lo_tau=max(0,4*(max(ds)-10));coef=(sum(sorted(ds,reverse=True)[:6])-6)//2
 # Cost independently formed as a sorted multiset of every actual pointpair incidence.
 costs=sorted(d for d in ds for _ in range(comb(d,2)));prefix=[0]
 for d in costs:prefix.append(prefix[-1]+d)
 count=0;fails=[];maximum=-1
 for n1 in range(397,526):
  b,rem=divmod(2*n1,30);fparts=[rem//5+int(i<rem%5) for i in range(5)];Pbox=360*b+sum(fparts[i]*fparts[k] for i in range(5) for k in range(i))
  for t in range((W-n1)//4+1):
   lo=max(0,-((-2*lo_tau+W-280+8*t-n1)//3),W+n1-1190-2*t)
   hi=min((560-W-8*t+n1)//3,(W-n1-4*t)//3)
   if (lo-W+n1)%2:lo+=1
   for m in range(lo,hi+1,2):
    tau=(W-280+3*m+8*t-n1)//2;n2=(W-n1-3*m-4*t)//2;n0=595-(W+n1-m-2*t)//2
    assert min(n0,n2,m,t)>=0 and lo_tau<=tau<=140 and n0+n1+n2+m+t==595
    caps=(33*n0,35*n1-prefix[n1],coef*n2,(8 if tau==0 else 12)*m,(2 if tau==0 else 3 if tau<=2 else 4)*t)
    # Layer-cake identity for optimal allocation; no greedy filling reused.
    v=6864*n1+sum(dw*min(Pbox,sum(caps[k:])) for k,dw in enumerate((36,84,210,462,924)))
    count+=1;maximum=max(maximum,v)
    if v>=5445440:fails.append({'n':[n0,n1,n2,m,t],'tau':tau,'twice_L':v})
 assert count==j['complete_domain'] and maximum==j['maximum_twice_L']
 assert sorted(fails,key=str)==sorted(j['survivors'],key=str)
 results.append({'spectrum_id':j['spectrum_id'],'complete_keys':count,'maximum_twice_L':maximum,'survivors':fails})
 assert time.process_time()-st<16
out={'status':'PASS','scope':__doc__,'all_complete_domains_and_maxima_equal':True,'jobs':results,'total_keys':sum(j['complete_keys'] for j in results),'strict_spectra':sum(not j['survivors'] for j in results),'cpu_seconds':time.process_time()-st}
(P/'TAU_SENSITIVE_VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
