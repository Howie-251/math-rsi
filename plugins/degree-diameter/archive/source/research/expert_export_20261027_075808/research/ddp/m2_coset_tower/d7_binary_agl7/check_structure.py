"""Finite field/module/group arithmetic only; no graph or generator-set search."""
import json
import time
from collections import Counter
from itertools import combinations
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent


def fm(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return result


def fp(a, n):
    result = 1
    for _ in range(n):
        result = fm(result, a)
    return result


Z = [fp(2, j) for j in range(7)]
assert len(set(Z)) == 7 and fp(2, 7) == 1
K = [(a, b, e) for e in range(2) for b in range(3) for a in range(7)]
KI = {k: i for i, k in enumerate(K)}


def kmul(k, l):
    a, b, e = k
    c, d, f = l
    return ((a + (-1 if e else 1) * 2**b * c) % 7, (b + d) % 3, e ^ f)


def kinv(k):
    a, b, e = k
    inverse_multiplier = ((-1 if e else 1) * 2**(-b % 3)) % 7
    return (-inverse_multiplier * a % 7, -b % 3, e)


def action(k, x):
    a, b, e = k
    u, v = x % 8, x // 8
    if e:
        u, v = v, u
    return fm(Z[a], fp(u, 2**b)) + 8 * fm(Z[-a % 7], fp(v, 2**b))


M = [[KI[kmul(k, l)] for l in K] for k in K]
INV = [KI[kinv(k)] for k in K]
ACTION = [[action(k, x) for x in range(64)] for k in K]
assert len({tuple(row) for row in ACTION}) == 42
assert all(M[i][INV[i]] == M[INV[i]][i] == 0 for i in range(42))
for i in range(42):
    for j in range(42):
        assert all(ACTION[M[i][j]][x] == ACTION[i][ACTION[j][x]] for x in range(64))


def fourier(mask):
    u = v = 0
    for j in range(7):
        if mask & (1 << j):
            u ^= Z[j]
            v ^= Z[-j % 7]
    return u + 8 * v


def permute_bits(mask, k):
    a, b, e = k
    result = 0
    multiplier = (-1 if e else 1) * 2**b
    for j in range(7):
        if mask & (1 << j):
            result |= 1 << ((a + multiplier * j) % 7)
    return result


even_masks = [m for m in range(128) if m.bit_count() % 2 == 0]
assert len({fourier(m) for m in even_masks}) == 64
for mask in even_masks:
    for kid, k in enumerate(K):
        assert fourier(permute_bits(mask, k)) == ACTION[kid][fourier(mask)]
assert all(fourier(x ^ y) == fourier(x) ^ fourier(y) for x in even_masks for y in even_masks)


def gm(g, h):
    x, kid = g % 64, g // 64
    y, lid = h % 64, h // 64
    return (x ^ ACTION[kid][y]) + 64 * M[kid][lid]


def gi(g):
    x, kid = g % 64, g // 64
    return ACTION[INV[kid]][x] + 64 * INV[kid]


def decode(g):
    x, kid = g % 64, g // 64
    return [x % 8, x // 8, *K[kid]]


def orbit_name(x):
    u, v = x % 8, x // 8
    if not u and not v:
        return 'zero'
    if not u or not v:
        return 'axes14'
    product = fm(u, v)
    if product == 1:
        return 'product1_7'
    if product in [Z[j] for j in [1, 2, 4]]:
        return 'product124_21'
    assert product in [Z[j] for j in [3, 5, 6]]
    return 'product356_21'


names = ['product1_7', 'axes14', 'product124_21', 'product356_21', 'zero']
orbits = {name: {x for x in range(64) if orbit_name(x) == name} for name in names}
for orbit in orbits.values():
    representative = min(orbit)
    assert {ACTION[k][representative] for k in range(42)} == orbit

involutions = {name: [] for name in names}
pairs = {name: [] for name in names}
for g in range(2688):
    inverse = gi(g)
    assert gm(g, inverse) == gm(inverse, g) == 0
    name = orbit_name(g % 64)
    assert orbit_name(inverse % 64) == name
    if g and inverse == g:
        involutions[name].append(g)
    elif g < inverse:
        pairs[name].append([g, inverse])
assert [len(involutions[name]) for name in names] == [14, 14, 42, 42, 7]
assert [len(pairs[name]) for name in names] == [140, 287, 420, 420, 17]

embedded_K = {64 * k for k in range(42)}
embedded_H = {64 * k for k, (a, _, _) in enumerate(K) if a == 0}
normalizer_H = [g for g in range(2688) if all(gm(gm(g, h), gi(g)) in embedded_H for h in embedded_H)]
normalizer_K = [g for g in range(2688) if all(gm(gm(g, k), gi(g)) in embedded_K for k in embedded_K)]
assert len(normalizer_H) == 12 and len(normalizer_K) == 42
assert set(normalizer_H) & set(normalizer_K) == embedded_H
fixed_H = [x for x in range(64) if all(ACTION[h // 64][x] == x for h in embedded_H)]
fixed_K = [x for x in range(64) if all(ACTION[k][x] == x for k in range(42))]
assert fixed_H == [0, 9] and fixed_K == [0]


def parent_block(g):
    x, kid = g % 64, g // 64
    return x + 64 * K[kid][0]


for g in range(2688):
    assert len({gm(g, h) for h in embedded_H}) == 6
    assert {parent_block(gm(g, h)) for h in embedded_H} == {parent_block(g)}
assert Counter(parent_block(g) for g in range(2688)) == Counter({b: 6 for b in range(448)})
translate = 64 * KI[(1, 0, 0)]
reflection = 64 * KI[(0, 0, 1)]
conjugate = gm(gm(translate, reflection), gi(translate))
assert decode(conjugate) == [0, 0, 2, 0, 1] and conjugate not in embedded_H


def component_h_orbits(components):
    unseen = set(components)
    answer = []
    while unseen:
        representative = min(unseen)
        orbit = {tuple(sorted(gm(gm(h, g), gi(h)) for g in representative)) for h in embedded_H}
        assert orbit <= unseen
        stabilizer = [decode(h) for h in sorted(embedded_H)
                      if tuple(sorted(gm(gm(h, g), gi(h)) for g in representative)) == representative]
        assert len(orbit) * len(stabilizer) == 6
        answer.append({'representative_G_codes': list(representative),
                       'representative_coordinates': list(map(decode, representative)),
                       'orbit_size': len(orbit), 'orbit_members_G_codes': sorted(map(list, orbit)),
                       'stabilizer_H_coordinates': stabilizer})
        unseen -= orbit
    return answer


O7_invol_orbits = component_h_orbits([(g,) for g in involutions['product1_7']])
O7_pair_orbits = component_h_orbits([tuple(pair) for pair in pairs['product1_7']])
assert len(O7_invol_orbits) == 4
assert sorted(o['orbit_size'] for o in O7_invol_orbits) == [1, 1, 6, 6]
branches = []
for invol_colors in combinations(range(4), 2):
    raw = anchored = 1
    for color in range(4):
        if color in invol_colors:
            count = len(involutions[names[color]])
            anchor_count = len(O7_invol_orbits) if color == 0 else count
        else:
            count = len(pairs[names[color]])
            anchor_count = len(O7_pair_orbits) if color == 0 else count
        raw *= count
        anchored *= anchor_count
    branches.append({'involution_colors': [names[i] for i in invol_colors],
                     'raw_component_choices': raw,
                     'choices_after_only_O7_H_orbit_anchor': anchored})
assert sum(b['raw_component_choices'] for b in branches) == 316355760

result = {
    'status': 'COMPLETE_FINITE_MODULE_AND_GROUP_CHECK_NO_GRAPH',
    'field': 'F8=F2[t]/(t^3+t+1), zeta=t encoded2',
    'field_zeta_powers': Z,
    'A_encoding': 'x=u+8v, u,v in0..7',
    'K_encoding': 'kid=a+7b+21e, a mod7,b mod3,e mod2',
    'G_encoding': 'gid=x+64kid',
    'K_order': 42, 'G_order': 2688, 'H_order': 6,
    'faithful_action_maps': 42,
    'representation_comparisons': 64 * 42,
    'action_multiplication_comparisons': 42 * 42 * 64,
    'fourier_even_mask_to_A': [[m, fourier(m)] for m in even_masks],
    'horizontal_orbits': [{
        'name': name, 'size': len(orbits[name]), 'A_members_encoded': sorted(orbits[name]),
        'nonidentity_involution_count': len(involutions[name]),
        'nonidentity_involutions_G_encoded': involutions[name],
        'inverse_pair_count': len(pairs[name]),
    } for name in names],
    'total_nonidentity_involutions': sum(map(len, involutions.values())),
    'total_nonselfinverse_pairs': sum(map(len, pairs.values())),
    'inverse_preserves_horizontal_orbit_all_2688': True,
    'right_H_parent_a_checked_all_2688_times_6': True,
    'block_parent_fibers': {'count': 448, 'each_size': 6},
    'fixed_vectors_H': fixed_H, 'fixed_vectors_K': fixed_K,
    'normalizer_H_in_G': list(map(decode, normalizer_H)),
    'normalizer_K_in_G': list(map(decode, normalizer_K)),
    'normalizer_H_and_K_intersection': list(map(decode, sorted(embedded_H))),
    'H_non_normal_witness': {'conjugator': decode(translate), 'element_H': decode(reflection),
                              'conjugate_not_H': decode(conjugate)},
    'O7_anchor_H_conjugation': {
        'involution_orbits': O7_invol_orbits,
        'inverse_pair_orbits': O7_pair_orbits,
        'involution_orbit_count': len(O7_invol_orbits),
        'inverse_pair_orbit_count': len(O7_pair_orbits),
        'involution_orbit_size_histogram': dict(sorted(Counter(o['orbit_size'] for o in O7_invol_orbits).items())),
        'inverse_pair_orbit_size_histogram': dict(sorted(Counter(o['orbit_size'] for o in O7_pair_orbits).items())),
        'two_pair_two_involution_branches': branches,
        'total_raw_choices': sum(b['raw_component_choices'] for b in branches),
        'total_choices_after_only_O7_anchor': sum(b['choices_after_only_O7_H_orbit_anchor'] for b in branches),
        'remaining_stabilizers_not_quotiented': True,
    },
    'cpu_seconds': time.process_time() - START,
    'scope': '64 vectors,42 K elements,2688 individual G elements; no S enumeration or graph expansion/BFS.',
}
(OUT / 'STRUCTURE_CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'K_order', 'G_order', 'H_order',
                                       'total_nonidentity_involutions', 'total_nonselfinverse_pairs',
                                       'cpu_seconds']}, indent=2))
print(json.dumps([{k: orbit[k] for k in ['name', 'size', 'nonidentity_involution_count', 'inverse_pair_count']}
                  for orbit in result['horizontal_orbits']], indent=2))
