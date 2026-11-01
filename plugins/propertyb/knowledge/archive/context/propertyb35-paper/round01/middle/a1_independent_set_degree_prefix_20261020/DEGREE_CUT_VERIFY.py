#!/usr/bin/env python3
"""Independent multiplicity-by-degree DP, with no import of the layer DP."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
import json,time
P=Path(__file__).resolve().parent
start=time.process_time();j=json.loads(P.joinpath('DEGREE_CUT_RESULT.json').read_text());out=[]
def f(s):
 return (s*s-sum((s//5+(i<s%5))**2 for i in range(5)))//2
for source in j['records']:
 e=source['e'];mode=source['allcritical'];target=2*e;t=source['n4_cap']
 def cap(r):
  N=35-r
  lb=max(0,N-21)
  if N>21:lb=max(lb,(8*N*(N-21)-105*t+83)//84,(8*N*(N-21)+188)//189)
  lb=max(lb,(152*N*(N-21)-2037*t+1427)//1428)
  return e+r*(r-1)//2-lb
 @lru_cache(None)
 def V(q,n,s,h):
  if s>target or s+q*(35-n)<target:return -10**9
  if n==35:return 0 if s==target else -10**9
  if q==0:
   if 35-n>3 or s!=target:return -10**9
   if any(s>cap(r) for r in range(n+1,36)):return -10**9
   return (35-n)*f(34)
  if target-s<max(0,32-n):return -10**9
  cmax=min(35-n,(target-s)//q)
  if q>29:cmax=min(cmax,0 if mode else 1-h)
  R=e-60+2*t
  if q>R:cmax=0
  if q==R:cmax=min(cmax,12)
  best=-10**9
  for c in range(cmax+1):
   if any(s+k*q>cap(n+k) for k in range(1,c+1)):continue
   value=c*f(34-q)+V(q-1,n+c,s+c*q,(h+c) if q>29 else 0)
   best=max(best,value)
  return best
 value=V(34,0,0,0)
 assert value==source['bound'],(e,mode,value,source['bound'])
 out.append(dict(e=e,n4_cap=t,allcritical=mode,bound=value,states=V.cache_info().currsize))
# Recompute all recorded weighted C allocations and decisions in Fraction arithmetic.
for p in j['profiles']:
 n=p['n'];caps=[33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4]]
 for mode in (0,):
  r=p['modes'][mode];rem=F(r['P_bound']);cs=[F(0)]*5
  for a in reversed(range(5)):cs[a]=min(caps[a],rem);rem-=cs[a]
  value=sum(x*w for x,w in zip(cs,(36,120,330,792,1716)))/2+3432*n[1]
  assert list(map(str,cs))==r['C'] and str(value)==r['L'] and (value>=2722720)==r['survives']
result=dict(status='PASS',scope='independent frequency DP for all actual (e,n4) optimal bounds with degree-specific q cuts; all25 exact greedy allocations',records=out,cpu_seconds=time.process_time()-start)
P.joinpath('DEGREE_CUT_VERIFY.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
