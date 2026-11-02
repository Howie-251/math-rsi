"""Exact CRT-projective translation classes for one fixed Loz phase pattern."""
from pathlib import Path
import collections
import json
import time

OUT = Path(__file__).resolve().parent
start = time.process_time()
modulus = 75
action = 2
phases = [1, 12, 11, 16]
powers = [pow(action, i, modulus) for i in range(20)]
assert pow(action, 20, modulus) == 1
gens = []
for i, phase in enumerate(phases):
    vector = [0, 0, 0]
    if i:
        vector[i - 1] = 1
    reverse = (-phase) % 20
    gens.extend([(phase, tuple(vector)),
                 (reverse, tuple(-powers[reverse] * x % modulus for x in vector))])
forms = [set() for _ in range(20)]
word_counts = [0] * 5


def visit(phase, vector, last, depth):
    forms[phase].add(vector)
    word_counts[depth] += 1
    if depth == 4:
        return
    scale = powers[phase]
    for index, (increment, shift) in enumerate(gens):
        if last >= 0 and index == (last ^ 1):
            continue
        visit((phase + increment) % 20,
              tuple((vector[k] + scale * shift[k]) % modulus for k in range(3)),
              index, depth + 1)


visit(0, (0, 0, 0), -1, 0)
counts = [len(values) for values in forms]
capacity = dict(status='CAPACITY_COMPLETE', counts=counts,
    minimum=min(counts), thinnest_phase=counts.index(min(counts)),
    word_counts=word_counts, CPU_seconds=time.process_time() - start)
(OUT / 'CAPACITY.json').write_text(json.dumps(capacity, indent=2) + '\n')

# Local primitive vectors modulo simultaneous unit multiplication. In Z25,
# normalize the first unit coordinate to one; earlier coordinates are
# multiples of five, rather than necessarily zero.
local3 = [(1, b, c) for b in range(3) for c in range(3)]
local3 += [(0, 1, c) for c in range(3)] + [(0, 0, 1)]
local25 = [(1, b, c) for b in range(25) for c in range(25)]
local25 += [(b, 1, c) for b in range(0, 25, 5) for c in range(25)]
local25 += [(b, c, 1) for b in range(0, 25, 5) for c in range(0, 25, 5)]
assert len(local3) == 13 and len(local25) == 775
representatives = [tuple(v[k] + 25 * ((u[k] - v[k]) % 3) for k in range(3))
                   for u in local3 for v in local25]
assert len(representatives) == len(set(representatives)) == 10075
ordered_phases = sorted(range(20), key=lambda phase: (counts[phase], phase))
ordered_forms = [sorted(values) for values in forms]
thin = ordered_phases[0]
histogram = collections.Counter()
survivors = []
hits = []
cases = 0
for B, C, D in representatives:
    if time.process_time() - start > 5:
        break
    cases += 1
    coverage = {}
    for phase in ordered_phases:
        values = {(b * B + c * C + d * D) % modulus
                  for b, c, d in ordered_forms[phase]}
        coverage[phase] = len(values)
        if phase == thin:
            histogram[len(values)] += 1
            if len(values) == modulus:
                survivors.append(dict(B=B, C=C, D=D))
        if len(values) != modulus:
            break
    else:
        parameters = dict(B=B, C=C, D=D, coverage=coverage)
        hits.append(parameters)
        print('FULL_HIT ' + json.dumps(parameters), flush=True)

result = dict(status='COMPLETE_PROJECTIVE_SCOPE' if cases == 10075 else 'CPU_LIMIT_UNATTEMPTED_REMAINDER',
    target_Delta=8, target_D=4, hypothetical_order=1500,
    fixed_modulus=75, fixed_action=2, fixed_inverse_pair_phases=phases,
    normalized_scope=10075, cases_executed=cases, cases_unattempted=10075 - cases,
    thinnest_phase=thin, thin_phase_survivors=len(survivors),
    thin_coverage_histogram=dict(sorted(histogram.items())), survivors=survivors,
    full_cover_hits=hits, new_graphs_generated=0, old_source_BFS_repeated=False,
    CPU_seconds=time.process_time() - start,
    prediction_supported=bool(survivors), general_CRT_graph_family_excluded=False,
    pending=[])
(OUT / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in ['survivors', 'full_cover_hits']}), flush=True)
