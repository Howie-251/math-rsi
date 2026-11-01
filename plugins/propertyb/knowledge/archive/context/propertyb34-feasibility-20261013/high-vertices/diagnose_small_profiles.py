"""Exact local-profile arithmetic for T34 preparation; no hypergraph search."""
import sys, json
from pathlib import Path
from itertools import combinations
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'computations'))
from multilock import Profile, link_certificate, rows, total_bound, json_value
from enumerate_pair_partitions import enumerate_partitions, canonical_large_blocks, exact_types
OUT = Path(__file__).parent

def run():
    doubles = []
    for lam in range(5, 9):
        best = None
        for pos in combinations(range(1, 25), 2):
            p = Profile(24, 5, pos, {0: 18 + lam, 1: 8 - lam, 2: 8 - lam, 3: lam})
            deductions = {pos[i]: link_certificate(p, i, 3)['deduction'] for i in range(2)}
            u = total_bound(rows(p, deductions=deductions))
            if best is None or u < best['bound']:
                best = {'bound': u, 'positions': pos, 'deductions': deductions}
        doubles.append(dict(codegree=lam, **best))
    (OUT / 'HIGH_DOUBLE_LOCK_DIAGNOSTIC.json').write_text(json.dumps(json_value(doubles), indent=2) + '\n')
    by_orbit = {}
    labelled = enumerate_partitions(5)
    for part in labelled:
        canon = canonical_large_blocks(part, 5)
        counts = exact_types(part, 5, degree=7, edges=34)['counts_by_mask']
        for start in range(7, 15):
            pos = tuple(range(start, start + 5))
            p = Profile(24, 5, pos, counts)
            deductions = {pos[i]: link_certificate(p, i, 2)['deduction'] for i in range(5)}
            u = total_bound(rows(p, deductions=deductions))
            if canon not in by_orbit or u < by_orbit[canon]['bound']:
                by_orbit[canon] = {'large_blocks': canon, 'bound': u, 'labelled_partition': part,
                                  'positions': pos, 'counts': counts, 'deductions': deductions}
    (OUT / 'FIVE_UNIT_SEVEN_DIAGNOSTIC.json').write_text(json.dumps(json_value(list(by_orbit.values())), indent=2) + '\n')
    print(json.dumps({'five_lock_labelled_inputs': len(labelled), 'five_lock_orbits': len(by_orbit),
                      'double_profiles': len(doubles), 'scope': 'Exact rational local-profile diagnostics; no Lean or full T34 proof.'}))

if __name__ == '__main__':
    run()
