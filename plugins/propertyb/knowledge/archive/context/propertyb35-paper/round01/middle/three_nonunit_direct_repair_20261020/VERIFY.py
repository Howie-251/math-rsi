from pathlib import Path
from itertools import combinations_with_replacement,permutations
from collections import Counter
from math import comb,factorial
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def extra(t,r):
 if t=='P':return 0
 if t==0:return C(11,r-5)+C(11,r)
 return C(11+t,r)
def bad(types,a,r):
 return a*C(12,r-4)+(31-a)*C(12,r)-max(a-1,0)*C(8,r-8)+sum(extra(t,r) for t in types)
typeslist=list(combinations_with_replacement(['P',0,2,3,4],3));tables={}
for types in typeslist:
 good=[];cert=[]
 for a in range(32):
  choices=[(Fraction(bad(types,a,r),C(16,r)),r,bad(types,a,r),C(16,r)) for r in range(17)]
  ratio,r,U,D=min(choices)
  if ratio<1:good.append(a)
  cert.append({'a':a,'best_r':r,'bad':U,'samples':D,'ratio':str(ratio),'strict':ratio<1})
 fail=[a for a in range(32) if a not in good];k=min(fail) if fail else 32
 # Derive the low-a prefix independently from each affine branch r>=8.
 candidates=[]
 assert min(bad(types,a,8) for a in range(32))>=C(16,8)
 for r in range(9,17):
  R=C(12,r-4);B=C(12,r);J=C(8,r-8);D=C(16,r);e=sum(extra(t,r) for t in types)
  assert R-B-J>=0 and R-B>=0
  if 31*B+e>=D:continue
  slope=R-B-J
  cmax=min(31,(D-1-31*B-J-e)//slope) if slope else (31 if 31*B+J+e<D else 0)
  cmax=max(0,cmax);candidates.append((cmax,r,bad(types,cmax,r),D))
 affine_k=max((x[0]+1 for x in candidates),default=0)
 assert affine_k==k
 fixed=min((x for x in candidates if x[0]==k-1),key=lambda x:Fraction(x[2],x[3])) if k else None
 tables[types]={'types':types,'first_failure_k':k,'safe_a':good,'failure_a':fail,'fixed_prefix_certificate':fixed,'per_a_optimum':cert}
# First full labeled domain: actual five-bit traces and actual S5 action.
allowed=[m for m in range(32) if m.bit_count() in (0,2,3,4)];assert len(allowed)==26
perms=list(permutations(range(5)))
maps=[[sum(1<<p[i] for i in range(5) if m>>i&1) for m in range(32)] for p in perms]
def canon(tr):return min(tuple(sorted(mp[m] for m in tr)) for mp in maps)
orbits=Counter(canon(tr) for tr in combinations_with_replacement(allowed,3));assert sum(orbits.values())==3276
# Different domain: eight incidence cells counts (vertices with membership mask in the three traces).
def comps(n,k):
 if k==1:yield (n,);return
 for x in range(n+1):
  for rest in comps(n-x,k-1):yield (x,)+rest
s3=list(permutations(range(3)))
def cellcanon(c):
 ans=[]
 for p in s3:
  d=[0]*8
  for m,n in enumerate(c):d[sum(1<<p[i] for i in range(3) if m>>i&1)]=n
  ans.append(tuple(d))
 return min(ans)
def cells(tr):return tuple(sum(sum(((tr[j]>>v)&1)<<j for j in range(3))==m for v in range(5)) for m in range(8))
cell_domain={}
for c in comps(5,8):
 sizes=[sum(n for m,n in enumerate(c) if m>>j&1) for j in range(3)]
 if any(j not in (0,2,3,4) for j in sizes):continue
 cc=cellcanon(c)
 if cc in cell_domain:continue
 # Number ordered labeled trace triples for this membership-cell pattern, summed over distinct row permutations, divided by multiplicity factorials.
 tr=[];v=0;ms=[0,0,0]
 for m,n in enumerate(c):
  for _ in range(n):
   for j in range(3):
    if m>>j&1:ms[j]|=1<<v
   v+=1
 tr=tuple(sorted(ms));multiplicity=Counter(tr)
 distinct_row_patterns=len({tuple(cells(tuple(tr[j] for j in p))) for p in s3})
 ordered=factorial(5)//__import__('functools').reduce(lambda a,b:a*factorial(b),c,1)*distinct_row_patterns
 # Every unordered triple has 3! / product multiplicity! orderings.
 labels=ordered*__import__('functools').reduce(lambda a,b:a*factorial(b),multiplicity.values(),1)//6
 cell_domain[cc]=labels
assert len(cell_domain)==len(orbits)
assert {cellcanon(cells(tr)):n for tr,n in orbits.items()}==cell_domain
rows=[]
for tr,labels in sorted(orbits.items()):
 types=[tuple(sorted(('P' if m>>v&1 else m.bit_count() for m in tr),key=lambda x:['P',0,2,3,4].index(x))) for v in range(5)]
 tt=[tables[t] for t in types];ks=[t['first_failure_k'] for t in tt]
 # Exact number of failed attachments, using all safe tails as well as low-a prefixes.
 count={0:1};witness={0:()}
 for t in tt:
  nc={};nw={}
  for old,n in count.items():
   for a in t['failure_a']:
    if old+a<=31:nc[old+a]=nc.get(old+a,0)+n;nw.setdefault(old+a,witness[old]+(a,))
  count,witness=nc,nw
 failcount=count.get(31,0);wit=witness.get(31)
 if sum(ks)>31:assert failcount==0
 if wit:
  assert sum(wit)==31 and all(a in t['failure_a'] for a,t in zip(wit,tt))
  assert all(bad(t,a,r)>=C(16,r) for t,a in zip(types,wit) for r in range(17))
 rows.append({'traces':tr,'trace_sizes':[m.bit_count() for m in tr],'labels':labels,'types_by_v':types,'k_by_v':ks,'sum_k':sum(ks),'failed_attachment_compositions':failcount,'attachment_witness':wit})
remaining=[r for r in rows if r['failed_attachment_compositions']]
out={'status':'COMPLETE_THRESHOLD_DOMAIN_DIAGNOSIS','scope':'qGamma(F)=3, original 21 vertices/35 distinct five-edges; three actual exception traces allowed repeated; no point degrees, paircover, criticality or exception Gamma-leaf assumption. One-red-in-F + uniform r red outside and arbitrary red-event tree only. Failure is failure of this upper-bound strategy, not noncolorability.','labeled_triples':3276,'S5_trace_orbits':len(orbits),'independent_eight_cell_orbits':len(cell_domain),'all_attachment_compositions_per_orbit':comb(35,4),'residual_types':list(tables.values()),'orbits':rows,'threshold_only_closed_orbits':sum(r['sum_k']>31 for r in rows),'full_safe_sets_closed_orbits':len(rows)-len(remaining),'remaining_orbit_count':len(remaining),'remaining':remaining,'cpu_seconds':time.process_time()-st}
assert out['cpu_seconds']<15
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: labeled3276 / orbit',len(orbits),'independent cells',len(cell_domain),'remaining',len(remaining),'cpu',out['cpu_seconds'])
for r in remaining:print(r['traces'],r['trace_sizes'],'k',r['k_by_v'],'sum',r['sum_k'],'failed',r['failed_attachment_compositions'],'witness',r['attachment_witness'])
