"""Cheap bounded raw-ABC screen using only the 15 pilot layouts.
No per-input DP and no quota. Fixed-layout coefficients have common denominator
16!, and every pilot is checked against the separately computed rational rows.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,time,sys
P=Path(__file__).resolve().parent;st=time.perf_counter();source=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());pilot=json.loads((P/'A7_TRIANGLE_PILOT.json').read_text());N=16;D=factorial(N);limit=int(sys.argv[1]) if len(sys.argv)>1 else 100
F=[factorial(i) for i in range(N+1)]
def fall(n,r):return F[n]//F[n-r] if 0<=r<=n else 0
class Fixed:
 def __init__(self,pos):
  self.pos=pos;self.rows=[]
  for k in range(1,26):
   left=sum(1<<i for i,p in enumerate(pos) if p<k);right=sum(1<<i for i,p in enumerate(pos) if p>k);pivot=next((1<<i for i,p in enumerate(pos) if p==k),0);a=k-1-left.bit_count();b=25-k-right.bit_count();ran=range(6) if pivot else range(1,6)
   ca=[0]*6;cb=[0]*6;cc=[]
   for r in ran:ca[r]=fall(a,r-int(not pivot))*F[N-r]*(1 if pivot else r);cb[r]=fall(b,r-int(not pivot))*F[N-r]*(1 if pivot else r)
   for r in ran:
    for q in ran:
     n=r+q-int(not pivot)
     if n<=N:
      w=fall(a,r-int(not pivot))*fall(b,q-int(not pivot))*F[N-n]
      if w:cc.append((r,q,w))
   r=5-pivot.bit_count();diag=fall(a,r-int(not pivot))*fall(b,r-int(not pivot))*F[N-2*r+int(not pivot)] if 2*r-int(not pivot)<=N else 0
   elig=[]
   for t in range(512):
    if t.bit_count()>5:elig.append((False,False,0));continue
    r=5-t.bit_count();ok=bool(t&pivot) if pivot else bool(r)
    elig.append((ok and not ((t^pivot if pivot else t)&~left),ok and not ((t^pivot if pivot else t)&~right),r))
   self.rows.append((pivot,ca,cb,cc,diag,elig))
 def bound(self,ns):
  total=0
  for pivot,ca,cb,cc,diag,elig in self.rows:
   ls=[0]*6;rs=[0]*6
   for t,n in ns.items():
    l,r,j=elig[t]
    if l:ls[j]+=n
    if r:rs[j]+=n
   A=sum(n*w for n,w in zip(ls,ca));B=sum(n*w for n,w in zip(rs,cb));C=sum(ls[r]*rs[q]*w for r,q,w in cc)-ns.get(pivot,0)*diag
   assert C>=0;total+=min(A,B,C)
  return total
engines={};checks=0
for z in pilot['results']:
 pos=tuple(z['positions']);engines.setdefault(pos,Fixed(pos));v=engines[pos].bound({int(t):n for t,n in z['counts'].items()});raw=sum(min(Q(r['A']),Q(r['B']),Q(r['C'])) for r in z['rows']);assert Q(v,D)==raw;checks+=1
families=[]
for f in source['results']:
 poses=list(dict.fromkeys(tuple(z['positions']) for z in pilot['results'] if (z['base'],z['partner'])==(f['base'],f['partner'])))
 zs=f['cases'] if limit==0 else f['cases'][:limit];values=[];res=[]
 for idx,z in enumerate(zs):
  ns={int(t):n for t,n in z['counts'].items()};vv=[engines[pos].bound(ns) for pos in poses];v=min(vv);values.append(v)
  if v>=D:res.append(dict(case_index=idx,minimum_raw=str(Q(v,D))))
 families.append(dict(base=f['base'],partner=f['partner'],positions=poses,tested=len(zs),domain=len(f['cases']),strict=len(zs)-len(res),residual=res,maximum_minimum_raw=str(Q(max(values),D))))
 print(f['base'],f['partner'],len(zs),len(res),families[-1]['maximum_minimum_raw'],flush=True)
out=dict(scope=__doc__,complete_screen=limit==0,pilot_identity_checks=checks,limit=limit,tested=sum(z['tested'] for z in families),strict=sum(z['strict'] for z in families),families=families,elapsed_seconds=time.perf_counter()-st)
(P/('A7_TRIANGLE_FIXED_PROFILE.json' if limit else 'A7_TRIANGLE_FIXED_SCREEN.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['complete_screen','tested','strict','elapsed_seconds']},indent=2))
