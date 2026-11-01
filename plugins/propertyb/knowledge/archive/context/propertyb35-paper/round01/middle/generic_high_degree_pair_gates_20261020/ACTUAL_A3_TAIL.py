from pathlib import Path
from fractions import Fraction as F
import sys,json,time
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[4]/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();out=[]
for dy,dz in ((11,11),):
 for t in (0,1):
  ns={0:14-t,1:4+t,2:dy-6+t,4:dz-6+t,3:1-t,5:1-t,6:5-t,7:t}
  assert sum(ns.values())==35
  assert [sum(n for mask,n in ns.items() if mask>>i&1) for i in range(3)]==[6,dy,dz]
  types=[frozenset(i+1 for i in range(3) if m>>i&1) for m in range(8) for _ in range(ns[m])]
  positions=[(x,1,21) for x in (9,10,11)]+[(x,20,21) for x in (9,10,11,12)]+[(1,y,20) for y in (9,10,11)]+[(1,20,21),(2,20,21),(3,20,21)]
  layouts=[]
  for pos in positions:
   rows=independent_rows(21,pos,types);v=sum((r['bound'] for r in rows),F(0))
   z={'positions':pos,'bound':str(v),'strict':v<1}
   if v<1:z['rows']=[{k:str(w) if isinstance(w,F) else w for k,w in r.items()} for r in rows]
   layouts.append(z)
  z=min(layouts,key=lambda z:F(z['bound']))
  out.append({'degrees':[6,dy,dz],'triple':t,'pair_codegrees':[1,1,5],'counts':ns,
   'original35_trace_masks':[sum(1<<(i-1) for i in ty) for ty in types],
   'quota':0,'layouts':layouts,'strict':z['strict'],'best_positions':z['positions'],'best_bound':z['bound']})
result={'scope':'four actual A3 forced triple inventories; zero quota, explicitly bounded18 layouts each',
        'cases':out,'strict_profiles':sum(r['strict'] for r in out),'cpu_seconds':time.process_time()-st}
(P/'ACTUAL_A3_TAIL.json').write_text(json.dumps(result,indent=2)+'\n')
print([(r['degrees'],r['triple'],r['best_positions'],r['best_bound']) for r in out]);print('CPU',result['cpu_seconds'])
