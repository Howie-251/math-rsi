"""Bounded exact diagnostic on the new 17/18 vertex cases; no full-H search."""
from pathlib import Path
from itertools import combinations
import importlib.util
import json
import time

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('previous_single_lock_diagnostic',
    ROOT/'context/propertyb34-feasibility-20261013/low-vertices/diagnose.py')
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
HERE=Path(__file__).resolve().parent

def double(v,m,d1,d2,codegree,positions):
    counts={0:m-d1-d2+codegree,1:d1-codegree,2:d2-codegree,3:codegree}
    p=old.Profile(v,5,positions,counts)
    certs=[old.certificate(p,i) for i in range(2)]
    rows=old.rows(p,deductions={positions[i]:certs[i]['loss'] for i in range(2)})
    return dict(v=v,m=m,degrees=[d1,d2],codegree=codegree,positions=positions,
                counts=counts,certificates=certs,rows=rows,bound=old.total_bound(rows))

if __name__=='__main__':
    start=time.monotonic(); singles=[]
    for v in (17,18):
      for m in range(35,40):
        for d in range((v+2)//4,5*m//v+1):
          best=min((old.one(v,m,(d,),(k,),'nested_pure') for k in range(1,v+1)),key=lambda x:x['bound'])
          old.check_independent(best);best['all_single_lock_positions_checked']=v;singles.append(best)
    (HERE/'SINGLE_LOCK_DIAGNOSTIC.json').write_text(json.dumps(old.json_value(dict(
        scope='All min degrees permitted by covering/average; all single positions, with total/pure link quotas. Exact ABC independently replayed.',cases=singles)),indent=2)+'\n')
    doubles=[]
    for v,d1,d2 in ((17,10,10),(18,8,8),(18,8,9),(18,9,9)):
      for c in range(1,min(d1,d2)+1):
        best=min((double(v,35,d1,d2,c,pos) for pos in combinations(range(1,v+1),2)),key=lambda x:x['bound'])
        old.check_independent(best);best['all_increasing_positions_checked']=v*(v-1)//2;doubles.append(best)
        print(v,d1,d2,c,str(best['bound']),flush=True)
    (HERE/'TWO_LOCK_DIAGNOSTIC.json').write_text(json.dumps(old.json_value(dict(
        scope='M35 only; specified degree pairs; all positive codegrees and increasing positions. Reflection covers reversed orders. Actual selection proved separately; not whole target proof.',
        elapsed_seconds=time.monotonic()-start,cases=doubles)),indent=2)+'\n')
