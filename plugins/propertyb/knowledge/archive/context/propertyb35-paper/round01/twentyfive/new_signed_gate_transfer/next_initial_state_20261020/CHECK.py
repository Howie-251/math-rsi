"""Verify a fixed actual initial-state witness, without optimizing its color."""
from itertools import combinations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
raw=json.loads((HERE.parents[1]/'MIXED_THREE_SIX_UNIT8_REALIZATION.json').read_text())
H=list(map(frozenset,raw['edges']))
G=frozenset({0,1,2,3,4})
K=frozenset({0,1,2})
B=frozenset({5,6,7,10,13,15,19,20})
assert all(e==G or (e&B and e-B) for e in H)
positive={g:[e-{g} for e in H if g in e and e!=G and e-{g}<=B] for g in K}
singletons={x:next(sorted(e) for e in H if not e&K and e&B=={x})
            for x in B if any(not e&K and e&B=={x} for e in H)}
assert set(singletons)=={5,10,13,19,20}
pair=frozenset({3,7,11,15,24})
assert pair in H and not pair&K and pair&B=={7,15}
cases=[]
for size in range(1,4):
    for selected in combinations(sorted(K),size):
        repairs=[]
        for n in range(len(B)+1):
            for recolored in combinations(sorted(B),n):
                blue=(B-set(recolored))|set(selected)
                if all(e&blue and e-blue for e in H):repairs.append(list(recolored))
        cases.append({'flipped_lows':selected,'exterior_repairs':repairs})
assert not next(z['exterior_repairs'] for z in cases if z['flipped_lows']==(0,1))
assert not next(z['exterior_repairs'] for z in cases if z['flipped_lows']==(0,1,2))
assert [] in next(z['exterior_repairs'] for z in cases if z['flipped_lows']==(2,))
out={'scope':'One fixed coloring of a frozen actual H; not a new minimizing rule.',
     'G':sorted(G),'initial_blue':sorted(B),
     'positive_blocks':{str(g):[sorted(A) for A in positive[g]] for g in K},
     'zero_low_singleton_witnesses':singletons,'zero_low_pair_edge':sorted(pair),
     'all_seven_low_subsets':cases,'status':'PASS'}
(HERE/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: fixed actual source, all seven low-flip subsets and256 exterior subsets each.')
