"""Exact local samples and one supplied occupancy relaxation; no H search."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
from time import process_time
import json

start = process_time()
parts = [(1,1,1,1,1), (2,1,1,1), (2,2,1), (3,1,1), (3,2), (4,1)]
edges = [sum(1 << (4*i+j) for i,n in enumerate(p) for j in range(n)) for p in parts]
full = (1 << 24)-1
samples = {}
for name, nr in [('A', 4), ('C', 5)]:
    seq = []
    for chosen in combinations(range(6), nr):
        chosen_set = set(chosen)
        base = sum(15 << (4*i) for i in range(6) if i not in chosen_set)
        for selected in product(range(4), repeat=nr):
            seq.append(base | sum(1 << (4*i+j) for i,j in zip(chosen, selected)))
    samples[name] = seq
two = [sum(1 << x for x in pair) for pair in combinations(range(4), 2)]
samples['B'] = [sum(mask << (4*i) for i,mask in enumerate(tup))
                for tup in product(two, repeat=6)]
expected = {
    'A': ['3/256','11/384','13/240','71/960','7/60','2/15'],
    'B': ['1/16','1/24','1/36','0','0','0'],
    'C': ['11/256','7/96','3/32','31/384','1/12','1/24'],
}
records = {}
for name, seq in samples.items():
    rows = []
    for part, edge, want in zip(parts, edges, expected[name]):
        red = sum(not (edge & b) for b in seq)
        blue = sum((edge & b) == edge for b in seq)
        probability = F(red+blue, len(seq))
        assert probability == F(want)
        # A separate product formula, conditioning only on chosen block roles.
        if name == 'B':
            formula = 2
            for n in part:
                formula *= F(comb(4-n, 2-n), 6) if n <= 2 else 0
        else:
            nr = 4 if name == 'A' else 5
            occupancy = tuple(part)+(0,)*(6-len(part))
            formula = F(0)
            for chosen in combinations(range(6), nr):
                blue_p, red_p = F(1), F(1)
                for i,n in enumerate(occupancy):
                    if i in chosen:
                        blue_p *= F(1,4) if n == 1 else int(n == 0)
                        red_p *= F(4-n,4)
                    elif n:
                        red_p = 0
                formula += red_p+blue_p
            formula /= comb(6,nr)
        assert formula == probability
        rows.append(dict(part=list(part),red_count=red,blue_count=blue,
                         total=len(seq),probability=str(probability)))
    records[name] = rows

base = F(3,256)
cost = [sum(comb(n,2) for n in part) for part in parts]
slopes = [(F(p)-base)/w for p,w in zip(expected['A'][1:], cost[1:])]
assert max(slopes) == F(403,15360)
gate = 29*base + 25*max(slopes)
assert gate == F(15295,15360) < 1
success_samples = len(samples['A']) - (gate*len(samples['A'])).numerator // (gate*len(samples['A'])).denominator
assert success_samples == 17

# Exact verification of a single supplied necessary six-block relaxation.
root = Path(__file__).parent
relax = json.loads((root/'PORTFOLIO_RELAXATION.json').read_text())
matrix = relax['rows']
assert len(matrix) == 29
types = Counter(tuple(sorted(row, reverse=True)) for row in matrix)
assert types == Counter({(1,1,1,1,1,0):17, (2,1,1,1,0,0):6, (3,2,0,0,0,0):6})
assert all(sum(row) == 5 and max(row) <= 4 for row in matrix)
column = [sum(row[i] for row in matrix) for i in range(6)]
cross = [sum(row[i]*row[j] for row in matrix) for i,j in combinations(range(6),2)]
assert min(column) >= 20 and min(cross) >= 16
W = sum(comb(x,2) for row in matrix for x in row)
assert W == 30
portfolio = {name:17*F(probs[0])+6*F(probs[1])+6*F(probs[4])
             for name, probs in expected.items()}
assert portfolio == {'A':F(1371,1280),'B':F(21,16),'C':F(427,256)}
assert all(v > 1 for v in portfolio.values())

fixed_pairs = []
matrix_edges = [sum(1 << (4*i+j) for i,n in enumerate(row) for j in range(n))
                for row in matrix]
for pair in combinations(range(6),2):
    rest = [i for i in range(6) if i not in pair]
    base_mask = sum(15 << (4*i) for i in pair)
    failure_incidence = 0
    for chosen in product(range(4),repeat=4):
        mask = base_mask | sum(1 << (4*i+j) for i,j in zip(rest,chosen))
        failure_incidence += sum(not (edge & mask) or (edge & mask)==edge
                                 for edge in matrix_edges)
    exact = F(failure_incidence,256)
    formula = F(0)
    for row in matrix:
        red, blue_p = F(1), F(1)
        for i,n in enumerate(row):
            if i in pair:
                if n:
                    red = F(0)
            else:
                red *= F(4-n,4)
                blue_p *= F(1,4) if n==1 else int(n==0)
        formula += red+blue_p
    assert exact == formula
    omitted = sum(row[pair[0]]==0 for row in matrix[:17]) + sum(row[pair[1]]==0 for row in matrix[:17])
    rainbow_formula = F(4*17-3*omitted,256)
    assert rainbow_formula >= 0
    fixed_pairs.append(dict(full_blue_blocks=list(pair),bound=str(exact),strict=exact<1))
assert sum(row['strict'] for row in fixed_pairs)==8
assert min(F(row['bound']) for row in fixed_pairs)==F(149,256)

# The global low-incidence polynomial inequality is pointwise, not fitted.
g = [low*comb(5-low,2) for low in range(6)]
envelope = [6*low-3*comb(low,2) for low in range(6)]
assert all(x <= y for x,y in zip(g,envelope))
assert all(36*r-3*comb(r,2) < 26*r for r in range(8,26))
result = dict(
    status='PASS', review_independence='same-family', acceptance_status='provisional',
    local_probabilities=records,
    sample_counts={name:len(seq) for name,seq in samples.items()},
    total_edge_sample_checks=sum(len(seq) for seq in samples.values())*6,
    inside_pair_costs=cost, A_excess_slopes=[str(s) for s in slopes],
    maximum_A_excess_slope=str(max(slopes)), W25_union_bound=str(gate),
    guaranteed_successful_A_samples_at_W25=success_samples,
    portfolio_relaxation=dict(type_counts=[17,6,0,0,6,0],W=W,columns=column,
                             block_pair_cross_counts=cross,
                             bounds={k:str(v) for k,v in portfolio.items()},
                             actual_H_claim=False),
    conditional_A_on_saved_matrix=fixed_pairs,
    conditional_edge_sample_checks=29*15*256,
    g_by_edge_low_count=g, g_quadratic_majorant=envelope,
    conditional_new_scope='all pair codegrees <=2 and r>=8 implies Property B',
    original_Hs_enumerated=0,new_layout_inventory=False,
    cpu_seconds=process_time()-start)
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','total_edge_sample_checks','W25_union_bound','cpu_seconds']}))
