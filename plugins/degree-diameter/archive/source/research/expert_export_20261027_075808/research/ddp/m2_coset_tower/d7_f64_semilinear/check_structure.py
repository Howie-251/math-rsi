"""Tiny finite-field/group audit only: no graph or generator-set search."""
import json
import time
from collections import Counter, defaultdict
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent

def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= 0x43
    return out

def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out

g = 2
assert len({power(g, j) for j in range(63)}) == 63
r = power(g, 3)
rp = [power(r, i) for i in range(21)]
assert r == 8 and len(set(rp)) == 21
frobenius = [power(x, 8) for x in range(64)]
assert all(frobenius[frobenius[x]] == x for x in range(64))

def action(k, x):
    i, e = k
    return mul(rp[i], frobenius[x] if e else x)

def kmul(k, ell):
    i, e = k
    j, f = ell
    return (i + (8 if e else 1) * j) % 21, e ^ f

def kinv(k):
    i, e = k
    return (-(8 if e else 1) * i) % 21, e

K = [(i, e) for i in range(21) for e in range(2)]
maps = {tuple(action(k, x) for x in range(64)) for k in K}
assert len(maps) == 42
assert all(frobenius[mul(r, frobenius[x])] == mul(rp[8], x) for x in range(64))
assert all(kmul(k, kinv(k)) == (0, 0) for k in K)
H = {(i, e) for i in (0, 7, 14) for e in range(2)}
assert len(H) == 6 and all(kmul(a, b) in H for a in H for b in H)
assert all(kmul(kmul(k, h), kinv(k)) in H for k in K for h in H)
ZK = [k for k in K if all(kmul(k, ell) == kmul(ell, k) for ell in K)]
assert set(ZK) == {(i, 0) for i in range(0, 21, 3)}
assert H & set(ZK) == {(0, 0)}
assert {kmul(z, h) for z in ZK for h in H} == set(K)

orbits = []
unseen = set(range(64))
while unseen:
    seed = min(unseen)
    orbit = {action(k, seed) for k in K}
    orbits.append(sorted(orbit))
    unseen -= orbit
assert sorted(map(len, orbits)) == [1, 21, 42]
A21 = set(rp)
BC42 = set(range(1, 64)) - A21
assert A21 in list(map(set, orbits)) and BC42 in list(map(set, orbits))

def orbit_name(x): return 'zero' if x == 0 else 'A21' if x in A21 else 'BC42'

def gmul(a, b):
    x, i, e = a
    y, j, f = b
    ki, ke = kmul((i, e), (j, f))
    return x ^ action((i, e), y), ki, ke

def ginv(a):
    x, i, e = a
    ki, ke = kinv((i, e))
    return action((ki, ke), x), ki, ke

G = [(x, i, e) for x in range(64) for i in range(21) for e in range(2)]
identity = (0, 0, 0)
counts = defaultdict(Counter)
involutions = []
for a in G:
    inv = ginv(a)
    assert gmul(a, inv) == identity
    assert orbit_name(a[0]) == orbit_name(inv[0])
    label = orbit_name(a[0])
    counts[label]['elements'] += 1
    if a == identity:
        counts[label]['identity'] += 1
    elif a == inv:
        counts[label]['nonidentity_involutions'] += 1
        counts[label]['translation_involutions' if a[1:] == (0, 0) else 'semilinear_involutions'] += 1
        involutions.append(a)
    elif a < inv:
        counts[label]['inverse_pairs'] += 1
assert len(involutions) == 87
assert counts['A21']['nonidentity_involutions'] == 42 and counts['A21']['inverse_pairs'] == 420
assert counts['BC42']['nonidentity_involutions'] == 42 and counts['BC42']['inverse_pairs'] == 861
assert counts['zero']['nonidentity_involutions'] == 3 and counts['zero']['inverse_pairs'] == 19
reflection_fixed = []
for i in (0, 7, 14):
    fixed = [x for x in range(64) if action((i, 1), x) == x]
    assert len(fixed) == 8 and set(fixed) - {0} <= A21
    reflection_fixed.append({'K_element': [i, 1], 'fixed_field_elements': fixed})
assert set().union(*(set(row['fixed_field_elements']) - {0} for row in reflection_fixed)) == A21

def conjugacy_class(a):
    return {gmul(gmul(b, a), ginv(b)) for b in G}

class_records = []
for representative in ((1, 0, 0), (2, 0, 0), (0, 0, 1)):
    conjugates = conjugacy_class(representative)
    assert all(a in involutions for a in conjugates)
    class_records.append({'representative': representative, 'class_size': len(conjugates),
                          'horizontal_orbit_counts': dict(Counter(orbit_name(a[0]) for a in conjugates))})
assert [row['class_size'] for row in class_records] == [21, 42, 24]

result = {
    'status': 'COMPLETE_SMALL_GROUP_STRUCTURE_CHECK',
    'field': 'GF64 = F2[t]/(t^6+t+1), binary polynomial encoding',
    'primitive_g': g, 'r': r, 'r_order': 21, 'f_action': 'x -> x^8',
    'K_coordinate': '(i,e)=r^i f^e, i mod21,e mod2',
    'K_multiplication': '(i,e)(j,f)=(i+8^e*j mod21,e+f mod2)',
    'K_inverse': '(i,e)^-1=(-8^e*i mod21,e)',
    'K_order': 42, 'distinct_action_maps': len(maps), 'faithful': True,
    'H_elements': sorted(H), 'H_order': 6, 'H_normal_in_K': True, 'K_H_index': 7,
    'K_center_elements': sorted(ZK), 'K_is_direct_product_C7_and_H': True,
    'additive_K_orbits': orbits,
    'G_order': len(G),
    'G_multiplication': '(x,i,e)(y,j,f)=(x+r^i*y^(8^e),i+8^e*j,e+f)',
    'G_inverse': '(x,i,e)^-1=(r^(-8^e*i)*x^(8^e),-8^e*i,e)',
    'counts_by_horizontal_K_orbit': {label: dict(value) for label, value in counts.items()},
    'total_nonidentity_involutions': len(involutions),
    'total_nonselfinverse_inverse_pairs': sum(c['inverse_pairs'] for c in counts.values()),
    'semilinear_reflection_fixed_spaces': reflection_fixed,
    'nonidentity_involution_G_conjugacy_classes': class_records,
    'cpu_seconds': time.process_time() - START,
    'scope': 'Field and individual group elements only. No generator-set enumeration, graph construction, graph BFS, or search normalization proof.',
}
(OUT / 'STRUCTURE_CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({key: value for key, value in result.items() if key not in ('additive_K_orbits',)}, indent=2))
