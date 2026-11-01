#!/usr/bin/env python3
"""Independent tiny size/intersection threshold table, with no trace permutation or composition enumeration."""
from math import comb
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();D=comb(18,11);R=comb(14,7);B=comb(14,11)
def f(a):return a*R+(32-a)*B-(120*max(a-1,0) if a<6 else 2616+120*(a-6))
def e(s,inside):return 1794 if s==0 else (0 if inside else comb(13+s,11))
assert all(f(a+1)>f(a) for a in range(32))
rows=[]
for p in [0,2,3,4]:
 for q in [0,2,3,4]:
  if p>q:continue
  for r in range(max(0,p+q-5),p+1):
   categories=[(r,True,True),(p-r,True,False),(q-r,False,True),(5-p-q+r,False,False)]
   lower=[]
   for n,ip,iq in categories:
    if n==0:continue
    h=int(ip)+int(iq);E=e(p,ip)+e(q,iq);b=next(a for a in range(33) if f(a)+E>=D)
    lower +=[max(6-h,b)]*n
   assert len(lower)==5 and sum(lower)>32
   rows.append({'p':p,'q':q,'r':r,'forced_bad_anchor_lower_bounds':sorted(lower),'sum':sum(lower)})
assert len(rows)==19
out={'status':'PASS','scope':'All19 size/intersection trace types; integer bad-anchor thresholds contradict sum a=32 using only selectedFdegrees>=7.','D':D,'R':R,'B':B,'rows':rows,'minimum_forced_sum':min(r['sum'] for r in rows),'cpu_seconds':time.process_time()-st}
(P/'Q2_THRESHOLD_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
