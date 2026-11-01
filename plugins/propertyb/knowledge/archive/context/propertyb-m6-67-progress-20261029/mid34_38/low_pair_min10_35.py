exec(open(__file__.replace('low_pair_min10_35.py','repair35_finalquota.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[]
for z in range(11,16):
 ds=(z,10,10)
 for tau in (0,1):
  ell={7:tau,3:1-tau,5:1-tau,6:2-tau}
  for j,d in enumerate(ds):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
  ell[0]=66-sum(ell.values());ell={b:n for b,n in ell.items() if n};best=None;count=0
  for center in [(16,17,18),(17,18,19),(15,16,17),(18,19,20)]+list(itertools.combinations(range(12,24),3)):
   for pos in itertools.permutations(center):
    u=c.profile_bound(35,pos,ell);count+=1
    if best is None or u<best[0]:best=(u,pos)
    if u<1:break
   if best[0]<1:break
  row=dict(v=35,degrees=ds,lam_other=2,tau=tau,ell=ell,positions=best[1],U=str(best[0]),strict=best[0]<1,evaluations=count);rows.append(row);print(row,flush=True)
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'LOW_PAIR_MIN10_35.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
