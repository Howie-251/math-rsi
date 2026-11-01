from kernel import *
start=time.process_time();rows=[]
for s,D in ((3,10),(4,11),(5,11)):
 for ds in itertools.combinations_with_replacement(range(8,D+1),s):
  if s>=4 and sum(ds)>10*s:continue
  for blocks in f.clique_partitions(s):
   ell={b:1 for b in blocks}
   for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
   ell[0]=66-sum(ell.values());best=None
   for shift in range(-2,3):
    pos=tuple(range(39//2-s//2+shift,39//2-s//2+s+shift));u=c.profile_bound(39,pos,ell)
    if best is None or u<best[0]:best=(u,pos)
    if u<1:break
   rows.append(dict(v=39,degrees=ds,blocks=blocks,U=str(best[0]),strict=best[0]<1,positions=best[1]))
 out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
 (P/'PROBE39.json').write_text(json.dumps(out,indent=2));rr=[r for r in rows if len(r['degrees'])==s];print(s,'rows',len(rr),'strict',sum(r['strict'] for r in rr),'CPU',out['cpu_seconds'],flush=True)
 if time.process_time()-start>60:break
