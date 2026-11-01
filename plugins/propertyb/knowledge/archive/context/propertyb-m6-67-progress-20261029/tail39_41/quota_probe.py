exec(open(__file__.replace('quota_probe.py','five41.py')).read().split('start=time.process_time()')[0])
from fractions import Fraction as F
orig=c.bad_pair_deletion

def deletion(v,pos,ell,j):
 bit=1<<j;other=((1<<len(pos))-1)^bit;typ=[T for T,n in ell.items() if n and T&bit];best=orig(v,pos,ell,j)
 cells=[]
 for ai,T in enumerate(typ):
  for U in typ[ai:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T|U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 for R in range(1<<len(pos)):
  if R&~other:continue
  d=sum(n for T,n in ell.items() if T&bit and not T&R);q=max(0,c.ceilings(5*d-(v-1-R.bit_count()),4));cost=F(0)
  for _,cap,w in sorted((cell for cell in cells if not cell[0]&R),key=lambda z:z[2]):
   take=min(q,cap);cost+=take*w;q-=take
  assert q==0
  best=max(best,cost)
 return best
c.bad_pair_deletion=deletion
rows=[];start=time.process_time()
for file in ('FIVE41.json',str(ROOT/'context/propertyb-m6-67-diagnosis-20261029/pilot/TAIL_LAYOUT_REPAIR.json')):
 for row in json.loads((P/file).read_text())['failures']:
  v=row['v']
  if v not in (40,41):continue
  ds=row['degrees'];blocks=row['blocks'];s=len(ds);ell={b:1 for b in blocks}
  for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
  ell[0]=66-sum(ell.values());best=None
  for shift in range(-4,4):
   pos=tuple(range(v//2-s//2+shift,v//2-s//2+s+shift));u=c.profile_bound(v,pos,ell)
   if best is None or u<best[0]:best=(u,pos)
   if u<1:break
  rows.append(dict(v=v,degrees=ds,blocks=blocks,U=str(best[0]),strict=best[0]<1,positions=best[1]))
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'QUOTA_PROBE.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'],'rows',len(rows),'fails',len(out['failures']));print(out['failures'])
