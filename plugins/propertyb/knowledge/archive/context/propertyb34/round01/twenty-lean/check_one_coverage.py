from pathlib import Path
from itertools import product,permutations
import json
B=Path(__file__).resolve().parent
Q=json.loads((B/'ONE_QUAD_DATA.json').read_text());T=json.loads((B/'REMAINING_TRIPLE_DATA.json').read_text())
quads={(tuple(d['co']),tuple(d['high'])) for d in Q}
triples={(d['high'],d['a'],d['b'],d['c'],d['t']) for d in T}
pairs=[3,5,9,6,10,12];high=[7,11,13,14,15]
P=[]
for p0 in permutations((1,2,3)):
 p=(0,)+p0
 tr=lambda m:sum(1<<p[j] for j in range(4) if m>>j&1)
 P.append(([pairs.index(tr(m)) for m in pairs],[high.index(tr(m)) for m in high]))
out={'complete_local_domain':0,'weak_residue':0,'triple':0,'quad':0}
for c in product((1,2),repeat=6):
 for h in product(range(3),repeat=5):
  budgets=(h[0]+h[1]+h[4],h[0]+h[2]+h[4],h[1]+h[2]+h[4],h[0]+h[3]+h[4],h[1]+h[3]+h[4],h[2]+h[3]+h[4])
  if any(x>y for x,y in zip(budgets,c)):continue
  out['complete_local_domain']+=1
  if h[4]==0 and sum(c[:3])!=4 and (c[:3]!=(1,1,1) or h==(0,)*5):out['weak_residue']+=1;continue
  ts=[(True,c[0],c[1],c[3],h[0]+h[4]),(True,c[0],c[2],c[4],h[1]+h[4]),(True,c[1],c[2],c[5],h[2]+h[4]),(False,c[3],c[4],c[5],h[3]+h[4])]
  if any(x in triples for x in ts):out['triple']+=1;continue
  assert any((tuple(c[j] for j in pc),tuple(h[j] for j in ph)) in quads for pc,ph in P),(c,h)
  out['quad']+=1
assert out['complete_local_domain']==674
out['scope']='Independent local-domain and weak-residue coverage, without numerical witness replay';out['status']='PASS'
(B/'ONE_COVERAGE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
