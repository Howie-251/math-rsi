#!/usr/bin/env python3
"""Read and directly verify the saved quotient survivors; no quotient search."""
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path
import json, time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'six_fiber_variable_internal_run'

def defect(d, q):
    r = [row[:] for row in q]
    for i in range(6):
        r[i][i] = d[i]
    b = [[sum(r[i][k] * r[k][j] for k in range(6)) + r[i][j]
          - 7 * (i == j) - 10 for j in range(6)] for i in range(6)]
    return r, b

def check(d, q):
    assert len(d) == 6 and list(d) == sorted(d) and min(d) >= 0 and max(d) <= 3
    assert min(d) != max(d) and sum(d) % 2 == 0
    assert len(q) == 6 and all(len(row) == 6 for row in q)
    for i in range(6):
        assert q[i][i] == 0 and sum(q[i]) == 8 - d[i]
        assert all(type(x) is int and x >= 0 for x in q[i])
        square = sum(x * x for x in q[i])
        assert 17 - d[i] - d[i]**2 <= square <= 22 - d[i] - d[i]**2
        for j in range(6):
            assert q[i][j] == q[j][i]
            if i != j:
                h = (1 + d[i] + d[j]) * q[i][j] + sum(q[i][k] * q[k][j] for k in range(6))
                assert h >= 10
    r, b = defect(d, q)
    assert all(sum(row) == 8 for row in r)
    assert all(sum(row) == 5 and min(row) >= 0 for row in b)
    return r, b

def main():
    start = time.process_time()
    result = json.loads((OUT / 'search.json').read_text())
    survivors = [json.loads(line) for line in (OUT / 'search.survivors.jsonl').read_text().splitlines()]
    assert result['complete'] and result['completed_eligible_tuples'] == 40
    assert len(survivors) == result['survivors'] == 98
    keys = [(tuple(s['d']), tuple(tuple(row) for row in s['Q'])) for s in survivors]
    assert len(set(keys)) == len(keys)
    counts = Counter()
    groups = defaultdict(list)
    for s in survivors:
        d = tuple(s['d']); q = s['Q']; check(d, q); counts[d] += 1
        codes = []
        for p in permutations(range(6)):
            if any(d[p[i]] != d[i] for i in range(6)):
                continue
            codes.append(tuple(q[p[i]][p[j]] for i in range(6) for j in range(i + 1, 6)))
        groups[(d, min(codes))].append(s)
    for entry in result['degree_tuples']:
        assert counts[tuple(entry['d'])] == entry['survivors']
        if entry['status'] != 'excluded_by_parity':
            assert entry['status'] == 'complete'
        assert sum(entry['minimum_capacity_histogram'].values()) == entry['row_compatible_matrices']
    assert sum(e['row_compatible_matrices'] for e in result['degree_tuples']) == result['row_compatible_matrices']
    orbits = []
    for (d, code), members in sorted(groups.items()):
        q = [[0] * 6 for _ in range(6)]; k = 0
        for i in range(6):
            for j in range(i + 1, 6):
                q[i][j] = q[j][i] = code[k]; k += 1
        orbit = set()
        for p in permutations(range(6)):
            if all(d[p[i]] == d[i] for i in range(6)):
                orbit.add(tuple(tuple(q[p[i]][p[j]] for j in range(6)) for i in range(6)))
        assert orbit == {tuple(tuple(row) for row in s['Q']) for s in members}
        r, b = check(d, q)
        orbits.append({'d': d, 'labeled_orbit_size': len(members), 'Q': q, 'R': r, 'defect_quotient': b})
    representative = json.loads((OUT / 'search.representative.json').read_text())
    r, b = check(representative['d'], representative['Q'])
    assert r == representative['R'] and b == representative['defect_quotient']
    assert (tuple(representative['d']), tuple(tuple(row) for row in representative['Q'])) in keys
    report = {
        'all_98_saved_survivors_directly_checked': True,
        'no_duplicate_saved_matrices': True,
        'all_reported_counts_consistent': True,
        'degree_preserving_orbit_count': len(orbits),
        'all_orbit_members_present': True,
        'orbits': orbits,
        'representative_defect_quotient_verified': True,
        'scope': 'Direct verification and relabeling of saved survivors only; no repeated quotient enumeration',
        'cpu_seconds': time.process_time() - start,
    }
    (OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'checked': len(survivors), 'orbits': len(orbits),
                      'orbit_sizes': [x['labeled_orbit_size'] for x in orbits],
                      'cpu_seconds': report['cpu_seconds']}, indent=2))

if __name__ == '__main__':
    main()
