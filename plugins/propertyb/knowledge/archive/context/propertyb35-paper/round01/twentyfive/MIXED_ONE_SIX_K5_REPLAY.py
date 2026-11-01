"""Independent full41 mixed-single-K5 forced inputs and raw ABC replay.
The36 type24 parameters are listed directly by hand cases; no original domain,
DP, probability, quota or position-coefficient implementation is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from itertools import product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());pilot=json.loads((P/'MIXED_ONE_SIX_K5_PILOT.json').read_text());t24=json.loads((P/'MIXED_ONE_SIX_K5_TYPE24.json').read_text())
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
for d in [6,8]:
 ds=[7]*5+[d];ns=restore(25,ds,[1,30]);expected[key(25,ds,ns)]=ns
for p,r in [([5,26],[3,28]),([3,28],[5,26])]:
 ds=[7]*5+[6,8];ns=restore(12,ds,p,r,{0:1});expected[key(12,ds,ns)]=ns
ds=[7]*5+[6,7];ns=restore(26,ds,[1,8,22],[1,8,22],{22:1});expected[key(26,ds,ns)]=ns
A=[1,2,28];B=[3,28]
for d,e in [(6,7),(6,8)]:
 for p,r in [(A,A),(A,B),(B,A)]:
  ds=[7]*5+[d,e];ns=restore(24,ds,p,r,{28:1});expected[key(24,ds,ns)]=ns
for j,k in product([0,1],repeat=2):
 for q0 in range(5-j-k):
  q={28:1}
  if j:q[1]=j
  if k:q[2]=k
  if q0:q[0]=q0
  ds=[7]*5+[7,8];ns=restore(24,ds,A,A,q);expected[key(24,ds,ns)]=ns
for p,r in [(A,B),(B,A)]:
 for q0 in range(5):
  ds=[7]*5+[7,8];q={28:1}
  if q0:q[0]=q0
  ns=restore(24,ds,p,r,q);expected[key(24,ds,ns)]=ns
for q0 in range(4):
 ds=[7]*5+[7,8];q={28:1,3:1}
 if q0:q[0]=q0
 ns=restore(24,ds,B,B,q);expected[key(24,ds,ns)]=ns
actual=pilot['results']+t24['results'];assert len(actual)==len(expected)==41
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
 ns={int(t):n for t,n in z['counts'].items()};bound=raw(ns,z['positions'],z['rows']);assert bound==Q(z['raw_ABC_bound']) and bound<1
 records.append(dict(id=z['id'],degrees=z['degrees'],positions=z['positions'],raw_ABC_bound=str(bound)))
families=[]
for ident in [12,24,25,26]:
 zz=[z for z in records if z['id']==ident];families.append(dict(id=ident,cases=len(zz),all_raw_strict=True,maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in zz))))
out=dict(scope=__doc__,passed=True,domain_complete=True,cases=41,all_raw_strict=True,families=families,results=records,elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_K5_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','domain_complete','cases','all_raw_strict','families','elapsed_seconds']},indent=2))
