"""One exact rerooting/position transport, no search or added vertex.
Minimum-empty residual2912 is the same nine-point inventory as covered3007
when I is privately exchanged and the old partner becomes an outside point.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent;d=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());f=next(z for z in d['results'] if z['base']==19 and z['partner']==4);a=f['cases'][2912];b=f['cases'][3007];ns={int(t):n for t,n in a['counts'].items()};target={int(t):n for t,n in b['counts'].items()};m=[5,6,2,3,7,0,1,4,8];assert sorted(m)==list(range(9))
transformed={sum(1<<m[i] for i in range(9) if t>>i&1):n for t,n in ns.items()};assert transformed==target
pos=[20,21,11,15,22,23,24,12,25]
pilot=json.loads((P/'A7_MINIMUM_EMPTY_PILOT.json').read_text())
assert any(z['positions']==pos for z in pilot['results'])
old=[pos[m[i]] for i in range(9)]
out=dict(scope=__doc__,passed=True,source_case=2912,target_case=3007,old_to_new=m,target_positions=pos,source_positions=old,target_raw_ABC_bound='38583/40040',point_roles=dict(old_partner=4,new_partner=7,new_first_outside=4,second_outside=8),source_counts=ns,target_counts=target)
(P/'A7_MINIMUM_EMPTY_REROOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(passed=True,map=m,target_positions=pos,source_positions=old),indent=2))
