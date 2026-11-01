"""Reuse the unchanged 86 five-graph representatives; generate no new domain."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
source=HERE.parents[1]/'twentyfour/positive_occ_three/five_graph_catalogue.json'
data=json.loads(source.read_text())
rows=[]
for z in data['graphs']:
    ps=[p['mask'] for p in z['points']]
    pair, triple=Counter(),Counter()
    count=0
    for ids in combinations(range(len(ps)),4):
        covered=0
        for i in ids:covered |= ps[i]
        if covered != 31:continue
        count+=1
        pair.update(combinations(ids,2))
        triple.update(combinations(ids,3))
    assert count == z['C4'] == z['C4_independent_IE']
    e2=max(pair.values(),default=0)
    e3=max(triple.values(),default=0)
    bad=max(e2*r+e3*(4-r)+e3*b+(17-b)
            for r in range(5) for b in range(5-r))
    rows.append({'old_orbit_id':z['index'],'E':z['E'],'M2':z['M2'],
                 'C4':count,'maximum_specified_pair_extension':e2,
                 'maximum_specified_triple_extension':e3,
                 'new_separate_union_bound':bad,'gap':count-bad})
residual=[r for r in rows if r['gap']<=0]
assert [r['old_orbit_id'] for r in residual]==[0,2,4,20,34,49,66]
assert all(r['E']==4 for r in residual)
p=F(7,16)
low=4*p**3+17*p**4
assert low < 1
out={'scope':'Only old 86 representatives and exact specified-subset extension counts; no new graph or H domain.',
     'low_occurrence_union_bound':str(low),
     'new_generic_C3_block_bound':16,'old_C3_threshold':14,
     'new_generic_C4_block_bound':201,'old_C4_minimum':178,
     'triangle_zero_matching_minimum_candidates':80,
     'triangle_new_separate_block_bound':81,
     'old_orbits':len(rows),'old_label_count':data['labeled_graphs'],
     'nonstrict_old_orbits':residual,'all_rows':rows,'status':'DIAGNOSIS_COMPLETE'}
(HERE/'EIGHT_FOUR_TRIPLES_DIAGNOSIS_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_rows'},indent=2))
