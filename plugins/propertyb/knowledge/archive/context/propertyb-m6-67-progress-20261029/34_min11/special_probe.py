exec(__import__('pathlib').Path(__file__).with_name('probe.py').read_text().split('start=time.process_time();rows=[]')[0])
from math import comb

def delete(v,slots,ell,j):
 types=[t for t in ell if t>>j&1];cells=[]
 for ai,t in enumerate(types):
  for u in types[ai:]:
   cap=comb(ell[t],2) if t==u else ell[t]*ell[u]
   if cap:cells.append((a.prob(v,slots,slots[j],t,u)+a.prob(v,slots,slots[j],u,t),cap,t|u))
 vals=[]
 for R in range(1<<len(slots)):
  if R>>j&1:continue
  f=sum(n for t,n in ell.items() if t>>j&1 and not t&R)
  need=a.quota(f,v-1-R.bit_count());val=Q(0)
  for w,cap,union in sorted(cells):
   if not union&R:
    z=min(cap,need);need-=z;val+=w*z
  assert not need
  vals.append(val)
 return max(vals)

a.deletion=delete
start=time.process_time();rows=[]
for center,lam in ((12,2),(12,3),(13,2)):
 for tau in (0,1):
  ell=a.triple((center,11,11),lam,tau);best=None
  for menu in [(11,12,13),(15,16,17),(16,17,18),(15,16,19),(11,12,19),(11,13,20),(19,20,21),(14,17,20)]:
   for pos in itertools.permutations(menu):
    value=a.bound(34,pos,ell)
    if best is None or value<best[0]:best=value,pos
    if value<1:break
   if best[0]<1:break
  rows.append(dict(kind='three',degrees=[center,11,11],lam=lam,tau=tau,ell=ell,U=str(best[0]),positions=best[1],strict=best[0]<1));print(rows[-1],flush=True)
for tau in range(4):
 ell={7:tau,3:3-tau,5:3-tau,6:3-tau,9:1,10:1,12:1,1:4+tau,2:4+tau,4:4+tau,8:9};ell[0]=66-sum(ell.values());ell={t:n for t,n in ell.items() if n};best=None
 for menu in [(14,15,16,17),(15,16,17,18),(16,17,18,19),(11,12,13,14),(11,12,19,20),(10,13,18,21)]:
  for pos in itertools.permutations(menu):
   value=a.bound(34,pos,ell)
   if best is None or value<best[0]:best=value,pos
   if value<1:break
  if best[0]<1:break
 rows.append(dict(kind='special_four',tau=tau,ell=ell,U=str(best[0]),positions=best[1],strict=best[0]<1));print(rows[-1],flush=True)
(HERE/'SPECIAL_PROBE.json').write_text(json.dumps(dict(rows=rows,cpu_seconds=time.process_time()-start),indent=2)+'\n')
