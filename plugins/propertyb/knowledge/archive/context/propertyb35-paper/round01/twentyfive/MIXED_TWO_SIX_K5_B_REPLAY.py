"""Independent116 forced CaseB inputs, complete51-partition conditioning.
Nonempty shared cells use all0/1 choices and empty0..min degrees, followed by
exact slot tests; no original domain/DP/probability/quota code is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from itertools import product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());pilot=json.loads((P/'MIXED_TWO_SIX_K5_B_PILOT.json').read_text())
def restore(ident,degrees,p,r=None,joint=None):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};x={t:1 for t in p};x[0]=degrees[5]-len(p);ns={}
 if r is None:
  for t,n in mu.items():
   a=x.get(t,0);assert 0<=a<=n
   if n-a:ns[t]=n-a
   if a:ns[t+32]=a
 else:
  y={t:1 for t in r};y[0]=degrees[6]-len(r);joint=joint or {}
  for t,n in mu.items():
   a=x.get(t,0);b=y.get(t,0);c=joint.get(t,0);vv=[n-a-b+c,a-c,b-c,c];assert min(vv)>=0
   for mask,v in enumerate(vv):
    if v:ns[t+32*mask]=v
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(degrees))
 for i in range(len(degrees)):
  for j in range(i+1,len(degrees)):
   lam=sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)
   assert lam==(2 if j<5 else sum(joint.values()) if (i,j)==(5,6) else 1)
   if degrees[i]==6 or degrees[j]==6:assert lam==1
 projected=Counter()
 for t,n in ns.items():projected[t&31]+=n
 assert dict(projected)==mu
 return ns
def key(ident,degrees,ns):return ident,tuple(degrees),tuple(sorted(ns.items()))
expected={}
parts={()}
for i in range(5):
 nxt=set()
 for pp in parts:
  nxt.add(tuple(sorted(pp+(1<<i,))))
  for j,t in enumerate(pp):nxt.add(tuple(sorted(pp[:j]+pp[j+1:]+(t|(1<<i),))))
 parts=nxt
assert len(parts)==52
parts.remove((31,))
def allowed(ident,T):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()}
 return sorted(p for p in parts if T in p and all(mu.get(t,0) for t in p))
def appendpair(ident,d,e,ps,T=None):
 mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()}
 for p,r in product(ps,repeat=2):
  common=sorted(set(p)&set(r));p0=d-len(p);r0=e-len(r)
  for bits in product([0,1],repeat=len(common)):
   qq={t:v for t,v in zip(common,bits) if v}
   if T is not None and qq.get(T,0)!=1:continue
   for q0 in range(min(p0,r0)+1):
    q=dict(qq)
    if q0:q[0]=q0
    lam=sum(q.values())
    if not (lam==1 if d==6 else 1<=lam<=(9 if d==e==8 else 5)):continue
    xx={t:1 for t in p};xx[0]=p0;yy={t:1 for t in r};yy[0]=r0
    if any(min(n-xx.get(t,0)-yy.get(t,0)+q.get(t,0),xx.get(t,0)-q.get(t,0),yy.get(t,0)-q.get(t,0),q.get(t,0))<0 for t,n in mu.items()):continue
    ds=[7]*5+[d,e];ns=restore(ident,ds,p,r,q);expected[key(ident,ds,ns)]=ns
for ident,ts in [(11,[22,26]),(13,[21,25]),(17,[13,19])]:
 for T in ts:
  for p in allowed(ident,T):
   ds=[7]*5+[6];ns=restore(ident,ds,p);expected[key(ident,ds,ns)]=ns
for ident,T in [(1,13),(5,11),(8,25),(10,13)]:appendpair(ident,7,8,allowed(ident,T),T)
for ident,T in [(7,22),(9,19)]:
 for d,e in [(6,6),(6,7)]:appendpair(ident,d,e,allowed(ident,T),T)
for d,e in [(6,8),(7,8)]:appendpair(26,d,e,allowed(26,22),22)
appendpair(12,8,8,[(5,26),(3,28)])
appendpair(24,8,8,allowed(24,28),28)
actual=pilot['results'];assert len(actual)==len(expected)==116
assert {key(z['id'],z['degrees'],{int(t):n for t,n in z['counts'].items()}) for z in actual}==set(expected)
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def raw(ns,pos,expected_rows):
 N=25-len(pos);total=Q(0)
 for k in range(1,26):
  left=sum(1<<i for i,p in enumerate(pos) if p<k);right=sum(1<<i for i,p in enumerate(pos) if p>k);pivot=next((1<<i for i,p in enumerate(pos) if p==k),0);a=k-1-left.bit_count();b=25-k-right.bit_count()
  def ew(t,side,slots):
   r=5-t.bit_count()
   if pivot:
    if not t&pivot or (t^pivot)&~side:return Q(0)
    return Q(C(slots,r),C(N,r))
   if not r or t&~side:return Q(0)
   return Q(r*C(slots,r-1),N*C(N-1,r-1))
  def pw(t,u):
   r=5-t.bit_count();q=5-u.bit_count()
   if pivot:
    if t&u!=pivot or (t^pivot)&~left or (u^pivot)&~right or r+q>N:return Q(0)
    return Q(C(a,r)*C(b,q),C(N,r)*C(N-r,q))
   if not r or not q or t&u or t&~left or u&~right or r+q-1>N:return Q(0)
   return Q(C(a,r-1)*C(b,q-1),N*C(N-1,r-1)*C(N-r,q-1))
  A=sum(n*ew(t,left,a) for t,n in ns.items());B=sum(n*ew(t,right,b) for t,n in ns.items());D=sum(n*(m-(t==u))*pw(t,u) for t,n in ns.items() for u,m in ns.items());rr=expected_rows[k-1];assert Q(rr['A'])==A and Q(rr['B'])==B and Q(rr['C'])==D;total+=min(A,B,D)
 return total


records=[]
for z in actual:
 ns={int(t):n for t,n in z['counts'].items()};b=raw(ns,z['positions'],z['rows']);assert b==Q(z['raw_ABC_bound']) and b<1;records.append(dict(id=z['id'],degrees=z['degrees'],raw_ABC_bound=str(b)))
bytype=[dict(id=i,cases=sum(z['id']==i for z in records),maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in records if z['id']==i))) for i in sorted({z['id'] for z in records})]
selection=json.loads((P/'MIXED_ONE_SIX_K5_SELECTION_CHECK.json').read_text());costs=[]
for ident in [14,20,22]:
 f=next(f for f in selection['old_sixlock_classes_transferred'] if f['id']==ident);mu={int(t):n for t,n in cat['representatives'][ident]['counts'].items()};cost=sum(mu[t]*t.bit_count()*(5-t.bit_count()) for t in f['strict_pair_traces']+f['strict_three_traces']);assert cost>20;costs.append(dict(id=ident,strict_trace_special_incidence_cost=cost))
out=dict(scope=__doc__,passed=True,domain_complete=True,cases=116,all_raw_strict=True,maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in records)),families=bytype,selection_costs=costs,elapsed_seconds=time.perf_counter()-st,results=records)
(P/'MIXED_TWO_SIX_K5_B_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
