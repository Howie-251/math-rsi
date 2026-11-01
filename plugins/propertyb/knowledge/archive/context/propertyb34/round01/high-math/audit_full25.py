"""Independent local extension recursion and full actual-profile/certificate binding for v25."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from unit_catalogue import canonical,fullblocks
from v25_nine_catalogue import profile

def alternative_extensions(big,n):
 old=fullblocks(big,n);choices={i:[t for t in old if t&(1<<i) and t.bit_count()<=4] for i in range(n)}
 def visit(left,promoted):
  if not left:
   yield tuple(sorted([t for t in big if t not in promoted]+[t|(1<<n) for t in promoted]));return
  b=left&-left;i=b.bit_length()-1
  yield from visit(left^b,promoted)
  for t in choices[i]:
   if t&left==t:yield from visit(left^t,promoted+(t,))
 yield from visit((1<<n)-1,())

def invariant(ns,degrees):
 s=len(degrees);assert sum(ns.values())==34 and all(c>0 and t.bit_count()<=5 for t,c in ns.items())
 assert all(sum(c for t,c in ns.items() if t&(1<<i))==degrees[i] for i in range(s))
 for i in range(s):
  for j in range(i):assert sum(c for t,c in ns.items() if t&(1<<i) and t&(1<<j))==1

if __name__=='__main__':
 start=time.perf_counter();out={};levels=[]
 for n in (7,8):
  parent=json.loads((HERE/f'UNIT_CATALOGUE_{n}.json').read_text());target=json.loads((HERE/f'UNIT_CATALOGUE_{n+1}.json').read_text());assert parent['complete'] and target['complete'];known={tuple(b) for b in target['orbits']};seen=set();raw=0
  for big in parent['orbits']:
   for e in alternative_extensions(tuple(big),n):
    k=canonical(e,n+1);assert k in known;seen.add(k);raw+=1
  assert seen==known and raw==target['raw_extensions'];levels.append(dict(n=n+1,independent_extensions=raw,orbits=len(seen),equal=True));print(levels[-1],flush=True)
 out['independent_extension_levels']=levels
 base=json.loads((HERE/'UNIT_CATALOGUE_9.json').read_text())['orbits'];cats={};colors=[]
 for q in (5,8,9):
  data=json.loads((HERE/f'V25_NINE_Q{q}_CATALOGUE.json').read_text());assert data['complete'];known={tuple(x['large_blocks']):x for x in data['results']};seen=set();raw=0
  for big in base:
   bs=fullblocks(big,9);deg=[sum(bool(t&(1<<i)) for t in bs) for i in range(9)]
   for low in combinations(range(9),q):
    single=[(6 if i in low else 7)-deg[i] for i in range(9)]
    if min(single)<0 or 34-len(bs)-sum(single)<0:continue
    raw+=1;k,p=canonical(big,9,[0 if i in low else 1 for i in range(9)],True)
    assert sum(1<<p[i] for i in low)==(1<<q)-1 and k in known
    assert profile(k,q)=={int(t):c for t,c in known[k]['counts'].items()};seen.add(k)
  assert seen==set(known) and raw==data['feasible_colorings'];cats[q]={x['id']:x for x in data['results']}
  bb=json.loads((HERE/f'V25_NINE_Q{q}_BOUNDS.json').read_text());assert bb['complete'];assert {x['id'] for x in bb['results']}==set(cats[q]);res=[]
  for z in bb['results']:
   assert z['counts']==cats[q][z['id']]['counts'] and z['independent_ABC'];ns={int(t):c for t,c in z['counts'].items()};invariant(ns,[6]*q+[7]*(9-q))
   if Q(z['bound'])>=1:res.append(z['id'])
  assert res==({5:[],8:[0,10],9:[0,3,6]}[q]);colors.append(dict(q=q,feasible_colorings=raw,colored_orbits=len(known),residue_ids=res,all_binding=True));print(colors[-1],flush=True)
 out['colored_catalogues']=colors;promotions=[]
 for q,filename in [(8,'V25_Q8_TENTH_BOUNDS.json'),(9,'V25_TENTH_BOUNDS.json')]:
  dd=json.loads((HERE/filename).read_text());assert dd['complete']
  for g in dd['results']:
   d=g['new_degree']
   for z in g['cases']:
    ns={int(t):c for t,c in z['counts'].items()};invariant(ns,[6]*q+[7]*(9-q)+[d]);assert Q(z['bound'])<1 and z['independent_ABC']
    proj={}
    for t,c in ns.items():u=t&511;proj[u]=proj.get(u,0)+c
    key,p=canonical([t for t in proj if t.bit_count()>=3],9,[0]*q+[1]*(9-q),True)
    assert key==tuple(cats[q][g['base']]['large_blocks'])
   promotions.append(dict(q=q,base=g['base'],new_degree=d,labelled=g['labelled_extensions'],orbits=len(g['cases']),all_strict=True))
 out.update(tenth_promotions=promotions,elapsed=time.perf_counter()-start,all_bindings_pass=True,scope=__doc__)
 (HERE/'FULL25_COVERAGE_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print('ALL_PASS',time.perf_counter()-start,flush=True)
