"""Independent fixed certificate checker. No producer imports or plan search."""

from collections import Counter, defaultdict
from functools import cache
from hashlib import sha256
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import json
from time import process_time


PREFIX = 'R7_E16_MU3_GAP7_EVEN_MINIMAL_'
HERE = Path(__file__).resolve().parent
SEVEN = Path('E:/\u65b0\u95ee\u9898/research/seven_directions')
SIX = tuple(range(6))
AXES = tuple(range(7))
S6 = tuple(permutations(SIX))


def read(path):
    return json.loads(path.read_bytes())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def bit(x, axis):
    return (x >> axis) & 1


def weight(x):
    return x.bit_count()


def permuted(x, perm):
    return sum(bit(x, i) << j for i, j in enumerate(perm))


def image(points, table):
    return tuple(sorted(table[x] for x in points))


def loads(points, axes=AXES):
    return tuple(sum(bit(x, i) for x in points) for i in axes)


@cache
def graph_count(degrees):
    """Count labeled simple graphs by resolving one vertex at a time."""
    if not degrees:
        return 1
    first, *rest = degrees
    return sum(
        graph_count(tuple(sorted((d - (i in neighbors) for i, d in enumerate(rest)), reverse=True)))
        for neighbors in combinations([i for i, d in enumerate(rest) if d > 0], first)
    )


def deficits():
    for three_tokens in combinations(range(8), 3):
        slots = set(three_tokens)
        bars = [-1, *(i for i in range(8) if i not in slots), 8]
        yield tuple(b - a - 1 for a, b in zip(bars, bars[1:]))


def verify_basis(base):
    tables = tuple(tuple(permuted(x, p) for x in range(128)) for p in S6)
    first_records = {tuple(r['L']): r for r in base['first_group_breakdown']}
    assert len(first_records) == len(base['first_group_breakdown']) == 24
    stabilizers = {}
    keys = set()
    for left, row in first_records.items():
        assert len(left) == 8 and left[0] == 0 and len(set(left)) == 8
        assert all(0 < e < 64 and weight(e) == 2 for e in left[1:])
        orbit = [image(left, t) for t in tables]
        keys.add(min(orbit))
        stabilizers[left] = tuple(t for t, candidate in zip(tables, orbit) if candidate == left)
        assert row['stabilizer_size'] == len(stabilizers[left])
    assert len(keys) == 24
    assert sum(factorial(6) // len(stab) for stab in stabilizers.values()) == comb(15, 7)

    independently_labeled = {}
    for left, row in first_records.items():
        degree = loads(left, SIX)
        count = queries = 0
        for a in SIX:
            for e in deficits():
                target = tuple(5 - degree[i] - (i == a) - e[i] for i in SIX)
                if min(target) < 0:
                    continue
                assert sum(target) == 12
                queries += 1
                count += graph_count(tuple(sorted(target, reverse=True)))
        assert (count, queries) == (row['bucket_hits'], row['lookups'])
        independently_labeled[left] = count

    right_keys = defaultdict(set)
    right_masses = Counter()
    spectra = Counter()
    colors_by_index = []
    for row in base['records']:
        left, right = tuple(row['L']), tuple(row['V'])
        assert left in stabilizers and len(right) == 8 and right[0] == 0
        assert len(set(right)) == 8 and all(0 < e < 128 and weight(e) == 2 for e in right[1:])
        columns = tuple(a + b for a, b in zip(loads(left), loads(right)))
        assert list(columns) == row['column_loads'] and columns[-1] == 1
        assert all(2 <= c <= 5 for c in columns[:-1]) and sum(columns) == 28
        assert sum(e >= 64 for e in right) == 1
        orbit = {image(right, table) for table in stabilizers[left]}
        key = min(orbit)
        assert key not in right_keys[left]
        right_keys[left].add(key)
        right_masses[left] += len(orbit)

        colors = (set(left), {127 ^ p for p in right})
        assert all(len(c) == 8 and all(weight(x) % 2 == parity for x in c) for parity, c in enumerate(colors))
        assert all(weight(x ^ y) >= 3 for x in colors[0] for y in colors[1])
        deltas = tuple(a - b for a, b in zip(*(loads(c) for c in colors)))
        assert deltas == tuple(c - 8 for c in columns)
        assert min(map(abs, deltas)) == 3 and sum(abs(d) == 7 for d in deltas) == 1
        spectra[tuple(sorted(map(abs, deltas)))] += 1
        colors_by_index.append(colors)

    assert right_masses == independently_labeled
    for left, row in first_records.items():
        assert len(right_keys[left]) == row['representatives']
    assert sum(right_masses.values()) == 58023
    assert len(colors_by_index) == 23032
    return colors_by_index, spectra


def face(points, axis, side):
    return {x for x in points if bit(x, axis) == side}


def directed_cut(colors, p, side_field):
    outer, a_side, alpha = p['outer'], p[side_field], p['alpha_parity']
    assert outer in AXES and a_side in (0, 1) and alpha in (0, 1)
    a = tuple(face(colors[c], outer, a_side) for c in (alpha, 1 - alpha))
    b = tuple(colors[c] - s for c, s in zip((alpha, 1 - alpha), a))
    assert len(a[1]) - len(a[0]) == len(b[0]) - len(b[1])
    return outer, a, b


def shape(*groups):
    return [list(map(len, group)) for group in groups]


def fixed_group(expected, saved):
    assert sorted(expected) == saved


def one_send(p, j, a, b, modes):
    k, r, inner = p['k'], p['r'], p['inner']
    assert inner in AXES and inner != j
    assert (r, k) in {(3, 3), (4, 3), (3, 4), (4, 4)}
    assert len(a[0]) == r and len(a[1]) == r + k and len(b[0]) == len(b[1]) + k
    fixed_group(a[0], p['donor_original_minority'])
    fixed_group(a[1], p['donor_original_majority'])
    x = set(p['X'])
    assert len(x) == len(p['X']) == k and x <= a[1]
    y = {v ^ (1 << j) for v in x}
    fixed_group(y, p['Y'])
    assert not y.intersection(set.union(*a, *b))
    assert [row['side'] for row in p['receiver_sides']] == [0, 1]
    for row in p['receiver_sides']:
        side = row['side']
        minority, majority, marked = (face(s, inner, side) for s in (b[1], b[0], y))
        fixed_group(minority, row['original_minority'])
        fixed_group(majority, row['original_majority'])
        fixed_group(marked, row['marks'])
        q = len(marked)
        assert q > 0 and len(majority | marked) - len(minority) == 2 * q
        interface = row['interface']
        if interface == 'Q5_A_ALL':
            assert q == 1 and len(minority) <= 14
        elif interface == 'Q5_T44':
            assert q == 2 and len(minority) == 0
        else:
            assert interface == 'Q5_T15_FULL' and q == 2 and len(minority) == 1
        modes[interface] += 1


def check_exact(donor, j, a, retained, marks, profile, good, s2, results):
    assert (len(a), len(retained), len(marks)) == (1, 3, 2)
    root, = a
    assert donor['normalization_root'] == root
    keep_axes = [i for i in AXES if i != j]
    groups = [sorted(sum(bit(x ^ root, i) << n for n, i in enumerate(keep_axes)) for x in points)
              for points in (retained, marks)]
    assert donor['normalized_groups'] == groups
    perm = donor['coordinate_transport']
    assert sorted(perm) == list(SIX)
    index = donor['index']
    assert index in good['union_closed_core_indices']
    assert index in s2['union_closed_core_indices'] or index in good['closed_core_indices']
    row = profile[index]
    targets = [sorted(permuted(x, perm) for x in group) for group in groups]
    assert targets == [row['included'], row['omitted']]
    results[index] += 1


def two_returns(p, j, a, b, profile, good, s2, results, kinds, shapes):
    r, s = len(a[0]), len(b[1])
    assert shape(a, b) == [[r, r + 3], [s + 3, s]] and r + s == 5
    x, u = set(p['X']), set(p['U'])
    assert len(x) == len(p['X']) == 1 and len(u) == len(p['U']) == 2
    assert x <= a[1] and u <= b[0]
    y, v = ({z ^ (1 << j) for z in pts} for pts in (x, u))
    assert len(y | v) == 3 and not (y | v).intersection(set.union(*a, *b))
    fixed_group(y, p['Y'])
    fixed_group(v, p['V'])
    ar, bn = a[1] - x, (b[0] - u) | y
    fixed_group(a[0], p['A_minor'])
    fixed_group(ar, p['A_retained'])
    fixed_group(b[1], p['B_minor'])
    fixed_group(bn, p['B_new_major'])
    assert shape((a[0], ar | v), (bn, b[1])) == [[r, r + 4], [s + 2, s]]

    inner = p['B_inner']
    assert inner in AXES and inner != j
    mark, = y
    side = bit(mark, inner)
    deltas = [len(face(bn, inner, q)) - len(face(b[1], inner, q)) for q in (0, 1)]
    assert deltas == p['B_deltas'] and side == p['B_marked_side']
    assert deltas[side] == 2 and deltas[1 - side] == 0

    donor = p['donor']
    kind = donor['kind']
    kinds[kind] += 1
    if kind == 'T15_exact_core':
        check_exact(donor, j, a[0], ar, v, profile, good, s2, results)
        return
    i = donor['inner']
    assert i in AXES and i != j
    on = donor.get('side', donor.get('inner_side'))
    assert on in (0, 1)
    maj = ar | v
    first = tuple(face(g, i, on) for g in (a[0], maj))
    second = tuple(g - f for g, f in zip((a[0], maj), first))
    (f, g), (h, k) = shape(first, second)
    shapes[(kind, f, g, h, k)] += 1
    if 'face_counts' in donor:
        assert donor['face_counts'] == [[f, g], [h, k]]
    if kind == 'T15_same_face':
        assert (f, g, h, k) == (1, 5, 0, 0)
    elif kind == 'T15_isolated_mark':
        isolated = donor['isolated_mark']
        assert (r, f, g, h, k) == (1, 0, 1, 1, 4)
        assert first[1] == {isolated} and isolated in v
    elif kind == 'T26_separated_two_root_choice':
        assert (f, g, h, k) == (2, 3, 0, 3)
        assert len(v & first[1]) == len(v & second[1]) == 1
        other_mark, = v & second[1]
        images = {z ^ (1 << i) for z in first[0]}
        assert other_mark not in images or images.intersection(second[1] - v)
    else:
        assert v <= first[1]
        if kind == 'Q6_same_side_majority_root':
            assert f in (0, 1) and g == f + 5 and 1 <= h <= 16 and k == h - 1
        elif kind == 'Q6_balanced_complement_avoid_two':
            assert f in (0, 1) and g == f + 4 and 1 <= h == k
        else:
            assert kind == 'Q6_T15_D4' and (f, g, h, k) == (0, 4, 1, 1)


def verify_plans(plan_file, colors_by_index, profile, good, s2):
    plans = plan_file['positives']
    assert plan_file['status'] == 'complete' and plan_file['first_failure'] is None
    assert plan_file['input_representatives'] == plan_file['visited'] == len(plans) == len(colors_by_index)
    assert plan_file['unvisited'] == 0
    assert {x['index'] for x in plans} == set(range(len(plans)))
    counts, kinds, core_counts, modes, controlled, donor_shapes = (Counter() for _ in range(6))
    for record in plans:
        index, p = record['index'], record['plan']
        colors = colors_by_index[index]
        gate = p['gate']
        counts[gate] += 1
        if gate == 'accepted_high_m':
            assert set(p['witnesses']) == {'R41'}
            w = p['witnesses']['R41']
            j, a, b = directed_cut(colors, w, 'donor_side')
            assert shape(a, b) == w['shape'] == [[4, 7], [4, 1]]
            assert list(map(sorted, a)) == w['original_A_by_alpha_beta']
            assert list(map(sorted, b)) == w['original_B_by_alpha_beta']
            root, = b[1]
            assert root == w['root']
            load = [[i, sum(bit(root ^ v, i) for v in b[0])] for i in AXES if i != j]
            usable = [i for i, c in load if c in (1, 2)]
            assert load == w['inner_loads'] and usable == w['usable'] and len(usable) >= 3
        elif gate == 'four_mono_capacity':
            j, a, b = directed_cut(colors, p, 'donor_side')
            assert shape(a, b) == p['shape'] == [[4, 8], [4, 0]]
            assert list(map(sorted, a)) == p['original_A_by_alpha_beta']
            assert list(map(sorted, b)) == p['original_B_by_alpha_beta']
            axes = [i for i in AXES if i != j and len(face(b[0], i, 1)) == 2]
            assert axes == p['split_axes']
            m = len(axes)
            assert m >= 3 and len(a[1]) > (m + 2 ** (5 - m) if m < 6 else 7)
        else:
            j, a, b = directed_cut(colors, p, 'A_side')
            if gate == 'E16_monochromatic_delta3':
                assert shape(a, b) == p['shape'] == [[5, 8], [3, 0]]
            elif gate == 'controlled_cycle_count':
                one_send(p, j, a, b, modes)
                controlled[f"{p['r']},{p['k']}"] += 1
            else:
                assert gate == 'k3_whole_receiver'
                two_returns(p, j, a, b, profile, good, s2, core_counts, kinds, donor_shapes)
    assert counts == plan_file['plan_counts']
    assert kinds == plan_file['k3_donor_counts']
    return counts, kinds, core_counts, modes, controlled, donor_shapes


def main():
    start = process_time()
    manifest_path = HERE / (PREFIX + 'CLOSURE_INPUTS.json')
    manifest = read(manifest_path)
    manifest_sha = digest(manifest_path)
    assert manifest_sha == '0c83829b72fb696eebf1e0bc4be0946dc1697bf3640fe4d8ba4df50d5fa684fd'
    hashes = manifest['sha256']
    assert len(hashes) == 64
    for name, expected in hashes.items():
        assert digest(HERE / name) == expected, name
    base_path = HERE / (PREFIX + 'BASE.json')
    base, plans = read(base_path), read(HERE / (PREFIX + 'FIXED_PLANS.json'))
    assert plans['base_sha256'] == digest(base_path)
    colors, spectra = verify_basis(base)
    assert [[list(k), v] for k, v in sorted(spectra.items())] == manifest['spectra_counts']

    profile_name = 'Q6_T15_ACTUAL_PROFILE.json'
    profile = {row['index']: row for row in read(SEVEN / profile_name)['orbits']}
    good = read(SEVEN / 'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
    s2_path = SEVEN / 'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json'
    s2 = read(s2_path)
    closed = read(SEVEN / 'Q6_T15_GOOD_ROOT_ALL_CLOSED.json')
    assert good['verdict'] == s2['verdict'] == 'PASS'
    assert good['audited_input_hashes'][profile_name] == s2['audited_input_hashes'][profile_name] == 'sha256:' + digest(SEVEN / profile_name)
    assert {row['core_index'] for row in closed['cores']} == set(good['union_closed_core_indices'])
    assert set(good['union_closed_core_indices']) == set(good['closed_core_indices']) | set(s2['union_closed_core_indices'])

    counts, kinds, core_counts, modes, controlled, donor_shapes = verify_plans(plans, colors, profile, good, s2)
    assert list(sorted(core_counts)) == manifest['exact_T15_targets']
    report = dict(
        verdict='PASS', manifest_sha256=manifest_sha, verified_manifest_hashes=len(hashes),
        representatives=len(colors), independent_labeled_right_count=58023,
        spectra=[[list(k), v] for k, v in sorted(spectra.items())],
        plan_counts=counts, k3_donor_counts=kinds, one_send_modes=modes, one_send_rk=controlled,
        k3_donor_shapes=[[list(k), v] for k, v in sorted(donor_shapes.items())],
        t15_core_receipts={i: dict(count=core_counts[i], included=profile[i]['included'], omitted=profile[i]['omitted'],
                                  direct_good_root=i in good['closed_core_indices'],
                                  direct_s2=i in s2['closed_core_indices'],
                                  s2_union=i in s2['union_closed_core_indices']) for i in sorted(core_counts)},
        s2_review_sha256=digest(s2_path), cpu_seconds=process_time() - start,
        producer_runs=0, plan_searches=0, matching_enumerations=0, solver_calls=0, rank_runs=0,
    )
    output = json.dumps(report, indent=2)
    (HERE / (PREFIX + 'REVIEW_CHECK.json')).write_text(output + '\n', encoding='utf-8')
    print(output)


if __name__ == '__main__':
    main()
