import itertools,json,time
from verify import *
start=time.process_time();rows=[];evals=0
for ds in itertools.combinations_with_replacement(range(8,13),3):
 for tri in (0,1):
  row=dict(v=37,kind='three',degrees=list(ds),tri=tri,positions=[17,18,19]);best=None;bp=None;bd=None
  for order in sorted(set(itertools.permutations(ds))):
   u=bound(row,(17,18,19),order);evals+=1
   if best is None or u<best:best,bp,bd=u,[17,18,19],order
  if best>=1:
   for pos in itertools.combinations(range(15,22),3):
    for order in sorted(set(itertools.permutations(ds))):
     u=bound(row,pos,order);evals+=1
     if u<best:best,bp,bd=u,pos,order
  rows.append(row|dict(U=str(best),approx=float(best),strict=best<1,best_positions=bp,ordered_degrees=bd))
result=dict(scope='all nondecreasing triples from 8..12, both patterns; all degree orders at positions17,18,19, then center+-3 positions only if necessary',profiles=len(rows),evaluations=evals,passed=sum(r['strict'] for r in rows),remaining=sum(not r['strict'] for r in rows),cpu_seconds=time.process_time()-start,rows=rows)
(OUT/'V37_THREE.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2));print('FAIL',*[r for r in rows if not r['strict']],sep='\n');print('WORST',max(rows,key=lambda r:r['approx']))
