from itertools import combinations
from pathlib import Path
import json
P=Path(__file__).resolve().parent;C=set(range(4));rows=[];exception=[];interfaces=[]
for h in [0,4]:
 for size in [3,4]:
  for TT in combinations(range(6),size):
   T=set(TT);eligible=sorted(C&T-{h});r=dict(nine=h,T=TT,size=size,eligible_eight=eligible)
   if not eligible:assert size==3 and h in C and T=={h,4,5};exception.append(r)
   rows.append(r)
  pair_count=7-size
  for s in range(pair_count+1):
   m=5-s;B=25+size-m;negT=pair_count-s
   assert 1<=m<=5 and B<=27 and negT<=4
   interfaces.append(dict(center_degree=8,high_trace_size=size,P2degree=s,positive4=m,negative3=negT,negative4=B))
for s in range(1,5):
 m=6-s;assert m<=5 and 4-s<=3 and 28-m<=26
 interfaces.append(dict(center_degree=9,high_trace_size=3,P2degree=s,positive4=m,negative3=4-s,negative4=28-m))
assert len(rows)==70 and len(exception)==1
out=dict(passed=True,trace_location_cases=len(rows),eight_common_cases=len(rows)-len(exception),exception=exception,valid_five_gate_interfaces=interfaces,residual=dict(positive4=6,negative3=4,negative4=22,outer_points=18,occurrence_upper=7,positive_union_lower=16))
(P/'ONE_HIGH_TRACE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='valid_five_gate_interfaces'},indent=2))
