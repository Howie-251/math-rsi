"""Reconcile the completed support and representation gates on existing rows."""
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
    return [str(p.relative_to(ROOT)) for p in sorted((HERE/folder).iterdir())
        if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'}]


support=load('f5_induced_support_closure/RESULT.json')
projection=load('f5_induced_support_closure/PROJECTION_RESULT.json')
density=load('f5_induced_support_closure/DENSITY_RESULT.json')
shared=load('f5_induced_shared_middle_routes/RESULT.json')
compression=load('d14_K2_exact_signature_compression/RESULT.json')
assert support['complete'] is True and support['prediction_H']=='REFUTED'
assert support['closed_supports_visited']==24575 and support['largest_proper_size']==19
assert support['distinct_Horn_rules']==129 and support['original_rules']==258
assert len(projection['cases'])==6
assert sum(x['size']==16 and not x['passes_necessary_projection'] for x in projection['cases'])==3
assert sum(x['size']==19 and x['passes_necessary_projection'] for x in projection['cases'])==3
assert density['status']=='ALL_THREE_19_SUPPORTS_HAVE_DENSITY_MATCHING4'
assert all(len(c['matching4'])==4 and c['fiber_count_upper_bound']==1875 for c in density['cases'])
assert shared['pairs_checked']==shared['pairs_with_exact_expected_routes']==20
assert shared['all_twenty_predictions_supported'] is True
assert compression['status']=='COMPLETE_EXACT_EQUALITY_COMPRESSION'
assert (compression['port_groups'],compression['target_row_classes'])==(3589,94069)
assert compression['source_graph_reads']==compression['BFS_runs']==compression['solver_calls']==0
ledger=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert ledger['record_count']==len(ledger['rows'])==374
ids=['ddp-f5-literal3750-induced-retention-max16-d3-20261029',
     'ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029']
old={r['id']:r for r in ledger['rows']}
rows={key:copy.deepcopy(old[key]['source_record']) for key in ids}

f5=rows[ids[0]]
variants={v['label']:v for v in f5['variants']}
additions=[
 dict(label='complete30_fiber_Horn_support_closure_prediction_H_refuted_20261029',
      status=support['status'],original_ordered_rules=258,distinct_reverse_reduced_rules=129,
      complete_NextClosure_closed_sets=24575,maximum_proper_support=19,
      prediction='Everyproperclosed support has<=15fibers',prediction_verdict='REFUTED',
      proper_supports_size_at_least16=dict(size16=3,size19=3),
      no_other_proper_sizes_at_least16=True,all_six_direct_original258_checks=True,
      source_graph_reads=0,graph_BFS=0,SAT_calls=0,new_graphs=0,
      compile_and_gate_CPU_seconds=support['aggregate_CPU_seconds'],
      gate_plus_extraction_CPU_seconds=support['total_check_plus_postprocessing_CPU_seconds']),
 dict(label='proper_support_projection_and_partial_fiber_density_full30_necessity_20261029',
      status='ALL_PROPER_SUPPORTS_EXCLUDED_FOR_ORDER_AT_LEAST1921',
      size16_supports=3,size16_controller_diameter=4,size16_projection_excluded=True,
      size19_supports=3,size19_controller_diameter=3,
      size19_projection_alone_excluded=False,
      density_lemma='Foranexternalu-vwithamissingcontrolneighbor,|S_u|+|S_v|<=125.',
      each_size19_bad_external_matching=4,
      size19_total_order_bound=1875,other_allowed_proper_supports_at_most15=True,
      conclusion='AnyinducedD3candidateoforder>=1921musthaveall30fibersnonempty.',
      all30_fibers_nonempty_necessary=True,whole_fibers_retained_necessary=False,
      arbitrary_full_support_partial_retention_excluded=False,
      density_local_independent_static_review='PASS_PARENT_REPORTED',
      combined_external_review_status='PENDING',
      projection_CPU_seconds=projection['CPU_seconds'],density_witness_CPU_seconds=density['CPU_seconds'],
      source_BFS=0,new_graphs=0,main_solver_calls=0,
      whole_fiber_correction='Trianglecontrol edge has an extra2stepplane; union29+16m<=109form<=5. Externalcase<=105.',
      small30variable_blocking_RAW_UNSAT='Counterexampleattackonly; not the strictproof.'),
 dict(label='external_five_short_routes_share_middle_point_new_retention_clauses_20261029',
      status=shared['status'],literal_w=0,literal_L=[1,2,3,4],
      literal_Y=[2500,2501,2502,2503,2504],literal_Z=[2250,2255,2260,2265,2270],
      literal_pairs_checked=20,all20_exactly5routes=True,all5_routes_share_w=True,
      source_short_path_cache_reads=1,source_edge_reads=0,BFS_calls=0,SAT_calls=0,new_graphs=0,
      old_unique_controller_distance3_template_applies=False,
      clauses=['keep[w] OR NOT ORkeep[L] OR NOT ORkeep[Y]',
               'ORkeep[Z] OR NOT ORkeep[L] OR NOT ORkeep[Y]'],
      exact_scope='Externalcontrollerdart,anotherportq!=p,Lomitsw;thesefivearealllength<=3pathsfortheCartesianendpointclass.',
      local_independent_static_review='PASS_PARENT_REPORTED',combined_external_review_status='PENDING',
      planned_general_groups=22500,planned_closure_clauses=45000,
      necessary_exact_OR4_flags=15000,OR4_binding_clauses=75000,
      total_extra_clauses_with_OR4_bindings=120000,
      previous_OR5_flags_reused=True,new_solver_run_recorded=False,
      CPU_seconds=shared['CPU_seconds'])]
variants.update({v['label']:v for v in additions})
f5['variants']=list(variants.values())
f5['scope']+='；新support层完整枚举反驳H，但projection+external密度证明已排所有proper支持的n≥1921候选，须全部30fiber非空（不要求整fiber保留）。另新增外边五路共享中点闭包及20对literal检验。'
f5['failure_or_result']+='；24575个闭support中maxproper19，3个16/3个19；H≤15被推翻。16支持投影D4，19支持各有4个badexternal匹配使N≤1875，故所有纪录候选需full30非空。20/20局部点对均恰5路共用w，新的两条必要闭包不属于旧unique控制D3模板；尚未据生成准备登记新RUN。'
f5['other_metrics'].update(
    support_prediction_H='REFUTED',support_closed_sets=24575,support_maximum_proper=19,
    large_proper_size16_count=3,large_proper_size19_count=3,
    proper_supports_excluded_for_order1921=True,
    all30_fibers_nonempty_necessary=True,whole_fibers_retained_necessary=False,
    shared_middle_literal_pairs=20,shared_middle_all20_predictions_supported=True,
    shared_middle_all5routes_share_w=True,shared_middle_new_clauses=45000,
    shared_middle_new_OR4_flags=15000,
    newest_support_density_shared_paper_external_review='PENDING',
    enhanced_retention_solver_run_recorded=False)
f5['lesson_and_restart_condition']='SupportH最初预测被完整枚举反驳，不能沿用为定理；projection对size19又不够，external缺邻居的密度上界才补足proper支持排除。故下一模型可无损要求每个fiber至少一点，不能强制整fiber。20对literal多路反例揭示共同中点是旧unique控制词未直接编码的结构，支持增加精确OR绑定的shared-middle规则；不能只把旧UNKNOWN续时称增强。本地新增结论仍等待本轮外审，未据派发登记主求解已运行。'
f5['unclosed_gap']='一般full30非空、n≥1921/max16/D3的partial-fiber诱导图仍开放。旧必要retention单次UNKNOWN保留且本批不续；新shared-middle/fullsupport规则准备增强表示，待实际模型/handle/RESULT。新support/density/shared推导只有本地静态PASS，不冒已完成整轮外审。'

k2=rows[ids[1]]
variants={v['label']:v for v in k2['variants']}
comp=dict(label='exact_joint_R3_R4_port_and_target_pair_equality_compression_20261029',
    status=compression['status'],original_ports=3685,exact_port_classes=3589,
    duplicate_ports_removed=96,port_reduction_percent=2.61,
    original_targets=94186,exact_target_rowpair_classes=94069,
    duplicate_target_rows_removed=117,target_reduction_percent=0.124,
    original_twohelper_fullrows=188372,equivalent_twohelper_fullrows=188138,
    maximum_group_size=2,group_capacity1_count=3480,group_capacity2_count=109,
    grouped_selector_variables=7178,
    exact_equality_only=True,containment_or_dominance_not_run=True,
    reconstruction='Samecoverageportclass usedbybothhelpers:onespare2portortwodistinctspare1ports;groupcapacitymin(2,sumspare).',
    CPU_seconds_including_compile_and_order_binding=compression['aggregate_CPU_seconds_including_order_binding'],
    source_reads=0,BFS_runs=0,SAT_calls=0,new_CNF_generated=False,new_graphs=0,
    decision='STOP_NO_MATERIAL_ROW_COMPRESSION_NO_NEW_SOLVER',
    K2_family_excluded=False)
variants[comp['label']]=comp
k2['variants']=list(variants.values())
k2['failure_or_result']+='；新增精确双signature等价压缩3685ports→3589、94186targetpairs→94069，仅2.61%/0.124%，含编译及行序绑定1.587400502CPU，0图读/BFS/SAT/CNF；缩减不足按预定规则停止，不重启旧K2求解。'
k2['other_metrics'].update(
    exact_joint_signature_compression_completed=True,
    exact_port_classes=3589,exact_target_rowpair_classes=94069,
    exact_port_duplicates_removed=96,exact_target_duplicates_removed=117,
    compression_CPU_seconds=1.587400502,
    compression_new_solver_calls=0,compression_decision='STOP_INSUFFICIENT_REDUCTION',
    fixed_K2_family_excluded=False)
k2['lesson_and_restart_condition']+='；完整双signature相等类几乎未减少targetrows，表示压缩未达到值得新SAT的效果；这不是可行性排除，也不据此扩成全dominance或换helper数。'
k2['unclosed_gap']='AllfreeK2 existence仍未决；原同batch最终UNKNOWN已停。新精确等价表示门只删117targetpairrows、没有实质压缩，停止此表示门且不生成/启动新CNF；不排一般K2。'

report='''# 支持预测、密度修正、共享中点与K2表示门

支持H“proper闭支持≤15”被完整NextClosure反驳：258词去反向129Horn规则有24575个闭支持，maxproper19；≥16的proper仅3个16和3个19。3个16投影D4，3个19投影D3仍存活，不能凭projection强制fullsupport。新external缺邻居密度|S_u|+|S_v|≤125与每个19支持中的4条互不相交badexternal边给N≤1875，补足所有proper排除；故n≥1921纪录候选必须30fiber均非空，但绝不强制wholefiber保留。密度引理本地静态PASS，整轮外审pending。wholefiber证明已补triangle额外2stepplane，界29+16m≤109；不移用external禁区到triangle。

新共享中点局部规则20/20对均恰5条≤3路线且全过同w。保留端点迫keep[w]及Z中至少一点，给两条OR必要clauses。该adjacent控制pair不属旧unique控制D3模板。通用22500组/45000closure还需15000exactOR4绑定、75000绑定clauses；这里只保存规则与literal检验，未把增强模型准备冒RUN。小30变量blocking的rawUNSAT仅反例攻击，不替代严格密度/枚举依据。

D14精确双signature equality完成：3685→3589ports，94186→94069targetpairrows，合并96/117，仅2.61%/0.124%，总1.587400502CPU。0source读/BFS/SAT/新CNF。完整两root系统仍188138rows，压缩不足停止，不排K2可行性。

两个existing聚合行附变体，ledger374（不是方法数），104/4、confirmed103/3、Lean1不变。原root与专家快照未改，最终query待main实际终态及root最终状态。
'''
report_path=HERE/'SUPPORT_SHARED_COMPRESSION_WIKI_REPORT.md'
report_path.write_text(screen(report))
paths_f5=evidence('f5_induced_support_closure')+evidence('f5_induced_shared_middle_routes')
paths_k2=evidence('d14_K2_exact_signature_compression')
for identifier,paths in [(ids[0],paths_f5),(ids[1],paths_k2)]:
    row=rows[identifier]
    row['report_paths']=list(dict.fromkeys(row['report_paths']+paths+[str(report_path.relative_to(ROOT))]))
    screen(json.dumps(row,ensure_ascii=False))
    assert all((ROOT/p).exists() for p in row['report_paths'])
pending=HERE/'SUPPORT_SHARED_COMPRESSION_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==374
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert ledger[key]==after[key]
with (HERE/'SUPPORT_SHARED_COMPRESSION_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Recorded exact supportH refutation, proper-support projection/density exclusion fororder>=1921,20shared-middle literalpredictions, and insufficientK2 equalitycompression on twoexistingrows. No newmethod/graph or enhancedmainRUN; newcombinedreviewpending; finalqueryawaitsroot.')
receipt=dict(status='PASS_SUPPORT_DENSITY_SHARED_AND_K2_EQUALITY_COMPLETED_PENDING_FINAL',
    updated_UTC=NOW,record_count=374,existing_ids=ids,
    H_prediction='REFUTED',closed_supports=24575,max_proper_support=19,
    all30_nonempty_necessary_for_n1921=True,whole_fibers_required=False,
    shared_middle_pairs=20,all20_exact5routes=True,
    K2_port_classes=3589,K2_target_pair_classes=94069,K2_new_SAT_calls=0,
    new_combined_external_review='PENDING',enhanced_main_solver_run_recorded=False,
    new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out=HERE/'SUPPORT_SHARED_COMPRESSION_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),record_count=374),ensure_ascii=False))
