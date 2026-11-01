"""Independent replay by generator BFS and base-color/orbit intersections.
The main calculation instead counted monochromatic subsets of colorings.
No main-script function or saved per-set frequency is used here.
"""
from pathlib import Path
from collections import Counter,deque
from itertools import product
from fractions import Fraction
from math import comb
import json,time
P=Path(__file__).resolve().parent; st=time.perf_counter();d=json.loads((P/'AFFINE_AUGMENTATION.json').read_text())
R={5*x+y for x,y in product(range(5),repeat=2) if (x==0 or y==0 or y==x*x%5) and (x,y)!=(0,0)}
base=sum(1<<v for v in R); full=2**25-1;assert R==set(d['base_red']) and len(R)==12
lines={tuple(sorted(5*x+y for x in range(5) for y in range(5) if (x==t))) for t in range(5)}
lines|={tuple(sorted(5*x+(m*x+t)%5 for x in range(5))) for m,t in product(range(5),repeat=2)}
assert len(lines)==30 and all(1<=len(R&set(L))<=4 for L in lines)
# Translations, swap, a shear, and a primitive diagonal scaling.
transforms=[lambda x,y:((x+1)%5,y),lambda x,y:(x,(y+1)%5),lambda x,y:(y,x),lambda x,y:((x+y)%5,y),lambda x,y:((2*x)%5,y)]
gens=[tuple(1<<(5*f(x,y)[0]+f(x,y)[1]) for x,y in product(range(5),repeat=2)) for f in transforms]
def act(mask,p):
 ans=0
 while mask:
  b=mask&-mask;mask-=b;ans|=p[b.bit_length()-1]
 return ans

def bfs(mask):
 seen={mask};q=deque([mask])
 while q:
  x=q.popleft()
  for p in gens:
   z=act(x,p)
   if z not in seen:seen.add(z);q.append(z)
 return seen
colors_bfs=bfs(base);saved={r['red_mask']:r['multiplicity'] for r in d['color_orbit']}
assert colors_bfs==set(saved) and len(colors_bfs)==3000
# Independently recreate all affine images of the base red set, in tuple form.
color_counts=Counter()
for a,b,c,e,s,t in product(range(5),repeat=6):
 if (a*e-b*c)%5:
  rr={(5*((a*(v//5)+b*(v%5)+s)%5)+(c*(v//5)+e*(v%5)+t)%5) for v in R}
  color_counts[sum(1<<v for v in rr)]+=1
assert dict(color_counts)==saved and set(color_counts.values())=={4}
seen=set(); checks=[]
for row in d['five_set_orbits']:
 orbit=bfs(row['representative_mask']);assert orbit==set(row['members'])
 assert not seen&orbit;seen|=orbit
 assert all(0<=m<=full and m.bit_count()==5 for m in orbit)
 mono=sum(m&base==m or m&(full^base)==m for m in orbit)
 probability=Fraction(mono,len(orbit))
 assert mono==row['base_coloring_mono_members'] and str(probability)==row['probability']
 assert probability==Fraction(row['mono_automorphisms'],12000)
 # Direct fixed-B subset tests on every independently reconstructed color.
 rep=row['representative_mask']
 direct=sum(w for cm,w in color_counts.items() if cm&rep==rep or (full^cm)&rep==rep)
 assert direct==row['mono_automorphisms']
 checks.append(dict(id=row['id'],size=len(orbit),base_mono=mono,probability=str(probability),representative=row['representative_points']))
assert len(seen)==comb(25,5)==53130
assert sum(c['base_mono'] for c in checks)==comb(12,5)+comb(13,5)==2079
maximum=max(Fraction(c['probability']) for c in checks);assert maximum==Fraction(21,500)
assert sum(c['size']*Fraction(c['probability']) for c in checks)==2079
out=dict(scope=__doc__,passed=True,checks=checks,max_probability=str(maximum),five_additional_union_bound=str(5*maximum),colorings=len(colors_bfs),five_sets=len(seen),distinct_orbits=len(checks),elapsed_seconds=time.perf_counter()-st)
(P/'AFFINE_AUGMENTATION_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
