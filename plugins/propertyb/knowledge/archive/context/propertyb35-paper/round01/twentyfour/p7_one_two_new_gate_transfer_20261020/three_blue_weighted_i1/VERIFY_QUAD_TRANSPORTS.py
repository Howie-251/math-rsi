"""Full S7-filter group verification of all 7770 stored quad multiset transports."""
from itertools import permutations,combinations_with_replacement
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'QUAD_ORBITS.json').read_text())
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
group={p for p in permutations(range(7)) if move(31,p)==31}
assert len(group)==240 and group==set(map(tuple,d['group']))
quads=[m for m in range(128) if m.bit_count()==4]
expected=set(combinations_with_replacement(quads,3))
assert len(expected)==7770
jobs=d['jobs'];assert len(jobs)==101 and [r['job'] for r in jobs]==list(range(101))
reps={r['job']:tuple(r['quad_masks']) for r in jobs}
actual={}
for row in d['all_7770_images']:
    key=tuple(row['quad_masks']);assert key not in actual
    p=tuple(d['group'][row['transport_index']]);assert p in group
    assert tuple(sorted(move(q,p) for q in reps[row['job']]))==key
    actual[key]=row['job']
assert set(actual)==expected
for row in jobs:
    rep=tuple(row['quad_masks'])
    orbit={tuple(sorted(move(q,p) for q in rep)) for p in group}
    assert min(orbit)==rep and len(orbit)==row['orbit_size']
    assert {key for key,j in actual.items() if j==row['job']}==orbit
result=dict(PASS=True,group_order=240,quad_multiset_orbits=101,
            complete_quad_multiset_keys_and_transports_checked=7770)
(HERE/'QUAD_TRANSPORT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS full S7-filter group, all7770 keys and actual transports,101 orbits')
