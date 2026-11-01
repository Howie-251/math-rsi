"""Independent inclusive-pair Mobius reconstruction, this10^4 quad only."""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
d=json.loads((P/'RESULT.json').read_text());PP=(3,5,6,9,10,12);CR=(5,6,9,10);TM=(7,11,13,14)
keys=set()
for vv in product(range(1,5),repeat=6):
 I=dict(zip(PP,vv));cs=sum(I[p] for p in CR)
 if cs<13:continue
 for full in range(min(vv)+1):
  cap=(cs-13-4*full)//2
  if cap<0:continue
  assert cap<=1
  for tri in (0,*TM) if cap else (0,):
   mu=[0]*16;mu[15]=full
   if tri:mu[tri]=1
   for p in PP:mu[p]=I[p]-full-int(bool(tri) and tri&p==p)
   if min(mu)<0 or mu[3]<1 or mu[12]<1 or sum(mu[p] for p in CR)<13:continue
   for i in range(4):mu[1<<i]=10-sum(n for m,n in enumerate(mu) if m.bit_count()>=2 and m>>i&1)
   mu[0]=35-sum(mu)
   if min(mu)<0:continue
   keys.add(tuple(mu))
expected={tuple(z['counts']) for z in d['cases']};assert keys==expected and len(keys)==310
out=dict(status='PASS_COMPLETE310_THIS_QUAD_ONLY',independent_inclusive_domain_equal=True,inputs=310,nonstrict_count=d['nonstrict_count'],nonstrict=[z for z in d['cases'] if not z['strict']],cpu_seconds=time.process_time()-st)
(P/'VERIFY_DOMAIN.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='nonstrict'})
