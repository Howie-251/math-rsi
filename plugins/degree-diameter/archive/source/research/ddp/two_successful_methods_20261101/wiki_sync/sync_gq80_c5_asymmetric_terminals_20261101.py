"""Upsert the existing GQ80 node;full family remains UNKNOWN."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='GQ80_C5_ASYMMETRIC_TERMINALS_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rid='ddp-wave11-gq80-paired-matchings'
def read(p):return json.loads((R/p).read_text())
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
assert rid in records and len(records)==before
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
P=S+'stale_record_transfer_d5D3/gq80_paired_matching_intuition/'
root,c5,asym=read(P+'ROOT_DISPOSITION.json'),read(P+'C5_ROOT_DISPOSITION.json'),read(P+'ASYM_ROOT_DISPOSITION.json')
assert root['status']=='GQ80_INTUITION_ROUND_TERMINAL_C5_COMPLETE_NO_FIXED_Q_RAW_UNSAT_FULL_FAMILY_UNKNOWN'
assert root['all_new_numeric_processes_terminal'] and root['unrestricted_family_status']=='UNKNOWN'
assert c5['status']=='ROOT_ACCEPTED_COMPLETE_NO_COMMON_SYMPLECTIC_C5_EQUIVARIANT_GQ80_PAIRED_MATCHINGS'
assert c5['joint_domain_implicit']==4306640625 and c5['all_P_queries_empty']==10769
assert c5['all_near_blocks_retained']==[44,44] and not c5['girth5_restriction']
assert asym['status']=='ROOT_ACCEPTED_REVIEWED_FIXED_Q1361_PFREE_RAW_SOLVER_UNSAT_NOT_FORMAL_CERTIFICATE'
assert asym['valid_search_calls']==1 and asym['solver_return_code']==20 and not asym['UNSAT_proof_logged_or_checked']
assert asym['Q_selected']==1361 and asym['other_Q_family']=='UNKNOWN_NOT_TESTED' and asym['all_processes_terminal']
raw=copy.deepcopy(records[rid]['source_record']);m=raw['other_metrics']
m['historical_five_window_checkpoint']=dict(title=raw['title'],status=raw['outcome_class'],scope=raw['scope'],
    distance_text=raw['distance_text'],all_five_UNKNOWN_no_incumbent=True,recorded_windows=5)
m['gq80_intuition_round_C5']=dict(status=c5['status'],actual_action='commonorder5symplecticcollineation',
    source='InheritedW3F3incidence80/160,40P+40L',all160incidenceedges_retained=True,
    source_orbits_per_side=[8,5],compressed_matching_blocks=280,degree_equalities=16,farorbit_cover_rows=216,
    complete_near_blocks_retained=[44,44],girth5_restriction=False,
    side_complete_matching_counts=[65625,65625],side_max_coverage=[114,113],
    predicted_maxsum_below216=True,prediction_refuted_by_sum227=True,
    first_argmax_union=158,first_argmax_overlap=69,first_argmax_is_jointoptimum=False,
    complete_implicit_joint_domain=4306640625,P_capacity_threshold=103,Q_capacity_threshold=102,
    P_pruned=54856,P_eligible_all_queried=10769,Q_pruned=50427,Q_eligible=15198,
    all_P_membership_intersections_empty=10769,membership_AND_steps=78098,
    explicit_four_billion_pair_iterations=0,complete_common_C5_NO=True,
    Sylow_conjugacy_scope='Allorder5subgroupsinsideSp4(F3),transportedbyincidencepreservingconjugation;notWLOGforarbitrarymatchings',
    solver_calls=0,source_candidate_BFS=0,wholecase_CPU_seconds=3.272020095,case_CPU_cap_seconds=10,terminal=True)
m['gq80_changed_fixedQ_Pfree_terminal']=dict(status=asym['status'],
    changed_rule='FixoneC5lineQ,allowarbitrarypointPincludingnear,collinearchoices;excludePcommutingwithsameC5usingacceptedcommonC5NO',
    Q_profile_domain=65625,Q_profile_eligible=41064,
    Q_profile_necessary='i_Q(L)<=3forlines,j_Q(p)<=1forpoints;full-validi+3j<=3,nogirthassumption',
    deterministic_selection='maxcoverage_thenminimumoldindexamongeligibleQ',Q_index=1361,Q_coverage=113,Q_concurrent_triangles=5,
    all_P_pair_variables=780,P_variables_not_explicitly_unit_false=330,original_matching_equalities=40,
    remaining_original_far_clauses=515,CNF_variables=9750,CNF_clauses=51436,
    actual_legal_solver_calls=1,argv_time_arguments=['-t','19'],return_code=20,actual_stdout='s UNSATISFIABLE',
    solver_conflicts=18,solver_decisions=87,actual_solver_CPU_seconds=.016967,
    startup_failures_preserved=asym['startup_failures_preserved'],startup_failures_were_searches=False,
    UNSAT_proof_logged_or_checked=False,formal_certified_fixedQ_exclusion=False,
    raw_solver_claim_only_this_fixedQ=True,other_Q_status='UNKNOWN_NOT_TESTED',full_paired_family='UNKNOWN',
    Q_reselected=False,CNF_rebuilt_after_launch_errors=False,source_geometry_BFS_repeated=False,
    cumulative_case_CPU_seconds=4.886162516,case_CPU_cap_seconds=30,
    no_Q2_newaction_newtimer_or_second_search=True,all_processes_terminal=True)
m.update(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
    old_five_windows_all_UNKNOWN=True,unrestricted_GQ80_family_status='UNKNOWN',
    no_target_candidate_or_distance_graph_saved=True,actual_badpairs=None,
    graph_BFS_count_all_windows=0,incumbents_all_recorded_windows=0,
    production_calls_all_recorded_windows=6,production_CNF_calls_all_recorded_windows=4,
    new_legal_search_calls=1,new_unsearched_startup_failures=2,
    local_Q_line_paused=True,all_current_numeric_processes_terminal=True,
    wholecase_CPU_seconds=4.886162516,wholecase_CPU_cap_seconds=30,
    current_round_newly_tested_shortlist_cell=[5,3],current_round_shortlist_cells_actually_tested=11)
raw.update(title='GQ80配对：共同symplecticC5族完整NO；单Q1361/P自由raw UNSAT；任意双匹配族仍UNKNOWN',
    wiki_verdict='partial',record_type='existing_paired_matching_mechanism_scope_refinements',
    outcome_class='FULL_GQ80_UNKNOWN_COMMON_C5_COMPLETE_NO_FIXED_Q1361_RAW_UNSAT_ONLY',
    scope='Retainall160incidenceedgesofactualW(3,3)40P+40L,andaddoneperfectmatchingeachside. Original1560-binary/80matching/1080far-clausefamily remainsUNKNOWNafterfiveoldwindows. NewscopeA:bothmatchingscommutewithacommonactualSp4(F3)C5action,all65625x65625pairsexcludedbycompletefinitejoin;SylowconjugacyonlytransferswithincommonsymplecticC5family,notWLOGforallmatchings. NewscopeB:singleprofile-selectedQ1361,arbitraryPincludingcollinearchoicessubjecttofull-validcuts,andnon-C5boundary justifiedbyscopeA;onelegalrawUNSATwithoutlogged/checkedproof. Nocertifiedall-Q/fullfamilyNO,nogirth5restrictioninnewscopes.',
    actual_D_scope='No80/200targetcandidate,distancegraph,BFSorordinarybadpairmeasure. C5completefinitecombinatorialNO;fixedQrawsolverUNSATisnotformalcertificate;fulltemplateUNKNOWN.',
    distance_text='旧五窗原MIP/overlapMIP/directCNF/girth5CNF/localbudgetCNF全部UNKNOWN且无incumbent，原1560变量/80matching等式/1080far41literal为D3充要，非只有必要筛选。新共同C5action实际绑定40P/40L各8×5循环与160incidence，280blocks/16degreeeq/216farorbit行，44+44nearblocks保留、不假设girth5。第一容量不足预测被114+113=227≥216推翻；两首argmax并集158/overlap69不是jointopt。继而完整join：侧各65625，严格容量筛P≥103/Q≥102后10769P/15198Q，全部membership交集为空，隐式覆盖4306640625组合而非逐4.3b枚举，commonSp4-C5族完整NO。再据此改变规则：从41064合法Qprofile中唯一确定Q1361/coverage113/5triangles，P可破C5且含全部780pointpairs，validcuts后330未被unitfalse；515剩余原far行，CNF9750/51436。两启动/CLI错误未search且成本保留，唯一合法-t 19调用实际exit20/s UNSATISFIABLE、18conflicts87decisions、child.016967CPU，无UNSATproof。故只记此Q的rawUNSAT，不排otherQ或fullfamily。累计4.886162516/30CPU，0图/BFS/重复geometry。',
    lesson_and_restart_condition='PauseGQlocalfixedQline andstopallcommonC5action/sideenum/jointrepeats,Q2,newaction/newsolver/timer. Capacitymargin alone didnot ensurecompatiblejoint routes,firstargmax wasnota globaljointoptimum,andremovingP symmetrywasagenuinechangedrule. Preserve the distinction C5completefiniteNO versus oneQrawUNSAT versus unrestrictedUNKNOWN. Nextrootquestion isread-only6D9three-cut6starjoint-newoldinterface;do not reviveoldsourcesingle-subdivisionorF6959normalfamilyNO,or branch a third independenttemplate here.',
    restart_condition='A newconcrete structural reason outside stoppedcommonC5/singleQ1361 scopes,with a newboundeddecision;oldUNKNOWN alone doesnotauthorizecontinuingits timer.',
    unclosed_gap='OtherfixedQ/freePchoices,arbitrarypairedmatchingsandgeneralN(5,3)remainUNKNOWN;fixedQ1361hasrawUNSATonly,noformalproof.0acceptedtargetgraph/parameter/Lean;GoalACTIVE.')
raw.setdefault('positive_guarantees',[]).extend([
    'The newcommonC5compressedORrows exactlyfoldallfiveoldfarrowsineachorbit;nearblocksretained,notgirth5only.',
    'The completefinitejoin excludesallcommonSp4(F3)C5pairedmatchings,includingconjugateC5subgroups,butdoesnotmakeC5invarianceWLOG.',
    'ForfixedQ1361,the780P-variable residual,full-valid78/6inputcutsandexistentialnoninvariancewitnesses are exact withinthatscope;onelegalrawUNSATisnotacheckedUNSATcertificate.'
])
newnames=['PRED.md','NOTE.md','HISTORY_SOURCE_GATE.json','SCOPE_ATTACK.md','PAPER_INTERFACE.md','C5_PRED.md','c5_once.py','C5_ACTION_SEARCH_TRIALS.json','C5_ACTION_AND_BINDING.json','C5_COMPRESSED_EXACT_MODEL.json','C5_SIDE_CAPACITY_AND_ARGMAX.json','C5_POINT_MATCHINGS.tsv','C5_LINE_MATCHINGS.tsv','C5_RESULT.json','C5_TERMINAL.json','C5_NOTE.md','PAPER_C5_COVERAGE_FACTOR.md','JOINT_PRED.md','joint_once.py','JOINT_DOMAIN.json','JOINT_Q_MEMBERSHIP.json','JOINT_ALL_P_STAGES.tsv','JOINT_RESULT.json','JOINT_TERMINAL.json','JOINT_NOTE.md','PAPER_C5_JOINT_GATE.md','FINAL_PROOF.md','C5_ROOT_DISPOSITION.json','ASYM_PRED.md','asym_once.py','ASYM_Q_BLOCK_PROFILES.json','ASYM_ALL_Q_PROFILE_GATE.tsv','ASYM_Q_SELECTION.json','ASYM_FIXED_Q.json','ASYM_MODEL.json','ASYM_FIXED_Q_PFREE.cnf','ASYM_INITIAL_LAUNCH_FAILURE_RESULT.json','ASYM_COMMAND_FORMAT_FAILURE_RESULT.json','ASYM_COMMAND_FORMAT_FAILURE.stderr','ASYM_COMMAND_FORMAT_FAILURE.stdout','asym_solver_actual_once.py','ASYM_ACTUAL_EXECUTION.json','ASYM_ACTUAL_SOLVER.stdout','ASYM_ACTUAL_SOLVER.stderr','ASYM_SOLVER_RESULT.json','ASYM_SOLVER_TERMINAL.json','ASYM_RESULT.json','ASYM_TERMINAL.json','ASYM_NOTE.md','PAPER_ASYMMETRIC_QFIX_INTERFACE.md','ASYM_ROOT_DISPOSITION.json','ROOT_DISPOSITION.json']
newpaths=[P+n for n in newnames];assert all((R/x).is_file()for x in newpaths)
raw['evidence_paths'].extend(x for x in newpaths if x not in raw['evidence_paths'])
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date']
assert n['id']==rid
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):c['write_node'](n)
assert re.search(r'^verdict: partial$',(W/'experiments'/f'{rid}.md').read_text(),re.M)
records[rid]=n;L.update(rows=list(records.values()),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+newpaths[-1]+') |'
mp=W/'DDP_METHOD_LEDGER.md';lines=mp.read_text().splitlines();ix=[i for i,line in enumerate(lines)if line.startswith('| [')and'(experiments/'+rid+'.md)'in line];assert len(ix)==1;lines[ix[0]]=table
md='\n'.join(lines)+'\n';md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' GQ80既有机制原位进展：C5有限NO／固定Q rawUNSAT／全文族UNKNOWN\n\n不新增节点或方法。完整common-symplecticC5 join隐式覆盖65625²、全部10769eligibleP的Q-membership交集为空；近端块保留，非girth5局部结论。固定Q1361/freeP是改变规则的一次窗口，合法exit20 rawUNSAT，无prooflog/check；两启动失败不算search且成本保留。其余Q/原五窗/任意双匹配仍UNKNOWN，verdict保持partial。总4.886162516/30CPU，0图/BFS/重复geometry。暂停Q线、不Q2/新action/旧timer，下一仅6D9三cut六星只读接口。442记录及153/43/47、savedmain105/4/global0保持。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' GQ80同机制终态：共同C5完整NO，唯一Q1361 rawUNSAT，任意双匹配仍UNKNOWN\n\n原五窗均UNKNOWN/无候选保留。新C5保44+44nearblocks，容量不足预测被max114+113=227推翻；首argmax并158/overlap69不是jointopt。完整join隐式覆盖65625²=4306640625，经必要容量筛10769P/15198Q全部membership交集空，commonSp4(F3)C5族严格NO（含Sylow共轭），不使C5成为WLOG、不排fullpaired模型。\n\n实际改变规则：按validi_Q≤3/j_Q≤1筛41064Q后唯一选maxcoverage/minindex的Q1361，coverage113/含5triangles；P任意可破C5，780Pvars/330未unitfalse、515剩余原farclauses、CNF9750/51436。两未search启动/CLI失败保留；唯一合法-t19调用实际exit20、s UNSATISFIABLE、18conflicts87decisions、child.016967CPU；无UNSATprooflog/check，只记固定Q rawsolverclaim。其他Q与任意双匹配仍UNKNOWN，不升级fullfamilyNO。累计4.886162516/30CPU，0图/BFS/旧geometry重跑；所有新进程终态。\n\n暂停此Q线，不Q2/新action/新solver/旧timer。下一root问题仅6D9三cut六星joint接口只读，不复跑旧single-subdivision/normal族，不添第三独立模板。本轮第11个老格有新实际检验而非新增图；'+str(before)+'记录不增，153图／43参数／Lean47、savedmain105/4/global0保持。人工15格顶部、sameGoal ACTIVE、旧N8/n61暂停继承。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
    if fn=='index.md':text=re.sub(r'^- `exp:'+re.escape(rid)+r'`[^\n]*','- `exp:'+rid+'` — '+n['title']+' [partial]',text,flags=re.M)
    assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': existingcanonicalGQ80upsert,no newnode/method. C5completefinitejoinNO separatefromQ1361rawsolverUNSAT(no proof logged/checked) andfullfamilyoldfiveUNKNOWN. Capacity<216predictionrefuted227,argmax158notjointopt,completejointall10769queriesempty;genuinechangedfixedQ/freePonelegalexit20,twostartupfailuresnotsearches. Nograf/BFS/geometry/solver/reviewrerun by sync;human15oldcells top preserved,442and153/43/47unchanged,verdictpartial,stopQ2/action/timer.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before and {k:after[k]for k in keys}==counts
assert next(r for r in after['rows']if r['id']==rid)['other_metrics']['unrestricted_GQ80_family_status']=='UNKNOWN'
receipt=dict(status='PASS_EXISTING_GQ80_NODE_C5_NO_ASYMMETRIC_RAW_UNSAT_FULL_UNKNOWN',updated_UTC=NOW,
    records_before=before,records_after=before,records_added=0,updated_experiment_id=rid,
    graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
    full_family_verdict='PARTIAL_UNKNOWN',old_five_UNKNOWN_windows_preserved=True,
    common_symplectic_C5_family='COMPLETE_FINITE_NO_NOT_WLOG',C5implicit_pair_domain=4306640625,
    selected_Q=1361,fixedQ_result='REVIEWED_RAW_SOLVER_UNSAT_ONLY',legal_solver_search_calls=1,
    unsearched_startup_failures_preserved=2,UNSAT_proof_logged_or_checked=False,
    other_Q_status='UNKNOWN_NOT_TESTED',case_CPU_seconds=4.886162516,case_CPU_cap_seconds=30,
    all_current_numeric_processes_terminal=True,no_Q2_newaction_oldtimer_authorized=True,
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    numerical_source_graph_BFS_Lean_solver_paidreview_hash_runs=0,
    root_STATE_HTML_REPORT_recovery_builder_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,
    sameGoal='ACTIVE',old_N8_n61='PAUSED',CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
