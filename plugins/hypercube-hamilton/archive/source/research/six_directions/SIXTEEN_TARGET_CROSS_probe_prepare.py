"""Producer: target crossing forces compressed B pair root--mate."""
from pathlib import Path
from itertools import permutations,combinations
from collections import defaultdict,Counter
import json
P=Path(__file__).resolve().parent
rows=json.loads((P/'SIXTEEN_NEW_TYPES_summary.json').read_text())['reports']+json.loads((P/'Q5_T37_INDEPENDENT_summary.json').read_text())['reports']
maps=[tuple(sum(((v>>p[k])&1)<<k for k in range(5)) for v in range(32)) for p in permutations(range(5))]
inv=[tuple(t.index(v) for v in range(32)) for t in maps];mask=lambda s:sum(1<<x for x in s)
lookup=defaultdict(list);shapes=set()
for ri,row in enumerate(rows):
 g=row['geometry'];shapes.add((len(g['minority']),len(g['majority']),len(g['omitted'])))
 for a in g['minority'] or g['omitted']:
  for pi,tr in enumerate(maps):
   key=tuple(mask(tr[x^a] for x in g[z]) for z in ('minority','majority','omitted'))
   lookup[key].append((ri,a,pi))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def peel(alive):
 alive=set(alive);out=[]
 while True:
  edge=next(((x,ns[0]) for x in sorted(alive) if len(ns:=[x^(1<<d) for d in range(6) if x^(1<<d) in alive])==1),None)
  if edge is None:return out
  out.append(edge);alive-=set(edge)
tasks=defaultdict(list);allcases=[]
for r in json.loads((P/'SIXTEEN_REMAINDER_geometry.json').read_text())['representatives'][:4]:
 v=r['v'];Z=set(r['Z']);W=set(r['W']);alive=set(range(64))-{0}-Z-W;known=peel(alive)
 for d in range(6):
  h=v^(1<<d)
  if h not in alive:continue
  allcases.append(dict(v=v,Z=r['Z'],W=r['W'],mate=h))
  if not v>>d&1:continue # u in A: root--mate is not a B pair
  if h in {x for e in known for x in e}:continue
  A=lambda x:x>>d&1
  za={x for x in Z if A(x)};wa={x for x in W if A(x)};s=len(za)+1-len(wa)
  if s>=2:
   if not wa:continue
   pool=za;minor={x for x in Z if not A(x)};major={x for x in W if not A(x)}
  elif s<=-2:
   s=-s;pool=wa-{1<<d};minor={x for x in W if not A(x)};major={x for x in Z if not A(x)}
  else:continue
  if (len(minor),len(major)+s,s) not in shapes:continue
  for S in combinations(sorted(pool),s):
   Y={x^(1<<d) for x in S};surviving=[(0,h)]+[e for e in known if all(not A(x) for x in e) and not set(e)&Y]
   M=[project(x,d) for x in minor];J=[project(x,d) for x in major|Y];U=[project(x,d) for x in Y];anchor=min(M or U)
   norm=tuple(mask(x^anchor for x in xs) for xs in (M,J,U))
   for ri,ca,pi in lookup.get(norm,[]):
    row=rows[ri];es=tuple(sorted(tuple(sorted(inv[pi][project(x,d)^anchor]^ca for x in e)) for e in surviving))
    assert len({x for e in es for x in e})==2*len(es)
    tasks[ri,es].append(dict(v=v,Z=r['Z'],W=r['W'],mate=h,cut=d,sources=S,anchor=anchor,canonical_anchor=ca,permutation_index=pi,known=known))
ordered=sorted(tasks)
out=[dict(task_index=j,source_prefix=rows[ri]['prefix'],geometry=rows[ri]['geometry'],edges=es,applications=tasks[ri,es]) for j,(ri,es) in enumerate(ordered)]
(P/'SIXTEEN_TARGET_CROSS_tasks.json').write_text(json.dumps(out,indent=2)+'\n')
(P/'SIXTEEN_TARGET_CROSS_tasks.txt').write_text(''.join(str(r['task_index'])+' '+r['source_prefix']+' '+str(32-len(r['geometry']['minority'])-len(r['geometry']['majority']))+' '+str(len(r['edges']))+' '+' '.join(str(x) for e in r['edges'] for x in e)+'\n' for r in out))
print('Tasks',len(out),Counter(len(r['edges']) for r in out));print([(r['task_index'],r['source_prefix'],r['edges']) for r in out])
