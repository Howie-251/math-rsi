from pathlib import Path
from fractions import Fraction as F
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();out=[]
for d2 in (10,11):
 for d1 in (7,8,9):
  for c in range(5,d1+1):
   ns={0:35-d1-d2+c,1:d1-c,2:d2-c,3:c}
   types=[frozenset(i+1 for i in range(2) if mask>>i&1) for mask in range(4) for _ in range(ns[mask])]
   assert len(types)==35
   layouts=[]
   for pos in ((10,21),(21,10)):
    rows=independent_rows(21,pos,types);v=sum((r['bound'] for r in rows),F(0))
    z={'positions':pos,'bound':str(v),'strict':v<1}
    if v<1:z['rows']=[{k:str(w) if isinstance(w,F) else w for k,w in r.items()} for r in rows]
    layouts.append(z)
   best=min(layouts,key=lambda z:F(z['bound']))
   out.append({'degrees':[d1,d2],'codegree':c,'counts':ns,'original35_trace_masks':[sum(1<<(i-1) for i in t) for t in types],
               'quota':0,'layouts':layouts,'best_positions':best['positions'],'best_bound':best['bound'],'strict':best['strict']})
j={'scope':'n21/M35/simple5 selected degree pair; no freedom-degree/coverage/A1 assumptions; exact expanded35 zero-quota injection rows',
   'phase':'pilot','inputs':len(out),'layouts':2*len(out),'strict_inputs':sum(r['strict'] for r in out),'cases':out,'cpu_seconds':time.process_time()-st}
(P/'PILOT.json').write_text(json.dumps(j,indent=2)+'\n')
print(json.dumps({k:v for k,v in j.items() if k!='cases'},indent=2))
for d2 in (10,11):
 for d1 in (7,8,9):
  print((d1,d2),[(r['codegree'],r['best_bound']) for r in out if r['degrees']==[d1,d2]])
