"""One symbolic route-capacity calculation; no graph or voltage sweep."""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import json
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
OUT = Path(__file__).resolve().parent
BASE = OUT.parent
assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_WORD_CAPACITY_ANALYSIS'
assert json.loads((OUT / 'CONTROLLED_PROFILE_PROTOCOL.json').read_text())['status'] == 'FROZEN_BEFORE_WORD_TABLE_COMPUTE'
construction = json.loads((BASE / 'construction.json').read_text())['construction']
charts = construction['charts']
perms = [construction['controller']['symbols'][0]['perm'], construction['controller']['symbols'][1]['perm']]
invperms = [[p.index(i) for i in range(4)] for p in perms]
INV = [1, 0, 3, 2]
SYMBOLS = 'aAbB'
reduced = [w for w in product(range(4), repeat=4) if all(w[i] != INV[w[i-1]] for i in range(1, 4))]
assert len(reduced) == 108
words = [()] + [w for length in range(1, 5) for w in product(range(4), repeat=length)]
digit = [tuple(x // 3**i % 3 for i in range(4)) for x in range(81)]
relation = []
for c in charts:
    M, d = c['M'], c['d']
    row = []
    for x in digit:
        center = [sum(M[i][j] * x[j] for j in range(4)) % 3 for i in range(4)]
        row.append(sum(1 << sum(((center[i] + lam*d[i]) % 3) * 3**i for i in range(4)) for lam in range(3)))
    relation.append(row)
images = {(): 1}
for word in words[1:]:
    previous, sym = images[word[:-1]], word[-1]
    bits = 0
    while previous:
        one = previous & -previous
        previous -= one
        bits |= relation[sym][one.bit_length()-1]
    assert bits.bit_count() in [1, 3, 9, 27, 81]
    images[word] = bits
bad = [i for i, w in enumerate(reduced) if images[w].bit_count() < 81]
badfile = list(map(int, (BASE / 'badwords_6156.txt').read_text().split()))
assert badfile[0] == len(badfile)-1 and bad == badfile[1:]
good = {w for w in reduced if images[w].bit_count() == 81}
all_reduced = set(reduced)


def endpoint(root, word):
    c, form = root, [0]*8
    for sym in word:
        kind = sym//2
        if sym % 2:
            before = invperms[kind][c]
            form[4*kind+before] -= 1
            c = before
        else:
            form[4*kind+c] += 1
            c = perms[kind][c]
    return c, tuple(form)


slots = [[{'forms': defaultdict(int), 'good': set(), 'even': set(), 'universal': set(), 'good_raw': 0} for j in range(4)] for i in range(4)]
ends = {}
for i in range(4):
    for word in words:
        j, form = endpoint(i, word)
        ends[i, word] = j, form
        s = slots[i][j]
        s['forms'][form] |= images[word]
        if word in good:
            s['good'].add(form)
            s['good_raw'] += 1
        if len(word) in [0, 2]:
            s['even'].add(form)
        if word in all_reduced:
            s['universal'].add(form)
symbolic = []
for i in range(4):
    for j in range(4):
        s = slots[i][j]
        symbolic.append({'root_base': i, 'target_base': j,
                         'good4_raw_words': s['good_raw'], 'good4_distinct_forms': len(s['good']),
                         'even0or2_distinct_forms': len(s['even']),
                         'good4_union_even_distinct_forms': len(s['good'] | s['even']),
                         'all108NB4_distinct_forms': len(s['universal']),
                         'all108NB4_union_even_distinct_forms': len(s['universal'] | s['even']),
                         'all_le4_distinct_forms': len(s['forms']),
                         'x0_form_fiber_incidence_capacity': sum(b.bit_count() for b in s['forms'].values()),
                         'good_forms': [list(x) for x in sorted(s['good'])],
                         'even_forms': [list(x) for x in sorted(s['even'])]})
numeric = []
volts = [0, 12, 4, 0, 17, 0, 0, 1]
for m in [19, 20]:
    roots = []
    for i in range(4):
        minimum = {}
        g4, even, u4 = set(), set(), set()
        reach0 = defaultdict(int)
        for word in words:
            j, form = ends[i, word]
            phase = sum(a*b for a, b in zip(form, volts)) % m
            key = (j, phase)
            minimum[key] = min(minimum.get(key, 5), len(word))
            reach0[key] |= images[word]
            if word in good:
                g4.add(key)
            if len(word) in [0, 2]:
                even.add(key)
            if word in all_reduced:
                u4.add(key)
        targets = {(j, phase) for j in range(4) for phase in range(m)}
        strict = sorted(key for key in targets if minimum.get(key, 5) > 4 or (minimum[key] in [1,3,4] and key not in g4))
        wide = sorted(targets - (g4 | even))
        universal_exact = sorted(targets - u4)
        universal_wide = sorted(targets - (u4 | even))
        roots.append({'root_base': i, 'controller_le4_missing': sorted(targets - set(minimum)),
                      'author_strict_filter_missing': strict,
                      'wide_I_R2_good4_missing': wide,
                      'universal_exactNB4_missing': universal_exact,
                      'universal_wide_missing': universal_wide,
                      'x0_full_fiber_missing_controller_slots': sorted(key for key in targets if reach0[key] != (1<<81)-1),
                      'x0_missing_endpoint_count': sum(81-reach0[key].bit_count() for key in targets),
                      'shortest1_but_has2walk': sorted(key for key in even if minimum[key] == 1)})
    numeric.append({'modulus': m, 'literal_voltage_vector': volts, 'roots': roots,
                    'strict_filter_missing_total': sum(len(x['author_strict_filter_missing']) for x in roots),
                    'wide_missing_total': sum(len(x['wide_I_R2_good4_missing']) for x in roots),
                    'universal_exactNB4_missing_total': sum(len(x['universal_exactNB4_missing']) for x in roots),
                    'universal_wide_missing_total': sum(len(x['universal_wide_missing']) for x in roots),
                    'x0_missing_endpoints_total': sum(x['x0_missing_endpoint_count'] for x in roots)})
minimum = min(x['good4_union_even_distinct_forms'] for x in symbolic)
result = {'status': 'COMPLETE_FIXED_BASE_WORD_ANALYSIS',
          'base_alpha': perms[0], 'base_beta': perms[1], 'inverse_labeling': 'a/A and b/B, not involutions',
          'reduced4_count': 108, 'rank_histogram_reduced4': dict(Counter({3:len(bad),4:len(good)})),
          'bad_word_ids_matched_author': bad, 'bad_word_labels': [''.join(SYMBOLS[s] for s in reduced[i]) for i in bad],
          'minimum_good4_plus_even_distinct_forms': minimum,
          'P_19_LOCAL_FORM_BOTTLENECK': 'SUPPORTED' if minimum <= 19 else 'REFUTED',
          'minimum_x0_form_fiber_incidence_capacity': min(x['x0_form_fiber_incidence_capacity'] for x in symbolic),
          'numerical_profiles': numeric, 'CPU_seconds': time.process_time()-START,
          'graph_generated': False, 'BFS': 0, 'voltage_grid_assignments': 0,
          'literal_fixed_profiles': 2,
          'scope': 'Abelian8integeredgeforms and exactx0routeimages of <=4words; numericprofiles onlythefixedpublishedvoltagevector modulo19/20. Noauthor19..27sweep repeated.'}
(OUT / 'SYMBOLIC_SLOTS.json').write_text(json.dumps(symbolic, indent=2)+'\n')
(OUT / 'NUMERIC_WORD_TABLES.json').write_text(json.dumps(numeric, indent=2)+'\n')
(OUT / 'RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='numerical_profiles'},indent=2))
print('NUMERIC '+json.dumps([{k:v for k,v in x.items() if k!='roots'} for x in numeric],indent=2))
