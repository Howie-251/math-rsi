"""Complete necessary local domains, M66; max of avoided-subset deletion bounds."""
from kernel import *
start=time.process_time();rows=[]
for v,s in ((40,4),(41,5)):
 for ds in itertools.combinations_with_replacement(range(8,11),s):
  for blocks in f.clique_partitions(s):
   ell={b:1 for b in blocks}
   for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
   ell[0]=66-sum(ell.values());best=None
   for shift in range(-4,4):
    pos=tuple(range(v//2-s//2+shift,v//2-s//2+s+shift));u=c.profile_bound(v,pos,ell)
    if best is None or u<best[0]:best=(u,pos)
    if u<1:break
   excluded=(v==40 and ds==(8,8,8,10) and blocks==(15,)) or (v==41 and blocks==(31,) and sum(ds)<=49)
   rows.append(dict(v=v,degrees=ds,blocks=blocks,ell=ell,U=str(best[0]),strict=best[0]<1,structural_excluded=excluded,positions=best[1]))
 out=dict(M=66,rows=rows,unclosed=[r for r in rows if not r['strict'] and not r['structural_excluded']],cpu_seconds=time.process_time()-start)
 (P/'CERT40_41.json').write_text(json.dumps(out,indent=2));print(v,len([r for r in rows if r['v']==v]),'unclosed',len(out['unclosed']),'CPU',out['cpu_seconds'],flush=True)
assert not out['unclosed']
