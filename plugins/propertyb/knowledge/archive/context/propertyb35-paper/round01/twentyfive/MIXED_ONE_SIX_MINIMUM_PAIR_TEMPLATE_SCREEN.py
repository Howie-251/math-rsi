"""Old a7 plus eight pilot fixed layouts transported to the four one-six minimum-empty roots.
Integer16! coefficients only; complete2069-input domain, no per-input DP.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=16;D=factorial(N)
dom=json.loads((P/'MIXED_ONE_SIX_MINIMUM_PAIRS.json').read_text());pilot=json.loads((P/'A7_MINIMUM_EMPTY_PILOT.json').read_text());old=json.loads((P/'A7_TRIANGLE_FIXED_SCREEN.json').read_text());reroot=json.loads((P/'A7_MINIMUM_EMPTY_REROOT.json').read_text())
inside=list(dict.fromkeys([tuple(p) for r in old['families'] if r['base']==19 and r['partner']==4 for p in r['positions']]+[tuple(z['positions']) for z in pilot['results']]+[tuple(reroot['source_positions'])]))
outside=list(dict.fromkeys([tuple(p) for r in old['families'] if r['base']==19 and r['partner']==0 for p in r['positions']]))
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

new=json.loads((P/'MIXED_ONE_SIX_MINIMUM_PAIR_PILOT.json').read_text())
results=[]
for f in dom['results']:
 base=f['base'];i=f['partner'];pos=outside if i==0 else inside
 if base==16 and i==2:
  # old C={4,5,6}, partner4, maps to C={2,3,6}, partner2; z6 fixed.
  m=[0,1,4,5,2,3,6,7,8];pos=[tuple(p[m[j]] for j in range(9)) for p in pos]
 pos=list(pos)
 for z in new['results']:
  m=list(range(9));m[i],m[z['partner']]=m[z['partner']],m[i];pp=tuple(z['positions'][m[j]] for j in range(9));pos.extend([pp,pp[:7]+(pp[8],pp[7])])
 pos=list(dict.fromkeys(pos));engines=[Fixed(p) for p in pos];rr=[];res=[]
 for idx,z in enumerate(f['cases']):
  ns={int(t):n for t,n in z['counts'].items()};vals=[e.bound(ns) for e in engines];v=min(vals);r=dict(case_index=idx,position_index=vals.index(v),minimum_raw=str(Q(v,D)));rr.append(r)
  if v>=D:res.append(r)
 r=dict(base=base,partner=i,positions=pos,cases=len(rr),strict=len(rr)-len(res),residual=res,maximum_minimum_raw=str(max(Q(z['minimum_raw']) for z in rr)),results=rr);results.append(r);print(base,i,len(pos),len(rr),len(res),r['maximum_minimum_raw'],flush=True)
out=dict(scope=__doc__,complete=True,cases=sum(f['cases'] for f in results),strict=sum(f['strict'] for f in results),residual=sum(len(f['residual']) for f in results),results=results,elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_MINIMUM_PAIR_TEMPLATE_SCREEN.json').write_text(json.dumps(out,indent=2)+'\n');print('seconds',out['elapsed_seconds'])
