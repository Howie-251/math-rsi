"""Independent complete443 triangle-extension cases for the seven-core with
one five-point trace. Stars are generated as partitions of eight labelled
incidences (partner twice), and fixed rawABC bounds use direct pair formulas.
No original generator, DP, probability, quota or fixed-coefficient code imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,product
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=16;domain=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());screen=json.loads((P/'A7_TRIANGLE_FIXED_SCREEN.json').read_text())
partitions={()}
for k in range(8):
 new=set()
 for pp in partitions:
  new.add(tuple(sorted(pp+(1<<k,))))
  for j,b in enumerate(pp):new.add(tuple(sorted(pp[:j]+pp[j+1:]+(b|(1<<k),))))
 partitions=new
assert len(partitions)==4140

def act(pp,g):return tuple(sorted((g[t],n) for t,n in pp))
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def raw(ns,pos):
 total=Q(0)
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
  A=sum(n*ew(t,left,a) for t,n in ns.items());B=sum(n*ew(t,right,b) for t,n in ns.items());D=sum(n*(m-(t==u))*pw(t,u) for t,n in ns.items() for u,m in ns.items());total+=min(A,B,D)
 return total
families=[]
for f in domain['results']:
 if f['base']!=21:continue
 i=f['partner'];mu={int(t):n for t,n in f['core_counts'].items()};labels=list(range(7))+[i];stars=set()
 for pp in partitions:
  counts=Counter();ok=True
  for b in pp:
   t=sum(1<<labels[j] for j in range(8) if b>>j&1)
   # Repeated partner in one block would give a duplicate bit contribution.
   js=[labels[j] for j in range(8) if b>>j&1]
   if len(set(js))!=len(js):ok=False;break
   t=sum(1<<j for j in js)
   if t.bit_count()>4 or not mu.get(t,0):ok=False;break
   counts[t]+=1
  if ok and all(n<=mu[t] for t,n in counts.items()) and 0<=7-len(pp)<=mu[0]:stars.add(tuple(sorted(counts.items())))
 assert len(stars)==f['stars']
 groups=[]
 for mm in permutations(range(7)):
  if mm[i]!=i or {mm[j] for j in range(2,7)}!=set(range(2,7)):continue
  groups.append([sum(1<<mm[j] for j in range(7) if t>>j&1) for t in range(128)])
 roots={min(act(p,g) for g in groups) for p in stars};expected=set()
 for ps in roots:
  p=dict(ps);p[0]=7-sum(p.values());stab=[g for g in groups if act(ps,g)==ps]
  for rs in stars:
   r=dict(rs);r[0]=7-sum(r.values());common=sorted(set(p)&set(r))
   for vv in product(*(range(max(0,p[t]+r[t]-mu[t]),min(p[t],r[t])+1) for t in common)):
    q=dict(zip(common,vv))
    if not 2<=sum(q.values())<=4:continue
    ns={};ok=True
    for t,n in mu.items():
     a=p.get(t,0);b=r.get(t,0);c=q.get(t,0);cells=[n-a-b+c,a-c,b-c,c]
     if min(cells)<0:ok=False;break
     for mask,z in enumerate(cells):
      if z:ns[t+128*mask]=z
    if not ok or any(t.bit_count()>5 for t in ns):continue
    expected.add(min(tuple(sorted(((t&384)|g[t&127],n) for t,n in ns.items())) for g in stab))
 actual={tuple(sorted((int(t),n) for t,n in z['counts'].items())) for z in f['cases']};assert actual==expected and len(actual)==len(f['cases'])
 positions=next(z['positions'] for z in screen['families'] if (z['base'],z['partner'])==(21,i));records=[]
 for idx,z in enumerate(f['cases']):
  ns={int(t):n for t,n in z['counts'].items()};vals=[raw(ns,pos) for pos in positions];best=min(vals);assert best<1
  records.append(dict(case_index=idx,positions=positions[vals.index(best)],raw_ABC_bound=str(best)))
 maximum=max(Q(z['raw_ABC_bound']) for z in records);assert maximum==Q(next(z['maximum_minimum_raw'] for z in screen['families'] if (z['base'],z['partner'])==(21,i)))
 families.append(dict(base=21,partner=i,independent_stars=len(stars),independent_domain=len(expected),all_raw_strict=True,maximum_raw=str(maximum),records=records));print(i,len(expected),maximum,flush=True)
out=dict(scope=__doc__,passed=True,domain_complete=True,cases=sum(z['independent_domain'] for z in families),families=families,elapsed_seconds=time.perf_counter()-st)
(P/'A7_TRIANGLE_FIVE_TRACE_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','domain_complete','cases','elapsed_seconds']},indent=2))
