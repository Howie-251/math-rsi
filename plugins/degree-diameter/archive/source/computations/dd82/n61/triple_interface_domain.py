"""Complete necessary (C,sigma) catalogue for the actual triple-repeat template.

Only 4x4 row/column-three matrices and already proved port rules are tested.
No actual adjacency completion or original-graph exclusion is decided.
Independent row/column orbits are diagnostic only: the fixed A matching
permits simultaneous permutations, with sigma conjugated by the same map.
"""
from itertools import permutations, product
from pathlib import Path
import json
import os
import resource
import time

PERMS = tuple(permutations(range(4)))


def relabel(c, p):
    return tuple(tuple(c[p[i]][p[j]] for j in range(4)) for i in range(4))


def conjugate(sigma, p):
    inverse = tuple(p.index(i) for i in range(4))
    return tuple(inverse[sigma[p[i]]] for i in range(4))


def compatible(c, sigma):
    return (all(c[i][i] != 1 or sigma[i] == i for i in range(4))
            and all(c[i][j] != 3 or sigma[i] == j
                    for i in range(4) for j in range(4)))


def main():
    os.sched_setaffinity(0, {1})
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    cpu0, wall0 = time.process_time(), time.monotonic()
    all_rows = tuple(r for r in product(range(4), repeat=4) if sum(r) == 3)
    domains = [tuple(r for r in all_rows if r[i] <= 1) for i in range(4)]
    assert len(all_rows) == 20 and all(len(d) == 16 for d in domains)
    labelled, pairs = 0, 0
    representatives, independent_orbits = set(), set()
    for c in product(*domains):
        if any(sum(c[i][j] for i in range(4)) != 3 for j in range(4)):
            continue
        labelled += 1
        pairs += sum(compatible(c, sigma) for sigma in PERMS)
        representatives.add(min(relabel(c, p) for p in PERMS))
        # Independent row/column equivalence is NOT used to reduce the
        # actual matching-preserving (C,sigma) domain.
        independent_orbits.add(min(tuple(sorted(tuple(row[j] for j in p)
                                                   for row in c))
                                   for p in PERMS))
    records = []
    for c in sorted(representatives):
        stabilizer = [p for p in PERMS if relabel(c, p) == c]
        allowed = [sigma for sigma in PERMS if compatible(c, sigma)]
        sigma_reps = sorted({min(conjugate(sigma, p) for p in stabilizer)
                             for sigma in allowed})
        records.append(dict(C=c, labelled_compatible_permutations=len(allowed),
                            sigma_representatives=sigma_reps,
                            stabilizer_size=len(stabilizer)))
    base = tuple(tuple(int(i != j) for j in range(4)) for i in range(4))
    witness = dict(C=base, sigma=tuple(range(4)),
                   z_cells=[((i+1) % 4, (i+2) % 4) for i in range(4)],
                   scope='A partial necessary-interface assignment only; not a full graph')
    assert compatible(base, witness['sigma'])
    for i, (j, k) in enumerate(witness['z_cells']):
        assert j != i and k != i and base[j][k]+1-int(j == k) > 0
    result = dict(status='COMPLETE_NECESSARY_INTERFACE_DOMAIN', complete=True,
                  row_domain_sizes=[len(d) for d in domains],
                  full_row_cartesian_domain=16**4,
                  labelled_C_matrices=labelled,
                  C_simultaneous_permutation_orbits=len(representatives),
                  C_independent_row_column_orbits_diagnostic=len(independent_orbits),
                  labelled_compatible_C_sigma_pairs=pairs,
                  simultaneous_C_sigma_orbits=sum(len(x['sigma_representatives']) for x in records),
                  records=records, zero_trace_D_in_R_partial_assignment=witness,
                  scope='Necessary finite domain only; no A/B completion, no graph and no exclusion',
                  equivalence='Simultaneous U/V relabeling preserving fixed A matching; side interchange not quotiented',
                  cpu_seconds=time.process_time()-cpu0,
                  wall_seconds=time.monotonic()-wall0)
    Path(__file__).with_suffix('.result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('records','zero_trace_D_in_R_partial_assignment')},indent=2))


if __name__ == '__main__':
    main()
