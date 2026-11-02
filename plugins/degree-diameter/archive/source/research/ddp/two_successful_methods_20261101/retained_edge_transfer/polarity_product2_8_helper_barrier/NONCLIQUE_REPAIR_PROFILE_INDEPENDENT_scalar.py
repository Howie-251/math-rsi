import time
START=time.process_time();WALL=time.time()
import json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(2,3))
D=Path(__file__).resolve().parent;STEM='NONCLIQUE_REPAIR_PROFILE_INDEPENDENT'
M=325;F=1625;CAP=31
degrees=[]
for d in range(32):
    upper=(d+6)*(31-d)
    degrees.append(dict(minimum_helper_degree=d,max_pins=31-d,
                        repair_bound_upper=upper,necessary_gate_pass=upper>=M))
allowed_d=[r['minimum_helper_degree'] for r in degrees if r['necessary_gate_pass']]
trows=[]
for t in range(1,32):
    p=31-t;Fbound=(6*t+24)*p;ok=Fbound>=F
    row=dict(t=t,helper_vertices=2*t,p_pin_cap=p,F_radius3_upper=Fbound,F_gate_pass=ok)
    if ok:
        assert t>=2 and p<=23
        c=max(0,(p-8)//2,p-16)
        left=(t-1)*M;right=t*((t+3)*p+c)
        row.update(C_p=c,global_union_intersection_left=left,
                   global_union_intersection_right_upper=right,
                   left_minus_right=left-right,necessary_global_gate_pass=left<=right,
                   max_union_size_two_parts=2*t*p,
                   max_union_at_least325=2*t*p>=M,
                   also_minimum_degree_gate=t in allowed_d)
    trows.append(row)
allowed_t=[r['t'] for r in trows if r['F_gate_pass']]
survivors=[r['t'] for r in trows if r['F_gate_pass'] and r['necessary_global_gate_pass']]
assert allowed_d==list(range(9,17))
assert allowed_t==list(range(8,20))
assert not survivors
eligible=[r for r in trows if r['F_gate_pass']]
result=dict(status='SUPPORTED_FIXED_LITERAL_CAP31_BALANCED_KTT_EXCLUSION_WITH_PLAIN_PROOF',
            inherited_g_table=[5,4,1,0,0,0],g_table_scope='fixed saved literal15 factor and its absolute/support pair; no new isomorphism/uniqueness claim',
            min_degree_allowed=allowed_d,balanced_t_after_F_bound=allowed_t,
            balanced_t_after_all_gates=survivors,
            minimum_strict_global_gap=min(r['left_minus_right'] for r in eligible),
            closest_rows=[r for r in eligible if r['left_minus_right']==min(x['left_minus_right'] for x in eligible)],
            degree_scalar_rows=degrees,balanced_scalar_rows=trows,
            whole_N_old_targets_per_class=26,free_vertices_per_class=5,
            actual_pin_counts_need_not_be_uniform_or_class_distinct=True,
            required_geometry_not_just_row_degree='genuine GQ unique point-to-line 3path gives other-absolute2support one hit on the8 B neighbors',
            mixed_F_helper_route_accounted_in_all_helper_pin_unions=True,
            global_intersection_charged_twice_per_class_minimum=True,
            closure_scope='balanced H=K(t,t) only in the fixed literal15 x genuine585, r4 uniform original-N copies, cap31, mandatoryedges retained, arbitrary added free-peer edges model',
            still_open=['arbitrary nonclique helper graphs','unbalanced bipartite helper graphs','changed source','changed old mandatory edges','other caps'],
            scalar_CPU_seconds=time.process_time()-START,CPU_budget_seconds=2,
            scalar_runs=1,old32_subset_or_toy_reruns=0,old585_or_Steiner_retests=0,
            graphs_generated_or_read=0,field_BFS_solver_Lean_paidreview_runs=0,
            root_state_Wiki_or_frozen_packets_modified=False,no_automatic_continuation=True)
(D/(STEM+'_RESULT.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
terminal=dict(status=result['status'],total_CPU_seconds=time.process_time()-START,
              wall_seconds=time.time()-WALL,CPU_budget_seconds=2,single_worker=True,
              all_processes_terminal=True,scalar_runs=1,no_automatic_continuation=True,
              measurement_boundary='One small integer d0..31/t1..31 sweep, imports, aggregation; no graph/field/table experiment.')
assert terminal['total_CPU_seconds']<2
(D/(STEM+'_TERMINAL.json')).write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(dict(terminal=terminal,min_degree_allowed=allowed_d,F_allowed_t=allowed_t,
                     final_survivors=survivors,min_gap=result['minimum_strict_global_gap'],closest=result['closest_rows']),indent=2))
