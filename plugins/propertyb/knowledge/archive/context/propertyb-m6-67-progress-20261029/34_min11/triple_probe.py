exec(__import__('pathlib').Path(__file__).with_name('probe.py').read_text().split('start=time.process_time();rows=[]')[0])
start=time.process_time();rows=[]
menus=[(11,12,13),(15,16,17),(16,17,18),(15,16,19),(11,12,19),(11,13,20),(19,20,21),(14,17,20)]
for center in (12,13):
 for lam in range(1,12):
  for tau in (0,1):
   if 10-lam+tau<0:continue
   ell=a.triple((center,11,11),lam,tau);best=None
   for pos in (p for m in menus for p in itertools.permutations(m)):
    val=a.bound(34,pos,ell)
    if best is None or val<best[0]:best=val,pos
    if val<1:break
   rows.append(dict(degrees=[center,11,11],lam=lam,tau=tau,ell=ell,U=str(best[0]),positions=best[1],strict=best[0]<1))
   print(center,lam,tau,str(best[0]),best[0]<1,flush=True)
(HERE/'TRIPLE_PROBE.json').write_text(json.dumps(dict(rows=rows,cpu_seconds=time.process_time()-start),indent=2)+'\n')
