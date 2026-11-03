"""Finite element arithmetic and 25 formal-word patterns only; no graph or S search."""
import json
import time
from collections import Counter
from itertools import product
from pathlib import Path

start = time.process_time()
out = Path(__file__).resolve().parent
p, r, k, index, h = 61, 4, 30, 5, 6

def order(a):
    x = 1
    for n in range(1, p):
        x = x*a % p
        if x == 1:
            return n
    raise AssertionError(a)

assert order(2) == 60 and order(r) == k
Q = {pow(r, i, p) for i in range(k)}
N = set(range(1, p))-Q
U = {pow(r, index*i, p) for i in range(h)}
assert len(Q) == len(N) == 30 and len(U) == 6
assert pow(r, 15, p) == p-1 and p-1 in U
assert Q == {x*x % p for x in range(1, p)}

def color(x):
    return 'zero' if x == 0 else ('Q' if x in Q else 'N')

def inverse(x, w, i):
    return -pow(r, -i % k, p)*x % p, -w % 3, -i % k

inventory = {c: {'internal_involutions': 0, 'internal_inverse_pairs': 0,
                 'cross_inverse_pairs': 0} for c in ['zero', 'Q', 'N']}
for x, i in product(range(p), range(k)):
    c = color(x)
    xi, wi, ii = inverse(x, 0, i)
    assert color(xi) == c
    assert inverse(xi, wi, ii) == (x, 0, i)
    assert (x+pow(r, i, p)*xi) % p == 0
    if (x, i) != (0, 0):
        if (x, i) == (xi, ii):
            assert i == 15
            inventory[c]['internal_involutions'] += 1
        elif (x, i) < (xi, ii):
            inventory[c]['internal_inverse_pairs'] += 1
    cross_inv = inverse(x, 1, i)
    assert cross_inv[1] == 2 and color(cross_inv[0]) == c
    inventory[c]['cross_inverse_pairs'] += 1
assert inventory == {
    'zero': {'internal_involutions': 1, 'internal_inverse_pairs': 14, 'cross_inverse_pairs': 30},
    'Q': {'internal_involutions': 30, 'internal_inverse_pairs': 435, 'cross_inverse_pairs': 900},
    'N': {'internal_involutions': 30, 'internal_inverse_pairs': 435, 'cross_inverse_pairs': 900}}

remaining, H_orbits = set(range(1, p)), []
while remaining:
    o = sorted({u*min(remaining) % p for u in U})
    assert len(o) == h
    H_orbits.append({'representative': min(o), 'color': color(o[0]), 'members': o})
    remaining -= set(o)
assert Counter(o['color'] for o in H_orbits) == {'Q': 5, 'N': 5}

# Free reduction is valid before evaluating words in any actual S.
names = ['A', 'a', 'B', 'b', 'I', 'J']
inv = [1, 0, 3, 2, 4, 5]
words = [()]
for length in range(1, 4):
    words += [w for w in product(range(6), repeat=length)
              if all(w[i+1] != inv[w[i]] for i in range(length-1))]
assert Counter(map(len, words)) == {0: 1, 1: 6, 2: 30, 3: 150}
patterns = []
for a, b in product(range(index), repeat=2):
    phase = [(a,1),(-a % index,2),(b,1),(-b % index,2),(0,0),(0,0)]
    counts = [0]*index
    by_length = [[0]*index for _ in range(4)]
    word_lists = [[] for _ in range(index)]
    for word in words:
        j = sum(phase[c][0] for c in word) % index
        w = sum(phase[c][1] for c in word) % 3
        if w == 0:
            counts[j] += 1
            by_length[len(word)][j] += 1
            word_lists[j].append(''.join(names[c] for c in word) or 'identity')
    assert sum(counts) == 59
    extra = [2,4,4,4,4]
    upper = [counts[j]+extra[j] for j in range(index)]
    passed = all(x >= 10 for x in upper)
    patterns.append({'a': a, 'b': b, 'C_j': counts, 'counts_by_length': by_length,
                     'head_route_upper': extra, 'nonzero_orbit_upper': upper,
                     'passes_necessary_bound': passed,
                     'failing_layers': [j for j in range(index) if upper[j] < 10],
                     'tight_layers': [j for j in range(index) if upper[j] == 10],
                     'tight_layer_words': {str(j): word_lists[j] for j in range(index)
                                           if passed and upper[j] == 10}})
survivors = [(row['a'],row['b']) for row in patterns if row['passes_necessary_bound']]
assert survivors == [(1,4),(2,3),(3,2),(4,1)]
anchor_indices = list(range(16))
filtered_anchors = [i for i in anchor_indices if i % index]
index_pairs = [(i,j) for i in filtered_anchors for j in range(k) if (i+j) % index == 0]
assert len(filtered_anchors) == 12 and len(index_pairs) == 72
assert k*k*30**3 == 24300000
assert len(anchor_indices)*k*30**3 == 12960000
assert len(index_pairs)*30**3 == 1944000

result = {
    'status': 'COMPLETE_ARITHMETIC_AND_FORMAL_WORD_FILTER_ONLY',
    'parameters': {'degree': 7, 'p': p, 'r': r, 'order_2': order(2), 'K_order': k,
                   'H_order': h, 'K_over_H_order': index, 'A_order': 183,
                   'layers': [5490,915,183], 'n': 6588, 'edges_if_legal_S': 23058},
    'Q': sorted(Q), 'N': sorted(N), 'U': sorted(U), 'nonzero_H_orbits': H_orbits,
    'single_element_inventory': inventory,
    'normalized_parameters': {'cross_Q': ['1',1,'i'], 'cross_N': ['y in N',1,'j'],
                              'internal_Q': ['u in Q',0,15], 'internal_N': ['v in N',0,15]},
    'C3_inversion_after_renormalizing': {
        'i_prime': '-i mod30', 'j_prime': '-j mod30',
        'y_prime': 'r^(i-j)*y mod61', 'u_prime': '-r^i*u mod61',
        'v_prime': '-r^i*v mod61'},
    'counts': {'raw_HH_generating_sets': 729000000,
               'after_unique_Q_cross_scaling': 24300000,
               'after_safe_first_index_sign_restriction': 12960000,
               'after_formal_word_necessary_bound': 1944000},
    'safe_first_indices': anchor_indices, 'filtered_first_indices': filtered_anchors,
    'filtered_full_index_pairs': index_pairs,
    'word_scope': {'alphabet': names, 'inverse_letter_indices': inv,
                   'maximum_length': 3, 'empty_word_included': True,
                   'reduced_word_counts_by_length': [1,6,30,150],
                   'w0_word_counts_by_length': [1,2,6,50],
                   'actual_generator_sets_enumerated': 0, 'graphs_built': 0},
    'patterns': patterns, 'surviving_residue_pairs': survivors,
    'limitations': ['Necessary BB orbit upper bound only; no actual BB sets evaluated.',
                    'Sign restriction is candidate preserving, not a list of isomorphism classes.',
                    'No construction or D5 existence assertion.'],
    'cpu_seconds': time.process_time()-start}
(out/'STRUCTURE_SCOPE.json').write_text(json.dumps(result, indent=2)+'\n')
(out/'WORD_PATTERNS.tsv').write_text('a\tb\tC0\tC1\tC2\tC3\tC4\tupper0\tupper1\tupper2\tupper3\tupper4\tpasses\n'+
    ''.join('\t'.join(map(str,[q['a'],q['b'],*q['C_j'],*q['nonzero_orbit_upper'],
                              int(q['passes_necessary_bound'])]))+'\n' for q in patterns))
print(json.dumps({'status': result['status'], 'counts': result['counts'],
                  'surviving_residue_pairs': survivors, 'cpu_seconds': result['cpu_seconds']},indent=2))
