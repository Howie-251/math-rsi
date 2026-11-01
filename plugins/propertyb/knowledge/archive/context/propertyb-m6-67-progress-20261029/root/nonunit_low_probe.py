exec(open(__file__.replace('nonunit_low_probe.py','pairs_probe.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[]
def check(v,ds,ls,tau):
 a,b,cc=ls
 ell={7:tau,3:a-tau,5:b-tau,6:cc-tau,1:ds[0]-a-b+tau,2:ds[1]-a-cc+tau,4:ds[2]-b-cc+tau};ell[0]=66-sum(ell.values())
 if min(ell.values())<0:return
 menu=[(16,17,18),(17,18,19),(12,13,14),(11,12,19),(11,13,20),(10,11,19),(15,16,19),(10,16,20)]
 best=None
 for pos in menu:
  for order in itertools.permutations(range(3)):
   ps=tuple(pos[order.index(j)] for j in range(3));u=c.profile_bound(v,ps,ell)
   if best is None or u<best[0]:best=(u,ps)
   if u<1:break
  if best[0]<1:break
 row=dict(v=v,ds=ds,ls=ls,tau=tau,ell=ell,U=str(best[0]),pos=best[1],strict=best[0]<1);rows.append(row)
 if not row['strict']:print('FAIL',ds,ls,tau,row['U'],flush=True)
for lam in range(1,11):
 ell=d.two(34,10,10,lam);best=min((c.profile_bound(34,ps,ell),ps) for ps in [(16,17),(16,19),(12,19),(12,20),(11,20)])
 rows.append(dict(v=34,ds=[10,10],lam=lam,ell=ell,U=str(best[0]),pos=best[1],strict=best[0]<1));print('PAIR',lam,rows[-1]['U'],flush=True)
for lam in range(1,12):
 for tau in range(3):check(34,(10,11,11),(2,2,lam),tau)
out=dict(rows=rows,cpu_seconds=time.process_time()-start)
(P/'NONUNIT_LOW_PROBE.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
