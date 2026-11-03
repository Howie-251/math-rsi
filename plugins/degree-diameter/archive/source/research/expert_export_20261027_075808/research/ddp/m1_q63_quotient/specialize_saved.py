#!/usr/bin/env python3
"""Exhaust the 7^5 translations of exactly the saved r2 quotient skeleton."""
from collections import Counter, deque
from itertools import product
from pathlib import Path
import importlib.util
import json
import random
import time

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('q63_symbolic', ROOT/'enumerate.py')
symbolic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(symbolic)


def mul(g, h):
    return ((g[0] + pow(2, g[1], 7)*h[0]) % 7, (g[1]+h[1]) % 9)


def inverse(g):
    return (-pow(2, -g[1], 7)*g[0] % 7, -g[1] % 9)


def direct_ball(root, a, b, S, max_depth=3):
    start = (root, 0, 0)
    seen = {start}
    queue = deque([(start, 0)])
    internal = ((a, inverse(a)), (b, inverse(b)))
    while queue:
        (side, x, i), depth = queue.popleft()
        if depth == max_depth:
            continue
        neighbors = [(side, *mul((x, i), t)) for t in internal[side]]
        neighbors += [(1-side, *mul((x, i), t if side == 0 else inverse(t))) for t in S]
        for v in neighbors:
            if v not in seen:
                seen.add(v)
                queue.append((v, depth+1))
    return seen


def evaluate_form(form, values):
    result = 0
    for value in values:
        result += (form % 7)*value
        form //= 7
    return result % 7


def instantiated_ball(balls, root, values):
    return {(side, evaluate_form(form, values), residue)
            for side, residues in enumerate(balls[root])
            for residue, bucket in enumerate(residues) for form in bucket}


def main():
    start = time.monotonic()
    result = json.loads((ROOT/'result.json').read_text())
    profile = result['profile_parameters']
    alpha, beta = profile['a'][1], profile['b'][1]
    original_S = sorted(profile['S'][1:], key=lambda s: s[1])
    sigmas = tuple(s[1] for s in original_S)
    balls = symbolic.symbolic_balls(alpha, beta, sigmas)
    # Independent exact group operations check full symbolic reachable sets,
    # including random skeletons outside the one being exhausted.
    rng = random.Random(631024)
    checks = []
    for trial in range(9):
        if trial == 0:
            aa, bb, ss = alpha, beta, sigmas
            values = (profile['a'][0], profile['b'][0], *(s[0] for s in original_S))
        else:
            aa, bb = rng.randrange(9), rng.randrange(9)
            ss = tuple(sorted(rng.randrange(9) for _ in range(3)))
            values = tuple(rng.randrange(7) for _ in range(5))
        a, b = (values[0], aa), (values[1], bb)
        S = [(0, 0)] + list(zip(values[2:], ss))
        trial_balls = symbolic.symbolic_balls(aa, bb, ss)
        for root in range(2):
            assert instantiated_ball(trial_balls, root, values) == direct_ball(root, a, b, S)
        checks.append({'alpha': aa, 'beta': bb, 'sigmas': ss, 'values': values})
    # All possible coefficient forms are evaluated once per assignment, then
    # reused across all36 root/side/residue buckets.
    forms = sorted({f for root in balls for side in root for bucket in side for f in bucket})
    form_index = {f: i for i, f in enumerate(forms)}
    digits = [tuple((f // (7**j)) % 7 for j in range(5)) for f in forms]
    buckets = [[[[form_index[f] for f in bucket] for bucket in side] for side in root] for root in balls]
    minimum = 253
    best = None
    minimum_count = 0
    histogram = Counter()
    tried = legal = 0
    for values in product(range(7), repeat=5):
        tried += 1
        a, b = (values[0], alpha), (values[1], beta)
        S = [(0, 0)] + list(zip(values[2:], sigmas))
        if a == (0, 0) or b == (0, 0) or len(set(S)) != 4:
            continue
        legal += 1
        v0,v1,v2,v3,v4 = values
        evaluated = [(d[0]*v0+d[1]*v1+d[2]*v2+d[3]*v3+d[4]*v4) % 7 for d in digits]
        counts = [[[len({evaluated[f] for f in bucket}) for bucket in side] for side in root] for root in buckets]
        score = 252-sum(n for root in counts for side in root for n in side)
        histogram[score] += 1
        if score < minimum:
            minimum = score
            minimum_count = 1
            best = {'a': a, 'b': b, 'S': S, 'values': values, 'covered_by_fiber': counts}
        elif score == minimum:
            minimum_count += 1
    # Verify the selected minimum against an independent direct graph walk.
    a, b, S = best['a'], best['b'], best['S']
    direct_score = sum(126-len(direct_ball(root, a, b, S)) for root in range(2))
    assert direct_score == minimum
    profile_values = (profile['a'][0], profile['b'][0], *(s[0] for s in original_S))
    profile_missing = []
    for root in range(2):
        reachable = instantiated_ball(balls, root, profile_values)
        profile_missing.append([[side,x,residue] for side in range(2) for residue in range(9)
                                for x in range(7) if (side,x,residue) not in reachable])
    output = {
        'status': 'SAVED_QUOTIENT_SKELETON_EXHAUSTED',
        'scope': {'alpha': alpha, 'beta': beta, 'sigmas': sigmas},
        'translation_assignments_checked': tried,
        'legal_translation_assignments': legal,
        'minimum_representative_missing_sum': minimum,
        'minimum_bad_unordered_pairs': 63*minimum//2,
        'assignments_attaining_minimum': minimum_count,
        'missing_sum_histogram': dict(sorted(histogram.items())),
        'best_parameters': best,
        'best_direct_bfs_missing_sum': direct_score,
        'saved_profile_missing_vertices_at_two_roots': profile_missing,
        'independent_symbolic_vs_direct_checks': checks,
        'elapsed_seconds': time.monotonic()-start,
        'nonclaim': 'No exclusion of other quotient skeletons, r4 template, or arbitrary graphs.'
    }
    (ROOT/'saved_skeleton_result.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['status','scope','translation_assignments_checked',
          'legal_translation_assignments','minimum_representative_missing_sum',
          'minimum_bad_unordered_pairs','assignments_attaining_minimum','elapsed_seconds']}))


if __name__ == '__main__':
    main()
