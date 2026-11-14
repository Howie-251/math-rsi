"""Bounded odd (2,2) check with the audited exact core 117 supplier."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_E16_CONTROLLED_SINGLE_ROOT_FIXED_PROBE import receiver_gate
from R7_E16_ODD_22_JOINT_COVERAGE import CPU_LIMIT, REP_LIMIT, check_time, orbit_representatives
from R7_E16_ODD_22_POSITIVE_SPLIT_FIXED_PROBE import positive_split
from R7_E16_ODD_22_WHOLE_FACE_PROBE import AXES, PAIRS, TRIPLES, UNITS, face, group, image, whole_face_gate


HERE = Path(__file__).resolve().parent
SOURCE = 'R7_E16_ODD_22_JOINT_COVERAGE.json'
RESEARCH = Path('E:/新问题/research/seven_directions')
IMPORTS = (
    SOURCE, 'R7_E16_ODD_22_JOINT_COVERAGE.py', 'R7_E16_ODD_22_WHOLE_FACE_PROBE.py',
    'R7_E16_ODD_22_POSITIVE_SPLIT_FIXED_PROBE.py', 'R7_E16_CONTROLLED_SINGLE_ROOT_FIXED_PROBE.py',
    'R7_E16_ODD_MU4_WEIGHT_REDUCTION.md', 'R7_E16_ODD_MU4_WEIGHT_REDUCTION_REVIEW.json',
    'R7_CONTROLLED_TWO_RETURN_BRIDGE.md', 'R7_DELTA2_DISTANCE2_REVIEW.json',
    'R7_CONTROLLED_CYCLE_DONOR_TRANSFER.md', 'R7_MU3_CONTROLLED_AND_T63_REVIEW.json',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS.md', 'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.json',
    'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT.md', 'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT_REVIEW.json',
)
EXTERNAL = ('R7_TWELVE_HOLE_STAR_HIGH_FOUR_BRIDGES.md', 'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json',
            'Q6_T15_ACTUAL_PROFILE.json')


def project(x, axes):
    return sum(((x >> i) & 1) << j for j, i in enumerate(axes))


def permute(x, permutation):
    return sum(((x >> i) & 1) << j for i, j in enumerate(permutation))


def core117(minority, retained, marks, outer):
    if len(minority) != 1 or len(retained) != 3 or len(marks) != 2:
        return None
    root = minority[0]
    axes = tuple(i for i in AXES if i != outer)
    included, omitted = [sorted(project(x ^ root, axes) for x in points) for points in (retained, marks)]
    missing = {63 ^ x for x in included}
    if any(x.bit_count() != 1 for x in missing) or not set(omitted) <= missing:
        return None
    remaining, = missing - set(omitted)
    source_units = [*reversed(omitted), *[x for x in UNITS[:6] if x not in missing], remaining]
    permutation = [source_units.index(x) for x in UNITS[:6]]
    assert sorted(permute(x, permutation) for x in included) == [31, 61, 62]
    assert sorted(permute(x, permutation) for x in omitted) == [1, 2]
    return dict(kind='core117', root=root, projected_axes=axes, normalized_retained=included,
                normalized_marks=omitted, coordinate_transport=permutation)


def get_plan(colors, outer, side, X, U, counters, fixed=False):
    a_colors = tuple(face(g, outer, side) for g in colors)
    beta = int(len(a_colors[1]) > len(a_colors[0]))
    alpha = 1 - beta
    a_min, a_maj = a_colors[alpha], a_colors[beta]
    b_min = face(colors[beta], outer, 1 - side)
    b_maj = face(colors[alpha], outer, 1 - side)
    assert len(a_maj) - len(a_min) == len(b_maj) - len(b_min) == 4
    assert set(X) <= set(a_maj) and set(U) <= set(b_maj)
    bit = 1 << outer
    Y, V = (tuple(sorted(x ^ bit for x in chosen)) for chosen in (X, U))
    assert set(Y + V).isdisjoint(colors[0] + colors[1])
    a_kept = tuple(x for x in a_maj if x not in X)
    new_a_maj = tuple(sorted(a_kept + V))
    supplier = core117(a_min, a_kept, V, outer) if fixed else whole_face_gate(a_min, new_a_maj, V, outer)
    if supplier is None and not fixed:
        supplier = core117(a_min, a_kept, V, outer)
    if supplier is None:
        return None
    counters['supplier_' + supplier['kind']] += 1

    new_b_maj = tuple(sorted(tuple(x for x in b_maj if x not in U) + Y))
    receiver = None if fixed else whole_face_gate(b_min, new_b_maj, Y, outer)
    if receiver is not None:
        receiver = dict(mode='whole_face', **receiver)
    else:
        receiver = None if fixed else positive_split(b_min, new_b_maj, Y, outer)
        if receiver is None:
            receiver = receiver_gate(b_min, new_b_maj, Y, outer)
            if receiver is None:
                return None
            receiver = dict(mode='controlled_single_root', **receiver)
    counters['receiver_' + receiver['mode']] += 1
    return dict(outer=outer, A_side=side, B_side=1 - side, alpha_parity=alpha, beta_parity=beta,
                X=X, U=U, Y=Y, V=V, H_prime_A=sorted(a_min + new_a_maj),
                H_prime_B=sorted(b_min + new_b_maj), H_prime_A_by_alpha_beta=(a_min, new_a_maj),
                H_prime_B_by_alpha_beta=(new_b_maj, b_min), supplier=supplier, receiver=receiver)


def find_plan(colors, loads, counters, start):
    for outer in AXES:
        if loads[outer] != 4:
            continue
        for side in (0, 1):
            a_colors = tuple(face(g, outer, side) for g in colors)
            beta = int(len(a_colors[1]) > len(a_colors[0]))
            b_maj = face(colors[1 - beta], outer, 1 - side)
            counters['directed_cuts_tested'] += 1
            for X in combinations(a_colors[beta], 2):
                for U in combinations(b_maj, 2):
                    check_time(start)
                    counters['source_pairs_tested'] += 1
                    plan = get_plan(colors, outer, side, X, U, counters)
                    if plan is not None:
                        return plan
    return None


def fixed_plan():
    input_data = json.loads((HERE / SOURCE).read_bytes())
    assert input_data['status'] == 'first_gate_failure'
    row = input_data['first_failure']
    assert (row['p'], row['q'], row['L_triples'], row['V_triples']) == (0, 0, [7, 11], [49, 81])
    colors = tuple(tuple(row[name]) for name in ('even_holes', 'odd_holes'))
    plan = get_plan(colors, 1, 0, (4, 8), (63, 95), Counter(), fixed=True)
    assert plan is not None and plan['supplier']['coordinate_transport'] == [2, 3, 4, 5, 1, 0]
    assert (plan['Y'], plan['V']) == ((6, 10), (61, 93))
    rec = plan['receiver']
    assert (rec['kind'], rec['inner'], rec['Z_side'], rec['a'], rec['w']) == ('same_side', 0, 0, 2, 3)
    return dict(even_holes=colors[0], odd_holes=colors[1], plan=plan)


def run():
    start = process_time()
    reviewed = json.loads((RESEARCH / EXTERNAL[1]).read_bytes())
    registry = json.loads((RESEARCH / EXTERNAL[2]).read_bytes())
    target = next(x for x in registry['orbits'] if x['index'] == 117)
    assert reviewed['verdict'] == 'PASS' and 117 in reviewed['union_closed_core_indices']
    assert (target['included'], target['omitted']) == ([31, 61, 62], [1, 2])
    fixed = fixed_plan()
    rows, cases = [], []
    failure, status = None, 'complete'
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
                    colors = (tuple(sorted(127 ^ y for y in V)), tuple(sorted(L)))
                    assert sum(loads) == 24 and max(loads) == 4
                    assert all((a ^ b).bit_count() >= 3 for a in colors[0] for b in colors[1])
                    counters = Counter()
                    geometry = dict(p=p, q=q, L_triples=pair_l, V_triples=pair_v, L=sorted(L), V=sorted(V),
                                    even_holes=colors[0], odd_holes=colors[1], column_loads=loads, plan_counts=counters)
                    plan = find_plan(colors, loads, counters, start)
                    stats.update(counters)
                    if plan is None:
                        status, failure = 'first_gate_failure', geometry
                        break
                    stats['positive_reps'] += 1
                    stats['selected_supplier_' + plan['supplier']['kind']] += 1
                    rows.append(dict(geometry, plan=plan))
                if status != 'complete':
                    break
            if status != 'complete':
                break
        check_time(start)
    except TimeoutError:
        status = 'cpu_limit'
    paths = [*((name, HERE / name) for name in IMPORTS), *((str(RESEARCH / name), RESEARCH / name) for name in EXTERNAL)]
    return dict(status=status, cpu_seconds=process_time() - start, cpu_limit_seconds=CPU_LIMIT,
                eligible_representative_limit=REP_LIMIT, raw_triple_points=len(TRIPLES),
                raw_pairs_per_group=len(PAIRS), fixed_plan=fixed, cases=cases, positive_count=len(rows),
                first_failure=failure, rows=rows, original_matching_enumerations=0, solver_calls=0,
                rank_runs=0, imported_hashes={name: sha256(file.read_bytes()).hexdigest() for name, file in paths})


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key not in ('rows', 'imported_hashes')}))
