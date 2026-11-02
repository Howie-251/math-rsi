"""SUPERSEDED / UNRUN: prepared screen, never executed; no result file exists.

The root stopped this pending experiment after a stronger analytic route
became available.  Retain this source as preparation history, not evidence
of an enumeration.  Do not execute it under the former authorization.

Exact necessary spectral screen for the (12,21,28) defect-component type.

Six matching pairs index the coordinates of the S=+1 space.  A C_(4k)
block of X selects three pairs on each parity; its balanced sign vector
epsilon is defined up to sign.  For pair-constant x with sum(x)=0, the
lifted vector has norm squared 2||x||^2 and the block contributes
k*(epsilon.x)^2 to ||X^T x||^2.  Thus M=1/2 sum w epsilon epsilon^T.

The actual row-four nonnegative B1 implies I <= M|1perp <= 9I.
Distinct sign types have inner product +/-2, whereas self product is 6.
The Rayleigh value in a type of aggregate weight w is (8w+7)/3, so w>=3
is impossible.  This leaves exactly all w in {0,1,2}^10 of total seven.

For B=(e0-e5,...,e4-e5), B^T B=I5+J5.  Both spectral inequalities are
tested by integer PSD of B^T(2M)B-2(I+J) and 18(I+J)-B^T(2M)B.
The fraction-free Schur test is exact, including zero pivots; no floating
point eigenvalue is computed or used.  These are weight templates only,
not complete X/Y/T realizations or a full graph exclusion.
"""
from itertools import combinations, product
from pathlib import Path
from collections import Counter, deque
from functools import reduce
from math import gcd
import json
import os
import resource
import time

START_WALL = time.monotonic()
OUT = Path(__file__).with_suffix('.result.json')


def psd_integer(matrix):
    """PSD iff every positive-pivot Schur complement is PSD.

    A zero diagonal with nonzero row has a negative 2x2 principal minor.
    A zero row can be removed.  For pivot p>0 use p*Arest-c*c^T and
    divide its positive common gcd; both transformations preserve PSD.
    """
    a = [row[:] for row in matrix]
    stage = 0
    while a:
        p = a[0][0]
        if p < 0:
            return False, dict(stage=stage, kind='negative_diagonal', value=p)
        if p == 0:
            for j in range(1, len(a)):
                if a[0][j]:
                    return False, dict(stage=stage, kind='zero_diagonal_nonzero_row', value=a[0][j])
            a = [row[1:] for row in a[1:]]
        else:
            c = a[0][1:]
            a = [[p*a[i+1][j+1]-c[i]*c[j] for j in range(len(c))] for i in range(len(c))]
            divisor = reduce(gcd, (abs(v) for row in a for v in row), 0)
            if divisor > 1:
                a = [[v//divisor for v in row] for row in a]
        stage += 1
    return True, None


def types_and_actions():
    # Fix epsilon[0]=+1; choose its other two positive coordinates.
    types = []
    for pair in combinations(range(1, 6), 2):
        plus = {0, *pair}
        types.append(tuple(1 if i in plus else -1 for i in range(6)))
    lookup = {v:i for i,v in enumerate(types)}
    actions = []
    for i in range(5):
        action = []
        for v in types:
            moved = list(v); moved[i], moved[i+1] = moved[i+1], moved[i]
            if moved[0] < 0: moved = [-x for x in moved]
            action.append(lookup[tuple(moved)])
        assert sorted(action) == list(range(10))
        actions.append(action)
    return types, actions


def transform(w, action):
    result = [0]*10
    for src, dst in enumerate(action): result[dst] = w[src]
    return tuple(result)


def compatibility(w):
    doubles = w.count(2)
    return ['7C4'] + (['C8+5C4'] if doubles >= 1 else []) + (['2C8+3C4'] if doubles >= 2 else [])


def main():
    os.sched_setaffinity(0, {1})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    assert not OUT.exists(), 'One authorized complete screen; preserve prior result'
    types, actions = types_and_actions()
    assert len(types) == 10 and all(sum(v) == 0 for v in types)
    assert all(abs(sum(x*y for x,y in zip(types[i],types[j]))) == 2
               for i in range(10) for j in range(i))
    contrasts = [[v[i]-v[5] for i in range(5)] for v in types]
    outer = [[[v[i]*v[j] for j in range(5)] for i in range(5)] for v in contrasts]
    domain = [w for w in product(range(3), repeat=10) if sum(w) == 7]
    assert len(domain) == 4740
    survivors = []
    rejected = []
    lower_pass = 0
    examined = 0
    counts = Counter()
    complete = True
    for w in domain:
        if time.process_time() >= 9:
            complete = False
            break
        k = [[sum(w[t]*outer[t][i][j] for t in range(10)) for j in range(5)] for i in range(5)]
        low = [[k[i][j]-2*(1+(i==j)) for j in range(5)] for i in range(5)]
        upper = [[18*(1+(i==j))-k[i][j] for j in range(5)] for i in range(5)]
        ok, why = psd_integer(low)
        examined += 1
        if ok:
            lower_pass += 1
            ok, why = psd_integer(upper)
            bound = 'upper'
        else:
            bound = 'lower'
        if ok:
            survivors.append(w)
            counts['survive_with_'+str(w.count(2))+'_double_weights'] += 1
        else:
            counts[bound+'_fail'] += 1
            rejected.append(dict(weights=w, failed_bound=bound, exact_failure=why))
    survivor_set = set(survivors)
    unseen = set(survivors)
    orbits = []
    orbit_complete = complete
    if complete:
        while unseen:
            if time.process_time() >= 9:
                orbit_complete = False
                break
            representative = min(unseen)
            queue = deque([representative]); members = {representative}; unseen.remove(representative)
            while queue:
                w = queue.popleft()
                for action in actions:
                    nxt = transform(w, action)
                    assert nxt in survivor_set, 'Spectral test must be S6 invariant'
                    if nxt not in members:
                        members.add(nxt); unseen.remove(nxt); queue.append(nxt)
            orbits.append(dict(representative=representative, orbit_size=len(members),
                               number_weight_two=representative.count(2),
                               support_size=sum(x>0 for x in representative),
                               compatible_cycle_decompositions=compatibility(representative)))
    by_family = {name:sum(name in compatibility(w) for w in survivors)
                 for name in ['2C8+3C4','C8+5C4','7C4']}
    # Analytic reference: sum over all ten types gives M=6I-J.  If seven
    # distinct types are selected, the omitted three-vector Gram has
    # diagonal 6 and off-diagonal +/-2, hence eigenvalues <=10.
    # Therefore every such weight vector has I<=M<=6I on 1perp.
    distinct_seven_pass = sum(w.count(1)==7 for w in survivors)
    if complete: assert distinct_seven_pass == 120
    result = dict(status='COMPLETE' if complete and orbit_complete else 'CPU_BOUND_PARTIAL',
        scope='Exact necessary S-plus spectral weight screen for the (12,21,28) quotient; not full X/Y/T realizability',
        complete_weight_enumeration=complete, complete_s6_orbit_classification=orbit_complete,
        domain_definition='ten balanced sign types modulo global sign; weights in {0,1,2}, sum seven',
        total_domain_size=4740, examined=examined, lower_bound_pass=lower_pass,
        both_bounds_pass=len(survivors), counts=dict(counts),
        type_vectors=types, s6_adjacent_transposition_type_actions=actions,
        exact_method='Integer Schur complement PSD on B^T(2M)B-2(I+J) and 18(I+J)-B^T(2M)B; no floats',
        labeled_surviving_weights=survivors, labeled_rejections=rejected,
        s6_orbit_count=len(orbits), s6_orbits=orbits,
        compatible_labeled_weight_counts=by_family,
        compatible_s6_orbit_counts={name:sum(name in o['compatible_cycle_decompositions'] for o in orbits) for name in by_family},
        seven_distinct_types_pass_count=distinct_seven_pass,
        cycle_compatibility_note='A C8 contributes weight two to one type; other weight-two totals may come from two C4 cycles. C12 was excluded analytically by the Rayleigh bound.',
        remaining_obligation='Shared X/Y/T equations, S-minus constraints and entrywise nonnegative actual defect blocks are not tested',
        threads=1, pinned_cpu=1, cpu_limit_seconds=10,
        cpu_seconds=time.process_time(), wall_seconds=time.monotonic()-START_WALL,
        solver_calls=0, graph_searches=0, floating_point_spectral_tests=0)
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
        ['labeled_surviving_weights','labeled_rejections','type_vectors','s6_adjacent_transposition_type_actions']}))


if __name__ == '__main__':
    main()
