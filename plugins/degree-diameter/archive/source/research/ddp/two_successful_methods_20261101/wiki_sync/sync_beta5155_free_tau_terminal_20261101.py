"""One canonical node for new free-tau domain and paper inverse-action transport."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,csv,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir());W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync';LABEL='D6D9_BETA5155_FREE_TAU_TERMINAL_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
P=S+'stale_record_transfer_d6D9/source_interface/shared_tau5155_pilot/'
a=read(P+'RESULT.json');t=read(P+'TERMINAL.json')
assert a['status']=='COMPLETE_NO_BETA5155_ALL_NORMAL_TRANSLATIONS_D9'
assert a['new_projective_representatives']==a['new_representatives_rejected']==6959 and a['new_representatives_unresolved']==0
assert a['prediction_phase0_supported'] and a['phase0_actual']['phase0_survivor_count']==2302
assert not a['hit'] and not a['time_cap_reached'] and a['literal_edges_written']==0
assert not a['inherited_tau1512_recomputed'] and not a['zero_branch_graph_generated']
assert t['all_processes_terminal'] and not t['running']
with (R/P/'PHASE_PROGRESS.csv').open() as f:progress=list(csv.DictReader(f))
assert [int(x['survivors']) for x in progress]==[2302,584,220,64,21,11,6,4,3,2,1,0]
assert a['representative_phase_evaluations']==10177
paper=(R/P/'PAPER_DOMAIN.md').read_text();assert 'τ*r^(-9)' in paper and 'remaining40' in paper
oldid='ddp-current331387-normalized-f6959-all42-embeddings-6d9-20261028'
rid='ddp-stale-d6d9-beta5155-free-tau-complete-inverse-action-20261101'
paths=[P+n for n in ['PRED.md','NOTE.md','PAPER_DOMAIN.md','RESULT.json','TERMINAL.json','PHASE0_RESULT.json','PHASE_PROGRESS.csv','REPRESENTATIVE_STATUS.csv','FORM_COUNTS.csv','FORM_SCHEMA.json','run.cpp','run_once.py']]
paths += [S+'stale_record_transfer_d6D9/source_interface/NEXT_SHARED_TRANSLATION_SCOPE.md','research/ddp/more_graphs_20261027/d6_D9_current331387_source/ANALYSIS_GAUGE_PROOF.md','research/ddp/more_graphs_20261027/d6_D9_current331387_source/field6959_all_embeddings/REPORT.md','research/ddp/more_graphs_20261027/d6_D9_current331387_source/field6959_all_embeddings/EXECUTION_MODEL.json']
assert all((R/p).is_file() for p in paths)
row=dict(id=rid,title='6D9固定β5155自由τ全域NO：2302案修复phase0却全失其它phase，逆action仅纸面传输不双计',family='semidirect Cayley shared-translation routing',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',record_type='necessary_route_parameter_image_gate',target_Delta=6,target_D=9,savedL=331387,baseline_date='2026-11-01 current main; oldsource and fixed1512 controls inherited',n=dict(actual=None,hypothetical=340991),actual_graph_Delta=None,actual_D=None,actual_D_scope='No target graph/BFS; complete projective parameter domain rejected by actual missing phase images',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=9,
 scope=a['exact_scope']+' Numeric action5155 only,6959new representatives; inherited1512NO plus disconnectedzero complete this action. Paper isomorphism transports fullfamily to5155 inverse;remaining40primitiveactions free-tau domains,otherfields/phases/Cayleysets are not excluded.',outcome_class=a['status'],new_lower_bound=False,
 distance_text='旧42controls仅固定τ1512，不能冒全部τ。本轮真正改变translation自由度：normal三元经conjugation置A0、scale为P1+zero；skip旧1512和zero，实际6958 finiteτ加infinity共6959新代表。phase0有2302survivors，故“能修复旧returnfiber”预测supported；phase1..11依次余584/220/64/21/11/6/4/3/2/1/0，所有代表都有实际failedphase/missingresidue。infinity phase0仅6085/6959、firstmiss18。10177rep-phase评估，非每代表49phase全算；一个failedphase已足以严格排该参数。0图/BFS。',
 lesson_and_restart_condition='STOP fixedF6959,phases1/36/45,beta5155 allnormaltranslations and its inverseaction by same-family paper transport. Do not rerun old1512,zero,secondbeta/field or bad-pair hillclimb. Remaining40actions freeτ are open here,not automatically authorized; no general6D9 nonexistence claim.',
 restart_condition='A separately authorized genuinely changed scope; this complete action family and its inverse are closed, not an invitation to an action/field ladder.',unclosed_gap='Remaining40 primitiveactions free-normal domains and other connection sets/general(6,9) are outside this result.',
 metrics_raw='RIGHT law(j,n)(a,c)=(j+a,n*r^a+c); appending a dart updates homogeneous coefficientsL_new=r^a*L_old+d_dart, inverse coefficients−r^(−a)d_pos. Constantcoordinate gaugeY=n+d givesc_new=c+(1−r^a)d; pureY=n+r^j*d is only a symmetry. Complete inverse-word sets satisfyU_−j=−r^(−j)U_j, so25phases could certify a positive, but the negative result needs only each representative oneactual missingphase. Paper transport:phi(j,n)=(-j,n):G_r→G_(r^-1). Inverse imagepositive gives(a,−c*r^(−a)); globalnormal scale−r^36 normalizesB1 and sendsτ→τ*r^(−9). Infinity/zero staytheir projective classes. Complete r family mapsbijectively to inverseaction; inherited1512 maps to1512*r^−9,not in general to target1512. No inverseaction numerics were run.',
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,Moore_bound=2929687,located_baseline=331387,Moore_space=2598300,Moore_gap_is_only_upper_bound_slack=True,hypothetical_target=340991,hypothetical_margin_if_legal=9604,
 field=6959,phase_modulus=49,fixed_positive_phases=[1,36,45],actual_numeric_beta=5155,actual_numeric_actions=1,new_projective_representatives=6959,new_finite_tau_representatives=6958,infinity_included=True,inherited_tau1512_recomputed=False,zero_paper_disconnected=True,
 raw_NB_words_generated_once=a['raw_NB_words_generated_once'],distinct_phase_coefficient_forms=a['distinct_phase_coefficient_forms'],representative_phase_evaluations=10177,phase_survivor_counts=[int(x['survivors']) for x in progress],phase_progress=progress,new_representatives_rejected=6959,new_representatives_unresolved=0,complete_parameter_domain=True,every_representative_has_failed_phase=True,all49phases_per_representative_tested=False,
 phase0_prediction_supported=True,phase0_summary={k:v for k,v in a['phase0_actual'].items() if k!='survivors'},infinity_phase0_image=6085,infinity_first_miss=18,
 inverse_action_transport=dict(status='PAPER_ONLY_SAME_FAMILY_ISOMORPHISM',action='r^-1 forr5155;numericvalue notcomputed',tau_map='tau*r^-9',infinity_and_zero_included=True,requires_complete_r_domain_including_inherited1512=True,actual_additional_numeric_actions=0,full_tau_actions_closed_by_numeric_plus_paper=2,remaining_primitive_actions_free_tau_open=40),
 older_all42_scope='all42actions at literalnormal1512 only;unchangedvalid closed scope',older_all42_node=oldid,
 cumulative_charged_CPU_seconds=t['cumulative_charged_CPU_seconds'],CPU_budget_seconds=20,prior_case_charge=t['prior_case_CPU_seconds'],preparation_charge=t['new_preparation_charge_seconds'],compile_CPU=t['actual_compile_CPU_seconds'],run_child_CPU=t['actual_run_child_CPU_seconds'],no_timer_reset=True,
 source_graph_fieldlaw_BFS_rechecks=0,target_graph_BFS=0,solver_Lean_remote_runs=0,terminal=True),evidence_paths=paths)
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];assert before==430
existing={x['id']:x for x in L['rows']};assert len(existing)==before and rid not in existing and oldid in existing and not(W/'experiments'/f'{rid}.md').exists()
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs'];counts={k:L[k] for k in keys};assert tuple(counts[k] for k in keys[:3])==(152,43,46)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 txt=(W/fn).read_text();assert txt.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and END in txt and LABEL not in txt;prefix[fn]=txt[:txt.index(END)+len(END)]
mdpath=W/'DDP_METHOD_LEDGER.md';assert LABEL not in mdpath.read_text()
oldnode=W/'experiments'/f'{oldid}.md';oldtext=oldnode.read_text();assert LABEL not in oldtext
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper'];helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
n=c['normalize'](row);n['goal']['baseline_date']=row['baseline_date']
with (OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):c['write_node'](n)
# Preserve the full original all42/fixed1512 text and add only a later-scope pointer.
oldnode.write_text(oldtext+'\n\n<!-- '+LABEL+' -->\n## 后续自由translation范围（2026-11-01，旧1512结论原文保留）\n\n以上all42结果严格固定normalratio1512，仍然有效；不能解释成全部τ已关。后续只对β5155实际穷尽6959个新P1代表，连继承1512与zero排完整normal域；纸面同构传到其逆action，未执行第二action。其余40primitiveactions的freeτ仍开放。见[完整新域与纸面传输]('+rid+'.md)。无图/BFS或独立新方法计数。\n')
update=dict(path='research-wiki/experiments/'+rid+'.md',date='2026-11-01',note='Later free-normal domaincompleteNO only forbeta5155, inverseactionpapertransport;originalall42/fixed1512scope preserved.')
oldrow=existing[oldid];oldrow.setdefault('other_metrics',{}).setdefault('later_scope_updates',[]).append(update);oldrow['source_record'].setdefault('other_metrics',{}).setdefault('later_scope_updates',[]).append(copy.deepcopy(update))
existing[rid]=n;L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+paths[0]+') |'
md=mdpath.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,'本页有431条记录；不以此宣称431种独立方法。',1);md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 最后自由τ域终态及逆action纸面传输\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n实际只有1action/6959新代表；r^-1同构传输不是第二数值run，不翻倍计实验或方法。旧all42/fixed1512原结论保留；图／参数／Lean增量0。\n';mdpath.write_text(md)
nav='<!-- '+LABEL+' -->\n### 2026-11-01 最后终态：β5155自由τ全域NO，逆action仅纸面传输\n\n新normal自由度有真实反馈：phase0的2302案过必要门，继而phase1..11剩584／220／64／21／11／6／4／3／2／1／0，6959新代表每案已有实际缺失phase，0unresolved。含旧1512与zero后关闭β5155完整normal域；同构τ→τr^-9覆盖r^-1族，未跑第二action，其余40primitiveactions freeτ仍开放。累计4.805153994/20CPU，0图/BFS，不继续β／field梯。旧all42只关fixed1512而非所有τ，原文保留。152／43／Lean46不变。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;text=text[:m.start()]+f'## Experiments ({int(m[1])+1})'+text[m.end():];pos=text.index('\n',m.start())+1;text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': onecanonicalnode foractualbeta5155 freeP1 normaldomain completeNO6959new reps;phase0prediction supported2302 butallfailbyphase11,0unresolved,0graphBFS. Same-node paper r→r^-1, tau→tau*r^-9 transport, nosecondnumeric action or doubledcount;remaining40free-tau actionsopen. Oldall42fixed1512text intact+backlink. No source/field/solver/Lean/review rerun;human top preserved,152/43/46 unchanged.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==431 and {k:after[k] for k in keys}==counts
receipt=dict(status='PASS_ONE_CANONICAL_FREE_TAU_TERMINAL_NODE_WITH_PAPER_TRANSPORT',updated_UTC=NOW,records_before=before,records_after=431,records_added=1,new_experiment_id=rid,old_all42_fixed1512_original_text_preserved=True,old_node_later_scope_backlink=True,actual_numeric_actions=1,actual_new_representatives=6959,inverse_action_isomorphism_paper_only=True,remaining_free_tau_primitive_actions_open=40,human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,counts_unchanged=counts,graph_parameter_Lean_method_increments=[0,0,0,0],source_BFS_field_solver_Lean_remote_hash_runs=0,root_STATE_REPORT_progress_HTML_frozen_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
