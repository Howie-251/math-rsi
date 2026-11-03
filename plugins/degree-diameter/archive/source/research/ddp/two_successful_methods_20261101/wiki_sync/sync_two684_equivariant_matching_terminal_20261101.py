"""One mechanism-level node for shared and full equivariant matching terminals."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='TWO684_EQUIVARIANT_MATCHING_TERMINAL_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(p,names):
    a=[p+n for n in names];assert all((R/x).is_file()for x in a);return a
P=S+'stale_record_transfer_d8D4/two684_shift_matching1368/'
root,shared,full,ft,history=read(P+'ROOT_DISPOSITION.json'),read(P+'RUN_RESULT.json'),read(P+'FULL_RESULT.json'),read(P+'FULL_TERMINAL.json'),read(P+'HISTORY_SOURCE_GATE.json')
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_FIXED684_ALL_HLEFT_EQUIVARIANT_ONE_MATCHING_FAMILY'
assert root['all_processes_terminal'] and ft['terminal'] and ft['active_processes']==0
assert shared['parameters_completed']==342 and shared['paper_automorphism_pruned_count']==2 and shared['nonautomorphism_t_evaluated']==340
assert full['full_domain_total']==233928 and full['new_domain_total']==233586
assert full['counts']==dict(new_candidates_visited=233586,old_shared_candidates_skipped=342,new_candidates_failed=233586,hits=0,combined_slots_evaluated=233586)
assert [x['new_candidates_visited']for x in full['by_pi']]==[116622,116964]
assert full['later_slots_after_first_failure']=='NOT_TESTED' and full['unvisited_new_parameters']==0
assert full['source_raw_parse_count_this_batch']==0 and not full['old_endpoint_DP_repeated']
assert full['old_shared_candidates_retested']==0 and not shared['positive_prediction_supported'] and not full['positive_prediction_supported']
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
assert len(records)==before
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
rid='ddp-stale-d8d4-two684-all-hleft-equivariant-matchings1368-no-20261101'
assert rid not in records and not(W/'experiments'/f'{rid}.md').exists()
paths=evidence(P,['PRED.md','NOTE.md','HISTORY_SOURCE_GATE.json','TERMINAL.json','PAPER_INTERFACE.md','RUN_PRED.md','run_gate_once.py','RUN_SOURCE_LITERAL_BINDING.json','OLD_LENGTH_LE3_ENDPOINT_SETS.json','RUN_RESULT.json','RUN_TERMINAL.json','RUN_NOTE.md','ALL342_T_SLOT_RESULTS.json','ALL342_T_SLOT_SUMMARY.tsv','PAPER_EQUIVARIANT_MATCHING_DOMAIN.md','FULL_PRED.md','full_gate_once.py','FULL_RESULT.json','FULL_TERMINAL.json','FULL_NOTE.md','FULL_PER_SIGMA_MASKS.json','FULL_ALL_NEW_PARAMETERS.tsv','FINAL_NOTE.md','ROOT_DISPOSITION.json'])
paths+=evidence('research/ddp/m1_sources/',['graph_7_4_n684.txt','684_recovered_construction.json','recover_684.py','SOURCE_NOTES.md'])
raw=dict(id=rid,title='8D4两份684一匹配：全部233928个H左等变参数完整NO；共享342与独立轨道全域两预测均失败',
    family='Two-copy matching extension on a two-orbit voltage source',idea_family='idea:ddp-open-parameter-construction-20261026',
    date='2026-11-01',wiki_verdict='no',record_type='complete_fixed_host_equivariant_matching_route_exclusion',
    target_Delta=8,target_D=4,savedL=1100,baseline_date='Inherited current-main1100/2006 and cached primaryMichel684/2026-10-05;no fresh public search',
    n=dict(actual=None,hypothetical=1368),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='No1368candidate graph emitted orBFS. Complete exact cross-slot endpoint gate excludesD<=4;inherited sourceD4 gives universal candidateD<=5,so rejectedfamily members haveD5 by proof.',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=4,
    scope='OnlythefixedactualMichel684simple7regularD4two-orbitright-voltagehost. Keep two identical684copies intact,andaddoneperfectmatchingcommutingwiththecommonfreeLEFT H342action. Precisely f(h,sigma)=(h*t_sigma,pi(sigma)),pi inS2,independentt0,t1 inH342;reversecrossing usesf^-1. Complete233928parameterfamily includesold342sharedid/t0=t1;notarbitrarynon-H-equivariantmatchings,otherhosts,otheraddedconnections or general8D4.',
    outcome_class=root['status'],new_lower_bound=False,
    distance_text='初“684是Cayley”前提由实际primary纠正：星号含former672，当前684不vertex-transitive，H342左作用有两个自由轨道，源边为right h*s。保两sourcecopy全部4788旧边＋684matching得名义1368/5472/all8regular；只欠cross≤4。共享t预测失败：342全NO，t0/171为Aut棱柱D5剪枝，其余340均首0→0槽fail。不能据此排独立轨道参数；后由完整left-equivariant域与精确一cross分解正式授权全域。完整233928=旧342严格skip＋233586新案；id116622、swap116964全首0→0槽fail，后三槽NOT_TESTED，0未决/命中。首新(id,0,1)缺138坐标、firstmissing group1。第二全覆盖预测亦失败；累计2.923628479/10CPU，一sourceparse/一≤3endpointDP，full阶段0重parse/重DP/旧342重测，0图/BFS/Lean/付费。',
    lesson_and_restart_condition='STOP thisfixedhost entireH-left-equivariantone-matchingfamily. Sourceprimary correction changedtheactualsymmetryandgenerator beforecomputation. Independentt0/t1andpi were a justified changedrule that mightcomplementtwointermediate-type routes;completefactorization made a finitefull test possible. Allnewcases stillfailthefirstcrossslot,notan aggregatebadpairscore. Do notextendtoarbitrarymatching/anotherhost/field/morecrossedges automatically. Nextrootpriority is read-only inspection of theexisting(5,3)GQpairingUNKNOWN actualinterface,notresumingitsoldtimer or runningfull3cut/othermatchingsearch.',
    restart_condition='Anotheropenparameter or a materiallynewroute-generatinginterface with a concrete bounded question. TheexistingGQpairingUNKNOWN may be read for itsactualscope;no numeric continuation authorized here.',
    unclosed_gap='Arbitrarynon-H-equivariantmatchings,otherhosts,differentaddedconnections and generalN(8,4) remain open. Source is public reproduction,auxiliaryendpoint gates do not produce newgraph/parameter/Lean/method results.',
    other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
        Moore_bound=3201,baseline=1100,Moore_space=2101,Moore_space_is_not_constructibility=True,
        hypothetical_order=1368,hypothetical_edges=5472,hypothetical_degree=8,hypothetical_main_margin_if_legal=268,
        source_name='Michel_684',source_author='Michel de Messieres',source_communication_date='2026-10-05',
        source_n=684,source_m=2394,source_degree=7,source_D4_inherited=True,source_public_reproduction_newgraph_increment=0,
        initial_Cayley_assumption_refuted=True,current684_Cayley=False,main_star_also_refers_to_former672=True,
        source_group_order=342,source_free_left_orbits=2,source_forward_edge='h*s,rightvoltage',
        actual_group_recipe=history['actual_recipe'],matching_domain='S2 x H342 x H342',
        matching='(h,sigma,0)--(h*t_sigma,pi(sigma),1)',inverse_crossing='f^-1;no conditiont1=t0^-1',
        all_sourcecopy_edges_retained=4788,matching_edges=684,
        exact_cross_gate='one crossing plus oldlegs total<=3;for all4typeslots OR ofindependent meetingtype0/1 masks equalsall342',
        three_cross_paths_reduce_by_consecutive_inverse_cancellation=True,
        shared_domain=342,shared_aut_pruned_labels=[0,171],shared_nonautomorphism_first00_failures=340,
        shared_positive_prediction_supported=False,shared_stage_CPU_seconds=1.846522801,
        complete_equivariant_domain=233928,old_shared_skipped=342,new_parameters_complete=233586,
        pi_id_new=116622,pi_swap_new=116964,new_parameters_failed_first_slot=[0,0],
        firstslot_evaluations=233586,later_three_slots='NOT_TESTED_AFTER_FIRST_FAILURE',
        unvisited_parameters=0,full_positive_prediction_supported=False,first_new_failure=full['first_failure'],
        source_raw_parses_total=1,old_le3_endpoint_DP_generations=1,full_stage_source_parses=0,
        full_stage_old_DP_repeated=False,shared_parameters_retested=0,
        candidate_graphs_generated=0,source_or_candidate_BFS=0,Lean_paidreview_runs=0,
        wholecase_CPU_seconds=root['wholecase_CPU_seconds'],CPU_budget_seconds=10,
        complete_fixed_family_exclusion=True,all_processes_terminal=True,
        next_readonly_priority='(5,3)existingGQpairingUNKNOWN actualinterface;nooldtimerresume'),evidence_paths=paths)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date']
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):c['write_node'](n)
records[rid]=n;L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 两684copy的一匹配H等变完整域终态（一个实验节点）\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n共享342与依据新独立轨道互补/完整factorization授权的全233928合一机制节点。两正预测均被推翻；新233586案全首0→0槽fail，其他3槽未测，0未决。只排fixedhost/H-left-equivariantmatchings，不排allmatching/general8D4。0图/参数/Lean/独立方法，153/43/47及savedmain105/4/global0不变。下一仅优先读既有(5,3)GQ配对UNKNOWN实际接口，不恢复旧timer/全3cut/任意matching。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新终态：两684copy全部H左等变匹配233928案NO\n\n初Cayley前提已由primary纠正：当前Michel684为两个H342自由左轨道，源边right h*s，星号兼指former672。保两7regular旧图再各加一matching余度本可得1368/5472/8regular。共享342全NO（2Aut棱柱剪枝＋340首0→0槽fail）后，依据独立t0/t1路线互补及精确factorization正式放宽到π∈S2,t0/t1∈H342完整233928域；逆跨边用f^-1，不强迫t1=t0^-1。\n\nfull严格跳旧342，新233586全部完成：id116622、swap116964全首0→0跨槽fail，后3槽NOT_TESTED；首新(id,0,1)漏138坐标/firstmissing1。两个“存在全覆盖”预测均失败，0未决/图/BFS/sourceD4重验，full0sourceparse/旧endpointDP重算；累计2.923628479/10CPU。停止此fixedhost/allH-left-equivariant一匹配族，不外推任意matching/其他host/general8D4，不自动匹配/field梯。\n\n下一优先只读(5,3)现有GQ配对UNKNOWN的actual接口，不恢复旧timer/全3cut或任意匹配。'+str(before+1)+'条记录（非方法）；153图／43参数／Lean47、savedmain105/4/global0不变，15格人工顶部、sameGoal ACTIVE及旧N8/n61暂停保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
    if fn=='index.md':
        m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m
        text=text[:m.start()]+f'## Experiments ({int(m[1])+1})'+text[m.end():];pos=text.index('\n',m.start())+1
        text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
    assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': onecanonicalmechanismnode;actual684twoorbitnonCayleyprimarycorrection,right-h*s,shared342NOthenrootauthorizedcompleteS2xH342xH342domain233928NOwith233586newfirst00failandold342skipped,other3slotsNOT_TESTED. Bothpositivepredictionsrefuted;fixedH-equivariantnotallmatching/general8D4. Case2.923628479/10CPU,no sourceDP/BFS/graph/Lean/paidrerun. Human15oldcells top preserved;counts153/43/47unchanged,nextonlyreadold5D3GQpairUNKNOWNinterface,nooldtimerresume/fullrebuild.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before+1 and {k:after[k]for k in keys}==counts
receipt=dict(status='PASS_ONE_CANONICAL_TWO684_EQUIVARIANT_MATCHING_TERMINAL_NODE',updated_UTC=NOW,
    records_before=before,records_after=before+1,records_added=1,new_experiment_id=rid,
    graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
    initial_Cayley_assumption_corrected_from_primary=True,source_actual_two_orbits=True,
    shared342_and_full233928_merged_one_node=True,new233586_complete=True,old342_strictly_skipped=True,
    new_parameters_all_first00_fail=True,later_three_slots='NOT_TESTED',unresolved_parameters=0,
    both_positive_predictions_supported=False,fixed_H_equivariant_family_only_not_all_matchings=True,
    wholecase_CPU_seconds=2.923628479,wholecase_CPU_cap_seconds=10,
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    numeric_source_graph_BFS_Lean_solver_paidreview_hash_runs=0,
    root_STATE_HTML_REPORT_recovery_builder_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,
    sameGoal='ACTIVE',old_N8_n61='PAUSED',CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
