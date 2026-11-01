"""Small role/edge check for TIGHT_B13_REPAIR.md; no H enumeration."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from time import process_time
import json

start = process_time()
owners = set(range(2, 11))
# Role 0 is the other sink, role 1 the double owner z.
flow_trials = valid_projections = 0
for triple in combinations(range(11), 3):
    X = set(triple)
    slots = X & owners
    subs = [set(t) for k in range(len(slots)+1)
            for t in combinations(sorted(slots), k)]
    rhs = int(0 in X)
    for size1 in (2, 3):
        for size2 in (2, 3):
            for inside1 in subs:
                for inside2 in subs:
                    flow_trials += 1
                    outside1, outside2 = size1-len(inside1), size2-len(inside2)
                    if min(outside1, outside2) < 0:
                        continue
                    if inside1 & inside2:
                        continue
                    if max(outside1, outside2) > rhs:
                        continue
                    if outside1+outside2 > len(owners-slots):
                        continue
                    valid_projections += 1
                    assert 0 in X and 1 not in X
                    assert size1 == size2 == 2
                    assert len(inside1) == len(inside2) == 1
assert valid_projections == 72

# Actual 25 labels; every possible five-set is visited.  Necessary role
# constraints are proved in the text, not inferred from this check.
z, h1, h2 = 0, 1, 2
blue = set(range(12, 25))
Y1, Y2 = {12, 13}, {14, 15}
Y = Y1 | Y2
G = {0, 3, 4, 5, 6}
new_blue = (blue-Y1) | {z, h1}
profiles = Counter()
admissible = hz_coedges = tested = 0
for tup in combinations(range(25), 5):
    tested += 1
    F = set(tup)
    B = F & blue
    j = len(B)
    if j == 0:
        if F != G:
            continue
    elif j == 5:
        continue
    else:
        if any(pair <= F and j != 2 for pair in (Y1, Y2)):
            continue
        if z in F and F & Y and (j != 4 or F-blue != {z}):
            continue
        if j == 4:
            if h1 in F or h2 in F:
                continue
            if z in F and not (len(F & Y1) == len(F & Y2) == 1):
                continue
        if j == 3 and z in F and (h1 in F or h2 in F):
            continue
        if j == 2:
            if B == Y1:
                if h2 not in F or z in F or h1 in F:
                    continue
            elif B == Y2:
                if h1 not in F or z in F or h2 in F:
                    continue
            else:
                continue
        if j == 1:
            if h1 in F and not B <= Y1:
                continue
            if h2 in F and not B <= Y2:
                continue
            if B <= Y1 and h1 not in F:
                continue
            if B <= Y2 and h2 not in F:
                continue
    admissible += 1
    hz_coedges += int(z in F and h1 in F)
    after = len(F & new_blue)
    profiles[f'{j}->{after}'] += 1
    if j == 0:
        assert after == 1
    elif j == 1:
        assert after == (2 if z in F else 1)
    elif j == 2:
        assert after == (0 if B == Y1 else 3)
    elif j == 3:
        assert 2 <= after <= 4
    elif j == 4:
        assert 3 <= after <= 4
assert tested == 53130 and hz_coedges == 0

result = {
    'status': 'PASS',
    'review_independence': 'same-family',
    'acceptance_status': 'provisional',
    'scope': 'b13,u0,N2=2 lexicographically selected unique-low-bad-edge source',
    'whole_twentyfive_branch_claimed': False,
    'flow_role_trials': flow_trials,
    'flow_valid_projections': valid_projections,
    'all_flow_projections_force': ['other sink in X', 'z not in X', 'both endpoints hit z N4'],
    'five_sets_visited': tested,
    'necessary_role_admissible_five_sets': admissible,
    'admissible_coedges_z_h1': hz_coedges,
    'four_flip_old_to_new_blue_size_counts': dict(sorted(profiles.items())),
    'counter_scope': 'all five-sets under proved necessary roles; not enumeration of 35-edge hypergraphs',
    'new_probability_layouts': 0,
    'cpu_seconds': process_time()-start,
}
Path(__file__).with_name('TIGHT_B13_RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': result['status'], 'cpu_seconds': result['cpu_seconds'],
                  'flow_valid_projections': valid_projections,
                  'admissible_coedges_z_h1': hz_coedges}))
