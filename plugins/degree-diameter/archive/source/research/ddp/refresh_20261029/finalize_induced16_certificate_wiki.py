"""Record the fixed-source LRAT-backed exclusion and current exact stop scope."""
from pathlib import Path
from datetime import datetime,timezone
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
ROOT_UPDATED='2026-10-30 00:36:09 UTC'


def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'aris_repo/tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


helper,capture=module('research_wiki'),module('capture_filter')


def screen(text):
    assert not capture.screen(text),capture.screen(text)
    return text


modeldir=HERE/'f5_induced_same_fiber_model'
cert=json.loads((modeldir/'lrat_certificate/RESULT.json').read_text())
binding=json.loads((modeldir/'SOURCE_CACHE_BINDING.json').read_text())
reviewprefix=ROOT/'reviews/ddp/f5_H65_route_classes_20261030'
review=json.loads(reviewprefix.with_suffix('.response.json').read_text())['structuredContent']
turn=json.loads((HERE/'INDUCED_GEOMETRIC_TURN_RESULT.json').read_text())
assert cert['status']=='LRAT_VERIFIED_UNSAT_EXACT_CNF'
assert cert['verified_UNSAT_of_exact_CNF'] is True
assert cert['input']['header']=='p cnf 333551 2316695'
assert cert['checker']['returncode']==20
assert 's VERIFIED' in (modeldir/'lrat_certificate/checker.stdout').read_text()
assert cert['source_CNF_modified_by_this_run'] is cert['old_terminal_modified'] is False
assert binding['status']=='CACHE_EQUALS_LITERAL_FULL_SOURCE_EDGE_RELATION'
assert binding['vertices_compared']==3750 and binding['directed_cache_entries']==75000
assert (review['status'],review['model'],review['effort'])==('SUCCESS','gemini-3.8-flash-high','high')
assert turn['status']=='FIXED_SOURCE_INDUCED16_COMPUTATIONALLY_EXCLUDED'
owned=[ROOT/'AGENTS.md',ROOT/'RESEARCH_BRIEF.md',
    ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',ROOT/'research/progress.html',
    ROOT/'expert_review_current/EXPERT_HANDOFF_20261029.md',
    ROOT/'expert_review_current/build_handoff_20261029.py']
owned_before={p:p.read_bytes() for p in owned}
brief=(ROOT/'RESEARCH_BRIEF.md').read_text()
assert '2026-10-30 00:36:09 UTC' in brief and 'INDUCED_GEOMETRIC_TURN_RESULT.json' in brief
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows'])==374
identifier='ddp-f5-literal3750-induced-retention-max16-d3-20261029'
row=copy.deepcopy(next(r for r in before['rows'] if r['id']==identifier)['source_record'])
review_meta=dict(status='SUCCESS_SOUND_AS_STATED',actual_model=review['model'],effort=review['effort'],
    thread_id=review['threadId'],
    accepted_scope='H65grid/nesting/threshold,boundary64vs65,allhighmax16obstruction,externalcompletepathclass,samefiberpathclassandfourclauseexpansion.',
    reviewer_double_direction_counting_wording_not_adopted=True,
    actual_total_shared_groups_including_both_directions=22500,
    each_direction_groups=11250,shared_clauses=45000,
    model_changed_due_to_review_wording=False,
    output_enumeration_CNF_LRAT_BFS_Lean_not_executed_by_reviewer=True,
    later_uniform75_plane_preserving_chart_obstruction_reviewed=False,
    response=str(reviewprefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition=str(reviewprefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
variants={v['label']:v for v in row['variants']}
for label in [
    'all30_fibers232500_pairs_exact_same_fiber_distance_CNF_prepared_20261030',
    'H65_partial_line_grid_rule_sharp_threshold_and_all_high_obstruction_20261030',
    'H65_exact_threshold_flags_and_conditional_line_CNF_fragments_prepared_20261030']:
    variants[label]['new_H65_and_routeclasses_external_review']='SUCCESS_SOUND_AS_STATED'
    variants[label]['actual_H65_routeclasses_static_review']=review_meta
    if 'new_route_classes_external_review' in variants[label]:
        variants[label]['new_route_classes_external_review']='SUCCESS_SOUND_AS_STATED'
raw=variants['combined_same_fiber_H65_333551_model_rawUNSAT_uncertified_20261030']
raw['stage']='PRESERVED_DISCOVERY_RAW_UNSAT_BEFORE_LRAT_CERTIFICATION'
raw['superseded_as_current_conclusion_by']='exact_same_CNF_LRAT_verified_and_graph_to_CNF_scope_preserved_20261030'
new=[
 dict(label='exact_same_CNF_LRAT_verified_and_graph_to_CNF_scope_preserved_20261030',
    status='COMPUTATIONALLY_CERTIFIED_FIXED_SOURCE_INDUCED_EXCLUSION',
    proposition='ThereisnoSsubsetV(G3750)with|S|>=1921,maxdegree(G[S])<=16anddiameter(G[S])<=3.',
    fixed_source_literal='research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges',
    subset_retention_independent_on_all3750_vertices=True,
    exact_order1921_assumed=False,whole_fiber_assumed=False,uniform_fiber_size_assumed=False,
    all_valid_target_sets_extend_to_final_necessary_CNF=True,
    preservation_chain='research/ddp/refresh_20261029/f5_induced_same_fiber_model/EXCLUSION_SCOPE.md',
    CNF_variables=333551,CNF_clauses=2316695,
    exact_CNF_LRAT_verified=True,independent_checker='lrat-trim0.2.0',
    checker_exit=20,checker_output='s VERIFIED',
    certificate_solver_CPU_seconds=cert['solver']['CPU_seconds'],
    certificate_checker_CPU_seconds=cert['checker']['CPU_seconds'],
    certificate_whole_CPU_seconds=cert['certificate_whole_CPU_seconds'],
    discovery_plus_certificate_whole_CPU_seconds=cert['combined_whole_CPU_seconds'],
    CNF_modified_for_certificate=False,old_raw_terminal_preserved=True,
    source_cache_literal_entries_equal=75000,
    cache_binding_CPU_seconds=binding['CPU_seconds'],cache_binding_source_reads=1,
    old_source_D3_BFS_repeated=False,new_graphs=0,
    fixed_source_vertex_retention_family_closed=True,
    general_N16D3_upper_bound_claimed=False,edge_rewiring_or_other_source_excluded=False,
    negative_Lean_formalized=False,automatic_retry=False),
 dict(label='uniform75_plane_preserving_external_chart_repair_shortword_capacity_obstruction_20261030',
    status='LOCAL_PAPER_EXCLUSION_NOT_EXTERNALLY_REVIEWED',
    scope='FixedC30,eachfiberthreefullcosetsofgivenE(75points),externalchartlinearpartmapsEsourceintotargetEandnoiseintargetE;edge-specificaffinechartsallowed.',
    controller_endpoint_pair=[0,28],
    all_control_walks_at_most3=[[0,20,28],[0,9,22,28]],
    both_words_only_external_edges=True,
    reachable_points_per_word_at_most=25,total_reachable_at_most=50,
    target_fiber_points=75,
    cycle_holonomy_identity_assumed=False,triangle_charts_restricted_for_witness=False,
    outside_plane_noise_or_general_nonuniform_or_different_controller_excluded=False,
    external_reviewed=False,solver_calls=0,new_graphs=0)]
variants.update({v['label']:v for v in new})
row['variants']=list(variants.values())
row['outcome_class']='COMPUTATIONALLY_CERTIFIED_FIXED_SOURCE_INDUCED_FAMILY_EXCLUDED'
row['scope']='固定已验3750/37500成功字面图G的全部独立顶点保留S；计算排除|S|≥1921、maxdegree(G[S])≤16、diameter(G[S])≤3。不限wholefiber、均匀层大小、对称或恰1921。EXCLUSION_SCOPE给合法图→必要CNF保全链，75000缓存邻接项与已验literal相等，exact333551/2316695 CNF经独立LRAT检查VERIFIED。只排该固定源诱导域，不排一般N(16,3)、改边或换源；负结论未Lean。'
row['failure_or_result']='历史固定3000/24000/16regular诱导图实际失败；旧必要模型UNKNOWN保留。新组合模型发现阶段rawUNSAT后，原样CNF唯一LRAT再现及独立lrat-trim验收s VERIFIED；认证62.004199912CPU、发现+认证whole119.899128932CPU。图→CNF必要性链及source cache全75000项对象绑定完成，故本固定源全部n≥1921/max16/D3诱导子图已计算排除。后续uniform75保平面chart修补另被两短词最多50<75局部阻断，未外审。'
row['other_metrics'].update(
    current_retention_main_status='LRAT_VERIFIED_FIXED_SOURCE_INDUCED_EXCLUSION',
    final_samefiber_H65_main_merged_or_run_recorded=True,
    H65_plus_new_route_classes_external_review='SUCCESS_SOUND_AS_STATED',
    exact_CNF_LRAT_verified=True,source_cache_full_literal_binding=True,
    source_cache_literal_entries_compared=75000,
    fixed_source_induced_n_at_least1921_computationally_excluded=True,
    arbitrary_nonuniform_subset_in_scope=True,
    fixed_source_vertex_deletion_stop=True,
    general_induced_problem_strictly_excluded=False,
    general_N16D3_excluded=False,negative_16_Lean=False,
    later_uniform75_plane_preserving_obstruction_external_reviewed=False,
    latest_batch_index='research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json')
row['lesson_and_restart_condition']='停止这张固定3750图所有删顶点seed、层大小调整及同类求解时间续算；限制来源是完整必要CNF的独立LRAT不可满足证书与图→CNF保全链，不再只是局部坏对或rawUNSAT。保留共享路线/H65结构认识，若继续16度必须实际改源或改边规则；uniform75且external每步保给定E的chart修补也被两词50<75局部排除。一般N(16,3)仍开放。'
row['unclosed_gap']='本固定3750源的诱导n≥1921/max16/D3全范围已计算排除并停止。一般16度图、其它源或真正改变边规则仍开放；负结论未Lean。uniform75局部chart障碍未外审。14度K2旧UNKNOWN不受该结论影响，新fractional诊断仅准备、尚无actual结果，不记RUN或LP终态。'
paths=[
    'research/ddp/refresh_20261029/f5_induced_same_fiber_model/EXCLUSION_SCOPE.md',
    'research/ddp/refresh_20261029/f5_induced_same_fiber_model/SOURCE_CACHE_BINDING.json',
    'research/ddp/refresh_20261029/f5_induced_same_fiber_model/model.cnf',
    'research/ddp/refresh_20261029/f5_induced_same_fiber_model/lrat_certificate/RESULT.json',
    'research/ddp/refresh_20261029/f5_induced_same_fiber_model/lrat_certificate/checker.stdout',
    'research/ddp/refresh_20261029/f5_induced_same_fiber_model/lrat_certificate/certificate.lrat',
    'research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json',
    'research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN.md']
paths+=[str(reviewprefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md','.response.json','.DISPOSITION.md']]
row['report_paths']=list(dict.fromkeys(row['report_paths']+paths))
assert all((ROOT/p).exists() for p in row['report_paths'])
screen(json.dumps(row,ensure_ascii=False))
pending=HERE/'INDUCED16_CERTIFIED_SCOPE_WIKI_ROWS.json'
pending.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- FIXED_SOURCE_INDUCED16_LRAT_CERTIFIED_20261030 -->'
note=f'''
## {NOW} 固定3750源诱导16度域已计算排除

当前[总索引](../research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json)／[研究解释](../research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN.md)与root00:36:09状态一致。任意独立顶点保留S、不限均匀/wholefiber/恰1921，只要|S|≥1921、maxdegree≤16、D≤3，就由[完整必要性链](../research/ddp/refresh_20261029/f5_induced_same_fiber_model/EXCLUSION_SCOPE.md)导出exact333551/2316695 CNF可满足；该CNF的[LRAT证书](../research/ddp/refresh_20261029/f5_induced_same_fiber_model/lrat_certificate/RESULT.json)已独立检查s VERIFIED。源cache与已验literal全部75000邻接项绑定完成，无旧D3BFS重验。因此仅此固定源的全部诱导目标已计算排除，停止删点seed/层大小/同类续算，不外推一般N(16,3)；负结论未Lean。

H65和同层完整路线外审实际SUCCESS/SOUND AS STATED；总22500组已含两向，审阅文字重复计数在DISPOSITION澄清，编码未改。晚出的uniform75保平面externalchart修补仅两短词覆盖≤50<75，是本地障碍，未冒外审。

14度新fractional诊断尚准备、没有actual结果，旧K2仍UNKNOWN。374记录、104/4合法例、confirmed103/3、Lean1保持；专家包冻结23:55快照，不重包。最后canonical index/query已在root00:36:09后重建，后续14实际终态另增量同步。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:out.write('\n\n'+marker+'\n'+screen(note))
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
assert '账本现374条实验／来源记录' in gap[:1800]
gap_marker='<!-- INDUCED16_CERTIFIED_CURRENT_20261030 -->'
gap_note=f'''{gap_marker}
当前16度固定源结论已收束（root00:36:09 UTC）：[总终态](../research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json)／[精确排除范围与图→CNF链](../research/ddp/refresh_20261029/f5_induced_same_fiber_model/EXCLUSION_SCOPE.md)。已验3750源不存在n≥1921、max16、D3的任意诱导子图，不限wholefiber/均匀/恰1921；sourcecache75000项绑定和独立LRAT VERIFIED齐备。仅排固定源，不是一般N(16,3)上界，负结论未Lean；停止该源删点seed/层大小/续时。H65/routeclasses实际外审SOUND，22500总组已含两向；后出的uniform75保平面chart≤50<75仅本地。14K2旧UNKNOWN，新fractional诊断仅准备无actual结果。专家23:55冻结快照不重包；374与104/4、confirmed103/3、Lean1不变。
'''
if gap_marker not in gap:
    anchor='<!-- EXPERT_HANDOFF_2355_CURRENT_DELIVERY_20261029 -->'
    assert anchor in gap
    gap=gap.replace(anchor,screen(gap_note)+'\n\n'+anchor,1)
gap=gap.replace('交付不是新研究成果；增强16主solver未启动，14K2仍UNKNOWN，新引理未外审。',
    '交付不是新研究成果；23:55快照当时增强16未启动、新引理未外审，后续证书和真实数学状态见上方当前研究入口。',1)
gap=gap.replace('当前最高研究阶段已收束（root23:22:14 UTC）',
    '前一研究阶段已收束（root23:22:14 UTC；后续16固定源已在上方计算排除）',1)
gap_path.write_text(screen(gap))
with (HERE/'INDUCED16_CERTIFIED_SCOPE_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Fixedliteral3750source fullinducedn>=1921/max16/D3 computationallyexcluded viaexactCNFLRATVERIFIED+graph-to-CNFpreservation+75000entrysourcebinding. Rawhistorypreserved;H65actualstaticSOUNDcountwordingcorrected;negative notLean/generalN16D3. Uniform75chart50<75onlylocal. Root00:36:09read;14fractionalnoactualyet;ledger374/1044/confirmed1033/Lean1 unchanged;expert23:55frozen.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==374
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key]==after[key]
assert all(p.read_bytes()==data for p,data in owned_before.items())
query=(WIKI/'query_pack.md').read_text()
assert len(query)<=8000 and 'INDUCED_GEOMETRIC_TURN_RESULT.json' in query
receipt=dict(status='PASS_FIXED_SOURCE_INDUCED16_CERTIFIED_SCOPE_QUERY_REBUILT',
    updated_UTC=NOW,root_state_update_UTC=ROOT_UPDATED,record_count=374,existing_id=identifier,
    exact_CNF_LRAT_verified=True,fixed_source_all_induced_n_at_least1921_max16_D3_excluded=True,
    general_N16D3_upper_bound_claimed=False,negative_Lean=False,
    source_cache_directed_entries_equal=75000,H65_static_review=review_meta,
    uniform75_chart_obstruction_external_reviewed=False,
    D14_fractional_actual_result_not_yet_recorded=True,
    new_experiments=0,new_methods=0,new_graphs=0,new_Lean_instances=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    expert_snapshot_preserved='2026-10-29 23:55 UTC',root_and_expert_files_unchanged=True,
    query_chars=len(query),canonical_helper='aris_repo/tools/research_wiki.py',
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    final_query_rebuild_after_root_update_pending=False,
    pending=['D14 fractional diagnosis actual result'],helper_stdout=run.stdout.strip())
out=HERE/'INDUCED16_CERTIFIED_SCOPE_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=374,query_chars=len(query)),ensure_ascii=False))
