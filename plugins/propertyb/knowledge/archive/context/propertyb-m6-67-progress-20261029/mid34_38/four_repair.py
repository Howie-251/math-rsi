exec((__import__('pathlib').Path(__file__).resolve().parent.parent/'tail39_41/kernel.py').read_text())
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
start=time.process_time();rows=[];coverage=[];stopped=False
A=json.loads((P/'ADAPTIVE_COMPONENT.json').read_text())
failures=[r for b in A['branches'] for r in b.get('failures',[])]
for v in (38,37):
 for row in [r for r in failures if r['v']==v]:
  ds=tuple(row['degrees']);delta=ds[0];t=sum(ds);E=5*t-3*(v-1);pool=v-3-E//2;D=delta+(396-t-(v-3)*delta)//pool
  case=dict(v=v,degrees=ds,oldblocks=row['blocks'],pool=pool,D=D,rows=0,failures=0,complete=True)
  # Preserve the known triple trace by retaining only clique multisets inducing it.
  known=sorted(row['blocks'])
  for d4 in range(delta,D+1):
   degrees=ds+(d4,)
   for double in (-1,0,1,2):
    target=[1]*6
    if double>=0:target[pidx[(double,3)]]=2
    for blocks in parts(tuple(target)):
     restriction=sorted(b&7 for b in blocks if (b&7).bit_count()>=2)
     if restriction!=known:continue
     ell={}
     for b in blocks:ell[b]=ell.get(b,0)+1
     for j,d in enumerate(degrees):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
     ell[0]=66-sum(ell.values());best=None
     if double>=0:
      mid=[j for j in range(3) if j!=double]
      orders=[(double,*mid,3),(3,*mid,double),(double,*mid[::-1],3),(3,*mid[::-1],double),(0,1,2,3)]
     else:orders=[(0,1,2,3),(3,0,1,2),(0,3,1,2)]
     for order in orders:
      for shift in (0,-1,1,-2,2,-3,3):
       center=tuple(range(v//2-2+shift,v//2+2+shift));pos=tuple(center[order.index(j)] for j in range(4));u=c.profile_bound(v,pos,ell)
       if best is None or u<best[0]:best=(u,pos)
       if u<1:break
      if best[0]<1:break
     rows.append(dict(v=v,parent_degrees=ds,parent_blocks=row['blocks'],degrees=degrees,double=double,blocks=blocks,U=str(best[0]),strict=best[0]<1,positions=best[1]));case['rows']+=1;case['failures']+=best[0]>=1
     if time.process_time()-start>65:case['complete']=False;stopped=True;break
    if stopped:break
   if stopped:break
  coverage.append(case);print(case,flush=True)
  if stopped:break
 if stopped:break
out=dict(rows=rows,coverage=coverage,complete=not stopped,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'FOUR_REPAIR.json').write_text(json.dumps(out,indent=2));print('rows',len(rows),'failures',len(out['failures']),'CPU',out['cpu_seconds'])
