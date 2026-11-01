#!/usr/bin/env python3
"""Literal-edge and matching replay; no solver, new instance, or color enumeration."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from time import process_time
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[2]/'middle/pairing_global/COUNTEREXAMPLE.json'

def main():
    start=process_time()
    original=json.loads(SOURCE.read_text())
    found=json.loads((HERE/'RESULT.json').read_text())
    points=set(range(24))
    edges=[frozenset(e) for e in original['edges']]
    base=[frozenset(e) for e in original['base_edges']]
    extra=[frozenset(e) for e in original['extra_edges']]
    assert original['vertices']==24 and len(original['points'])==24
    assert len(edges)==35 and len(set(edges))==35
    assert all(len(e)==5 and e<=points for e in edges)
    assert len(base)==30 and len(extra)==5 and set(base)|set(extra)==set(edges) and not(set(base)&set(extra))
    degree={v:sum(v in e for e in edges) for v in range(24)}
    assert min(degree.values())>=7 and sum(degree.values())==175
    codegree=Counter(p for e in edges for p in combinations(sorted(e),2))
    assert len(codegree)==276 and min(codegree.values())>=1
    base_codegree=Counter(p for e in base for p in combinations(sorted(e),2))
    alpha=original['weighted_matching_vertex_dual']
    assert len(alpha)==24 and sum(alpha)==2 and all(a>=0 for a in alpha)
    for u,v in combinations(range(24),2):
        assert 1<=base_codegree[u,v]<=1+alpha[u]+alpha[v]
    matching=[tuple(p) for p in found['matching']]
    assert len(matching)==12 and all(len(p)==2 and p[0]!=p[1] for p in matching)
    assert Counter(v for p in matching for v in p)==Counter(points)
    pairsets=[frozenset(p) for p in matching]
    hit=[i for i,e in enumerate(edges) if any(p<=e for p in pairsets)]
    unhit=[i for i in range(35) if i not in hit]
    base_hit=sum(any(p<=e for p in pairsets) for e in base)
    extra_hit=sum(any(p<=e for p in pairsets) for e in extra)
    base_pair_total=sum(base_codegree[tuple(sorted(p))] for p in matching)
    assert base_hit<=base_pair_total<=len(matching)+sum(alpha)==14
    assert len(hit)==found['actual_hit_count']==19 and len(unhit)==16
    assert hit==found['hit_edge_indices'] and unhit==found['unhit_edge_indices']
    assert base_hit==base_pair_total==14 and extra_hit==5
    component={v:(i,side) for i,p in enumerate(matching) for side,v in enumerate(p)}
    signatures={i:{component[v][0]:component[v][1] for v in edges[i]} for i in unhit}
    assert all(len(signatures[i])==5 for i in unhit)
    compatible=[]
    incompatible=[]
    for i,j in combinations(unhit,2):
        shared=sorted(set(signatures[i])&set(signatures[j]))
        relative=[signatures[i][k]^signatures[j][k] for k in shared]
        okay=len(set(relative))<=1
        row={'edge_indices':[i,j],'shared_components':shared,'relative_signs':relative}
        if okay:
            k=len(shared)
            probability=Fraction(1,256) if k==0 else Fraction(1,2**(9-k))
            row['intersection_probability']=str(probability)
            compatible.append(row)
        else:
            row['actual_vertex_intersection']=sorted(edges[i]&edges[j])
            incompatible.append(row)
    assert len(compatible)==40
    assert compatible==found['compatible_unhit_pairs']
    largest=max(Fraction(r['intersection_probability']) for r in compatible)
    best=next(r for r in compatible if Fraction(r['intersection_probability'])==largest)
    assert best['edge_indices']==[10,14] and len(best['shared_components'])==3 and best['relative_signs']==[1,1,1]
    assert largest==Fraction(1,64)
    example=next(r for r in incompatible if r['edge_indices']==[1,10])
    assert len(example['actual_vertex_intersection'])==1 and len(example['shared_components'])==2
    assert set(example['relative_signs'])=={0,1}
    single_edge_probability=Fraction(1,16)
    union_bound=len(unhit)*single_edge_probability-largest
    assert union_bound==Fraction(63,64)<1
    out={'status':'PASS','scope':'Only the stored actual24/35 H and stored perfect matching; no MILP, new instance, orientation/color enumeration.',
         'input_hypergraph':'../../../middle/pairing_global/COUNTEREXAMPLE.json',
         'actual_vertices':24,'actual_edges':35,'minimum_degree':min(degree.values()),'paircover_checked':276,
         'matching':matching,'matching_size':12,'exact_hit_count':19,'unhit_count':16,
         'verified_old_dual_inequalities':276,'dual_vertex_weight_sum':sum(alpha),
         'base_pair_codegree_sum':base_pair_total,'base_edges_hit':base_hit,'extra_edges_hit':extra_hit,
         'analytic_matching_hit_upper_bound':19,'exact_maximum_by_matching_and_dual':19,
         'unhit_pair_count':len(compatible)+len(incompatible),'compatible_pair_count':len(compatible),
         'incompatible_pair_count':len(incompatible),'compatible_pairs':compatible,
         'selected_joint_event':best,'actual_intersection_one_incompatible_example':example,
         'single_unhit_edge_bad_probability':str(single_edge_probability),
         'failure_probability_upper_bound':str(union_bound),'proper_coloring_existence_proved_for_this_H':True,
         'new_general_unconditional_matching_selection_claimed':False,
         'proof_reason':'All hit edges proper; each unhit edge uses5 distinct fair matching components. Subtract the selected two-event intersection from the16 single-event union bound. Component-relative signs supply its joint count.',
         'cpu_seconds':process_time()-start}
    (HERE/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='compatible_pairs'}))

if __name__=='__main__':main()
