#!/usr/bin/env python3
"""Replay stored actual affine-extension witnesses, independently of ATTACK.py."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from time import process_time
import json

HERE=Path(__file__).resolve().parent

def check_candidate_upper(orbit):
    low=set(orbit['L'])
    assert len(low)==3 and low<=set(range(25))
    base={frozenset(5*x+y for y in range(5)) for x in range(5)}
    base.update(frozenset(5*x+(m*x+b)%5 for x in range(5)) for m in range(5) for b in range(5))
    pair_weight={}
    for line in base:
        contribution=len(line&low)
        for pair in combinations(sorted(line),2):
            assert pair not in pair_weight, 'Affine base does not give unique pair line'
            pair_weight[pair]=contribution
    assert len(base)==30 and len(pair_weight)==300
    count=0
    maximum=-1
    maximum_set=None
    for edge in combinations(sorted(set(range(25))-low),5):
        if frozenset(edge) in base:continue
        # The original affine pair has surplus zero; each extra contributes
        # one surplus unit to each of its ten pairs. The low centers placing
        # that pair in one block are exactly the low points of its base line.
        weight=sum(pair_weight[p] for p in combinations(edge,2))
        count+=1
        if weight>maximum:
            maximum=weight
            maximum_set=edge
    assert count==orbit['candidate_count'], 'Reported full candidate count differs'
    assert maximum==orbit['single_edge_weight_max'], 'Reported single-edge maximum differs'
    assert 5*maximum==orbit['top_five_weight_upper'], 'Reported five-extra upper bound differs'
    return {'name':orbit['name'],'L':sorted(low),'status':'PASS',
            'candidate_count':count,'single_edge_weight_max':maximum,
            'maximum_witness_extra':maximum_set,'five_extra_upper_bound':5*maximum,
            'sum_ge_78_possible_in_this_family':5*maximum>=78,
            'all_W_ge_26_possible_in_this_family':5*maximum>=78,
            'reported_solver_status':orbit['numerical_status'],
            'reported_solver_message':orbit['numerical_message'],
            'solver_failure_is_an_infeasibility_certificate':False}

def check_witness(row):
    points=set(range(25))
    low=set(row['L'])
    assert len(low)==3 and low<=points, 'Expected a three-point fixed low set'
    raw=row['edges']
    assert len(raw)==35, 'Not35 original edges'
    edges=[frozenset(e) for e in raw]
    assert all(len(e)==5 and len(e)==len(a) and e<=points for e,a in zip(edges,raw)), 'Invalid five-edge'
    assert len(set(edges))==35, 'Repeated original edge'
    base={frozenset(5*x+y for y in range(5)) for x in range(5)}
    base.update(frozenset(5*x+(m*x+b)%5 for x in range(5)) for m in range(5) for b in range(5))
    assert len(base)==30 and base<=set(edges), 'Missing affine line in encoding5*x+y'
    extra=set(edges)-base
    assert len(extra)==5, 'Not five non-line extras'
    if 'extra_edges' in row:
        assert {frozenset(e) for e in row['extra_edges']}==extra, 'Reported extras disagree'
    assert all(not(e&low) for e in extra), 'Extra intersects fixed low set'
    assert set.union(*(set(e) for e in extra))==points-low, 'Extra supports do not cover all and only nonlow points'
    degree={v:sum(v in e for e in edges) for v in range(25)}
    assert {v for v,d in degree.items() if d==6}==low, 'Actual six-degree set differs from fixed L'
    assert min(degree.values())==6 and sum(degree.values())==175, 'Wrong degree data'
    pair_count=Counter(p for e in edges for p in combinations(sorted(e),2))
    assert len(pair_count)==300 and min(pair_count.values())>=1, 'Pair coverage fails'
    W={}
    for z in sorted(low):
        blocks=[e-{z} for e in edges if z in e]
        assert len(blocks)==6 and all(len(q)==4 for q in blocks), 'Not a six four-block star'
        assert sum(map(len,blocks))==24 and set.union(*(set(q) for q in blocks))==points-{z}, 'Star is not the full partition'
        direct=sum(sum(len(e&q)*(len(e&q)-1)//2 for q in blocks) for e in edges if z not in e)
        pair_formula=sum(pair_count[tuple(sorted(p))]-1 for q in blocks for p in combinations(q,2))
        assert direct==pair_formula, 'The two independent W expressions disagree'
        W[z]=direct
    reported={int(k):int(v) for k,v in row['W'].items()}
    assert reported==W, 'Reported W values disagree with actual edges'
    total=sum(W.values())
    assert row['sum_W']==total, 'Reported total W disagrees'
    thresholds={'sum_ge_78':total>=78,'all_ge_26':min(W.values())>=26}
    if 'strong_average_counterexample' in row:
        assert row['strong_average_counterexample']==thresholds['sum_ge_78'], 'Reported strong-average flag disagrees'
    if 'all_low_W_at_least_26' in row:
        assert row['all_low_W_at_least_26']==thresholds['all_ge_26'], 'Reported minimum-W flag disagrees'
    if 'thresholds' in row:
        for key,claimed in row['thresholds'].items():
            assert key in thresholds and claimed==thresholds[key], 'Reported threshold claim disagrees'
    return {'status':'PASS','L':sorted(low),'degree_histogram':dict(sorted(Counter(degree.values()).items())),
            'base_lines_present':30,'extras':5,'W':W,'sum_W':total,'min_W':min(W.values()),
            'thresholds':thresholds,'mean_candidate_refuted':thresholds['sum_ge_78'],
            'minimum_candidate_refuted':thresholds['all_ge_26']}

def main():
    start=process_time()
    result=json.loads((HERE/'RESULT.json').read_text())
    assert 'stop_reason' in result, 'Wait for the complete attack receipt, not a prefix'
    witnesses=result['witnesses']
    candidate_checks=[check_candidate_upper(orbit) for orbit in result['orbits']]
    assert len(candidate_checks)==2
    checked=[]
    for index,row in enumerate(witnesses):
        try:
            checked.append({'index':index,**check_witness(row)})
        except (AssertionError,KeyError,TypeError,ValueError) as error:
            checked.append({'index':index,'status':'FAIL','error':str(error)})
    status='FAIL' if any(r['status']=='FAIL' for r in checked) else 'PASS'
    output={'status':status,'scope':'Two authorized affine low-three orbits: complete single-extra candidate bounds, plus stored actual witnesses if any. No ATTACK import, baseline construction, or coloring enumeration.',
            'input':'RESULT.json','attack_stop_reason':result['stop_reason'],'encoding':'vertex5*x+y, x,y inF5','witness_count':len(checked),
            'candidate_upper_checks':candidate_checks,'checks':checked,
            'no_actual_counterexample_stored':not bool(checked),
            'interpretation':'Exact candidate maxima exclude both threshold goals in these two affine-extension orbits only. Solver time limits are not used as infeasibility evidence.',
            'cpu_seconds':process_time()-start}
    (HERE/'VERIFY.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output))
    if status=='FAIL':raise SystemExit(1)

if __name__=='__main__':main()
