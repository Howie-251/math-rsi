"""Different labeled-domain implementation; no primary threshold/orbit import."""
from pathlib import Path
from itertools import combinations_with_replacement, permutations, product
from math import comb
from functools import lru_cache
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def binom(n,k):
 if k<0 or k>n:return 0
 return comb(n,k)
@lru_cache(None)
def failures(sig):
 # sig has counts of P,empty,2,3,4 residual events.
 ans=[]
 for a in range(31):
  strict=False
  for r in range(17):
   value=a*binom(12,r-4)+(30-a)*binom(12,12-r)
   if a>=2:value-=(a-1)*binom(8,16-r)
   value+=sig[1]*(binom(11,16-r)+binom(11,11-r))
   for size in (2,3,4):value+=sig[size]*binom(11+size,11+size-r)
   if value<binom(16,r):strict=True;break
  if not strict:ans.append(a)
 return tuple(ans)
# Build signatures without using the primary type keys.
def sig(tr,v):
 out=[0]*5
 for t in tr:
  out[0 if t&(1<<v) else (1 if not t else t.bit_count())]+=1
 return tuple(out)
perms=[(0,)+p for p in permutations(range(1,5))]
def transformed(t,p):return sum(1<<p[v] for v in range(5) if t&(1<<v))
def jointcanon(tr,a):
 out=[]
 for p in perms:
  b=[0]*5
  for v in range(5):b[p[v]]=a[v]
  out.append((tuple(sorted(transformed(t,p) for t in tr)),tuple(b)))
 return min(out)
remaining=set();labeled=0;tail_labeled=0
allowed=[0]+[t for t in range(1,31) if t.bit_count() in (2,3,4)]
for tr in combinations_with_replacement(allowed,4):
 labeled+=1
 if any(sum(bool(t&(1<<i)) and bool(t&(1<<j)) for t in tr)>=4 for i in range(5) for j in range(i)):continue
 if sum((t&30).bit_count() for t in tr if t&1)>4:continue
 h=[sum(bool(t&(1<<v)) for t in tr) for v in range(5)]
 a0=5-h[0]
 if a0 not in failures(sig(tr,0)):continue
 choices=[tuple(a for a in failures(sig(tr,v)) if 7<=1+a+h[v]<=13) for v in range(1,5)]
 for first in product(*choices[:2]):
  for a3 in choices[2]:
   a4=30-a0-sum(first)-a3
   if a4 not in choices[3]:continue
   a=(a0,)+first+(a3,a4)
   d=[1+a[v]+h[v] for v in range(5)]
   if sum(max(x-9,0) for x in d)>4 or d.count(7)>3:continue
   tail_labeled+=1;remaining.add(jointcanon(tr,a))
source=json.loads((P/'RESULT.json').read_text())
expected={jointcanon(tuple(z['traces']),tuple(z['attachments'])) for z in source['tail']}
assert remaining==expected
assert labeled==23751
for row in source['thresholds']:
 ss=[0]*5
 for t in row['types']:ss[0 if t=='P' else 1 if t==0 else t]+=1
 assert list(failures(tuple(ss)))==row['fails']
result={'status':'PASS','method':'Full original 23751 labeled domain, independent count signatures, complementary-binomial event arithmetic and whole(trace,attachment) marked S4 quotient. Primary orbit or threshold routines not imported.','labeled_inputs':labeled,'labeled_tail_assignments':tail_labeled,'joint_tail_orbits':len(remaining),'tail_matches_primary':True,'all70_threshold_failure_sets_match':True,'cpu_seconds':time.process_time()-st}
(P/'INDEPENDENT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
