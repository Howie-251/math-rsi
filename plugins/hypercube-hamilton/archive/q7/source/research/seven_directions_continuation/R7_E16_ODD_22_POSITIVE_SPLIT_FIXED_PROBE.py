"""Test the audited positive-split receiver for one frozen E16 hole set."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_E16_ODD_22_WHOLE_FACE_PROBE import AXES, face, whole_face_gate


HERE = Path(__file__).resolve().parent
SOURCE = 'R7_E16_ODD_22_JOINT_COVERAGE.json'
CPU_LIMIT = 5
IMPORTS = (
    SOURCE,
    'R7_E16_ODD_22_WHOLE_FACE_PROBE.py',
    'R7_CONTROLLED_TWO_RETURN_BRIDGE.md',
    'R7_DELTA2_DISTANCE2_REVIEW.json',
    'R7_CONTROLLED_CYCLE_DONOR_TRANSFER.md',
    'R7_MU3_CONTROLLED_AND_T63_REVIEW.json',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS.md',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.json',
)


def positive_split(minority, majority, marks, outer):
    for inner in AXES:
        if inner == outer:
            continue
        sides = []
        for side in (0, 1):
            small, large, marked = (face(points, inner, side) for points in (minority, majority, marks))
            if len(marked) != 1 or len(large) - len(small) != 2:
                break
            sides.append(dict(side=side, minority=small, majority=large, marks=marked,
                              hole_counts=(len(small), len(large)), interface='Q5_A_ALL'))
        if len(sides) == 2:
            return dict(inner=inner, mode='positive_split', sides=sides)
    return None


def find_plan(colors, loads, counters, start):
    holes = set(colors[0] + colors[1])
    for outer in AXES:
        if loads[outer] != 4:
            continue
        bit = 1 << outer
        for side in (0, 1):
            a_colors = [face(vertices, outer, side) for vertices in colors]
            beta = int(len(a_colors[1]) > len(a_colors[0]))
            alpha = 1 - beta
            a_min, a_maj = a_colors[alpha], a_colors[beta]
            b_min = face(colors[beta], outer, 1 - side)
            b_maj = face(colors[alpha], outer, 1 - side)
            assert len(a_maj) - len(a_min) == len(b_maj) - len(b_min) == 4
            counters['directed_cuts_visited'] += 1
            for X in combinations(a_maj, 2):
                Y = tuple(sorted(x ^ bit for x in X))
                a_kept = tuple(x for x in a_maj if x not in X)
                for U in combinations(b_maj, 2):
                    if process_time() - start >= CPU_LIMIT:
                        raise TimeoutError
                    counters['source_choices_visited'] += 1
                    V = tuple(sorted(u ^ bit for u in U))
                    assert set(Y + V).isdisjoint(holes)
                    a_majority = tuple(sorted(a_kept + V))
                    supply = whole_face_gate(a_min, a_majority, V, outer)
                    if supply is None:
                        continue
                    counters['old_supplier_hits'] += 1
                    b_majority = tuple(sorted(tuple(x for x in b_maj if x not in U) + Y))
                    receive = positive_split(b_min, b_majority, Y, outer)
                    if receive is None:
                        continue
                    counters['old_supplier_and_positive_split_hits'] += 1
                    return dict(outer=outer, A_side=side, B_side=1 - side,
                                alpha_parity=alpha, beta_parity=beta,
                                original_A_by_alpha_beta=(a_min, a_maj),
                                original_B_by_alpha_beta=(b_maj, b_min), X=X, U=U, Y=Y, V=V,
                                H_prime_A=sorted(a_min + a_majority), H_prime_B=sorted(b_min + b_majority),
                                H_prime_A_by_alpha_beta=(a_min, a_majority),
                                H_prime_B_by_alpha_beta=(b_majority, b_min), supplier=supply, receiver=receive)
    return None


def run():
    start = process_time()
    source = json.loads((HERE / SOURCE).read_bytes())
    assert source['status'] == 'first_gate_failure'
    failure = source['first_failure']
    assert (failure['p'], failure['q'], failure['L_triples'], failure['V_triples']) == (0, 0, [7, 11], [49, 81])
    colors = tuple(tuple(failure[name]) for name in ('even_holes', 'odd_holes'))
    assert len(set(colors[0] + colors[1])) == 16
    assert all((a ^ b).bit_count() != 1 for a in colors[0] for b in colors[1])
    counters = Counter()
    try:
        plan = find_plan(colors, failure['column_loads'], counters, start)
        status = 'first_plan' if plan else 'no_plan'
    except TimeoutError:
        plan, status = None, 'cpu_limit'
    return dict(status=status, fixed_inputs=1, cpu_seconds=process_time() - start,
                cpu_limit_seconds=CPU_LIMIT, realizability_decided=False,
                candidate_supplier_used=False, original_matching_enumerations=0, solver_calls=0,
                first_failure=failure, counters=dict(counters), plan=plan,
                imported_hashes={name: sha256((HERE / name).read_bytes()).hexdigest() for name in IMPORTS})


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key not in ('first_failure', 'imported_hashes')}))
