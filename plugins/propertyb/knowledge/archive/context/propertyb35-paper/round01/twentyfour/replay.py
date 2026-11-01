"""Deterministic replay: fixed-position bounds and independent direct color-count probabilities."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,product
from math import comb
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate
from fourlock_pilot import inventory
st=time.time();nprofiles=0
for name,s in [('FOURLOCK_PILOT.json',4),('FIVELOCK_PILOT.json',5)]:
 z=json.loads((HERE/name).read_text());profile=z['profiles'];domains={}
 for r in profile:
  k=int(r['conflict']) if s==4 else r['matching_edges'];ns={int(a):b for a,b in r['counts'].items()}
  pairs={(i,j):1+int((i,j) in [(0,1),(2,3)][:k]) for i in range(s) for j in range(i+1,s)}
  domains.setdefault(k,set()).add(tuple(ns[m] for m in range(1<<s)))
  ev=evaluate(24,ns,tuple(r['positions']),True)
  assert ev['bound']==Q(r['bound']) and ev['strict']==r['strict'];nprofiles+=1
 for k,seen in domains.items():
  pairs={(i,j):1+int((i,j) in [(0,1),(2,3)][:k]) for i in range(s) for j in range(i+1,s)}
  assert seen=={tuple(ns[m] for m in range(1<<s)) for ns in inventory(s,[7]*s,pairs)}
templates=json.loads((HERE/'SIX_TEMPLATE_PILOT.json').read_text())['profiles']
for r in templates:
 ns={int(a):b for a,b in r['counts'].items()};ev=evaluate(24,ns,tuple(r['positions']),True);assert ev['bound']==Q(r['bound']) and ev['strict']==r['strict'];nprofiles+=1
z=json.loads((HERE/'LINK_BLOCK_PILOT.json').read_text());colors=z['colors'];edges=z['edges'];P=z['probabilities']
assert {tuple(c) for c in colors}=={(pc,*sorted((a,b)),*sorted(cs)) for pc in (0,1) for a in range(4-pc) for b in range(4-pc) for cs in product(range(4),repeat=4)}
assert {tuple(e) for e in edges}=={(ep,*sorted((a,b)),*sorted(cs)) for ep in (0,1) for a in range(4) for b in range(4) for cs in product(range(5),repeat=4) if ep+a+b+sum(cs)==5}
recomputed=[]
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
for co,row in zip(colors,P):
 pc,*cs=co;variants={a+b for a in permutations(cs[:2]) for b in permutations(cs[2:])};rr=[]
 for ed,stored in zip(edges,row):
  ep,*es=ed;prob=Q()
  for rs in variants:
   denom=1;red=int(not ep or pc);blue=int(not ep or not pc)
   for n,r,e in zip((3,3,4,4,4,4),rs,es):
    denom*=comb(n,r);red*=choose(n-e,r-e);blue*=choose(n-e,r)
   prob+=Q(red+blue,denom)
  prob/=len(variants);assert prob==Q(stored);rr.append(prob)
 recomputed.append(rr)
o=json.loads((HERE/'BLOCK_TYPE_OBSTRUCTION.json').read_text());bytype={tuple(r['edge']):r['count'] for r in o['type_counts']};ns=[bytype.get(tuple(e),0) for e in edges];scores=[sum(n*p for n,p in zip(ns,row)) for row in recomputed];assert sum(ns)==29 and min(scores)==Q(o['exact_minimum'])>=1
constraints=[sum(ns),sum(n*e[0] for n,e in zip(ns,edges)),sum(n*sum(e[1:3]) for n,e in zip(ns,edges)),sum(n*sum(e[3:]) for n,e in zip(ns,edges)),sum(n*e[1]*e[2] for n,e in zip(ns,edges)),sum(n*sum(e[1:3])*sum(e[3:]) for n,e in zip(ns,edges)),sum(n*sum(e[i]*e[j] for i in range(3,7) for j in range(i+1,7)) for n,e in zip(ns,edges))]
assert constraints==o['constraints'] and all(a>=b for a,b in zip(constraints,o['required']))
out=dict(scope=__doc__,passed=True,local_inventory_profiles=nprofiles,independent_A_B_C_rows=24*nprofiles,color_families=len(colors),edge_types=len(edges),independent_exact_probability_cells=len(colors)*len(edges),type_obstruction_minimum=str(min(scores)),elapsed_seconds=time.time()-st)
(HERE/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
