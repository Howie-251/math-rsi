"""Small exact triple profiles on 22/23 vertices; actual selection still required."""
from pathlib import Path
import runpy,itertools,json,time
ns=runpy.run_path(str(Path(__file__).with_name('middle_diagnostic.py')))
Profile,rows,total_bound,certificate,json_value=[ns[k] for k in ['Profile','rows','total_bound','certificate','json_value']]
start=time.perf_counter();data=[]
for v in (22,23):
 for a,b,c in itertools.combinations_with_replacement(range(1,4 if v==22 else 5),3):
  for t in range(min(a,b,c)+1):
   counts={0:13+a+b+c-t,1:7-a-b+t,2:7-a-c+t,4:7-b-c+t,3:a-t,5:b-t,6:c-t,7:t}
   if min(counts.values())<0:continue
   best=None
   for pp in [tuple(range(k,k+3)) for k in range(7,15)]+[(1,11,13),(1,12,14)]:
    for pos in itertools.permutations(pp):
     p=Profile(v,5,pos,counts);cs=[certificate(p,i) for i in range(3)]
     rr=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(3)})
     u=total_bound(rr)
     if best is None or u<best['bound']:best=dict(v=v,pairs=(a,b,c),triple=t,counts=counts,positions=pos,bound=u,certificates=cs,rows=rr)
   data.append(best);print(v,(a,b,c),t,best['positions'],best['bound'],flush=True)
Path(__file__).with_name('MIDDLE_TRIPLE_RESULTS.json').write_text(json.dumps(json_value(dict(elapsed_seconds=time.perf_counter()-start,cases=data)),indent=2)+'\n')
