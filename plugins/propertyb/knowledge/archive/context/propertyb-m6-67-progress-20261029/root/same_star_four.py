exec(open(__file__.replace('same_star_four.py','pairs_probe.py')).read().split('start=time.process_time()')[0])
from fractions import Fraction
# Use each avoided quota individually against the same actual cell vector.
def mxdelete(v,pos,ell,j):
 bit=1<<j;typ=[T for T,n in ell.items() if n and T&bit];cells=[]
 for i,T in enumerate(typ):
  for U in typ[i:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T|U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 best=Fraction(0)
 for R in range(1<<len(pos)):
  if R&bit:continue
  f=sum(n for T,n in ell.items() if T&bit and not T&R);q=d.quota(v-R.bit_count(),f);cost=Fraction(0)
  for union,cap,w in sorted((a for a in cells if not a[0]&R),key=lambda a:a[2]):
   use=min(q,cap);cost+=use*w;q-=use
  assert q==0
  best=max(best,cost)
 return best
c.bad_pair_deletion=mxdelete
start=time.process_time();rows=[]
for ls in itertools.product((2,3),repeat=3):
 for tau in range(min(ls)+1):
  ell={3:1,5:1,9:1,6:ls[0]-tau,10:ls[1]-tau,12:ls[2]-tau,14:tau}
  for j,deg in enumerate((9,12,12,12)):ell[1<<j]=deg-sum(n for T,n in ell.items() if T&(1<<j))
  ell[0]=66-sum(ell.values());best=None
  for pos in [(16,17,18,19),(15,16,17,18),(17,18,19,20),(12,13,19,20),(11,12,19,20),(12,13,14,15)]:
   for order in itertools.permutations(range(4)):
    ps=tuple(pos[order.index(j)] for j in range(4));u=c.profile_bound(35,ps,ell)
    if best is None or u<best[0]:best=(u,ps)
    if u<1:break
   if best[0]<1:break
  row=dict(ls=ls,tau=tau,ell=ell,pos=best[1],U=str(best[0]),strict=best[0]<1);rows.append(row)
  if not row['strict']:print('FAIL',ls,tau,row['U'],flush=True)
out=dict(rows=rows,cpu_seconds=time.process_time()-start,strict=all(r['strict'] for r in rows))
(P/'SAME_STAR_FOUR.json').write_text(json.dumps(out,indent=2));print('TOTAL',len(rows),'strict',out['strict'],'CPU',out['cpu_seconds'])
