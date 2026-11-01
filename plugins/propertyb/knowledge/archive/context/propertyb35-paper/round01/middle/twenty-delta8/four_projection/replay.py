"""Independent explicit four-point inclusion-exclusion domain plus all fixed/strict-dual replay.
Reads previously checked triple8 certificates only as the necessary residual predicate; no old triple search.
"""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parents[1]/'20-new-high/low_seven_r23'))
from replay_r3 import fixed,joint

def key(ns):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(16))
def main():
 start=time.time();old=json.loads((HERE.parents[1]/'20-new-high/DIAGNOSIS.json').read_text())['triples'];allowed={(tuple(r['codegrees']),r['triple']) for r in old if r['degrees']==[8,8,8] and not r['strict']};assert len(allowed)==21
 pairs=[sum(1<<i for i in S) for S in combinations(range(4),2)];trips=[sum(1<<i for i in S) for S in combinations(range(4),3)];expected=set()
 for cs in product((1,2,3),repeat=6):
  c=dict(zip(pairs,cs))
  for ts in product(range(4),repeat=4):
   t=dict(zip(trips,ts))
   if any((tuple(sorted(c[B] for B in pairs if A&B==B)),t[A]) not in allowed for A in trips):continue
   for q in range(min(ts)+1):
    ns={15:q};ns.update({A:v-q for A,v in t.items()});ns.update({B:v-sum(n for A,n in t.items() if A&B==B)+q for B,v in c.items()})
    for i in range(4):b=1<<i;ns[b]=8-sum(v for B,v in c.items() if B&b)+sum(v for A,v in t.items() if A&b)-q
    ns[0]=3+sum(cs)-sum(ts)+q
    if min(ns.values())>=0:expected.add(key(ns))
 dom=json.loads((HERE/'DOMAIN.json').read_text());assert len(expected)==4878 and expected=={key(r['counts']) for r in dom['labelled']} and len(dom['orbits'])==385
 for r in dom['labelled']:
  ns={int(t):n for t,n in dom['orbits'][r['orbit']]['counts'].items()};p=r['from_representative_permutation'];move=lambda t:sum(1<<p[i] for i in range(4) if t>>i&1)
  assert key({move(t):n for t,n in ns.items()})==key(r['counts'])
 dp=json.loads((HERE/'FOUR_DP.json').read_text());assert dp['complete'] and len(dp['cases'])==385;vals={r['id']:fixed(r) for r in dp['cases']};pure={i for i,v in vals.items() if v<1};js=[]
 for z in json.loads((HERE/'FOUR_JOINT.json').read_text())['results']:
  if Q(z.get('bound','2'))>=1:continue
  verified=joint.verify(z,v=20,s=4,expected_degrees=[8]*4);vals[z['source_id']]=Q(verified['bound']);js.append(z['source_id'])
 remaining={i for i,v in vals.items() if v>=1};assert len(remaining)==44 and remaining=={r['id'] for r in json.loads((HERE/'FOUR_REMAINDERS.json').read_text())['cases']}
 result=dict(status='PASS',scope=__doc__,old_three_residual_predicate=21,independent_labelled_count=4878,true_S4_orbits=385,transport_checks=4878,fixed_strict=len(pure),joint_strict=len(js),remaining_count=44,remaining_ids=sorted(remaining),max_accepted_bound=str(max(v for v in vals.values() if v<1)),elapsed_seconds=time.time()-start)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
