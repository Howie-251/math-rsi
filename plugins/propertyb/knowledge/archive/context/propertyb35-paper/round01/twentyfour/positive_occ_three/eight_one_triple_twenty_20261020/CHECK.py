"""New scalar budgets and exact replay of existing seven/86 representatives only."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent;BASE=HERE.parent
PAIRS=tuple(combinations(range(5),2))

def ie(vector):
 sets=[set() for _ in range(5)];pid=0
 for (a,b),n in zip(PAIRS,vector):
  for _ in range(n):sets[a].add(pid);sets[b].add(pid);pid+=1
 for s in sets:
  while len(s)<4:s.add(pid);pid+=1
 U=set().union(*sets)
 return sum((-1)**m.bit_count()*comb(len(U-set().union(*(sets[i] for i in range(5) if m>>i&1))),4)
            for m in range(32))

seven=json.loads((BASE/'eighteen_one_triple'/'THREE_EDGE_CHECK.json').read_text())
old=json.loads((BASE/'INDEPENDENT_COUNT_REPLAY.json').read_text())
assert seven['orbit_count']==len(seven['results'])==7 and sum(r['orbit_size'] for r in seven['results'])==220
seven_counts=[]
for r in seven['results']:
 c=ie(r['vector']);assert c==r['C4_direct']==r['C4_IE'];seven_counts.append(c)
assert min(seven_counts)==144
assert old['orbits_replayed']==len(old['all_counts'])==86
for r in old['all_counts']:assert ie(r['edge_vector'])==r['C4']
assert min(r['C4'] for r in old['all_counts'])==178
params=[(t,b,u,v) for t in range(2) for b in range(21)
        for u in range(t+1) for v in range(b+1) if u+v<=4]
budgets={
 'E3_C4':max(50*u+14*(t-u+v)+(b-v) for t,b,u,v in params),
 'E_ge4_C4':max(46*u+13*(t-u+v)+(b-v) for t,b,u,v in params),
 'zero_M2_constructed_C4':max(16*u+4*(t-u+v)+(b-v) for t,b,u,v in params),
 'C3':max(4*u+(t-u+v) for t,b,u,v in params),
}
assert budgets==dict(E3_C4=109,E_ge4_C4=102,zero_M2_constructed_C4=45,C3=7)
p=F(7,16);low=p**3+20*p**4
assert low==F(13377,16384)<1
assert 16+20*4==96<256
assert all((4-j)*(1-j)+3-j<(4-j)**2 for j in (0,1))
assert 3<9 and 7<16 and 5<16
out=dict(pass_all=True,low_occurrence_bound=str(low),complete_scalar_parameter_count=len(params),
         blocking_bounds=budgets,imported_existing_seven_C4=seven_counts,old_seven_minimum=144,
         replayed_existing_86_representatives=86,old_86_minimum=178,
         new_graph_domains_generated=False)
(HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
