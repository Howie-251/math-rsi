exec(open(__file__.replace('two_arms35_joint.py','repair35_finalquota.py')).read().split('start=time.process_time()')[0])
src=open(__file__.replace('two_arms35_joint.py','adaptive_component.py')).read();exec(src[src.index('def deletion(v,pos,ell,j):'):src.index('def best(v,ds,blocks):')])
quota=lambda f,N:dp.quota(N+1,f)
start=time.process_time();rows=[]
for r in json.loads((P/'TWO_ARMS35.json').read_text())['failures']:
 ds=r['degrees'];lam=r['lam_yz'];tau=r['tau'];ell={7:tau,3:1-tau,5:1-tau,6:lam-tau}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
 ell[0]=66-sum(ell.values());ell={b:n for b,n in ell.items() if n};best=None
 for center in ((16,17,18),(17,18,19),(15,16,17),(18,19,20),tuple(sorted(r['positions']))):
  for pos in itertools.permutations(center):
   u=bound(35,pos,ell)
   if best is None or u<best[0]:best=(u,pos)
   if u<1:break
  if best[0]<1:break
 rows.append(r|dict(U=str(best[0]),positions=best[1],strict=best[0]<1));print(rows[-1],flush=True)
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'TWO_ARMS35_JOINT.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
