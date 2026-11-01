from pathlib import Path
from fractions import Fraction as F
import sys,json,time
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[4]/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();out=[]
for d1,d2,c in ((6,9,5),(10,12,5),(11,11,5)):
 ns={0:35-d1-d2+c,1:d1-c,2:d2-c,3:c}
 types=[frozenset(i+1 for i in range(2) if m>>i&1) for m in range(4) for _ in range(ns[m])]
 positions=[(10,21),(21,10)] if d1==6 else [(9,21),(21,9),(11,21),(21,11),(10,20),(20,10)]
 layouts=[]
 for pos in positions:
  rows=independent_rows(21,pos,types);v=sum((r['bound'] for r in rows),F(0))
  layouts.append({'positions':pos,'bound':str(v),'strict':v<1,
    'rows':[{k:str(w) if isinstance(w,F) else w for k,w in r.items()} for r in rows]})
 z=min(layouts,key=lambda z:F(z['bound']))
 out.append({'degrees':[d1,d2],'codegree':c,'counts':ns,'original35_trace_masks':[sum(1<<(i-1) for i in t) for t in types],
             'layouts':layouts,'strict':z['strict'],'best_positions':z['positions'],'best_bound':z['bound']})
result={'scope':'zero quota fixed injections only; three justified alternate layouts for two actual possible lambda5 boundaries',
        'cases':out,'cpu_seconds':time.process_time()-st}
(P/'REFINE.json').write_text(json.dumps(result,indent=2)+'\n')
print([(r['degrees'],r['codegree'],r['best_positions'],r['best_bound']) for r in out]);print('CPU',result['cpu_seconds'])
