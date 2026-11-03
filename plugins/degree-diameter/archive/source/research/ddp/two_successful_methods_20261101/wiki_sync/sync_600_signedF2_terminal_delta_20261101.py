"""Two canonical terminal nodes only; preserve human navigation blocks."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir());W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync';LABEL='EXOO600_SIGNED_F2_TERMINAL_DELTA_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(p,names):
 q=[p+n for n in names];assert all((R/x).is_file() for x in q);return q
def raw(rid,title,family,degree,D,L,n,scope,status,distance,lesson,metrics,paths):
 return dict(id=rid,title=title,family=family,idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',record_type='bounded_candidate_or_input_transfer_gate',target_Delta=degree,target_D=D,savedL=L,baseline_date='2026-11-01 current main table; source legality inherited',n=dict(actual=None,hypothetical=n),actual_graph_Delta=None,actual_D=None,actual_D_scope='No accepted final target graph or complete global target diameter; source facts and scoped checks only',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=D,scope=scope,outcome_class=status,new_lower_bound=False,distance_text=distance,lesson_and_restart_condition=lesson,restart_condition=lesson,unclosed_gap='The general degree/diameter target remains open; stop only the explicitly sampled or failed input rule.',other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,**metrics),evidence_paths=paths)
P=S+'stale_record_transfer_d3D9/two_helper_repair602/'
a=read(P+'RESULT.json');at=read(P+'TERMINAL.json');b=read(P+'four_cut_spread_pins/RESULT.json');bt=read(P+'four_cut_spread_pins/TERMINAL.json')
assert a['status']==b['status']=='UNKNOWN_10000_SAMPLE_NO_HIT'
assert a['distinct_configurations_finished']==b['distinct_configurations_finished']==10000
assert a['both_helpers_passed']==b['both_helpers_passed']==0
assert not a['complete_configuration_family_exclusion'] and not b['complete_configuration_family_exclusion']
assert at['all_processes_terminal'] and bt['all_processes_terminal']
id600='ddp-stale-d3d9-exoo600-three-four-cut-helper-samples-20261101'
rows=[raw(id600,
 '3D9 Exoo600→602改边：三cut与四cut各10000样本均漏helper覆盖，整规则保持UNKNOWN并停止',
 'vertex splitting and matching',3,9,600,602,
 'One fixed inherited Exoo600 cubic/D9 source. First fixed-seed10000 distinct configurations:3matching cuts,1original-nonedge endpoint repair,remaining4pins2+2 at adjacent helpers. Second10000:4matching cuts,onepin percut,remaining4endpoints2old repairs,adjacent helpers2+2. Bounded samples only, not complete domains; no other seed/source/cut pattern.',
 'UNKNOWN_TWO_10000_SAMPLES_NO_HIT_STOP',
 '旧source非二分，不能使用odd-bipartite自动细分覆盖。三cut样本9999先漏helper600、1案600通过却601到old2距10；四cut真实消除“同cut两端必同为pins”的强制关联，但10000案全部漏helper600R9。两轮双方helper都通过为0，modified old-labelled BFS均0，不能说本轮发现old-old损伤。两次“出现双方helper覆盖”预测均被样本推翻；不是整个3cut/4cut族NO。',
 'STOP both bounded samples under the same20CPU ledger. No fifth cut, secondseed or source-D9/BFS rerun. A future experiment needs a genuinely changed premise; AFY70/D5 completeNO must not be imported as Exoo600/D9 exclusion.',
 dict(Moore_bound=1534,located_baseline=600,Moore_space=934,Moore_gap_is_not_constructibility=True,
 source_order=600,source_edges=900,source_degree=3,source_D9='primary inherited; no sourceD9BFS',source_bipartite=False,symmetry_unbound=True,
 target_cubic_edges=903,
 three_cut={k:a[k] for k in ['seed','distinct_configurations_finished','rejected_helper600','rejected_helper601','both_helpers_passed','rejected_old_old','helper_root_BFS_count','modified_graph_old_label_BFS_count','first_helper600_failure','first_helper601_failure','prediction_both_helpers_supported','complete_configuration_family_exclusion']},
 four_cut={k:b[k] for k in ['seed','distinct_configurations_finished','rejected_helper600','rejected_helper601','both_helpers_passed','rejected_old_old','helper_root_BFS_count','modified_graph_old_label_BFS_count','first_helper600_failure','prediction_both_helpers_supported','complete_configuration_family_exclusion']},
 first_rule_charged_CPU=at['total_charged_CPU_seconds'],cumulative_charged_CPU=bt['total_charged_CPU_seconds'],CPU_budget=20,no_timer_reset=True,
 actual_modified_helper_root_BFS_total=a['helper_root_BFS_count']+b['helper_root_BFS_count'],modified_old_label_root_BFS=0,source_validity_D9_BFS=0,
 helper_cooperation_formula='R7_K(A) union R7_K(B) union [R8_K(A) intersect R8_K(B)] covers all old vertices',
 complete_family_exclusion=False,ordinary_fulltarget_badpairs=None,global_target_D=None,terminal=True),
 evidence(P,['PRED.md','NOTE.md','PAPER_NOTE.md','RESULT.json','TERMINAL.json','run.cpp','run_once.py','ATTEMPTS.csv','four_cut_spread_pins/PRED.md','four_cut_spread_pins/NOTE.md','four_cut_spread_pins/PAPER_NOTE.md','four_cut_spread_pins/RESULT.json','four_cut_spread_pins/TERMINAL.json','four_cut_spread_pins/run.cpp','four_cut_spread_pins/run_once.py','four_cut_spread_pins/ATTEMPTS.csv'])
 +['research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md','research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json','research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md'])]
Q=S+'retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/'
f=read(Q+'RESULT.json');ft=read(Q+'TERMINAL.json');counter=read(Q+'COUNTEREXAMPLE.json')
assert f['status']=='STOP_SIGNED_F2_TRUE_INVERSE_FAILURE' and ft['all_processes_terminal'] and not ft['running']
assert counter['source_label']==0 and counter['target_label']==183 and counter['reverse_target_arc_count']==1
assert [x['label'] for x in counter['all_actual_reverse_noise_candidates']]==[2,13]
assert not f['graph_generated'] and f['new_true_arc_reverse_tests_before_stop']==26
idF2='ddp-stale-d10d4-signed-f2-15552-transfer3072-inverse-failure-20261101'
rows.append(raw(idF2,
 '10D4目标3072的signed-F2迁移：0→183无反向，指定整数lift仅char3可能互反，未构造图',
 'Route-chart source transfer',10,4,2556,3072,
 'Only the literal signed integer lift0→0,1→1,2→−1 of the five actual F3 affine templates, then reduction toF2; original192 controller unchanged. No field-homomorphism claim, symmetrization, alternate integer representatives or other fields/templates tested. Paper corollary uses the same signed integers and unique11→0 return arc to require characteristic3.',
 f['status'],
 'F2不是旧F3证明自动特化：26个新关系逆检查后实际0→183(globaltype1,noise1)仅有type3可回controller0，binary reverse噪声候选标签2/13都非0；真互反关系失败，8个真实global stays跳过。singularB本非GL，检查的是存在reverse noise。signed整数B3v1=−3e1，旧mod3为0而F2残留e1；指定同一整数lift在任意char≠3亦无法由v3=(1,1,1,1)抵消。0图/0BFS，未尝试ORsymm修度数或第二lift。',
 'STOP this one signed-F2 recipe and do not scan positive2/fields or silently symmetrize. The characteristic condition is only for these exact signed integer representatives; redesigned matrices or different representatives and general10D4 remain open. OldF3 source/kernel remains accepted but is not a certificate for the failed transfer.',
 dict(Moore_bound=8201,located_baseline=2556,Moore_space=5645,hypothetical_target=3072,target_margin_if_legal=516,Moore_gap_is_not_constructibility=True,
 inherited_source=dict(n=15552,controller_count=192,fiber='F3^4',published_reproduction=True,controller_only_inherited=True),
 coefficient_rule=f['coefficient_rule'],counterexample=counter,new_true_arc_reverse_tests=26,actual_global_stays_skipped=f['new_actual_global_stays_skipped'],
 paper_char3_necessary_corollary=dict(status='PAPER_ONLY_SAME_SIGNED_INTEGER_FAMILY',unique_return_controller11_to0=True,obstruction='0=−3e1+s(1,1,1,1) forces s0 then3=0',scope='all fields of char!=3 for these fixed signed coefficients; not different integer lifts or redesigned relations',new_field_runs=0),
 integral_type0_contrast='B0v0=0 and B0^2=I−v0e0^T hold as signed integer identities; one successfultype does not transfer alltypes',
 actual_process_CPU=ft['actual_process_CPU_seconds'],charged_CPU=ft['total_charged_CPU_seconds'],preparation_charge=ft['preparation_charge_seconds'],CPU_budget=20,
 new_target_graph_generated=False,target_BFS=0,old_F3_field_rank_graph_BFS_Lean_checks=0,solver_remote_runs=0,terminal=True),
 evidence(Q,['PRED.md','NOTE.md','PAPER_INTERFACE.md','RESULT.json','TERMINAL.json','COUNTEREXAMPLE.json','NEW_BINARY_GLOBAL_TYPES.json','run_once.py'])))
# Precheck all actual scope and current navigation before canonical mutations.
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];existing={r['id']:r for r in L['rows']};assert len(existing)==before
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs'];counts={k:L[k] for k in keys};assert tuple(counts[k] for k in keys[:3])==(152,43,46)
newids=[r['id'] for r in rows];assert all(i not in existing and not(W/'experiments'/f'{i}.md').exists() for i in newids)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and END in text and LABEL not in text;prefix[fn]=text[:text.index(END)+len(END)]
mdpath=W/'DDP_METHOD_LEDGER.md';assert LABEL not in mdpath.read_text()
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper'];helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
norm=[]
with (OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
 for r in rows:
  n=c['normalize'](r);n['goal']['baseline_date']=r['baseline_date'];c['write_node'](n);norm.append(n)
for n in norm:existing[n['id']]=n
L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def table(n):
 safe=c['safe'];return '| ['+safe(n['title'])+'](experiments/'+n['id']+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
md=mdpath.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{len(existing)}条记录；不以此宣称{len(existing)}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 600改边样本与signed-F2输入门：两节点终态\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+'\n'.join(table(n) for n in norm)+'\n\n600两次10000样本合一机制节点，均UNKNOWN，不借70/D5完整NO。F2实际逆失败与同signed整数的paper特征条件合一节点，无新field遍历。图／参数／Lean／独立方法增量均0。\n';mdpath.write_text(md)
links='；'.join('['+n['title']+'](experiments/'+n['id']+'.md)' for n in norm)
nav='<!-- '+LABEL+' -->\n### 2026-11-01 终态：Exoo600两样本UNKNOWN与signed-F2逆失败\n\nExoo600三cut／四cut各10000distinct均无双方helper-R9覆盖；old-labelled BFS0，不得称旧点路线被破坏或完整规则NO。最后signed-F2/3072输入门实际0→183无reverse（仅2/13），26新关系检查即停，未生成图。相同signed整数lift唯一返回arc给必要char3条件，0追加field测试；不排换整数代表/重设计。两个问题全部terminal，不5cut／第二seed／第二lift／field梯。152／43／Lean46和旧n61暂停不变。\n\n'+links+'\n\n'
preserved={}
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;text=text[:m.start()]+f'## Experiments ({int(m[1])+2})'+text[m.end():];pos=text.index('\n',m.start())+1;text=text[:pos]+''.join('- `exp:'+n['id']+'` — '+n['title']+(' [partial]\n' if 'UNKNOWN' in n['status'] else ' [no]\n') for n in norm)+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': two terminal experiment nodes via canonical helper;Exoo600 threecut and fourcut each10000sampleUNKNOWN with all failures still helper-old, no old-label BFS; signedF2 actual inverse failure0→183 and paper-only sameinteger char3 corollary. No graph/parameter/Lean/method increments, no full rebuild, human top preserved;152/43/46 unchanged.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before+2 and {k:after[k] for k in keys}==counts
receipt=dict(status='PASS_TWO_CANONICAL_TERMINAL_NODES_MINIMAL_DELTA',updated_UTC=NOW,records_before=before,records_after=after['record_count'],records_added=2,new_experiment_ids=newids,source600_samples_merged_in_one_node=True,source600_family_exclusion_claim=False,F2_actual_inverse_failure=True,signed_integer_char3_corollary_paper_only=True,new_field_tests_for_corollary=0,human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,counts_unchanged=counts,graph_parameter_Lean_method_increments=[0,0,0,0],source_validation_BFS_solver_Lean_remote_or_hash_runs=0,root_STATE_REPORT_progress_HTML_frozen_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
