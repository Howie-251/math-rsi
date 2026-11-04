"""Structured and random diagnostics for T15; not exhaustive matchings."""
import itertools,json,random
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rng=random.Random(20261101)
odd=[x for x in range(32) if x.bit_count()%2]
rows=[]
for mode in ('arbitrary','short_greedy','half_layer','same_parity'):
 for trial in range(250):
  f=[]
  if mode=='half_layer':
   j=rng.randrange(5)
   # Choose the half layer that does not contain vertex 0.
   f=[(x,x^(1<<j)) for x in range(32) if not(x>>j&1) and (x&~(1<<j)).bit_count()%2==1]
   blocked={x for e in f for x in e}
   O=rng.sample([x for x in odd if x not in blocked],5)
  else:O=rng.sample(odd,5)
  holes={0,*O};avoid=sorted(rng.sample(O,2));covered=set(range(32))-holes
  remaining=covered-{x for e in f for x in e}
  if mode=='short_greedy':
   possible=[(x,y) for x in remaining for y in remaining if x<y and (x^y).bit_count()==1]
   rng.shuffle(possible)
   for x,y in possible:
    if x in remaining and y in remaining:f.append((x,y));remaining-={x,y}
  if mode=='same_parity':
   for parity in (0,1):
    xs=[x for x in remaining if x.bit_count()%2==parity];rng.shuffle(xs)
    for i in range(0,len(xs)-1,2):f.append((xs[i],xs[i+1]));remaining-={xs[i],xs[i+1]}
  xs=list(remaining);rng.shuffle(xs);f.extend(zip(xs[::2],xs[1::2]))
  assert len(f)==13 and {x for e in f for x in e}==covered
  rows.append({'id':len(rows),'mode':mode,'holes':sorted(holes),'avoid':avoid,'matching':[list(e) for e in f]})
(ROOT/'q5_t15_probe_inputs.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
(ROOT/'q5_t15_probe_inputs.txt').write_text('\n'.join(' '.join(map(str,[r['id'],*r['avoid'],13,*[x for e in r['matching'] for x in e]])) for r in rows)+'\n')
print('generated',len(rows),'diagnostic inputs')
