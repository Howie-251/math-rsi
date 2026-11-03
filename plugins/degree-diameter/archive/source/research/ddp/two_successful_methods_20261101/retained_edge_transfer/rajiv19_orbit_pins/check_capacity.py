#!/usr/bin/env python3
"""Exact integer capacity gate for every one-Wline-plus8 pointpin rule.
Reads the already generated small gadget only; does not regenerate the source.
"""
import itertools
import json
import time
from pathlib import Path
HERE=Path(__file__).resolve().parent

def main():
    t=time.process_time()
    W=json.loads((HERE/'SOURCE_PARAMETERS.json').read_text())
    gn=[set() for _ in range(121)]
    for a,b in W['gadget']:gn[a].add(b);gn[b].add(a)
    rows=[]
    for a,b in itertools.combinations(range(11),2):
        target=set(range(11*a,11*(a+1)))|set(range(11*b,11*(b+1)))
        top=sorted([(len(gn[v]&target),v) for v in range(121) if v//11 not in (a,b)],reverse=True)[:9]
        cap=sum(c for c,v in top)
        rows.append({'omitted_pencils':[a,b],'target_count':22,'top9_optimistic_contributions':top,'coverage_upper':cap,'excluded':cap<22})
    survivors=[x for x in rows if not x['excluded']]
    assert [x['omitted_pencils'] for x in survivors]==[[3,9]]
    target=set(range(33,44))|set(range(99,110))
    groups=[]
    for a in range(11):
        if a in (3,9):continue
        candidates=[(len(gn[v]&target),v,sorted(gn[v]&target)) for v in range(11*a,11*(a+1))]
        maximum=max(x[0] for x in candidates)
        groups.append({'pencil':a,'maximum':maximum,'maximizers':[x for x in candidates if x[0]==maximum]})
    cap=sum(g['maximum'] for g in groups)
    assert cap==21<22
    proof={'status':'ALL_ONE_WLINE_PLUS8_POINTPIN_RULES_STRICTLY_EXCLUDED','selected_K_vertices_required':9,'reason_at_least9':'Each provider has15vertices;8*15=120<121','all55_omitted_pairs':rows,'only_surviving_optimistic_pair':[3,9],'at_least3_omitted_impossible':'Any3 omitted pencils contain a pair other than3,9, already excluded','thus_exactly9_selected_pencils':True,'one_selected_vertex_per_remaining_pencil':groups,'group_capacity_upper':cap,'required_omitted_targets':22,'CPU_seconds':time.process_time()-t,'solver_calls':0,'source_regenerated':False}
    (HERE/'ALL_BASE_CAPACITY_FINAL.json').write_text(json.dumps(proof,indent=2)+'\n')
    pre=json.loads((HERE/'PREPROCESS_RESULT.json').read_text())
    result={'status':proof['status'],'source_parameter':[19,3],'source_n':2783,'source_m':25773,'source_point_degree':18,'source_line_degree':19,'orbit11_point_targets_covered':1331,'orbit11_line_targets_covered':600,'one_Wline11_point_targets_covered':1331,'one_Wline11_line_targets_covered':1346,'only_exceptional_class_remaining_lines':106,'all_base_rules_compact_equivalence':'Choose9classKvertices with providers full11linepencil plus4gadgetneighbors; any one lifts to11basepoints and other8to singlepoints','all55_omitted_pairs_initially_excluded':54,'sole_surviving_pair':[3,9],'final_per_pencil_capacity':21,'required_omitted_target_count':22,'source_diameter':'inherited public source/Theorem1, not rerun','source_generated_once':True,'source_BFS_roots':0,'actual_point_line_provider_checks':1331,'preprocessing_CPU_seconds':pre['CPU_seconds'],'final_capacity_CPU_seconds':proof['CPU_seconds'],'solver_calls':0,'solver_budget_used':False,'graphs_added':0,'scope':'Any11affine points of one Wline plus at most8 additional old pointpins, across every baseKvertex and class; not arbitrary19pins, different geometry/source or cooperative helpers.'}
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'TERMINAL.json').write_text(json.dumps({'status':proof['status'],'running':False,'source_BFS_roots':0,'solver_calls':0,'graphs_added':0,'next':'Do not seed/base/class-scan the closed Wline family; arbitrary19pins and orbit+8 are unexcluded and unsearched.'},indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
