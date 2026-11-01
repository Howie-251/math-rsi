"""Independent explicit (8,8,9) three-point inclusion-exclusion domain and fixed replay; no search."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parents[2]/'20-new-high/low_seven_r23'))
from replay_r3 import fixed,joint
start=time.time();rs=json.loads((HERE/'GATE.json').read_text())['cases'];expected=set()
for c in range(1,4):
 for a in range(1,5):
  for b in range(a,5):
   if a+b>5:continue
   for t in range(min(c,a,b)+1):expected.add((c,a,b,t))
assert {(tuple(r['codegrees'])+(r['triple'],)) for r in rs}==expected and len(rs)==40
vals={};strict=[]
for r in rs:
 c,a,b=r['codegrees'];t=r['triple'];ns={7:t,3:c-t,5:a-t,6:b-t,1:8-c-a+t,2:8-c-b+t,4:9-a-b+t,0:10+c+a+b-t};assert {k:v for k,v in ns.items() if v}=={int(k):v for k,v in r['counts'].items() if v}
 v=fixed(r)
 if r.get('joint') and Q(r['joint'].get('bound','2'))<1:v=Q(joint.verify(r['joint'],v=20,s=3,expected_degrees=[8,8,9])['bound'])
 assert (v<1)==r['strict'];vals[r['id']]=v
result=dict(status='PASS',scope=__doc__,complete_orbits=40,strict=17,remaining=23,max_strict_bound=str(max(v for v in vals.values() if v<1)),elapsed_seconds=time.time()-start)
(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
