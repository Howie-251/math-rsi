"""Two actual cubic-target terminal mechanisms; minimal canonical Wiki delta."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir());W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync';LABEL='TWO_CUBIC_TERMINALS_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(base,names):
 p=[base+n for n in names];assert all((R/x).is_file() for x in p);return p
def make(rid,title,D,L,target,status,scope,distance,lesson,metrics,paths):
 return dict(id=rid,title=title,family='edge surgery and subdivision',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',record_type='bounded_or_exact_modified_graph_gate',target_Delta=3,target_D=D,savedL=L,baseline_date='2026-11-01 current main;sourceD inherited from primary',n=dict(actual=None,hypothetical=target),actual_graph_Delta=None,actual_D=None,actual_D_scope='No accepted final target graph; actual candidate root checks and exact scope below',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=D,scope=scope,outcome_class=status,new_lower_bound=False,distance_text=distance,lesson_and_restart_condition=lesson,restart_condition=lesson,unclosed_gap='Only this bounded sample or exact fixedsource edit scope stops; generaltarget remainsopen. Same Goal ACTIVE,oldN8/n61 PAUSED.',other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,**metrics),evidence_paths=paths)
P=S+'stale_record_transfer_d3D6/source132_interface/';C=P+'adjacent_helpers_repair134/'
a=read(C+'RESULT.json');at=read(C+'TERMINAL.json');ad=read(C+'ROOT_DISPOSITION.json')
assert a['status']=='UNKNOWN_10000_SAMPLE_NO_HIT' and ad['status']=='ROOT_ACCEPTED_SAMPLE_UNKNOWN_NOT_FAMILY_NO'
assert a['distinct_configurations_finished']==10000 and a['rejected_helper132']==9997 and a['rejected_helper133']==3
assert a['both_helpers_passed']==a['modified_graph_old_label_BFS_count']==0
assert not a['complete_configuration_family_exclusion'] and at['all_processes_terminal']
assert a['source_input_binding']['status']=='PASS_LITERAL_SIMPLE_CUBIC_INPUT' and a['source_input_binding']['raw_parse_count']==1
id132='ddp-stale-d3d6-exoo132-adjacent-helpers-repair134-sample-20261101'
rows=[make(id132,
 '3D6 Exoo132→134：10000三cut相邻helpers样本全漏联合覆盖，原规则UNKNOWN并停止',6,132,134,a['status'],
 a['exact_rule']+' One fixedseed10000-distinct sample only;not allmatching/repair choices. Source is actualExoo1998 cubicD6,not degree6/D3 PSL132. Sourcegate andsample are one mechanismnode.',
 'source132/198上界input一次绑定132labels/198simpleedges/全3degree；D6由primary继承。133由degree≤2根B6≤127迫全cubic再奇偶排，因此试134/201。新相邻helper条件R4_H(A)∪R4_H(B)∪[R5_H(A)∩R5_H(B)]=all，比D5多一层提供试验依据。实际10000distinct：9997先helper132R6失败，余3 helper133R6失败，both0/old-labelled BFS0。联合cover预测未获本样本支持，不能写成old-old损伤或整个familyNO。首helper132到old3、helper133到old11各距7，完整路线保存。',
 'STOP this completed sample: no automaticseed/cutpattern/sample extension. A future experiment requires genuinely changed helpercoverage generation,not merely re-running the samepattern. Broader134graphs andotheroldedge edits remainopen;no numericalplan is started here.',
 dict(Moore_bound=190,located_baseline=132,Moore_space=58,Moore_gap_is_not_constructibility=True,
 source_order=132,source_edges=198,source_D6='PRIMARY_INHERITED_NOT_NUMERICALLY_VALIDATED',source_identity='Exoo1998 cubicD6,notPSL132',source_input_binding=a['source_input_binding'],
 target_cubic_edges=201,degree2_root_B6_upper=127,n133_impossible_by_local_degree_and_parity=True,
 seed=a['seed'],distinct_configurations=10000,first_helper_failures=9997,second_helper_failures_after_firstpass=3,both_helpers_passed=0,
 actual_modified_helper_BFS_roots=a['helper_root_BFS_count'],modified_old_label_BFS=0,source_D6_BFS=0,optional_original_pair_diagnostic_BFS=0,
 first_helper132_failure=a['first_helper132_failure'],first_helper133_failure=a['first_helper133_failure'],
 whole_configuration_family_excluded=False,prediction_joint_coverage_supported=False,root_acceptance=ad['status'],
 cumulative_CPU=at['total_charged_CPU_seconds'],CPU_budget=20,no_timer_reset=True,terminal=True,
 reporting_template_correction=dict(status='ROOT_CORRECTED_WITHOUT_NUMERIC_RERUN',current_radius=6,current_target=[134,201],paper='../PAPER_SCOPE_REVIEW.md',old600template_not_current_scope=True)),
 evidence(C,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json','SOURCE_INPUT_BINDING.json','ATTEMPTS.csv','run.cpp','run_once.py'])+evidence(P,['NOTE.md','RESULT.json','ROOT_DISPOSITION.json','PAPER_SCOPE_REVIEW.md','SOURCE_LITERAL_RETRIEVAL.json']))]
Q=S+'stale_record_transfer_d3D8/source360_interface/';D=Q+'single_subdivision361/'
b=read(D+'RESULT.json');bt=read(D+'TERMINAL.json');bd=read(D+'ROOT_DISPOSITION.json');first=read(D+'FIRST_NEWROOT_FAILURE.json')
assert b['status']=='COMPLETE_NO_FIXED_CHEN360_ALL540_SINGLE_SUBDIVISIONS'
assert bd['status']=='ROOT_ACCEPTED_COMPLETE_FIXED_CHEN360_SINGLE_EDGE_SUBDIVISION_NO'
assert b['candidates_finished']==b['rejected_newroot_R8']==540 and b['newroot_R8_passed']==b['candidate_old_label_BFS_count']==0
assert b['whole_fixed_source_single_subdivision_family_excluded'] and b['all540_oldedges_explicit_no_symmetry_inference']
assert bt['all_processes_terminal'] and bt['source_literal_parses_cumulative']==2 and bt['source_literal_successful_input_bindings']==1 and bt['HTTP_download_calls_inherited']==1
id360='ddp-stale-d3d8-chen360-all-single-edge-subdivision361-no-20261101'
rows.append(make(id360,
 '3D8 Chen360→361：逐540旧边新rootR8均失败，严格排固定源全部单细分，非一般3D8',8,360,361,b['status'],
 b['scope']+' All540literal oldedges explicitly tested;noautomorphism representative assumption. Sourcegate/formatcorrection/peredgechecks are one mechanismnode,not540methods.',
 'sourceChen2018 360/540 cubic,input binding1次成功；initial数值upper-neighbor错误guard先失败，修正只要求每无向边出现一次，HTTP仍1/rawparse累计2，0candidate/0BFS失败成本保留。随后540/540oldedge都生成对应361/541单细分邻接并检查actualnewrootR8，全部FAIL，firstfailedtargetdist9共540次；oldoldBFS0。newroot条件R7_(G-e)({u,v})=all，且endpoint-min等于原G。degree2rootB8≤511大于361，只说明可试，不保证覆盖。首rawedge[1,141]对应normalized[0,140]，new360到old22的shortest9路保存。',
 'STOP every single-edge subdivision of this fixedChen360 source;do not rerun anotherlabel of the sameedge orall540. A subsequent attempt must change the actualgenerationrule beyondonesubdivision,not infer general3D8nonexistence. Multipleedits/othersources remainoutside and are not automatically scheduled.',
 dict(Moore_bound=766,located_baseline=360,Moore_space=406,Moore_gap_is_not_constructibility=True,
 source_identity='JianxiangChen360,primary2018-10-16',source_order=360,source_edges=540,source_cubic_binding=True,source_D8='PRIMARY_INHERITED_NOT_NUMERICALLY_VALIDATED',
 target_edges=541,target_degree_histogram_by_construction={'2':1,'3':360},degree2_root_B8_upper=511,root_capacity_does_not_exclude_target=True,
 all_oldedges_tested=540,all_distinct_edges_explicit=True,newroot_R8_failures=540,newroot_R8_passes=0,recorded_first_failure_distance_histogram={'9':540},
 actual_final_newroot_BFS=540,old_label_BFS=0,source_D8_validation_BFS=0,original_pair_diagnostic_BFS=0,
 first_newroot_failure=first,complete_fixed_single_subdivision_scope_excluded=True,general_parameter_excluded=False,
 newroot_distance_formula='1+min(d_(G-e)(u,t),d_(G-e)(v,t))',endpoint_min_preserved='d_(G-e)({u,v},t)=d_G({u,v},t)',paper_global_upper9=True,newrootpass_not_oldoldcertificate=True,
 failed_format_attempt_preserved=True,format_failure_was_not_mathematicalNO=True,HTTP_downloads=1,raw_parse_attempts=2,successful_input_bindings=1,
 cumulative_CPU=bt['cumulative_charged_CPU_seconds'],CPU_budget=20,no_timer_reset=True,terminal=True,root_acceptance=bd['status']),
 evidence(D,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json','FIRST_NEWROOT_FAILURE.json','ATTEMPTS.csv','OUTPUT_ACCOUNTING.json','run.cpp','run_once.py','format_guard_failure/RESULT.json','format_guard_failure/TERMINAL.json','format_guard_failure/NOTE.md'])+evidence(Q,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','PAPER_SCOPE_REVIEW.md'])))
# Only the two mechanism rows are changed/added; all portfolio totals remain fixed.
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];assert before==434
existing={x['id']:x for x in L['rows']};ids=[x['id'] for x in rows];assert len(existing)==before and all(i not in existing and not(W/'experiments'/f'{i}.md').exists() for i in ids)
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs'];counts={k:L[k] for k in keys};assert tuple(counts[k] for k in keys[:3])==(152,43,46)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and END in text and LABEL not in text;prefix[fn]=text[:text.index(END)+len(END)]
mdpath=W/'DDP_METHOD_LEDGER.md';assert LABEL not in mdpath.read_text()
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper'];helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
norm=[]
with (OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
 for source in rows:
  n=c['normalize'](source);n['goal']['baseline_date']=source['baseline_date'];c['write_node'](n);norm.append(n)
for n in norm:existing[n['id']]=n
L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def table(n):
 safe=c['safe'];return '| ['+safe(n['title'])+'](experiments/'+n['id']+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
md=mdpath.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,'本页有436条记录；不以此宣称436种独立方法。',1);md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 两个小cubic目标终态：样本UNKNOWN与全边单细分NO\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+'\n'.join(table(n) for n in norm)+'\n\n两项sourcegate与各自candidate门分别合一个机制节点，不按每sample／每edge增方法；失败候选不计新图。152／43／Lean46，SameGoalACTIVE，旧N8/n61PAUSED。\n';mdpath.write_text(md)
links='；'.join('['+n['title']+'](experiments/'+n['id']+'.md)' for n in norm)
nav='<!-- '+LABEL+' -->\n### 2026-11-01 两小cubic目标实际终态：132样本UNKNOWN，360单细分全NO\n\nExoo132→134三cut/repair/相邻helpers的10000distinct中9997先helper132R6失败、余3helper133失败；both0/old-labelled BFS0，联合R4/R5cover预测在样本中不支持，整族UNKNOWN并STOP。Chen360→361逐条540oldedges新rootR8全失败，首failtarget距离均9；严格排这一个source的全部单边细分，不排其它改边／source／一般3D8。其source初始numeric-upperguard误限已修，HTTP1/rawparse2/successfulbinding1、失败成本全保留。累计CPU分别1.872316415/20、3.760862073/20；0sourceD6/D8全验或oldoldBFS，不续seed/cut。152／43／Lean46、SameGoalACTIVE、旧N8/n61暂停不变。\n\n'+links+'\n\n后续仅STATE已列的(3,10)1250源只读接口／5CPU，尚未启动数值；bipartite前提待核，不在本增量另建方法节点或派发研究。\n\n'
preserved={}
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);pos=len(pre);text=text[:pos]+'\n\n'+nav+text[pos:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;text=text[:m.start()]+f'## Experiments ({int(m[1])+2})'+text[m.end():];at=text.index('\n',m.start())+1;text=text[:at]+''.join('- `exp:'+n['id']+'` — '+n['title']+(' [partial]\n' if 'UNKNOWN' in n['status'] else ' [no]\n') for n in norm)+text[at:]
 assert text[:pos]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': twoactualcubicterminalmechanisms,Exoo132to13410000sampleUNKNOWNwith9997firsthelperand3secondhelperfails/both0/oldold0;Chen360to361all540singleedge subdivisions exactNO/newrootdistance9/oldold0. Sourcegate andperedge/sample stages merged,formatguardfailure androotcorrected132 reporting preserved. No source/BFS/solver/Lean/remote rerun,counts152/43/46 unchanged,oldn61paused,sameGoalACTIVE,human15celltopblock preserved. Readonly1250futurepointer is not a newexperiment or launchedplan.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==436 and {k:after[k] for k in keys}==counts
receipt=dict(status='PASS_TWO_SMALL_CUBIC_TERMINALS_MINIMAL_CANONICAL_DELTA',updated_UTC=NOW,records_before=before,records_after=436,records_added=2,new_experiment_ids=ids,ledger_rows=str(rawpath.relative_to(R)),Exoo132_sample_UNKNOWN_not_family_NO=True,Chen360_all540_single_subdivision_NO_only_fixed_source=True,sourcegates_peredge_samples_not_separatemethods=True,failed_candidates_count_as_new_graphs=False,rootcorrected132_reporting_template_recorded=True,Chen360_format_failure_costs_preserved=True,human15cell_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,counts_unchanged=counts,graph_parameter_Lean_method_increments=[0,0,0,0],same_Goal='ACTIVE',old_N8_n61='PAUSED',future1250_readonly_pointer_only_no_method_or_execution=True,source_BFS_solver_Lean_remote_hash_runs=0,root_STATE_REPORT_progress_HTML_frozen_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
