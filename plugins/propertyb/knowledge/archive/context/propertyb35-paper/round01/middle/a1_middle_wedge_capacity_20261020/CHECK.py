"""Exact wedge scalars / coefficient algebra; no H enumeration."""
from itertools import product
from fractions import Fraction as F
from math import gcd,ceil
from functools import lru_cache
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def f(s):
 a,r=divmod(s,5);return (s*s-(5-r)*a*a-r*(a+1)**2)//2
cnt=0
for t in product(range(9),repeat=5):
 s=sum(t)
 if s>34:continue
 p=sum(t[i]*t[j] for i in range(5) for j in range(i+1,5))
 assert 17*p<=231*s and p<=f(s);cnt+=1
assert f(34)==462 and all(f(s+1)-f(s)==s-s//5 for s in range(34))
owner=[]
for v0 in range(4):
 S=10-v0;k=(20-S)//3;l=6-ceil(F(S,4));bonus=int(v0==2)
 owner.append(k+l+bonus)
assert owner==[6,6,9,8]
# alpha36 and120 after P<=(132n1+594)/5.
A36=F(24996,5);K36=A36*368+3528*140+F(81882,5)
assert K36==F(11750010,5)
assert (2722720-K36)*5==1863590
assert 3*A36-3*3528+6048==F(52308,5)
assert 8*A36-6*3528+3360==F(110928,5)
assert -2*A36+3528==-F(32352,5)
assert 5016*368+2520*140+7128==2205816
assert 2722720-2205816==516904
assert (3*5016-3*2520+5376,8*5016-6*2520+3192,-2*5016+2520)==(12864,28200,-7512)
assert gcd(gcd(12864,28200),7512)==24
assert ceil(F(516904,24))==21538
assert (12528,28200,-7512)==(24*522,24*1175,-24*313)
assert 139*30<=2822+131*11<139*31
# Exact difference L120-L36 on the A1 moment parameterization.
for tau,n3,n4 in product(range(3),repeat=3):
 n1=368-2*tau+3*n3+8*n4;n2=140+tau-3*n3-6*n4
 L36=A36*n1+3528*n2+6048*n3+3360*n4+F(81882,5)
 L120=5016*n1+2520*n2+5376*n3+3192*n4+7128
 assert L120-L36==-F(19250+196*tau+5012*n2+3024*n3,5)
 n0=87+tau-n3-3*n4
 Lold=594*n0+4992*n1+3960*n2+6336*n3+3432*n4+20340
 assert L120-Lold==-(15598+353*tau+1729*n2+1161*n3)
# Independent direct threshold-building check of the scalar recurrence at small N.
@lru_cache(None)
def T(n,m,r):
 if m<0 or m>n*(n-1)//2:return -10**9
 if n==0:return 0
 return max(f(r)+T(n-1,m,r),f(n-1+r)+T(n-1,m-n+1,r+1))
for N in range(1,10):
 best={}
 for bits in product((0,1),repeat=N-1):
  deg=[0]
  for b in bits:
   if b:deg=[d+1 for d in deg]+[len(deg)]
   else:deg.append(0)
  m=sum(deg)//2;best[m]=max(best.get(m,-1),sum(f(d) for d in deg))
 for m,v in best.items():assert T(N,m,0)==v
j=json.loads((P/'GRAPH_PILOT.json').read_text());w=j['minimum_high_witness'];n=w['n'];tau=w['tau'];C=list(map(F,w['C']))
assert j['conditional_n4_upper']==11 and j['surviving_profiles']==219 and len(j['survivors'])==219 and j['C3_multiplier']==15
assert 403*34<=10426+309*11<403*35
assert sum(n)==595 and sum(i*v for i,v in enumerate(n))==648 and sum(i*(i-1)//2*v for i,v in enumerate(n))==140+tau
assert sum(C)<=F(w['P_bound']) and C[0]<=33*n[0] and C[1]<=26*n[1]+339 and C[2]<=24*n[2] and C[3]<=15*n[3] and C[4]<=4*n[4]
assert sum(a*b for a,b in zip((36,120,330,792,1716),C))/2+3432*n[1]==F(w['L'])>=2722720
out={'status':'PASS','scope':__doc__,'five_attachment_tuples_checked':cnt,'sf34_maximum':f(34),'exceptional_edge_upper_by_xp_Vcount':owner,'joint_linear_P_bound':'(132*n1+594)/5','intermediate_nonB_necessary':'536*n3+1175*n4-313*tau>=21538','new_nonB_necessary':'522*n3+1175*n4-313*tau>=21538','unconditional_high_pair_lower':ceil(F(21538,1175)),'pure_n3_lower':ceil(F(21538,522)),'conditional_n4_le11_n3_lower':ceil(F(21538-1175*11,522)),'conditional_graph_relaxation_survives':True,'conditional_graph_witness':w,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
