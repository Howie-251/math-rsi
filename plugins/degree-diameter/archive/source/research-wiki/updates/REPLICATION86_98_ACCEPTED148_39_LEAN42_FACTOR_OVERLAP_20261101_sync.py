from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';Q=S+'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/';F=Q+'replication86_98_batch/';I=Q+'multiplicity5_17_independent_acceptance/';T=S+'retained_edge_transfer/polarity_product2_8_helper_barrier/'
B='REPLICATION86_98_ACCEPTED148_39_LEAN42_FACTOR_OVERLAP_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
ids=['ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101','ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
formal=json.loads((R/F/'formalization/FINAL.json').read_text());indep=json.loads((R/I/'TERMINAL.json').read_text());experiment=json.loads((R/T/'FACTOR_RADIUS2_SUPPORT_EXPERIMENT_RESULT.json').read_text());ext=json.loads((R/T/'FACTOR_RADIUS2_SUPPORT_EXPERIMENT_TERMINAL.json').read_text());paper=json.loads((R/T/'FACTOR_RADIUS2_OVERLAP_INDEPENDENT_RESULT.json').read_text())
assert formal['status']=='BOTH_ORIGINAL_D86_D98_KERNEL_AUDIT_EXTERNAL_ROLE_BINDING_PASS' and formal['new_module_count']==8 and formal['failed_attempts']==0
assert formal['typed_external_binding_rows']==84520 and indep['status']=='PASS_BOTH_INDEPENDENT_G1_TARGETS' and indep['actual_new_BFS_roots']==136
assert experiment['status']=='ALL_PREDECLARED_SUPPORT_AND_COMPLETION_PREDICTIONS_PASS' and all(experiment['checks'].values()) and ext['subsets_examined']==32 and ext['pairs_examined']==10
assert paper['status']=='SUPPORTED_PAPER_ONLY_MATRIX_SUPPORT_INTERSECTION_AND_UNION_BOUND'
r=rows[0];m=r['other_metrics'];e=[];case_summaries=[]
for degree,n,edges,sub,public,margin in [(86,363420,15573870,'multiplicity5_degree86/',363350,70),(98,414132,19680570,'multiplicity17_degree98/',414050,82)]:
    d=Q+sub;release=json.loads((R/d/'ROOT_GRAPH_RELEASE.json').read_text());z=json.loads((R/d/'independent_acceptance/RESULT.json').read_text());f=json.loads((R/d/'formalization/FINAL.json').read_text());binding=json.loads((R/d/'formalization/EXTERNAL_INPUT_BINDING.json').read_text())
    assert release['status']=='ROOT_ACCEPTED_COMPLETE_MATH_CONCRETE_LEAN_NEW_REVIEWS_PENDING_PRIORITY_UNKNOWN' and release['n']==n
    assert z['status']=='PASS' and z['n']==n and z['hist_mismatches']==0 and z['actual_lastblock_new_BFS_roots']==68 and z['old_root_BFS']==0
    assert f['no_user_certificate_premises'] and f['genuine_Walk_D3'] and f['not_D2'] and f['label']=='Fin'+str(n) and set(f['axioms'])=={'propext','Classical.choice','Quot.sound'}
    assert binding['row_count']==z['new_roles_bound']
    g=dict(Delta=degree,D=3,n=n,m=edges,actual_diameter=3,mathematically_validated_complete_graph=True,complete_Lean_graph_instance=True,
        known_nonrecord=False,known_publicly_dominated=False,latest_global_record_confirmed=False,confirmed_publictable_improvement=False,best_located_public_lower_bound=public,bounded_gain=margin,
        public_comparison_status='EXCEEDS_CHECKED4225Delta_GUARANTEE_PRIORITY_GLOBAL_UNKNOWN',graph_path=d+f'graph_d{degree}_D3_n{n}.edges',degree_histogram=z['degree_histogram'],
        source_n=346516,source_m=14204970,source_is_actual_G1_not83=True,source_all14204970_edges_retained=True,additional_role_blocks=z['additional_blocks'],total_multiplicity=z['total_multiplicity'],new_roles_complete_N_bound=z['new_roles_bound'],
        actual_new_BFS_roots=68,unmeasured_new_roots=z['unmeasured_new_roots'],old_BFS_roots=0,actual_lastblock_hist_distributions=z['actual_hist_distributions'],
        allpair_every_prefix_old_G1_interior_Walk_proof=True,no_sample_orbit_extrapolation=True,complete_concrete_Lean_status=f['status'],concrete_original_target=f['target'],formal_final_receipt=d+'formalization/FINAL.json',formal_label=f['label'],formal_standard_axioms=f['axioms'],formal_user_certificate_premises=False,
        formal_ASCII_parser_or_Audit_eval_all_rows_claimed=False,external_A='CELL655_ACTUAL_EXPLICIT_NEW_SCOPE_DISPATCH_PENDING_NOT_PASS',external_A_thread='e4b6c102-1c55-4739-82e4-d281acc2e835',external_B='NOT_DISPATCHED',external_fresh_C='NOT_DISPATCHED',old_three_review_or_frozen_packet_inherited=False,
        independent_result=d+'independent_acceptance/RESULT.json',ROOT_release=d+'ROOT_GRAPH_RELEASE.json',public_priority='UNKNOWN')
    m['validated_graph_instances'].append(g);case_summaries.append(dict(Delta=degree,n=n,m=edges,fullN_newrole_bindings=z['new_roles_bound'],actual_BFS_roots=68,unmeasured_new_roots=z['unmeasured_new_roots'],hist=z['actual_hist_distributions'],public_guarantee=public,bounded_gain=margin,FINAL=d+'formalization/FINAL.json',ROOT_release=d+'ROOT_GRAPH_RELEASE.json'))
    e += [d+x for x in ['ROOT_GRAPH_RELEASE.json','PARAMETERS.json','RESULT.json','TERMINAL.json','PROOF.md',f'graph_d{degree}_D3_n{n}.edges','independent_acceptance/NOTE.md','independent_acceptance/RESULT.json','independent_acceptance/TERMINAL.json','independent_acceptance/ALL_NEW_ROLE_BINDINGS.tsv','independent_acceptance/ALL_68_LAST_BLOCK_NEW_ROOT_BFS.csv','independent_acceptance/PRESELECTED_LAST_BLOCK_ROOTS.json','independent_acceptance/NON_D2_ACTUAL_LAST_HUB_WITNESS.json','formalization/FINAL.json','formalization/EXTERNAL_INPUT_BINDING.json']]
    e += [F+f'formalization/Q8DiagonalFill{degree}Audit_attempt001.log',f'formal/DegreeDiameter/Portfolio/Q8DiagonalFill{degree}Definitions.lean',f'formal/DegreeDiameter/Portfolio/Q8DiagonalFill{degree}Inputs.lean',f'formal/DegreeDiameter/Portfolio/Q8DiagonalFill{degree}Exact.lean',f'formal/Q8DiagonalFill{degree}Audit.lean']
m['new_named_complete_graphs']=7;m['new_Lean_instances']=7;m['accepted_q8_terminal_graphs']=[327744,342290,346515,346516,350742,363420,414132]
m['all_row_graph_instances_complete_Lean']=True;m['all_row_original_A_B_distinctfreshC_complete']=False
m['completed_Lean_and_A_B_C_scope']='all7q8rowinstancesactualkernelcomplete;old5finalreviewscomplete;new86_98A655pending_B_Cnotdispatched_notinoldthreefrozenpacket'
m['replication86_98_actual_batch']=dict(status='ROOT_ACCEPTED_BOTH_COMPLETE_LITERAL_MATH_KERNEL_AUDIT_BINDING_NEW_REVIEWS_PENDING',cases=case_summaries,
    source='actualG1_346516_never83graph',parent_literal_parse_once=True,candidate_literal_stream_each_once=True,new_roles_bound=84520,actual_lastblock_BFS_per_case=68,actual_BFS_total=136,old_BFS=0,
    unmeasured_new_roots=[16836,67548],allpair_every_prefix_source_interior_proof=True,
    producer_total_CPU=6.013320505,producer_CPU_budget=30,independent_total_CPU=indep['total_CPU_seconds'],independent_CPU_budget=60,
    concrete_Lean_total_CPU=formal['CPU_seconds'],concrete_Lean_CPU_budget=300,new_modules=8,all_first_PASS=True,failed_attempts=0,new_finite_geometry_or_old_module_recompile=0,
    A=dict(status='ACTUAL_ROOT_DISPATCH_CELL655_PENDING_RESULT',thread='e4b6c102-1c55-4739-82e4-d281acc2e835',scope='onlynewexact86and98originaltuples',actual_shared_calls=1,request=S+'reviews/REPLICATION86_98_A_REQUEST.json',request_file_is_not_returned_verdict=True),
    B='NOT_DISPATCHED',distinctfreshC='NOT_DISPATCHED',old_three_PASS_or_frozen_packet_inherited=False,priority='UNKNOWN',not_dispatched=[90,94])
m['future_window84_98_public_gate_only'].update(status='FINITE_GATE_COMPLETE_TWO_SEPARATELY_AUTHORIZED_ENDPOINTS_NOW_ACCEPTED_OTHERS_NOT_DISPATCHED',actual_graphs_or_queue=2,active_queue=0,completed_selected_endpoints=[86,98],remaining_selected_not_dispatched=[90,94],separate_root_production_authorization=True)
r['title']='q8同一G1规则：86/363420与98/414132数学/具体Lean新接受，A655在途，旧三图包不变'
r['outcome_class']='SEVEN_Q8_ROW_LITERAL_KERNEL_COMPLETE_NEW86_98_EXPLICIT_REVIEWS_PENDING'
r['scope']+=' 最新只新增实际86与98两端点，sharedG1source346516/14204970，不是83链源；16904/67616新roles完整绑定，68lastblockroots各实测、其余16836/67548与old0BFS，完整G1内点Walk/prefix证明覆盖未测点对。新A655明确两tuple在途，B/freshC未派，旧三图审阅/146快照ZIP不覆盖新图；90/94未派。'
r['distance_text']+=' 两新完整图86/363420/15573870与98/414132/19680570已ROOTrelease、fresh独验、具体原目标/FinalClaim/final_claim/Finlabel/std3/no用户前提及Audit外部84520rows全PASS。producer6.013320505CPU、独验9.484730169CPU、8新Lean首PASS19.612733651CPU/300，0旧source/finite重编。每case68lastblockroots全部逐预测match，不冒全根BFS；公开仅对4225Δ保证+70/+82，priorityUNKNOWN。新A655在途/新B及freshC未派，不继承旧3图或冻结包。'
r['lesson_and_restart_condition']+=' 84..98有限门实际改变参数选择，只授权两个分散端点86/98，均由同一G1first-role冻结完整N复制成功；增multiplicity后每root新增B2恰同role copies，others入B3，136实测hist支持预测。16904/67616全部新role绑定与源内点Walk补未测范围，既有role唯一性直接重用使8module零失败无新finite。下一步只完成这两新scope审阅，90/94仍未派；旧三图冻结包永久146/37/40快照不变。'
e += [I+x for x in ['STRUCTURE_PROOF.md','RESULT.json','TERMINAL.json','PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv']]+[F+'COMPLETION.md',F+'RESULT.json',F+'TERMINAL.json',F+'formalization/FINAL.json',F+'formalization/EXTERNAL_INPUT_BINDING.json',S+'reviews/REPLICATION86_98_A_REQUEST.json']
assert all((R/x).is_file()for x in e);r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+e))
bar=rows[1];m=bar['other_metrics'];m['factor_radius2_overlap_paper_and_literal15_experiment']=dict(status='INDEPENDENT_PAPER_SUPPORTED_AND_ROOT_LITERAL15_ALL_PREDICTIONS_PASS',
    matrix='M^3=2qM+J;M^4=2qM^2+(q+1)J',support='q(q+1)',pair_intersection='q+1',union_upper='(q+1)((q-1)t+1)',
    q8_t8_union_at_most=513,q8_nonabsolute_targets=520,q8_missed_at_least=7,requires_at_least_one_external_unowned_class=True,not_seven_classes=True,not_cap31_exclusion=True,not_everyhelper9pins=True,
    paper_computational_runs=0,literal_factor_vertices=15,literal_subsets_checked=32,literal_pair_checks=10,literal_all_predictions_PASS=True,
    exact_required_external_classes_by_distinct_own_count=[5,4,1,0,0,0],required_class_completion_exact_and_necessary=True,
    root_experiment_CPU_reported=0.0,CPU_below_timer_resolution_not_zero_cost=True,CPU_budget=2,old225_230_not_rerun=True,q8_finite_table_examined=False,
    portfolio_graph_parameter_Lean_increment=[0,0,0],in_prior_three_C_or_new86_98_review_scope=False,
    paper=T+'FACTOR_RADIUS2_OVERLAP_INDEPENDENT_NOTE.md',experiment=T+'FACTOR_RADIUS2_SUPPORT_EXPERIMENT_RESULT.json')
m['clique_helper_free_target_prediction']=dict(status='PREDICTION_SAVED_INDEPENDENT_PAPER_ATTACK_IN_PROGRESS_NOT_YET_SUPPORTED',
    prediction=T+'CLIQUE_HELPER_FREE_TARGET_PREDICTION.md',scope='fixedproduct2x8_mandatoryfamily_cliquehelperrestrictedmodel',PASS_claimed=False,new_graphs=0,new_Lean=0,new_search=0)
bar['distance_text']+=' 新factor-overlap paper已独立SUPPORTED：M³/4、abs支持q(q+1)/pair交q+1与union界成立，q8/t8至多513/520漏至少7个点，至少1unownedclass须外援，非7类/非31排除/非每helper9pins。root另literal15仅32subsets/10pairs一次全PASS，外援类数t0..5=5/4/1/0/0/0，0.0CPU读数低于timer分辨率非零成本，没重跑225/230/field/BFS/Lean。新clique-helper-free-target只是预存预测、gq纸面攻击在途，不能PASS。'
bar['lesson_and_restart_condition']+=' 支持数与交数说明8类pin在q8仍有路线重复并漏点，下一代cap31规则需显式存每helper的未覆盖target与唯一owner externalclass，不能把heavy8row当完成；literalq2全32子集的外援类集合支持此接口但不外推q8表。新clique-helper模型攻击仍待结果，不提前排31/启动solver；86/98是另同G1扩参，0旁支图计数。'
te=[T+x for x in ['FACTOR_RADIUS2_OVERLAP_PREDICTION.md','FACTOR_RADIUS2_OVERLAP_INDEPENDENT_NOTE.md','FACTOR_RADIUS2_OVERLAP_INDEPENDENT_RESULT.json','FACTOR_RADIUS2_OVERLAP_INDEPENDENT_TERMINAL.json','FACTOR_RADIUS2_SUPPORT_EXPERIMENT_RESULT.json','FACTOR_RADIUS2_SUPPORT_EXPERIMENT_TERMINAL.json','factor_radius2_support_once.py','CLIQUE_HELPER_FREE_TARGET_PREDICTION.md']]
assert all((R/x).is_file()for x in te);bar['evidence_paths']=list(dict.fromkeys(bar['evidence_paths']+te))
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
block=f'''<!-- {B} -->
# 当前：86/363420与98/414132数学及具体Lean已接受，148／39／Lean42；新A655在途

同Goal ACTIVE，ledger420复用[现q8机制](experiments/{ids[0]}.md)和[现barrier](experiments/{ids[1]}.md)两节点/0新行；148合法／39参数、stage44／36／Lean42、outside42／35，known43/main103_3/global0不变。两新图共同sourceactualG1/346516而非83，84520完整newrole N绑定；每case68lastblockroots实测全部histmatch，未测16836/67548、old0BFS，由完整源内点Walk/prefix证明覆盖。producer6.013320505/30、fresh9.484730169/60、8newLean首PASS19.612733651/300含binding，无旧source/finite重编。

公开仅对4225Δ保证多70/82，priorityUNKNOWN。A655同e4线程明确两新tuplescope一次已派在途，B/freshC未派，不继承旧三图PASS或146/37/40冻结包；90/94仍未派。factor-overlap纸面SUPPORTED与rootliteral15的32subset/10pair全PASS另记0图/Lean；q8八类pin仍漏≥7点，需≥1外援类，非31排除。新clique-helper-free-target预测正独立纸面攻击，尚未PASS，不重复研究或验证。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 同G1两分散端点实际接受＋具体Lean完成；factor支持与重叠预测分别实测/纸面归档

现Wiki只复用[q8机制](experiments/{ids[0]}.md)、[局部barrier](experiments/{ids[1]}.md)，ledger420/0新方法行。root RELEASE正式接受86/363420/15573870和98/414132/19680570，新增2合法图/2参数/2具体Lean，使148／39／Lean42、stage44／36、outside42／35，known43/main103_3/global0不变。它们是同规则两个端点，不新增构造framework，未把90/94或其余window caps算作已生成。

两case共同sourceactualG1/346516的14204970边全部逐条保留，producer只source1stream；fresh共同parent1stream/candidate各1stream，独立actual4226模板，每actualnewedge先check模板membership，再fullactualdegree+simple推出完整N相等，总16904+67616=84520rows。两case各lastblock预选65diag+2off+hub共68root，全部事前hist逐根支持；未测16836/67548和old0BFS，没有全根或对称性外推。共同STRUCTURE_PROOF给oldG1内点端点替换/same-role两步/different-role三步及每prefix全对保证。actualhub见证363419—342225—5265—342290及414131—342225—5265—342290都是距离3。共同producer6.013320505CPU/30、fresh9.484730169CPU/60；共享parent成本不每case重复计。

8newLean模块全首PASS/19.612733651CPU/300含binding，两个实际原目标d86_363420、d98_414132及FinalClaim/final_claim、Fin363420/Fin414132、独立Audit逐type/body/std3/no用户证书前提/真WalkD3/nonD2全闭合，0新finite/旧source或module重编。import83只复用关于G1的role唯一性，sourcegraph不是350742。外部84520label绑定与literal N证据分列，不冒LeanASCIIparser或Audit#eval全rows。新A655沿e4b6c102线程只明确新两tuplescope一次actualdispatch，request文件不是returnedverdict；B/freshC未派。旧三图A/B/C不继承，新两图不在146/37/40immutable专家包内，旧包不动。

公开比较仍只对已核4225Δ：86保证363350多70、98保证414050多82，exactpriority/globalUNKNOWN；若filledH+普通copy已公开剩5/17，若samehubrule公开归0。90/94仍未派，下一步只收两新scope审阅。

另存实际新理解：factor-overlap纸面独立支持真实GQ M³=2qM+J、M⁴与offdiagM²≤1，绝对二步nonabs支持q(q+1)/交q+1，union≤(q+1)((q−1)t+1)。q8/t8至多513/520漏≥7个点，但不是7个类，至少1个unownedbasedclass须外援，非cap31排除/非人人9pins。root literal15独立重建只作5supports、10pairs、32subsets新支持实验，所有预测与必要/充分外援类全PASS，t0..5需5/4/1/0/0/0类；没有重跑225/230、q8表/field/BFS/Lean。观测CPU0.0低于timer分辨率不当零真实成本，0图/参数/Lean增量且不在旧3图或新2图外审scope。新CLIQUE_HELPER_FREE_TARGET预测已保存、gq独立paperattack在途，仅PRED非PASS，本agent未重复攻击/solver。根状态与冻结包未改。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Actualnew86_363420_15573870and98_414132_19680570ROOTreleasedmathfreshkernelPASS/sourceactualG1not83/84520fullNrows/only68lastblockrootseachallhistmatch/unmeasured16836_67548old0BFS/allpairprefixsourceinteriors;producer6.013320505CPU/fresh9.484730169CPU/new8LeanfirstPASS19.612733651CPU0finite_oldsource_recompile. Ledger420twoexistingrows148_39Lean42stage44_36/outside42_35known43main103_3global0. A655actualdispatchtwonewtuplepending/BfreshCnotdispatched/nooldthreePASSorZIPinherit/90_94notdispatched. FactoroverlappaperSUPPORTED/rootliteral15_32subsets10pairsallPASS/time0.0belowresolutionnotzerocost/0graphLean;cliquefreepredictionattackpendingNOTPASS.0reruns_rootedits_frozenpacketwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_NEW86_98_ACCEPTED148_39_LEAN42_AND_SEPARATE_FACTOR_OVERLAP_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=148,legal_parameter_pairs=39,stage_graphs=44,stage_pairs=36,complete_formula_Lean=42,outside_pending_graphs=42,outside_pending_pairs=35,known43_main103_3_global0=True,new_graphs=2,new_parameters=2,new_Lean=2,new_frameworks=0,
    accepted_cases=case_summaries,producer_CPU=6.013320505,fresh_CPU=indep['total_CPU_seconds'],formal8_CPU=formal['CPU_seconds'],new_module_failed_attempts=0,total_newrole_bindings=84520,actual_new_BFS_roots=136,old_BFS_roots=0,A655='ACTUAL_DISPATCH_PENDING_NEW_TWO_SCOPE',B_freshC='NOT_DISPATCHED',old_packet_146_37_40_untouched=True,
    factor_support32subsets10pairs_actualPASS=True,factor_overlap_paperSUPPORTED=True,factor_CPU_belowresolution_notzerocost=True,factor_graph_or_Lean_increment=0,clique_helper_free_target='PRED_ONLY_INDEPENDENT_ATTACK_IN_PROGRESS_NOT_PASS',not_dispatched=[90,94],
    evidence_paths_checked=len(e)+len(te),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
