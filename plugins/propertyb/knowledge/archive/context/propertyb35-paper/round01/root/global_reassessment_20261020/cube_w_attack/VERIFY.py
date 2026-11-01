#!/usr/bin/env python3
"""Independent stdlib replay for the one authorized fixed cube-star attack."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from time import process_time
import json

HERE=Path(__file__).resolve().parent
POINTS=set(range(25)); LOW={0,1,2}

def derive_base():
    edges={frozenset((0,1,2,3,4))}
    for i in range(3):
        first=[{5+k for k in range(8) if (k>>i)&1==bit} for bit in range(2)]
        second=[{13+k for k in range(8) if (k>>i)&1==bit} for bit in range(2)]
        spare={21,22,23,24}
        if i==2:
            first[0].remove(5);first[0].add(21)
            spare.remove(21);spare.add(5)
        for block in first+second+[spare]:
            assert len(block)==4
            edges.add(frozenset({i}|block))
    assert len(edges)==16 and all(len(e)==5 for e in edges)
    return edges

def pair_counts(edges):
    return Counter(p for e in edges for p in combinations(sorted(e),2))

def check_base():
    edges=derive_base()
    deg={v:sum(v in e for e in edges) for v in range(25)}
    pairs=pair_counts(edges)
    for z in LOW:
        star=[e-{z} for e in edges if z in e]
        assert len(star)==6 and sum(map(len,star))==24
        assert set.union(*(set(q) for q in star))==POINTS-{z}
        assert all(pairs[tuple(sorted((z,v)))]==1 for v in POINTS-{z})
    target={v:(6 if v in LOW else 8 if v in (22,23,24) else 7) for v in range(25)}
    assert sum(target.values())==175
    residual={v:target[v]-deg[v] for v in range(25)}
    assert all(value>=0 for value in residual.values()) and sum(residual.values())==95
    missing=[list(p) for p in combinations(range(25),2) if pairs[p]==0]
    assert all(not (set(p)&LOW) for p in missing)
    base_W=[]
    for z in sorted(LOW):
        star=[e-{z} for e in edges if z in e]
        direct=sum(sum(len(e&q)*(len(e&q)-1)//2 for q in star) for e in edges if z not in e)
        second=sum(pairs[tuple(sorted(p))]-1 for q in star for p in combinations(q,2))
        assert direct==second
        base_W.append(direct)
    positive_repeat={v:sum(max(pairs[tuple(sorted((v,w)))]-1,0) for w in POINTS-{v}) for v in range(3,25)}
    repeat_left={v:4*target[v]-24-positive_repeat[v] for v in range(3,25)}
    return {'base_edge_count':len(edges),'base_degrees':deg,'target_degrees':target,
            'residual_degrees':residual,'base_covered_pairs':len(pairs),
            'base_missing_pairs':len(missing),'missing_high_pairs':missing,
            'base_maximum_codegree':max(pairs.values()),'extra_edge_count':19,
            'base_W':base_W,'base_high_pairs_covered':sum(not(set(p)&LOW) for p in pairs),
            'positive_base_repeat_rows':positive_repeat,'repeat_budget_left':repeat_left,
            'all_extra_vertices_high':True,'base_low_stars_full_partitions':True}

def check_actual(result,base):
    raw=result['edges'];edges=[frozenset(e) for e in raw]
    assert len(raw)==35 and len(set(edges))==35
    assert all(len(e)==5 and len(a)==5 and e<=POINTS for e,a in zip(edges,raw))
    assert derive_base()<=set(edges), 'Reconstructed cube base is missing'
    extras=set(edges)-derive_base()
    assert len(extras)==19 and all(not(e&LOW) for e in extras)
    assert set(result['L'])==LOW
    degree={v:sum(v in e for e in edges) for v in range(25)}
    assert degree==base['target_degrees'], 'Final target degrees fail'
    pairs=pair_counts(edges)
    assert len(pairs)==300 and min(pairs.values())>=1, 'Original pair cover fails'
    W={}
    for z in sorted(LOW):
        star=[e-{z} for e in edges if z in e]
        assert len(star)==6 and sum(map(len,star))==24
        assert set.union(*(set(q) for q in star))==POINTS-{z}
        first=sum(sum(len(e&q)*(len(e&q)-1)//2 for q in star) for e in edges if z not in e)
        second=sum(pairs[tuple(sorted(p))]-1 for q in star for p in combinations(q,2))
        assert first==second
        W[z]=first
    assert W=={int(k):int(v) for k,v in result['W'].items()}
    assert sum(W.values())==result['sum_W']
    assert min(W.values())>=26, 'Stored incumbent does not meet the authorized all-low W threshold'
    return {'status':'PASS','actual_original_edges':35,'L':sorted(LOW),'degrees':degree,
            'paircover':True,'W':W,'sum_W':sum(W.values()),'all_low_W_ge_26':True,
            'strong_average_candidate_refuted':sum(W.values())>=78,
            'property_B_counterexample_claimed':False}

def check_safe_candidates(base,reported):
    edges=derive_base()
    pairs=pair_counts(edges)
    old_neighbors={v:sum(1<<w for w in POINTS-{v} if pairs[tuple(sorted((v,w)))]>0) for v in range(3,25)}
    star=[[e-{z} for e in edges if z in e] for z in sorted(LOW)]
    raw_count=0;kept=0
    support=Counter();pair_support=Counter()
    maxima=[0,0,0];sum_max=0
    for candidate in combinations(range(3,25),5):
        raw_count+=1
        mask=sum(1<<v for v in candidate)
        if any((old_neighbors[v]&mask).bit_count()>base['repeat_budget_left'][v] for v in candidate):continue
        kept+=1
        support.update(candidate)
        pair_support.update(combinations(candidate,2))
        edge=set(candidate)
        coefficients=[sum(len(edge&q)*(len(edge&q)-1)//2 for q in blocks) for blocks in star]
        for i,value in enumerate(coefficients):maxima[i]=max(maxima[i],value)
        sum_max=max(sum_max,sum(coefficients))
    missing=base['missing_high_pairs']
    unsupported=[p for p in missing if pair_support[tuple(p)]==0]
    insufficient=[v for v in range(3,25) if support[v]<base['residual_degrees'][v]]
    actual={'all_high_five_sets':raw_count,'after_safe_row_prune':kept,
            'unsupported_missing_pairs':unsupported,'insufficient_vertex_support':insufficient,
            'single_extra_W_max':maxima,
            'nineteen_extra_linear_W_upper':[base['base_W'][i]+19*maxima[i] for i in range(3)],
            'single_extra_sumW_max':sum_max,
            'nineteen_extra_sumW_upper':sum(base['base_W'])+19*sum_max,
            'milp_rows':1+22+len(missing)+3+22}
    for key,value in actual.items():assert reported[key]==value, f'Reported cheap candidate field differs: {key}'
    actual['W_residual_thresholds']=[26-w for w in base['base_W']]
    assert actual['W_residual_thresholds']==[2,2,6]
    actual['safe_prune_reason']='Every base-covered pair gains one surplus unit per extra containing it. Fixed target degree and full paircover give row surplus4*d-24; existing positive surplus is already spent. New pair repetitions can only spend more.'
    return actual

def main():
    start=process_time()
    result=json.loads((HERE/'RESULT.json').read_text())
    assert 'stop_reason' in result, 'Wait for final authorized attack receipt'
    base=check_base()
    assert set(result['L'])==LOW
    assert {frozenset(e) for e in result['base_edges']}==derive_base()
    assert {int(k):int(v) for k,v in result['target_degree'].items()}==base['target_degrees']
    cheap=result['cheap_base']
    assert cheap['base_edge_count']==base['base_edge_count']
    assert cheap['base_W']==base['base_W']
    assert cheap['base_high_pairs_covered']==base['base_high_pairs_covered']
    assert cheap['missing_high_pairs']==base['base_missing_pairs']
    assert cheap['remaining_degree_sum']==sum(base['residual_degrees'].values())
    assert {int(k):int(v) for k,v in cheap['remaining_degree'].items()}=={v:base['residual_degrees'][v] for v in range(3,25)}
    for key in ('positive_base_repeat_rows','repeat_budget_left'):
        assert {int(k):int(v) for k,v in cheap[key].items()}==base[key]
    candidate_check=check_safe_candidates(base,cheap)
    checks=[]
    # No baseline generation: absent incumbent means base validation only.
    for row in result['witnesses']:
        try:checks.append(check_actual(row,base))
        except (AssertionError,KeyError,TypeError,ValueError) as error:
            checks.append({'status':'FAIL','error':str(error)})
    status='FAIL' if any(r['status']=='FAIL' for r in checks) else 'PASS'
    out={'status':status,'scope':'One fixed cube-star base, with actual incumbent replay only if present; no ATTACK import, optimization, coloring enumeration, or baseline.',
         'point_encoding':'cubeA5+bitint, cubeB13+bitint, LSB bit i; i2 swap21 and5',
         'stop_reason':result['stop_reason'],'base':base,'actual_incumbent_stored':bool(checks),
         'cheap_candidate_check':candidate_check,
         'actual_checks':checks,'reported_numerical_status':result.get('numerical_status'),
         'reported_numerical_message':result.get('numerical_message'),
         'solver_failure_is_infeasibility_certificate':False,
         'candidate_prune_independently_replayed':True,'optimization_independently_replayed':False,
         'cpu_seconds':process_time()-start}
    (HERE/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
    if status=='FAIL':raise SystemExit(1)

if __name__=='__main__':main()
