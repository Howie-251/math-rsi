from diagnose import *
def partitions(seq):
 if not seq:yield [];return
 x,*tail=seq
 for p in partitions(tail):
  yield [{x},*p]
  for i in range(len(p)):yield [*p[:i],p[i]|{x},*p[i+1:]]
def ell_for(part,tau):
 ell={}
 for block in part:
  T=1+sum(1<<i for i in block);ell[T]=1
 for i,j in itertools.combinations((1,2,3),2):
  used=any(i in B and j in B for B in part);ell[(1<<i)|(1<<j)]=3-used-tau
 ell[14]=tau
 for i,d in enumerate((9,14,14,14)):
  ell[1<<i]=d-sum(n for T,n in ell.items() if T&(1<<i))
 ell[0]=66-sum(ell.values());assert min(ell.values())>=0
 return {T:n for T,n in ell.items() if n}
if __name__=='__main__':
 rows=[];start=time.process_time()
 for part in partitions([1,2,3]):
  upper=min(3-any(i in B and j in B for B in part) for i,j in itertools.combinations((1,2,3),2))
  for tau in range(upper+1):
   ell=ell_for(part,tau);best=None
   for p in ((18,19,20,21),(17,18,19,20),(16,17,18,19),(15,16,17,18),(13,14,15,16),(11,12,13,14),(18,19,20,22),(12,13,18,19)):
    U=c.profile_bound(33,p,ell)
    if best is None or U<best[0]:best=(U,p)
   row=dict(partition=[sorted(B) for B in part],tau=tau,ell=ell,U=str(best[0]),positions=best[1],strict=best[0]<1);rows.append(row)
   print(row,flush=True)
 out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
 Path(__file__).with_name('FOUR.json').write_text(json.dumps(out,indent=2))
