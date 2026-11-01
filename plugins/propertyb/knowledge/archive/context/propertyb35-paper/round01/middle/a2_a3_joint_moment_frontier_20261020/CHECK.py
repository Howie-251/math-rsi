"""Exact verification of every saved relaxation survivor, moment and shared capacity."""
from pathlib import Path
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();j=json.loads((P/'RESULT.json').read_text());rows=json.loads((P/'SURVIVORS.json').read_text());T={int(k):v for k,v in json.loads((P/'THRESHOLD_TABLE.json').read_text()).items()}
assert set(T)==set(range(397,596))
jobs={z['unique_degree_key']:z for z in j['jobs']};assert len(jobs)==16
seen=set();ct=Counter();binding=0
for z in rows:
 key=z['unique_degree_key'];job=jobs[key];n=z['n'];tau=z['tau'];ds=job['degrees'];e=job['e']
 assert len(ds)==21 and sum(ds)==175 and sum(comb(d,2) for d in ds)==job['W']
 assert sum(n)==595 and sum(i*x for i,x in enumerate(n))==job['W']
 assert sum(comb(i,2)*x for i,x in enumerate(n))==140+tau
 assert min(n)>=0 and 397<=n[1]<=595 and 0<=tau<=140
 a,b=divmod(2*n[4],35);Wmin=(35-b)*comb(a,2)+b*comb(a+1,2);assert 3*Wmin<=4*tau
 # Verify mincost by cost-level totals, not the discovery's individual-point filling.
 capacity=Counter()
 for d in ds:capacity[d]+=comb(d,2)
 left=n[1];cost=0
 for d,c in sorted(capacity.items()):take=min(left,c);cost+=take*d;left-=take
 assert left==0
 cap=[33*n[0],35*n[1]-cost,((sum(sorted(ds)[-6:])-6)//2)*n[2],14*n[3],4*n[4]]
 assert sum(sorted(ds)[-6:])==54+e and cap==z['C_caps']
 C=z['C'];assert all(0<=x<=y for x,y in zip(C,cap)) and sum(C)<=T[n[1]]==z['P']
 rem=T[n[1]];expected=[0]*5
 for k in range(4,-1,-1):expected[k]=min(rem,cap[k]);rem-=expected[k]
 assert expected==C
 L2=sum(x*y for x,y in zip(C,(36,120,330,792,1716)))+6864*n[1]
 assert L2==z['twice_L'] and L2>=5445440
 fullkey=(key,tuple(n),tau);assert fullkey not in seen;seen.add(fullkey);ct[key]+=1
 binding+=C[1]==cap[1]
assert all(ct[k]==v['survivor_count'] for k,v in jobs.items())
result={'status':'PASS','saved_survivors_checked':len(rows),'degree_spectra':len(jobs),'C1_binding_survivors':binding,'n1_range':[min(r['n'][1] for r in rows),max(r['n'][1] for r in rows)],'tau_range':[min(r['tau'] for r in rows),max(r['tau'] for r in rows)],'n4_range':[min(r['n'][4] for r in rows),max(r['n'][4] for r in rows)],'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
