from kernel import *
start=time.process_time();rows=[]
for row in json.loads((P/'WEAK_FOUR39.json').read_text())['failures']:
 ds=row['degrees'];s=4;ell={}
 for b in row['blocks']:ell[b]=ell.get(b,0)+1
 for j,d in enumerate(ds):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
 ell[0]=66-sum(ell.values());best=(F(row['U']),row['positions'])
 double=row['double'];middles=[j for j in range(3) if j!=double]
 for order in ((double,*middles,3),(3,*middles,double)):
  for shift in range(-3,4):
   center=tuple(range(17+shift,21+shift));pos=tuple(center[order.index(j)] for j in range(4));u=c.profile_bound(39,pos,ell)
   if u<best[0]:best=(u,pos)
   if u<1:break
  if best[0]<1:break
 rows.append(dict(**{k:v for k,v in row.items() if k not in ('U','strict','positions')},U=str(best[0]),strict=best[0]<1,positions=best[1]))
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'WEAK_REPAIR39.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'],'rows',len(rows),'fails',len(out['failures']));print(out['failures'])
