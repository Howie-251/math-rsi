"""Independent four-root domain reconstruction and raw ABC replay.
Stars use first-uncovered-coordinate recursion, not labelled set partitions.
Every ordered pair and allowed intersection split is generated without symmetry
reduction. Full-domain coverage is checked against exact automorphic images of
all2069 concrete raw witnesses. No original domain/DP/coeff/quota code imported.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction as Q
from math import comb
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;root=P.parents[3];st=time.perf_counter();src=json.loads((root/'context/propertyb34/round01/high-math/UNIT_CATALOGUE_7.json').read_text());cert=json.loads((P/'MIXED_ONE_SIX_MINIMUM_PAIR_CERTIFICATE.json').read_text());records=[];verified=0

def core(base):
 big=src['orbits'][base];used=set();blocks=list(big)
 for t in big:
  for a,b in combinations([j for j in range(7) if t>>j&1],2):assert (a,b) not in used;used.add((a,b))
 for a,b in combinations(range(7),2):
  if (a,b) not in used:blocks.append((1<<a)+(1<<b))
 ns={t:1 for t in blocks}
 for j in range(7):
  n=7-int(j==6)-sum(t>>j&1 for t in blocks)
  if n:ns[1<<j]=n
 ns[0]=35-sum(ns.values());assert ns[0]==(6 if base==16 else 7);return ns

def stars(mu,i):
 ts=sorted(t for t in mu if t);out=set()
 def rec(rem,p,start=0):
  if not any(rem):
   r=7-sum(p.values())
   if 0<=r<=mu[0]:out.add(tuple(sorted(p.items())))
   return
  j=next(j for j,n in enumerate(rem) if n)
  for t in ts:
   if t<start or not t>>j&1 or p.get(t,0)>=mu[t] or t.bit_count()>4 or any(t>>k&1 and not rem[k] for k in range(7)):continue
   nxt=tuple(n-int(t>>k&1) for k,n in enumerate(rem));pp=dict(p);pp[t]=pp.get(t,0)+1
   if sum(pp.values())<=7:rec(nxt,pp,t if nxt[j] else 0)
 rec(tuple(2 if j==i else 1 for j in range(7)),{})
 kept=[]
 for key in sorted(out):
  p=dict(key);p[0]=7-sum(p.values());changed=Counter()
  for t,n in mu.items():
   u=t&~(1<<i);changed[u]+=n-p.get(t,0);changed[u|(1<<i)]+=p.get(t,0)
  changed={t:n for t,n in changed.items() if n};e=changed.get(0,0);large=[t for t,n in changed.items() for _ in range(n) if t.bit_count()>=3]
  # Exactly the already-proved residual marked unit7 gate, plus minimum empty.
  allow=(e==6 and len(large)==2 and all(t.bit_count()==3 and t>>6&1 for t in large)) or (e==7 and len(large)==1 and large[0].bit_count()==3 and large[0]>>6&1) or (e==8 and not large)
  if allow and e>=mu[0]:kept.append(p)
 return len(out),kept

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def raw(ns,pos):
 assert len(pos)==len(set(pos))==9 and all(1<=v<=25 for v in pos);N=16;total=Q(0)
 for k in range(1,26):
  L=sum(1<<i for i,p in enumerate(pos) if p<k);R=sum(1<<i for i,p in enumerate(pos) if p>k);piv=next((1<<i for i,p in enumerate(pos) if p==k),0);a=k-1-L.bit_count();b=25-k-R.bit_count()
  def ew(t,S,s):
   r=5-t.bit_count()
   if piv:
    if not t&piv or (t^piv)&~S:return Q(0)
    return Q(C(s,r),C(N,r))
   if not r or t&~S:return Q(0)
   return Q(r*C(s,r-1),N*C(N-1,r-1))
  def pw(t,u):
   r=5-t.bit_count();q=5-u.bit_count()
   if piv:
    if t&u!=piv or (t^piv)&~L or (u^piv)&~R or r+q>N:return Q(0)
    return Q(C(a,r)*C(b,q),C(N,r)*C(N-r,q))
   if not r or not q or t&u or t&~L or u&~R or r+q-1>N:return Q(0)
   return Q(C(a,r-1)*C(b,q-1),N*C(N-1,r-1)*C(N-r,q-1))
  A=sum(n*ew(t,L,a) for t,n in ns.items());B=sum(n*ew(t,R,b) for t,n in ns.items());D=sum(n*(m-(t==u))*pw(t,u) for t,n in ns.items() for u,m in ns.items());total+=min(A,B,D)
 return total

roots=[]
for base,i in [(16,0),(16,2),(19,0),(19,4)]:
 mu=core(base);original,ss=stars(mu,i);free=[j for j in range(7) if j not in [6,i]];gs=[]
 for order in permutations(free):
  m=list(range(9))
  for a,b in zip(free,order):m[a]=b
  tab=[sum(1<<m[j] for j in range(9) if t>>j&1) for t in range(512)]
  if all(mu.get(tab[t],0)==mu.get(t,0) for t in range(128)):gs.append((m,tab))
 cs=[z for z in cert['results'] if (z['base'],z['partner'])==(base,i)];images={};original_keys=set()
 for z in cs:
  ns={int(t):n for t,n in z['counts'].items()};key=tuple(sorted(ns.items()));assert key not in original_keys;original_keys.add(key)
  b=raw(ns,z['positions']);assert b==Q(z['raw_ABC_bound']) and b<1;verified+=1;records.append(dict(base=base,partner=i,case_index=z['case_index'],raw_ABC_bound=str(b)))
  for m,tab in gs:
   kk=tuple(sorted((tab[t],n) for t,n in ns.items()));images.setdefault(kk,z['case_index'])
 encountered=set();expanded=0
 for p in ss:
  for r in ss:
   common=sorted(set(p)&set(r));ranges=[range(max(0,p[t]+r[t]-mu.get(t,0)),min(p[t],r[t])+1) for t in common]
   for nums in product(*ranges):
    q={t:n for t,n in zip(common,nums) if n};lam=sum(q.values())
    if not 2<=lam<=4:continue
    ns={};valid=True
    for t,n in mu.items():
     a=p.get(t,0);b=r.get(t,0);c=q.get(t,0);cells=[n-a-b+c,a-c,b-c,c]
     if min(cells)<0:valid=False;break
     for mask,v in enumerate(cells):
      if v:ns[t+128*mask]=v
    if not valid or any(t.bit_count()>5 for t in ns):continue
    key=tuple(sorted(ns.items()));assert key in images,(base,i,p,r,q)
    assert sum(ns.values())==35 and all(sum(n for t,n in ns.items() if t>>j&1)==7-int(j==6) for j in range(9))
    assert all(sum(n for t,n in ns.items() if t>>a&1 and t>>b&1)==(lam if (a,b)==(7,8) else 2 if a==i and b>=7 else 1) for a,b in combinations(range(9),2))
    encountered.add(key);expanded+=1
 assert original_keys<=encountered and set(images)==encountered
 roots.append(dict(base=base,partner=i,original_single_stars=original,retained_single_stars=len(ss),mark_partner_automorphisms=len(gs),unquotiented_ordered_pair_inputs=expanded,distinct_unquotiented_inputs=len(encountered),certificate_representatives=len(cs),maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in cs))));print(roots[-1],flush=True)
assert verified==len(cert['results'])==2069
out=dict(scope=__doc__,passed=True,full_domain_complete=True,raw_bounds_replayed=verified,roots=roots,maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in records)),elapsed_seconds=time.perf_counter()-st,results=records)
(P/'MIXED_ONE_SIX_MINIMUM_PAIR_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['elapsed_seconds'])
