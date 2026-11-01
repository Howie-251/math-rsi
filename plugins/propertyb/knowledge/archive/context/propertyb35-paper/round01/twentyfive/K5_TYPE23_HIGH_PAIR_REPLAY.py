"""Independent full 18-domain and raw ABC replay for type23 high B-B pairs.
No DP, probability, quota or original domain generator is imported.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as Q
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=18
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());mu={int(t):n for t,n in cat['representatives'][23]['counts'].items()};src=json.loads((P/'K5_TYPE23_HIGH_PAIR.json').read_text());Bs=[(3,4,24),(3,8,20),(3,12,16)]
assert mu=={0:14,**{1<<i:2 for i in range(5)},**{(1<<i)+(1<<j):1 for i in range(5) for j in range(i+1,5)},31:1}
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def restore(p,r,q):
 out={}
 for t,n in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);c=q.get(t,0)
  vv=[n-a-b+c,a-c,b-c,c]
  if min(vv)<0:return None
  for mask,v in enumerate(vv):
   if v:out[t+32*mask]=v
 if any(t.bit_count()>5 for t in out):return None
 assert sum(out.values())==35 and all(sum(n for t,n in out.items() if t>>i&1)==7 for i in range(7))
 assert all(sum(n for t,n in out.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(5) for j in range(i+1,7))
 assert sum(n for t,n in out.items() if t&96==96)==sum(q.values())
 projected=Counter()
 for t,n in out.items():projected[t&31]+=n
 assert dict(projected)==mu
 return out

def signature(p,r,q):
 p,r=sorted([tuple(sorted(p)),tuple(sorted(r))]);return p,r,tuple(sorted((int(t),n) for t,n in q.items() if n))
expected={}
for p,r in product(Bs,repeat=2):
 p,r=sorted([p,r])
 common=sorted(set(p)&set(r));opts=[[1] if t==3 else list(range(max(0,2-mu[t]),2)) for t in common]
 for vals in product(*opts):
  for q0 in range(5):
   q={t:c for t,c in zip(common,vals) if c}
   if q0:q[0]=q0
   if sum(q.values()) not in [4,5]:continue
   ns=restore(p,r,q)
   if ns is not None:expected[signature(p,r,q)]=ns
actual={signature(z['P'],z['Q'],z['joint']):{int(t):n for t,n in z['counts'].items()} for z in src['results']}
assert len(actual)==len(src['results'])==18 and actual==expected
results=[]
for z in src['results']:
 ns=actual[signature(z['P'],z['Q'],z['joint'])];pos=z['positions'];assert len(pos)==7 and len(set(pos))==7 and all(1<=p<=25 for p in pos);total=Q(0)
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
  A=sum(n*ew(t,left,a) for t,n in ns.items());B=sum(n*ew(t,right,b) for t,n in ns.items());D=sum(n*(m-(t==u))*pw(t,u) for t,n in ns.items() for u,m in ns.items())
  stored=z['rows'][k-1];assert Q(stored['A'])==A and Q(stored['B'])==B and Q(stored['C'])==D
  total+=min(A,B,D)
 assert total==Q(z['raw_ABC_bound']) and total<1
 results.append(dict(P=z['P'],Q=z['Q'],joint=z['joint'],codegree=z['codegree'],raw_ABC_bound=str(total),positions=pos))
# Independently record the six exact stabilizer orbits relevant to the proof.
orbits={}
for z in results:
 equal=z['P']==z['Q'];singleton=next((t for t in z['P'] if t.bit_count()==1),None) if equal else None;j=int(z['joint'].get(str(singleton),0)) if equal else None
 key=(equal,z['codegree'],j);orbits.setdefault(key,set()).add(z['raw_ABC_bound'])
assert len(orbits)==6 and all(len(v)==1 for v in orbits.values())
classes=[dict(equal_partitions=k[0],codegree=k[1],common_singleton_selected=k[2],raw_ABC_bound=next(iter(v))) for k,v in sorted(orbits.items())]
out=dict(scope=__doc__,passed=True,domain_complete=True,cases=18,all_raw_strict=True,maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in results)),six_stabilizer_classes=classes,results=results,elapsed_seconds=time.perf_counter()-st)
(P/'K5_TYPE23_HIGH_PAIR_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','domain_complete','cases','all_raw_strict','maximum_raw','six_stabilizer_classes','elapsed_seconds']},indent=2))
