from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';V=S+'reviews/';D=S+'retained_edge_transfer/published_d16_1920_source_transfer_gate/degree17_plane96/';F=D+'formalization/';E4='expert_review_current/REPLICATION_FOUR_ENDPOINTS_20261101';E17='expert_review_current/C30_D17_2016_20261101'
B='C90_94_FINAL_C_COMPLETE_C30_FULL_QUEUE_DRAFTS_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
L=read('research-wiki/DDP_METHOD_LEDGER.json');keys=['record_count','validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances'];assert tuple(L[k]for k in keys)==(420,151,42,44)
ids=['ddp-wave4-mizuno-d3-source','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
c=read(V+'REPLICATION90_94_FINAL_C_GEMINI_RAW.json')['structuredContent'];assert c['status']=='SUCCESS' and c['threadId']=='bf1ebe1d-0649-4649-a7bd-98cd27b3956a'
assert c['threadId']not in ['e4b6c102-1c55-4739-82e4-d281acc2e835','5da20cd4-ab3f-4327-9df5-8d0e80d7eee3']
verdict=next(json.loads(x)['targets']for x in re.findall(r'```json\s*([\s\S]*?)```',c['content'])if 'targets'in json.loads(x));assert {(g['Delta'],g['D'],g['n'],g['m'])for g in verdict}=={(90,3,380324,16942770),(94,3,397228,18311670)};assert all(all(g[k]=='PASS'for k in ['math','formal','binding'])and g['priority']=='UNKNOWN'for g in verdict)
four=read(E4+'_DRAFT_RECEIPT.json');small=read(E17+'_DRAFT_RECEIPT.json');pilot=read(F+'PILOT_TERMINAL.json');handle=read(F+'DRIVER_HANDLE.json');checkpoint=read(F+'CHECKPOINT.json')
assert four['new_pair_complete_render_requested'] and all(four['new_pair_review_states'].values()) and not four['delivery_ZIP_created']
assert four['snapshot']==dict(named=150,parameters=41,Lean=44) and four['selected_local_links']==141
assert small['snapshot']==dict(named=151,parameters=42,Lean=44) and not small['full_original_target_kernel_closed'] and small['external_review_for17']=='NOT_DISPATCHED' and not small['delivery_ZIP_created']
assert pilot['status']=='PILOT_COMPLETE_LITERAL_DEFS_MATRIX_WALKS_ONE_FULL_ROW_KERNEL_PASS_FULL_TARGETS_PENDING' and len(pilot['completed_modules'])==8 and pilot['failed_attempts']==1
assert not pilot['source_full_D3_kernel_complete'] and not pilot['clone2016_final_claim_kernel_complete']
assert handle['driver_pid']==1468135 and handle['running'] and checkpoint['running'] and checkpoint['CPU_budget_seconds']==1200

q8=rows[1];m=q8['other_metrics'];batch=m['replication90_94_actual_batch'];batch['status']='BOTH_NEW_ORIGINALS_MATH_KERNEL_A_B_DISTINCTFRESH_C_ACTUAL_COMPLETE_PRIORITY_UNKNOWN'
batch['distinctfreshC']=dict(status='ACTUAL_SUCCESS_TWO_EXACT_ORIGINAL_MATH_FORMAL_BINDING_PASS_DISTINCT_FRESH',cell=732,store='endpoint90_94_C_actual',thread=c['threadId'],actual_shared_calls=1,response_chars=len(c['content']),targets=verdict,priority='UNKNOWN',
 A_actual_thread='e4b6c102-1c55-4739-82e4-d281acc2e835',B_actual_thread='5da20cd4-ab3f-4327-9df5-8d0e80d7eee3',distinct_from_actual_A_B=True,terminal=True,live=False,no_retry=True,old_scope_PASS_inherited=False,new17_or_local_research_in_scope=False,
 raw=V+'REPLICATION90_94_FINAL_C_GEMINI_RAW.json',disposition=V+'REPLICATION90_94_FINAL_C_DISPOSITION.md',request=V+'REPLICATION90_94_FINAL_C_REQUEST.json')
for g in m['validated_graph_instances']:
 if g['n']in [380324,397228]:g.update(external_fresh_C='ACTUAL_SUCCESS_NEW_SCOPE_MATH_FORMAL_BINDING_PASS',external_final_C_thread=c['threadId'],external_final_C_distinct_from_actual_A_B=True,external_B_C_complete=True,new_case_reviews_complete=True,priority='UNKNOWN')
m['all_row_original_A_B_distinctfreshC_complete']=True
m['completed_Lean_and_A_B_C_scope']='all9actualq8originalsmath_kernel_A_B_distinctfreshCcomplete;new17andlocalresearchoutsideScope'
m['all_local_formal_processes_scope']='all9q8originalscompleted;noq8localorremoteLiveJobs;separateC30fullkernelqueuerunningnotq8scope'
m['replication_four_endpoint_expert_DRAFT'].update(status=four['status'],snapshot=four['snapshot'],HTML_bytes=36331,HTML_source_bytes=36331,Word_bytes=9929,selected_local_paths=141,missing_local_paths=0,actual_prepare_CPU=four['CPU_seconds'],render_generation_UTC=four['generated_UTC'],
 rendered_new_pair_review_states=four['new_pair_review_states'],render_predates_actual_A707=False,new_pair_complete_render_requested=True,actual_current_new_pair_A='PASS',actual_current_new_pair_B='PASS',actual_current_new_pair_C='PASS',C_thread=c['threadId'],ZIP_created=False,freeze_performed=False,current_live_snapshot_including_new17=[151,42,44],new17_in_four_endpoint_DRAFT=False)
batch['four_endpoint_expert_lightpage']=dict(status='ACTUAL_UNFROZEN_DRAFT_READY_NEW_PAIR_COMPLETE_RENDERED',receipt=E4+'_DRAFT_RECEIPT.json',snapshot=[150,41,44],new_pair_C_complete=True,ZIP_created=False)
q8['title']='90/94最终distinctfreshC732实际PASS；q8九原目标审阅全齐，四端点轻量DRAFT已更新但未ZIP'
q8['outcome_class']='ALL_NINE_Q8_ORIGINALS_MATH_KERNEL_A_B_DISTINCTFRESHC_ACTUAL_COMPLETE_FOUR_ENDPOINT_UNFROZEN_DRAFT_READY'
q8['distance_text']+=' 最终C732实际SUCCESS，8011chars及两tuple math/formal/bindingPASS/priorityUNKNOWN已root全读处置，真实threadbf1ebe1d-0649-4649-a7bd-98cd27b3956a异A e4/B5da。一次sharedfreshcall逐90/94原目标，不是两calls/旧C继承；732terminal且remote0live，不再等/重试。四endpoint已实际--new-pair-complete轻更新HTML/source各36331B、Word9929B、141links/.020790179CPU，0ZIP，固定150/41/44snapshot。新17不在审阅/旧draftscope，live151/42/44与优先权UNKNOWN保留。'
q8['lesson_and_restart_condition']+=' 最新finalC732已经闭合，覆盖此前pending恢复指令：本q8节点全部9原目标math/kernel/A/B/distinctfreshC实际完毕，无remote live；不再poll732，不追加付费/复验。四端点专家材料保持轻量未冻结0ZIP，不改旧包；sourcefill/同规则优先权风险不因审阅PASS消失。'

source=rows[0];sm=source['other_metrics'];sg=sm['validated_graph_instances'][0];assert sg['n']==2016 and not sg['complete_Lean_graph_instance']
sg['formal_status']='PILOT8_MODULES_PASS_ONLY_ROW0_FULL_SOURCE_AND_FIN2016_TARGET_QUEUE_RUNNING_NOT_COMPLETE'
sm['degree17_literal_C30_and_Fin2016_Lean_pilot'].update(status='ACTUAL_PILOT8_PASS_FULL_QUEUE_SEPARATELY_AUTHORIZED_RUNNING_NOT_COMPLETE',actual_pilot_CPU=pilot['CPU_seconds'],actual_pilot_failed_attempts=1,actual_pilot_modules_PASS=8,
 row_scope='onlyforallxFin64_vFin1920_genuineWalk_fromliftAt0x;notfullsourceorcloneFinalClaim',pilot_std3=pilot['axioms'],pilot_terminal=F+'PILOT_TERMINAL.json',
 full_cumulative_authorized_CPU=1200,pilot_included_in_full_budget=True,full_queue_status='RUNNING_AS_SAVED_HANDLE',session=4008,driver_pid=1468135,
 observed_as_saved_handle_CPU=handle['CPU_seconds'],observed_checkpoint_CPU=checkpoint['CPU_seconds'],observed_checkpoint_completed_modules=len(checkpoint['completed']),
 per_module_limit_CPU=60,max_source_leaves=2,driver_handle=F+'DRIVER_HANDLE.json',checkpoint=F+'CHECKPOINT.json',old_pilot_TERMINAL_not_full_stop=True,
 source1920_reproduction_counted_as_new_Lean=False,only2016_original_target_Audit_can_increment_Lean=True,concrete_instance_increment=0,all_PASS_old_field_modules_imported_not_recompiled=True,complementary_CloneInputs_source_only_no_second_compile_timer=True)
sm['degree17_literal_C30_and_Fin2016_Lean_pilot']['compile_handle']=F+'DRIVER_HANDLE.json'
sm['degree17_expert_DRAFT']=dict(status=small['status'],snapshot=small['snapshot'],HTML=E17+'.html',HTML_source=E17+'.html.txt',Word=E17+'.docx',receipt=E17+'_DRAFT_RECEIPT.json',
 HTML_bytes=17577,HTML_source_bytes=17577,Word_bytes=9897,selected_local_paths=46,missing_local_paths=0,actual_prepare_CPU=small['CPU_seconds'],generated_UTC=small['generated_UTC'],
 math_accepted=True,full_kernel_complete=False,external_reviews_for17='NOT_DISPATCHED',old_scope_PASS_inherited=False,priority='UNKNOWN',ZIP_created=False,freeze_performed=False,
 draft_generation_before_full_queue_running_claim=True,current_full_queue_scope='actualDRIVER_HANDLErunning_notDRAFTgenerationclaim')
source['title']='17度2016数学验收：8module pilot仅Row0通过；累计1200CPU完整C30/Fin2016队列在途，Lean仍44'
source['outcome_class']='D17_COMPLETE_MATH_FRESH_ACCEPTED_PILOT_PASS_FULL_CONCRETE_KERNEL_RUNNING_NOT_YET_COMPLETE'
source['distance_text']+=' 120CPU pilot实际8modules PASS/59.69639203CPU含1失败修复，只有Row0任意64源点到1920目标真Walk/std3，source完整D3和cloneFinalClaim尚未闭。根据成本root新授权累计1200CPU含pilot，实际full source rows1..29+clone目标session4008/driver1468135已运行，最多2newsourceleaf/permodule60；以formalization/DRIVER_HANDLE与CHECKPOINT为live入口，旧pilotTERM不作全批停止。本次只读handle已观察accounted'+str(round(handle['CPU_seconds'],6))+'CPU、checkpoint完成'+str(len(checkpoint['completed']))+'modules，此为中途快照非预算重置或预计PASS。所有PASS/旧field仅import不重编，另agent只备CloneInputs源码无第二compiletimer。source1920公开复现不加图/Lean，唯2016原target及Audit闭合才Lean+1，当前仍44。新17专家HTML/source17577B各、Word9897B、46links/.028130478CPU actualDRAFT snapshot151/42/44，mathPASS/fullkernelpending/17reviews未派/priorityUNKNOWN/0ZIP。'
source['lesson_and_restart_condition']+=' fullkernel恢复只能沿现session4008与DRIVER_HANDLE/CHECKPOINT、累计1200含pilot、sourceleaf最多2，不误读旧PILOT_TERMINAL为full停止，不重新编PASS/旧field。8pilot模块和Row0不计具体完整Lean，不能拿q8 finalC审阅代17target，不能提前计45。新专家draft是可读研究材料、未冻结；当前仅fullkernel队列推进，无新图/研究由本同步派发。'

ce=[V+x for x in ['REPLICATION90_94_FINAL_C_GEMINI_RAW.json','REPLICATION90_94_FINAL_C_DISPOSITION.md','REPLICATION90_94_FINAL_C_REQUEST.json']]+[E4+x for x in ['_DRAFT_RECEIPT.json','.html','.html.txt','.docx']]
se=[F+x for x in ['PILOT_TERMINAL.json','PILOT_CHECKPOINT.json','DRIVER_HANDLE.json','CHECKPOINT.json']]+[E17+x for x in ['_DRAFT_RECEIPT.json','.html','.html.txt','.docx']]
assert all((R/x).is_file()for x in ce+se);q8['evidence_paths']=list(dict.fromkeys(q8['evidence_paths']+ce));source['evidence_paths']=list(dict.fromkeys(source['evidence_paths']+se))
rawrows=W/f'updates/{B}_ROWS.json';rawrows.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',rawrows).strip());L=read('research-wiki/DDP_METHOD_LEDGER.json');assert tuple(L[k]for k in keys)==(420,151,42,44)
block=f'''<!-- {B} -->
# 当前：90/94最终C732实际全PASS且remote0live；17度完整kernel沿现4008队列推进，Lean仍44

同Goal ACTIVE，ledger420复用[C30](experiments/{ids[0]}.md)与[q8](experiments/{ids[1]}.md)，0新行/方法/图；151合法named／42参数／Lean44、stage47／39、outside45／38、known43/main103_3/global0保持。

90/94最终C732已实际SUCCESS，8011chars/两精确tuple math/formal/bindingPASS、priorityUNKNOWN，真实threadbf1ebe1d-0649-4649-a7bd-98cd27b3956a异A e4/B5da。一次freshsharedcall逐原目标，732terminal/remote0live，勿再等或重试，不认证global或17目标。四endpoint专家已实际--new-pair-complete：HTML/txt36331各、Word9929、141links/.020790179CPU，0ZIP，固定150/41/44snapshot。

17专家actualDRAFT：HTML/txt17577各、Word9897、46links/.028130478CPU，snapshot151/42/44，mathPASS/fullkernelpending/reviewsNOT_DISPATCHED/priorityUNKNOWN/0ZIP。pilot8modules实际59.69639203CPU含1失败PASS，仅Row0的64任意源点→1920目标真Walk/std3，不是fullsource或2016原claim。root授权累计1200CPU含pilot，完整rows1..29+clone队列实际session4008/driver1468135在跑、最多2sourceleaf/permodule60；本次只读handle快照accounted{handle['CPU_seconds']:.6f}CPU、checkpoint完成{len(checkpoint['completed'])}modules，非最终完成。恢复只沿formalization/DRIVER_HANDLE与CHECKPOINT，旧pilotTERM不作full停止。PASS/旧field只import不重编，另agent仅准备CloneInputs不另起timer。source1920公开复现0图/Lean，只有2016原target/Audit闭才Lean+1，当前不计45。

本次只同步已有实际receipt，不编译、重验图、检索、外审、重渲染、重检links或冻包；根文件不动，完成后停止写入。

'''
gap=W/'gap_map.md';assert B not in gap.read_text();gap.write_text(block+gap.read_text());comments=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';comments.write_text(comments.read_text()+f'\n\n## {now} 90/94最终C实际闭合与两个轻量草稿；17完整kernel真实队列入口\n\n'+block.split('\n\n',1)[1])
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Actual90_94finalC732SUCCESSbf1ebe1dDistinctAe4B5da8011chars2exacttuplemathformalbindingPASSpriorityUNKNOWNoneSharedFreshCall_terminalremote0liveNoRetry_n17outsideScope. FourendpointnewpaircompleteDRAFT36331htmltxt9929Word141linksCPU.020790179snapshot150_41_44zeroZIP. New17DRAFT17577htmltxt9897Word46linksCPU.028130478snapshot151_42_44mathPASSfullkernelPendingreviewsNOTDISPATCHEDpriorityUNKNOWNzeroZIP. Pilot8PASS59.69639203incl1fail_onlyRow0all64to1920genuineWalkStd3_notFullSourceCloneFinalClaim. FullrootAuthorizedCumulative1200includesPilot_liveSession4008driver1468135max2sourceleavespermodule60_actualSavedHandleCheckpointRead_resumeOnlySameQueue_notOldPilotTERM_notRecompilePASS_oldfield_noSecondCloneInputsCompileTimer. PublishedSource1920reproduction0graphLean_only2016originalAuditcompletionCanAdd1_currentLean44. Ledger420twoExistingRows151_42Lean44stage47_39outside45_38known43main103_3global0unchanged0newMathGraphBFSLeanSolverWebPaidReviewRenderLinksRootownedFrozenWrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W);(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
for i,row in zip(ids,rows):assert row['title']in(W/'experiments'/f'{i}.md').read_text()
assert len(calls)==4 and all(x['returncode']==0 for x in calls)
receipt=dict(status='PASS_90_94_FINAL_C_COMPLETE_TWO_ACTUAL_DRAFTS_C30_FULL_KERNEL_SAME_LIVE_QUEUE',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=151,legal_parameter_pairs=42,complete_formula_Lean=44,stage_graphs=47,stage_pairs=39,outside_graphs=45,outside_pairs=38,known_publicly_dominated=43,global_records=0,
 endpoint90_94_finalC='ACTUAL_SUCCESS_TWO_ORIGINAL_THREE_FACET_PASS',C732_terminal=True,remote_live=0,C_thread=c['threadId'],C_distinct_actual_A_B=True,C_chars=len(c['content']),
 fourendpointDRAFTsnapshot=[150,41,44],fourendpointDRAFTbytes=[36331,36331,9929],fourendpointDRAFTlinks=141,new17DRAFTsnapshot=[151,42,44],new17DRAFTbytes=[17577,17577,9897],new17DRAFTlinks=46,new_ZIP=0,
 pilot_PASS_modules=8,pilot_CPU=pilot['CPU_seconds'],pilot_failed_attempts=1,pilot_scope='ONLY_ROW0_64_ORIGINS_TO1920_TARGETS_NOT_FULL_SOURCE_OR_CLONECLAIM',
 full_kernel=dict(status=handle['status'],session=4008,driver_pid=1468135,cumulative_budget_CPU=1200,pilot_included=True,as_read_handle_CPU=handle['CPU_seconds'],as_read_checkpoint_completed_modules=len(checkpoint['completed']),max_source_leaves=2,final2016_complete=False),
 only2016_original_target_Audit_can_add_Lean=True,new_graph_Lean_method_increments=[0,0,0],evidence_paths_checked=len(ce)+len(se),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',static_scope_check='PASS_counts_existing2nodes_fourActualHelperCalls_evidencePaths',math_graph_BFS_Lean_solver_web_paid_runs_this_sync=0,expert_rerender_or_links_recheck=False,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
