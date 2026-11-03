"""HH-compatible 0/1-pair scope counts and O7 subset anchors; no S search."""
import json
import time
from collections import Counter
from itertools import combinations
from math import comb, prod
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
source = json.loads((OUT / 'STRUCTURE_CHECK.json').read_text())
NAMES = ['product1_7', 'axes14', 'product124_21', 'product356_21', 'zero']
INV_COUNTS = [14, 14, 42, 42, 7]
PAIR_COUNTS = [140, 287, 420, 420, 17]
assert [o['name'] for o in source['horizontal_orbits']] == NAMES
assert [o['nonidentity_involution_count'] for o in source['horizontal_orbits']] == INV_COUNTS
assert [o['inverse_pair_count'] for o in source['horizontal_orbits']] == PAIR_COUNTS
O7 = source['horizontal_orbits'][0]['nonidentity_involutions_G_encoded']
assert len(set(O7)) == 14


def fm(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return value


def fp(a, n):
    value = 1
    for _ in range(n):
        value = fm(value, a)
    return value


H = [(d, f) for f in range(2) for d in range(3)]


def conjugate_by_H(g, h):
    d, f = h
    x, k = g % 64, g // 64
    a, b, e = k % 7, (k // 7) % 3, k // 21
    u, v = x % 8, x // 8
    if f:
        u, v = v, u
    new_x = fp(u, 2**d) + 8 * fp(v, 2**d)
    new_a = ((-1 if f else 1) * 2**d * a) % 7
    return new_x + 64 * (new_a + 7*b + 21*e)


def decode(g):
    x, k = g % 64, g // 64
    return [x % 8, x // 8, k % 7, (k // 7) % 3, k // 21]


assert all({conjugate_by_H(g, h) for g in O7} == set(O7) for h in H)
subset_orbits = {}
for size in [1, 2, 3]:
    unseen = set(combinations(sorted(O7), size))
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {tuple(sorted(conjugate_by_H(g, h) for g in representative)) for h in H}
        assert orbit <= unseen
        stabilizer = [h for h in H if tuple(sorted(conjugate_by_H(g, h) for g in representative)) == representative]
        assert len(stabilizer) * len(orbit) == 6
        orbits.append({
            'representative_G_codes': list(representative),
            'representative_coordinates_u_v_a_b_e': list(map(decode, representative)),
            'orbit_size': len(orbit), 'orbit_members_G_codes': sorted(map(list, orbit)),
            'stabilizer_H_d_f': stabilizer,
        })
        unseen -= orbit
    assert sum(o['orbit_size'] for o in orbits) == comb(14, size)
    fixed_subsets = [sum(tuple(sorted(conjugate_by_H(g, h) for g in subset)) == subset
                         for subset in combinations(sorted(O7), size)) for h in H]
    assert sum(fixed_subsets) == 6 * len(orbits)
    subset_orbits[size] = {
        'subset_size': size, 'total_subsets': comb(14, size), 'orbit_count': len(orbits),
        'orbit_size_histogram': dict(sorted(Counter(o['orbit_size'] for o in orbits).items())),
        'fixed_subset_counts_in_H_order': fixed_subsets, 'orbits': orbits,
    }
assert [subset_orbits[k]['orbit_count'] for k in [1,2,3]] == [4,17,64]


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total+1):
        for rest in compositions(total-first, parts-1):
            yield (first,) + rest


def invol_choices(counts):
    return prod(comb(population, count) for population, count in zip(INV_COUNTS, counts))


zero_rows = []
for counts in compositions(6, 5):
    if not all(counts[color] >= 1 for color in range(4)):
        continue
    anchor_count = subset_orbits[counts[0]]['orbit_count']
    raw = invol_choices(counts)
    anchored = anchor_count * prod(comb(INV_COUNTS[i], counts[i]) for i in range(1, 5))
    zero_rows.append({'involution_counts_by_colour': counts, 'O7_subset_size': counts[0],
                      'O7_anchor_orbit_count': anchor_count, 'raw_choices': raw, 'anchored_choices': anchored})
zero_summary = [{
    'O7_subset_size': size, 'O7_subsets': comb(14,size),
    'O7_anchor_orbits': subset_orbits[size]['orbit_count'],
    'other_colour_choices': sum(prod(comb(INV_COUNTS[i], r['involution_counts_by_colour'][i]) for i in range(1,5))
                               for r in zero_rows if r['O7_subset_size'] == size),
    'raw_choices': sum(r['raw_choices'] for r in zero_rows if r['O7_subset_size'] == size),
    'anchored_choices': sum(r['anchored_choices'] for r in zero_rows if r['O7_subset_size'] == size),
} for size in [1,2,3]]

pair_anchor_count = source['O7_anchor_H_conjugation']['inverse_pair_orbit_count']
assert pair_anchor_count == 26
one_rows = []
for pair_colour in range(5):
    for counts in compositions(4, 5):
        if not all(counts[colour] >= 1 or pair_colour == colour for colour in range(4)):
            continue
        raw = PAIR_COUNTS[pair_colour] * invol_choices(counts)
        if pair_colour == 0:
            anchored = pair_anchor_count * invol_choices(counts)
            method = 'existing_26_O7_inverse_pair_representatives'
        else:
            anchored = PAIR_COUNTS[pair_colour] * subset_orbits[counts[0]]['orbit_count'] * prod(
                comb(INV_COUNTS[i], counts[i]) for i in range(1, 5))
            method = f'O7_involution_subset_size_{counts[0]}'
        one_rows.append({'pair_colour': NAMES[pair_colour], 'involution_counts_by_colour': counts,
                        'anchor_method': method, 'raw_choices': raw, 'anchored_choices': anchored})
one_summary = [{
    'pair_colour': name, 'available_inverse_pairs': PAIR_COUNTS[i],
    'raw_choices': sum(r['raw_choices'] for r in one_rows if r['pair_colour'] == name),
    'anchored_choices': sum(r['anchored_choices'] for r in one_rows if r['pair_colour'] == name),
    'row_count': sum(r['pair_colour'] == name for r in one_rows),
} for i, name in enumerate(NAMES)]

# Independent coefficient counts: one-dimensional generating-polynomial convolution.
def coefficient_count(total, covered_colour=None):
    polynomial = [1] + [0]*total
    for colour, population in enumerate(INV_COUNTS):
        minimum = 0 if colour == 4 or colour == covered_colour else 1
        factor = [comb(population, k) if k >= minimum else 0 for k in range(total+1)]
        polynomial = [sum(polynomial[j]*factor[k-j] for j in range(k+1)) for k in range(total+1)]
    return polynomial[total]


raw_zero = sum(r['raw_choices'] for r in zero_rows)
raw_one = sum(r['raw_choices'] for r in one_rows)
assert raw_zero == coefficient_count(6) == 689125416
assert raw_one == sum(PAIR_COUNTS[c] * coefficient_count(4,c) for c in range(5)) == 1298700900
result = {
    'status': 'COMPLETE_PURE_COMBINATORIAL_SCOPE_NO_CANDIDATE_SEARCH',
    'colour_order': NAMES, 'involution_counts': INV_COUNTS, 'inverse_pair_counts': PAIR_COUNTS,
    'H_order_d_f': H,
    'H_conjugation': '(u,v,a,b,e) -> (Frob2^d(swap^f(u,v)), (-1)^f 2^d a mod7,b,e)',
    'O7_subset_orbits': subset_orbits,
    'existing_O7_inverse_pair_anchor_source': 'STRUCTURE_CHECK.json:O7_anchor_H_conjugation.inverse_pair_orbits',
    'zero_pair_six_involution': {'raw_HH_choices': raw_zero,
                               'anchored_choices': sum(r['anchored_choices'] for r in zero_rows),
                               'summary_by_O7_size': zero_summary, 'all_colour_count_rows': zero_rows},
    'one_pair_four_involution': {'raw_HH_choices': raw_one,
                                'anchored_choices': sum(r['anchored_choices'] for r in one_rows),
                                'summary_by_pair_colour': one_summary, 'all_colour_count_rows': one_rows},
    'residual_stabilizers_quotiented': False,
    'all_a_s_zero_exclusion_applied': False,
    'computation_scope': 'Subsets of 14 O7 involutions of sizes1..3, six H actions, colour-count compositions and polynomial coefficients only; no six-element S or graph expanded.',
    'cpu_seconds': time.process_time()-START,
}
(OUT / 'REMAINING_SCOPE.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({
    'subset_orbit_counts': {k:v['orbit_count'] for k,v in subset_orbits.items()},
    'zero_pair': {k:v for k,v in result['zero_pair_six_involution'].items() if k!='all_colour_count_rows'},
    'one_pair': {k:v for k,v in result['one_pair_four_involution'].items() if k!='all_colour_count_rows'},
    'cpu_seconds': result['cpu_seconds'],
}, indent=2))
