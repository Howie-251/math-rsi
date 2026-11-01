from pilot import *
from independent_structure_bounds import independent_rows
from math import comb
out=[]
for d in (5,6,7):
 z=best(19,{0:35-d,1:d});ns=z['counts'];pos=z['positions'];types=[frozenset({1})]*d+[frozenset()]*(35-d)
 rr=independent_rows(19,tuple(pos),types);loss=z['quotas'][0]['loss'];value=Q()
 for saved,r in zip(z['rows'],rr):
  assert all(Q(saved[k])==r[k] for k in ('A','B','C'))
  val=min(r['A'],r['B'],r['C']-(loss if r['k']==pos[0] else Q()));value+=val
 assert value==z['bound']<1
 out.append(dict(degree=d,position=pos[0],bound=str(value),q=z['quotas'][0]['q_total'],loss=str(loss),expanded_rows_agree=True))
(HERE/'NINETEEN_LOW_REPLAY.json').write_text(json.dumps(dict(status='PASS',scope='M35 v19 degree5/6/7 single-lock exact expanded-edge-stub check',cases=out),indent=2)+'\n')
print(json.dumps(out,indent=2))
