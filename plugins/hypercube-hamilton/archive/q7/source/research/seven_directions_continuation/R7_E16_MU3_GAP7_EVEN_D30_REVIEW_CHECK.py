"""Independent audit of the frozen D30 basis and its fixed plans."""

from collections import Counter, defaultdict
from functools import cache
from itertools import combinations
from math import comb
from pathlib import Path
import json
from time import process_time

from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import (
    AXES, HERE, SEVEN, SIX, S6, bit, digest, directed_cut, face, image, loads,
    one_send, permuted, read, shape, two_returns, weight,
)

PREFIX = 'R7_E16_MU3_GAP7_EVEN_D30_'
MANIFEST_SHA = '69615bb3700bd5d0386afb500fabe1366afa62bf964c4dfcf78ee47f71709ed6'
S2_NAME = 'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json'
S2_DATA = 'Q6_T15_S2_COMBINED_EXTENSION.json'
PROFILE_NAME = 'Q6_T15_ACTUAL_PROFILE.json'
GROUP_BP = tuple(p for p in S6 if p[0] == 0 and set(p[1:4]) == {1, 2, 3})
LOW = 63
FOUR = 15
BP_FORBIDDEN = LOW ^ FOUR
FIRST_EDGES = dict(A_R=7, A_P=8, B_R4=7, B_R2=7, B_P=6)


@cache
def count_completions(degrees, forbidden):
    """Count labeled graphs by assigning the neighbors of the first vertex."""
    if not degrees:
        return 1
    first, *remaining = degrees
    neighbors = [i for i, d in enumerate(remaining, 1)
                 if d > 0 and (1 | (1 << i)) != forbidden]
    return sum(
        count_completions(tuple(d - (i in selected) for i, d in enumerate(remaining, 1)),
                          forbidden >> 1 if not forbidden & 1 else 0)
        for selected in combinations(neighbors, first)
    )


def special_supports(case, graph):
    if case in ('A_R', 'A_P'):
        yield from ((1 << a) for a in SIX)
    elif case == 'B_P':
        yield FOUR
    else:
        size = 3 if case == 'B_R4' else 4
        for support in combinations(SIX, size):
            mask = sum(1 << i for i in support)
            if all(mask & edge for edge in graph):
                if case == 'B_R4':
                    yield mask
                else:
                    yield from ((mask, a) for a in SIX)


def independent_right_count(case, graph):
    labeled = queries = 0
    degree = loads(graph, SIX)
    for support in special_supports(case, graph):
        if case == 'B_R2':
            special, a = support
            extra = tuple(bit(special, i) + (i == a) for i in SIX)
        else:
            extra = tuple(bit(support, i) + (case == 'B_P' and i == 0) for i in SIX)
        for deficiency in SIX:
            target = tuple(5 - degree[i] - extra[i] - (i == deficiency) for i in SIX)
            if min(target) >= 0:
                queries += 1
                labeled += count_completions(target, BP_FORBIDDEN if case == 'B_P' else 0)
    return queries, labeled


def first_orbits(base):
    group = tuple(tuple(permuted(x, (*p, 6)) for x in range(128)) for p in S6)
    group_bp = tuple(tuple(permuted(x, (*p, 6)) for x in range(128)) for p in GROUP_BP)
    assert len(group) == 720 and len(group_bp) == 12
    by_case = {}
    for case, size in FIRST_EDGES.items():
        tables = group_bp if case == 'B_P' else group
        rows = base['first_orbit_information'][case]
        keys = {}
        mass = 0
        first_sizes = Counter()
        for row in rows:
            graph = tuple(row['first'])
            assert len(set(graph)) == len(graph) == size
            assert all(0 < x <= LOW and weight(x) == 2 for x in graph)
            orbit = [image(graph, t) for t in tables]
            assert graph == min(orbit) and graph not in keys
            stabilizer = tuple(t for t, im in zip(tables, orbit) if im == graph)
            orbit_size = len(tables) // len(stabilizer)
            assert len(stabilizer) == row['stabilizer_size'] and len(set(orbit)) == orbit_size
            mass += orbit_size
            first_sizes[orbit_size] += 1
            assert independent_right_count(case, graph) == (row['queries'], row['hits']), (case, graph)
            keys[graph] = (row, stabilizer)
        assert mass == comb(15, size)
        assert len(keys) == (528 if case == 'B_P' else 24)
        by_case[case] = keys
        if case == 'B_P':
            assert first_sizes == {1: 4, 2: 3, 3: 25, 6: 172, 12: 324}
    return by_case


def verify_basis(base):
    assert base['status'] == 'complete'
    assert base['original_matchings_enumerated'] == 0
    first = first_orbits(base)
    keys, multiplicities = defaultdict(set), defaultdict(Counter)
    colors_by_index, cases = [], []
    for index, row in enumerate(base['records']):
        light, heavy = tuple(row['L']), tuple(row['V'])
        case = row['case']
        assert len(light) == len(set(light)) == len(heavy) == len(set(heavy)) == 8, index
        assert all(0 <= x < 128 for x in light + heavy), index
        assert light[0] == 0 and all(weight(x) == 2 for x in light[1:]), index
        fours = [x for x in heavy if weight(x) == 4]
        if fours:
            four, = fours
            assert heavy[0] == 0 and sum(weight(x) == 2 for x in heavy) == 6, index
            assert all(four & x for x in light[1:]), index
        else:
            assert all(weight(x) == 2 for x in heavy), index
        columns = tuple(a + b for a, b in zip(loads(light), loads(heavy)))
        assert list(columns) == row['column_loads'] and columns[6] == 1, index
        assert sorted(columns[:6]) == [4, 5, 5, 5, 5, 5], index
        high, = [x for x in light + heavy if bit(x, 6)]
        if high in light:
            expected = 'B_P' if fours else 'A_P'
        else:
            expected = ('B_R4' if high == four else 'B_R2') if fours else 'A_R'
        assert case == expected, index
        if case == 'B_P':
            assert high == 65 and four == FOUR, index
        first_group, second_group = (heavy, light) if high in light else (light, heavy)
        graph = tuple(x for x in first_group if weight(x) == 2)
        _, stabilizer = first[case][graph]
        orbit = {image(second_group, t) for t in stabilizer}
        key = min(orbit)
        assert second_group == key and key not in keys[case, graph], index
        keys[case, graph].add(key)
        multiplicities[case, graph][str(len(orbit))] += 1

        colors = set(light), {127 ^ x for x in heavy}
        assert all(weight(x) % 2 == color for color, group in enumerate(colors) for x in group)
        assert all(weight(x ^ y) >= 3 for x in colors[0] for y in colors[1]), index
        deltas = tuple(a - b for a, b in zip(*(loads(g) for g in colors)))
        assert deltas == tuple(c - 8 for c in columns), index
        colors_by_index.append(colors)
        cases.append(case)

    totals = {}
    for case, rows in first.items():
        totals[case] = dict(first_orbits=len(rows), queries=0, hits=0, representatives=0)
        for graph, (row, _) in rows.items():
            sizes = multiplicities[case, graph]
            count = len(keys[case, graph])
            assert count == sum(sizes.values()) == row['orbits'], (case, graph)
            assert sizes == row['orbit_size_multiplicities'], (case, graph)
            assert sum(int(k) * v for k, v in sizes.items()) == row['hits'], (case, graph)
            totals[case]['queries'] += row['queries']
            totals[case]['hits'] += row['hits']
            totals[case]['representatives'] += count
    assert totals == base['counts']
    assert sum(t['queries'] for t in totals.values()) == base['queries'] == 9713
    assert sum(t['hits'] for t in totals.values()) == 60587
    assert len(colors_by_index) == base['record_count'] == 27936
    return colors_by_index, cases, totals


def high_m(colors, witnesses):
    assert set(witnesses) in ({'R41'}, {'R32'}, {'R41', 'R32'})
    for kind, w in witnesses.items():
        j, a, b = directed_cut(colors, w, 'donor_side')
        assert shape(a, b) == w['shape']
        assert list(map(sorted, a)) == w['original_A_by_alpha_beta']
        assert list(map(sorted, b)) == w['original_B_by_alpha_beta']
        if kind == 'R41':
            assert shape(a, b) == [[4, 7], [4, 1]]
            root, = b[1]
            assert root == w['root']
            load = [[i, sum(bit(root ^ x, i) for x in b[0])] for i in AXES if i != j]
            usable = [i for i, c in load if c in (1, 2)]
            assert len(usable) >= 3
        else:
            assert shape(a, b) == [[3, 6], [5, 2]]
            load = [[i, [len(face(g, i, 1)) for g in b]] for i in AXES if i != j]
            usable = [i for i, cs in load if tuple(cs) in {(2, 0), (2, 1), (3, 1), (3, 2)}]
            assert len(usable) >= 4
        assert load == w['inner_loads'] and usable == w['usable']


def verify_plans(plans, colors, cases, profile, good, s2):
    entries = plans['positives']
    assert plans['status'] == 'complete' and plans['first_failure'] is None
    assert len(entries) == plans['input_representatives'] == plans['visited'] == len(colors)
    assert {x['index'] for x in entries} == set(range(len(colors)))
    assert all(plans[k] == 0 for k in (
        'unvisited', 'original_matchings_enumerated', 'solver_calls', 'rank_runs', 'new_geometries'))
    counts, high, rk, modes, kinds, cores, donor_shapes = (Counter() for _ in range(7))
    case_counts = defaultdict(Counter)
    for entry in entries:
        i, p = entry['index'], entry['plan']
        gate = p['gate']
        counts[gate] += 1
        case_counts[cases[i]][gate] += 1
        try:
            if gate == 'accepted_high_m':
                high_m(colors[i], p['witnesses'])
                high['+'.join(sorted(p['witnesses']))] += 1
            elif gate == 'four_mono_capacity':
                j, a, b = directed_cut(colors[i], p, 'donor_side')
                assert shape(a, b) == p['shape'] == [[4, 8], [4, 0]]
                assert list(map(sorted, a)) == p['original_A_by_alpha_beta']
                assert list(map(sorted, b)) == p['original_B_by_alpha_beta']
                axes = [t for t in AXES if t != j and len(face(b[0], t, 1)) == 2]
                assert axes == p['split_axes'] and len(axes) in (3, 4, 5, 6)
                assert len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(axes)]
            else:
                j, a, b = directed_cut(colors[i], p, 'A_side')
                if gate == 'E16_monochromatic_delta3':
                    assert shape(a, b) == p['shape'] == [[5, 8], [3, 0]]
                elif gate == 'controlled_cycle_count':
                    one_send(p, j, a, b, modes)
                    rk[f"{p['r']},{p['k']}"] += 1
                else:
                    assert gate == 'k3_whole_receiver'
                    two_returns(p, j, a, b, profile, good, s2, cores, kinds, donor_shapes)
        except (AssertionError, KeyError, ValueError) as exc:
            raise AssertionError((i, gate)) from exc
    assert counts == plans['plan_counts'] and kinds == plans['k3_donor_counts']
    assert case_counts == plans['case_plan_counts']
    assert high == {'R41': 8940, 'R32': 146, 'R32+R41': 95}
    assert rk == {'3,3': 15469, '4,3': 2046, '3,4': 601, '4,4': 58}
    assert modes == {'Q5_A_ALL': 17515, 'Q5_T44': 5684, 'Q5_T15_FULL': 13149}
    assert cores == {361: 1}
    return dict(plan_counts=counts, high_m=high, controlled_rk=rk, receiver_modes=modes,
                k3_donors=kinds, k3_donor_shapes=[[list(k), v] for k, v in sorted(donor_shapes.items())],
                core_counts=cores, case_plan_counts=case_counts)


def main():
    start = process_time()
    manifest_path = HERE / (PREFIX + 'CLOSURE_INPUTS.json')
    assert digest(manifest_path) == MANIFEST_SHA
    manifest = read(manifest_path)
    hashes = manifest['sha256']
    assert len(hashes) == 85
    for name, expected in hashes.items():
        assert digest(HERE / name) == expected, name
    old = read(HERE / 'R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW.json')
    e14 = read(HERE / 'R7_MU1_CENTRAL_T1_AND_E14_REVIEW.json')
    assert old['verdict'] == e14['verdict'] == 'PASS'
    base_path = HERE / (PREFIX + 'BASE.json')
    base, plans = read(base_path), read(HERE / (PREFIX + 'FIXED_PLANS.json'))
    assert plans['base_sha256'] == digest(base_path)
    colors, cases, totals = verify_basis(base)
    assert totals == manifest['D30_case_counts']
    profile = {r['index']: r for r in read(SEVEN / PROFILE_NAME)['orbits']}
    good = read(SEVEN / 'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
    s2 = read(SEVEN / S2_NAME)
    s2_data = read(SEVEN / S2_DATA)
    assert good['verdict'] == s2['verdict'] == 'PASS'
    assert good['audited_input_hashes'][PROFILE_NAME] == s2['audited_input_hashes'][PROFILE_NAME] == 'sha256:' + digest(SEVEN / PROFILE_NAME)
    assert s2['audited_input_hashes'][S2_DATA] == 'sha256:' + digest(SEVEN / S2_DATA)
    assert 361 in good['union_closed_core_indices'] and 361 in s2['closed_core_indices']
    good_all = read(SEVEN / 'Q6_T15_GOOD_ROOT_ALL_CLOSED.json')
    assert {r['core_index'] for r in good_all['cores']} == set(good['union_closed_core_indices'])
    core, = [r for r in s2_data['cores'] if r['core_index'] == 361]
    assert profile[361]['included'] == [31, 59, 61] and profile[361]['omitted'] == [1, 7]
    assert len(core['roots']) == 15
    checks = verify_plans(plans, colors, cases, profile, good, s2)
    assert checks['plan_counts'] == manifest['D30_plan_counts']
    assert checks['k3_donors'] == manifest['D30_k3_donors']
    assert list(checks['core_counts']) == manifest['exact_T15_targets']
    assert len(colors) == manifest['new_D30_representatives']
    assert manifest['accepted_D28_representatives'] == 23032
    assert manifest['combined_even_representatives'] == 23032 + len(colors)
    elapsed = process_time() - start
    assert elapsed < 60
    result = dict(verdict='PASS', manifest_sha256=MANIFEST_SHA, bindings=len(hashes),
                  branch_totals=totals, queries=9713, labeled_completions=60587,
                  representatives=len(colors), combined_representatives=23032 + len(colors),
                  s2_receipt_sha256=digest(SEVEN / S2_NAME), s2_data_sha256=digest(SEVEN / S2_DATA),
                  cpu_seconds=elapsed, cpu_budget=60, producer_runs=0, plan_searches=0,
                  matching_enumerations=0, solver_calls=0, rank_runs=0, **checks)
    output = json.dumps(result, indent=2)
    (HERE / (PREFIX + 'REVIEW_CHECK.json')).write_text(output + '\n', encoding='utf-8')
    print(output)


if __name__ == '__main__':
    main()
