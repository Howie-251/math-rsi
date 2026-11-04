"""Independent stdlib checks of the explicit exact-six-change obstruction.

Does not import the search program or use its EXHAUSTED status as evidence.
The lower bound uses all 60 possible new-neighbor choices and the degree
capacity argument in L6, rather than enumerating orders of path components.
"""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edges(seq):
    return {tuple(sorted((a, b))) for a, b in zip(seq, seq[1:] + seq[:1])}


def short(a, b):
    return (a ^ b).bit_count() == 1


def degrees(es):
    return Counter(x for e in es for x in e)


def main():
    source = ROOT/'a4_structured_repair_probe.json'
    raw = source.read_bytes()
    c = json.loads(raw)['bad']
    f = {tuple(sorted(e)) for e in c['matching']}
    assert len(f) == 14 and len({x for e in f for x in e}) == 28
    assert set(range(32)) - {x for e in f for x in e} == {0, 1, 14, 31}
    old, new = c['cycle29'], c['repair6']['cycle']
    assert len(old) == 29 and set(old) == set(range(32)) - {0, 1, 31}
    assert len(new) == 31 and set(new) == set(range(32)) - {1}
    eo, en = edges(old), edges(new)
    assert f <= eo and f <= en
    assert all(short(*e) for e in (eo | en) - f)
    h = {(x, x+1) for x in (2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, 26, 28)}
    h |= {(14, 15), (14, 30)}
    assert eo - f == h and len(eo - en) == 6
    assert len(en - eo) == 8  # new cycle has two more edges
    old_degrees = degrees(h)
    assert old_degrees[14] == 2
    assert all(old_degrees[x] == 1 for x in set(old) - {14})
    target = old_degrees + Counter({0: 2, 31: 2})
    assert degrees(en - f) == target
    a_neighbors = [x for x in range(32) if x != 1 and short(0, x)]
    b_neighbors = [x for x in range(32) if x != 1 and short(31, x)]
    assert a_neighbors == [2, 4, 8, 16]
    assert b_neighbors == [15, 23, 27, 29, 30]
    checked = 0
    for na in itertools.combinations(a_neighbors, 2):
        for nb in itertools.combinations(b_neighbors, 2):
            used = set(na + nb)
            removed = {e for e in h if used.intersection(e)}
            assert len(removed) == 4
            added = {tuple(sorted((0, x))) for x in na}
            added |= {tuple(sorted((31, x))) for x in nb}
            partial = degrees((h - removed) | added)
            assert all(partial[x] <= target[x] for x in range(32))
            deficit = {x: target[x] - partial[x] for x in target if target[x] != partial[x]}
            assert sum(deficit.values()) == 4
            assert not (set(deficit) & (used | {0, 1, 31}))
            assert all(not short(x, y) for x, y in itertools.combinations(deficit, 2))
            assert all(partial[x] == target[x] for x in target if x not in deficit)
            checked += 1
    assert checked == 60
    out = dict(status='PASS', scope='L6 exact-six-change witness and 60 degree-deficit cases; not A4 proof',
               input_sha256=hashlib.sha256(raw).hexdigest(),
               independent_of_search=True, neighbor_choices=checked,
               old_edges_deleted=6, new_edges_added=8,
               lower_bound=6, witness_attains_lower_bound=True,
               a4_proved=False, full_p6_proved=False)
    (ROOT/'a4_repair_obstruction_verification.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
