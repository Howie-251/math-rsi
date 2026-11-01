"""Secondary-min-u source: scalar checks only, not H/coloring enumeration."""
from itertools import product
from pathlib import Path
import json

low_rows={}
for u,t in ((0,2),(1,1),(2,0)):
 rows=[]
 for bh in range(t+1):
  for a in range(6):
   if 2*a+bh!=6:
    continue
   if u==0 and a>u+1+t-bh:
    continue
   rows.append([a,bh])
 assert rows==[[3,0]]
 low_rows[f'{u},{t}']=rows
assert 3*(3-1)>2*2  # three unique-blue neighbors each need both N2's
assert 1-(3-1)+1==0<1
assert 2-(3-1)==0<2

capacity=[]
for u,t,kappa in ((0,2,3),(1,1,3),(2,0,2)):
 for c in range(8-u):
  margin=kappa*(1+u+c)-2*c
  assert margin>0
  capacity.append(dict(u=u,N2=t,cut_half=c,each_sink_kappa_lower=kappa,
                       sinks_lower=1+u+c,strict_margin=margin))

# Extras2: if all four multiple-private indices contain h, only two doubles
# can attain four (one triple contributes just three indices).
multiple_shapes=[(3,), (2,2)]
assert sum(multiple_shapes[0])==3 and sum(multiple_shapes[1])==4
assert len(multiple_shapes[1])==2  # two different repeated cross pairs

single_transfer=[]
for u,up,c in product(range(2),repeat=3):
 if u+up+c<=1 and up>=u:
  assert u==0
  single_transfer.append([u,up,c])

out=dict(status='PASS',scope='secondary-min-u local scalar checks only',
         low_sink_possible_local_counts=low_rows,
         capacity_rows=capacity,
         single_N4_secondary_transfer_rows=single_transfer,
         exact_scope='global minblue12, then minimum u among all such sources',
         conclusion='N1+N2>=15; delta_B+2u+c<=15',
         not_claimed_for_every_minblue_source=True,not_a_coloring_proof=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(capacity),'capacity rows; all three equality classes excluded for secondary min-u')
