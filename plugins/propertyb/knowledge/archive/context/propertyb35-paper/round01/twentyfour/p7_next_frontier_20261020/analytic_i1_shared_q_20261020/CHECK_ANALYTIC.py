"""Check scalar consequences and inventory partition; no source-set generation."""
from pathlib import Path
from itertools import product
import json

DIR=Path(__file__).parent
base=json.loads((DIR/"CHECK.json").read_text())
old={tuple(t) for t in base["previous_closed"]}
new={(10,2,1),(9,1,2),(8,0,3)}
all_inventory={(17-2*a-3*b,a,b) for a in range(9) for b in range(6)
               if 17-2*a-3*b>=0}
assert len(old)==14 and len(new)==3 and not old&new
remaining=all_inventory-old-new
assert len(all_inventory)==33 and len(remaining)==16

# One quad: shared weighted q-failure inequality.
for a in range(3):
    for b in range(2):
        for s in range(8-a-b):
            if b==1:
                failed=a+s<=1
            elif a==2:
                failed=s==0
            elif a==1:
                failed=s<=2
            else:
                failed=s<=3
            if failed:
                assert s+a+2*b<=3
assert 21-2==19<20

# Both larger cases: every C failure has s <=4-2h.
frequency_rows=[]
for n4,n2,total_h,lo,hi in [(3,8,12,6,8),(2,9,11,5,7)]:
    for h in product(range(3),repeat=5):
        H=sum(h)
        if not lo<=H<=hi:
            continue
        C_upper=sum(4-2*x for x in h)
        assert C_upper==20-2*H
        D_min=2*n2-C_upper
        assert D_min==2*n2-20+2*H
        z=h.count(2)
        if H>5:
            assert z>=1
        if n4==3 and H==8:
            assert z>=3
        if n4==2 and H==7:
            assert (z,h.count(1),h.count(0)) in [(2,3,0),(3,1,1)]
        frequency_rows.append(dict(n4=n4,H_C=H,h=list(h),C_J_upper=C_upper,D_J_min=D_min))

# All-C-frequency-one mixed case: D degrees 3..5 and C degrees at most2.
endpoint_rows=[]
for d0,d1 in product(range(3,6),repeat=2):
    for c in product(range(3),repeat=5):
        if sum(c)+d0+d1!=18:
            continue
        K=sum(v==2 for v in c)
        assert K>=3
        if max(d0,d1)<=4:
            assert K>min(d0,d1) # A non-neighbor is forced.
        # When K is adjacent to both D vertices, all K-D multiplicities are1;
        # the above contradiction forces one D degree5.
        endpoint_rows.append(dict(D=[d0,d1],C=list(c),K=K))

# Exact imported gate parameters (all-high d3, or q2/d2s6).
pure_calls=[]
for n2,n1 in [(8,23),(9,22)]:
    for sd in [4,5]:
        m,t,b=10-sd,n2-sd,n1-(10-sd)
        assert (m==6 and t<=6 and b<=35) or (m<=5 and t+b<=35)
        pure_calls.append(dict(n2=n2,m=m,t=t,b=b))
    m,t,b=5,n2-6,n1-5
    assert t+b<=35
for ell in [0,1]:
    assert 4+ell<=5 and 1+ell<=3
assert 4+1<=5 and 3<=3

out=dict(status="PASS",scope="integer frequencies, counts and gate parameters only",
         previous_closed_count=14,new_whole_inventories=sorted(new),
         current_closed_count=17,remaining_count=16,
         remaining_inventories=sorted(remaining,key=lambda t:(t[2],t[1])),
         C_frequency_row_count=len(frequency_rows),endpoint_degree_row_count=len(endpoint_rows),
         pure_gate_calls=pure_calls)
(DIR/"CHECK_ANALYTIC.json").write_text(json.dumps(out,indent=2)+"\n")
print(out)
