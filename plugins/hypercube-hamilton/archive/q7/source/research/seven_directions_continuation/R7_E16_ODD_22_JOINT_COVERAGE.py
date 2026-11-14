"""Bounded joint two-return coverage for the E16 odd (2,2) profile."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_E16_CONTROLLED_SINGLE_ROOT_FIXED_PROBE import receiver_gate
from R7_E16_ODD_22_WHOLE_FACE_PROBE import AXES, PAIRS, TRIPLES, UNITS, face, group, image, whole_face_gate


HERE = Path(__file__).resolve().parent
CPU_LIMIT = 20
REP_LIMIT = 2000
IMPORTS = (
    'R7_E16_ODD_MU4_WEIGHT_REDUCTION.md',
    'R7_E16_ODD_MU4_WEIGHT_REDUCTION_REVIEW.json',
    'R7_CONTROLLED_TWO_RETURN_BRIDGE.md',
    'R7_DELTA2_DISTANCE2_REVIEW.json',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS.md',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.json',
    'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT.md',
    'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT_REVIEW.json',
    'R7_E16_ODD_22_WHOLE_FACE_PROBE.py',
    'R7_E16_CONTROLLED_SINGLE_ROOT_FIXED_PROBE.py',
)


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def orbit_representatives(actions, start):
    covered = set()
    for pair in PAIRS:
        if pair not in covered:
            check_time(start)
            covered.update(image(pair, action) for action in actions)
            yield pair


def find_plan(odd, even, loads, stats, start):
    colors = (even, odd)
    holes = set(even + odd)
    for outer in AXES:
        if loads[outer] != 4:
            continue
        outer_bit = 1 << outer
        for side in (0, 1):
            a_colors = tuple(face(g, outer, side) for g in colors)
            beta = int(len(a_colors[1]) > len(a_colors[0]))
            alpha = 1 - beta
            a_min, a_maj = a_colors[alpha], a_colors[beta]
            b_min = face(colors[beta], outer, 1 - side)
            b_maj = face(colors[alpha], outer, 1 - side)
            assert len(a_maj) - len(a_min) == len(b_maj) - len(b_min) == 4
            stats['directed_cuts_tested'] += 1
            for X in combinations(a_maj, 2):
                Y = tuple(sorted(x ^ outer_bit for x in X))
                a_kept = tuple(x for x in a_maj if x not in X)
                for U in combinations(b_maj, 2):
                    check_time(start)
                    stats['source_pairs_tested'] += 1
                    V = tuple(sorted(u ^ outer_bit for u in U))
                    assert set(Y + V).isdisjoint(holes)
                    new_a_maj = tuple(sorted(a_kept + V))
                    supplier = whole_face_gate(a_min, new_a_maj, V, outer)
                    if supplier is None:
                        continue
                    stats['supplier_hits'] += 1
                    new_b_maj = tuple(sorted(tuple(x for x in b_maj if x not in U) + Y))
                    receiver = whole_face_gate(b_min, new_b_maj, Y, outer)
                    if receiver is None:
                        receiver = receiver_gate(b_min, new_b_maj, Y, outer)
                        if receiver is None:
                            continue
                        assert receiver['a'] in b_min and receiver['w'] not in holes
                        receiver_mode = 'controlled_single_root'
                    else:
                        receiver_mode = 'whole_face'
                    stats['receiver_' + receiver['kind']] += 1
                    return dict(outer=outer, A_side=side, B_side=1 - side,
                                alpha_parity=alpha, beta_parity=beta,
                                original_A_by_alpha_beta=(a_min, a_maj),
                                original_B_by_alpha_beta=(b_maj, b_min), X=X, U=U, Y=Y, V=V,
                                H_prime_A=sorted(a_min + new_a_maj), H_prime_B=sorted(b_min + new_b_maj),
                                H_prime_A_by_alpha_beta=(a_min, new_a_maj),
                                H_prime_B_by_alpha_beta=(new_b_maj, b_min), supplier=supplier,
                                receiver_mode=receiver_mode, receiver=receiver)
    return None


def run():
    start = process_time()
    rows = []
    cases = []
    first_failure = None
    status = 'complete'
    try:
        for p, q in ((0, 0), (0, 1)):
            check_time(start)
            actions = tuple(group({p, q}))
            stats = Counter()
            cases.append(dict(p=p, q=q, group_size=len(actions), counts=stats))
            for pair_l in orbit_representatives(actions, start):
                stats['L_reps'] += 1
                stabilizer = tuple(action for action in actions if image(pair_l, action) == pair_l)
                for pair_v in orbit_representatives(stabilizer, start):
                    stats['paired_reps_before_filter'] += 1
                    L = tuple(e for e in UNITS if e != 1 << p) + pair_l
                    V = tuple(e for e in UNITS if e != 1 << q) + pair_v
                    loads = tuple(sum(bool(x & e) for x in L + V) for e in UNITS)
                    if max(loads) > 4:
                        stats['excluded_load'] += 1
                        continue
                    if any(not x & y for x in pair_l for y in pair_v):
                        stats['excluded_cross_intersection'] += 1
                        continue
                    if len(rows) >= REP_LIMIT:
                        status = 'representative_limit'
                        break
                    stats['eligible_reps_tested'] += 1
                    odd, even = tuple(sorted(L)), tuple(sorted(127 ^ y for y in V))
                    assert all((x ^ y).bit_count() >= 3 for x in odd for y in even)
                    assert sum(loads) == 24 and max(loads) == 4
                    counters = Counter()
                    geometry = dict(p=p, q=q, L_triples=pair_l, V_triples=pair_v, L=sorted(L), V=sorted(V),
                                    odd_holes=odd, even_holes=even, column_loads=loads, plan_counts=counters)
                    plan = find_plan(odd, even, loads, counters, start)
                    stats.update(counters)
                    if plan is None:
                        status, first_failure = 'first_gate_failure', geometry
                        break
                    stats['positive_reps'] += 1
                    rows.append(dict(geometry, plan=plan))
                if status != 'complete':
                    break
            if status != 'complete':
                break
        check_time(start)
    except TimeoutError:
        status = 'cpu_limit'
    return dict(status=status, cpu_seconds=process_time() - start, cpu_limit_seconds=CPU_LIMIT,
                eligible_representative_limit=REP_LIMIT, raw_triple_points=len(TRIPLES),
                raw_pairs_per_group=len(PAIRS), cases=cases, positive_count=len(rows),
                first_failure=first_failure, rows=rows if status == 'complete' else [],
                original_matching_enumerations=0, solver_calls=0, rank_runs=0,
                imported_hashes={name: sha256((HERE / name).read_bytes()).hexdigest() for name in IMPORTS})


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key not in ('rows', 'imported_hashes')}))
