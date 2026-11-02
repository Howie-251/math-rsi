from pathlib import Path
from datetime import datetime, timezone
import copy
import json
import subprocess
import sys

R = Path(__file__).resolve().parents[2]
W = R / 'research-wiki'
S = 'research/ddp/two_successful_methods_20261101/'
D = S + 'retained_edge_transfer/mixed_copy_cycle_sigma_31/'
P = S + 'retained_edge_transfer/mixed_spread_omissions_u130_31/'
Q = S + 'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/'
B = 'MIXED_RULE_TERMINALS_AND_90_94_PENDING_20261101'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def read(path):
    return json.loads((R / path).read_text())

L = read('research-wiki/DDP_METHOD_LEDGER.json')
count_keys = ['record_count', 'validated_named_graph_examples', 'validated_named_parameter_pairs', 'complete_Lean_graph_instances']
assert tuple(L[k] for k in count_keys) == (420, 148, 39, 42)
ids = [
    'ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101',
    'ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101',
]
rows = [copy.deepcopy(next(x for x in L['rows'] if x['id'] == ident)['source_record']) for ident in ids]
batch = read(D + 'MODEL_BATCH_RESULT.json')
frac = read(D + 'FRACTIONAL_WITNESS_RESULT.json')
strata = read(D + 'LOOP_ROUTE_STRATA_RESULT.json')
binding = read(D + 'INTEG_BLOCK_LOCAL_BINDING_RESULT.json')
paper = read(D + 'INTEGER_BLOCK_BARRIER_INDEPENDENT_RESULT.json')
base = read(P + 'RESULT.json')
color = read(P + 'COLOR_RESULT.json')
terminal = read(P + 'COLOR_TERMINAL.json')
model = read(P + 'COLOR_MODEL.json')
reach = read(P + 'SPREAD_REACH_PREDICTION_RESULT.json')
assert batch['all_processes_terminal'] and batch['all_local_binding_included_total_CPU_seconds'] == 96.064628
assert frac['min_own_B2_R_count'] == 3 and len(frac['own_prediction_failed_targets']) == 960
assert frac['checks']['all10070_full_LP_coverage_numerator_at_least7']
assert all(strata['checks'].values()) and all(binding['checks'].values())
assert paper['mathematical_integer_completion_excluded_in_exact_scope']
assert (paper['global_attachment_lower_bound'], paper['six_helper_total_attachment_budget']) == (160, 156)
assert (base['n'], base['m'], base['unrestricted_eligible_pool_size'], base['restricted_npz_pool_size']) == (10070, 154385, 1750, 130)
assert base['omission_B_labels_by_A'] == [73, 138, 204, 269, 334]
assert terminal['exit_code'] == 0 and terminal['all_processes_terminal']
assert terminal['status'] == 'UNKNOWN_NO_INTEGER_COLORING_WITHIN_ONE_BUDGET'
assert not color['integer_pins_saved'] and not color['strict_infeasibility_proof_claimed']
assert reach['all_match'] and all(reach['checks'].values())

bar = rows[1]
p = bar['other_metrics']['mixed_five_holes_copycycles_sigma31_experiment']
p.update(
    status='ROOT_ACCEPTED_EXACT_FIXED_RULE_INTEGER_EXCLUSION_NUMERICAL_UNKNOWN_HISTORY_RETAINED',
    feasibility='EXACT_SAME_COLUMN_CURRENT_CYCLES_SIGMA_K6_INTEGER_COMPLETION_EXCLUDED',
    proof_of_feasibility_or_nonexistence_claimed=True,
    proof_scope='only exact five same-B-column fourth-copy omissions/current copycycles/current saved sigma/K6/all1750eligible pool/cap31',
    numerical_MILP=dict(status=paper['numerical_MILP_status'], attempts=1, CPU_seconds=95.395974, integer_incumbent=False, history_unchanged=True, session=65524, all_terminal=True, no_timer_restart=True),
    full_rational_LP_witness=dict(status='PASS_FULL_COVERAGE_AND_CAPACITY', assignment=frac['rational_assignment'], old_targets=10070, minimum_full_numerator_over7=7, own_B2_ge7_prediction='REFUTED', refuted_targets=960, minimum_own_B2=3, full_numerator_on_refuted_stratum=18, result=D+'FRACTIONAL_WITNESS_RESULT.json'),
    refined_five_route_strata=dict(status=strata['status'], all_predictions_match=True, actual_strata=strata['actual_strata'], result=D+'LOOP_ROUTE_STRATA_RESULT.json'),
    local_integer_block_binding=dict(status=binding['status'], actual_pool_vertices=1750, original_targets=960, A_support_rows=15, A_pair_checks=105, A_pair_absolute_checks=2625, new_old585_R2_Steiner_sigma_field_BFS_Lean_reruns=0, result=D+'INTEG_BLOCK_LOCAL_BINDING_RESULT.json'),
    independent_integer_exclusion=dict(status=paper['status'], blocks=8, minimum_attachments_per_block=20, total_minimum=160, K6_capacity=156, contradiction_gap=4, paper_only=True, no_helper_prefix_assumption=True, note=D+'INTEGER_BLOCK_BARRIER_INDEPENDENT_NOTE.md', result=D+'INTEGER_BLOCK_BARRIER_INDEPENDENT_RESULT.json', root_disposition=D+'ROOT_FIXED_RULE_DISPOSITION.md'),
    total_original_model_batch_CPU=96.064628, total_original_model_budget=120, all_processes_terminal=True,
    stop_exact_rule=True, different_holes_peers_helpers_general31_excluded=False,
    no_integer_pins_no10076_graph=True, new_graph_parameter_Lean_increments=[0,0,0],
    same_retained_edge_mechanism_not_new_framework=True,
)
p['solver_saved_handle'].update(state_scope='TERMINAL_NUMERICAL_UNKNOWN;rootseparate160gt156paperexclusion;do_not_poll_or_restart', resume_allowed=False)
p['actual_outcome_not_inferred_from_capacity'] = True
bar['other_metrics']['mixed_dispersed_five_holes_U130_own_cover_terminal'] = dict(
    status='ONE_OWN_COVER_COLOR_BATCH_TERMINAL_UNKNOWN_SUBMODEL_STOPPED',
    parent_experiment='mixed_five_holes_copycycles_sigma31_experiment', same_retained_edge_mechanism=True, independent_method_increment=0,
    why_rule_changed='same-column invariant eight-block repair demands160>156; disperse holes to different B coverage groups instead',
    omitted_B_by_A=[73,138,204,269,334], actual_G0_n=10070, actual_G0_m=154385,
    all_eligible_pool=1750, chosen_freed_U_pool=130, excluded_from_current_color_pool_F=1620,
    actual_degree_histogram=base['degree_histogram'], actual_cycles=1620, actual_sigma_matching=795,
    source_prep_root_inclusive_CPU=0.380353, source_prep_budget=15,
    reach_prediction=dict(status='ALL_PASS', nonabsolute_B_reach_five_groups=105, nonabsolute_B_reach_eight_groups=15, absolute_B_reach_one_group=10, result=P+'SPREAD_REACH_PREDICTION_RESULT.json'),
    color_model=dict(scope='six disjoint OWN closedR2 oldtarget covers from130freedU;eachpinassignedonce;eachhelper<=26pins', variables=781, binary_colors=780, rows=51659, nonzeros=403036, old_targets=10070, unique_masks=8711, retained_masks=8582, every_old_target_has_retained_subset_witness=True, minimum_mask_size=7, extra_variable='maximumload'),
    only_solver_batch=dict(status=terminal['status'], session=91896, exit_code=0, CPU_seconds=terminal['child_CPU_seconds'], budget=60, solver_limit=45, workers=1, integer_incumbent=False, runs=1, optimality_claimed=False, strict_infeasibility_claimed=False, all_terminal=True),
    subset_witness_file=P+'ALL_OLD_TARGET_MASK_WITNESSES.tsv', root_decision=P+'ROOT_RESULT_AND_NEXT_DECISION.md',
    next_action='stop this OWN-cover submodel;preserve exact masks;no timer_seed_hole_ladder',
    U_only_JOINT_K6_excluded=False, F_pin_repairs_excluded=False, general_cap31_excluded=False,
    new_graph_parameter_Lean_increments=[0,0,0], in86_98_finalC_scope=False,
)
bar['title'] = '同列mixed规则由160>156精确关闭；分散holes的U130 OWN-cover单批UNKNOWN并停止，均非一般31度排除'
bar['outcome_class'] = 'EXACT_SAME_COLUMN_INTEGER_RULE_CLOSED_SEPARATE_DISPERSED_OWN_COVER_UNKNOWN_NO_NEW_GRAPHS'
bar['scope'] += ' 当前收束：原同列MILP数值UNKNOWN历史不改，另由当前1750pool→960target绑定和独立八块160>156证明严格排exact同列/copycycles/currentσ/K6；新分散holes的U130六套OWNcover仅单批UNKNOWN，不排U-only JOINT/Frepair/general31。两试验为同机制改变连接规则，不拆成两method。'
bar['distance_text'] += ' 本轮旧ownB2≥7预言被960targets/min3反驳，但FULL有理LP全10070约束仍PASS，五refinedstrata全部实测相符；LP可行不等于整数图。1750pool→960targets及A15/105/2625局部绑定PASS后，独立八块各≥20pins给160>156，root接受exact同列规则严格关闭，原95.395974CPU UNKNOWN不追改，整个原model总96.064628/120全terminal。为改变跨块重用，holes改B=[73,138,204,269,334]；actualG0=10070/154385、pool1750但只用130freedU做六套OWNcover。reach预测105/15/10分别跨5/8/1组全PASS。COLOR唯一session91896 exit0 UNKNOWN49.845277/60、solver45无integerincumbent，781vars/51659rows/403036nnz；10070targets的8711unique masks约化到8582并保逐target subsetwitness，min7。该强OWN子模型已停，不排一般U-only JOINT或Frepair，0新图/Lean。'
bar['lesson_and_restart_condition'] += ' 最新终态覆盖此前65524恢复指令：同列exactscope现已有严格数学排除，65524/91896都terminal，不poll、不续timer/seed/hole梯子。理解改变从同列八块孤立到分散holes跨组互补，实际reach预测获支持，但唯一OWNcover限时无解点仍只UNKNOWN；下一次须有能同时实现的jointpin/freepeer规则，不能把fullLP或坏对数字当图。原uniformclique/Ktt固定scope保持STOP；otherholes/peers/helpers及一般31仍未排。本轮小参数工作均不在86/98 Cscope，0portfolio/Lean或新机制数。'

q8 = rows[0]
m = q8['other_metrics']
window = m['future_window84_98_public_gate_only']
window.update(status='FINITE_GATE_TWO_COMPLETED_ENDPOINTS_PLUS_TWO_NEW_ROOT_AUTHORIZED_UNACCEPTED_ENDPOINTS', production_authorized=True, active_queue=2, actual_graphs_or_queue=4,
    completed_selected_endpoints=[86,98], remaining_selected_not_dispatched=[], pending_root_acceptance_endpoints=[90,94], new_endpoints_accepted=0, new_review_scope_dispatched=False)
m['replication90_94_pending_batch'] = dict(
    status='ROOT_AUTHORIZED_NEW_TWO_ENDPOINT_BATCH_NOT_ROOT_ACCEPTED_NOT_COUNTED',
    source_actual_G1_n=346516, source_actual_G1_m=14204970, chain_from98_or_other_replicates=False,
    frozen_first_roles=4226, immutable_source_N=True,
    targets=[dict(Delta=90,D=3,n=380324,m=16942770,extra_G1_role_copies=8,total_multiplicity=9,best_located_public=380250,margin=74,math_accepted=False,concrete_Lean_complete=False),dict(Delta=94,D=3,n=397228,m=18311670,extra_G1_role_copies=12,total_multiplicity=13,best_located_public=397150,margin=78,math_accepted=False,concrete_Lean_complete=False)],
    budgets_CPU=dict(production=30,independent=60,new_Lean=300,workers_per_batch=1),
    A_B_freshC_dispatched=False, old_reviews_inherited=False, priority='UNKNOWN', global_record_claimed=False,
    old_baseline_gate_inherited=True, new_web_queries=0, new_validated_graph_instances_added=0,
    prediction=Q+'replication90_94_batch/PREDICTION_AND_SCOPE.md',
    source_publication_caveat='ifpublishedfilledsourceplusordinarycopyexistsremaininggains9/13;ifsamerulepublishedgain0',
)
q8['scope'] += ' 本轮root另派90/380324及94/397228，源仍实际G1/346516而非98链式；当前未数学验收计数，newscope A/B/C未派，旧86/98的PASS不继承。'
q8['distance_text'] += ' 已核有限window剩余分散端点90/380324/16942770(r8)与94/397228/18311670(r12)现由root明确派出，producer30CPU/fresh60/newLean300、各1worker，固定G1源一次batch；目前仅待验收候选，未加validated_instances/Lean计数。4225Δ公开已核保证分别380250/397150，条件margin74/78；sourcefill/同规则priorityUNKNOWN，不添网络查询或模板方法。'
q8['lesson_and_restart_condition'] += ' 当前90/94为此前门控同一规则的两个新scope，不以98扩张，不把授权/producer输出当fresh接受；须root明确接受后再增图、实际具体原目标终态后再增Lean，A/B/freshC也需明确新scope，绝不继承86/98旧审阅。'

de = [D+x for x in ['ROOT_FIXED_RULE_DISPOSITION.md','MODEL_BATCH_RESULT.json','SCIPY_MILP_RESULT.json','MILP_TERMINAL.json','FRACTIONAL_WITNESS_PREDICTION.md','FRACTIONAL_WITNESS_RESULT.json','LOOP_ROUTE_STRATA_PREDICTION.md','LOOP_ROUTE_STRATA_RESULT.json','INTEG_BLOCK_LOCAL_BINDING_PRED.md','INTEG_BLOCK_LOCAL_BINDING_RESULT.json','INTEG_BLOCK_LOCAL_BINDING_TERMINAL.json','INTEGER_BLOCK_BARRIER_PREDICTION.md','INTEGER_BLOCK_BARRIER_INDEPENDENT_NOTE.md','INTEGER_BLOCK_BARRIER_INDEPENDENT_RESULT.json','CURRENT_G0_POOL_ENVELOPE_BINDINGS.tsv','INTEGER_BLOCK_GROUP_BINDINGS.tsv']]
pe = [P+x for x in ['PREDICTION_AND_SCOPE.md','RESULT.json','TERMINAL.json','SPREAD_REACH_PREDICTION_RESULT.json','COLOR_RESULT.json','COLOR_TERMINAL.json','COLOR_MODEL.json','COLOR_HANDLE.json','ROOT_RESULT_AND_NEXT_DECISION.md','INDEPENDENT_COLORING_INTERFACE_NOTE.md','ALL_OLD_TARGET_MASK_WITNESSES.tsv','COVER_HYPERGRAPH.json','FREED_U130.tsv','OMITTED_COPY_CLASSES.tsv','PIN_POOL_ALL.tsv']]
qe = [Q+x for x in ['replication90_94_batch/PREDICTION_AND_SCOPE.md','multiplicity9_degree90/PREDICTION_AND_SCOPE.md','multiplicity13_degree94/PREDICTION_AND_SCOPE.md','replication90_94_batch/formalization/PRED.md']]
assert all((R/x).is_file() for x in de+pe+qe)
bar['evidence_paths'] = list(dict.fromkeys(bar['evidence_paths']+de+pe))
q8['evidence_paths'] = list(dict.fromkeys(q8['evidence_paths']+qe))
raw = W/f'updates/{B}_ROWS.json'
raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
calls = []
def call(*cmd):
    t = subprocess.run([str(x) for x in cmd],cwd=R,text=True,capture_output=True)
    calls.append(dict(command=[str(x) for x in cmd],returncode=t.returncode,stdout=t.stdout,stderr=t.stderr))
    assert t.returncode == 0,(cmd,t.stderr,t.stdout)
    return t.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L = read('research-wiki/DDP_METHOD_LEDGER.json')
assert tuple(L[k] for k in count_keys) == (420,148,39,42)
block = f'''<!-- {B} -->
# 当前：同列mixed规则严格关闭；分散holes OWN子模型UNKNOWN停止；90/94新批次未验收

同Goal ACTIVE，ledger420只复用[q8](experiments/{ids[0]}.md)与[barrier](experiments/{ids[1]}.md)，0新行/方法；148／39／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。86/98最终C实际完毕，轻量材料Ccomplete仍未ZIP，旧冻包不动。

同列mixed唯一数值MILP保持UNKNOWN95.395974CPU；FULL有理LP全10070约束PASS，ownB2≥7预言在960targets/min3被反驳，五refinedstrata实测全相符。后来1750pool→960targets和A15/105/2625字面绑定PASS，独立八块各需20pins给160>156，root接受exact同列holes/currentcycles/σ/K6严格排除。原model合计96.064628/120全terminal，不再poll65524或续timer；不是一般31度排除。

改变holes到B=[73,138,204,269,334]后G0=10070/154385、poolall1750/选130freedU；prep根级合计.380353/15。reach预测105/15/10pins分别跨5/8/1组全PASS。六套OWNcover唯一COLOR session91896 exit0 UNKNOWN49.845277/60，solver45无integerincumbent；781vars/51659rows/403036nnz，10070targets保逐target subsetwitness，8711unique→8582retained/min7。该强OWN子模型已停，不排U-only JOINT/Frepair/general31，不续timer/seed/holes梯子，0图/Lean，非86/98 Cscope。

root已另派原window的90/380324/16942770(r8)与94/397228/18311670(r12)，sourceactualG1/346516固定，非98链式。生产30CPU/fresh60/新Lean300各1worker，当前未root数学接受/未计图Lean，newscope A/B/C未派不继承旧PASS；已有4225Δ比较margin74/78及priorityUNKNOWN继承，不新网查。

'''
p0=W/'gap_map.md'
assert B not in p0.read_text()
p0.write_text(block+p0.read_text())
p0=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
p0.write_text(p0.read_text()+f'''\n\n## {now} 同一retained-edge机制两次有限试验终态与下一批90/94\n\n'''+block.split('\n\n',1)[1])
helper=R/'aris_repo/tools/research_wiki.py'
call(sys.executable,helper,'log',W,'Actualterminalsync: samecolumnmixednumericUNKNOWN95.395974retained;FULLrationalLPvalid_ownB2ge7REFUTED960min3_fiverefinedstrataPASS;current1750pool_to960targets_A15_105_2625bindingPASS_independent8blocks20pins160gt156ROOTacceptedexactcurrentcyclesSigmaK6exclusion_originalmodel96.064628of120allterminal0graphLean. DispersedBholes73_138_204_269_334G010070_154385pool1750freedU130prepRoot.380353of15_reach105five15eight10onePASS;soleCOLOR91896exit0UNKNOWN49.845277of60solver45noincumbent_781vars51659rows403036nnz_10070targetsubsetwitness8711to8582min7_OWNsubmodelSTOPnotUonlyJOINT_Frepair_general31_no_timer_seed_holeladder. SameoneMechanismnot2method. Rootnew90_380324_16942770r8and94_397228_18311670r12fromactualG1346516not98chain_production30fresh60Lean300each1worker_UNACCEPTED0count_newAB_Cnotdispatched_oldPASSnotinherited. Ledger420twoexistingrows148_39Lean42stage44_36outside42_35known43main103_3global0unchanged_0newqueries_math_graph_BFS_Lean_solver_paidreview_rootowned_orfrozenwrites.')
call(sys.executable,helper,'rebuild_index',W)
call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_MINIMAL_EXISTING_WIKI_TWO_RULE_TERMINALS_AND_90_94_UNACCEPTED_BATCH',updated_UTC=now,
    ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=148,legal_parameter_pairs=39,complete_formula_Lean=42,stage_graphs=44,stage_pairs=36,outside_graphs=42,outside_pairs=35,known_publicly_dominated=43,main103_3=True,global_records=0,
    same_column_numeric_UNKNOWN_retained_CPU=95.395974,same_column_exact_fixed_rule_paper_excluded=True,pin_lower_bound=160,pin_budget=156,model_all_terminal_total_CPU=96.064628,original_model_budget=120,
    fractional_FULL_LP_valid=True,own_B2_ge7_prediction_refuted_targets=960,minimum_own_B2=3,five_refined_strata_PASS=True,local_pool_target_A_binding_PASS=[1750,960,15,105,2625],
    dispersed_model_status=terminal['status'],dispersed_session91896_terminal=True,dispersed_CPU=terminal['child_CPU_seconds'],dispersed_total_budget=60,dispersed_integer_incumbent=False,dispersed_scope='six disjoint OWN covers only;not general JOINT_Frepair_cap31',no_timer_seed_hole_ladder=True,
    new90_94_batch='ROOT_AUTHORIZED_NOT_ROOT_ACCEPTED_OR_COUNTED',new90_94_review_scope='A_B_freshC_NOT_DISPATCHED_NO_INHERITANCE',new_graph_Lean_framework_increments=[0,0,0],
    evidence_paths_checked=len(de)+len(pe)+len(qe),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_graph_BFS_Lean_solver_web_paid_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
