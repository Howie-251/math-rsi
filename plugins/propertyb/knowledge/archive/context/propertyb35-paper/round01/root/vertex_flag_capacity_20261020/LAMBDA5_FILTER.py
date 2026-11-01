from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();M=P.parent.parent/'middle/min_degree_seven_unique_codegree_five_20261020'
old=json.loads((M/'HIGH_ROW_REFINEMENT.json').read_text());src=json.loads((M/'ALL_EIGHTEEN_SCALAR_RESULT.json').read_text());spectra={j['spectrum_id']:j for j in src['jobs']}
def f(d,t):
 q,r=divmod(2*t,d);return (d-r)*q*q+r*(q+1)**2
results=[]
for job in old['jobs']:
 sid=job['spectrum_id'];ds=spectra[sid]['degrees'];marg=sorted(f(d,t)-f(d,t-1) for d in ds for t in range(1,comb(d,2)-max(0,(4*d-18)//3)+1));prefix=[0]
 for a in marg:prefix.append(prefix[-1]+a)
 new=[]
 for k in job['cases']:
  if k['strict']:continue
  n1=k['n'][1];q,r=divmod(2*n1,30);p=min(k['P'],(900*q+r*r-prefix[n1])//2);remain=p;v=6864*n1
  for cap,w in zip(reversed(k['new_caps']),reversed((36,120,330,792,1716))):u=min(cap,remain);v+=u*w;remain-=u
  new.append({**k,'vertex_P':p,'vertex_twice_L':v,'vertex_strict':v<5445440})
 results.append({'spectrum_id':sid,'degrees':ds,'cases':new,'strict':all(k['vertex_strict'] for k in new)})
out={'status':'COMPLETE100_KEY_FILTER','scope':'unique lambda5 actual caller inherited; new vertex flag bound no paircap4 needed','new_strict':[j['spectrum_id'] for j in results if j['strict']],'remaining':sum(not k['vertex_strict'] for j in results for k in j['cases']),'jobs':results,'cpu_seconds':time.process_time()-st}
(P/'LAMBDA5_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['new_strict'],out['remaining'],out['cpu_seconds'])
for j in results:print(j['spectrum_id'],sum(not k['vertex_strict'] for k in j['cases']))
