"""Four-variable minimal monotone UNSAT kernels, with actual unit-star disjointness."""
from core_pilot import *
from fractions import Fraction
from math import comb
FULL=(1<<16)-1
MASKS=range(1,16)
def antichain(ms):return all(a&b not in (a,b) for a,b in itertools.combinations(ms,2))
FAMS=[tuple(m for m in MASKS if fam>>(m-1)&1) for fam in range(1,1<<15)]
FAMS=[p for p in FAMS if antichain(p)]
POS={t:sum(1<<r for r in range(16) if not r&t) for t in MASKS}
NEG={t:sum(1<<r for r in range(16) if r&t==t) for t in MASKS}
def union(fs,side):
 z=0
 for t in fs:z|=side[t]
 return z
def min_union(fs):
 # In an antichain, singleton traces are disjoint from every other trace.
 # Larger traces can share an outside point only for complementary two-sets.
 large=[t for t in fs if t.bit_count()>=2]
 total=sum(5-t.bit_count() for t in large)
 for a,b in [(3,12),(5,10),(6,9)]:
  if a in large and b in large:total-=3
 return max(total,4 if any(t.bit_count()==1 for t in fs) else 0)
def event(r,b):
 if r>9 or b>10:return Fraction(0)
 return Fraction(comb(19-r-b,9-r),comb(19,9))
def main():
 st=time.time();kernels=[]
 for p in FAMS:
  up=union(p,POS)
  for n in FAMS:
   un=union(n,NEG)
   if up|un!=FULL:continue
   if any(union(tuple(t for t in p if t!=x),POS)|un==FULL for x in p):continue
   if any(union(tuple(t for t in n if t!=x),NEG)|up==FULL for x in n):continue
   kernels.append((p,n,min_union(p),min_union(n)))
 print('antichains',len(FAMS),'minimal kernels',len(kernels),flush=True)
 out=[]
 for index,ns in enumerate(domain('four_cycle')):
  ub=Fraction(0);active=0;single=Fraction(0)
  for p,n,b,r in kernels:
   # Positive clauses arise from all-blue outside, negative from all-red.
   count=1
   for t in set(p)|set(n):
    count*=ns[t]*(ns[t]-1) if t in p and t in n else ns[t]
   if not count:continue
   term=count*event(r,b);ub+=term;active+=1
   if len(p)+len(n)==2:single+=term
  bad0=ns[0]*Fraction(comb(9,5)+comb(10,5),comb(19,5))
  out.append(dict(index=index,counts=ns,empty_bad=str(bad0),core_unsat_union=str(ub),opposite_singleton_union=str(single),total=str(bad0+ub),active_kernels=active))
  print(index,'empty',bad0,'core unsat',ub,'total',bad0+ub,flush=True)
 (HERE/'C4_SIGNED_PILOT.json').write_text(json.dumps(dict(scope=__doc__,elapsed_seconds=time.time()-st,antichains=len(FAMS),kernels=[dict(positive=p,negative=n,min_blue=b,min_red=r) for p,n,b,r in kernels],profiles=out),indent=2)+'\n')
if __name__=='__main__':main()
