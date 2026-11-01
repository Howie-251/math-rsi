"""Only the815 minimum-empty old inputs, screened using six new pilot layouts
plus the two previous fixed layouts. No new input domain or per-input DP.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=16;D=factorial(N)
dom=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());fil=json.loads((P/'A7_MINIMUM_EMPTY_FILTER.json').read_text());pilot=json.loads((P/'A7_MINIMUM_EMPTY_PILOT.json').read_text());old=json.loads((P/'A7_TRIANGLE_FIXED_SCREEN.json').read_text())
f=next(z for z in dom['results'] if z['base']==19 and z['partner']==4);indices=[z['case_index'] for r in fil['results'] if r['partner']==4 for z in r['retained_cases']]
positions=list(dict.fromkeys([tuple(p) for r in old['families'] if r['base']==19 and r['partner']==4 for p in r['positions']]+[tuple(z['positions']) for z in pilot['results']]))
reroot=json.loads((P/'A7_MINIMUM_EMPTY_REROOT.json').read_text());assert reroot['passed']
if tuple(reroot['source_positions']) not in positions:positions.append(tuple(reroot['source_positions']))
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

engines=[Fixed(p) for p in positions]
for z in pilot['results']:
 eng=engines[positions.index(tuple(z['positions']))];assert Q(eng.bound({int(t):n for t,n in z['counts'].items()}),D)==Q(z['raw_ABC_bound'])
results=[];res=[]
for idx in indices:
 ns={int(t):n for t,n in f['cases'][idx]['counts'].items()};vv=[e.bound(ns) for e in engines];v=min(vv);r=dict(case_index=idx,position_index=vv.index(v),minimum_raw=str(Q(v,D)));results.append(r)
 if v>=D:res.append(r)
out=dict(scope=__doc__,positions=positions,cases=len(results),strict=len(results)-len(res),residual=res,maximum_minimum_raw=str(max(Q(z['minimum_raw']) for z in results)),results=results,elapsed_seconds=time.perf_counter()-st)
(P/'A7_MINIMUM_EMPTY_TEMPLATE_SCREEN.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['cases','strict','maximum_minimum_raw','elapsed_seconds']},indent=2));print('templates',len(positions),'residual',len(res))
