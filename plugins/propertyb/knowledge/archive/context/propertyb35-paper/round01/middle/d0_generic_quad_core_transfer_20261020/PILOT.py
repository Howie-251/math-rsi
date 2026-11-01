"""Exactly four specified6/7/8 quad-core degree vectors, with x-repeat codegrees2."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();jobs=[]
for r in range(4):
 degree=(6,)+(7,)*r+(8,)*(3-r);out=[]
 for a,b,c in product(range(3),repeat=3):
  for t in range(min(a,b,c)+1):
   ns={15:2,1:4,2:degree[1]-2-a-b+t,4:degree[2]-2-a-c+t,8:degree[3]-2-b-c+t,6:a-t,10:b-t,12:c-t,14:t,0:35-sum(degree[1:])+a+b+c-t}
   assert min(ns.values())>=0 and sum(ns.values())==35
   e=SubsetEngine(21,4,ns);z=e.verify(e.solve())
   out.append({'parameters':[a,b,c,t],'counts':ns,'degrees':degree,'positions':z['positions'],'bound':z['bound'],'certificates':z['certificates'],'rows':z['rows'],'strict':z['bound']<1})
 jobs.append({'r':r,'degree':degree,'complete_keys':[[q['counts'].get(m,0) for m in range(16)] for q in out],'cases':out,'nonstrict':[i for i,z in enumerate(out) if not z['strict']],'maximum_bound':max(z['bound'] for z in out)})
 print(r,degree,len(out),str(jobs[-1]['maximum_bound']),jobs[-1]['nonstrict'],flush=True)
 assert time.process_time()-st<30
result={'scope':__doc__,'jobs':jobs,'complete':True,'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print('CPU',result['cpu_seconds'])
