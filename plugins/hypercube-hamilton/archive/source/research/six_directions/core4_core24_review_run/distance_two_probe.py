"""Z8 finite branch checks; not exhaustive matching enumeration."""
import json
import random
from itertools import combinations
from pathlib import Path
from single_bridge_probe import random_maximum, verify
from split_transfer import local_path
from unbalanced_transfer import prepare_core, finish, half_layers, edge

ROOT = Path(__file__).resolve().parent


def main():
    rng = random.Random(20261109)
    odd = [q for q in range(1, 64, 2) if q.bit_count() % 2 == 1
           and (q ^ 3).bit_count() != 1]
    cases = []
    for w, t in combinations(odd, 2):
        m = random_maximum(6, {0, 3, w, t}, rng)
        assert len(m) == 30
        v = next(q for q in (61, 59, 55) if q not in (w, t))
        cross = [e for e in m if e[0] ^ e[1] == 1]
        if len(cross) == 1:
            a = next(q for q in cross[0] if q % 2 == 0)
            b = a ^ 1
            ma = [e for e in m if all(q % 2 == 0 for q in e)]
            mb = [e for e in m if all(q % 2 == 1 for q in e)]
            ra, rb = local_path(6, 0, 0, ma, 0, a), local_path(6, 0, 1, mb, b, v)
            assert ra['status'] == rb['status'] == 'FOUND'
            path = ra['path'] + rb['path']
            verify(6, m, 0, v, path)
            result = dict(status='FOUND', matching=m, u=0, v=v, path=path, branch='D5')
        else:
            prepared = prepare_core(m, odd_holes=(w, t), choose_root_pair=True)
            assert prepared['status'] == 'PREPARED'
            result = dict(finish(prepared, v), branch='Z8_multiple_cross')
            assert result['status'] == 'FOUND'
        cases.append(dict(result, holes=[0, 3, w, t]))
    # A targeted case: the naive completion is the full direction-2 matching,
    # and both endpoint choices have a half-layer. The Z8 choice must repair it.
    ma = [edge(a, a ^ 4) for a in range(0, 64, 2) if not a & 4
          and a not in (0, 24)]
    cross = [(4, 5), (24, 25), (28, 29)]
    local_holes = {q >> 1 for q in (3, 13, 21, 5, 25, 29)}
    mb = [edge(2*a+1, 2*b+1) for a, b in random_maximum(5, local_holes, rng)]
    assert len(mb) == 13
    m = ma + cross + mb
    naive = ma + [(0, 4), (24, 28)]
    mate = {a: b for e in naive for a, b in (e, e[::-1])}
    blocked = []
    for d in (12, 20):
        compression = [e for e in naive if 2 not in e and d not in e]
        compression.append(edge(mate[2], mate[d]))
        blocked.append(half_layers(compression, range(0, 64, 2), range(1, 6)))
    assert all(blocked)
    prepared = prepare_core(m, odd_holes=(13, 21), choose_root_pair=True)
    assert prepared['status'] == 'PREPARED'
    targeted = finish(prepared, 61)
    assert targeted['status'] == 'FOUND'
    cases.append(dict(targeted, holes=[0, 3, 13, 21], branch='Z8_targeted_repair',
                      naive_half_obstacles=blocked))
    result = dict(scope='55 normalized hole geometries, one matching each, plus one targeted repair; not exhaustive Q6',
                  cases=cases, full_p6_proved=False)
    (ROOT/'distance_two_results.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(dict(status='PASS', cases=len(cases), naive_blocked=blocked,
                          repaired_D=targeted['D']), indent=2))


if __name__ == '__main__':
    main()
