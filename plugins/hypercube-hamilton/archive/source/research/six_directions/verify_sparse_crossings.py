"""Independent stdlib verification of S5/S6 hypotheses and path expansions."""
import hashlib
import json
from collections import Counter
from pathlib import Path
from verify_recut import edges, matching, sequence

R = Path(__file__).resolve().parent
V = set(range(64))


def check(c):
    assert c['status'] == 'FOUND'
    m = matching(c['matching'])
    assert all(0 <= a < b < 64 and (a ^ b).bit_count() == 1 for a, b in m)
    u, v, cut = c['u'], c['v'], c['cut']
    holes = V-{q for e in m for q in e}
    assert u in holes and (u.bit_count()-v.bit_count()) % 2 == 1
    aa = {q for q in V if ((q ^ v) >> cut) & 1 == 0}
    bb = V-aa
    pe = sequence(c['path'], V, m)
    assert c['path'][0] == u and c['path'][-1] == v
    if c['mode'] == 'S6':
        assert u in aa
        ma = {e for e in m if set(e) <= aa}
        mb = {e for e in m if set(e) <= bb}
        cross = m-ma-mb
        assert len(cross) == 2
        a, d = c['ports']
        assert {a, d} == {q for e in cross for q in e if q in aa}
        assert (a ^ d).bit_count() == 1
        aux = tuple(sorted((a, d)))
        ka = sequence(c['K_A'], aa, ma | {aux})
        kb = sequence(c['K_B'], bb, mb)
        assert c['K_A'][0] == u and c['K_A'][-1] == v
        assert c['K_B'][0] == a ^ (1 << cut) and c['K_B'][-1] == d ^ (1 << cut)
        assert pe == (ka-{aux}) | kb | cross
    else:
        assert c['mode'] == 'S5' and len(holes) == 6 and v not in holes
        h = c['h']
        vh, uh = tuple(sorted((v, h))), tuple(sorted((u, h)))
        assert vh in m
        star = matching(c['M_star'])
        assert star == m-{vh} | {uh}
        ma = {e for e in star if set(e) <= aa}
        mb = {e for e in star if set(e) <= bb}
        cross = star-ma-mb
        assert len(cross) == 1 and not {u, h} <= bb
        assert all((a ^ b).bit_count() == 1 for a, b in mb)
        ah = (holes-{u} | {v}) & aa
        shape = (sum(q.bit_count() % 2 == 0 for q in ah), sum(q.bit_count() % 2 == 1 for q in ah))
        assert shape in {(1, 2), (0, 3)}
        a, b, t, y = (c[k] for k in ('a', 'b', 'terminal', 'y'))
        assert a in aa and b in bb and cross == {tuple(sorted((a, b)))}
        assert t in ah-{v} and y == t ^ (1 << cut)
        assert y in {q for e in mb for q in e}
        aux = tuple(sorted((a, t)))
        la = matching(c['L_A'])
        assert la == ma | {aux}
        free_a = aa-{q for e in la for q in e}
        assert len(free_a) == 2 and v in free_a
        assert all(q.bit_count() % 2 == 1 for q in free_a)
        cae = sequence(c['C_A'], aa-{v}, la, cycle=True)
        j = c['transferred_path']
        assert j[0] == b and j[-1] == y
        assert len(j) == 33 and set(j[1:-1]) == aa-{v}
        je = edges(j)
        assert je == (cae-{aux}) | cross | {tuple(sorted((t, y)))}
        kb = sequence(c['K_B'], bb, mb)
        assert c['K_B'][0] == b and c['K_B'][-1] == y
        ge = sequence(c['C_global'], V-{v}, star, cycle=True)
        assert ge == kb | je
        assert pe == ge-{uh} | {vh}
    return len(holes)


raw = (R/'sparse_crossing_results.json').read_bytes()
d = json.loads(raw)
counts = Counter()
for c in d['cases']:
    counts[(c['mode'], check(c))] += 1
assert len(d['cases']) == 40
old = json.loads((R/'remaining_samples_after_Z5.json').read_text(encoding='utf8'))['remaining']
removed = {c['old_index'] for c in d['cases']}
assert len(removed) == 40
for c in d['cases']:
    o = old[c['old_index']]
    assert c['u'] == o['u'] and c['v'] == o['v']
    assert matching(c['matching']) == matching(o['matching'])
rem = json.loads((R/'remaining_samples_after_S5_S6.json').read_text(encoding='utf8'))
assert rem['remaining'] == [c for i, c in enumerate(old) if i not in removed]
remaining_holes = Counter(64-2*len(c['matching']) for c in rem['remaining'])
out = dict(status='PASS', verified=len(d['cases']), input_sha256=hashlib.sha256(raw).hexdigest(),
           branches_by_holes={f'{mode}_{holes}_holes':n for (mode,holes), n in counts.items()},
           remaining_old_samples=rem['count'], remaining_by_holes=dict(remaining_holes),
           full_p6_proved=False, exhaustive_q6=False)
(R/'sparse_crossing_verification.json').write_text(json.dumps(out, indent=2), encoding='utf8')
print(json.dumps(out, indent=2))
