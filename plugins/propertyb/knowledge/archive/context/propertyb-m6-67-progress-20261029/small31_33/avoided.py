from diagnose import *
@lru_cache(None)
def choices(v,els,j):
 ell=dict(els);bit=1<<j;other=7^bit;typ=[T for T,n in els if n and T&bit];cells=[]
 for i,T in enumerate(typ):
  for U in typ[i:]:
   cap=comb(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T,U,cap))
 core=next(x for x in cells if x[:2]==(bit,bit));rest=[x for x in cells if x!=core]
 qs=[]
 for R in range(8):
  if R&~other:continue
  f=sum(n for T,n in els if T&bit and not T&R)
  qs.append((R,quota(v-R.bit_count(),f)))
 sols=[]
 for zs in itertools.product(*(range(x[2]+1) for x in rest)):
  zcore=max([0]+[q-sum(z for z,(T,U,cap) in zip(zs,rest) if not (T|U)&R) for R,q in qs])
  if zcore<=core[2]:sols.append((zcore,*zs))
 return (core,*rest),tuple(sols)
def avoid_delete(v,pos,ell,j):
 cells,sols=choices(v,tuple(sorted(ell.items())),j)
 ws=[c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T) for T,U,cap in cells]
 return min(sum(z*w for z,w in zip(sol,ws)) for sol in sols)
def triple(ds,l,t):
 d,e,f=ds;ell={7:t,3:1-t,5:1-t,6:l-t,1:d-2+t,2:e-1-l+t,4:f-1-l+t};ell[0]=66-sum(ell.values());return {T:n for T,n in ell.items() if n}
if __name__=='__main__':
 c.bad_pair_deletion=avoid_delete
 for d in (9,10,11):
  for t in(0,1):
   ell=triple((d,14,14),3,t);best=None
   for p in ((19,20,21),(11,12,13),(15,16,19),(16,17,18),(11,12,19)):
    u=c.profile_bound(33,p,ell)
    if best is None or u<best[0]:best=(u,p)
   print(d,t,best,flush=True)
