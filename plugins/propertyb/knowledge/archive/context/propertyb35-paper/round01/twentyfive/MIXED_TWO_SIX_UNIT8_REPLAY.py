"""Reconstruct all65 unit8 families with each pair of degree6 labels; replay raw ABC.
No original domain, orbit transporter, DP, quota or coefficient code is imported.
The complete65-family unit catalogue itself is an explicit imported classification.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from itertools import combinations
import json,time
P=Path(__file__).resolve().parent;root=P.parents[3];st=time.perf_counter()
src=json.loads((root/'context/propertyb34/round01/high-math/UNIT_CATALOGUE_8.json').read_text());cert=json.loads((P/'MIXED_TWO_SIX_UNIT8_CERTIFICATE.json').read_text());domain={};new=[]
for base,big in enumerate(src['orbits']):
 used=set();blocks=list(big)
 for t in big:
  assert 3<=t.bit_count()<=5
  for i,j in combinations([i for i in range(8) if t>>i&1],2):
   assert (i,j) not in used;used.add((i,j))
 for i,j in combinations(range(8),2):
  if (i,j) not in used:blocks.append((1<<i)+(1<<j))
 singles=[7-sum(t>>i&1 for t in blocks) for i in range(8)];empty=37-len(blocks)-sum(singles)
 for low in combinations(range(8),2):
  ss=[v-int(i in low) for i,v in enumerate(singles)]
  if min(ss)<0 or empty<0:continue
  ns={t:1 for t in blocks};ns.update({1<<i:v for i,v in enumerate(ss) if v})
  if empty:ns[0]=empty
  assert sum(ns.values())==35
  assert all(sum(n for t,n in ns.items() if t>>i&1)==7-int(i in low) for i in range(8))
  assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==1 for i,j in combinations(range(8),2))
  domain[(base,low)]=ns
 if empty<2 and sum(v>=1 for v in singles)>=2:new.append(base)
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def raw(ns,pos):
 assert len(set(pos))==8 and all(1<=v<=25 for v in pos);N=17;total=Q(0)
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
assert src['complete'] and len(src['orbits'])==65
assert {(z['base'],tuple(z['low'])) for z in cert['results']}==set(domain)
records=[]
for z in cert['results']:
 ns=domain[(z['base'],tuple(z['low']))];assert ns=={int(t):n for t,n in z['counts'].items() if n};b=raw(ns,z['positions']);assert b==Q(z['raw_ABC_bound']) and b<1
 records.append(dict(base=z['base'],low=z['low'],raw_ABC_bound=str(b)))
out=dict(passed=True,complete_conditional_unit8_domain=True,source_families=65,feasible_families=len({i for i,j in domain}),marked_inputs=len(domain),new_old_negative_empty_families=new,all_raw_strict=True,maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in records)),elapsed_seconds=time.perf_counter()-st,results=records)
(P/'MIXED_TWO_SIX_UNIT8_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))
