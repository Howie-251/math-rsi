from component_kernel import *
start=time.process_time();rows=[]
for center,a,b in [(12,9,9),(12,9,10),(13,9,10)]:
 for tau in (0,1):
  ell={7:tau,3:1-tau,5:1-tau,6:2-tau,1:center-2+tau,2:a-3+tau,4:b-3+tau};ell[0]=66-sum(ell.values());best=None
  for pos in itertools.combinations(range(11,24),3):
   for order in itertools.permutations(range(3)):
    ps=tuple(pos[order.index(j)] for j in range(3));u=c.profile_bound(35,ps,ell)
    if best is None or u<best[0]:best=(u,ps)
    if u<1:break
   if best[0]<1:break
  row=dict(ds=[center,a,b],tau=tau,ell=ell,U=str(best[0]),pos=best[1],strict=best[0]<1);rows.append(row);print(row,flush=True)
out=dict(rows=rows,cpu_seconds=time.process_time()-start)
(P/'LOW_PAIR_CENTER35.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
