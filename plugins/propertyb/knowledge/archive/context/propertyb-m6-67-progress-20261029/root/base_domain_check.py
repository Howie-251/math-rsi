"""Fresh exact balanced-coloring and unlocked checks for the M=66 reduction."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,time
start=time.process_time()
def C(n,r):return comb(n,r) if 0<=r<=n else 0
balanced=[]
for v in range(11,27):
 p=Q(C(v//2,6)+C(v-v//2,6),C(v,6));U=66*p
 assert U<1
 balanced.append(dict(v=v,red=v//2,blue=v-v//2,p=str(p),U=str(U)))
unlocked=[]
for v in range(27,31):
 q=-(-(990-C(v,2))//10);gamma=66*65-2*q;U=Q(0)
 for h in range(1,v+1):
  A=Q(396*C(h-1,5),v*C(v-1,5));B=Q(396*C(v-h,5),v*C(v-1,5))
  W=Q(C(h-1,5)*C(v-h,5),v*C(v-1,5)*C(v-6,5))
  U+=min(A,B,gamma*W)
 assert U<1
 unlocked.append(dict(v=v,q=q,gamma=gamma,U=str(U)))
assert 44*((43+4)//5)==396 and 45*((44+4)//5)>396
out=dict(status='PASS',M=66,total_degree=396,balanced=balanced,balanced_max=str(max(Q(r['U'])for r in balanced)),unlocked=unlocked,unlocked_max=str(max(Q(r['U'])for r in unlocked)),necessary_vertex_domain=list(range(27,45)),cpu_seconds=time.process_time()-start)
Path(__file__).with_name('BASE_DOMAIN_CHECK.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
