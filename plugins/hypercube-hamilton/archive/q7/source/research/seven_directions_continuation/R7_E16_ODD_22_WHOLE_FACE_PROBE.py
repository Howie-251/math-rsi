"""Bounded (2,2) odd-group probe for two whole-face return-bridge gates."""

from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations
import json
from pathlib import Path
from time import process_time


HERE = Path(__file__).resolve().parent
CPU_LIMIT = 30
REP_LIMIT = 2000
AXES = tuple(range(7))
UNITS = tuple(1 << i for i in AXES)
TRIPLES = sorted(sum(bits) for bits in combinations(UNITS, 3))
PAIRS = tuple(combinations(TRIPLES, 2))
IMPORTS = (
    'R7_E16_ODD_MU4_WEIGHT_REDUCTION.md',
    'R7_E16_ODD_MU4_WEIGHT_REDUCTION_REVIEW.json',
    'R7_CONTROLLED_TWO_RETURN_BRIDGE.md',
    'R7_DELTA2_DISTANCE2_REVIEW.json',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS.md',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.json',
)


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def group(fixed):
    free = tuple(i for i in AXES if i not in fixed)
    for perm in permutations(free):
        axis = dict(zip(free, perm))
        yield {x: sum(1 << axis.get(i, i) for i in AXES if x & (1 << i)) for x in TRIPLES}


def image(pair, action):
    return tuple(sorted(action[x] for x in pair))


def orbit_reps(actions, start):
    covered = set()
    for pair in PAIRS:
        if pair not in covered:
            check_time(start)
            covered.update(image(pair, action) for action in actions)
            yield pair


def face(points, axis, side):
    return tuple(x for x in points if ((x >> axis) & 1) == side)


def whole_face_gate(minority, majority, marks, outer):
    for inner in AXES:
        if inner == outer:
            continue
        side = (marks[0] >> inner) & 1
        if (marks[1] >> inner) & 1 != side:
            continue
        s, a = len(face(minority, inner, side)), len(face(majority, inner, side))
        t, b = len(minority) - s, len(majority) - a
        if s in (0, 1) and a == s + 5 and 1 <= t <= 16 and b == t - 1:
            kind = 'majority_root'
        elif (s, a) == (2, 5) and 0 <= t <= 15 and b == t + 1:
            kind = 'two_minority_roots'
        else:
            continue
        return dict(kind=kind, inner=inner, mark_side=side, hole_counts=((s, a), (t, b)))
    return None


def whole_plan(odd, even, loads, stats, start):
    colors = (even, odd)
    for outer in AXES:
        if loads[outer] != 4:
            continue
        check_time(start)
        for side in (0, 1):
            a_colors = tuple(face(g, outer, side) for g in colors)
            a_major_color = int(len(a_colors[1]) > len(a_colors[0]))
            a_major, a_minor = a_colors[a_major_color], a_colors[1 - a_major_color]
            b_major, b_minor = face(colors[1 - a_major_color], outer, 1 - side), face(colors[a_major_color], outer, 1 - side)
            assert len(a_major) - len(a_minor) == len(b_major) - len(b_minor) == 4
            stats['directed_cuts_tested'] += 1
            bit = 1 << outer
            for X in combinations(a_major, 2):
                check_time(start)
                Y = tuple(sorted(x ^ bit for x in X))
                a_kept = tuple(x for x in a_major if x not in X)
                for U in combinations(b_major, 2):
                    stats['source_pairs_tested'] += 1
                    marks_a = tuple(sorted(u ^ bit for u in U))
                    assert set(marks_a + Y).isdisjoint(even + odd)
                    b_kept = tuple(u for u in b_major if u not in U)
                    supply = whole_face_gate(a_minor, a_kept + marks_a, marks_a, outer)
                    receive = whole_face_gate(b_minor, b_kept + Y, Y, outer)
                    stats['donor_hits'] += supply is not None
                    stats['receiver_hits'] += receive is not None
                    if supply is not None and receive is not None:
                        return dict(outer=outer, donor_side=side, donor_majority_parity=a_major_color,
                                    X=X, U=U, donor_minor=a_minor, donor_kept=a_kept, donor_marks=marks_a,
                                    receiver_minor=b_minor, receiver_kept=b_kept, receiver_marks=Y,
                                    donor=supply, receiver=receive)
    return None


def run():
    start = process_time()
    cases = []
    positives = []
    failure = None
    status = 'complete'
    try:
        for p, q in ((0, 0), (0, 1)):
            actions = tuple(group({p, q}))
            stats = Counter()
            cases.append(dict(p=p, q=q, group_size=len(actions), visited_counts=stats))
            for pair_l in orbit_reps(actions, start):
                stats['L_reps'] += 1
                stabilizer = tuple(action for action in actions if image(pair_l, action) == pair_l)
                for pair_v in orbit_reps(stabilizer, start):
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
                    if len(positives) >= REP_LIMIT:
                        status = 'representative_limit'
                        break
                    stats['eligible_reps_tested'] += 1
                    odd, even = sorted(L), sorted(127 ^ y for y in V)
                    counters = Counter()
                    geometry = dict(p=p, q=q, L_triples=pair_l, V_triples=pair_v, L=sorted(L), V=sorted(V),
                                    odd=odd, even=even, column_loads=loads, plan_counts=counters)
                    plan = whole_plan(tuple(odd), tuple(even), loads, counters, start)
                    stats.update(counters)
                    if plan is None:
                        status, failure = 'first_gate_failure', geometry
                        break
                    positives.append(dict(geometry, plan=plan))
                    stats['positive_reps'] += 1
                if status != 'complete':
                    break
            if status != 'complete':
                break
    except TimeoutError:
        status = 'cpu_limit'
    return dict(status=status, cpu_seconds=process_time() - start, cpu_limit_seconds=CPU_LIMIT,
                representative_limit=REP_LIMIT, raw_triple_points=len(TRIPLES), raw_pairs_per_group=len(PAIRS),
                cases=cases, positive_count=len(positives), first_failure=failure,
                positive_rows=positives if status == 'complete' else [],
                imported_hashes={name: sha256((HERE / name).read_bytes()).hexdigest() for name in IMPORTS})


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key != 'positive_rows'}))
