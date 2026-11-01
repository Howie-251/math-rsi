"""Bounded actual-budget triple diagnosis for the v22 minimum-six branch."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from joint_layout_lp import Engine,solve_profile,json_value
start=perf_counter();eng=Engine(22,3);out=[]
for ds in [(6,6,6),(6,6,7),(6,7,7)]:
 rows=[]
 for a,b,c in product(range(1,7),repeat=3):
  if min(ds[0],ds[1])<a or min(ds[0],ds[2])<b or min(ds[1],ds[2])<c:continue
  if a+b-2>4*ds[0]-21 or a+c-2>4*ds[1]-21 or b+c-2>4*ds[2]-21:continue
  for t in range(min(a,b,c)+1):
   ns={7:t,3:a-t,5:b-t,6:c-t,1:ds[0]-a-b+t,2:ds[1]-a-c+t,4:ds[2]-b-c+t}
   ns[0]=34-sum(ns.values())
   if min(ns.values())<0:continue
   ns={k:n for k,n in ns.items() if n};r=eng.solve(ns)
   w=dict(graph='-'.join(map(str,ds)),group=len(rows),degrees=ds,codegrees=[a,b,c],common=t,counts=ns,**r)
   if r['bound']>=1:w['joint']=solve_profile(eng,w)
   rows.append(w)
  if perf_counter()-start>110:break
 nbad=sum(r.get('joint',r).get('bound',Q(9))>=1 for r in rows)
 print(ds,'profiles',len(rows),'remaining',nbad,'seconds',perf_counter()-start,flush=True)
 out.append(dict(degrees=ds,complete=perf_counter()-start<=110,profiles=rows,unresolved=nbad))
 (HERE/'TWENTYTWO_SIX_TRIPLES.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=perf_counter()-start,groups=out)),indent=2)+'\n')
 if perf_counter()-start>110:break
