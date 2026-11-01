"""Independent fixed certificate replay; no position search, DP, SciPy, or external models."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle/twenty_remaining'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'computations')]
from audit_core import verify
import verify_joint_layout as verifier

def check35(ns,s,v,expected_degrees=None):
 assert v==20 and sum(ns.values())==35 and all(t.bit_count()<=5 and n>=0 for t,n in ns.items())
 assert len(expected_degrees)==s and all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(expected_degrees))
 return [frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
verifier.check_profile=check35
start=time.time();cpu=time.process_time();out=[]
for filename in ['EIGHT_FIVE_DP.json']:
 records=json.loads((HERE/filename).read_text())['cases'];vals=[verify(dict(r,quotas=r['certificates'])) for r in records]
 out.append(dict(source=filename,cases=len(vals),strict=sum(v<1 for v in vals),max_strict=str(max((v for v in vals if v<1),default=Q()))));print(out[-1],flush=True)
for source,basefile,s in [('JOINT_EIGHT_FIVE.json','EIGHT_FIVE_DP.json',6)]:
 base=json.loads((HERE/basefile).read_text())['cases'];total=0
 for x in json.loads((HERE/source).read_text())['results']:
  if Q(x.get('bound','2'))>=1:continue
  r=base[x['source_id']];assert {int(t):n for t,n in x['counts'].items() if n}=={int(t):n for t,n in r['counts'].items() if n}
  verifier.verify(x,v=20,s=s,expected_degrees=[7]+r['neighbor_degrees']);total+=1
 out.append(dict(source=source,strict_joint_certificates=total));print(out[-1],flush=True)
result=dict(status='PASS',scope=__doc__,results=out,cpu_seconds=time.process_time()-cpu,wall_seconds=time.time()-start)
(HERE/'REPLAY_EIGHT_FIVE.json').write_text(json.dumps(result,indent=2)+'\n');print(result['wall_seconds'])
