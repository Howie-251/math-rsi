import importlib.util,json,time,itertools
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
spec=importlib.util.spec_from_file_location('f',ROOT/'context/propertyb-m6-66-20261029/pilot/FOUR.py');f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f);c=f.c;c.M=66
start=time.process_time();patterns=f.clique_partitions(5);rows=[]
for v in (41,):
 for ds in itertools.combinations_with_replacement(range(8,11),5):
  for blocks in patterns:
   ell={b:1 for b in blocks}
   for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
   ell[0]=66-sum(ell.values());assert min(ell.values())>=0
   best=None
   for shift in range(-3,4):
    pos=tuple(range(v//2-2+shift,v//2+3+shift));u=c.profile_bound(v,pos,ell)
    if best is None or u<best[0]:best=(u,pos)
    if u<1:break
   rows.append(dict(v=v,degrees=ds,blocks=blocks,U=str(best[0]),strict=best[0]<1,positions=best[1]))
out=dict(patterns=len(patterns),rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'FIVE41.json').write_text(json.dumps(out,indent=2));print('patterns',len(patterns),'CPU',out['cpu_seconds'],'rows',len(rows),'fails',len(out['failures']));print(out['failures'])
