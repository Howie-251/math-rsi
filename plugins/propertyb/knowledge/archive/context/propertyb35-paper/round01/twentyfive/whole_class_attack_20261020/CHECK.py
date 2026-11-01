"""Tiny arithmetic receipt; no original-H or coloring enumeration."""
import json
from pathlib import Path
from time import process_time

start = process_time()
types = {}
local_tests = 0
for blue in range(8, 14):
    t = 15 - blue
    found = []
    for a in range(7):
        for q in range(7):
            for n3 in range(7):
                local_tests += 1
                if a + q + n3 != 6 or 2*a + q != 18-blue:
                    continue
                if q > t or a*(a-1) > 2*(t-q):
                    continue
                found.append([a, q, n3])
    expected = []
    for a in (2, 3):
        q, n3 = 18-blue-2*a, blue-12+a
        if min(q, n3) >= 0:
            expected.append([a, q, n3])
    assert sorted(found) == sorted(expected)
    types[str(blue)] = found

caps = {}
for blue, low_cap in ((9, 1), (10, 1), (11, 1), (12, 3), (13, 2)):
    root_term = (blue*(25-blue)-136)//2 - 9
    feasible = [c for c in range(26)
                if root_term+c <= low_cap + 2*c//3]
    caps[str(blue)] = max(feasible)
assert caps == {'9': 18, '10': 9, '11': 3, '12': 6, '13': 3}

# B12 with u=0,t=3: A is c=0 and the imported zero-cut theorem
# excludes c=0 for both types. Record only necessary integer projections.
b12 = {}
for low_total in range(3, 26):
    allowed = []
    for low_sinks in range(1, min(3, (low_total-1)//3)+1):
        for c in range(1, 26):
            if c+1 <= low_sinks + 2*c//3:
                allowed.append([low_sinks, c])
    b12[str(low_total)] = allowed
    if low_total <= 6:
        assert not allowed
    elif low_total <= 9:
        assert allowed == [[2, c] for c in range(1, 4)]
    else:
        assert allowed == ([[2, c] for c in range(1, 4)] +
                           [[3, c] for c in range(1, 7)])

# B13 extra owner charge g>=1. Include every possible c and low-S count.
b13 = []
for c in range(26):
    for g in range(1, 6):
        for low_sinks in range(3):
            for high_sinks in range(26):
                if 3*high_sinks > 2*c:
                    continue
                if 1+c+g <= low_sinks+high_sinks:
                    b13.append([c, g, low_sinks, high_sinks])
assert b13 == [[0, 1, 2, 0]]

result = {
    'status': 'PASS',
    'claim_status': 'same-family/provisional; conditional source reduction only',
    'original_H_enumeration': False,
    'new_probability_layouts': 0,
    'local_integer_tuples_tested': local_tests,
    'local_domain': 'b=8..13, each a,q,n3=0..6; all six-star row and capacity conditions',
    'tight_low_sink_types': types,
    'cross_excess_domain': 'c=0..25; total pair excess is 50, so actual 2c<=50',
    'unrestricted_low_sink_c_caps': caps,
    'b12_matching_remaining_integer_pairs_by_r': b12,
    'b13_extra_owner_projection_c_g_lowS_highS': b13,
    'whole_r_ge_3_branch_closed': False,
    'new_complete_r_branches_closed': [],
    'imports': [
        'TWENTYFIVE_SIX_STAR_SOURCE_NORMAL_FORM.md sections 9,13,14',
        'general_min_blue_20261020/GENERAL_SOURCE_REDUCTION.md sections 1..4',
        'TWENTYFIVE_B12_ZERO_CUT_SOURCE_BOUND.md (B12 c=0 only)'],
    'cpu_seconds': process_time()-start,
}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: result[k] for k in ('status', 'local_integer_tuples_tested', 'cpu_seconds')}))
