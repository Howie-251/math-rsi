"""Independent verification of frozen marked gap-six geometry and plans."""

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb
from time import process_time
import json

from R7_E16_MU3_GAP7_EVEN_MINIMAL_REVIEW_CHECK import (
    AXES, HERE, S6, SEVEN, bit, digest, directed_cut, face, fixed_group,
    graph_count, image, loads, one_send, permuted, read, shape,
)
from R7_E16_MU3_GAP7_EVEN_D30_REVIEW_CHECK import high_m
from R7_E16_MU3_GAP7_ODD_REVIEW_CHECK import (
    actual_returns, double_omit, k4, project,
)


PREFIX = 'R7_E16_MU3_GAP6_EVEN_02_'
MANIFEST_SHA = '4a650aaa1b1d5a8b8798e0d51ce280a309e2d8d81f7c0800d7b2bc129a7df817'
CPU_LIMIT = 90
LOW = tuple(range(6))
TRANSPORTS = tuple(tuple((x & 64) | permuted(x & 63, p) for x in range(128)) for p in S6)


def deadline(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError('independent audit exceeded CPU budget')


def labeled_right_count(left):
    degree = loads(left, LOW)
    result = 0
    for endpoints in combinations(LOW, 2):
        base = tuple(d + (i in endpoints) for i, d in enumerate(degree))
        ranges = [range(max(0, 2 - d), 6 - d) for d in base]
        for target in product(*ranges):
            if sum(target) == 10:
                result += graph_count(tuple(sorted(target, reverse=True)))
    return result


def verify_basis(base, start):
    assert base['status'] == 'complete' and base['original_matchings_enumerated'] == 0
    first_rows = {tuple(row['first']): row for row in base['first_information']}
    assert len(first_rows) == len(base['first_information']) == 24
    stabilizers, first_keys = {}, set()
    independent = {}
    for first, row in first_rows.items():
        deadline(start)
        assert len(first) == len(set(first)) == 7
        assert all(0 < v < 64 and v.bit_count() == 2 for v in first)
        first = tuple(sorted(first))
        orbit = tuple(image(first, t) for t in TRANSPORTS)
        assert min(orbit) not in first_keys
        first_keys.add(min(orbit))
        stab = tuple(t for t, transformed in zip(TRANSPORTS, orbit) if transformed == first)
        assert len(stab) == row['stabilizer_order']
        stabilizers[first] = stab
        independent[first] = labeled_right_count(first)
    assert sum(720 // len(stab) for stab in stabilizers.values()) == comb(15, 7)

    right_keys, full_mass = defaultdict(set), Counter()
    partial_mass, final_sizes, load_two_axes, eligible_axes, spectra = (Counter() for _ in range(5))
    colors = {}
    for i, row in enumerate(base['records']):
        if i % 512 == 0:
            deadline(start)
        left, right = tuple(row['L']), tuple(row['V'])
        first = tuple(sorted(set(left) - {0}))
        assert len(left) == len(right) == len(set(left)) == len(set(right)) == 8
        assert 0 in left and 0 in right and first in stabilizers and row['case'] == 'degree_0_2'
        assert all(0 <= x < 128 and x.bit_count() == 2 for x in right if x)
        high = tuple(sorted(x for x in right if x & 64))
        assert len(high) == 2
        left_load, right_load = loads(left), loads(right)
        columns = tuple(a + b for a, b in zip(left_load, right_load))
        assert list(columns) == row['column_loads'] and columns[-1] == 2
        assert min(columns) == 2 and max(columns) == 5 and sum(columns) == 28
        assert all(2 <= c <= 5 for c in columns)
        orbit = {image(right, t) for t in stabilizers[first]}
        key = min(orbit)
        assert key not in right_keys[first]
        right_keys[first].add(key)
        full_mass[first] += len(orbit)
        final_orbit = {image(right, t) for t in stabilizers[first]
                       if image(high, t) == high and
                       all(columns[i] == columns[t[1 << i].bit_length() - 1] for i in LOW)}
        size = len(final_orbit)
        assert size > 0
        final_sizes[size] += 1
        partial_mass[first] += size
        selectable = sum((a, b) in {(0, 2), (2, 0)} for a, b in zip(left_load, right_load))
        assert selectable in (1, 2)
        eligible_axes[selectable] += 1
        load_two_axes[columns.count(2)] += 1
        holes = (set(left), {127 ^ v for v in right})
        assert all((v.bit_count() & 1) == parity for parity, group in enumerate(holes) for v in group)
        assert all((x ^ y).bit_count() >= 3 for x in holes[0] for y in holes[1])
        gaps = tuple(a - b for a, b in zip(*(loads(group) for group in holes)))
        assert gaps == tuple(c - 8 for c in columns) and min(map(abs, gaps)) == 3
        spectra[tuple(sorted(map(abs, gaps)))] += 1
        colors[i] = holes

    assert all(full_mass[g] == count for g, count in independent.items())
    assert len(colors) == base['record_count'] == 59129
    assert sum(partial_mass.values()) == 65617
    assert {int(k): n for k, n in base['orbit_size_multiplicities'].items()} == final_sizes
    assert load_two_axes == {1: 51669, 2: 7460}
    for g, row in first_rows.items():
        assert len(right_keys[g]) == row.get('representatives', 0)
        assert partial_mass[g] == row.get('bucket_multiplicity', 0)

    result = dict(first_orbits=len(stabilizers), representatives=len(colors),
                  labeled_right_count=sum(independent.values()),
                  labeled_right_count_by_first=[[list(g), independent[g]] for g in sorted(independent)],
                  final_orbit_sizes=final_sizes, final_bucket_mass=sum(partial_mass.values()),
                  load_two_axes=load_two_axes, eligible_02_marked_axes=eligible_axes,
                  spectra=[[list(k), v] for k, v in sorted(spectra.items())])
    return colors, result


def whole_receiver_k3(p, outer, a, b, registry, cores):
    retained, returned, rb, marks = actual_returns(p, outer, a, b, 3)
    for name, group in (('Y', marks), ('V', returned), ('A_minor', a[0]), ('A_retained', retained),
                        ('B_minor', b[1]), ('B_new_major', rb | marks)):
        fixed_group(group, p[name])
    inner = p['B_inner']
    assert inner in AXES and inner != outer
    mark, = marks
    side = bit(mark, inner)
    differences = [len(face(rb | marks, inner, i)) - len(face(b[1], inner, i)) for i in (0, 1)]
    assert differences == p['B_deltas'] and p['B_marked_side'] == side
    assert differences[side] == 2 and differences[1 - side] == 0

    donor = p['donor']
    majority = retained | returned
    if donor['kind'] == 'T15_same_face':
        i, side = donor['inner'], donor.get('side', donor.get('inner_side'))
        assert i in AXES and i != outer and side in (0, 1)
        assert len(a[0]) == 1 and len(majority) == 5 and len(returned) == 2
        assert all(bit(v, i) == side for v in a[0] | majority)
        if 'face_counts' in donor:
            assert donor['face_counts'] == [[1, 5], [0, 0]]
    else:
        double_omit(donor, a[0], majority, returned, outer, registry, cores)


def check_single_fallback(p, outer, a, b, t63):
    r, k = p['r'], p['k']
    assert r == 4 and k in (3, 4) and shape(a, b) == [[r, r + k], [8-r, 8-r-k]]
    sources = set(p['sources'])
    assert len(sources) == len(p['sources']) == k and sources <= a[1]
    marks = {x ^ (1 << outer) for x in sources}
    original_holes = set.union(*a, *b)
    assert not marks & original_holes
    fixed_group(marks, p['marks'])
    fixed_group(b[1], p['receiver_minority'])
    fixed_group(b[0], p['receiver_majority'])
    if p['gate'] == 'universal_delta3':
        assert k == 3
        inner, root, mirror = p['inner'], p['root'], p['mirror']
        assert inner in AXES and inner != outer and b[1] == {root}
        assert mirror == root ^ (1 << inner) and mirror not in marks | original_holes
        z = bit(root, inner)
        assert len(face(b[0], inner, z)) == 2
        assert len(face(marks, inner, z)) == 2
    else:
        assert k == 4
        receiver = p['receiver']
        inner = receiver['inner']
        assert inner in AXES and inner != outer
        axes = [i for i in AXES if i not in (inner, outer)]
        assert axes == receiver['projected_axes'] and len(receiver['faces']) == 2
        exact_call = None
        for side, row in enumerate(receiver['faces']):
            n, m, y = (set(project(face(g, inner, side), axes)) for g in (b[1], b[0] | marks, marks))
            for key, group in (('minority', n), ('majority', m), ('marks', y)):
                fixed_group(group, row[key])
            interface = row['interface']
            kind = interface['kind']
            assert y <= m and len(m) - len(n) == 2 * len(y)
            if kind == 'Q5_A_ALL':
                assert len(y) == 1 and len(n) <= 14
                continue
            assert exact_call is None and not n and len(m) == 6 and len(y) == 3
            rank = interface['rank']
            exact_call = (kind, rank)
            target = t63[exact_call]
            if kind == 'T63_old':
                perm, shift = interface['rank_to_local_permutation'], interface['rank_to_local_xor']
                assert sorted(perm) == list(range(5)) and 0 <= shift < 32
                assert tuple({permuted(x, perm) ^ shift for x in group} for group in target) == (m, y)
            else:
                assert kind == 'T63_new'
                shift, perm = interface['local_to_rank_xor'], interface['local_to_rank_permutation']
                assert sorted(perm) == list(range(5)) and 0 <= shift < 32
                assert tuple({permuted(x ^ shift, perm) for x in group} for group in (m, y)) == target
        assert exact_call is not None
        return exact_call


def verify_plans(plans, colors, registry, t63, start):
    entries = plans['positives']
    assert plans['status'] == 'complete' and plans['first_failure'] is None
    assert len(entries) == plans['input_representatives'] == plans['visited'] == len(colors)
    assert {x['index'] for x in entries} == set(colors)
    assert all(plans[k] == 0 for k in ('unvisited', 'original_matchings_enumerated', 'solver_calls',
                                       'rank_runs', 'new_geometries'))
    counts, k3_donors, k3_cores, k4_tools, k4_receivers, modes, rk, high = (Counter() for _ in range(8))
    small_gates, registered = defaultdict(list), {}
    same_face = []
    for entry in entries:
        index, p = entry['index'], entry['plan']
        if index % 512 == 0:
            deadline(start)
        gate = p['gate']
        counts[gate] += 1
        try:
            assert p.get('required_forced_edge') is None
            if gate == 'accepted_high_m':
                assert set(p['witnesses']) == {'R41'}
                high_m(colors[index], p['witnesses'])
                high['+'.join(sorted(p['witnesses']))] += 1
                continue
            side_field = 'donor_side' if gate in {
                'four_mono_capacity', 'controlled_cycle_registered_split', 'universal_delta3'} else 'A_side'
            outer, a, b = directed_cut(colors[index], p, side_field)
            if gate == 'E16_monochromatic_delta3':
                assert shape(a, b) == p['shape'] == [[5, 8], [3, 0]]
            elif gate == 'four_mono_capacity':
                assert shape(a, b) == p['shape'] == [[4, 8], [4, 0]]
                assert list(map(sorted, a)) == p['original_A_by_alpha_beta']
                assert list(map(sorted, b)) == p['original_B_by_alpha_beta']
                axes = [i for i in AXES if i != outer and len(face(b[0], i, 1)) == 2]
                assert axes == p['split_axes'] and len(axes) in (3, 4, 5, 6)
                assert len(a[1]) > {3: 7, 4: 6, 5: 6, 6: 7}[len(axes)]
            elif gate == 'controlled_cycle_count':
                one_send(p, outer, a, b, modes)
                rk[f"{p['r']},{p['k']}"] += 1
            elif gate == 'k3_whole_receiver':
                whole_receiver_k3(p, outer, a, b, registry, k3_cores)
                k3_donors[p['donor']['kind']] += 1
                if p['donor']['kind'] == 'T15_same_face':
                    same_face.append(index)
            elif gate == 'k4_two_return':
                _, mode, kind = k4(p, outer, a, b, registry, k4_tools)
                assert (mode, kind) == ('controlled_single_root', 'separated')
                k4_receivers[f'{mode}:{kind}'] += 1
                small_gates[gate].append(index)
            else:
                assert gate in {'universal_delta3', 'controlled_cycle_registered_split'}
                exact = check_single_fallback(p, outer, a, b, t63)
                if exact is not None:
                    registered[index] = exact
                small_gates[gate].append(index)
        except (AssertionError, KeyError, ValueError) as exc:
            raise AssertionError((index, gate)) from exc

    assert counts == plans['plan_counts'] and k3_donors == plans['k3_donor_counts']
    return dict(plan_counts=counts, k3_donors=k3_donors, k3_cores=k3_cores,
                k4_tools={':'.join(k): v for k, v in sorted(k4_tools.items())},
                k4_receivers=k4_receivers, controlled_modes=modes, controlled_rk=rk,
                high_m=high, small_gate_indices=dict(small_gates), registered_T63=registered,
                k3_same_face_indices=same_face)


def verify_imports():
    profile_path = SEVEN / 'Q6_T15_ACTUAL_PROFILE.json'
    profile = {r['index']: [r['included'], r['omitted']] for r in read(profile_path)['orbits']}
    good = read(SEVEN / 'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
    s2 = read(SEVEN / 'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json')
    union = set(good['union_closed_core_indices'])
    assert len(union) == 1017 and union == set(good['closed_core_indices']) | set(s2['union_closed_core_indices'])
    closed = read(SEVEN / 'Q6_T15_GOOD_ROOT_ALL_CLOSED.json')
    assert {r['core_index'] for r in closed['cores']} == union
    for receipt in (good, s2):
        assert receipt['verdict'] == 'PASS'
        assert receipt['audited_input_hashes'][profile_path.name] == 'sha256:' + digest(profile_path)

    easy_path = SEVEN / 'Q6_TWO_AVOIDED_EASY_FACES.md'
    easy = read(SEVEN / 'Q6_TWO_AVOIDED_EASY_REVIEW.json')
    assert easy['verdict'] == 'PASS'
    assert easy['audited_input_hashes'][easy_path.name] == 'sha256:' + digest(easy_path)

    six = SEVEN.parent / 'six_directions'
    old_path = six / 'Q5_T63_RANK_PROOF.md'
    old_receipt = read(six / 'Q5_T63_RANK_REVIEW.json')
    assert old_receipt['verdict'] == 'PASS'
    assert old_receipt['audited_input_hashes'][old_path.name] == digest(old_path)
    old_target = {0, 3, 5, 10, 20, 30}, {0, 3, 5}
    assert '|0|0,3,5,10,20,30|0,3,5|' in old_path.read_text(encoding='utf-8')

    new_proof = HERE / 'R7_MU3_T63_NEW_RANK.md'
    new_inputs = HERE / 'R7_MU3_T63_NEW_RANK_INPUTS.json'
    new_checks = HERE / 'R7_MU3_T63_NEW_RANK_REVIEW_CHECK.json'
    new_receipt = read(HERE / 'R7_MU3_CONTROLLED_AND_T63_REVIEW.json')
    assert new_receipt['verdict'] == 'PASS'
    for path in (new_proof, new_inputs):
        assert new_receipt['audited_input_hashes'][path.name] == 'sha256:' + digest(path)
    assert new_receipt['evidence_hashes'][new_checks.name] == 'sha256:' + digest(new_checks)
    new_evidence = read(new_checks)
    assert new_evidence['inputs_sha256'] == digest(new_inputs)
    assert new_evidence['proof_sha256'] == digest(new_proof)
    target, = (r for r in read(new_inputs)['targets'] if r['target_class'] == 2)
    verified, = (r for r in new_evidence['verified'] if r['target_class'] == 2)
    assert verified['verifier'] == 'PASS forests=4096 columns=4096 bits=16777216 rank=4096'
    new_target = set(target['H']), set(target['U'])
    assert new_target == (set(verified['H']), set(verified['U'])) == ({0, 3, 5, 6, 9, 30}, {0, 9, 30})

    universal = 'R7_CYCLE_DONOR_THREE_BRIDGE_UNIVERSAL'
    universal_receipt = read(HERE / (universal + '_REVIEW.json'))
    assert universal_receipt['verdict'] == 'PASS'
    for name in (universal + '.md', universal + '_INPUTS.json'):
        assert universal_receipt['audited_input_hashes'][name] == 'sha256:' + digest(HERE / name)
    return {i: profile[i] for i in union}, {('T63_old', 0): old_target, ('T63_new', 2): new_target}


def verify_excerpts(excerpts, base, plans, checked, registry, hashes):
    assert excerpts['base_sha256'] == hashes[PREFIX + 'BASE.json']
    assert excerpts['plans_sha256'] == hashes[PREFIX + 'FIXED_PLANS.json']
    plans_by_id = {r['index']: r['plan'] for r in plans['positives']}
    assert set(excerpts['selected_plans']) == set(checked['small_gate_indices'])
    for gate, records in [*excerpts['selected_plans'].items(),
                          ('k3_same_face', excerpts['k3_T15_same_face_plans'])]:
        expected = (checked['k3_same_face_indices'] if gate == 'k3_same_face'
                    else checked['small_gate_indices'][gate])
        assert [r['index'] for r in records] == expected
        for row in records:
            assert row['basis_record'] == base['records'][row['index']]
            assert row['plan'] == plans_by_id[row['index']]
    actual_counts = {}
    for row in excerpts['T15_exact_targets']:
        i = row['index']
        assert i not in actual_counts and registry[i] == [row['included'], row['omitted']]
        actual_counts[i] = row['uses']
    assert actual_counts == checked['k3_cores']
    for name, sha in excerpts['exact_and_same_face_import_sha256'].items():
        assert digest(HERE / name) == sha


def main(start):
    manifest_path = HERE / (PREFIX + 'CLOSURE_INPUTS.json')
    assert digest(manifest_path) == MANIFEST_SHA
    manifest = read(manifest_path)
    hashes = manifest['sha256']
    assert len(hashes) == 152
    for name, expected in hashes.items():
        assert digest(HERE / name) == expected, name
    for name in ('R7_MU3_THREE_BRIDGE_FULL_REVIEW.json', 'R7_E16_MU3_GAP7_ODD_REVIEW.json'):
        assert read(HERE / name)['verdict'] == 'PASS'
    registry, t63 = verify_imports()

    base, plans, excerpts = (read(HERE / (PREFIX + suffix)) for suffix in
                            ('BASE.json', 'FIXED_PLANS.json', 'PLAN_EXCERPTS.json'))
    assert plans['base_sha256'] == hashes[PREFIX + 'BASE.json']
    colors, basis = verify_basis(base, start)
    print(f"Independent labeled-right mass: {basis['labeled_right_count']}", flush=True)
    checked = verify_plans(plans, colors, registry, t63, start)
    verify_excerpts(excerpts, base, plans, checked, registry, hashes)
    assert len(colors) == manifest['marked_gap6_representatives']
    assert basis['final_bucket_mass'] == manifest['bucket_multiplicity']
    assert checked['plan_counts'] == manifest['plan_counts']
    assert checked['k3_donors'] == manifest['k3_donor_counts']
    assert checked['k3_cores'] == {int(k): n for k, n in manifest['exact_T15_targets'].items()}
    assert checked['registered_T63'] == {749: ('T63_old', 0), 2960: ('T63_new', 2)}
    assert checked['controlled_rk'] == {'3,3': 21719, '4,3': 13875, '3,4': 7790, '4,4': 2189}
    assert checked['controlled_modes'] == {'Q5_A_ALL': 35594, 'Q5_T44': 27799, 'Q5_T15_FULL': 27753}
    assert checked['small_gate_indices']['k4_two_return'] == [597, 2859, 3011, 3012]
    assert checked['k3_same_face_indices'] == [767, 772, 2139, 2154]
    deadline(start)
    result = dict(verdict='PASS', manifest_sha256=MANIFEST_SHA, verified_manifest_hashes=len(hashes),
                  cpu_seconds=process_time() - start, cpu_budget=CPU_LIMIT, basis=basis,
                  producer_runs=0, plan_searches=0, original_matchings_enumerated=0,
                  solver_calls=0, rank_runs=0, old_certificate_replays=0, **checked)
    out_path = HERE / (PREFIX + 'REVIEW_CHECK.json')
    with out_path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(f"Checked {len(colors)} plans in {result['cpu_seconds']:.6f} CPU seconds", flush=True)


if __name__ == '__main__':
    started = process_time()
    try:
        main(started)
    except Exception:
        print(f'Check failed after {process_time() - started:.6f} CPU seconds', flush=True)
        raise
