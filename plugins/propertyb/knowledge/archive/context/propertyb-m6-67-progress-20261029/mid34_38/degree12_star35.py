exec(open(__file__.replace('degree12_star35.py','four_repair.py')).read().split('start=time.process_time()')[0])
exec(open(__file__.replace('degree12_star35.py','repair35_finalquota.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[]
for e in (11,12):
 ds=(10,e,12,12);target=[1,1,1,3,3,3]
 for blocks in parts(tuple(target)):
  ell={}
  for b in blocks:ell[b]=ell.get(b,0)+1
  for j,d in enumerate(ds):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
  ell[0]=66-sum(ell.values())
  if min(ell.values())<0:continue
  best=None
  for order in itertools.permutations(range(4)):
   for shift in (0,-1,1,-2,2,-3,3):
    center=tuple(range(15+shift,19+shift));pos=tuple(center[order.index(j)] for j in range(4));u=c.profile_bound(35,pos,ell)
    if best is None or u<best[0]:best=(u,pos)
    if u<1:break
   if best[0]<1:break
  row=dict(v=35,degrees=ds,blocks=blocks,U=str(best[0]),positions=best[1],strict=best[0]<1);rows.append(row)
  if not row['strict']:print('FAIL',row,flush=True)
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'DEGREE12_STAR35.json').write_text(json.dumps(out,indent=2));print('rows',len(rows),'fails',len(out['failures']),'CPU',out['cpu_seconds'])
