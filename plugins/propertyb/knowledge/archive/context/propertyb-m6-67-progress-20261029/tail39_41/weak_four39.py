from kernel import *
from functools import lru_cache
pairs=list(itertools.combinations(range(4),2));pidx={p:i for i,p in enumerate(pairs)}
cliques=[]
for size in range(2,5):
 for vs in itertools.combinations(range(4),size):cliques.append((sum(1<<i for i in vs),tuple(pidx[p] for p in itertools.combinations(vs,2))))
@lru_cache(None)
def parts(target,idx=0):
 if not any(target):return ((),)
 out=[]
 for ci in range(idx,len(cliques)):
  mask,es=cliques[ci]
  if all(target[e]>0 for e in es):
   new=list(target)
   for e in es:new[e]-=1
   for tail in parts(tuple(new),ci):out.append((mask,)+tail)
 return tuple(out)
start=time.process_time();rows=[];patterns={}
for ds in itertools.combinations_with_replacement(range(8,11),3):
 t=sum(ds);E=5*t-114;p=36-E//2;D=8+(108-t)//p
 for d4 in range(8,D+1):
  degrees=ds+(d4,)
  for double in (-1,0,1,2):
   target=[1]*6
   if double>=0:target[pidx[(double,3)]]=2
   blockslist=parts(tuple(target));patterns[str(double)]=len(blockslist)
   for blocks in blockslist:
    ell={}
    for b in blocks:ell[b]=ell.get(b,0)+1
    for j,d in enumerate(degrees):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
    ell[0]=66-sum(ell.values());best=None
    for shift in range(-3,4):
     pos=tuple(range(39//2-2+shift,39//2+2+shift));u=c.profile_bound(39,pos,ell)
     if best is None or u<best[0]:best=(u,pos)
     if u<1:break
    rows.append(dict(degrees=degrees,double=double,blocks=blocks,U=str(best[0]),strict=best[0]<1,positions=best[1]))
out=dict(patterns=patterns,rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'WEAK_FOUR39.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'],'rows',len(rows),'fails',len(out['failures']));print(out['failures'][:20])
