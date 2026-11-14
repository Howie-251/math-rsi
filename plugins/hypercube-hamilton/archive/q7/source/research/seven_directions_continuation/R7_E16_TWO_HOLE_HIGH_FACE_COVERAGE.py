"""Bounded joint gate check on the fixed 2,505 high-face hole candidates."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time

import R7_E16_DISTANCE2_TWO_RETURN_PLAN as broad_returns
from R7_E16_ODD_22_COMPLETE_COVERAGE import find_plan as find_four_return_plan


HERE = Path(__file__).resolve().parent
OUTPUT = Path(__file__).with_suffix('.json')
SOURCE = 'R7_E16_TWO_HOLE_HIGH_FACE_REDUCTION.json'
SOURCE_HASH = 'c9f90b7f7d8b5e1af9c5e06f04fe1bca48a503ae6716d0044c1677c834e41f5b'
AXES = tuple(range(7))
CPU_LIMIT = 30
LIMIT = 2505


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def face(points, axis, side):
    return tuple(p for p in points if (p >> axis) & 1 == side)


def original_geometry(pair, w):
    alpha = pair['L'][0].bit_count() % 2
    alpha_holes = (*pair['L'], *(64 | x for x in w))
    beta_holes = tuple(63 ^ x for x in pair['V'])
    colors = (alpha_holes, beta_holes) if alpha == 0 else (beta_holes, alpha_holes)
    colors = tuple(tuple(sorted(group)) for group in colors)
    assert all(len(set(group)) == 8 and all(x.bit_count() % 2 == i for x in group)
               for i, group in enumerate(colors))
    assert all((x ^ y).bit_count() != 1 for x in colors[0] for y in colors[1])
    return colors


def counts_orbits(colors):
    bit_one_gaps = tuple(len(face(colors[0], axis, 1)) - len(face(colors[1], axis, 1)) for axis in AXES)
    if min(map(abs, bit_one_gaps)) == 4:
        return {'gate': 'E16_mu4', 'bit_one_even_minus_odd': bit_one_gaps}
    for outer in AXES:
        for side in (0, 1):
            for alpha in (0, 1):
                a, b = (len(face(colors[i], outer, side)) for i in (alpha, 1 - alpha))
                c, d = 8 - a, 8 - b
                shape = ((a, b), (c, d))
                if a == b and c == d and a <= 5 and c <= 5:
                    gate = 'B'
                elif a <= 2 and b == a + 1 and d <= 5 and c == d + 1:
                    gate = 'D'
                elif shape == ((5, 7), (3, 1)):
                    gate = 'E16_edge_delta2'
                elif shape == ((4, 6), (4, 2)):
                    gate = 'E16_central_delta2'
                elif shape == ((5, 8), (3, 0)):
                    gate = 'E16_monochromatic_delta3'
                else:
                    continue
                return {'gate': gate, 'outer': outer, 'A_side': side, 'alpha_parity': alpha, 'shape': shape}
    for outer in AXES:
        if bit_one_gaps[outer]:
            continue
        inner_plans = []
        for side in (0, 1):
            even, odd = (face(group, outer, side) for group in colors)
            hits = [(inner, len(face(even, inner, 1)) - len(face(odd, inner, 1)))
                    for inner in AXES if inner != outer]
            inner_plans.append(next((hit for hit in hits if abs(hit[1]) <= 1), None))
        if all(hit is not None for hit in inner_plans):
            return {'gate': 'Q_plus', 'outer': outer, 'inner_axes_and_gaps_by_outer_bit': inner_plans}
    return None


def forced_original_edges(colors):
    holes = set(colors[0] + colors[1])
    endpoint_owner = {}
    edges = set()
    for vertex in range(128):
        if vertex in holes:
            continue
        neighbors = [vertex ^ (1 << i) for i in AXES if vertex ^ (1 << i) not in holes]
        if not neighbors:
            return (), {'gate': 'impossible_isolated_covered_vertex', 'vertex': vertex}
        if len(neighbors) == 1:
            edge = tuple(sorted((vertex, neighbors[0])))
            for endpoint in edge:
                other = endpoint_owner.setdefault(endpoint, edge)
                if other != edge:
                    return (), {'gate': 'impossible_conflicting_forced_edges', 'edges': (other, edge),
                                'common_endpoint': endpoint}
            edges.add(edge)
    return tuple(sorted(edges)), None


def near_balanced_plan(colors):
    for outer in AXES:
        for side in (0, 1):
            for alpha in (0, 1):
                a, b = (face(colors[i], outer, side) for i in (alpha, 1 - alpha))
                if (len(a), len(b)) != (6, 8):
                    continue
                for inner in AXES:
                    if inner == outer:
                        continue
                    d = len(face(b, inner, 1)) - len(face(a, inner, 1))
                    if -1 <= d <= 3:
                        return {'gate': 'near_balanced_two_hole', 'outer': outer, 'A_side': side,
                                'alpha_parity': alpha, 'inner': inner,
                                'donor_bit_one_beta_minus_alpha': d}
    return None


def run():
    start = process_time()
    raw = (HERE / SOURCE).read_bytes()
    assert sha256(raw).hexdigest() == SOURCE_HASH
    data = json.loads(raw)
    assert data['status'] == 'complete' and data['complete_pair_reps'] == len(data['pair_rows']) == 23
    assert data['full_reps_counted'] == sum(len(pair['W']) for pair in data['pair_rows']) == LIMIT
    assert all(pair['complete'] for pair in data['pair_rows'])
    broad_returns.CPU_LIMIT = CPU_LIMIT
    broad_find = None
    positive, impossible = [], []
    gate_counts = Counter()
    stages = Counter()
    failure, current = None, None
    status = 'complete'
    try:
        for pair_id, pair in enumerate(data['pair_rows']):
            for w_id, w in enumerate(pair['W']):
                check_time(start)
                colors = original_geometry(pair, w)
                current = {'pair_id': pair_id, 'W_id': w_id, 'case': pair['case'], 'L': pair['L'], 'V': pair['V'],
                           'W': w, 'even_holes': colors[0], 'odd_holes': colors[1]}
                plan = counts_orbits(colors) or near_balanced_plan(colors)
                if plan is None:
                    forced, exclusion = forced_original_edges(colors)
                    if exclusion:
                        gate_counts[exclusion['gate']] += 1
                        impossible.append({**current, 'exclusion': exclusion})
                        current = None
                        continue
                    current['forced_edges'] = forced
                    loads = tuple(8 - abs(len(face(colors[0], j, 1)) - len(face(colors[1], j, 1))) for j in AXES)
                    counts = Counter()
                    stages['four_return_searches'] += 1
                    four = find_four_return_plan(colors, loads, counts, start)
                    if four:
                        plan = {'gate': 'k4_two_return', **four}
                    else:
                        stages['broad_return_searches'] += 1
                        check_time(start)
                        if broad_find is None:
                            broad_find = broad_returns.make_search()
                        sets = tuple(frozenset(group) for group in colors)
                        for edge in forced or (None,):
                            check_time(start)
                            broad, broad_counts = broad_find(sets, edge, start)
                            stages.update({f'broad_{name}': count for name, count in broad_counts.items()})
                            if broad:
                                plan = {'gate': 'registry_two_return', 'forced_edge': edge, **broad}
                                break
                        if plan is None:
                            failure = {**current, 'k4_counters': dict(counts)}
                            status = 'first_joint_gate_failure'
                            break
                gate_counts[plan['gate']] += 1
                positive.append({**current, 'plan': plan})
                current = None
            if status != 'complete':
                break
        check_time(start)
    except TimeoutError:
        status = 'cpu_limit'
    return {'status': status, 'cpu_seconds': process_time() - start, 'cpu_limit_seconds': CPU_LIMIT,
            'source': SOURCE, 'source_sha256': SOURCE_HASH, 'source_pair_representatives': 23,
            'target_representatives': LIMIT, 'positive_count': len(positive), 'impossible_count': len(impossible),
            'completed_count': len(positive) + len(impossible) + int(failure is not None),
            'gate_counts': dict(gate_counts), 'stage_counts': dict(stages), 'positive': positive,
            'impossible': impossible, 'first_failure': failure,
            'in_progress_at_timeout': current if status == 'cpu_limit' else None,
            'original_matching_enumerations': 0, 'matching_solver_calls': 0,
            'hamilton_solver_calls': 0, 'rank_runs': 0}


if __name__ == '__main__':
    receipt = run()
    OUTPUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ('positive', 'impossible')}, ensure_ascii=False))
