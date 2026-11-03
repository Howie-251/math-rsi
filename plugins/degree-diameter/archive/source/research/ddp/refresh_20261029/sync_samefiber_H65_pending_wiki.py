"""Record completed new route classes and local H65 evidence, not a future run."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'aris_repo/tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


helper,capture=module('research_wiki'),module('capture_filter')


def screen(text):
    assert not capture.screen(text),capture.screen(text)
    return text


def load(relative):
    return json.loads((HERE/relative).read_text())


def evidence(folder):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE/folder).rglob('*'))
        if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'} and '__pycache__' not in p.parts]


shared=load('f5_induced_shared_routes_model/CEGIS_TERMINAL.json')
same=load('f5_induced_same_fiber_route_gate/RESULT.json')
samemodel=load('f5_induced_same_fiber_model/SAME_FIBER_ONLY_MODEL.json')
combined_model=load('f5_induced_same_fiber_model/MODEL.json')
combined_actual=load('f5_induced_same_fiber_model/CEGIS_TERMINAL.json')
h65=load('f5_partial_line_occupancy/RESULT.json')
h65model=load('f5_partial_line_occupancy/H65_CNF/MODEL.json')
prefix=ROOT/'reviews/ddp/f5_induced_support_shared_20261030'
review=json.loads(prefix.with_suffix('.response.json').read_text())['structuredContent']
assert (review['status'],review['model'],review['effort'])==('SUCCESS','gemini-3.8-flash-high','high')
assert shared['status']=='UNKNOWN' and shared['actual_solver_calls']==1 and shared['running'] is False
assert shared['solver_CPU_seconds']==59.879698
assert shared['exact_bad_pair_cuts']==0 and shared['hit'] is None
assert same['status']=='COMPLETE_ALL_PREDICTIONS_SUPPORTED' and same['pairs_checked']==7750
assert (samemodel['pairs'],samemodel['additional_clauses'],samemodel['additional_variables'])==(232500,930000,0)
assert (samemodel['variables'],samemodel['clauses'])==(315221,2220903)
assert (combined_model['variables'],combined_model['clauses'])==(333551,2316695)
assert combined_actual['status']=='RAW_UNSAT_UNCERTIFIED'
assert combined_actual['actual_solver_calls']==1 and combined_actual['running'] is False
assert combined_actual['rounds'][0]['solver']['returncode']==20
assert combined_actual['pending']==[] and combined_actual['hit'] is None
assert h65['quotient']['subsets_checked']==33554432 and h65['quotient']['largest_triangle_free_subset']==12
assert h65model['status']=='PREPARED_NOT_SOLVED' and h65model['solver_calls']==0
assert (h65model['new_variables'],h65model['total_new_clauses_if_all_fragments_used'])==(18330,95792)
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows'])==374
identifier='ddp-f5-literal3750-induced-retention-max16-d3-20261029'
row=copy.deepcopy(next(r for r in before['rows'] if r['id']==identifier)['source_record'])
variants={v['label']:v for v in row['variants']}
review_meta=dict(status='SUCCESS_SOUND_AS_STATED',actual_model=review['model'],effort=review['effort'],
    thread_id=review['threadId'],
    scope='StaticNextClosurecompletenesslogic,sixsavedlargesupports,densitymatching/full30necessity,andexternalshared-middleformula;nooutputrerun,CNF,UNSAT,graphorLean certification.',
    subsequent_H65_or_same_fiber_classification_reviewed=False,
    response=str(prefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition=str(prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
for label in [
    'complete30_fiber_Horn_support_closure_prediction_H_refuted_20261029',
    'proper_support_projection_and_partial_fiber_density_full30_necessity_20261029',
    'external_five_short_routes_share_middle_point_new_retention_clauses_20261029']:
    variants[label]['combined_external_review_status']='SUCCESS_SOUND_AS_STATED'
    variants[label]['actual_support_shared_static_review']=review_meta
variants['external_five_short_routes_share_middle_point_new_retention_clauses_20261029']['new_solver_run_recorded']=True
additions=[
 dict(label='shared_middle_full30_model315221_single60second_UNKNOWN_20261030',
    status='UNKNOWN_TERMINAL',variables=315221,clauses=1290903,
    actual_solver_calls=1,solver_CPU_seconds=59.879698,
    whole_CPU_seconds=shared['total_CPU_seconds_including_prior_preparation'],
    SAT_candidates=0,exact_bad_pair_cuts=0,hit=None,running=False,pending=[],
    result='research/ddp/refresh_20261029/f5_induced_shared_routes_model/CEGIS_TERMINAL.json',
    automatic_resume_allowed=False,general_induced_problem_excluded=False),
 dict(label='fixed_fiber0_all7750_pairs_full_short_route_gate_20261030',
    status=same['status'],pairs=7750,two_midpoint_histogram={'0':6750,'5':1000},
    three_walk_count_histogram_fixed_x_less_y={'2':7750},
    unordered_internal_AND_term_histogram={'2':7750},
    all_four_internal_vertices_distinct=True,four_direction_pairs_each=250,
    total_two_step_paths=5000,total_three_walks_fixed_x_less_y=15500,
    exact_no_two_step_condition='RetainedendpointsrequireoneoftwodisjointinternalpairANDtermswhollyretained.',
    aggregate_CPU_seconds=same['aggregate_compile_run_driver_CPU_seconds'],
    source_cache_reads=1,source_edge_reads=0,BFS_runs=0,solver_calls=0,new_graphs=0),
 dict(label='all30_fibers232500_pairs_exact_same_fiber_distance_CNF_prepared_20261030',
    status='PREPARED_NOT_SOLVED',pairs=232500,with_two_step_pairs=30000,
    without_two_step_pairs=202500,total_two_step_paths=150000,total_three_step_paths=465000,
    all_four_internal_vertices_distinct=True,old_exact_OR5_flags_reused=3000,
    new_clauses=930000,new_variables=0,prepared_variables=315221,prepared_clauses=2220903,
    exact_condition='keepx&keepy=>OR5midpointsOR(keepa&keepb)OR(keepc&keepd);fourdistributiveclausesperpair.',
    complete_same_fiber_endpoint_class=True,complete_global_D3_model=False,
    aggregate_prepare_CPU_seconds=samemodel['aggregate_CPU_seconds'],
    source_cache_reads=1,source_edge_reads=0,BFS_runs=0,solver_calls=0,new_graphs=0,
    new_route_classes_external_review='PENDING',merged_H65_main_run_recorded=True,
    standalone_same_fiber_only_CNF_not_solved=True),
 dict(label='H65_partial_line_grid_rule_sharp_threshold_and_all_high_obstruction_20261030',
    status='LOCAL_PAPER_AND_FINITE_QUOTIENT_COMPLETE_EXTERNAL_REVIEW_PENDING',
    exact_single_row_truth_states=2048,quotient_points=25,
    quotient_subsets_enumerated=33554432,noncollinear_direction_triangles=100,
    maximum_subset_without_such_triangle=12,
    H65_scope='Bothendsofoneexternaledgehave>=65retainedpointsandobeybidirectionalshared-middlecenterconditions.',
    H65_conclusion='Sourceisunionoffulledgelines;targetisitsT_ptransport;thetwosizesareequal.',
    H65_provider_flags_not_needed=True,
    lowering_threshold_to64_refuted_by=dict(source_size=64,target_size=65,
        provider_flags_relaxed_true=True,local_grid_conditions_checked=750,
        full_graph_degree_or_D3_feasibility_claimed=False),
    unqualified_full_or_zero_prediction='REFUTED by adjacent singleton pair',
    all30_fibers_at_least65_impossible_under_max16_D3=True,
    all_high_obstruction='Twoexternaldirectionsgive25m,degree16forcesallm=3;dart0->20p1failsplane_transport.',
    record_candidate_n1921_requires_at_least_one_high_and_one_low=True,
    each_external_C5_has_a_low_fiber_proved=False,
    general_nonuniform_induced_problem_excluded=False,
    aggregate_CPU_seconds=h65['aggregate_CPU_seconds'],
    source_edge_reads=0,source_BFS=0,SAT_calls=0,new_graphs=0,
    local_independent_static_review='PASS_PARENT_REPORTED',
    new_H65_and_routeclasses_external_review='PENDING'),
 dict(label='H65_exact_threshold_flags_and_conditional_line_CNF_fragments_prepared_20261030',
    status='PREPARED_NOT_SOLVED',parent_variable_max=315221,
    high_definition='h_a iff retainedcountinfibera>=65',new_variables=18330,
    highest_new_variable=333551,
    exact_count_flags_and_bindings_clauses=76290,
    conditional_line_saturation_and_transport_clauses=19500,
    exists_high_clause=1,not_all_high_clause=1,total_new_clauses=95792,
    prepare_CPU_seconds=h65model['CPU_seconds'],source_edge_reads=0,BFS_runs=0,
    solver_calls=0,merged_final_main_model_recorded=True,
    independent_fragment_range_rebasing_required_if_other_new_variables_collide=True),
 dict(label='combined_same_fiber_H65_333551_model_rawUNSAT_uncertified_20261030',
    status='RAW_UNSAT_UNCERTIFIED',variables=333551,clauses=2316695,
    exact_same_fiber_added_clauses=930000,H65_added_clauses=95792,
    original_same_fiber_only_CNF_and_MODEL_preserved=True,
    separate_from_old_shared_UNKNOWN_batch=True,
    actual_solver_calls=1,solver_exit_code=20,
    solver_CPU_seconds=combined_actual['solver_CPU_seconds'],
    whole_CPU_seconds=combined_actual['total_CPU_seconds_including_prior_preparation'],
    solver_CPU_budget=300,whole_CPU_budget=360,maximum_calls=3,first_window=180,
    SAT_candidates=0,exact_bad_pair_cuts=0,hit=None,running=False,pending=[],
    proof_log_certified=False,strict_general_induced_exclusion_registered=False,
    automatic_resume_allowed=False,
    result='research/ddp/refresh_20261029/f5_induced_same_fiber_model/CEGIS_TERMINAL.json')]
variants.update({v['label']:v for v in additions})
row['variants']=list(variants.values())
row['failure_or_result']+='；shared/full30增强315221/1290903单call UNKNOWN：59.879698solver/60.46906406wholeCPU，0候选/cuts。新同层门全7750支持预测，随后全30层232500pair精确类编码增930000clauses（零变量），准备1.385191193CPU。H65局部商1.162269237CPU、64/65边界反例与全高不可能为本地证明。实际合并333551/2316695主模型唯一call返回rawUNSAT/code20、54.406117solver/57.894923521wholeCPU，0候选/cuts；未认证，不登记一般诱导域严格排除。'
row['other_metrics'].update(
    newest_support_density_shared_paper_external_review='SUCCESS_SOUND_AS_STATED',
    enhanced_retention_solver_run_recorded=True,
    shared_full30_model_status='UNKNOWN_TERMINAL',
    shared_full30_solver_calls=1,shared_full30_solver_CPU_seconds=59.879698,
    shared_full30_whole_CPU_seconds=60.46906406,
    shared_full30_candidates=0,shared_full30_exact_cuts=0,
    same_fiber_local7750_pairs_supported=True,
    same_fiber_all30_pairs=232500,same_fiber_new_clauses=930000,
    same_fiber_class_model_prepared=True,same_fiber_class_solver_calls=0,
    H65_local_lemma_supported=True,H65_sharp_boundary=[64,65],
    all30_layers_high_impossible=True,general_nonuniform_problem_excluded=False,
    H65_plus_new_route_classes_external_review='PENDING',
    final_samefiber_H65_main_merged_or_run_recorded=True,
    current_retention_main_status='RAW_UNSAT_UNCERTIFIED',
    combined_samefiber_H65_variables=333551,combined_samefiber_H65_clauses=2316695,
    combined_samefiber_H65_actual_solver_calls=1,
    combined_samefiber_H65_solver_CPU_seconds=combined_actual['solver_CPU_seconds'],
    combined_samefiber_H65_whole_CPU_seconds=combined_actual['total_CPU_seconds_including_prior_preparation'],
    general_induced_problem_strictly_excluded=False)
row['lesson_and_restart_condition']='旧shared/full30必要模型已实际UNKNOWN停止，未因静态审阅PASS续预算。同fiber完整类和H65高低混合提供实际不同的结构表示，合并新主模型已唯一call得发现级rawUNSAT，非旧timer续时；原same_fiber_only和旧shared终态保留。无可信proof-log证书，不能由code20或在途外审登记一般诱导不存在，也不因仍有预算自动续算。'
row['unclosed_gap']='同层+H65完整必要模型本批实际RAW_UNSAT_UNCERTIFIED、0候选、已停；缺严格求解证书，尚不登记一般n≥1921非均匀诱导域排除。support_shared外审已SUCCESS/SOUND AS STATED，仅覆盖支持/密度/shared旧证明；H65和新routeclasses外审仍真实在途，不冒PASS。'
report='''# 同层完整路线与H65：已完成内容及待回执边界

shared/full30增强模型315221变量/1290903子句已实际单call59.879698solverCPU、60.46906406wholeCPU后UNKNOWN，0候选/精确cuts，已停止。support_shared实际GeminiSUCCESS/SOUND AS STATED限原支持枚举逻辑、density/full30及shared-middle证明，不认证输出重跑、CNF或新H65。

固定fiber0全部7750对直接路线门支持预测，总0.769884981CPU；每对2三步walk，对应2个不同且内部不交的AND项，1000对另有5二步中点。全30层随后完整枚举232500对，累计150000二步路、465000三步路；复用3000exactOR5，四条分配子句/对，共930000新clauses、零变量，315221/2220903模型准备完成（1.385191193CPU），仍非全部D3条件、未求解。

H65精确网格单行2048状态及25点商全部2^25枚举完成，后者最大无三方向非共线三角形集12；总1.162269237CPU。双端≥65的external局部必要规则迫整线及T_p运输；64/65局部反例说明不能直接降阈值。所有30层均≥65与max16逐点度及0→20平面运输冲突，所以纪录候选须有高低混合；不证明每C5有低层。H65分量95792clauses/18330variables与同层规则实际合并为333551vars/2316695clauses，唯一call已终态RAW_UNSAT_UNCERTIFIED/code20，54.406117solver/57.894923521wholeCPU，0候选/cuts。原same_fiber_only与旧shared终态保留；这是新规则生成模型而非续旧timer。未认证求解证书，不能据此登记一般非均匀域严格排除。

H65+新routeclasses外审仍是真实在途原call，不重试、不声明通过。复用原induced一行，ledger374、104/4、confirmed103/3、Lean1不变；专家23:55快照冻结不重包，root文件未改。等最终主批真实终态后再最后query。
'''
report_path=HERE/'SAMEFIBER_H65_PENDING_WIKI_REPORT.md'
report_path.write_text(screen(report))
paths=[]
for folder in ['f5_induced_shared_routes_model','f5_induced_same_fiber_route_gate',
               'f5_induced_same_fiber_model','f5_partial_line_occupancy']:
    paths+=evidence(folder)
paths+=[str(prefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md','.response.json','.DISPOSITION.md']]
paths+=[str(report_path.relative_to(ROOT))]
row['report_paths']=list(dict.fromkeys(row['report_paths']+paths))
screen(json.dumps(row,ensure_ascii=False))
assert all((ROOT/p).exists() for p in row['report_paths'])
pending=HERE/'SAMEFIBER_H65_PENDING_WIKI_ROWS.json'
pending.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==374
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key]==after[key]
with (HERE/'SAMEFIBER_H65_PENDING_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Existinginducedrow updated:shared315221model actualUNKNOWN,fullsamefiberclass/H65 merged333551/2316695 actualsinglecall rawUNSATuncertified54.406117solver/57.894923521wholeCPU. support_sharedactualSUCCESS/SOUND AS STATED distinctfrompendingH65review; no strictgeneralexclusion. ledger374 andvalidgraphcountsunchanged;expert23:55frozen;finalquerypendingroot.')
receipt=dict(status='PASS_SAMEFIBER_H65_RAW_UNSAT_RECORDED_PENDING_REVIEW_FINAL',
    updated_UTC=NOW,existing_id=identifier,record_count=374,
    shared_main_status='UNKNOWN_TERMINAL',shared_solver_CPU_seconds=59.879698,
    shared_whole_CPU_seconds=60.46906406,same_fiber_all30_pairs=232500,
    same_fiber_added_clauses=930000,same_fiber_only_model_status='PREPARED_INCREMENT_PRESERVED',
    H65_local_status='SUPPORTED_WITH_64_65_BOUNDARY_AND_ALL_HIGH_EXCLUSION',
    new_H65_routeclasses_review='PENDING',support_shared_review=review_meta,
    final_merged_main_run_recorded=True,combined_main_status='RAW_UNSAT_UNCERTIFIED',
    combined_main_variables=333551,combined_main_clauses=2316695,
    combined_main_solver_CPU_seconds=combined_actual['solver_CPU_seconds'],
    combined_main_whole_CPU_seconds=combined_actual['total_CPU_seconds_including_prior_preparation'],
    strict_general_induced_exclusion_registered=False,
    new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    expert_snapshot_preserved='2026-10-29 23:55 UTC',
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out=HERE/'SAMEFIBER_H65_PENDING_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),record_count=374),ensure_ascii=False))
