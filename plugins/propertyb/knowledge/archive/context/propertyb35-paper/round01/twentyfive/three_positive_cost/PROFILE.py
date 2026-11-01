"""Complete small Venn/cost diagnostic, no H or free pivot enumeration.
Exact recursion tests whether negative pairs/triples can block every minimal transversal.
"""
from pathlib import Path
from itertools import product,combinations
from functools import lru_cache
import json,time
P=Path(__file__).resolve().parent;start=time.perf_counter();nodes=0

def cover(triples,slots,t):
 global nodes
 pairs=sorted({p for z in triples for p in combinations(z,2)})
 cov=[sum(1<<i for i,z in enumerate(triples) if set(p)<=set(z)) for p in pairs]
 # Same cost, so a pair with weaker coverage can always be replaced.
 kept=[i for i,c in enumerate(cov) if not any(c!=d and c&d==c or c==d and j<i for j,d in enumerate(cov))]
 pairs=[pairs[i] for i in kept];cov=[cov[i] for i in kept]
 allbits=(1<<len(triples))-1
 @lru_cache(None)
 def rec(bits,s,tt):
  global nodes;nodes+=1
  if bits.bit_count()<=tt:return ()
  if s==0 or tt<0:return None
  gains=sorted(((c&bits).bit_count() for c in cov),reverse=True)
  if bits.bit_count()-sum(gains[:s])>tt:return None
  i=(bits&-bits).bit_length()-1
  for j,c in enumerate(cov):
   if c>>i&1:
    r=rec(bits&~c,s-1,tt)
    if r is not None:return (j,)+r
  # The first surviving triple may instead be its own negative triple.
  r=rec(bits&~(1<<i),s,tt-1)
  if r is not None:return r
  return None
 ans=rec(allbits,slots,t)
 if ans is None:return None
 pp=sorted(set(pairs[j] for j in ans));left=[z for z in triples if not any(set(p)<=set(z) for p in pp)]
 assert len(pp)<=slots and len(left)<=t
 return pp,left

records=[];raw=0;skipped_equal=0;survivors=[]
for n3,n5,n6,n7 in product(range(5),repeat=4):
 c=(4-n3-n5-n7,4-n3-n6-n7,n3,4-n5-n6-n7,n5,n6,n7)
 if min(c)<0 or sum(c)<7:continue
 raw+=1;A=[set() for _ in range(3)];cells=[];counter=0
 for mask,size in enumerate(c,1):
  cell=list(range(counter,counter+size));counter+=size;cells.append(cell)
  for j in range(3):
   if mask>>j&1:A[j].update(cell)
 if any(A[i]==A[j] for i in range(3) for j in range(i)):
  skipped_equal+=1;continue
 # F lies in the positive union; other forbidden vertices never affect repairs.
 for ff in product(range(3),repeat=7):
  q=sum(ff)
  if q>2 or any(z>cap for z,cap in zip(ff,c)):continue
  F=set(x for cell,num in zip(cells,ff) for x in cell[:num]);AA=[z-F for z in A]
  U=sorted(set.union(*AA));minimal=[]
  for size in [1,2,3]:
   for z in combinations(U,size):
    zz=set(z)
    if all(zz&bb for bb in AA) and not any(set(w)<=zz for w in minimal):minimal.append(z)
  singles=[z for z in minimal if len(z)==1];forced=[z for z in minimal if len(z)==2];triples=[z for z in minimal if len(z)==3]
  status='strict_singleton' if singles else 'strict_cost';witness=None
  if not singles:
   p0=len(forced);B1=24-9*q;B2=12-3*q
   for p in range(p0,min(B1//4,B2//2)+1):
    t=min(B1-4*p,B2-2*p)
    r=cover(triples,p-p0,t)
    if r is not None:
     pairs,neg3=r;neg2=forced+pairs
     assert 9*q+4*len(neg2)+len(neg3)<=24 and 3*q+2*len(neg2)+len(neg3)<=12
     assert all(any(set(b)<=set(z) for b in neg2+neg3) for z in minimal)
     status='feasible_relaxation';witness=dict(A=[sorted(z) for z in A],F=sorted(F),negative_pairs=neg2,negative_triples=neg3,n1=q,n2=len(neg2),n3=len(neg3))
     break
  row=dict(cells=c,forbidden_cells=ff,q=q,minimal_counts=[len(singles),len(forced),len(triples)],status=status)
  if witness is not None:row['witness']=witness;survivors.append(row)
  records.append(row)
summary=dict(raw_Venn_families=raw,excluded_equal_positive_families=skipped_equal,marked_cases=len(records),by_q=[dict(q=q,total=sum(z['q']==q for z in records),feasible=sum(z['q']==q and z['status']=='feasible_relaxation' for z in records)) for q in range(3)],recursion_nodes=nodes,elapsed_seconds=time.perf_counter()-start)
(P/'PROFILE.json').write_text(json.dumps(dict(summary=summary,records=records),indent=2)+'\n');print(json.dumps(summary,indent=2));print('first witness',json.dumps(survivors[:1],indent=2))
