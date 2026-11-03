#!/usr/bin/env python3
"""Exact symbolic short-word capacity for the q63 two-orbit 2+4 template.

One CPU; standard library only. No random search or graph annealing.
"""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time

OUT = Path(__file__).resolve().parent
POW2 = tuple(pow(2, i, 7) for i in range(9))
POW7 = tuple(7**i for i in range(5))


def symbolic_balls(alpha, beta, sigmas, max_depth=3):
    """Return 2 roots x 2 destination sides x 9 residue sets of F7^5 forms.

    A linear form is encoded by five base7 coefficient digits. Variables are
    ax,bx,s1x,s2x,s3x. No assignment restrictions are used in this bound.
    """
    internal = (alpha, beta)
    generators = []
    for side in range(2):
        residue = internal[side]
        edges = [(side, residue, side, 1),
                 (side, (-residue) % 9, side, -POW2[(-residue) % 9] % 7),
                 (1-side, 0, -1, 0)]
        for v, sigma in enumerate(sigmas, 2):
            if side == 0:
                edges.append((1, sigma, v, 1))
            else:
                edges.append((0, (-sigma) % 9, v,
                              -POW2[(-sigma) % 9] % 7))
        generators.append(edges)
    balls = []
    for root in range(2):
        seen = {(root, 0, 0)}
        frontier = seen.copy()
        for depth in range(max_depth):
            new = set()
            for side, residue, form in frontier:
                for target, delta, variable, coefficient in generators[side]:
                    nxt = form
                    if variable >= 0:
                        place = POW7[variable]
                        digit = (form // place) % 7
                        value = (digit + POW2[residue] * coefficient) % 7
                        nxt += (value - digit) * place
                    state = (target, (residue + delta) % 9, nxt)
                    if state not in seen:
                        new.add(state)
            seen.update(new)
            frontier = new
        buckets = [[set() for residue in range(9)] for side in range(2)]
        for side, residue, form in seen:
            buckets[side][residue].add(form)
        balls.append(buckets)
    return balls


def capacities(balls):
    return [[[len(bucket) for bucket in side] for side in root] for root in balls]


def main():
    start = time.monotonic()
    histogram = Counter()
    survivors = []
    best_deficit = None
    minimum_examples = []
    checked = 0
    for alpha in range(9):
        for beta in range(9):
            for sigmas in combinations_with_replacement(range(9), 3):
                counts = capacities(symbolic_balls(alpha, beta, sigmas))
                deficit = sum(max(0, 7-n) for root in counts for side in root for n in side)
                histogram[deficit] += 1
                checked += 1
                row = {'alpha': alpha, 'beta': beta, 'sigmas': sigmas,
                       'symbolic_deficit': deficit, 'capacities': counts}
                if best_deficit is None or deficit < best_deficit:
                    best_deficit = deficit
                    minimum_examples = [row]
                elif deficit == best_deficit and len(minimum_examples) < 20:
                    minimum_examples.append(row)
                if deficit == 0:
                    survivors.append(row)
    # The saved root profile is read only after enumeration and never constrains it.
    project = OUT.parents[2]
    profile_path = project/'computations/ddp/m1/split_profile/Meta_7_9_2_r2.json'
    metadata_path = project/'computations/ddp/m1/group_tables/Meta_7_9_2.json'
    profile = json.loads(profile_path.read_text())
    labels = json.loads(metadata_path.read_text())['labels']
    a = labels[profile['A'][0]]
    b = labels[profile['B'][0]]
    S = [labels[i] for i in profile['S']]
    ordered_S = sorted(S[1:], key=lambda x: x[1])
    sigmas = tuple(s[1] for s in ordered_S)
    counts = capacities(symbolic_balls(a[1], b[1], sigmas))
    result = {
        'status': 'EXHAUSTIVE_SYMBOLIC_CAPACITY_ENUMERATION_COMPLETE',
        'scope': 'G=F7 semidirect C9 by action2, two orbits, internal2/cross4, diameter3',
        'skeleton_count': checked,
        'enumeration': 'alpha,beta in0..8; sorted three S quotient labels in0..8 with repetitions; fourth S=e',
        'minimum_symbolic_deficit': best_deficit,
        'survivor_count': len(survivors),
        'deficit_histogram': dict(sorted(histogram.items())),
        'minimum_examples': minimum_examples,
        'profile_parameters': {'a': a, 'b': b, 'S': S},
        'profile_symbolic_capacities': counts,
        'profile_symbolic_deficit': sum(max(0, 7-n) for root in counts for side in root for n in side),
        'profile_actual_missing_sum': profile['representative_missing_sum'],
        'elapsed_seconds': time.monotonic() - start,
    }
    (OUT/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    (OUT/'surviving_skeletons.json').write_text(json.dumps(survivors, separators=(',', ':'))+'\n')
    print(json.dumps({k: result[k] for k in [
        'status', 'skeleton_count', 'minimum_symbolic_deficit', 'survivor_count',
        'profile_symbolic_deficit', 'profile_actual_missing_sum', 'elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
