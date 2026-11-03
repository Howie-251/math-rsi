"""One experiment-level Combination C record. No math/solver/rebuild rerun."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';ST='research/ddp/two_successful_methods_20261101/'
OUT=R/ST/'wiki_sync';LABEL='COMBINATION_C_CURRENT16416_TERMINALS_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=ST+'retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/'
A=P+'available_pin_extension16417/';C=P+'cooperative_fourblocker_repair16417/'
S=A+'source_neighborhood_seed_cover/';D=S+'direct_sat_atmost5/'
rid='ddp-d16d4-current16416-combination-c-cover-cooperative-seeded-sat-terminal-20261101'
def read(p):return json.loads((R/p).read_text())
available=read(A+'RESULT.json');coop=read(C+'RESULT.json');k5=read(C+'K5_RELAXATION_POSTPROCESS.json')
seeded=read(S+'RESULT.json');sat=read(D+'RESULT.json')
assert available['status']=='UNKNOWN_NO_AT_MOST16_PIN_COVER_FOUND' and available['best_handchecked_cover_count']==29
assert coop['status']=='COMPLETE_NO_FIXED342_FOURBLOCKER_DONATION_ALL_MAXIMAL_HELPER_H'
assert coop['counts']['centers_complete']==342 and coop['counts']['H_evaluated']==5886
assert k5['category_counts']=={'EVEN_K5_BASE_FAIL':342,'K5_BASE_PASS_BUT_ALL_DEGREE_LEGAL_H_FAIL':0}
assert seeded['status']=='UNKNOWN_NO_AT_MOST16_SOURCE_SEEDED_COVER_FOUND' and seeded['best_total_pin_count']==21
assert seeded['templates_greedy_processed']==162 and seeded['frozen_template_v']==12312
assert sat['status']=='UNKNOWN_FIXED_V12312_SAT_NO_ATMOST5_WITNESS'
assert sat['native_comment_status']=='c UNKNOWN' and sat['native_return_code']==0
assert sat['native_stats']['conflicts']==56159 and sat['native_stats']['decisions']==204313
assert abs(sat['wholecase_CPU_seconds']-92.342922089)<1e-8
assert read(S+'ROOT_DISPOSITION.json')['at_most16_status']=='UNKNOWN_NOT_NO_NOT_OPTIMAL21'
assert read(D+'ROOT_DISPOSITION.json')['UNSAT_claim']is False
for p in [A,C,S,D]:assert read(p+'TERMINAL.json')['active_processes']==0
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
assert len(records)==before and rid not in records
assert not any('combination-c'in r['id']or'current16416-combination'in r['id']for r in L['rows'])
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances',
 'saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs',
 'pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs',
 'known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
paths=[]
def evidence(prefix,names):
 for name in names:
  p=prefix+name;assert(R/p).is_file(),p;paths.append(p)
evidence(A,['PRED.md','AVAILABLE_PIN_EXTENSION_PAPER.md','cover_child.py','run_once.py','NOTE.md',
 'ALL_AVAILABLE_PINS.json','SUPPORT_SCHEMA.json','ALL4050_CLOSED_R3_SUPPORTS.bits','ALL4050_PIN_SUPPORT_PROFILE.tsv',
 'COVER_COLUMN_MAPPING.json','GREEDY_RESULT.json','BEST_COVER_PIN_SET.json','MODEL.json','WARM_START_RETURN.json',
 'RAW_SOLUTION.json','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json'])
evidence(C,['PRED.md','COOPERATIVE_BLOCKER_REPAIR_PAPER.md','finite_child.py','run_once.py','NOTE.md',
 'IMMUTABLE_BASE_DISTANCE_SCHEMA.json','CURRENT_OLDSOURCE15552_R3.bits','ALL_VISITED_CENTER_HELPER_INTERFACES.json',
 'ALL_CAPACITY_MAXIMAL_H_DOMAINS.json','ALL_MAXIMAL_H_STAGES.tsv','ALL_FAILURE_ROUTE_DECOMPOSITIONS.jsonl',
 'HELPER_BALL_SCHEMA.json','ALL_VISITED_CASE_HELPER_B0_B3.bits','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json',
 'K5_RELAXATION_PRED.md','k5_relaxation_once.py','K5_INITIAL_SYNTAX_FAILURE.json','K5_RELAXATION_POSTPROCESS.json'])
evidence(S,['PRED.md','seed_child.py','run_once.py','NOTE.md','ALL_TEMPLATE_GREEDY_RECORDS.jsonl',
 'TEMPLATE_GREEDY_SUMMARY.json','FROZEN_TEMPLATE.json','SOLVER_PRED.md','RESIDUAL_COLUMN_ROW_MAPPING.json',
 'RESIDUAL_MODEL.json','RAW_RESIDUAL_SOLUTION.json','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json'])
evidence(D,['PRED.md','SAT_FEASIBILITY_INTERFACE_PAPER.md','run_once.py','NOTE.md',
 'FIXED_V12312_COVER_ATMOST5.cnf','CNF_MODEL.json','REAL_VARIABLE_TO_ACTUAL_PIN.json','NATIVE_EXECUTION.json',
 'SAT_STDOUT.log','SAT_STDERR.log','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json'])
raw=dict(id=rid,title='16D4 current16416组合C终态：全可用pin／seeded／SAT仍UNKNOWN，四donor固定域即使K5也NO',
 family='Combination C: one-point extension of accepted current16416 with retained or repaired clone edges',
 idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',wiki_verdict='partial',
 record_type='fixed_current_host_singlepoint_cover_and_cooperative_repair_experiment',
 target_Delta=16,target_D=4,savedL=16416,
 baseline_date='Acceptedlocalcurrent16416host;public-main16384comparisoninheritedseparately,notglobalprioritycertification',
 n=dict(actual=None,hypothetical=16417),actual_graph_Delta=None,actual_D=None,
 actual_D_scope='No16417candidategraphordiameteracceptance. C1/C3/C4returnednogated<=16coverandremainUNKNOWN;C2completeweightedNOonlyforthefixed342deterministicdonation/oldPfamily,includingK5relaxation.',
 ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=4,new_lower_bound=False,
 outcome_class='COMBINATION_C_CURRENT16416_STOP_COOP_FIXED_NO_AVAILABLE_SEEDED_SAT_UNKNOWN',
 scope='Singleconcretequestion:extendtheacceptedcomplete16416/129240max16D4hostto16417. C1all4050currentdegree<16pins/currentclosedR3,onegreedy+onewarmminsumcoverwindow;C2exact342unselectedoldsourcecenterswith4distinctblockingowners,deterministicblockededge donationtofullsourceNvnewZ,andalllegalfivehelperHcoveredbyallinclusion-maximalHplusK5relaxation;C3all162unselectedoldsourcecenterswithexact4saturatedneighbours,fixedavailableNvseed,onegreedypervthenonefrozenv12312residualMIP;C4samefrozenv/seed11/1744holes/3771residualcolumns,oneCaDiCaLatmost5decision. TheseareoneCombinationCproblemrecord,not4methodsornewgraphclaims. Stopthiscurrent16416line;notgeneral16D4NO,notallcurrenthostaugmentationsNOandnotthenonorbit15552binarypackingmodel.',
 distance_text='目标比已接受16416多1点，但本C没有16417图。全4050available（3186oldsource+864currentclones）精确currentR3已存，均考虑16416targets；greedy/warm29，唯一30sHiGHS node0/timecap未改进，≤16仍UNKNOWN。为修复满槽改四donor合作：342v、5886全部inclusion-maximalH完整失败（324helperpair/5562helper-base）；随后旧球K5放宽342仍fail/0cliquePASS，表明该fixedoldP的缺路线不是Hdegree不足，有限域严格NO。于是保全部旧边改用sourceNv设计：162个free11seed模板各greedy21，具体holes类别/每extra修复已存；冻结v12312/1744holes（含74currentclones），单20s residualMIP仍10extras、node0/timecap，21非最优证明，≤16UNKNOWN。再因MIP未branch改同一decision的SAT：22626vars/43219clauses，合法-t19一次，stdout c UNKNOWN/exit0/无s行，56159conflicts/204313decisions而无SAT或UNSAT。总92.342922089/120CPU含所有prior/prep/可见K5启动前失败，不reset；0新图/参数/Lean。',
 lesson_and_restart_condition='STOPCombinationCcurrent16416line:noadditionalavailablepinMIP,SAT,template,seed,H/S5orlocalswapladder. K5allfailurechangedtheactualnextgenerationfromdeletingcriticaldonorattachmentsbacktoretainingalloldedges;sourceNvseedthenreducedthemodelto1744actualholes. HiGHSnode0feedbackmotivatedoneactualSATdecision,whichentered204313decisionsbutremainedUNKNOWN. Thesearetestablealgorithm/routefindings,notconstructionrecords. Fullcurrenttargetcoverageandpinavailabilitywereneverreplacedbyoldsource-onlycoverage. Preserveallcacheddataforfutureboundedquestions;do notinterpretunknownasfamilyNOorunusedCPUaspermissiontocontinue.',
 restart_condition='Anewboundedquestionwithchangedstructure,hostormeaningfullynewalgorithmicreasonunderthecontinuingGoal. ThisterminaldoesnotresumeanyfixedCtimeranddoesnotclosegeneral16D4;theindependentnonorbit15552linehasitsownnode/scope.',
 unclosed_gap='Whetherany<=16availablepinsetexistsremainsUNKNOWN,includingthefixedv12312seed11/atmost5decision;rawSATwasUNKNOWN,notUNSAT. Othercenters,oldPchanges,morehelpers,oldedgechanges,otherhostsandgeneral16D4remainunexcluded. C2NOisonlytheexact342oldP/donationfamily,notarbitraryonepointconstruction. GoalACTIVE,humanfeedbackandglobalpriorityrequirementsremain;0newgraph/parameter/Lean.',
 positive_guarantees=[
  'C1usescurrentgraphdegreesandall16416targetsincluding864clones;availablebotholdsource3186andcurrentclones864. Exactsupportsandactualmappingarepersisted.',
  'C2base15552+860fullNcloneshasinheritedD4;currentstablemetricretractionjustifiescachedballs. cost2overlapandallinclusion-maximalHareincluded,notonlymaximum-edgeH.',
  'Everyoneofthe342fixedoldPcasesfailsbasecoverageevenunderdegree-ignoredcompleteK5;completeHnegativesdonotclaimglobal16D4infeasibility.',
  'C3keepsseed11andallcurrenthole rows;4050availableextrasareonlycompressedbyidenticalresidualcoverage,notrestrictedtooriginalsourceoroldgreedyset.',
  'C4positiveholeORplusprefixatmost5isexactexistentialdecisionforfixedresidual;onlyrealvarsmaptopins. NoSATwitness,checkedUNSATproof,valid16417graphornewLeanclaimresulted.'
 ],
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
  current_host=dict(n=16416,m=129240,maxdegree=16,D4_inherited=True,source_parent_graph_node='ddp-d16d4-whole27-fulln-clone864-graph16416-20261101',
   public_main_order_inherited=16384,global_priority='UNKNOWN',hypothetical_target_order=16417),
  C1_available=dict(status='UNKNOWN',available_pins=4050,oldsource_pins=3186,currentclone_pins=864,
   exact_newquestion_depth3_roots=4050,allcurrenttargets=16416,unique_columns=3798,model_nonzeros=9779328,
   greedy_and_warm_best=29,configured_single_HiGHS_seconds=30,actual_HiGHS_CPU=30.285677327,
   raw_model_status='kTimeLimit',mip_nodes=0,dual_bound=0,phase_cumulative_CPU=35.491164489),
  C2_cooperative=dict(status='COMPLETE_NO_SPECIFIED_FIXED342_RULE',centers=342,maximal_H_evaluated=5886,
   helperpair_firstfail=324,helper_to_base_firstfail=5562,
   oldsource_R3_reused=3186,new_oldsource_R3_bitset_rows=12366,new_current_R2_rows=16416,
   degree14_overlap_cost2_retained=True,all_inclusion_maximal_not_only_maximum_edge_H=True,
   raw_finite_cumulative_CPU=37.767076346,K5_even_clique_basefail=342,K5_cliquepass_degreelegalfail=0,
   K5_first_v15_helper15560_target1_prediction_supported=True,
   K5_preexecution_syntax_failure_preserved=True,K5_failure_conservative_CPU_charge=.05,
   phase_cumulative_CPU=37.985870069),
  C3_seeded=dict(status='UNKNOWN',actual_templates=162,seed_size=11,greedy_best_count_all_templates=21,
   frozen_v=12312,initialholes=1744,initialhole_oldsource=1670,initialhole_currentclones=74,
   residual_columns=3771,residual_nonzeros=1028362,seedcovered_rows_deleted=14672,
   extra_budget=5,best_extras=10,best_total=21,configured_single_HiGHS_seconds=20,
   actual_HiGHS_CPU=20.66267475,mip_nodes=0,dual_bound=0,phase_cumulative_CPU=71.065033579),
  C4_SAT=dict(status='UNKNOWN_NOT_UNSAT',fixed_v=12312,seed=11,hole_OR_clauses=1744,
   real_variables=3771,prefix_aux_variables=18855,total_variables=22626,cardinality_clauses=41475,total_clauses=43219,
   configured_argv=['-t','19','FIXED_V12312_COVER_ATMOST5.cnf'],native_calls=1,
   raw_native_comment='c UNKNOWN',formal_s_status_line=None,native_return_code=0,
   conflicts=56159,decisions=204313,propagations=44480436,native_CPU_seconds=19.009266,
   parent_CPU_seconds=1.768622510,proof_logged=False,proof_checked=False,SAT_witness=False,UNSAT_claim=False),
  wholecase_CPU_seconds=92.342922089,wholecase_CPU_cap_seconds=120,no_timer_reset=True,
  all_numeric_processes_terminal=True,source_current_literal_parses_across_three_rules=3,
  old_D4_validity_allroot_BFS_field_Lean_ARIS_runs=0,new_candidate_route_BFS_roots=0,
  stopped_fixed_current16416_C_line=True,general_16D4_status='NOT_EXCLUDED',
  distinct_prior_nonorbit_node='ddp-d16d4-source15552-nonorbit-fulln-local-exchange-no-global-unknown-20261101',
  same_Goal='ACTIVE',old_N8_n61='PAUSED'),evidence_paths=paths)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in text
 prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date'];assert n['id']==rid
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):c['write_node'](n)
assert re.search(r'^verdict: partial$',(W/'experiments'/f'{rid}.md').read_text(),re.M)
records[rid]=n;L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[最终SAT处置](../'+D+'ROOT_DISPOSITION.json) |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 当前16416组合C：一个具体扩张问题的真实终态\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n一个记录合并C1全4050pin／warm29UNKNOWN，C2四donor342×5886完整指定域NO且K5全342仍fail，C3 sourceNv162模板greedy21／冻v12312 residualMIPUNKNOWN，C4同残余atmost5 directSAT cUNKNOWN（非UNSAT）。0新图／参数／Lean／独立方法。92.342922089/120CPU含可见失败不reset，fixedcurrent16416 C线全部STOP，其他16D4范围不排。153/43/47、savedmain105/4/global0保持；独立15552非整层模型另节点。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 当前16416组合C已收束：有限合作域NO，其余cover/SAT仍UNKNOWN\n\n具体目标是accepted16416→16417，尚无新图。C1全4050可用pin精确R3（3186oldsource+864clone、all16416targets），greedy/warm29，单30sHiGHS node0/timecap，≤16UNKNOWN。C2转接四donor：342v/5886全inclusion-maximalH失败；旧球K5放宽342也全fail，说明fixedoldP的缺路线不是Hdegree不足，指定域严格NO。\n\n据此C3保全部旧边、用sourceNv设计修4blocked缺口：162模板各seed11+extra10=21，冻v12312仅1744holes（含74currentclones），单20s残余MIP仍10extras/node0/timecap，≤16UNKNOWN。因MIP未branch，再对同一v/seed/residual做一次SAT atmost5：22626vars/43219clauses，合法-t19，实际cUNKNOWN/exit0/无s行，56159conflicts/204313decisions，无SAT或UNSAT见证。\n\n0新图／参数／Lean；累计92.342922089/120CPU含所有prior/prep及K5启动前语法失败，无reset。全部数值终态，停止fixedcurrent16416这条C线，不第二solve/seed/template/H/S5，不排一般16D4。'+str(before+1)+'条记录非方法，153图／43参数／Lean47、savedmain105/4/global0不变。人工15格顶块、sameGoal ACTIVE和旧N8/n61暂停保留；独立nonorbit15552节点保持自身范围。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={};index_before=None
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;index_before=int(m[1])
  text=text[:m.start()]+f'## Experiments ({index_before+1})'+text[m.end():]
  pos=text.index('\n',m.start())+1;text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [partial]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': one concretecurrent16416CombinationCexperimentnode,not4methods. Available4050/warm29UNKNOWN;cooperative342/all5886maximalHNOandK5all342fail;seeded162greedy21/fixedv12312MIPUNKNOWN;directSATsame1744holes3771varsatmost5cUNKNOWN/exit0,notUNSAT,56159conflicts204313decisions. Total92.342922089/120includesallvisiblefailurecosts,nograph/parameter/Lean. FixedClineSTOP,notgeneral16D4NO;human15top exact,153/43/47unchanged,no fullrebuild/state/progress/builder edits.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before+1 and len(after['rows'])==before+1
assert {k:after[k]for k in keys}==counts
receipt=dict(status='PASS_ONE_COMBINATION_C_CURRENT16416_TERMINAL_EXPERIMENT_NODE',updated_UTC=NOW,
 records_before=before,records_after=before+1,records_added=1,new_experiment_id=rid,
 index_experiment_count_before=index_before,index_experiment_count_after=index_before+1,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 available4050='UNKNOWN_WARM29_NO_ATMOST16_WITNESS',cooperative342_maximalH5886='COMPLETE_SPECIFIED_DOMAIN_NO',
 K5_relaxation='ALL342_BASE_FAIL_NOT_DEGREE_COMPATIBILITY_ONLY',seeded162='ALL_GREEDY21_SINGLE_FIXED_MIP_UNKNOWN',
 directSAT='cUNKNOWN_EXIT0_NOT_UNSAT_NO_S_STATUS_LINE',SAT_conflicts=56159,SAT_decisions=204313,
 C_cumulative_CPU_seconds=92.342922089,C_CPU_cap_seconds=120,visible_K5_failure_cost_preserved=True,
 new_seeded_ROOT_disposition=S+'ROOT_DISPOSITION.json',new_SAT_ROOT_disposition=D+'ROOT_DISPOSITION.json',
 all_C_processes_terminal=True,current16416_C_line_stopped=True,general16D4_not_excluded=True,
 human_top_blocks_preserved_exact=preserved,full_rebuild_reimport=False,
 new_math_BFS_solver_field_Lean_ARIS_hash_runs=0,
 root_STATE_ROUND_recovery_progress_builder_modified=False,
 sameGoal='ACTIVE',old_N8_n61='PAUSED',CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
