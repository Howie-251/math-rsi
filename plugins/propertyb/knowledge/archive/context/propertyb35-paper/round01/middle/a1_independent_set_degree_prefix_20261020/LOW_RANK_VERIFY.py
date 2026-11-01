#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
import json,subprocess,time,resource
P=Path(__file__).resolve().parent
start=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
j=json.loads(P.joinpath('LOW_RANK_RESULT.json').read_text());verified=[]
for r in j['records']:
 v=json.loads(subprocess.check_output(['/tmp/a1_low_rank_frequency',str(r['e']),str(r['n4_cap'])],text=True))
 assert v['bound']==r['bound'],(r,v)
 q=r['q'];assert q==sorted(q,reverse=True) and sum(q)==2*r['e'] and q.count(0)<=3 and q.count(0)+q.count(1)<=20
 assert q[0]+q.count(1)+q.count(0)<=50 and q[0]+q[1]<=r['e']-49+2*r['n4_cap']
 verified.append(v)
for p in j['profiles']:
 n=p['n'];r=p['modes'][0];rem=F(r['P_bound']);C=[F(0)]*5
 for a,cap in reversed(list(enumerate((33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4])))):
  C[a]=min(cap,rem);rem-=C[a]
 L=sum(c*w for c,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
 assert list(map(str,C))==r['C'] and str(L)==r['L'] and (L>=2722720)==r['survives']
c=resource.getrusage(resource.RUSAGE_CHILDREN)
out=dict(status='PASS',scope='independent degree-frequency DP versus fixed-maximum layer DP with low-block rank cut, all19(e,n4), all25 rational allocations',records=verified,cpu_seconds=time.process_time()-start+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime)
P.joinpath('LOW_RANK_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
