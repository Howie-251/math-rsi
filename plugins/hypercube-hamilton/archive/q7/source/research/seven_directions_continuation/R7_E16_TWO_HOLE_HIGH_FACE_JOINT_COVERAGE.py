"""Continue the fixed high-face check with the audited controlled cycle-donor count gate."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time

import R7_E16_TWO_HOLE_HIGH_FACE_COVERAGE as old_gates


HERE = Path(__file__).resolve().parent
OUTPUT = Path(__file__).with_suffix('.json')
OLD = 'R7_E16_TWO_HOLE_HIGH_FACE_COVERAGE.json'
OLD_HASH = '41652b9a0f236d39dbb7213372bd169571477129f1311ff1935c32f3951b6222'
AXES = old_gates.AXES
CPU_LIMIT = old_gates.CPU_LIMIT
LIMIT = old_gates.LIMIT


def read_frozen(name, digest):
    raw = (HERE / name).read_bytes()
    assert sha256(raw).hexdigest() == digest
    return json.loads(raw)


def controlled_at(colors, outer, a_side, inner, fixed_sources=None):
    face = old_gates.face
    a_colors = tuple(face(group, outer, a_side) for group in colors)
    beta = int(len(a_colors[1]) > len(a_colors[0]))
    alpha = 1 - beta
    a_min, a_major = a_colors[alpha], a_colors[beta]
    r, k = len(a_min), len(a_major) - len(a_min)
    if r > 5 or k not in (2, 3, 4):
        return None
    b_min = face(colors[beta], outer, 1 - a_side)
    b_major = face(colors[alpha], outer, 1 - a_side)
    candidates = tuple(sorted(x ^ (1 << outer) for x in a_major))
    fixed_marks = None if fixed_sources is None else tuple(sorted(x ^ (1 << outer) for x in fixed_sources))
    if fixed_marks is not None and (len(set(fixed_marks)) != k or not set(fixed_marks) <= set(candidates)):
        return None
    sides = []
    for side in (0, 1):
        minority = face(b_min, inner, side)
        majority = face(b_major, inner, side)
        q = len(majority) - len(minority)
        marks = face(candidates if fixed_marks is None else fixed_marks, inner, side)
        if q == 1:
            interface = 'Q5_A_ALL'
        elif q == 2 and len(minority) in (0, 1):
            interface = 'Q5_T44' if not minority else 'Q5_T15_FULL'
        else:
            return None
        if len(marks) < q or (fixed_marks is not None and len(marks) != q):
            return None
        sides.append({'side': side, 'original_minority': minority, 'original_majority': majority,
                      'marks': marks[:q], 'interface': interface})
    y = tuple(sorted(mark for side in sides for mark in side['marks']))
    x = tuple(sorted(mark ^ (1 << outer) for mark in y))
    assert len(x) == k and not set(y) & set(colors[alpha] + colors[beta])
    return {'gate': 'controlled_cycle_count', 'outer': outer, 'A_side': a_side, 'alpha_parity': alpha,
            'r': r, 'k': k, 'inner': inner, 'X': x, 'Y': y, 'donor_original_minority': a_min,
            'donor_original_majority': a_major, 'receiver_sides': sides}


def controlled_count(colors):
    for outer in AXES:
        for a_side in (0, 1):
            for inner in AXES:
                if inner == outer:
                    continue
                plan = controlled_at(colors, outer, a_side, inner)
                if plan:
                    return plan
    return None


def fixed_plan(colors):
    plan = controlled_at(colors, 0, 1, 2, (7, 31, 59))
    assert plan is not None and (plan['r'], plan['k'], plan['alpha_parity']) == (3, 3, 0)
    assert plan['Y'] == (6, 30, 58)
    assert plan['donor_original_minority'] == (9, 17, 75)
    assert plan['donor_original_majority'] == (7, 31, 47, 55, 59, 61)
    assert [(row['original_minority'], row['original_majority'], row['marks'], row['interface'])
            for row in plan['receiver_sides']] == [((56,), (10, 34), (58,), 'Q5_A_ALL'),
                                                    ((62,), (20, 36, 116), (6, 30), 'Q5_T15_FULL')]
    return plan


def run():
    start = process_time()
    prior = read_frozen(OLD, OLD_HASH)
    assert prior['status'] == 'first_joint_gate_failure' and not prior['impossible']
    assert prior['source_sha256'] == old_gates.SOURCE_HASH
    data = read_frozen(old_gates.SOURCE, old_gates.SOURCE_HASH)
    assert data['status'] == 'complete' and len(data['pair_rows']) == 23
    assert sum(len(pair['W']) for pair in data['pair_rows']) == LIMIT
    previous = {(row['pair_id'], row['W_id']): row for row in prior['positive']}
    assert len(previous) == 274
    fixed_key = (prior['first_failure']['pair_id'], prior['first_failure']['W_id'])
    assert fixed_key == (3, 21)
    old_gates.broad_returns.CPU_LIMIT = CPU_LIMIT
    broad_find = None
    positive, impossible = [], []
    gate_counts, stages = Counter(), Counter()
    status = 'complete'
    failure, current = None, None
    try:
        for pair_id, pair in enumerate(data['pair_rows']):
            for w_id, w in enumerate(pair['W']):
                old_gates.check_time(start)
                key = (pair_id, w_id)
                if key in previous:
                    old = previous.pop(key)
                    assert (old['L'], old['V'], old['W']) == (pair['L'], pair['V'], w)
                    positive.append({**old, 'plan_origin': 'frozen_prior'})
                    gate_counts[old['plan']['gate']] += 1
                    stages['reused_prior'] += 1
                    continue
                colors = old_gates.original_geometry(pair, w)
                current = {'pair_id': pair_id, 'W_id': w_id, 'case': pair['case'], 'L': pair['L'], 'V': pair['V'],
                           'W': w, 'even_holes': colors[0], 'odd_holes': colors[1]}
                if key == fixed_key:
                    assert all(list(colors[i]) == prior['first_failure'][field]
                               for i, field in enumerate(('even_holes', 'odd_holes')))
                    plan = fixed_plan(colors)
                    origin = 'verified_fixed_controlled'
                else:
                    origin = 'new_unvisited'
                    plan = old_gates.counts_orbits(colors) or old_gates.near_balanced_plan(colors)
                    if plan is None:
                        stages['controlled_count_searches'] += 1
                        plan = controlled_count(colors)
                if plan is None:
                    forced, exclusion = old_gates.forced_original_edges(colors)
                    if exclusion:
                        gate_counts[exclusion['gate']] += 1
                        impossible.append({**current, 'exclusion': exclusion})
                        current = None
                        continue
                    current['forced_edges'] = forced
                    loads = tuple(8 - abs(len(old_gates.face(colors[0], j, 1)) -
                                          len(old_gates.face(colors[1], j, 1))) for j in AXES)
                    counts = Counter()
                    stages['four_return_searches'] += 1
                    four = old_gates.find_four_return_plan(colors, loads, counts, start)
                    if four:
                        plan = {'gate': 'k4_two_return', **four}
                    else:
                        stages['broad_return_searches'] += 1
                        broad_counters = Counter()
                        if max(8 - load for load in loads) >= 4:
                            if broad_find is None:
                                broad_find = old_gates.broad_returns.make_search()
                            sets = tuple(frozenset(group) for group in colors)
                            for edge in forced or (None,):
                                old_gates.check_time(start)
                                broad, broad_counts = broad_find(sets, edge, start)
                                broad_counters.update(broad_counts)
                                if broad:
                                    plan = {'gate': 'registry_two_return', 'forced_edge': edge, **broad}
                                    break
                        stages.update({f'broad_{name}': count for name, count in broad_counters.items()})
                        if plan is None:
                            failure = {**current, 'k4_counters': dict(counts), 'broad_counters': dict(broad_counters),
                                       'bit_one_abs_gaps': tuple(8 - load for load in loads)}
                            status = 'first_joint_gate_failure'
                            break
                gate_counts[plan['gate']] += 1
                positive.append({**current, 'plan_origin': origin, 'plan': plan})
                current = None
            if status != 'complete':
                break
        old_gates.check_time(start)
        assert not previous
    except TimeoutError:
        status = 'cpu_limit'
    completed = len(positive) + len(impossible) + int(failure is not None)
    return {'status': status, 'cpu_seconds': process_time() - start, 'cpu_limit_seconds': CPU_LIMIT,
            'input_sha256': {old_gates.SOURCE: old_gates.SOURCE_HASH, OLD: OLD_HASH},
            'target_representatives': LIMIT, 'completed_count': completed, 'unvisited_count': LIMIT - completed,
            'positive_count': len(positive), 'impossible_count': len(impossible), 'gate_counts': dict(gate_counts),
            'stage_counts': dict(stages), 'positive': positive, 'impossible': impossible,
            'first_failure': failure, 'in_progress_at_timeout': current if status == 'cpu_limit' else None,
            'original_matching_enumerations': 0, 'matching_solver_calls': 0,
            'hamilton_solver_calls': 0, 'rank_runs': 0}


if __name__ == '__main__':
    receipt = run()
    OUTPUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ('positive', 'impossible')}, ensure_ascii=False))
