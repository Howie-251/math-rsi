"""One K19 terminal experiment delta; no numerical, source, or solver execution."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/K19_exact_matching_interface';F=D/'exact_point_model';A=F/'assignment_then_shift';P=A/'tight_row_propagation'
st=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d8d4-two684-k19-exact-point-assignment-shift-terminal-unknown-20261102'
marker='<!-- K19_EXACT_POINT_AND_ASSIGNMENT_SHIFT_TERMINAL_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==452
assert not any(r['id']==slug or 'K19_exact_matching_interface' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
oldrows=copy.deepcopy(ledger['rows']);counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
root=json.loads((D/'ROOT_DISPOSITION.json').read_text());full=json.loads((F/'RESULT.json').read_text());assignment=json.loads((A/'ASSIGNMENT_RESULT.json').read_text());fixed=json.loads((A/'RESULT.json').read_text());prop=json.loads((P/'RESULT.json').read_text())
assert root['status']=='ROOT_ACCEPTED_K19_FULL_AND_FIXED_LAYOUT_UNKNOWN_CASE_STOP' and root['whole_case_CPU_seconds']==96.356641619
assert root['native_SAT_windows_seconds']==[60,20,5] and full['status']=='UNKNOWN_SINGLE_CADICAL_WINDOW' and fixed['status']=='UNKNOWN_SINGLE_FIXED_SIGMA_SHIFT_WINDOW' and prop['status']=='UNKNOWN_PROPAGATION_WINDOW'
assert full['model']['cover_literals']==29499552 and full['model']['clauses']==172800 and assignment['minimum_capacity']==19
oldid='ddp-stale-d8d4-two684-all-hleft-equivariant-matchings1368-no-20261101';old=next(r for r in ledger['rows'] if r['id']==oldid)
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
evidence=[]
for parent,names in [
(D,['ROOT_DISPOSITION.json','NOTE.md','READ_GATE.md','READ_GATE.json','MODEL_EXACTNESS_PAPER.md','MODEL_SCOPE_ATTACK.md','ASSIGNMENT_SHIFT_DECOMPOSITION_PAPER.md','LOCAL_TIGHT_ROW_PAPER.md','TIGHT_ROW_PROPAGATION_PAPER.md','independent_acceptance/PREPARATION_RESULT.json','independent_acceptance/verify_candidate.py','independent_acceptance/README.md']),
(F,['PRED.md','convert_cache.py','build_model.cpp','run_once.py','CACHE_CONVERSION.json','ORBIT_MAPPING.json','A_EXACT_LENGTH0_3.u32','BASE_COVER_MASKS.u32','MODEL_SCHEMA.json','BUILD_RESULT.json','K19_EXACT_POINT.cnf','DRIVER_HANDLE.json','NATIVE_EXECUTION.json','SAT_STDOUT.log','RESULT.json','TERMINAL.json','NOTE.md']),
(A,['PRED.md','run_assignment_once.py','ASSIGNMENT_MATRIX.npz','M_POPCOUNTS.u8','ASSIGNMENT_MODEL.json','ASSIGNMENT_WARM.json','ASSIGNMENT_RAW.json','ASSIGNMENT_INTEGER_CHECK.json','ASSIGNMENT_RESULT.json','FROZEN_SIGMA.json','FROZEN_SIGMA.tsv','build_shift_once.py','SHIFT_MODEL_RESULT.json','FIXED_SIGMA_SHIFT.cnf','run_once.py','positive_candidate.py','NATIVE_EXECUTION.json','SAT_STDOUT.log','RESULT.json','TERMINAL.json','NOTE.md','TIGHT_ROW_PRED.md','TIGHT_ROW_RESULT.json']),
(P,['PRED.md','DERIVED_BINARY_MODEL.json','STRENGTHENED_SHIFT.cnf','HANDLE.json','SAT_STDOUT.log','RESULT.json','TERMINAL.json'])]:
 for n in names:evidence.append(str((parent/n).relative_to(ROOT)))
assert all((ROOT/p).exists() for p in evidence)
# Read only existing native textual statistics; no model generation/checking here.
proptext=(P/'SAT_STDOUT.log').read_text(errors='replace');pstats={}
for k in ['conflicts','decisions','propagations','restarts']:
 h=re.findall(r'^c\s+'+k+r':\s*([0-9,]+)',proptext,re.M);pstats[k]=int(h[-1].replace(',','')) if h else None
raw={
'id':slug,'title':'8D4两684的K19实际点模型：60/20/5三SAT窗口均UNKNOWN，assignment与紧行诊断未成图',
'family':old['method_family'],'idea_family':'idea:ddp-open-parameter-construction-20261026','date':'2026-11-02','wiki_verdict':'partial',
'record_type':'fixed_two_source_copies_K19_equivariant_actualpoint_matching_CNF_experiment',
'target_Delta':8,'target_D':4,'savedL':old['goal']['savedL'],'baseline_date':old['goal']['baseline_date'],
'n':{'actual':None,'hypothetical':1368},'actual_graph_Delta':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':4,'new_lower_bound':False,
'actual_D_scope':'No1368candidategraph,sourceparse,newgraphBFS,freshsuiteorformalgraphwitness. FullK19model60sUNKNOWN;onesigmafixed20sUNKNOWN;entailedbinarysamessigma5sUNKNOWN. NeitherK19norselectedsigmaexcluded; noSATorUNSATreturned.',
'outcome_class':'TERMINAL_UNKNOWN_K19_FULL_AND_ONE_ASSIGNMENT_SHIFT_ENTAILED_PROPAGATION_CASE_STOP',
'scope':'ActualfixedMichel684simple7regularD4two-orbitH342source,twofulloldedgecopies,oneK19-equivariantmatching. K19orbitsr=18tau+2b+epsilon,nu(r,k)=342tau+9(epsilon+2k)+b; matching(r,k)->(sigma(r),k+t_r),sigmaarbitraryS36/t_rindependentZ19;reverseinverse,nosigmainvolution. GlobaltargetKshiftgiveslegalt0=0gaugewithoutfixingsigma0. OldH342233928domainstrictNOisinheritedstrictsubset,notK19NO. OnefullpointCNF;onemaxmincapacityassignment;onefrozensusigmaexactshiftCNF;onetightrowdiagnostic/entailedbinaryfollowup;oneproblemrecord,same100CPUbudget,noσ2.',
'distance_text':'完整actualpoint CNF24624choices/24624跨点义务，73800vars/172800clauses/29499552coverlits/166236739B，空point0；唯一60sCaDiCaL cUNKNOWN。随后按真实全模型长OR/assignment-shift耦合反馈分解：5sHiGHS TimeLimit返回唯一整数sigma，1296容量全核min19仅必要门，非最优/graph；冻结后1332vars/26586clauses，唯一20s仍cUNKNOWN。再预测tight28→28自身不能铺满，被DFS5的实际tile反驳，不能据该行称global不相容。因该行sum19，补2603条entailed non-overlapbinary得29189clauses，同sigma/解域唯一5s仍cUNKNOWN。三SAT60/20/5与一次assignmentMIP5全部记录，总96.356641619/100CPU不reset；0新图/参数/Lean，K19及固定sigma均仍UNKNOWN。',
'lesson_and_restart_condition':'STOPthisK19case:noσ2/seed/newtranslation/MIPorSATcontinuation. Fullactualpointmodelwasnotreplacedbywalkcapacity;projectionusedonlytoselectonefeasibleorbitassignment,thenreturnedtoall24624pointclauses. Intrinsic-rowNOpredictionwasrefutedbyatilingandchangedthenextmodeltoexplicitentailedpropagation,withoutclaimingglobalfeasibilityorconflict. Maxmin18to19isnotagraphresult;threeUNKNOWNsearchwindowsarealgorithmfeedback,notfamilyNO.',
'restart_condition':'Onlyanewauthorizedboundedquestionwithchangedstructure/hostormeaningfulnewalgorithmicreason;allcurrentfull/fixed/propagationtimersstopped. Noautomaticunused-budgetcontinuationorsigma2. Rootnewsource672isaseparateproblem,notthisnodeornewK19result.',
'unclosed_gap':'FullK19matchingdomainremainsUNKNOWN,asdoestheuniquechosensigma. OldH342strictNOcannotbeextended. Row28to28tiledoesnotsettleother1295rowsorjointshiftcompatibility. ExactCNFhasnopointmodelwitnessorcheckedUNSATproof. General8D4/othermatching/hostrulesremainunexcluded. Independentfreshverifieronlydraft/ASTsyntaxprepared,neverdata-run. GoalACTIVE/oldN8n61PAUSED.',
'positive_guarantees':[
'Oldexact-length0..3Hendpointcacheistranslatedbylefth_r*uandactuallabeldecompositionto36K19orbits;10656storedendpointtranslations/5184masks,nooldDP/sourceD4recheck.',
'B(i,j;r,s)=union_(a+b<=3)(A_a(i,r)+A_b(s,j));selectedchoicecoversrot19(B,t). All24624pointORs,72rowcolEXOandglobaltargetKshiftgaugeareexactunderinheritedsourceD4;no sigma0orinvolutionassumption.',
'Onlyoneactualsigmafrozenafterintegerrowcolandall1296capacitychecks;fixedmodelretainsall24624targets. Min19iscapacitynecessary,notpointcoverageoroptimalityevidence.',
'Oneuniquetightrow28to28sum19canindividuallytile(DFS5). Its2603pairwiseoverlapbinariesareentailedbyfull19pointcoverage,sum19andonechoiceperrow;nochangeinsigma/solutiondomain.',
'NativeSATcallsarefullydisclosedas60/20/5fordifferentmodelstages,samebudget;allreturnedcUNKNOWN/exit0/nosstatus,notSATorUNSAT. No successful graphornegativeLeantheoremclaimed.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,'single_record_all_stages':True,'old_H342_node':oldid,'old_H_domain_parameters':233928,'old_H_domain_verdict':'STRICT_NO_INHERITED_NOT_RERUN','K19_strictly_larger_than_H':True,'K19_not_arbitrary684pointmatching':True,
'orbit_domain':{'orbits':36,'orbit_size':19,'sigma':'S36','shifts':'Z19^36','selectedchoices':36,'physicalmatching_edges_ifpositive':684,'t0gauge':True,'sigma0fixed':False,'sigma_involution_required':False},
'full_model':root['full_exact_model'],'full60_window':{'raw':'c UNKNOWN','exit':0,'s_status_lines':[],'stats':full['native']['statistics'],'native_actual_CPU':60.041635,'cumulative_stage_CPU':63.697950855},
'assignment_projection':{'binary':1296,'integer_z':1,'equalities':72,'capacity_rows':1296,'matrix_nnz':504144,'configured_HiGHS_seconds':5,'actual_HiGHS_CPU':5.149360753,'raw_status':'TimeLimit','nodes':0,'identity_warm_min':18,'returned_sigma_min':19,'sigma':assignment['sigma'],'all1296_integer_caps_checked':True,'rawdual':-668,'not_optimality_or_graph':True,'unique_sigma_frozen':True},
'fixed20_model':root['frozen_shift_model'],'fixed20_window':{'raw':'c UNKNOWN','exit':0,'s_status_lines':[],'stats':fixed['native']['statistics'],'native_actual_CPU':19.961063,'cumulative_stage_CPU':90.922314663},
'local_tight_row':{'root_orbit':28,'target_orbit':28,'sum_packet_sizes':19,'one_row_only':True,'nonempty_packets':9,'DFS_nodes':5,'actual_verdict':'INDIVIDUALLY_TILEABLE','prediction_intrinsic_row_NO':'REFUTED','does_not_establish_global_compatibility_or_incompatibility':True,'cumulative_stage_CPU':91.137800205},
'entailed_propagation':{'same_sigma':True,'same_variables':1332,'original_clauses':26586,'added_entailed_binary':2603,'total_clauses':29189,'solution_domain_unchanged':True,'configured_SAT_seconds':5,'raw':'c UNKNOWN','exit':0,'stats':pstats,'native_actual_CPU':5.002062},
'SAT_calls_total':3,'SAT_configured_seconds':[60,20,5],'MIP_calls_total':1,'MIP_configured_seconds':[5],'wholecase_CPU':96.356641619,'case_CPU_cap':100,'no_timer_reset':True,'all_processes_terminal':True,'full_K19_verdict':'UNKNOWN_NOT_NO','frozen_sigma_verdict':'UNKNOWN_NOT_UNSAT','no_second_sigma_or_seed':True,
'source_parse_count':0,'old_endpoint_DP_repeated':0,'sourceD4validation_BFS':0,'old_H233928_repeated':0,'candidate_graphs':0,'candidate_BFS':0,'fresh_suite_runs':0,'fresh_verifier_status':'DRAFT_AST_ONLY_NOT_EXECUTED','field_Lean_ARIS_runs':0,'negative_Lean_required':False,'proof_logged_or_checked':False,'same_Goal':'ACTIVE','old_N8_n61':'PAUSED'
},'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'K19_EXACT_POINT_AND_ASSIGNMENT_SHIFT_TERMINAL_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'K19_EXACT_POINT_AND_ASSIGNMENT_SHIFT_TERMINAL_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'].append(row);ledger['record_count']=453;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n');node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} K19三个actualpoint窗口终态UNKNOWN，旧H域NO不扩张

同一684source两copy/K19-equivariantmatching问题合一个节点：完整CNF73800vars/172800clauses/29499552coverlits，60s cUNKNOWN；5sassignment MIP只选唯一sigma，整数容量min19必要门不计图；固定sigma1332vars/26586clauses，20s cUNKNOWN。tight28→28 sum19能tile（DFS5），反驳intrinsic-rowNO预测，既不证全局可行也不证不相容；添加2603条entailedbinary的同sigma模型29189clauses，最后5s仍cUNKNOWN。

三SAT60/20/5及一次MIP5全部记账，wholecase96.356641619/100CPU不reset；sourceparse/oldDP/D4BFS/graph/fresh/Lean/ARIS均0，fresh verifier仅草稿。K19完整域及唯一冻结sigma仍UNKNOWN；旧H342233928strictNO继续继承、不套给K19。停止，不sigma2/seed/窗口续算，min18→19不是构造成果。

452→453一实验节点，不拆方法；153/43/47、savedmain105/4/global0保持。人工15格top逐字保留，sameGoalACTIVE/旧N8n61暂停。新source672属于root独立问题，不在本节点预造结果。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert m;oldexp=int(m.group(1));text=text[:m.start(1)]+str(oldexp+1)+text[m.end(1):]
 (W/name).write_text(text);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} K19 exactpoint：full／一sigma／entailed propagation皆UNKNOWN

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (8,4)；L{raw['savedL']}；目标1368，未生成图 | full60s UNKNOWN；一次MIP min19仅必要门→one-sigma20s UNKNOWN；tight28→28 tile反驳intrinsic-rowNO，2603entailedbinary后5s仍UNKNOWN。 | 旧H342233928NO只保旧范围；K19及固定sigma均未排。三SAT/一MIP同case96.356641619/100，sourceparse/DP/BFS/fresh0。[root实际终态](../{str((D/'ROOT_DISPOSITION.json').relative_to(ROOT))}) |

一个实验452→453，不把容量18→19、单行tile或模型缩小当新图。完整actualpointCNF29499552coverlits/172800clauses；全部models/coords/raw已存。0新增图/参数/Lean/独立方法，153/43/47保持；停止K19case，无sigma2/续timer，GoalACTIVE/旧N8n61暂停。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==453 and after['rows'][:-1]==oldrows;assert all(after[k]==v for k,v in counts.items());assert (W/node).exists()
receipt={'status':'PASS_ONE_K19_EXACT_POINT_ASSIGNMENT_SHIFT_TIGHT_PROPAGATION_UNKNOWN_NODE','updated_UTC':now,'records_before':452,'records_after':453,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),'index_experiment_count_before':oldexp,'index_experiment_count_after':oldexp+1,'SAT_calls_disclosed':3,'SAT_seconds':[60,20,5],'MIP_calls_disclosed':1,'MIP_seconds':[5],'all_windows_terminal_UNKNOWN':True,'wholecase_CPU':96.356641619,'casecap':100,'no_reset':True,'oldH233928_strictNO_preserved_not_K19_NO':True,'full_K19_and_frozen_sigma':'UNKNOWN','tight_row28to28_tile_prediction_refuted':True,'single_row_tile_not_global_compatibility_claim':True,'entailed_binaries':2603,'positive_fresh_verifier':'DRAFT_NOT_RUN','sourceparse_oldDP_sourceD4BFS_graph_fresh_Lean_ARIS':0,'graph_parameter_Lean_method_increments':[0,0,0,0],'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']},'all_other452_rows_preserved_exact':True,'human_top_blocks_preserved_exact':{p:True for p in files},'full_rebuild_reimport':False,'new_math_solver_BFS_Lean_paid_hash_runs':0,'root_STATE_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-st,'stop':True}
(S/'K19_EXACT_POINT_AND_ASSIGNMENT_SHIFT_TERMINAL_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
