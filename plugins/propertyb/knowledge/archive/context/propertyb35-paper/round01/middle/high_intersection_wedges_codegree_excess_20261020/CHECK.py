"""Exact local triple multiplicity, binomial identity, and M35 scalar wedge bounds."""
from itertools import combinations,product
from math import comb
from fractions import Fraction
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,k):return comb(n,k) if n>=k>=0 else 0
# Every labeled simple graph on3 vertices, not only representatives.
tri=[]
pairs=list(combinations(range(3),2))
for bits in product((0,1),repeat=3):
 ds=[sum(bit for bit,(a,b) in zip(bits,pairs) if i in (a,b)) for i in range(3)]
 w=sum(C(d,2) for d in ds)
 assert w in (0,1,3) and w<=3
 tri.append({'edge_bits':bits,'degrees':ds,'wedges':w})
for lam in range(101):assert 3*C(lam,3)==lam*C(max(lam-1,0),2)
rows=[]
for t in range(36):
 a,b=divmod(2*t,35)
 wedge=(35-b)*C(a,2)+b*C(a+1,2)
 tau=(3*wedge+3)//4
 assert 4*tau>=3*wedge and (tau==0 or 4*(tau-1)<3*wedge)
 rows.append({'Q_edges':t,'average_floor':a,'remainder':b,'minimum_wedges':wedge,'necessary_tau_lower':tau})
assert [z['Q_edges'] for z in rows if z['necessary_tau_lower']==0]==list(range(18))
# Integer smoothing is the discrete-convex step used in the general proof.
for x in range(36):
 for y in range(x+2,36):assert C(x,2)+C(y,2)>C(x+1,2)+C(y-1,2)
out={'status':'PASS','scope':__doc__,'all_three_vertex_graphs':tri,'lambda_identity_checked':list(range(101)),'M35_r5_L4_table':rows,'tau_zero_maximum_Q_edges':17,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'tau_zero_maximum_Q_edges':17,'tau_table':[(z['Q_edges'],z['minimum_wedges'],z['necessary_tau_lower']) for z in rows],'cpu_seconds':out['cpu_seconds']}))
