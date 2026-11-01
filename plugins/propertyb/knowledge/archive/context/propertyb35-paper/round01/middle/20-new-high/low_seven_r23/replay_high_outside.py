from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE))
from replay_r3 import fixed,joint
start=time.time();d=json.loads((HERE/'HIGH_OUTSIDE_PILOT.json').read_text());count=0
for r in d['pairs']+d['triples']:
 val=fixed(r);strict=val<1
 if not strict and r.get('joint') and Q(r['joint'].get('bound','2'))<1:
  joint.verify(r['joint'],v=20,s=3,expected_degrees=r['degrees']);strict=True
 assert strict==r['strict'];count+=1
supplement=json.loads((HERE/'C2_HIGH_UNIT_16_19.json').read_text())['cases']
for r in supplement:assert fixed(r)==Q(r['bound'])<1
result=dict(unit_high_16_19_fixed_replayed=len(supplement),status='PASS',pairs=len(d['pairs']),triples=len(d['triples']),fixed_candidates_replayed=count,strict_pairs=sum(r['strict'] for r in d['pairs']),strict_triples=sum(r['strict'] for r in d['triples']),elapsed_seconds=time.time()-start)
(HERE/'HIGH_OUTSIDE_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
