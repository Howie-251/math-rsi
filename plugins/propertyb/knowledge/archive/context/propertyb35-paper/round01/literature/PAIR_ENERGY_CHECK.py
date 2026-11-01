"""Original a5 pair-energy consequence inspired by design-coloring double counts.
No source theorem is imported beyond elementary pair counting.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from math import comb
from collections import Counter
import json
P=Path(__file__).resolve().parent;R=P.parents[3]
values=[]
for r in combinations_with_replacement(range(6),5):
 red=sum(r);phi=comb(red,2)+comb(25-red,2)+sum(comb(a,2)+comb(5-a,2) for a in r)
 values.append((phi,r))
minimum=min(p for p,r in values)
assert minimum==164
source=R/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json'
d=json.loads(source.read_text());edges=d['edges'];redset=set([3,9,11,13,15,16,17,18,21,22,23])
r=[sum(p in redset for p in range(25) if ((p%5)-(p//5)**2)%5==g) for g in range(5)]
splits=Counter(len(set(e)&redset) for e in edges)
assert sum(splits[k]*(comb(k,2)+comb(5-k,2)) for k in splits)==168
assert splits.get(0,0)+splits.get(5,0)==0
assert splits[1]+splits[4]==14
out=dict(scope=__doc__,all_252_group_count_orbits_checked=True,minimum_pair_energy=minimum,minimizing_sorted_red_counts=[list(r) for p,r in values if p==minimum],block_equitable_two_coloring_required_energy=35*4,conclusion='block-equitable 2-coloring impossible; every proper 2-coloring has at least 12 edges split 1/4',actual_known_coloring=dict(group_red_counts=r,red_total=len(redset),pair_energy=168,edge_split_counts=dict(splits),one_four_edges=14))
(P/'PAIR_ENERGY_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
