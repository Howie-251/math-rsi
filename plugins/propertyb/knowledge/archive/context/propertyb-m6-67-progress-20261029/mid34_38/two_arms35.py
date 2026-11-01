exec(open(__file__.replace('two_arms35.py','repair35_finalquota.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[]
for e,f in ((11,11),(11,12),(12,12)):
 for lam in range(1,min(e,f)+1):
  for tau in (0,1):
   ell={7:tau,3:1-tau,5:1-tau,6:lam-tau}
   ds=(10,e,f)
   for j,d in enumerate(ds):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
   ell[0]=66-sum(ell.values())
   if min(ell.values())<0:continue
   ell={t:n for t,n in ell.items() if n};best=None;count=0
   for pos in [(16,17,18),(17,18,19),(15,16,17),(18,19,20)]+list(itertools.combinations(range(13,23),3)):
    for order in itertools.permutations(range(3)):
     ps=tuple(pos[order.index(j)] for j in range(3));u=c.profile_bound(35,ps,ell);count+=1
     if best is None or u<best[0]:best=(u,ps)
     if u<1:break
    if best[0]<1:break
   row=dict(v=35,degrees=ds,lam_yz=lam,tau=tau,positions=best[1],U=str(best[0]),strict=best[0]<1,evaluations=count);rows.append(row)
   if not row['strict']:print('FAIL',row,flush=True)
   (P/'TWO_ARMS35.partial.json').write_text(json.dumps(dict(rows=rows,cpu_seconds=time.process_time()-start),indent=2))
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'TWO_ARMS35.json').write_text(json.dumps(out,indent=2));print('rows',len(rows),'fails',len(out['failures']),'CPU',out['cpu_seconds'])
