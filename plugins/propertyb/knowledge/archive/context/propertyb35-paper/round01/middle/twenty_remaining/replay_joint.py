"""Independent exact M35 shared-slot dual replay; no SciPy or layout search.
Reuses independent injection verifier with an explicit35-edge profile contract.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'computations')]
import verify_joint_layout as verifier

def check35(ns,s,v,expected_degrees=None):
 assert v==20 and sum(ns.values())==35 and all(t.bit_count()<=5 and n>=0 for t,n in ns.items())
 assert len(expected_degrees)==s and all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(expected_degrees))
 return [frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
verifier.check_profile=check35
start=time.time();out=[]
for source,basefile,s in [('STAR_THREE_JOINT.json','STAR_THREE_REFINED.json',4),('STAR_FOUR_JOINT.json','STAR_FOUR_DP.json',5)]:
 base=json.loads((HERE/basefile).read_text())['cases']
 byid={r.get('source_id',i):r for i,r in enumerate(base)}
 for x in json.loads((HERE/source).read_text())['results']:
  if Q(x.get('bound','2'))>=1:continue
  r=byid[x['source_id']]
  assert {int(t):n for t,n in x['counts'].items() if n}=={int(t):n for t,n in r['counts'].items() if n}
  z=verifier.verify(x,v=20,s=s,expected_degrees=[6]+r['neighbor_degrees']);z.update(source=source,source_id=x['source_id']);out.append(z)
 print(source,'strict',sum(z['source']==source for z in out),flush=True)
result=dict(status='PASS',scope=__doc__,exact_M35_source_binding=True,results=out,elapsed_seconds=time.time()-start)
(HERE/'JOINT_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print('passed',len(out),'seconds',time.time()-start)
