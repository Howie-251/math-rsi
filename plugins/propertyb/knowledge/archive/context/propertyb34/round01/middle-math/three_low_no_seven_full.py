"""v22 exactly three sixes/no sevens: two common-unit degree-eight neighbors."""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction as Q
from time import perf_counter
import sys,json
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'high-math'))
from subset_position_dp import SubsetEngine
from extend_low import extensions,project
from mixed_low import canon
from joint_layout_lp import solve_profile,Engine,json_value
from verify_joint_layout import verify
start=perf_counter();source=json.loads((HERE/'MIXED_LOW_22.json').read_text())
bad=[r for r in source['results'] if Q(r['final_bound'])>=1];badkeys={canon({int(t):n for t,n in r['counts'].items()},3) for r in bad};groups={};raw=0;filtered=0
def can5(ns):
 return min(tuple(sorted((sum(1<<p[i] for i in range(5) if t&(1<<i)),n) for t,n in ns.items())) for pl in permutations(range(3)) for ph in [(3,4),(4,3)] for p in [pl+ph])
for w in bad:
 ns={int(t):n for t,n in w['counts'].items()}
 for out in extensions(ns,4,22,new_degree=8,max_extra=7,old_degrees=[6,6,6,8]):
  if any(sum(n for t,n in out.items() if t&(1<<i) and t&16)!=1 for i in range(3)):continue
  raw+=1
  if canon(project(out,[0,1,2,4]),3) not in badkeys:continue
  filtered+=1;key=can5(out)
  if key not in groups:groups[key]=len(groups)
print('raw',raw,'filtered',filtered,'groups',len(groups),flush=True);rows=[];eng=Engine(22,5)
for key,gid in groups.items():
 ns=dict(key);sub=SubsetEngine(22,5,ns);r=sub.solve();w=dict(r,graph='three6-two8',group=gid,counts=ns)
 if r['bound']>=1:
  w['joint']=solve_profile(eng,w);w['final_bound']=w['joint'].get('bound',9)
  if Q(w['final_bound'])<1:w['independent']=verify(w['joint'],22,5,[6,6,6,8,8])
 else:sub.verify(r);w['final_bound']=r['bound'];w['independent_ABC']=True
 rows.append(w);print(gid,w['final_bound'],flush=True)
(HERE/'THREE_LOW_NO_SEVEN_FULL_22.json').write_text(json.dumps(json_value(dict(scope=__doc__,raw=raw,filtered=filtered,groups=len(groups),complete=True,results=rows,elapsed_seconds=perf_counter()-start)),indent=2)+'\n')
