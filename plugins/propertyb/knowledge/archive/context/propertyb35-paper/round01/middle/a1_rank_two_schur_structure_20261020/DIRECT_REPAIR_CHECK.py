from math import comb
from fractions import Fraction as F
from pathlib import Path
import json,time
st=time.process_time();P=Path(__file__).resolve().parent
D=comb(16,9)
pR=F(comb(9,4),comb(16,4));pB=F(comb(7,4),comb(16,4))
pG=F(comb(9,5)+comb(7,5),comb(16,5))
assert pR==F(comb(12,5),D) and pB==F(comb(12,9),D)
assert pG==F(comb(11,4)+comb(11,9),D)
cases=[(34,6,F(0)),(33,6,pG),(33,7,F(0))]
failure=[a*pR+(s-a)*pB+p for s,a,p in cases]
assert failure==[F(434,455),F(1007,1040),F(448,455)]
counts=[f*D for f in failure]
assert counts==[10912,11077,11264]
success=[D-c for c in counts]
assert success==[528,363,176] and all(f<1 for f in failure)
out={'status':'PASS','samples':D,'red_attachment_count':comb(12,5),
     'blue_attachment_count':comb(12,9),'disjoint_exception_count':385,
     'failure_probabilities':[str(f) for f in failure],
     'union_upper_counts':[int(c) for c in counts],
     'success_lower_counts':[int(c) for c in success],
     'cpu_seconds':time.process_time()-st}
(P/'DIRECT_REPAIR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
