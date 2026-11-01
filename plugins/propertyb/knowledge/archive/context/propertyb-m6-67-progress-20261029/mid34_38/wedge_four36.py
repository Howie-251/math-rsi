exec(open(__file__.replace('wedge_four36.py','four_repair.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[]
for tau,known in ((0,[3,5,6,6]),(1,[6,7])):
 for double in (-1,0,1,2):
  target=[1]*6;target[pidx[(1,2)]]=2
  if double>=0:target[pidx[(double,3)]]=2
  for blocks in parts(tuple(target)):
   if sorted(b&7 for b in blocks if (b&7).bit_count()>=2)!=known:continue
   ell={}
   for b in blocks:ell[b]=ell.get(b,0)+1
   for j in range(4):ell[1<<j]=11-sum(n for b,n in ell.items() if b&(1<<j))
   ell[0]=66-sum(ell.values());best=None
   orders=[(1,0,3,2),(2,0,3,1)]+list(itertools.permutations(range(4)))
   for order in orders:
    for shift in (0,-1,1,-2,2,-3,3):
     center=tuple(range(16+shift,20+shift));pos=tuple(center[order.index(j)] for j in range(4));u=c.profile_bound(36,pos,ell)
     if best is None or u<best[0]:best=(u,pos)
     if u<1:break
    if best[0]<1:break
   rows.append(dict(v=36,degrees=[11]*4,parent_tau=tau,double=double,blocks=blocks,U=str(best[0]),strict=best[0]<1,positions=best[1]));
   if not rows[-1]['strict']:print('FAIL',rows[-1],flush=True)
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'WEDGE_FOUR36.json').write_text(json.dumps(out,indent=2));print('rows',len(rows),'failures',len(out['failures']),'CPU',out['cpu_seconds'])
