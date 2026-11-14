"""Independent checker for the frozen marked odd gap-seven basis and plans."""

from collections import Counter, defaultdict
from functools import cache, lru_cache
from itertools import combinations
import json
from time import process_time

from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import (
    AXES, HERE, SEVEN, S6, bit, digest, directed_cut, face, fixed_group,
    one_send, permuted, read, shape,
)
from R7_E16_MU3_GAP7_EVEN_D30_REVIEW_CHECK import high_m


PREFIX = 'R7_E16_MU3_GAP7_ODD_'
MANIFEST_HASH = 'ed4b87853663df0e230648b80012f66841d1a920a2fcd58ab5113297a5c50458'
HIGH = 64
FULL = 127
UNIT = tuple(1 << i for i in range(6))
PAIR = tuple(sum(s) for s in combinations(UNIT, 2))
TRIPLE = tuple(sum(s) for s in combinations(UNIT, 3))
FIVE = tuple(63 ^ x for x in UNIT)
TRANSPORTS = tuple(tuple((x & HIGH) | permuted(x & 63, p) for x in range(128)) for p in S6)
DEGREE = tuple(sum(bit(x, i) << (4 * i) for i in range(6)) for x in range(128))


def image(points, trans):
    return tuple(sorted(trans[x] for x in points))


def branch(n, p):
    h, = (x for x in p if x & HIGH)
    t_n = sum(x.bit_count() == 3 for x in n)
    t_p = sum(x.bit_count() == 3 for x in p)
    fives = [(side, x) for side, group in enumerate((n, p)) for x in group if x.bit_count() == 5]
    if not fives:
        family = {1: 'q0_h1', 3: 'q0_h3'}[h.bit_count()]
    else:
        (side, f), = fives
        if side == 0:
            assert h.bit_count() == 3
            family = 'q1_n5_h3'
        elif h.bit_count() == 1:
            family = 'q1_p5_h1'
        else:
            assert h.bit_count() == 3
            family = 'q1_p5_h3_inside' if (h & 63) & ~f == 0 else 'q1_p5_h3_cross'
    return family, t_n, t_p


def branch_table():
    rows = {(f, a, b) for f in ('q0_h1', 'q0_h3') for a in range(2, 7)
            for b in range(1 if f == 'q0_h1' else 2, 6) if a + b <= 7}
    rows |= {('q1_n5_h3', a, b) for a in (1, 2) for b in (3, 4) if a + b <= 5}
    rows |= {('q1_p5_h3_' + side, a, b) for side in ('inside', 'cross')
             for a in (3, 4) for b in (1, 2) if a + b <= 5}
    rows |= {('q1_p5_h1', a, b) for a in range(3, 6) for b in range(3) if a + b <= 5}
    excluded = {row: 'all_seven_units' for row in rows if
                (row[0] == 'q0_h1' and row[2] == 1) or (row[0] == 'q1_p5_h1' and row[2] == 0)}
    return rows - excluded.keys(), excluded


def partial_sets(case, side):
    family, t_n, t_p = case
    if side == 0:
        fs = FIVE if family == 'q1_n5_h3' else (0,)
        for f in fs:
            for u in combinations(UNIT, 8 - t_n - bool(f)):
                yield (*u, *((f,) if f else ())), t_n
        return
    if family.endswith('h1'):
        hs, high_is_triple = (HIGH,), 0
    else:
        hs, high_is_triple = tuple(HIGH | x for x in PAIR), 1
    fs = FIVE if family.startswith('q1_p5_') else (0,)
    for h in hs:
        for f in fs:
            inside = (h & 63) & ~f == 0
            if (family.endswith('inside') and not inside) or (family.endswith('cross') and inside):
                continue
            for u in combinations(UNIT, 7 - t_p + high_is_triple - bool(f)):
                yield (h, *u, *((f,) if f else ())), t_p - high_is_triple


def separated(a, b):
    return all((x ^ y).bit_count() <= 4 for x in a for y in b)


@lru_cache(maxsize=256)
def degree_histogram(pool, count):
    """Count labeled simple triple systems by degree via vertex elimination."""
    if count == 0:
        return {0: 1}
    if count < 0 or count > len(pool):
        return {}
    if count == len(pool):
        return {sum(DEGREE[x] for x in pool): 1}
    pivot = (pool[0] & -pool[0])
    incident = tuple(x for x in pool if x & pivot)
    remaining = tuple(x for x in pool if not x & pivot)
    histogram = Counter()
    for n in range(max(0, count - len(remaining)), min(len(incident), count) + 1):
        tails = degree_histogram(remaining, count - n)
        for chosen in combinations(incident, n):
            local = sum(DEGREE[x] for x in chosen)
            for residual, multiplicity in tails.items():
                histogram[local + residual] += multiplicity
    return histogram


@cache
def in_range(encoded):
    digits = tuple((encoded >> (4 * i)) & 15 for i in range(6))
    return min(digits) >= 1 and max(digits) == 5


def labeled_second_count(first, candidates):
    pool = tuple(x for x in TRIPLE if separated((x,), first))
    first_degree = sum(DEGREE[x] for x in first)
    total = 0
    for partial, n_triples in candidates:
        if not separated(first, partial):
            continue
        fixed_degree = first_degree + sum(DEGREE[x] for x in partial)
        if any(((fixed_degree >> (4 * i)) & 15) > 5 for i in range(6)):
            continue
        # At most one fixed unit plus special supports per side, and at most
        # five new triples. Every per-coordinate sum here fits in four bits.
        total += sum(m for degree, m in degree_histogram(pool, n_triples).items()
                     if in_range(fixed_degree + degree))
    return total


def first_orbits(case, side):
    images = {}
    stabilizers = {}
    for partial, n_triples in partial_sets(case, side):
        for triples in combinations(TRIPLE, n_triples):
            first = tuple(sorted((*partial, *triples)))
            if first in images:
                continue
            first_degree = sum(DEGREE[x] for x in first)
            if any(((first_degree >> (4 * i)) & 15) > 5 for i in range(6)):
                continue
            orbit = {image(first, p): p for p in TRANSPORTS}
            key = min(orbit)
            stabilizers[key] = tuple(p for p in TRANSPORTS if image(key, p) == key)
            # Keep one transport from the canonical object to each orbit point.
            for p in TRANSPORTS:
                images[image(key, p)] = key, p
    return images, stabilizers


@cache
def inverse_map(transport):
    return tuple(transport.index(x) for x in range(128))


def verify_basis(base):
    included, excluded = branch_table()
    by_case = {(row['family'], row['t_N'], row['t_P']): row for row in base['marked_rows']}
    actual_excluded = {(row['family'], row['t_N'], row['t_P']): row['reason']
                       for row in base['excluded_rows']}
    assert set(by_case) == included and len(base['marked_rows']) == len(included) == 32
    assert set(excluded.items()) <= set(actual_excluded.items())
    assert set(actual_excluded) - set(excluded) == {('q1_h5', 4, 1)}
    assert len(actual_excluded) == len(base['excluded_rows']) == 9
    records = defaultdict(list)
    colors = {}
    for index, row in enumerate(base['records']):
        n, p = (tuple(row[k]) for k in ('L', 'V'))
        assert all(len(s) == len(set(s)) == 8 and s == tuple(sorted(s)) for s in (n, p))
        assert all(0 < x < 128 and x.bit_count() in (1, 3, 5) for x in n + p)
        assert all(x < HIGH for x in n) and sum(bool(x & HIGH) for x in p) == 1
        assert sum(x.bit_count() == 1 for x in n) <= 6 and sum(x.bit_count() == 1 for x in p) <= 6
        assert separated(n, p)
        c = [sum(bit(x, i) for x in n + p) for i in AXES]
        assert c == row['column_loads'] and min(c) >= 1 and max(c) == 5 and c[6] == 1
        case = branch(n, p)
        assert case == (row['case'], row['t_N'], row['t_P']) and case in included
        records[case].append((n, p))
        colors[index] = ({FULL ^ x for x in p}, set(n))

    counts = {}
    final_bucket_mass = 0
    for case in sorted(included):
        label = by_case[case]['chosen_first']
        assert label in ('N', 'P')
        side = int(label == 'P')
        first_index, stabilizers = first_orbits(case, side)
        opposites = tuple(partial_sets(case, 1 - side))
        mass = defaultdict(set)
        subgroup_sizes = Counter()
        for pair in records[case]:
            key, trans = first_index[pair[side]]
            other = image(pair[1 - side], inverse_map(trans))
            orbit = {image(other, p) for p in stabilizers[key]}
            assert mass[key].isdisjoint(orbit), (case, key, other)
            mass[key].update(orbit)
            fixed = tuple(x for x in other if x.bit_count() != 3 or x & HIGH)
            subgroup_orbit = {image(other, p) for p in stabilizers[key] if image(fixed, p) == fixed}
            subgroup_sizes[str(len(subgroup_orbit))] += 1
        independent_count = 0
        for key in stabilizers:
            wanted = labeled_second_count(key, opposites)
            assert len(mass[key]) == wanted, (case, key, len(mass[key]), wanted)
            independent_count += wanted
        assert len(records[case]) == by_case[case]['representatives']
        assert subgroup_sizes == by_case[case]['orbit_size_multiplicities']
        bucket_mass = sum(int(k) * v for k, v in subgroup_sizes.items())
        assert bucket_mass == by_case[case]['hits']
        final_bucket_mass += bucket_mass
        counts[str(case)] = dict(first_orbits=len(stabilizers), second_mass=independent_count,
                                 final_subgroup_mass=bucket_mass, representatives=len(records[case]))
    assert len(colors) == base['record_count'] == 45355
    assert final_bucket_mass == 84106
    return colors, counts, final_bucket_mass


def project(points, axes, root=0):
    return sorted(sum(bit(x ^ root, axis) << i for i, axis in enumerate(axes)) for x in points)


def exact_core(minor, major, marks, outer, index, root, normalized, perm, registry):
    assert minor == {root} and len(marks) == 2 and len(major - marks) == 3
    assert sorted(perm) == list(range(6))
    axes = [axis for axis in AXES if axis != outer]
    groups = [project(major - marks, axes, root), project(marks, axes, root)]
    assert groups == normalized
    assert [sorted(permuted(x, perm) for x in group) for group in groups] == registry[index]


def whole_face(minor, major, marks, outer, inner, side, kind, counts):
    assert inner in AXES and inner != outer and side in (0, 1)
    a, b = (face(g, inner, side) for g in (minor, major))
    assert marks <= b and len(marks) == 2
    assert shape((a, b), (minor - a, major - b)) == counts
    (f, g), (h, k) = counts
    if kind == 'majority_root':
        assert f in (0, 1) and g == f + 5 and 1 <= h <= 16 and k == h - 1
    else:
        assert kind == 'two_minority_roots'
        assert (f, g) == (2, 5) and 0 <= h <= 15 and k == h + 1


def double_omit(donor, minor, major, marks, outer, registry, cores):
    kind = donor['kind']
    assert len(marks) == 2 and marks <= major and len(major) == len(minor) + 4
    if kind == 'T15_exact_core':
        index = donor['index']
        exact_core(minor, major, marks, outer, index, donor['normalization_root'],
                   donor['normalized_groups'], donor['coordinate_transport'], registry)
        cores[index] += 1
        return
    if kind == 'Q6_T26_paired_S1':
        (i, s), (j, t) = donor['inner_sides']
        assert i in AXES and j in AXES and len({i, j, outer}) == 3 and s in (0, 1) and t in (0, 1)
        a, b = (face(g, i, s) for g in (minor, major))
        c, d = (face(g, j, t) for g in (minor, major))
        assert shape((a, b), (c, d), (minor - a, major - b), (minor - c, major - d)) == [
            [1, 4], [1, 4], [1, 2], [1, 2]]
        assert a == c == {donor['root']} and marks <= b & d
        assert len((major - b) & (major - d)) in (0, 2)
        return
    inner = donor['inner']
    side = donor.get('side', donor.get('inner_side'))
    assert inner in AXES and inner != outer and side in (0, 1)
    a, b = (face(g, inner, side) for g in (minor, major))
    c, d = minor - a, major - b
    actual_counts = shape((a, b), (c, d))
    if kind == 'T26_separated_two_root_choice':
        assert actual_counts == [[2, 3], [0, 3]] and len(marks & b) == len(marks & d) == 1
        mirrors = {x ^ (1 << inner) for x in a}
        assert not (mirrors & d & marks) or mirrors & (d - marks)
    elif kind == 'T15_isolated_mark':
        assert actual_counts == [[0, 1], [1, 4]] and b == {donor['isolated_mark']} <= marks
    else:
        assert marks <= b
        if kind in {'Q6_same_side_majority_root', 'Q6_same_side_two_minority_roots'}:
            whole_face(minor, major, marks, outer, inner, side,
                       'majority_root' if kind == 'Q6_same_side_majority_root' else 'two_minority_roots',
                       donor['face_counts'])
        elif kind == 'Q6_balanced_complement_avoid_two':
            (f, g), (h, k) = actual_counts
            assert actual_counts == donor['face_counts']
            assert f in (0, 1) and g == f + 4 and 1 <= h == k <= 16
        elif kind == 'T26_two_majority_roots':
            assert actual_counts == [[0, 6], [2, 0]]
        else:
            assert kind == 'Q6_T15_D4' and actual_counts == donor['face_counts'] == [[0, 4], [1, 1]]


def actual_returns(p, outer, a, b, k):
    r, s = len(a[0]), len(b[1])
    assert shape(a, b) == [[r, r + k], [s + k, s]] and r + s + k == 8
    x, u = set(p['X']), set(p['U'])
    assert len(x) == len(p['X']) == k - 2 and x <= a[1]
    assert len(u) == len(p['U']) == 2 and u <= b[0]
    y, v = ({z ^ (1 << outer) for z in g} for g in (x, u))
    assert not ((y | v) & set.union(*a, *b))
    donor_retained, receiver_retained = a[1] - x, b[0] - u
    assert shape((a[0], donor_retained | v), (receiver_retained | y, b[1])) == [[r, r + 4], [s + 2*k - 4, s]]
    return donor_retained, v, receiver_retained, y


def whole_receiver_k3(p, outer, a, b, registry, cores):
    retained, v, rb, y = actual_returns(p, outer, a, b, 3)
    for name, group in (('Y', y), ('V', v), ('A_minor', a[0]), ('A_retained', retained),
                        ('B_minor', b[1]), ('B_new_major', rb | y)):
        fixed_group(group, p[name])
    inner = p['B_inner']
    assert inner in AXES and inner != outer
    mark, = y
    side = bit(mark, inner)
    differences = [len(face(rb | y, inner, i)) - len(face(b[1], inner, i)) for i in (0, 1)]
    assert differences == p['B_deltas'] and p['B_marked_side'] == side
    assert differences[side] == 2 and differences[1 - side] == 0
    double_omit(p['donor'], a[0], retained | v, v, outer, registry, cores)


def split_shape(minor, major, marks, q, name):
    assert marks <= major and len(marks) == q and len(major) - len(minor) == 2*q
    if name in ('avoid_one', 'Q5_A_ALL'):
        assert q == 1 and len(minor) <= 14
    elif name == 'T44':
        assert q == 2 and not minor
    else:
        assert name == 'T15' and q == 2 and len(minor) == 1


def projected_split(receiver, outer, minor, major, marks, t63=None):
    inner = receiver['inner']
    assert inner in AXES and inner != outer
    axes = [i for i in AXES if i not in (outer, inner)]
    assert axes == receiver['projected_axes'] and len(receiver['faces']) == 2
    for side, row in enumerate(receiver['faces']):
        n, m, y = (set(project(face(group, inner, side), axes)) for group in (minor, major, marks))
        for label, group in (('minority', n), ('majority', m), ('marks', y)):
            fixed_group(group, row[label])
        interface = row['interface']
        kind = interface['kind']
        if kind == 'T63_new':
            assert t63 is not None and not n and len(m) == 6 and len(y) == 3 and y <= m
            assert interface['rank'] == 6
            shift, perm = interface['local_to_rank_xor'], interface['local_to_rank_permutation']
            assert 0 <= shift < 32 and sorted(perm) == list(range(5))
            assert tuple({permuted(x ^ shift, perm) for x in group} for group in (m, y)) == t63
        else:
            split_shape(n, m, y, len(y), kind)


def k4(p, outer, a, b, registry, fallback):
    retained, v, rb, y = actual_returns(p, outer, a, b, 4)
    for label, group in (('Y', y), ('V', v), ('H_prime_A', a[0] | retained | v),
                         ('H_prime_B', rb | y | b[1])):
        fixed_group(group, p[label])
    assert p['B_side'] == 1 - p['A_side'] and p['beta_parity'] == 1 - p['alpha_parity']
    assert p['H_prime_A_by_alpha_beta'] == list(map(sorted, (a[0], retained | v)))
    assert p['H_prime_B_by_alpha_beta'] == list(map(sorted, (rb | y, b[1])))
    supplier, receiver = p['supplier'], p['receiver']
    supplier_kind, mode = supplier['kind'], receiver['mode']
    fallback[(supplier_kind, mode)] += 1
    if supplier_kind == 'core117':
        assert supplier['projected_axes'] == [i for i in AXES if i != outer]
        exact_core(a[0], retained | v, v, outer, 117, supplier['root'],
                   [supplier['normalized_retained'], supplier['normalized_marks']],
                   supplier['coordinate_transport'], registry)
    else:
        whole_face(a[0], retained | v, v, outer, supplier['inner'], supplier['mark_side'],
                   supplier_kind, supplier['hole_counts'])
    inner = receiver['inner']
    assert inner in AXES and inner != outer
    minor, major = b[1], rb | y
    if mode == 'whole_face':
        whole_face(minor, major, y, outer, inner, receiver['mark_side'], receiver['kind'],
                   receiver['hole_counts'])
    elif mode == 'positive_split':
        assert [row['side'] for row in receiver['sides']] == [0, 1]
        for side, row in enumerate(receiver['sides']):
            n, m, z = (face(g, inner, side) for g in (minor, major, y))
            assert [len(n), len(m)] == row['hole_counts']
            for key, group in (('minority', n), ('majority', m), ('marks', z)):
                fixed_group(group, row[key])
            split_shape(n, m, z, 1, row['interface'])
    else:
        assert mode == 'controlled_single_root'
        z, t = receiver['Z_side'], receiver['T_side']
        assert z in (0, 1) and t == 1 - z
        root, mirror = receiver['a'], receiver['w']
        f, g = (face(group, inner, z) for group in (minor, major))
        h, j = minor - f, major - g
        assert root in f and mirror == root ^ (1 << inner) and mirror not in y
        assert receiver['p'] == len(f) and receiver['q'] == len(h)
        assert shape((f, g), (h, j)) == receiver['hole_counts']
        marks = [len(y & g), len(y & j)]
        assert marks == receiver['mark_counts']
        if receiver['kind'] == 'same_side':
            assert len(f) in (1, 2) and len(g) - len(f) == 3 and len(j) - len(h) == 1 and marks == [2, 0]
        else:
            assert receiver['kind'] == 'separated' and len(f) >= 1 and len(h) in (0, 1)
            assert len(g) - len(f) == 1 and len(j) - len(h) == 3 and marks == [1, 1]
    return supplier_kind, mode, receiver.get('kind')


def verify_plans(plans, colors, registry, t63):
    entries = plans['positives']
    assert plans['status'] == 'complete' and plans['first_failure'] is None
    assert len(entries) == plans['input_representatives'] == plans['visited'] == len(colors)
    assert {x['index'] for x in entries} == set(colors)
    assert all(plans[k] == 0 for k in ('unvisited', 'original_matchings_enumerated', 'solver_calls', 'rank_runs', 'new_geometries'))
    counts, k3_donors, k3_cores, broad_cores, fallback, k4_receivers, modes, rk, high = (Counter() for _ in range(9))
    broad, registered = [], []
    for entry in entries:
        index, p = entry['index'], entry['plan']
        gate = p['gate']
        counts[gate] += 1
        try:
            if gate == 'accepted_high_m':
                high_m(colors[index], p['witnesses'])
                high['+'.join(sorted(p['witnesses']))] += 1
                continue
            side_field = 'donor_side' if gate in {
                'four_mono_capacity', 'controlled_cycle_registered_split', 'registry_two_return'} else 'A_side'
            if gate == 'registry_two_return':
                p = dict(p, alpha_parity=1 - p['donor_majority_parity'])
            outer, a, b = directed_cut(colors[index], p, side_field)
            if gate == 'E16_monochromatic_delta3':
                assert shape(a, b) == p['shape'] == [[5, 8], [3, 0]]
            elif gate == 'four_mono_capacity':
                assert shape(a, b) == p['shape'] == [[4, 8], [4, 0]]
                assert list(map(sorted, a)) == p['original_A_by_alpha_beta']
                assert list(map(sorted, b)) == p['original_B_by_alpha_beta']
                axes = [t for t in AXES if t != outer and len(face(b[0], t, 1)) == 2]
                assert axes == p['split_axes'] and len(axes) in (3, 4, 5, 6)
                assert len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(axes)]
            elif gate == 'controlled_cycle_count':
                one_send(p, outer, a, b, modes)
                rk[f"{p['r']},{p['k']}"] += 1
            elif gate == 'k3_whole_receiver':
                whole_receiver_k3(p, outer, a, b, registry, k3_cores)
                k3_donors[p['donor']['kind']] += 1
            elif gate == 'k4_two_return':
                _, mode, receiver_kind = k4(p, outer, a, b, registry, fallback)
                k4_receivers[f'{mode}:{receiver_kind}'] += 1
            elif gate == 'registry_two_return':
                k = p['k']
                assert p['required_forced_edge'] is None and k in (4, 5)
                retained, v, rb, y = actual_returns(p, outer, a, b, k)
                for key, group in (('donor_minority', a[0]), ('donor_retained', retained), ('donor_marks', v),
                                   ('receiver_minority', b[1]), ('receiver_retained', rb), ('receiver_marks', y)):
                    fixed_group(group, p[key])
                double_omit(p['donor'], a[0], retained | v, v, outer, registry, broad_cores)
                receiver = p['receiver']
                assert receiver['kind'] == 'positive_split_Q5'
                projected_split(receiver, outer, b[1], rb | y, y)
                broad.append(index)
            else:
                assert gate == 'controlled_cycle_registered_split' and p['r'] == p['k'] == 4
                assert shape(a, b) == [[4, 8], [4, 0]]
                source = set(p['sources'])
                assert len(source) == len(p['sources']) == 4 and source <= a[1]
                y = {x ^ (1 << outer) for x in source}
                assert not y & set.union(*a, *b)
                fixed_group(y, p['marks'])
                fixed_group(b[1], p['receiver_minority'])
                fixed_group(b[0], p['receiver_majority'])
                projected_split(p['receiver'], outer, b[1], b[0] | y, y, t63)
                assert {x['interface']['kind'] for x in p['receiver']['faces']} == {'Q5_A_ALL', 'T63_new'}
                registered.append(index)
        except (AssertionError, KeyError, ValueError) as exc:
            raise AssertionError((index, gate)) from exc

    assert counts == plans['plan_counts'] and k3_donors == plans['k3_donor_counts']
    assert high == {'R41': 4896, 'R32': 708, 'R32+R41': 310}
    assert rk == {'3,3': 26705, '4,3': 3718, '3,4': 2021, '4,4': 40}
    assert modes == {'Q5_A_ALL': 30423, 'Q5_T44': 7447, 'Q5_T15_FULL': 27098}
    assert k3_cores == {85: 14, 113: 23, 117: 23, 407: 1, 692: 40, 697: 9, 950: 5, 1048: 12, 1054: 7}
    assert broad_cores == {113: 1} and broad == [53, 65, 478, 479] and registered == [3422]
    assert Counter({kind: sum(v for (k, _), v in fallback.items() if k == kind)
                    for kind in ('majority_root', 'two_minority_roots', 'core117')}) == {
        'majority_root': 262, 'two_minority_roots': 57, 'core117': 16}
    assert k4_receivers == {'whole_face:majority_root': 111, 'whole_face:two_minority_roots': 3,
                            'positive_split:None': 64, 'controlled_single_root:same_side': 19,
                            'controlled_single_root:separated': 138}
    return dict(plan_counts=counts, k3_donors=k3_donors, k3_cores=k3_cores, broad_cores=broad_cores,
                fallback={':'.join(k): v for k, v in sorted(fallback.items())},
                k4_receivers=k4_receivers, controlled_modes=modes, controlled_rk=rk, high_m=high,
                registry_two_return_indices=broad, registered_single_forward_indices=registered)


def imports():
    profile_name = 'Q6_T15_ACTUAL_PROFILE.json'
    profile = {x['index']: [x['included'], x['omitted']] for x in read(SEVEN / profile_name)['orbits']}
    good = read(SEVEN / 'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
    s2 = read(SEVEN / 'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json')
    assert good['verdict'] == s2['verdict'] == 'PASS'
    assert good['audited_input_hashes'][profile_name] == s2['audited_input_hashes'][profile_name] == 'sha256:' + digest(SEVEN / profile_name)
    accepted = set(good['union_closed_core_indices'])
    assert len(accepted) == 1017
    assert accepted == set(good['closed_core_indices']) | set(s2['union_closed_core_indices'])
    assert 113 in good['closed_core_indices']
    for i, target in ((85, [[31, 47, 55], [1, 2]]), (1054, [[28, 61, 62], [7, 11]])):
        stem = f'Q6_T15_CORE{i}_MARKED'
        receipt = read(SEVEN / (stem + '_REVIEW.json'))
        assert receipt['verdict'] == 'PASS' and receipt[f'core{i}_universal_proved']
        for name in (stem + '_CLOSURE.md', profile_name):
            assert receipt['audited_input_hashes'][name] == 'sha256:' + digest(SEVEN / name)
        assert i not in accepted and profile[i] == target
        accepted.add(i)
    controlled = read(HERE / 'R7_MU3_CONTROLLED_AND_T63_REVIEW.json')
    assert controlled['verdict'] == 'PASS'
    t63_data = 'R7_MU3_T63_NEW_RANK_INPUTS.json'
    t63_results = 'R7_MU3_T63_NEW_RANK_REVIEW_CHECK.json'
    for name in (t63_data, 'R7_MU3_T63_NEW_RANK.md'):
        assert controlled['audited_input_hashes'][name] == 'sha256:' + digest(HERE / name)
    assert controlled['evidence_hashes'][t63_results] == 'sha256:' + digest(HERE / t63_results)
    row, = [x for x in read(HERE / t63_data)['targets'] if x['target_class'] == 6]
    verified, = [x for x in read(HERE / t63_results)['verified'] if x['target_class'] == 6]
    t63 = set(row['H']), set(row['U'])
    assert t63 == (set(verified['H']), set(verified['U'])) == ({0, 3, 5, 15, 24, 30}, {0, 24, 30})
    return {i: profile[i] for i in accepted}, t63


def main():
    start = process_time()
    path = HERE / (PREFIX + 'CLOSURE_INPUTS.json')
    assert digest(path) == MANIFEST_HASH
    manifest = read(path)
    hashes = manifest['sha256']
    assert len(hashes) == 129
    for name, expected in hashes.items():
        assert digest(HERE / name) == expected, name
    for name in ('R7_MU1_CENTRAL_T1_AND_E14_REVIEW.json', 'R7_MU3_THREE_BRIDGE_FULL_REVIEW.json',
                 'R7_E16_MU3_GAP7_EVEN_D30_REVIEW.json'):
        assert read(HERE / name)['verdict'] == 'PASS'
    base_path, plan_path = (HERE / (PREFIX + s) for s in ('BASE.json', 'FIXED_PLANS.json'))
    base = read(base_path)
    colors, basis, bucket_mass = verify_basis(base)
    print('Independent basis verified', flush=True)
    plans = read(plan_path)
    assert plans['base_sha256'] == digest(base_path)
    registry, t63 = imports()
    checks = verify_plans(plans, colors, registry, t63)
    assert checks['plan_counts'] == manifest['odd_plan_counts']
    assert checks['k3_donors'] == manifest['odd_k3_donor_counts']
    assert sorted(checks['k3_cores']) == manifest['exact_T15_targets']
    assert len(colors) == manifest['odd_marked_representatives']
    assert bucket_mass == manifest['odd_bucket_hits_before_final_stabilizer']
    elapsed = process_time() - start
    assert elapsed < 90
    output = dict(manifest_sha256=MANIFEST_HASH, bindings=len(hashes), representatives=len(colors),
                  basis=basis, final_bucket_mass=bucket_mass, cpu_seconds=elapsed, cpu_budget=90,
                  producer_runs=0, plan_searches=0, matching_enumerations=0, solver_calls=0,
                  rank_runs=0, old_certificate_replays=0, **checks)
    (HERE / (PREFIX + 'REVIEW_CHECK.json')).write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(f'Fixed plan verification completed in {elapsed:.4f} CPU seconds')


if __name__ == '__main__':
    main()
