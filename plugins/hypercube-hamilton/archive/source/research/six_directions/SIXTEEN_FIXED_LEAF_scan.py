"""Producer fixed-original-edge tasks on the nonstar118 residual."""
from pathlib import Path
from itertools import permutations,combinations
from collections import defaultdict,Counter
import json,sys
P=Path(__file__).resolve().parent
rows=json.loads((P/'SIXTEEN_NEW_TYPES_summary.json').read_text())['reports']
maps=[tuple(sum(((v>>p[k])&1)<<k for k in range(5)) for v in range(32)) for p in permutations(range(5))]
inv=[tuple(t.index(v) for v in range(32)) for t in maps]
mask=lambda s:sum(1<<x for x in s)
lookup=defaultdict(list);shapes=set()
for row in rows:
 g=row['geometry'];shapes.add((len(g['minority']),len(g['majority']),len(g['omitted'])))
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
tasks=defaultdict(list);profile=[];branchf={}
prefix='SIXTEEN_FIXED_LEAF'
if '--branch-f' in sys.argv:
 prefix='SIXTEEN_FIXED_LEAF_BADF'
 for task in json.loads((P/'SIXTEEN_FIXED_LEAF_tasks.json').read_text()):
  for a in task['applications']:
   d=a['cut'];side=1-(a['v']>>d&1);tr=maps[a['permutation_index']]
   def glob(x):
    q=tr[x^a['canonical_anchor']]^a['anchor']
    return (q&((1<<d)-1))|((q>>d)<<(d+1))|(side<<d)
   pair=tuple(sorted((glob(8),glob(24))));key=a['v'],a['input_index']
   assert key not in branchf or branchf[key]==pair;branchf[key]=pair
geo=json.loads((P/'SIXTEEN_REMAINDER_geometry.json').read_text())
for r in geo['rows']:
 if r['all_Z_B_cuts']:continue
 v=r['v'];Z=set(r['Z']);W=set(r['W']);alive=set(range(64))-{0}-Z-W
 if branchf:
  ff=branchf[v,r['index']];known=[ff]+peel(alive-set(ff))
 else:known=peel(alive)
 profile.append(dict(v=v,input_index=r['index'],leaf_chain=known))
 for d in range(6):
  A=lambda x:(x>>d&1)==(v>>d&1)
  za={x for x in Z if A(x)};wa={x for x in W if A(x)};s=len(za)+1-len(wa)
  if s>=2:
   if not wa:continue
   pool=za;minor={x for x in Z if not A(x)};major={x for x in W if not A(x)}
  elif s<=-2:
   s=-s;pool=wa-{1<<d};minor={x for x in W if not A(x)};major={x for x in Z if not A(x)}
  else:continue
  if (len(minor),len(major)+s,s) not in shapes:continue
  for S in combinations(sorted(pool),s):
   Y={x^(1<<d) for x in S};surviving=[edge for edge in known if all(not A(x) for x in edge) and not set(edge)&Y]
   if not surviving:continue
   M=[project(x,d) for x in minor];J=[project(x,d) for x in major|Y];U=[project(x,d) for x in Y];anchor=min(M or U)
   norm=tuple(mask(x^anchor for x in xs) for xs in (M,J,U))
   for i,ca,pi in lookup.get(norm,[]):
    es=tuple(sorted(tuple(sorted(inv[pi][project(x,d)^anchor]^ca for x in edge)) for edge in surviving))
    assert len({x for e in es for x in e})==len(es)*2
    tasks[i,es].append(dict(v=v,input_index=r['index'],cut=d,sources=S,anchor=anchor,canonical_anchor=ca,permutation_index=pi,known=known))
ordered=sorted(tasks)
(P/(prefix+'_tasks.json')).write_text(json.dumps([dict(local_index=i,edges=es,applications=tasks[i,es]) for i,es in ordered],indent=2)+'\n')
(P/(prefix+'_profile.json')).write_text(json.dumps(profile,indent=2)+'\n')
print('Fixed leaf tasks',len(tasks),dict(Counter(len(es) for i,es in tasks)))
print([(i,es,len(tasks[i,es])) for i,es in ordered])
