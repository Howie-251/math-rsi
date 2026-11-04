"""Exhaust the stated six-hole GEOMETRY domain, not matchings or P6.

Translate one non-root even hole to 0. Enumerate the other non-root even
hole q, the three odd holes W nonadjacent to {0,q}, and covered odd target v.
The root and the matching are intentionally absent: the S4/S7 shape tests
depend only on {0,q}, W, v.
"""
import itertools
import json
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ODD = [x for x in range(64) if x.bit_count() % 2]
EVEN = [x for x in range(64) if not x.bit_count() % 2]
TABLE = {
    'three_triples': (28, 44, 52),
    'triangle': (13, 21, 25),
    'star': (13, 21, 37),
    'path': (13, 25, 49),
    'top_adjacent': (13, 21, 61),
    'top_disjoint': (13, 49, 61),
}
S4 = {(1, 2), (1, 3), (0, 3)}


def shapes(q, w, v):
    return [(sum(((x ^ v) >> i) & 1 == 0 for x in (0, q)),
             1 + sum(((x ^ v) >> i) & 1 == 0 for x in w))
            for i in range(6)]


def permute(x, order):
    return sum(((x >> source) & 1) << target for target, source in enumerate(order))


def representative(q, w, v):
    assert q.bit_count() == 2
    order = [i for i in range(6) if q & (1 << i)] + [i for i in range(6) if not q & (1 << i)]
    w, v = tuple(permute(x, order) for x in w), permute(v, order)
    r = w[0] & 3
    assert all(x & 3 == r for x in w)
    if r == 3:
        w, v = tuple(x ^ 3 for x in w), v ^ 3
    elif r == 2:
        w, v = tuple(permute(x, [1, 0, 2, 3, 4, 5]) for x in w), permute(v, [1, 0, 2, 3, 4, 5])
    for tail in itertools.permutations(range(2, 6)):
        order = [0, 1] + list(tail)
        nw = tuple(sorted(permute(x, order) for x in w))
        for name, target in TABLE.items():
            if nw == target:
                return name, permute(v, order)
    raise AssertionError((q, w, v))


def main():
    start = time.monotonic()
    counts = Counter()
    by_type_s4, by_type_extended = Counter(), Counter()
    representatives = {}
    for name, w in TABLE.items():
        old = [v for v in ODD if v not in w and not any(s in S4 for s in shapes(3, w, v))]
        new = [v for v in old if (1, 1) not in shapes(3, w, v)]
        representatives[name] = dict(q=3, W=w, no_S4_targets=old, no_S4_or_S7_targets=new)
    assert [len(representatives[name]['no_S4_targets']) for name in TABLE] == [4, 4, 29, 8, 8, 2]
    assert [representatives[name]['no_S4_or_S7_targets'] for name in TABLE] == [
        [4], [1], [1, 25, 41, 49, 61], [1, 37], [1, 37], [1]]
    for q in EVEN[1:]:
        candidates = [x for x in ODD if x.bit_count() != 1 and (x ^ q).bit_count() != 1]
        for w in itertools.combinations(candidates, 3):
            for v in ODD:
                if v in w:
                    continue
                counts['all_normalized_geometry_inputs'] += 1
                ss = shapes(q, w, v)
                direct = any(s in S4 for s in ss)
                # Independent coordinate formula derived in the proof.
                constant_on_D = all(len({(x >> i) & 1 for x in w}) == 1
                                    for i in range(6) if q & (1 << i))
                bad_columns = sum(1 << i for i in range(6)
                                  if not q & (1 << i) and sum((x >> i) & 1 for x in w) == 2)
                formula_no_s4 = constant_on_D and not v & bad_columns
                assert not direct == formula_no_s4
                if direct:
                    counts['has_S4_cut'] += 1
                    continue
                counts['no_S4_cut'] += 1
                name, nv = representative(q, w, v)
                assert nv in representatives[name]['no_S4_targets']
                by_type_s4[name] += 1
                if (1, 1) in ss:
                    counts['new_S7_cut'] += 1
                else:
                    counts['no_S4_or_S7_cut'] += 1
                    assert nv in representatives[name]['no_S4_or_S7_targets']
                    by_type_extended[name] += 1
    result = dict(status='PASS', scope='all stated geometry inputs after z=0 normalization, not all matchings',
                  counts=dict(counts), old_exception_types=dict(by_type_s4),
                  remaining_types=dict(by_type_extended), representatives=representatives,
                  elapsed=time.monotonic()-start, a4_proved=False, full_p6_proved=False,
                  s7_path_conclusion_conditional_on_a4=True)
    (ROOT/'six_hole_geometry_census.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps({k: result[k] for k in ('status', 'scope', 'counts', 'old_exception_types', 'remaining_types', 'elapsed')}, indent=2))


if __name__ == '__main__':
    main()
