"""Independent D=24 source-basis and fixed-plan verifier, without searches or solvers."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from time import process_time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AXES = tuple(range(7))
BITS = (0, 1)
UNITS = tuple(1 << i for i in AXES)
TRIPLES = tuple(sum(axes) for axes in combinations(UNITS, 3))
ORBIT_MASSES = {
    (0, 'one_side'): 420, (0, 'outside'): 70,
    (1, 'common'): 315, (1, 'one_side'): 1260, (1, 'outside'): 630,
    (2, 'common'): 420, (2, 'one_side'): 420, (2, 'outside'): 630,
}


def read(path):
    return json.loads(path.read_bytes())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def in_face(vertices, axis, side):
    return {v for v in vertices if (v >> axis) & 1 == side}


def partition(vertices, axis):
    zeros = in_face(vertices, axis, 0)
    return zeros, vertices - zeros


def color(v):
    return v.bit_count() % 2


def directed(colors, axis, B_bit):
    receiver = tuple(in_face(g, axis, B_bit) for g in colors)
    assert len(receiver[0]) != len(receiver[1])
    alpha = int(len(receiver[1]) > len(receiver[0]))
    aa, ba = receiver[alpha], receiver[1-alpha]
    return alpha, (colors[alpha]-aa, colors[1-alpha]-ba), (aa, ba)


def donor_ok(r, a, ell):
    t = r - a
    return (
        a in (0, 1) and (
            ell == 4 and t >= 1 or ell == 5 and 1 <= t <= 16 or ell == 6 and t in (2, 3)
        )
        or a == 2 and ell == 3 and 0 <= t <= 15
        or a == 1 and ell == 3 and 1 <= r <= 15
    )


def early(colors, loads):
    # Only the three nonzero early routes in the submitted counter are used.
    directed_cuts = []
    for j, b in product(AXES, BITS):
        k = 8 - loads[j]
        if k not in (3, 4, 5):
            continue
        _, (am, aM), (bM, bm) = directed(colors, j, b)
        r, s = len(am), len(bm)
        assert len(aM) == r+k and len(bM) == s+k and r+s+k == 8
        directed_cuts.append((j, k, r, s, am, aM, bM, bm))
    for j, k, r, s, am, aM, bM, bm in directed_cuts:
        if (r, k, s) != (3, 3, 2):
            continue
        for i, t in product(AXES, BITS):
            if i == j or len(in_face(bM, i, t)) < 2:
                continue
            a, b = len(in_face(am, i, t)), len(in_face(aM, i, t))
            if any(donor_ok(r, a, b-int((x>>i)&1 == t)+2-a) for x in aM):
                return 'free_A6_same_side'
    for j, k, r, s, am, aM, bM, bm in directed_cuts:
        if s > 2:
            continue
        for i in AXES:
            if i == j:
                continue
            minors, majors, returns = map(lambda g: partition(g, i), (am, aM, bM))
            for xside in BITS:
                if not majors[xside]:
                    continue
                for q in product((1, 2), repeat=2):
                    if sum(q) == k-1 and all(
                        len(returns[t]) >= q[t]
                        and len(majors[t])-len(minors[t])-int(t == xside) == q[t]
                        and (q[t] == 1 or len(minors[t]) <= 1)
                        for t in BITS
                    ):
                        return 'split_small_receiver'
    for j, k, r, s, am, aM, bM, bm in directed_cuts:
        if (r, k, s) != (2, 3, 3):
            continue
        for x, i in product(aM, AXES):
            if i == j:
                continue
            sb = x >> i & 1
            recv = in_face(bM, i, sb)
            g = len(recv)-len(in_face(bm, i, sb))
            if not 1 <= g <= 3:
                continue
            for t_axis, t in product(AXES, BITS):
                if t_axis == j:
                    continue
                a, b = len(in_face(am, t_axis, t)), len(in_face(aM, t_axis, t))
                if not donor_ok(r, a, b-int((x>>t_axis)&1 == t)+2-a):
                    continue
                choices = in_face(bM, t_axis, t)
                if len(choices & recv) >= g-1 and len(choices-recv) >= 3-g:
                    return 'reverse_old_five'
    return 'outside_checked_gates'


def regenerate(data):
    expected = {}
    aggregate = Counter()
    orbit_keys = set()
    for idx, f in enumerate(data['families']):
        A, B, p = set(f['A']), set(f['B']), f['missing_unit']
        assert len(A) == len(B) == 3 and A | B <= set(AXES) and A != B and p in AXES
        t = len(A & B)
        pos = 'common' if p in A & B else 'one_side' if p in A | B else 'outside'
        orbit = (t, pos)
        assert (f['t'], f['position']) == orbit and orbit not in orbit_keys
        orbit_keys.add(orbit)
        assert f['first_group_orbit_mass'] == ORBIT_MASSES[orbit]
        pa, pb = (sum(UNITS[i] for i in g) for g in (A, B))
        P = (set(UNITS) - {UNITS[p]}) | {pa, pb}
        assert sorted(P) == f['P']
        counts = Counter()
        row = 0
        for q, (C, D) in product(AXES, combinations(TRIPLES, 2)):
            counts['generated'] += 1
            Q = (set(UNITS) - {UNITS[q]}) | {C, D}
            colors = ({127 ^ v for v in Q}, P)
            if any((v ^ u).bit_count() == 1 for v, u in product(*colors)):
                counts['reject_nonindependent'] += 1
                continue
            delta = [len(in_face(colors[0], j, 1)) - len(in_face(colors[1], j, 1)) for j in AXES]
            if min(delta) != 3 or max(delta) > 6:
                counts['reject_load'] += 1
                continue
            counts['admitted'] += 1
            loads = [8-d for d in delta]
            result = early(colors, loads)
            counts[result] += 1
            if result != 'outside_checked_gates':
                continue
            case = dict(q=q, C=C, D=D, Q=sorted(Q), lambda_by_axis=loads,
                        even_holes=sorted(colors[0]), odd_holes=sorted(P))
            assert case == f['surviving_inputs'][row], (idx, row, case)
            expected[idx, row] = case
            row += 1
        assert counts == f['counts'], (idx, counts, f['counts'])
        assert row == len(f['surviving_inputs']) and f['next_Q_parameter'] is None
        aggregate.update(counts)
    assert orbit_keys == set(ORBIT_MASSES) and sum(ORBIT_MASSES.values()) == 4165
    assert aggregate == data['total'] and data['complete']
    return expected, aggregate


def transport(v, axes):
    return sum(((v >> old) & 1) << new for new, old in enumerate(axes))


def permute(v, perm):
    return sum(((v >> old) & 1) << new for old, new in enumerate(perm))


def approved_targets():
    good = read(ROOT / 'Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json')
    s2 = read(ROOT / 'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json')
    profile = ROOT / 'Q6_T15_ACTUAL_PROFILE.json'
    for receipt in (good, s2):
        assert receipt['verdict'] == 'PASS'
        assert receipt['audited_input_hashes'][profile.name] == 'sha256:' + digest(profile)
    indices = set(good['union_closed_core_indices'])
    assert len(indices) == 1017
    assert indices == set(good['closed_core_indices']) | set(s2['union_closed_core_indices'])
    core = read(ROOT / 'Q6_T15_CORE1054_MARKED_REVIEW.json')
    assert core['verdict'] == 'PASS' and core['core1054_universal_proved']
    for f in (profile.name, 'Q6_T15_CORE1054_MARKED_CLOSURE.md'):
        assert core['audited_input_hashes'][f] == 'sha256:' + digest(ROOT / f)
    indices.add(1054)
    registry = {o['index']: (set(o['included']), set(o['omitted']))
                for o in read(profile)['orbits'] if o['index'] in indices}
    assert len(registry) == 1018 and registry[117] == ({31, 61, 62}, {1, 2})
    assert registry[1054] == ({28, 61, 62}, {7, 11})
    t63_receipt = read(ROOT / 'R7_MU3_CONTROLLED_AND_T63_REVIEW.json')
    assert t63_receipt['verdict'] == 'PASS'
    config, checked = ('R7_MU3_T63_NEW_RANK_INPUTS.json', 'R7_MU3_T63_NEW_RANK_REVIEW_CHECK.json')
    assert t63_receipt['audited_input_hashes'][config] == 'sha256:' + digest(ROOT / config)
    assert t63_receipt['evidence_hashes'][checked] == 'sha256:' + digest(ROOT / checked)
    def targets(records):
        return {row['target_class']: (set(row['H']), set(row['U'])) for row in records}
    t63 = targets(read(ROOT / config)['targets'])
    assert t63 == targets(read(ROOT / checked)['verified'])
    return registry, t63


def whole_face_test(minor, major, marks, spec, outer, side_key, count_key):
    i, t = spec['inner'], spec[side_key]
    assert i in AXES and i != outer and t in BITS
    a, b = in_face(minor, i, t), in_face(major, i, t)
    f, g, h, k = len(a), len(b), len(minor-a), len(major-b)
    assert marks <= b and len(marks) == 2
    assert [[f, g], [h, k]] == spec[count_key]
    return f, g, h, k


def majority_test(counts):
    f, g, h, k = counts
    assert f in (0, 1) and g == f+5 and 1 <= h <= 16 and k == h-1


def exact_test(minor, retained, marks, outer, spec, registry, index):
    assert len(minor) == 1 and len(retained) == 3 and len(marks) == 2
    root, = minor
    axes = [i for i in AXES if i != outer]
    if spec['kind'] == 'core117':
        assert spec['projected_axes'] == axes and spec['root'] == root
        recorded = [spec['normalized_retained'], spec['normalized_marks']]
    else:
        assert spec['normalization_root'] == root
        recorded = spec['normalized_groups']
    groups = [sorted(transport(v ^ root, axes) for v in g) for g in (retained, marks)]
    assert groups == recorded
    perm = spec['coordinate_transport']
    assert sorted(perm) == list(range(6))
    assert tuple({permute(v, perm) for v in g} for g in groups) == registry[index]


def verify_split(outer, bmin, bmaj, marks, spec, registry_t63, stats, k4):
    inner = spec['inner']
    assert inner in AXES and inner != outer
    axes = [i for i in AXES if i not in (outer, inner)]
    if not k4:
        assert spec['kind'] == 'positive_split_Q5' and spec['projected_axes'] == axes
    rows = spec['sides'] if k4 else spec['faces']
    assert len(rows) == 2
    for side, row in enumerate(rows):
        n, m, y = (in_face(g, inner, side) for g in (bmin, bmaj, marks))
        if k4:
            assert row['side'] == side and row['hole_counts'] == [len(n),len(m)]
            assert row['interface'] == 'Q5_A_ALL'
            kind = row['interface']
        else:
            n, m, y = ({transport(v, axes) for v in g} for g in (n, m, y))
            kind = row['interface']['kind']
        assert list(map(sorted, (n,m,y))) == [row['minority'],row['majority'],row['marks']]
        assert y <= m and y and len(m)-len(n) == 2*len(y)
        if kind in ('avoid_one', 'Q5_A_ALL'):
            assert len(y) == 1 and len(n) <= 14
        elif kind == 'T44':
            assert len(y) == 2 and len(n) == 0
        elif kind == 'T15':
            assert len(y) == 2 and len(n) == 1
        else:
            assert kind == 'T63_new' and len(y) == 3 and len(n) == 0
            data = row['interface']
            shift = data['local_to_rank_xor']
            perm = data['local_to_rank_permutation']
            assert shift in range(32) and sorted(perm) == list(range(5))
            assert tuple({permute(v ^ shift, perm) for v in g} for g in (m,y)) == registry_t63[data['rank']]
            stats['T63 ranks'][data['rank']] += 1
        stats['receiver local interfaces'][kind] += 1


def check_receiver(outer, bmin, bmaj, marks, spec, t63, stats, k4):
    if not k4 or spec['mode'] == 'positive_split':
        verify_split(outer, bmin, bmaj, marks, spec, t63, stats, k4)
        stats['receivers']['positive_split' if k4 else 'positive_split_Q5'] += 1
        return
    kind = spec['kind']
    stats['receivers'][kind] += 1
    if spec['mode'] == 'whole_face':
        counts = whole_face_test(bmin, bmaj, marks, spec, outer, 'mark_side', 'hole_counts')
        if kind == 'majority_root':
            majority_test(counts)
        else:
            f,g,h,k = counts
            assert kind == 'two_minority_roots' and (f,g) == (2,5) and 0 <= h <= 15 and k == h+1
        return
    assert spec['mode'] == 'controlled_single_root'
    i, z = spec['inner'], spec['Z_side']
    assert i in AXES and i != outer and z in BITS and spec['T_side'] == 1-z
    n,m = in_face(bmin,i,z), in_face(bmaj,i,z)
    p,q = len(n),len(bmin-n)
    counts = [[p,len(m)],[q,len(bmaj-m)]]
    marked = [len(m & marks), len(marks-m)]
    assert counts == spec['hole_counts'] and marked == spec['mark_counts']
    assert (p,q) == (spec['p'],spec['q'])
    assert spec['a'] in n and spec['w'] == (spec['a'] ^ UNITS[i]) and spec['w'] not in marks
    if kind == 'same_side':
        assert p in (1,2) and counts == [[p,p+3],[q,q+1]] and marked == [2,0]
    else:
        assert kind == 'separated' and p >= 1 and q in (0,1)
        assert counts == [[p,p+1],[q,q+3]] and marked == [1,1]


def all_edge_free(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if 'edge' in key:
                assert key == 'required_forced_edge' and value is None
            all_edge_free(value)
    elif isinstance(obj, list):
        for value in obj:
            all_edge_free(value)


def verify_plan(entry, colors, registry, t63, stats):
    plan = entry['plan']
    all_edge_free(plan)
    gate = entry['gate']
    assert gate == plan['gate'] and gate in ('k4_two_return', 'registry_two_return')
    stats['outer gates'][gate] += 1
    k4 = gate == 'k4_two_return'
    j = plan['outer']
    A_bit = plan['A_side'] if k4 else plan['donor_side']
    assert j in AXES and A_bit in BITS
    alpha,(amin,amaj),(bmaj,bmin) = directed(colors,j,1-A_bit)
    r,s,k = len(amin),len(bmin),len(bmaj)-len(bmin)
    assert k in (4,5,6) and len(amaj) == r+k and r+s+k == 8
    if k4:
        assert k == 4 and (plan['alpha_parity'], plan['beta_parity']) == (alpha,1-alpha)
        assert plan['B_side'] == 1-A_bit
    else:
        assert plan['donor_majority_parity'] == 1-alpha and plan['k'] == k
    X,U = set(plan['X']),set(plan['U'])
    assert len(X) == len(plan['X']) == k-2 and len(U) == len(plan['U']) == 2
    assert X <= amaj and U <= bmaj
    Y,V = ({v ^ UNITS[j] for v in g} for g in (X,U))
    assert not (Y | V) & set.union(*colors)
    retained_A,retained_B = amaj-X,bmaj-U
    aM,bM = retained_A|V,retained_B|Y
    assert len(aM) == r+4 and len(bM) == s+2*k-4
    if k4:
        assert plan['Y'] == sorted(Y) and plan['V'] == sorted(V)
        assert plan['H_prime_A'] == sorted(amin|aM) and plan['H_prime_B'] == sorted(bmin|bM)
        assert plan['H_prime_A_by_alpha_beta'] == list(map(sorted,(amin,aM)))
        assert plan['H_prime_B_by_alpha_beta'] == list(map(sorted,(bM,bmin)))
        donor = plan['supplier']
    else:
        for label, group in zip(('donor_minority','donor_retained','donor_marks',
                                 'receiver_minority','receiver_retained','receiver_marks'),
                                (amin,retained_A,V,bmin,retained_B,Y)):
            assert plan[label] == sorted(group)
        donor = plan['donor']
    kind = donor['kind']
    stats['donors'][kind] += 1
    if kind in ('core117','T15_exact_core'):
        index = 117 if kind == 'core117' else donor['index']
        exact_test(amin,retained_A,V,j,donor,registry,index)
        stats['cores'][index] += 1
    elif kind == 'majority_root':
        assert k4
        majority_test(whole_face_test(amin,aM,V,donor,j,'mark_side','hole_counts'))
    elif kind == 'Q6_same_side_majority_root':
        majority_test(whole_face_test(amin,aM,V,donor,j,'side','face_counts'))
    elif kind == 'Q6_T15_D4':
        assert whole_face_test(amin,aM,V,donor,j,'side','face_counts') == (0,4,1,1)
    else:
        assert kind == 'T15_isolated_mark'
        i,t = donor['inner'],donor['inner_side']
        assert i in AXES and i != j and t in BITS
        assert r == 1 and in_face(amin|aM,i,t) == {donor['isolated_mark']} <= V
    check_receiver(j,bmin,bM,Y,plan['receiver'],t63,stats,k4)


def main():
    started = process_time()
    pre = HERE / 'ODD_D24_PREFLIGHT.json'
    fixed = HERE / 'ODD_D24_FIXED_PLANS.json'
    source = read(pre)
    plans = read(fixed)
    assert plans['input_sha256'] == digest(pre)
    legacy = ROOT / 'global_bridge_2026_11_15' / 'exception_legacy_menu.py'
    assert plans['legacy_menu_sha256'] == digest(legacy)
    for name, bound in plans['dependency_sha256'].items():
        assert digest(ROOT / name) == bound
    expected, counts = regenerate(source)
    registry, t63 = approved_targets()
    stats = {name: Counter() for name in ('outer gates','donors','receivers','receiver local interfaces','cores','T63 ranks')}
    visited = set()
    for entry in plans['positives']:
        key = (entry['family'],entry['row'])
        try:
            assert key not in visited and expected[key] == entry['input']
            visited.add(key)
            colors = tuple(set(expected[key][name]) for name in ('even_holes','odd_holes'))
            assert all(len(g) == 8 and all(color(v) == c for v in g) for c,g in enumerate(colors))
            assert entry['delta'] == [8-x for x in expected[key]['lambda_by_axis']]
            verify_plan(entry,colors,registry,t63,stats)
        except (AssertionError, ValueError, KeyError) as error:
            raise AssertionError((key,entry['gate'],entry['plan'])) from error
    assert visited == set(expected) and len(visited) == 1534
    assert plans['complete'] and plans['failure'] is None
    assert plans['gate_counts'] == stats['outer gates']
    assert plans['positive_count'] == plans['visits_completed'] == len(visited)
    files = [pre, fixed, Path(__file__), legacy] + [
        ROOT / name for name in plans['dependency_sha256']
    ] + [ROOT / name for name in (
        'Q6_T15_ACTUAL_PROFILE.json', 'Q6_T15_S2_COMBINED_EXTENSION_REVIEW.json',
        'Q6_T15_CORE1054_MARKED_REVIEW.json', 'Q6_T15_D45_D3_REVIEW.json',
        'Q6_TWO_AVOIDED_EASY_REVIEW.md', 'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT_REVIEW.md',
        'R7_MU3_CONTROLLED_AND_T63_REVIEW.json', 'R7_MU3_T63_NEW_RANK_INPUTS.json',
        'R7_MU3_T63_NEW_RANK_REVIEW_CHECK.json', 'Q5_T15_FULL_REVIEW.json',
    )]
    result = dict(verdict='PASS', counts=counts, plan_stats=stats,
                  hashes={str(p.relative_to(ROOT)): digest(p) for p in files},
                  cpu_seconds=process_time()-started)
    (HERE / 'ODD_D24_CLOSURE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k != 'hashes'},indent=2))


if __name__ == '__main__':
    main()
