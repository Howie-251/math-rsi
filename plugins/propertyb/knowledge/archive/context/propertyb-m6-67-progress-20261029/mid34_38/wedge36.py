exec((__import__('pathlib').Path(__file__).resolve().parent.parent/'tail39_41/kernel.py').read_text())
start=time.process_time();rows=[]
for lam in (1,2):
 for tau in (0,1):
  ell={7:tau,3:1-tau,5:1-tau,6:lam-tau}
  for j in range(3):ell[1<<j]=11-sum(n for b,n in ell.items() if b&(1<<j))
  ell[0]=66-sum(ell.values());ell={t:n for t,n in ell.items() if n};best=None;count=0
  for pos in itertools.combinations(range(12,25),3):
   for order in ((0,1,2),(1,0,2),(1,2,0)):
    ps=tuple(pos[order.index(j)] for j in range(3));u=c.profile_bound(36,ps,ell);count+=1
    if best is None or u<best[0]:best=(u,ps)
    if u<1:break
   if best[0]<1:break
  rows.append(dict(v=36,degrees=[11,11,11],lam_yz=lam,triple=tau,U=str(best[0]),positions=best[1],strict=best[0]<1,evaluations=count));print(rows[-1],flush=True)
out=dict(rows=rows,complete=True,cpu_seconds=time.process_time()-start)
(P/'WEDGE36.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
