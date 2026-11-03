from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';A=S+'reviews/DIAGONAL_REALLOCATION_DEGREE83_A_';E='expert_review_current/DIAGONAL_REALLOCATION_THREE_RESULTS_20261101'
B='DIAGONAL_THREE_ACTUAL_SECOND_A_PASS_B608_PENDING_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
a=json.loads((R/(A+'GEMINI_RAW.json')).read_text())['structuredContent'];draft=json.loads((R/(E+'_DRAFT_RECEIPT.json')).read_text())
assert a['status']=='SUCCESS' and a['threadId']=='e4b6c102-1c55-4739-82e4-d281acc2e835'
footers=[json.loads(x)for x in re.findall(r'```json\s*([\s\S]*?)```',a['content'])];footer=next(x for x in footers if 'original_targets'in x)
targets=footer['original_targets'];expected={(26,3,7532,97750),(82,3,346516,14204970),(83,3,350742,14547195)}
assert {(x['Delta'],x['D'],x['n'],x['m'])for x in targets}==expected
assert all(all(x[k]=='PASS'for k in ['math','formal','binding'])and x['priority']=='UNKNOWN'for x in targets)
assert draft['snapshot']==dict(named=146,parameters=37,Lean=40,stage_graphs=42,stage_parameters=34) and draft['actual_kernel_complete_count']==3 and draft['delivery_archives_created']==0
review=dict(status='ACTUAL_SUCCESS_EXPLICIT_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',cell=599,thread=a['threadId'],actual_additional_shared_calls=1,total_A_shared_calls=2,
    target_verdicts=targets,scope='original83plusprior2finalkernelnewexplicitscope',first_A2_historical_formal_pending_preserved=True,
    final_C=False,three_independent_calls_claimed=False,priority='UNKNOWN',raw=A+'GEMINI_RAW.json',disposition=A+'DISPOSITION.md')
bjob=dict(status='ACTUAL_THREE_ORIGINAL_DISPATCH_PENDING_NEW_THREAD_NOT_RETURNED',cell=608,store='diagonal_reallocation_B3_review',actual_calls=1,
    target_tuples=sorted([list(x)for x in expected]),thread=None,verdict=None,old_C_inherited=False)
for r in rows:
    m=r['other_metrics'];m['diagonal_reallocation_A83_continuation']=copy.deepcopy(review);m['diagonal_reallocation_B3_current_job']=copy.deepcopy(bjob)
    m['all_new_reallocation_three_A_actual_complete']=True;m['all_new_reallocation_three_final_reviews_complete']=False
    x=m['diagonal_reallocation_two_targets_pending_proof_and_review'];x.update(external_A='SECOND_EXPLICIT_A_CALL_ACTUAL_MATH_FORMAL_BINDING_PASS',external_A_thread=a['threadId'],formal_A='PASS_SECOND_SCOPE_FIRST_PENDING_HISTORY_PRESERVED',external_B='CELL608_ACTUAL_DISPATCH_PENDING',external_fresh_C='NOT_DISPATCHED')
    p=m['diagonal_fill_reallocation_prediction']['new_review_status'];p.update(external_A='SECOND_EXPLICIT_A_CALL_ACTUAL_MATH_FORMAL_BINDING_PASS',external_A_thread=a['threadId'],formal_A='PASS_SECOND_SCOPE_FIRST_PENDING_HISTORY_PRESERVED',external_B='CELL608_ACTUAL_DISPATCH_PENDING',external_fresh_C='NOT_DISPATCHED')
    for g in m['validated_graph_instances']:
        if g['n']in [7532,346516,350742]:g.update(external_A='ACTUAL_SECOND_SHARED_A_SCOPE_MATH_FORMAL_BINDING_PASS',external_A_thread=a['threadId'],external_A_formal='PASS_EXPLICIT_SECOND_SCOPE',external_A_call=599,external_B='CELL608_ACTUAL_DISPATCH_PENDING_NO_VERDICT',external_fresh_C='NOT_DISPATCHED',external_B_C_complete=False)
    r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+[A+'GEMINI_RAW.json',A+'DISPOSITION.md',E+'_DRAFT_RECEIPT.json']))
    r['lesson_and_restart_condition']+=' A599现actualSUCCESS，e4b6c102同Athread第二次明确sharedcall，三精确tuple各math/formal/bindingPASS、priorityUNKNOWN；首A2当时formalPENDING保留为历史，不冒3独立calls或finalC。新B3 cell608/storediagonal_reallocation_B3_review已真实派发一次，新thread和结果待返，C3未派；不重付费call/图/Lean。专家builder实际DRAFT146/37/Lean40、三kernelPASS与freeze入口ready但0ZIP，未重复prepare；实际新A结果由Wiki更新，DRAFT旧review快照不当live判定。q4small27..34仅公开门0图在途，q8window仍0图0queue，当前三图交付后再选参数。'
m=rows[0]['other_metrics'];m['future_q4_public_window27_34_only']=dict(status='ROOT_DISPATCHED_TO_GQ_PUBLIC_GATE_IN_PROGRESS',new_graphs=0,queue=0,new_method_claimed=False)
q8=rows[1];m=q8['other_metrics'];m['degree83_multiplicity2_single_target'].update(external_A='ACTUAL_EXPLICIT_SECOND_A_SHARED_SCOPE_MATH_FORMAL_BINDING_PASS',external_A_thread=a['threadId'],external_B='CELL608_ACTUAL_DISPATCH_PENDING',external_fresh_C='NOT_DISPATCHED')
m['completed_Lean_and_A_B_C_scope']='all5q8instancesLeancomplete;old3A_B_Ccomplete;new346516_350742secondAactualPASS/B608pending/Cnotdispatched'
m['new_reallocation_three_expert_delivery'].update(status='ACTUAL_DRAFT_PREPARED_KERNEL3_FREEZE_ENTRY_READY_ZERO_ZIP',snapshot=draft['snapshot'],
    actual_kernel_complete_count=3,freeze_implemented=True,freeze_executed=False,remaining_gate='B3actual/distinctfreshCactualthenrootfreezeauthorization',
    DRAFT_receipt_checked_UTC=draft['checked_UTC'],DRAFT_review_snapshot_not_live_authority=True,extra_prepare_or_render_run=False)
q8['title']='新规则三原目标kernel与第二次A逐目标全PASS；B3/608在途，freshC及冻结待'
q8['outcome_class']='THREE_NEW_RULE_ORIGINAL_KERNEL_BINDINGS_SECOND_A_PASS_B_PENDING_C_NOT_DISPATCHED'
q8['scope']+=' 最新A第二次明确call实际逐7532/346516/350742三tuple math/formal/bindingPASS，未认证全球priority；新B3/608已派在途，freshC未派，0新ZIP。'
q8['distance_text']+=' A599actualSUCCESS，thread e4b6c102-1c55-4739-82e4-d281acc2e835一次新增sharedscope逐三原tuple math/formal/binding全PASS，首A2formalPENDING仍历史原样。此为A第二call非3独立call/finalC。B3cell608一次实际派发、newthread/结果未返，freshC尚未派。专家DRAFT实际146/37/Lean40三kernelPASS/freeze入口ready，0新ZIP/未重复prepare。'
e=[A+'GEMINI_RAW.json',A+'DISPOSITION.md',E+'_DRAFT_RECEIPT.json','expert_review_current/build_diagonal_reallocation_three_results_20261101.py'];assert all((R/x).is_file()for x in e)
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
block=f'''<!-- {B} -->
# 当前：A第二明确scope三tuple逐math/formal/bindingPASS；B3/608在途，C未派，0新ZIP

同Goal ACTIVE，ledger420仅复用[7532](experiments/{ids[0]}.md)与[q8](experiments/{ids[1]}.md)两现节点，146／37／Lean40、stage42／34、outside40／33、known43/main103_3/global0不变。A599实际SUCCESS，同e4b6c102thread第二次sharedcall，三原tuple7532/346516/350742各math/formal/bindingPASS、priorityUNKNOWN；首A2formalPENDING是历史，不改为过去已审，不冒3calls或finalC。

新B3已真实发cell608/storediagonal_reallocation_B3_review，一次三原目标scope，新thread/结果待返，C3未派，不继承旧q8C。专家DRAFT实际146/37/Lean40三kernelPASS、freeze入口ready但0ZIP；未重复prepare或数学检查，须B/freshC实际齐再root授权freeze。q4small27..34仅公开门在途0图，q8window四端点仍候选0图/0queue。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} A第二明确scope实际三目标全PASS；B608已派在途，保持finalC与冻结边界

原Wiki只复用[7531/7532节点](experiments/{ids[0]}.md)、[q8节点](experiments/{ids[1]}.md)，ledger420/0新行，146图／37参数、stage42／34、Lean40、outside40／33、known43/main103_3/global0不变。实际读取A599完整raw及rootdisposition，机器footer精确(26,3,7532,97750)/(82,3,346516,14204970)/(83,3,350742,14547195)逐math/formal/bindingPASS、priorityUNKNOWN。thread e4b6c102-1c55-4739-82e4-d281acc2e835与首A相同，本轮是第二次明确sharedcall，新增83original与前两finalkernel状态；首A2mathbindingPASS/formalPENDING原样留历史，未把两calls冒成三独立审阅或finalC。

root处置接受exact原声明/FinalClaims/Finlabels/Auditstd3与外部绑定；真实290/66/68BFS同未测4160/4158off分界保留，[0,21]producer归属和fresh7532实际7242→0见证更正不重call。108.234539769与9.560036958是完整执行batch总CPU含准备/失败/binding，不仅成功编译时间。

新B三原目标一次actualdispatch cell608/storediagonal_reallocation_B3_review，独立新thread待返回，当前无verdict；distinctfreshC3未派，旧q8C不能代入。实际DRAFT_RECEIPT146/37/Lean40、三per-targetkernelcomplete、freeze代码入口ready但deliveryarchives0已读；其中review状态是prepare时历史快照，liveA现状按本次实际raw更新，未重复prepare/1453links/Word/图/Lean。需新B及freshC实际齐、root明确再授权freeze，现无新ZIP。q4小27..34purepublicgate由gq在途0图，q8大window0图/队列，三图当前交付结束后再选新参数。rootowned及旧冻结包未改。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'ActualA599SUCCESSsamee4b6c102threadsecondexplicitsharedcall/threeexact7532_346516_350742tuplemath_formal_bindingPASS_priorityUNKNOWN;firstA2formalPENDINGhistorypreserved/not3calls/notfinalC. NewB3actualdispatchcell608storediagonal_reallocation_B3_review/threadverdictpending/C3notdispatched/nooldCinherit. DRAFTreceipt146_37Lean40kernel3PASSfreezeentryready0ZIPread/noextrareprepare. Q4small27_34publicgate0graphinprogress/Q8window0graphsqueue. Ledger420twoexistingrows146_37Lean40stage42_34unchanged/0mathBFSLeanruns/rootedits/frozenpacketwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_ACTUAL_SECOND_A_THREE_TARGETS_B608_DISPATCH_PENDING_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=146,legal_parameter_pairs=37,stage_graphs=42,stage_pairs=34,complete_formula_Lean=40,outside40_33=True,known43_main103_3_global0=True,
    A599_actual_status='SUCCESS',A_thread=a['threadId'],A_total_actual_shared_calls=2,A_this_continuation_calls=1,three_precise_tuple_math_formal_binding_PASS=True,first_A2_formal_pending_history_preserved=True,finalC_claimed=False,
    B3='CELL608_ACTUAL_DISPATCH_PENDING_THREAD_AND_VERDICT',B_thread=None,C3='NOT_DISPATCHED',new_ZIP=0,extra_expert_prepare=0,future_window_graphs_or_queue=0,evidence_paths_checked=len(e),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
