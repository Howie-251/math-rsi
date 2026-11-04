"""Probe alternate local cuts conditional on the original bad short edge f."""
from pathlib import Path
from itertools import permutations,combinations
from collections import defaultdict,Counter
import json
P=Path(__file__).resolve().parent
rows=json.loads((P/'FOURTEEN_NEW_TYPES_summary.json').read_text())['reports']
maps=[tuple(sum(((v>>p[k])&1)<<k for k in range(5)) for v in range(32)) for p in permutations(range(5))]
inv=[tuple(t.index(v) for v in range(32)) for t in maps]
mask=lambda s:sum(1<<x for x in s)
lookup=defaultdict(list)
for row in rows:
 g=row['geometry']
 for a in g['minority'] or g['omitted']:
  for pi,tr in enumerate(maps):
   key=tuple(mask(tr[x^a] for x in g[z]) for z in ('minority','majority','omitted'))
   lookup[key].append((row['index'],a,pi))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def peel(alive):
 alive=set(alive);out=[]
 while True:
  edge=next(((x,ns[0]) for x in sorted(alive) if len(ns:=[x^(1<<d) for d in range(6) if x^(1<<d) in alive])==1),None)
  if edge is None:return out
  out.append(edge);alive-=set(edge)
tasks=defaultdict(list)
for r in json.loads((P/'FOURTEEN_FIXED_E_AVOID_F_application.json').read_text())['conditional_records']:
 v=r['v'];rec=r['record'];Z=set(rec[:6]);W=set(rec[6:]);ff=r['forbidden_pairs'][0]
 known=peel(set(range(64))-{0}-Z-W)+[ff]
 for d in range(6):
  A=lambda x:(x>>d&1)==(v>>d&1)
  za={x for x in Z if A(x)};wa={x for x in W if A(x)};s=len(za)+1-len(wa)
  if s>=3:
   if not wa:continue
   pool=za;minor={x for x in Z if not A(x)};major={x for x in W if not A(x)}
  elif s<=-3:
   s=-s;pool=wa-{1<<d};minor={x for x in W if not A(x)};major={x for x in Z if not A(x)}
  else:continue
  if (len(minor),len(major)+s,s) not in [(3,9,3),(2,10,4),(1,11,5),(0,12,6)]:continue
  for S in combinations(sorted(pool),s):
   Y={x^(1<<d) for x in S};surviving=[edge for edge in known if all(not A(x) for x in edge) and not set(edge)&Y]
   if not surviving:continue
   M=[project(x,d) for x in minor];J=[project(x,d) for x in major|Y];U=[project(x,d) for x in Y];anchor=min(M or U)
   norm=tuple(mask(x^anchor for x in xs) for xs in (M,J,U))
   for i,ca,pi in lookup.get(norm,[]):
    # all known surviving edges are disjoint actual original short M edges
    es=tuple(sorted(tuple(sorted(inv[pi][project(x,d)^anchor]^ca for x in edge)) for edge in surviving))
    if len({x for e in es for x in e})!=len(es)*2:continue
    tasks[i,es].append(dict(v=v,input_index=r['input_index'],cut=d,sources=S,anchor=anchor,canonical_anchor=ca,permutation_index=pi,known=known))
ordered=sorted(tasks)
(P/'FOURTEEN_FIXED_E_AVOID_F_bad_tasks.txt').write_text(''.join(str(i)+' '+str(len(es))+' '+' '.join(str(x) for e in es for x in e)+'\n' for i,es in ordered))
(P/'FOURTEEN_FIXED_E_AVOID_F_bad_tasks.json').write_text(json.dumps([dict(local_index=i,edges=es,applications=tasks[i,es]) for i,es in ordered],indent=2)+'\n')
print('Bad original-f branch tasks',len(tasks),dict(Counter(len(es) for i,es in tasks)))
