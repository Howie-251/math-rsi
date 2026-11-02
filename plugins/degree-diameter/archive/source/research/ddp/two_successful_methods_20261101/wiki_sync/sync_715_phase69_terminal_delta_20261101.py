"""One minimal canonical Wiki delta: two terminal experiments, no full rebuild."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if (p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='STALE_715_PHASE69_TERMINAL_DELTA_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(directory,names):
 paths=[directory+n for n in names];assert all((R/p).is_file() for p in paths);return paths
def raw(rid,title,family,degree,diameter,baseline,hypothetical,scope,status,distance,lesson,metrics,paths):
 return dict(id=rid,title=title,family=family,idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',record_type='necessary_route_or_local_counting_gate',target_Delta=degree,target_D=diameter,savedL=baseline,baseline_date='2026-11-01 current Comellas main; source and old scopes inherited',n=dict(actual=None,hypothetical=hypothetical),actual_graph_Delta=None,actual_D=None,actual_D_scope='No new full target graph; finite local premise or route-image gate only',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=diameter,scope=scope,outcome_class=status,new_lower_bound=False,distance_text=distance,lesson_and_restart_condition=lesson,restart_condition=lesson,unclosed_gap='General target parameter remains open; only the explicitly fixed source/rule is closed.',other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,**metrics),evidence_paths=paths)
P=S+'stale_record_transfer_d11D3/cooperative715_interface/'
p=read(P+'RESULT.json');pt=read(P+'TERMINAL.json');pd=read(P+'ROOT_DISPOSITION.json');support=read(P+'CORE_SUPPORT_RESULT.json')
assert p['status']=='SUPPORTED_ACTUAL715_FIXED_OLD_INDUCED_ARBITRARY_HELPER_OBSTRUCTION_STOP'
assert pt['stop'] and not pt['active_processes']
assert pd['status']=='ROOT_ACCEPTED_PAPER_OBSTRUCTION_WITH_ACTUAL_LOCAL_SUPPORT'
assert support['status']=='PASS_ACTUAL715_NEW_CORE_R2_AND_DESIGN_PREMISES'
assert p['paper_corollary_intra_class_completion']['new_numerical_checks']==0
oldid='ddp-more-graphs-20261027-source-slack-monotone'
id715='ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101'
rows=[raw(id715,
 '11D3旧715源：P3实际结构推翻裸twins猜想，owner-moment排任意finite helper并继承内部K3完成',
 'Retained-source helper routing',11,3,715,None,
 'Actual published715 literal with its old induced adjacency fixed, any nonempty finite helper graph and legal spokes, max11/D3. Corollary also permits any subset of the65 missing leaf-leaf edges inside the original P3 classes. No cross-class old-old additions or old-edge deletion/replacement; not generalN(11,3).',
 p['status'],
 '实际715为3770边、degree9:130/10:65/11:520；65个P3类各共享8core邻点，原195个独立degree8猜想REFUTED。Petersen10各8pins共80，class目标已需至少195spokes。更强actual715新core-R2支持给65个size72支持、520个9块3-(65,9,1)、owner内交8/外交1；任意H取min-degree r，r0/1可达core≤462/515；a≤7类数≤36<65；a8/a9强制坏owner≥28/23，超邻helper能提供24/18。排所有fixed-old-induced helper数与拓扑，未生成725或其它图。',
 'STOP this exact frozen715 helper rule and internal P3→K3 completion. A future source-based attempt must change cross-class old adjacency, delete/replace old edges, or use another source. Do not repeat a helper topology/size ladder or call this parameter optimality.',
 dict(Moore_bound=1222,located_baseline=715,Moore_space=507,Moore_gap_is_not_constructibility=True,
 actual_source=p['actual_source'],source_prediction_status=p['source_prediction_status'],
 old_source_slack_node=oldid,old_t_at_most5_exclusion='historical valid subset, preserved; stronger scope linked rather than falsified',
 local_support={k:support[k] for k in ['canonical_class_core_R2_expansions','T_size_histogram','S_size_histogram','single_multiplicity_histogram','pair_multiplicity_histogram','triple_multiplicity_histogram','intersection_histogram','scalar_partition_bounds']},
 proof_cases=p['proof_cases'],outside_moment_identity=p['outside_moment_identity'],reentry_attack=p['reentry_attack'],
 class_completion_corollary=p['paper_corollary_intra_class_completion'],
 min_helper_argument_not_Petersen_only=True,root_paper_acceptance=pd['status'],Lean='NOT_FORMALIZED_LOCAL_PAPER_RESULT',
 measured_CPU_seconds=pt['CPU_measured_seconds'],CPU_budget_seconds=20,CPU_note=p['CPU_note'],
 new715_adjacency_parses=1,sourceD3_BFS=0,old585_R2_or_Steiner_rechecks=0,helpergraph_solver_runs=0,terminal=True),
 evidence(P,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json','ARBITRARY_HELPER_PRED.md','ARBITRARY_HELPER_NOTE.md','ARBITRARY_HELPER_RESULT.json','CORE_SUPPORT_RESULT.json','CORE_SUPPORT_DATA.json','check_core_support.py','SOURCE_CLASS_INTERFACE.json','PETERSEN10_NOTE.md','PETERSEN10_RESULT_HISTORY.json'])
 +['research/ddp/more_graphs_20261027/d3d4_transfer/REPORT.md','research/ddp/more_graphs_20261027/d3d4_transfer/RESULT.json','research/ddp/more_graphs_20261027/d3d4_transfer/SOURCES.json'])]
Q=S+'stale_record_transfer_d4D8/loz3243_interface/'
interface=read(Q+'RESULT.json');capacity=read(Q+'phase69_capacity_gate/RESULT.json');forms=read(Q+'coefficient_alias_gate/RESULT.json')
norm=read(Q+'normalized_parameter_gate/RESULT.json');nt=read(Q+'normalized_parameter_gate/TERMINAL.json')
assert capacity['minimum_words']==160 and 'REFUTED' in capacity['prediction']
assert forms['minimum_distinct_form_count']==159 and 'REFUTED' in forms['prediction']
assert norm['status']=='COMPLETE_NO_FIXED_FOUR_PARAMETER_D8_FAMILY'
assert norm['parameter_representatives_evaluated']==19462 and norm['complete_normalized_parameter_domain']
assert norm['critical_slot_survivor_count']==0 and norm['maximum_actual_image_cardinality']==117
assert nt['all_processes_terminal'] and not nt['running']
id69='ddp-stale-d4d8-loz69-f139-shared4-normalized-endpoints-20261101'
rows.append(raw(id69,
 '4D8旧Loz规则迁移：raw160/coeff159两次必要门预测被推翻，19462归一参数全失败且最大image117<139',
 'ordinary graph-cover transfer',4,8,3243,9591,
 norm['exact_scope']+' One mechanism node combines raw NB capacity, shared coefficient aliasing and complete normalized parameter evaluation. Not a repeat of the old3243 ordinary-cover or fixed centered-control checks; not all4D8 graphs.',
 norm['status'],
 '固定69-state=3bases×23phases。raw≤8NB最小160≥139、distinctcoeff最小159≥139，两个“容量不足”预测均REFUTED，只是必要PASS。随后gauge c→c+(6^a−1)d置c2=0，再非零scale置首非零1，P²(F139)+zero全19462代表均在tight46→52漏端点；实际image最大117、至少缺22/139，best(1,102,0,128)。所有159form的gauge-offset绑定通过。未造9591图，未用sourceBFS或旧失败singlecontrol冒新排除。',
 'STOP this exact fixed phase/r6/F139 four-shared-translation family. Raw/per-form necessary passes do not guarantee simultaneous endpoint coverage. Do not restart the19462 domain or prior ordinary-cover/girth10/centered-control scopes; other phases, per-phase maps or arbitrary permutation lifts require genuinely changed premises and remain outside this finiteNO.',
 dict(Moore_bound=13121,located_baseline=3243,Moore_space=9878,hypothetical_target=9591,target_below_Moore_by=3530,Moore_gap_is_not_constructibility=True,
 accepted_source=interface['source'],inherited_stops=interface['inherited_stops'],inherited_single_control=interface['inherited_single_control'],
 raw_gate=dict(status=capacity['status'],prediction=capacity['prediction'],ordered_slots=capacity['actual_ordered_pairs_counted'],minimum_words=160,tight_pair=capacity['tight_pair'],required_endpoints=139),
 coefficient_gate=dict(status=forms['status'],prediction=forms['prediction'],minimum_distinct_forms=159,all4761_slots_computed=forms['all4761_coefficient_slots_computed']),
 normalized_gate={k:norm[k] for k in ['parameter_representatives_evaluated','complete_normalized_parameter_domain','critical_slot','critical_slot_survivor_count','maximum_actual_image_cardinality','required_image_cardinality','best_representative','gauge_binding_all159','all_representatives_have_saved_first_missing_endpoint']},
 phase_coordinate='Z23; 69 is total controller-state count, not phase modulus',
 normalization_review='same-slot affine endpoint bijection; no false fixed-normal0-root premise',
 cumulative_charged_CPU_seconds=nt['cumulative_charged_CPU_seconds'],CPU_budget_seconds=nt['cumulative_CPU_budget_seconds'],
 actual_new_parameter_evaluation_CPU_seconds=nt['actual_evaluation_process_CPU_seconds'],
 prior_and_failed_preparation_charges_preserved=True,no_timer_reset=True,
 source_graph_BFS=0,old_word_or_form_recounts=0,solver_Lean_review_runs=0,terminal=True),
 evidence(Q,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json',
 'phase69_capacity_gate/PRED.md','phase69_capacity_gate/NOTE.md','phase69_capacity_gate/RESULT.json','phase69_capacity_gate/TERMINAL.json',
 'coefficient_alias_gate/PRED.md','coefficient_alias_gate/NOTE.md','coefficient_alias_gate/RESULT.json','coefficient_alias_gate/TERMINAL.json','coefficient_alias_gate/FORM_MODEL.json',
 'normalized_parameter_gate/PRED.md','normalized_parameter_gate/NOTE.md','normalized_parameter_gate/RESULT.json','normalized_parameter_gate/TERMINAL.json','normalized_parameter_gate/PREPARATION_RESULT.json','normalized_parameter_gate/NORMALIZATION_BINDING.json','normalized_parameter_gate/ALL_REPRESENTATIVE_COVERAGES.csv','normalized_parameter_gate/BEST_CRITICAL_SLOT_COVERAGE.json','normalized_parameter_gate/run_once.py','normalized_parameter_gate/parameter_gate_normalization_review.md'])))
# All factual terminal/root inputs are checked before any Wiki mutation.
L=read('research-wiki/DDP_METHOD_LEDGER.json');countkeys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']
counts={k:L[k] for k in countkeys};assert tuple(counts[k] for k in countkeys[:3])==(152,43,46)
before=L['record_count'];existing={x['id']:x for x in L['rows']};assert len(existing)==before
newids=[r['id'] for r in rows];assert len(newids)==2 and all(i not in existing for i in newids)
assert all(not(W/'experiments'/f'{i}.md').exists() for i in newids)
oldnode=W/'experiments'/f'{oldid}.md';oldtext=oldnode.read_text();assert oldid in existing and LABEL not in oldtext
STARTMARK='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->';ENDMARK='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
prefixes={}
for filename in ['index.md','query_pack.md','gap_map.md']:
 text=(W/filename).read_text();assert text.startswith(STARTMARK) and ENDMARK in text and LABEL not in text
 prefixes[filename]=text[:text.index(ENDMARK)+len(ENDMARK)]
assert LABEL not in (W/'DDP_METHOD_LEDGER.md').read_text()
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
common=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
helper=common['helper'];helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
normalized=[]
with (OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
 for source in rows:
  n=common['normalize'](source);n['goal']['baseline_date']=source['baseline_date'];common['write_node'](n);normalized.append(n)
# Keep the older t<=5 source/slack record intact and add a dated forward pointer.
oldtext+='\n\n<!-- '+LABEL+' -->\n## 后续更强精确范围（2026-11-01，原结论保留）\n\n原715单点及t≤5排除仍有效，以上为历史实验原文；不是把旧结论改为错误。后续实际715的65类core-R2新支持和owner-moment论证已排任意finite helperH，前提是旧诱导图固定；paper corollary允许各P3内部补leaf-leaf变K3，仍不允许跨原class新边或删改旧边。见[更强本scope节点]('+id715+'.md)。没有sourceD3重验、solver/Lean或新图计数。\n'
oldnode.write_text(oldtext)
update=dict(path='research-wiki/experiments/'+id715+'.md',date='2026-11-01',note='Later stronger fixed-induced arbitrary-helper obstruction; oldt<=5 remains a valid historical subset. Internal P3→K3 corollary uses no new numerics.')
oldrow=existing[oldid];oldrow.setdefault('other_metrics',{}).setdefault('later_scope_updates',[]).append(update)
oldrow['source_record'].setdefault('other_metrics',{}).setdefault('later_scope_updates',[]).append(copy.deepcopy(update))
for row in normalized:existing[row['id']]=row
L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def tab(row):
 safe=common['safe'];return '| ['+safe(row['title'])+'](experiments/'+row['id']+'.md) | '+safe(common['goal_text'](row))+' | '+safe(common['gap_text'](row))+' | '+safe(row['exact_scope'])+'；'+safe(row['lesson'])+'；[原始证据](../'+row['evidence_paths'][0]+') |'
mdpath=W/'DDP_METHOD_LEDGER.md';md=mdpath.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{len(existing)}条记录；不以此宣称{len(existing)}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 两个长期目标机制的终态增量\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+'\n'.join(tab(r) for r in normalized)+'\n\n本增量2个实验节点，不宣称2种新独立方法；715子门与三个phase69必要／参数门分别合并，同一机制不拆门增计。图／参数／Lean增量均0。\n'
mdpath.write_text(md)
links='；'.join('['+r['title']+'](experiments/'+r['id']+'.md)' for r in normalized)
nav='<!-- '+LABEL+' -->\n### 2026-11-01 新终态：715任意H固定源障碍与69phase四参数完整NO\n\n715实际为P3三胞、degree9/10/11，裸degree8独立twins预测已推翻；新的actual715 core-R2设计绑定支持固定旧诱导图下任意finiteH严格NO，并继承类内P3→K3完成；跨class新边／删改源仍未排。4D8的raw160／coeff159容量预测两次REFUTED，最终19462归一参数全失败、最佳image117<139，排固定phase/r6/F139四共享参数族而非一般4D8。两节点真实Moore空间507／9878不是可实现保证；没有新图／参数／Lean，152／43／46及旧n61暂停保持。\n\n'+links+'\n\n'
preserved={}
for filename,prefix in prefixes.items():
 path=W/filename;text=path.read_text();assert text.startswith(prefix);pos=len(prefix);text=text[:pos]+'\n\n'+nav+text[pos:]
 if filename=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m
  n0=int(m[1]);text=text[:m.start()]+f'## Experiments ({n0+2})'+text[m.end():]
  at=text.index('\n',m.start())+1;text=text[:at]+''.join('- `exp:'+r['id']+'` — '+r['title']+' [no]\n' for r in normalized)+text[at:]
 assert text[:pos]==prefix;path.write_text(text);preserved[filename]=True
helper.append_log(str(W),LABEL+': two canonical experiment nodes added;715 actualP3 correction plus arbitrary finiteH fixed-induced obstruction and paper internalK3 corollary;69phase raw160/coeff159 predictions refuted,19462 normalized domain completeNO max117/139. Prior source/slackt<=5 remains valid historical subset with backlink. No source/solver/Lean/review rerun, no full index/query rebuild, human top blocks preserved;152/43/46 unchanged.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before+2 and {k:after[k] for k in countkeys}==counts
assert all((R/n['wiki_path']).is_file() for n in normalized)
receipt=dict(status='PASS_TWO_CANONICAL_TERMINAL_NODES_MINIMAL_DELTA',updated_UTC=NOW,records_before=before,records_after=after['record_count'],records_added=2,existing_historical_node_backlinked=oldid,new_experiment_ids=newids,canonical_helper='sync_ledger.py normalize/write_node → research_wiki.py add_experiment',full_index_query_rebuild=False,human_top_blocks_preserved_exact=preserved,old_t_at_most5_scope_preserved=True,raw_coefficient_normalized_gates_one_node=True,counts_unchanged=counts,graph_parameter_Lean_method_increments=[0,0,0,0],source_BFS_solver_Lean_field_review_hash_runs=0,old3243_cover_girth10_single_control_inherited=True,root_STATE_REPORT_progress_HTML_frozen_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,receipt_file=str((OUT/f'{LABEL}_RECEIPT.json').relative_to(R)),CPU_seconds=time.process_time()-START)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
