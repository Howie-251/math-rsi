from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';V=S+'reviews/';E='expert_review_current/REPLICATION_FOUR_ENDPOINTS_20261101'
B='REPLICATION90_94_A_PASS_B716_PENDING_FOUR_DRAFT_READY_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
L=read('research-wiki/DDP_METHOD_LEDGER.json');keys=['record_count','validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances'];assert tuple(L[k]for k in keys)==(420,150,41,44)
ident='ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101';row=copy.deepcopy(next(x for x in L['rows']if x['id']==ident)['source_record']);m=row['other_metrics']
a=read(V+'REPLICATION90_94_A_GEMINI_RAW.json')['structuredContent'];assert a['status']=='SUCCESS' and a['threadId']=='e4b6c102-1c55-4739-82e4-d281acc2e835'
verdict=next(json.loads(x)['targets']for x in re.findall(r'```json\s*([\s\S]*?)```',a['content'])if 'targets'in json.loads(x))
assert {(g['Delta'],g['D'],g['n'],g['m'])for g in verdict}=={(90,3,380324,16942770),(94,3,397228,18311670)}
assert all(all(g[k]=='PASS'for k in ['math','formal','binding'])and g['priority']=='UNKNOWN'for g in verdict)
b=read(V+'REPLICATION90_94_B_REQUEST.json');assert b['status']=='ACTUALLY_DISPATCHED_ONE_SHARED_NEW_SCOPE_B_PENDING' and b['cell_id']=='716' and b['threadId']=='5da20cd4-ab3f-4327-9df5-8d0e80d7eee3' and b['shared_calls']==1
d=read(E+'_DRAFT_RECEIPT.json');assert d['snapshot']==dict(named=150,parameters=41,Lean=44) and not d['delivery_ZIP_created'] and not d['freeze_performed']
assert d['selected_local_links']==136 and not d['missing_local_links']
batch=m['replication90_94_actual_batch'];batch.update(status='ROOT_ACCEPTED_COMPLETE_MATH_KERNEL_A_ACTUAL_PASS_B716_PENDING_C_NOT_DISPATCHED')
batch['A']=dict(status='ACTUAL_SUCCESS_TWO_EXACT_ORIGINAL_MATH_FORMAL_BINDING_PASS',cell=707,thread=a['threadId'],actual_shared_calls=1,response_chars=len(a['content']),targets=verdict,priority='UNKNOWN',old_case_PASS_inherited=False,
    raw=V+'REPLICATION90_94_A_GEMINI_RAW.json',disposition=V+'REPLICATION90_94_A_DISPOSITION.md',terminal=True,no_retry=True)
batch['B']=dict(status='ACTUALLY_DISPATCHED_ONE_SHARED_NEW_SCOPE_B_PENDING',cell=716,store=b['store_key'],thread=b['threadId'],actual_shared_calls=1,request=V+'REPLICATION90_94_B_REQUEST.json',old_case_PASS_inherited=False)
batch['distinctfreshC']=dict(status='NOT_DISPATCHED',old_scope_PASS_inherited=False)
for g in m['validated_graph_instances']:
    if g['n']in [380324,397228]:g.update(external_A='ACTUAL_SUCCESS_NEW_SCOPE_MATH_FORMAL_BINDING_PASS',external_A_thread=a['threadId'],external_A_cell=707,external_B='NEW_EXPLICIT_TWO_TARGET_SCOPE_ACTUALLY_DISPATCHED_PENDING',external_B_thread=b['threadId'],external_B_cell=716,external_fresh_C='NOT_DISPATCHED',external_B_C_complete=False,new_case_reviews_complete=False)
m['completed_Lean_and_A_B_C_scope']='all9q8originalsmath_kernelcomplete;prior7A_B_distinctfreshCcomplete;new90_94AactualPASS_B716pending_Cnotdispatched;smallhelpermixedandfuture16_1920gatesexcluded'
m['replication_four_endpoint_expert_DRAFT']=dict(status=d['status'],snapshot=d['snapshot'],degrees=d['four_degrees'],HTML=E+'.html',HTML_source=E+'.html.txt',Word=E+'.docx',receipt=E+'_DRAFT_RECEIPT.json',HTML_bytes=35670,HTML_source_bytes=35670,Word_bytes=9937,selected_local_paths=136,missing_local_paths=0,actual_prepare_CPU=d['CPU_seconds'],ZIP_created=False,freeze_performed=False,
    render_generation_UTC=d['generated_UTC'],rendered_new_pair_review_states=d['new_pair_review_states'],render_predates_actual_A707=True,actual_current_new_pair_A='PASS',actual_current_new_pair_B='716_PENDING',actual_current_new_pair_C='NOT_DISPATCHED',no_rerender_this_sync=True)
batch['four_endpoint_expert_lightpage']=dict(status='ACTUAL_UNFROZEN_DRAFT_READY',receipt=E+'_DRAFT_RECEIPT.json',ZIP_created=False,render_predates_actual_A707=True)
m['published16_1920_interface_gate_status']='READ_ONLY_IN_PROGRESS_NO_RETURNED_FORMAL_GATE_RECEIPT_NO_VALIDATED_CONCLUSION_NEW_GRAPH_OR_LOCAL_COMPUTATION_CLAIMED'
row['title']='90/94数学/kernel及新A707已实际通过，B716在途、freshC未派；四端点专家草稿已生成，150/41/Lean44'
row['outcome_class']='NINE_Q8_MATH_KERNEL_COMPLETE_90_94_A_PASS_B_PENDING_C_NOT_DISPATCHED_FOUR_ENDPOINT_DRAFT_READY'
row['scope']+=' 新90/94 A707 actualSUCCESS，真实e4thread逐两精确tuple三facetPASS/priorityUNKNOWN；B716沿5da独立thread一次新scope已派，freshC未派。四端点DRAFT实际ready未ZIP，生成时早于新A终态，不追改其历史receipt。'
row['distance_text']+=' A707已实际SUCCESS，root实读10798chars/两原目标math/formal/bindingPASS并处置，nonempty/disjoint N本身非D3证明，实际source-interior Walk负责覆盖；136BFS为精选根而非全根。B716/storeendpoint90_94_B_actual已沿真实独立5da20cd4-ab3f-4327-9df5-8d0e80d7eee3一次shared新两scope派出，freshC未派，不继承旧review。四端点HTML/.txt各35670B/Word9937B、136selectedlinks、.020191577CPU实际DRAFTready，0ZIP；draft原生成时newA=false只属历史渲染，当前Wiki明确actualA=PASS，不重渲染。published16/1920接口仅只读门在途，正式receipt未返，不记已验结论/新图/本地计算。'
row['lesson_and_restart_condition']+=' 当前只待同一B716实际终态后由root决定唯一distinctfreshC，A707已完不再等/重试；四端点材料可阅但未冻结，旧packet不动。未来published16/1920 gate未返不得推定数学接口或竞争结论，也不启动任何新研究。'
evidence=[V+'REPLICATION90_94_A_GEMINI_RAW.json',V+'REPLICATION90_94_A_DISPOSITION.md',V+'REPLICATION90_94_B_REQUEST.json',E+'_DRAFT_RECEIPT.json',E+'.html',E+'.html.txt',E+'.docx'];assert all((R/p).is_file()for p in evidence)
row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+evidence));raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip());L=read('research-wiki/DDP_METHOD_LEDGER.json');assert tuple(L[k]for k in keys)==(420,150,41,44)
block=f'''<!-- {B} -->
# 当前：90/94新A707实际PASS，B716在途、freshC未派；四端点专家DRAFT已ready

同Goal ACTIVE，ledger420只复用[q8现节点](experiments/{ident}.md)；150合法named／41参数／Lean44、stage46／38、outside44／37、known43/main103_3/global0不变，0新method或图。

A707实际SUCCESS，root全读10798chars与90/380324/16942770、94/397228/18311670两精确tuple math/formal/bindingPASS、priorityUNKNOWN，e4thread一次新scope，707已终态不重试。B716/storeendpoint90_94_B_actual沿独立5da20cd4-ab3f-4327-9df5-8d0e80d7eee3已真实派发一次sharedcall；freshC未派，不继承86/98旧C。

四端点专家HTML/source各35670B、Word9937B、136selectedlinks实际ready，DRAFT snapshot150/41/44，0ZIP/未freeze；其原render早于实际A终态，历史receipt不追改，当前A通过以本Wiki与raw处置为准。本次不重渲染/重检links/图/Lean。两个published16/1920接口只读门尚未返回正式gate receipt，不能记已验结论/新图/本地计算；不启动新研究。

'''
gap=W/'gap_map.md';assert B not in gap.read_text();gap.write_text(block+gap.read_text());comments=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';comments.write_text(comments.read_text()+f'\n\n## {now} 90/94实际A终态与B716、四端点已有草稿\n\n'+block.split('\n\n',1)[1])
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'New90_94A707actualSUCCESSe4thread10798chars2exacttuplemathformalbindingPASSpriorityUNKNOWNrootdispositionread_AterminalnoRetry;B716actualsharednewscope5da20threadpendingstoreendpoint90_94_B_actual_Cnotdispatched_noOldPASSinheritance. FourendpointDRAFTactualreadyhtmltxt35670eachWord9937links136CPU.020191577snapshot150_41_44zeroZIP_renderPredatesAterminal_historyPreserved_noRerender. Futurepublished16_1920readonlyGatesInProgressNoFormalReceiptNoConclusionNoNewGraphLocalCompute. Existingq8oneRowLedger420counts150_41Lean44stage46_38outside44_37known43main103_3global0unchanged0newMethod_noMathGraphBFSLeanSolverWebPaidCallRootownedFrozenWrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W);(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
assert row['title']in(W/'experiments'/f'{ident}.md').read_text() and len(calls)==4 and all(c['returncode']==0 for c in calls)
receipt=dict(status='PASS_MINIMAL_EXISTING_Q8_90_94_ACTUAL_A_PASS_B716_PENDING_FOUR_ENDPOINT_DRAFT_READY',updated_UTC=now,ledger_records=420,records_added=0,records_updated=1,named_legal_graphs=150,legal_parameter_pairs=41,complete_formula_Lean=44,stage_graphs=46,stage_pairs=38,outside_graphs=44,outside_pairs=37,known_publicly_dominated=43,global_records=0,
 A707='ACTUAL_SUCCESS_TWO_EXACT_TUPLES_THREE_FACETS_PASS',A_thread=a['threadId'],A_response_chars=len(a['content']),B716='ACTUALLY_DISPATCHED_ONE_SHARED_NEW_SCOPE_PENDING',B_thread=b['threadId'],freshC='NOT_DISPATCHED',old_PASS_inherited=False,
 four_endpoint_DRAFT_ready=True,HTML_source_Word_bytes=[35670,35670,9937],selected_paths136_from_existing_receipt=True,draft_render_predates_actual_A=True,new_ZIP=0,future16_1920_gates='READ_ONLY_PENDING_NO_FORMAL_RECEIPT_NO_VALIDATED_CONCLUSION',
 evidence_paths_checked=len(evidence),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',static_scope_check='PASS_counts_existingNode_and_fourActualHelperCalls',new_graph_Lean_method_increments=[0,0,0],math_graph_BFS_Lean_solver_web_paid_runs_this_sync=0,expert_rerender_or_full_links_recheck=False,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
