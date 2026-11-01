"""Scalar threshold-degree majorant for the singleton-intersection graph; no H search."""
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
st=time.process_time()
def f(s):
 a,r=divmod(s,5);return (s*s-((5-r)*a*a+r*(a+1)**2))//2
assert all(f(s+1)-f(s)==s-s//5 for s in range(34))
@lru_cache(None)
def T(n,m,r):
 if m<0 or m>comb(n,2):return -10**9
 if n==0:return 0
 return max(f(r)+T(n-1,m,r), f(n-1+r)+T(n-1,m-(n-1),r+1))
vals={m:T(35,m,0) for m in range(397,547)}
def cap(n):
 return min(F(vals[n[1]]),F(132*n[1]+594,5))
def weighted(n):
 U=[33*n[0],26*n[1]+339,24*n[2],15*n[3],4*n[4]]
 B=cap(n);z=[F(0)]*5
 for j in range(4,-1,-1):z[j]=min(B,U[j]);B-=z[j]
 return sum(w*x for w,x in zip((36,120,330,792,1716),z)),z
cnt=0;surv=[]
for tau in range(141):
 for n4 in range(12): # CONDITIONAL n4<=11; root-checked new import, fresh cross-family review pending.
  for n3 in range((140+tau-6*n4)//3+1):
   n=[87+tau-n3-3*n4,368-2*tau+3*n3+8*n4,140+tau-3*n3-6*n4,n3,n4]
   if min(n)<0 or not 397<=n[1]<=546:continue
   cnt+=1;R,z=weighted(n);L=R/2+3432*n[1]
   if L>=2722720:surv.append({'n':n,'tau':tau,'P_bound':str(cap(n)),'C':[str(v) for v in z],'L':str(L)})
out={'scope':__doc__,'f_values':[f(s) for s in range(35)],'threshold_Pmax':vals,'conditional_n4_upper':11,'C3_multiplier':15,'moment_profiles':cnt,'surviving_profiles':len(surv),'survivors':surv,'first_survivor':surv[0] if surv else None,'minimum_n3':min((x['n'][3] for x in surv),default=None),'minimum_high_pairs':min((x['n'][3]+x['n'][4] for x in surv),default=None),'minimum_high_witness':min(surv,key=lambda x:(x['n'][3]+x['n'][4],x['tau'])) if surv else None,'Pmax_at508':vals[508],'states':T.cache_info().currsize,'cpu_seconds':time.process_time()-st}
(P/'GRAPH_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('threshold_Pmax','f_values','survivors')})
