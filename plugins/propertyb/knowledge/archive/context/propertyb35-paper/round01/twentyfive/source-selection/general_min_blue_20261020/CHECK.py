from pathlib import Path
from itertools import product
import json
import time

start=time.process_time()
thresholds={}
for b in range(8,13):
    rows=[]
    for a in range(7):
        bh=18-b-2*a
        n3=b-12+a
        if min(bh,n3)<0 or a+bh+n3!=6:
            continue
        minimum=bh+max(a*(a-1)//2, a-1 if a else 0)
        rows.append([a,bh,n3,minimum])
    best=min(r[3] for r in rows)
    thresholds[str(b)]={'minimum_t':best,'attainers':[r for r in rows if r[3]==best]}
    assert best == (8 if b==8 else 15-b)
    if b>=9:
        assert all(r[0] in (2,3) for r in rows if r[3]==best)

for b,eps,k,kappa in product(range(8,13),(0,1),range(36),range(101)):
    if b+kappa < 6-eps+3*k:
        continue
    if b==8:
        assert k <= eps+kappa
    if b==9:
        assert 2*k <= 2+kappa
    if b==10:
        assert k <= 1+kappa

general={}
for b in range(8,13):
    general[str(b)]={}
    for u in range(6):
        values=[]
        for a in range(7):
            bh=18-b-2*a
            n3=b-12+a
            if min(bh,n3)<0: continue
            shared=(max(0,a-u)*max(0,a-1)+1)//2
            individual=a-1 if a>u else 0
            values.append(bh+max(shared,individual))
        general[str(b)][str(u)]=min(values)

result={'status':'PASS','u0_thresholds':thresholds,'general_low_sink_minimum_t':general,
        'scope':'Five blue sizes, degree-six scalar stars, owner price implications only',
        'cpu_seconds':time.process_time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
