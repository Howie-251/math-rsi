"""Bounded 246/444 central-cut completion and audited gate checks."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

import R7_E16_CENTRAL_LOCAL_REDUCTION as local
from R7_E16_CENTRAL_SOURCE_CONSTRAINTS import branch_pools, constraints, load
from R7_E16_CONTROLLED_SINGLE_ROOT_FIXED_PROBE import receiver_gate
from R7_E16_ODD_22_WHOLE_FACE_PROBE import whole_face_gate
import R7_E16_TWO_HOLE_HIGH_FACE_COVERAGE as old_gates
from R7_E16_TWO_HOLE_HIGH_FACE_JOINT_COVERAGE import controlled_count


HERE = Path(__file__).resolve().parent
OUTPUT = Path(__file__).with_suffix('.json')
LOCAL = 'R7_E16_CENTRAL_LOCAL_REDUCTION.json'
LOCAL_HASH = '24125592d30e7c450145df69209c34f52757c4eb8c8a8a5088f121ceaa8ca3cd'
SOURCE = 'R7_E16_CENTRAL_SOURCE_CONSTRAINTS.json'
SOURCE_HASH = 'f053c2996267b30cf97dabc9917f173f83410f00e082a7d1cb57fe7a76df0770'
TARGETS = (('246', 9), ('444', 20), ('444', 21))
AXES = tuple(range(7))
CPU_LIMIT = 17  # Reserve three seconds for the aborted invocation of the legacy helper.
REP_LIMIT = 3000


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def read_frozen(name, digest):
    raw = (HERE / name).read_bytes()
    assert sha256(raw).hexdigest() == digest
    return json.loads(raw)


def source_candidates(kind, index):
    if kind == '246':
        assert index == 9
        return {tuple(sorted((1, 2, 32, 35, x))) for x in (4, 7, 37, 38)}
    if index == 20:
        return {(1, 2, 7, 11, 19)}
    assert index == 21
    units = (1, 4, 8, 16, 32)
    supports = [units]
    supports.extend((0, *(u for u in units if u != omit)) for omit in units)
    supports.extend((0, u | v, *(w for w in units if w not in (u, v))) for u, v in combinations(units, 2))
    return {tuple(sorted((x | ((x.bit_count() % 2) << 1)) ^ 1 for x in five)) for five in supports}


def valid_source(y, t, constant, fixed, sparse):
    return (len(set(y)) == 5 and all(x.bit_count() % 2 == 1 and x not in t for x in y)
            and all(load(y, 1 << i, 1) in (0, 5) for i in constant)
            and all(load(y, 1 << i, side) == 5 for i, side in fixed)
            and all(load(y, 1 << i, side) <= 1 for i, side in sparse))


def image(points, action):
    return tuple(sorted(action[p] for p in points))


def orbit_reps(items, actions, start):
    remaining = set(items)
    while remaining:
        check_time(start)
        rep = min(remaining)
        images = {image(rep, action) for action in actions}
        assert images <= remaining
        remaining.difference_update(images)
        yield rep, len(images)


def basis(start, records, result):
    local_data = read_frozen(LOCAL, LOCAL_HASH)
    source_data = read_frozen(SOURCE, SOURCE_HASH)
    assert source_data['frozen_sha256'] == LOCAL_HASH and local_data['status'] == 'complete'
    source = {(row['distance_type'], row['local_index']): row for row in source_data['rows']}
    local.CPU_LIMIT = CPU_LIMIT
    maps = tuple(local.permutation_maps(start))
    for kind, expected in (('246', 21), ('444', 22)):
        block = next(row for row in local_data['rows'] if row['distance_type'] == kind)
        s = tuple(block['S'])
        assert len(block['representatives']) == expected
        actions_s = local.stabilizer(s, maps, start)
        for index, receiver in enumerate(block['representatives']):
            key = kind, index
            row = source[key]
            t = tuple(receiver['T'])
            assert tuple(row['S']) == s and tuple(row['T']) == t
            condition = constraints(s, t)
            assert json.dumps(condition) == json.dumps(tuple(row[k] for k in ('constant', 'fixed', 'sparse')))
            if key not in TARGETS:
                pools, reason, _ = branch_pools(t, *condition)
                assert not pools and row['status'] == 'completed' and not row['representatives']
                records['zero_Y_' + kind] += 1
                records['zero_reason_' + reason] += 1
                continue
            raw_y = source_candidates(kind, index)
            ys = {y for y in raw_y if valid_source(y, t, *condition)}
            actions_st = tuple(action for action in actions_s if image(t, action) == t)
            summary = {'distance_type': kind, 'local_index': index, 'raw_source_sets': len(raw_y),
                       'eligible_labelled_Y': len(ys), 'stabilizer_ST': len(actions_st), 'Y_rows': []}
            records['local_rows'].append(summary)
            for y, y_orbit in orbit_reps(ys, actions_st, start):
                u_pool = tuple(u for u in range(64) if u.bit_count() % 2 == 0 and u not in s
                               and all((u ^ x).bit_count() != 1 for x in y))
                actions_sty = tuple(action for action in actions_st if image(y, action) == y)
                u_rows = list(orbit_reps(combinations(u_pool, 3), actions_sty, start))
                summary['Y_rows'].append({'Y': y, 'Y_orbit_size': y_orbit, 'U_pool': u_pool,
                                          'stabilizer_STY': len(actions_sty), 'U_representatives': len(u_rows),
                                          'labelled_U_count': sum(size for _, size in u_rows)})
                for u, _ in u_rows:
                    if len(result) >= REP_LIMIT:
                        raise OverflowError
                    even = tuple(sorted((*s, *(64 ^ p for p in y))))
                    odd = tuple(sorted((*t, *(64 ^ p for p in u))))
                    assert len(even) == len(odd) == 8 and all((a ^ b).bit_count() != 1 for a in even for b in odd)
                    result.append({'distance_type': kind, 'local_index': index, 'S': s, 'T': t, 'Y': y, 'U': u,
                                   'even_holes': even, 'odd_holes': odd})


def two_hole_full(colors):
    for outer in AXES:
        for side in (0, 1):
            for alpha in (0, 1):
                shape = tuple(len(old_gates.face(colors[i], outer, side)) for i in (alpha, 1 - alpha))
                if shape == (6, 8):
                    return {'gate': 'E16_two_hole_full', 'outer': outer, 'A_side': side,
                            'alpha_parity': alpha, 'shape': ((6, 8), (2, 0))}
    return None


def balanced_half_receiver(minority, majority, y, outer):
    face = old_gates.face
    for inner in AXES:
        if inner == outer:
            continue
        for side in (0, 1):
            ms = len(face(minority, inner, side))
            if len(face(y, inner, side)) == 2 and ms <= 1 and len(face(majority, inner, side)) == ms + 2:
                if len(minority) - ms >= 1:
                    return {'kind': 'balanced_half_omission', 'inner': inner, 'marked_side': side,
                            'marked_side_original_minority': ms}
    return None


def original_double_bridge(colors, start):
    face = old_gates.face
    for outer in AXES:
        for side in (0, 1):
            a = tuple(face(group, outer, side) for group in colors)
            beta = int(len(a[1]) > len(a[0]))
            alpha = 1 - beta
            r = len(a[alpha])
            if r > 5 or len(a[beta]) - r != 2:
                continue
            b_min = face(colors[beta], outer, 1 - side)
            b_major = face(colors[alpha], outer, 1 - side)
            for x in combinations(a[beta], 2):
                check_time(start)
                y = tuple(sorted(p ^ (1 << outer) for p in x))
                new_major = tuple(sorted(b_major + y))
                gate = receiver_gate(b_min, new_major, y, outer)
                if gate is not None:
                    mode = 'single_root'
                else:
                    gate = whole_face_gate(b_min, new_major, y, outer)
                    mode = 'whole_face'
                if gate is None:
                    gate = balanced_half_receiver(b_min, b_major, y, outer)
                    mode = 'balanced_half_omission'
                if gate is not None:
                    return {'gate': 'original_double_bridge', 'outer': outer, 'A_side': side, 'alpha_parity': alpha,
                            'r': r, 'X': x, 'Y': y, 'B_original_minority': b_min,
                            'B_original_majority': b_major, 'receiver_mode': mode, 'receiver': gate}
    return None


def run():
    start = process_time()
    records = Counter()
    records['local_rows'] = []
    targets, positive, impossible = [], [], []
    gate_counts = Counter()
    status = 'complete'
    phase = 'finite_basis'
    failure, current = None, None
    old_gates.broad_returns.CPU_LIMIT = CPU_LIMIT
    original_surviving = old_gates.broad_returns.surviving

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else original_surviving(edge, outer, side, omitted)

    old_gates.broad_returns.surviving = surviving_optional
    broad_find = None
    try:
        basis(start, records, targets)
        assert records['zero_Y_246'] == records['zero_Y_444'] == 20
        phase = 'plan_search'
        for current in targets:
            check_time(start)
            colors = current['even_holes'], current['odd_holes']
            plan = (old_gates.counts_orbits(colors) or two_hole_full(colors)
                    or original_double_bridge(colors, start) or controlled_count(colors))
            if plan is None:
                forced, exclusion = old_gates.forced_original_edges(colors)
                if exclusion:
                    gate_counts[exclusion['gate']] += 1
                    impossible.append({**current, 'exclusion': exclusion})
                    continue
                current['forced_edges'] = forced
                loads = tuple(8 - abs(len(old_gates.face(colors[0], j, 1)) -
                                      len(old_gates.face(colors[1], j, 1))) for j in AXES)
                counts = Counter()
                four = old_gates.find_four_return_plan(colors, loads, counts, start)
                if four:
                    plan = {'gate': 'k4_two_return', **four}
                elif max(8 - load for load in loads) >= 4:
                    check_time(start)
                    if broad_find is None:
                        broad_find = old_gates.broad_returns.make_search()
                    sets = tuple(frozenset(group) for group in colors)
                    for edge in forced or (None,):
                        check_time(start)
                        broad, _ = broad_find(sets, edge, start)
                        if broad:
                            plan = {'gate': 'registry_two_return', 'forced_edge': edge, **broad}
                            break
                if plan is None:
                    failure = {**current, 'k4_counters': dict(counts),
                               'bit_one_abs_gaps': tuple(8 - load for load in loads)}
                    status = 'first_joint_gate_failure'
                    break
            gate_counts[plan['gate']] += 1
            positive.append({**current, 'plan': plan})
        check_time(start)
    except TimeoutError:
        status = 'cpu_limit'
    except OverflowError:
        status = 'representative_limit'
    return {'status': status, 'phase': phase, 'cpu_seconds': process_time() - start, 'cpu_limit_seconds': CPU_LIMIT,
            'representative_limit': REP_LIMIT, 'basis_counts': dict(records), 'basis_size': len(targets),
            'completed_count': len(positive) + len(impossible) + int(failure is not None),
            'positive_count': len(positive), 'impossible_count': len(impossible), 'gate_counts': dict(gate_counts),
            'positive': positive, 'impossible': impossible, 'first_failure': failure,
            'in_progress_at_timeout': current if status == 'cpu_limit' else None,
            'input_sha256': {LOCAL: LOCAL_HASH, SOURCE: SOURCE_HASH}, 'original_matching_enumerations': 0,
            'matching_solver_calls': 0, 'hamilton_solver_calls': 0, 'rank_runs': 0}


if __name__ == '__main__':
    receipt = run()
    OUTPUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in receipt.items() if key not in ('positive', 'impossible')}))
