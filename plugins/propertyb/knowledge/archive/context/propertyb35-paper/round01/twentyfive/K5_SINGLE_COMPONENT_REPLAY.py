"""Independent selected-domain and rational replay for one real K5 component.
Rebuilds all 135 selected pair inputs without importing DP/probability/quota
code. Also records the uncorrected ABC bounds used by the mathematical proof.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=18
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());six=json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text());source=json.loads((P/'K5_SINGLE_COMPONENT_DOMAIN.json').read_text());complete=json.loads((P/'K5_SINGLE_COMPONENT_COMPLETE.json').read_text())
parts={frozenset()}
for i in range(5):
 new=set()
 for pp in parts:
  new.add(pp|{1<<i})
  for t in pp:new.add((pp-{t})|{t|(1<<i)})
 parts=new
parts.remove(frozenset({31}));assert len(parts)==51

def restore(mu,p,r,q):
 ns={}
 for t,n in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);c=q.get(t,0)
  cells=[n-a-b+c,a-c,b-c,c]
  if min(cells)<0:return None
  for mask,nn in enumerate(cells):
   if nn:ns[t+32*mask]=nn
 if any(t.bit_count()>5 for t in ns):return None
 assert sum(ns.values())==35
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(7))
 assert all(sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(5) for j in range(i+1,7))
 assert sum(c for t,c in ns.items() if t&96==96)==sum(q.values())
 proj=Counter()
 for t,c in ns.items():proj[t&31]+=c
 assert dict(proj)==mu
 return ns
def C(n,k):return comb(n,k) if 0<=k<=n else 0
# Independent set-partition generation by joining each next element to an
# existing block or forming a new block, compared as unordered block families.
parts={frozenset()}
for i in range(5):
 nxt=set()
 for pp in parts:
  nxt.add(pp|{1<<i})
  for t in pp:nxt.add((pp-{t})|{t|(1<<i)})
 parts=nxt
parts.discard(frozenset({31}));assert len(parts)==51

def replay(z):
 ns={int(t):c for t,c in z['counts'].items()};pos=z['positions'];mu={int(t):c for t,c in cat['representatives'][z['id']]['counts'].items()}
 rebuilt=restore(mu,tuple(z['P']),tuple(z['Q']),{int(t):c for t,c in z['joint'].items()});assert rebuilt==ns
 assert len(pos)==7 and len(set(pos))==7 and all(1<=x<=25 for x in pos)
 total=Q(0);certs=[]
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
  A=sum(c*ew(t,left,a) for t,c in ns.items());B=sum(c*ew(t,right,b) for t,c in ns.items())
  rawC=sum(c*(d-(t==u))*pw(t,u) for t,c in ns.items() for u,d in ns.items());loss=Q(0)
  if pivot:
   ts=sorted(t for t in ns if t&pivot);slots=[]
   for j,t in enumerate(ts):
    for u in ts[j:]:
     cap=C(ns[t],2) if t==u else ns[t]*ns[u]
     if cap:slots.append([pw(t,u)+pw(u,t),cap,t==u==pivot])
   pure=max(0,(4*ns.get(pivot,0)-N+2)//3);assert pure<=2
   rem=pure
   for slot in slots:
    if slot[2]:take=min(rem,slot[1]);rem-=take;slot[1]-=take;loss+=take*slot[0]
   assert rem==0
   rem=2-pure
   for weight,cap,flag in sorted(slots):
    take=min(rem,cap);loss+=take*weight;rem-=take
   assert rem==0
   i=pivot.bit_length()-1;cc=z['certificates'][i];assert cc['q_total']==2 and cc['q_pure']==pure and Q(cc['loss'])==loss
   certs.append(dict(center=i,q_total=2,q_pure=pure,loss=str(loss)))
  row=z['rows'][k-1];assert Q(row['A'])==A and Q(row['B'])==B and Q(row['C'])==rawC
  assert Q(row['deduction'])==loss and Q(row['corrected_C'])==rawC-loss
  v=min(A,B,rawC-loss);assert v==Q(row['bound']);total+=v
 assert total==Q(z['bound'])
 return total

def signature(z):return z['id'],z['T'],tuple(sorted(z['P'])),tuple(sorted(z['Q'])),tuple(sorted((int(t),n) for t,n in z['joint'].items()))
expected={}
for f in source['results']:
 ident=f['id'];mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};T=f['chosen_T'];L=1+4//(4-T.bit_count())
 old=next((g for g in six['families'] if g['id']==ident),None)
 eligible=[frozenset(p) for p in old['residual_partitions']] if old else [p for p in parts if all(mu.get(t,0) for t in p) and mu[0]>=7-len(p)]
 assert set(eligible)=={frozenset(p) for p in f['initial_partitions']}
 for p,r in product([p for p in eligible if T in p],repeat=2):
  p,r=sorted([tuple(sorted(p)),tuple(sorted(r))]);commons=sorted(set(p)&set(r));options=[]
  for t in commons:
   options.append([1] if t==T else list(range(max(0,2-mu[t]),2)))
  p0=7-len(p);r0=7-len(r)
  for vals in product(*options):
   for q0 in range(max(0,p0+r0-mu[0]),min(p0,r0)+1):
    q={t:c for t,c in zip(commons,vals) if c}
    if q0:q[0]=q0
    if not 1<=sum(q.values())<=L:continue
    ns=restore(mu,p,r,q)
    if ns is not None:expected[(ident,T,p,r,tuple(sorted(q.items())))]=ns
actual={signature(z):{int(t):n for t,n in z['counts'].items()} for f in source['results'] for z in f['cases']}
assert len(actual)==135 and expected==actual
assert {signature(z) for z in complete['results']}==set(expected)
results=[]
for z in complete['results']:
 bound=replay(z);raw=sum(min(Q(r['A']),Q(r['B']),Q(r['C'])) for r in z['rows']);assert bound<=raw
 results.append(dict(id=z['id'],T=z['T'],P=z['P'],Q=z['Q'],joint=z['joint'],codegree=z['codegree'],bound=str(bound),raw_ABC_bound=str(raw)))
families=[]
for f in source['results']:
 zz=[z for z in results if z['id']==f['id']];families.append(dict(id=f['id'],T=f['chosen_T'],cases=len(zz),strict=sum(Q(z['bound'])<1 for z in zz),raw_strict=sum(Q(z['raw_ABC_bound'])<1 for z in zz),maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in zz)),residual=[z for z in zz if Q(z['raw_ABC_bound'])>=1]))
assert [f['id'] for f in families if f['raw_strict']!=f['cases']]==[23]
out=dict(scope=__doc__,passed=True,cases=135,strict=131,all_nine_eliminated_families_strict_without_quota=True,families=families,results=results,elapsed_seconds=time.perf_counter()-st)
(P/'K5_SINGLE_COMPONENT_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','cases','strict','all_nine_eliminated_families_strict_without_quota','elapsed_seconds']},indent=2));print([(z['id'],z['T'],z['cases'],z['raw_strict'],z['maximum_raw']) for z in families])
