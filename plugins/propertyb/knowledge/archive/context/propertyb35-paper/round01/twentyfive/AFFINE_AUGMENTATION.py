"""Exact AGL(2,5) orbit certificate for one proper coloring of AG(2,5).
Only the 53130 five-subsets and 12000 affine automorphisms are examined;
no hypergraphs or augmentations are enumerated.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from math import comb
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent; root=P.parents[3]; st=time.perf_counter()
H=json.loads((root/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json').read_text())
E=H['edges']; lines=[set(e) for e in E[:30]]
R=json.loads((P/'ANCHOR_TRANSFER_CHECK.json').read_text())['two_ray_repair']['red']
assert len(R)==12 and all(0<len(set(R)&e)<5 for e in lines)
full=(1<<25)-1
GL=[(a,b,c,d) for a,b,c,d in product(range(5),repeat=4) if (a*d-b*c)%5]
assert len(GL)==480
perms=[]; colors=Counter()
for a,b,c,d in GL:
 for s,t in product(range(5),repeat=2):
  p=tuple(1<<(5*((a*x+b*y+s)%5)+(c*x+d*y+t)%5) for x,y in product(range(5),repeat=2))
  assert len(set(p))==25
  perms.append(p); colors[sum(p[v] for v in R)]+=1
assert len(perms)==12000 and sum(colors.values())==12000
profile=dict(group_and_color_seconds=time.perf_counter()-st,unique_red_colorings=len(colors))
# Direct incidence count: enumerate every monochromatic five-subset of each
# distinct transformed coloring, retaining its full group multiplicity.
all_B={sum(1<<v for v in B):0 for B in combinations(range(25),5)}
assert len(all_B)==comb(25,5)==53130
for cm,w in colors.items():
 for side in (cm,full^cm):
  vs=[1<<v for v in range(25) if side>>v&1]
  for B in combinations(vs,5):all_B[sum(B)]+=w
profile['direct_incidence_seconds']=time.perf_counter()-st
line_masks={sum(1<<v for v in e) for e in lines}
assert all(all_B[m]==0 for m in line_masks)
# Independent orbit computation from affine point maps, then direct subset
# tests on the orbit representative and a separate base-color intersection.
base=sum(1<<v for v in R); unseen=set(all_B); orbits=[]
while unseen:
 rep=min(unseen); vs=[v for v in range(25) if rep>>v&1]
 orb={sum(p[v] for v in vs) for p in perms}
 assert rep in orb and orb<=unseen
 unseen-=orb
 freqs={all_B[m] for m in orb};assert len(freqs)==1
 m=freqs.pop()
 by_direct_test=sum(w for cm,w in colors.items() if (rep&cm)==rep or (rep&(full^cm))==rep)
 assert by_direct_test==m
 base_mono=sum((v&base)==v or (v&(full^base))==v for v in orb)
 assert len(orb)*m==12000*base_mono
 orbits.append(dict(id=len(orbits),representative_mask=rep,representative_points=vs,size=len(orb),mono_automorphisms=m,probability=str(Fraction(m,12000)),base_coloring_mono_members=base_mono,is_line=rep in line_masks,members=sorted(orb)))
assert sum(o['size'] for o in orbits)==53130
assert sum(o['base_coloring_mono_members'] for o in orbits)==comb(12,5)+comb(13,5)==2079
assert sum(all_B.values())==12000*2079
assert sum(o['size']*o['mono_automorphisms'] for o in orbits)==12000*2079
maxn=max(all_B.values()); worst=[o for o in orbits if o['mono_automorphisms']==maxn]
cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text()); feasible={r['id'] for r in json.loads((P/'GROUP5_PARTITIONS.json').read_text())['results'] if r['status']=='FEASIBLE'}
ids=[r['id'] for r in cat['representatives'] if r['counts'].get('31',0)==1]
out=dict(scope=__doc__,standard_field=5,point_encoding='5*x+y',base_red=R,base_blue=[v for v in range(25) if v not in R],group_definition='(x,y) -> (a*x+b*y+s,c*x+d*y+t) modulo 5; ad-bc nonzero',GL2_matrices=[list(m) for m in GL],automorphisms=12000,color_orbit=[dict(red_mask=m,multiplicity=w) for m,w in sorted(colors.items())],profile=profile,five_set_orbits=orbits,summary=dict(five_sets=53130,orbits=len(orbits),colorings=len(colors),color_multiplicity_sum=sum(colors.values()),base_mono_five_sets=2079,total_incidence_sum=sum(all_B.values()),max_mono_automorphisms=maxn,max_probability=str(Fraction(maxn,12000)),strictly_below_one_fifth=5*maxn<12000,worst_orbit_ids=[o['id'] for o in worst],worst_representatives=[o['representative_points'] for o in worst],line_orbit_ids=[o['id'] for o in orbits if o['is_line']],mu_full_group_one_ids_among_27=ids,mu_full_group_one_ids_among_22=[i for i in ids if i in feasible],elapsed_seconds=time.perf_counter()-st))
(P/'AFFINE_AUGMENTATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['summary'],indent=2));print(json.dumps(profile,indent=2))
