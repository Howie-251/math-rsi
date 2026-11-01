"""Exact standalone aggregate verifier. No scipy; no H assertion."""
from pathlib import Path
from math import comb
from fractions import Fraction as F
from itertools import product
import json
P=Path(__file__).resolve().parent
beta=[comb(8+j,5)+comb(8+j,2+j) for j in range(5)]
assert beta==[84,210,462,924,1716]
D=comb(21,10);p=F(2,57);threshold=10*(2-35*p)
assert threshold==F(440,57) and threshold*D==2722720
# Rebuild all labeled Venn possibilities independently, then quotient pair labels.
keys=set()
for a,b,c in product(range(5),repeat=3):
 for t in range(5):
  if t>min(a,b,c):continue
  if min(5-a-b+t,5-a-c+t,5-b-c+t)<0:continue
  keys.add((tuple(sorted((a,b,c))),t))
assert len(keys)==44

def check(n,lam,terms):
 n=list(map(F,n));lam=list(map(F,lam));tau=sum(comb(l-1,2)*v for l,v in enumerate(lam,1))
 assert sum(n)==595 and sum(j*n[j] for j in range(5))==648 and n[1]>=397
 assert sum(comb(j,2)*n[j] for j in range(5))==140+tau
 assert sum(lam)==210 and sum(l*v for l,v in enumerate(lam,1))==350
 terms=[(tuple(js),t,F(v)) for js,t,v in terms]
 assert all((js,t) in keys and v>=0 for js,t,v in terms)
 assert sum(v for js,t,v in terms)==comb(35,3)
 for j in range(5):assert sum(v*js.count(j) for js,t,v in terms)==33*n[j]
 assert sum(t*v for js,t,v in terms)==1399
 m2=sum(comb(t,2)*v for js,t,v in terms)
 assert m2==sum(comb(l,3)*v for l,v in enumerate(lam,1))
 f=[F(0)]*5
 for js,t,v in terms:
  if t==0:
   for k in range(3):
    if all(js[l]==1 for l in range(3) if l!=k):f[js[k]]+=v
 for j in range(5):assert f[j]<=min(33,8*(5-j))*n[j]
 for j,base in ((2,18),(3,8),(4,2)):
  assert f[j]<=base*n[j]+sum((9-l)**(1 if j==4 else 2)*max(l-2,0)*v for l,v in enumerate(lam,1))
 val=sum(a*b for a,b in zip(f,beta));assert val>threshold*D
 return {'flag_counts_by_outer_intersection':[str(v) for v in f],'weighted_flag_numerator':str(val),'EU':str(val/D),'tau':str(tau),'pointpair_third_moment':str(m2)}
j=json.loads((P/'AGGREGATE.json').read_text())
terms=[(q['pair_intersections'],q['triple_intersection'],q['count']) for q in j['witness']]
float_found=check(j['n'],j['pointpair_codegree_counts'],terms)
# Hand-rounded INTEGRAL aggregate witness, not an integral H incidence system.
n=[28,540,0,0,27];lam=[90,102,16,2,0,0,0,0,0]
terms=[([0,0,0],0,308),([1,1,1],0,4684),([1,1,1],1,678),([1,1,4],0,170),([1,1,4],1,697),([4,4,4],3,8)]
integer=check(n,lam,terms)
assert integer['weighted_flag_numerator']=='3242640'
out={'status':'PASS','scope':'beta and complete44 Venn parameter domain; exact two aggregate feasibility checks, not H realizability','denominator':D,'EU_required_lower_bound':str(threshold),'fractional_LP_witness':float_found,'integral_aggregate_witness':dict(integer,n=n,pointpair_codegree_counts=lam,triple_terms=[dict(pair_intersections=js,triple_intersection=t,count=v) for js,t,v in terms])}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
