from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';BRAW=S+'reviews/DIAGONAL_REALLOCATION_THREE_TARGETS_B_'
PUB=S+'public_baseline_audit/Q4_NEW_ROLE_REPLICATION_WINDOW27_34_20261101';T=S+'retained_edge_transfer/polarity_product2_8_helper_barrier/'
BASE='DIAGONAL_B_ACTUAL_C618_PENDING_Q4_STOP_PRODUCT_BARRIER_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101','ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101']
rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
raw=json.loads((R/(BRAW+'GEMINI_RAW.json')).read_text())['structuredContent'];assert raw['status']=='SUCCESS' and raw['threadId']=='67beb729-7e25-457e-be3a-019fc820466d'
footer=next(json.loads(x)for x in re.findall(r'```json\s*([\s\S]*?)```',raw['content'])if 'original_targets'in json.loads(x))
expected={(26,3,7532,97750),(82,3,346516,14204970),(83,3,350742,14547195)};targets=footer['original_targets']
assert {(x['Delta'],x['D'],x['n'],x['m'])for x in targets}==expected
assert all(all(x[k]=='PASS'for k in ['math','formal','binding'])and x['priority']=='UNKNOWN'for x in targets)
assert footer['thread_id']!='67beb729-7e25-457e-be3a-019fc820466d'
window=json.loads((R/(PUB+'.json')).read_text());th=json.loads((R/T/'INDEPENDENT_RESULT.json').read_text());term=json.loads((R/T/'INDEPENDENT_TERMINAL.json').read_text())
assert window['status']=='ALL_EIGHT_Q4_ROLE_REPLICATION_ENDPOINTS_BLOCKED_STOP' and len(window['cases'])==8 and not window['recommended_endpoints']
assert all(x['margin']<0 and x['status']=='BLOCKED'for x in window['cases'])
assert th['status']=='SUPPORTED_PAPER_ROUTE_BARRIER_SCALAR_PASS' and th['excluded_caps']==[27,28,29,30]
review=dict(status='ACTUAL_SUCCESS_THREE_PRECISE_ORIGINAL_MATH_FORMAL_BINDING_PASS',cell=608,actual_calls=1,
    thread=raw['threadId'],authoritative_thread_source='MCPstructuredContent.threadId',A_thread='e4b6c102-1c55-4739-82e4-d281acc2e835',thread_distinct_from_A=True,
    rejected_generated_footer_thread=footer['thread_id'],generated_footer_thread_not_used=True,target_verdicts=targets,priority='UNKNOWN',not_final_C=True,
    source_receipt_review_not_new_literal_parse=True,new_graph_field_BFS_Lean_runs=0,raw=BRAW+'GEMINI_RAW.json',disposition=BRAW+'DISPOSITION.md')
cjob=dict(status='ONE_DISTINCT_FRESH_C_ACTUAL_DISPATCH_PENDING_NO_RETURNED_THREAD_OR_VERDICT',cell=618,store='diagonal_reallocation_C3_review',actual_calls=1,thread=None,
    target_tuples=sorted([list(x)for x in expected]),must_differ_from_actual_A_and_B=['e4b6c102-1c55-4739-82e4-d281acc2e835',raw['threadId']],
    excludes_generated_wrong_B_footer_id=True,old_C_inherited=False,freeze_authorized_before_return=False)
small=dict(status=window['status'],conditional_n='290Delta-8',conditional_m='97750+7225*(Delta-26)',
    cases=[{k:x[k]for k in ['Delta','conditional_n','conditional_m','best_checked_guarantee','margin','status']}for x in window['cases']],
    blocker27_32='publishedq2xq8polarityproductand325absoluteproductreplication:325Delta',blocker33_34='Delormeq32folded33825plus1025percopy',
    CPU=window['CPU_seconds'],CPU_budget=5,primary_batches=1,primary_queries=3,decision='STRICT_PUBLIC_COMPETITION_STOP_NO_PRODUCTION',new_graphs=0,queue=0,
    PolarStar_q23_d8_correct_n=9954,old11060_not_legal_IQ=True,
    public35875_credit='Delorme1985q32degree33order33825+2*1025absolutevertexcopies;notanewlyestablishedMizunoD3package',
    old35875_value_and_known_nonrecord_counts_changed=False,report=PUB+'.md')
for row in rows[:2]:
    m=row['other_metrics'];m['diagonal_reallocation_B3_current_job']=copy.deepcopy(review);m['diagonal_reallocation_fresh_C3_current_job']=copy.deepcopy(cjob)
    m['all_new_reallocation_three_A_B_actual_complete']=True;m['all_new_reallocation_three_final_reviews_complete']=False
    m['diagonal_reallocation_two_targets_pending_proof_and_review'].update(external_B='ACTUAL_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_B_thread=raw['threadId'],external_fresh_C='CELL618_ACTUAL_DISPATCH_PENDING')
    rowp=m['diagonal_fill_reallocation_prediction']['new_review_status'];rowp.update(external_B='ACTUAL_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_B_thread=raw['threadId'],external_fresh_C='CELL618_ACTUAL_DISPATCH_PENDING')
    for g in m['validated_graph_instances']:
        if g['n']in [7532,346516,350742]:g.update(external_B='ACTUAL_SUCCESS_MATH_FORMAL_BINDING_PASS',external_B_thread=raw['threadId'],external_B_thread_from_MCP=True,external_fresh_C='CELL618_ACTUAL_DISPATCH_PENDING_NO_VERDICT',external_B_C_complete=False)
    row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+[BRAW+'GEMINI_RAW.json',BRAW+'DISPOSITION.md',PUB+'.md',PUB+'.json',PUB+'.py']))
    row['lesson_and_restart_condition']+=' 新B608实际逐三精确tuple math/formal/bindingPASS，真实MCPthread67beb729…与A e4b6c102…不同；generatedfooter自称b41f…非真实metadata已按root处置拒用，不影响数学/不加paidcall。唯一freshC已实际派cell618/storediagonal_reallocation_C3_review，thread/verdict待返并须异真实A/B，未返不freeze。小q4window27..34实际八cap全被公开正向构造阻断，严格STOP/0图；这选择更强公开q2×q8源作纸面helper障碍，而非盲续27..30。大84..98仍候选0图/queue，当前三图交付后再选。'
rows[0]['other_metrics']['future_q4_public_window27_34_only']=small
q8=rows[1];m=q8['other_metrics'];m['degree83_multiplicity2_single_target'].update(external_B='ACTUAL_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_B_thread=raw['threadId'],external_fresh_C='CELL618_ACTUAL_DISPATCH_PENDING')
m['new_reallocation_three_expert_delivery'].update(remaining_gate='actualdistinctfreshC3PASSthenrootexplicitfreezeauthorization',status='DRAFT_READY_A_B_ACTUAL_PASS_FRESH_C618_PENDING_ZERO_ZIP')
q8['title']='新规则三原目标kernel/A/B逐目标PASS；唯一freshC618在途，优先权UNKNOWN、0新ZIP'
q8['outcome_class']='THREE_NEW_RULE_KERNEL_A_B_ACTUAL_PASS_FRESH_C_PENDING'
q8['scope']+=' 新B608真实MCPthread67beb729…实际三目标PASS，generatedfooter b41f…身份拒用；唯一freshC618在途，不复用旧C或提前freeze。'

bar=rows[2];m=bar['other_metrics'];m['polarity_product2_8_fixed_mandatory_freeedge_helper_barrier']=dict(
    status=th['status'],prediction_saved_before_independent_attack=True,source='genuineloopedGQ2andGQ8polarityproductSwithproductselfloopsremoved',
    source_order=8775,source_max_degree=27,absolute_product_code=325,old_noncenter_count=8450,center_mandatory_degree=26,noncenter_mandatory_degree=27,
    uniform_copy_r='integer>=0',cap='27+r',free_set='oldCplusall325rclones',free_spare_slots='r+1',
    fixed_all_source_and_mandatory_clone_edges=True,arbitrary_free_free_edges_allowed=True,arbitrary_nonempty_finite_helper_batch_allowed=True,
    hard_targets='(AminusO_A)timesO_B',hard_target_count=650,pin_mandatory_direct_bound=2,pin_mandatory_radius2_bound=6,
    per_helper_necessary='650<=(6+2r)*p_h+2*sum_{g~h}p_g',summed_necessary='650<=2*(r+15)^2',maximizing_helper_degree=12,
    excluded_r=[0,1,2,3],excluded_caps=[27,28,29,30],r3_shortfall=2,r4_cap31='NOT_EXCLUDED_NO_SEARCH_NO_EXISTENCE_RESULT',
    arbitrary_class_ownership_or_repeated_copies_handled=True,both_end_degree_costs_respected=True,
    source8775_graph_generated=False,not_new_framework_or_graph_or_Lean=True,global_N_bound=False,current_three_target_A_B_C_scope=False,
    scalar_runs=1,reported_time_process_time_CPU=0.0,CPU_measurement_below_resolution=True,actual_zero_cost_claimed=False,
    independent_complementary_2_6_check='f9paperonlySUPPORTED0tools',new_graph_field_geometry_BFS_Lean_solver_or_paid_review_runs=0,
    open_scopes=['changeoromitmandatoryedges','nonuniformorincompletecopying','differentcodeorsource','concretejointcap31rule'],
    prediction=T+'PREDICTION_AND_PROOF.md',independent_NOTE=T+'INDEPENDENT_NOTE.md',independent_RESULT=T+'INDEPENDENT_RESULT.json',independent_TERMINAL=T+'INDEPENDENT_TERMINAL.json')
bar['title']='分接口局部障碍：q8满code多copy/free-edge界及公开q2×q8源helper路线界，非全局N上界'
bar['outcome_class']='SCOPED_Q8_AND_PUBLISHED_PRODUCT_LOCAL_BARRIERS_SUPPORTED_NO_GRAPH_LEAN_OR_THREE_TARGET_REVIEW_CLAIM'
bar['scope']+=' 另一个独立接口是公开真实loopedGQ2×GQ8的S8775/C325，而非前述filledH/matching条件的自动特例；保全部mandatory源/clone边、uniformr、允许任意F-F和非空helperbatch在cap27+r需650≤2(r+15)^2，只排r0..3。该额外范围不宣称globalN或P33/F9结论，不在当前三图Cscope。'
bar['distance_text']+=' 新公开q2×q8接口：hardX650，每实际freepin直达≤2、两mandatory步≤6，所有helper短路分类及双计数给650≤2(r+15)^2；r0..3界450/512/578/648严格不足，r3差2，cap31/r4未排且没搜。独立paper+f9零工具2/6核对SUPPORTED，仅1tiny整数scalar读数0.0低于计时分辨率，不当零实际成本；0source8775/field/BFS/Lean/solver/新图。'
bar['positive_guarantees'].append('q2×q8旧C独立、26N两两不交且325×26=8450恰分割所有非C点；uniformr使hardX650全饱和。首h-f花掉f一个spare只余r个peer，因此每pin≤6+2r；经helper只余两步每pin≤2，undirected双计数消去任意helperbatch/重复classowner。')
bar['unclosed_gap']=bar['unclosed_gap'].replace('新26度7532预测恰改变17条mandatoryclone-filler边，不能用本barrier先验否定；未验收。','新7532及q8/346516、350742已实际数学/具体Lean通过；它们改变或基于改变后的mandatory规则，不是本保边障碍反例。')
bar['unclosed_gap']+=' 新product界cap31未排不等于有构造，不启动r4；需真实joint pin/helper/Fpeer规则，非只正上界。旧q8各自scope保留，不能混用2/6系数或hardX于别源。'
bar['lesson_and_restart_condition']+=' 最新实际publicgate已停止弱q4newrole27..34全部端点；转较强公开product源的明确hardX路线问题，独立支持后关闭其固定mandatory27..30任何非空helperbatch，而非排所有小图。cap31只在出现具体联合连接规则时再考虑，未派solver/图；当前三图交付完成前不盲续。'
te=[T+x for x in ['PREDICTION_AND_PROOF.md','INDEPENDENT_NOTE.md','INDEPENDENT_RESULT.json','INDEPENDENT_TERMINAL.json','INDEPENDENT_SCALAR.py']];bar['evidence_paths']=list(dict.fromkeys(bar['evidence_paths']+te+[PUB+'.md',PUB+'.json',PUB+'.py']))
e=[BRAW+'GEMINI_RAW.json',BRAW+'DISPOSITION.md',PUB+'.md',PUB+'.json',PUB+'.py']+te;assert all((R/x).is_file()for x in e)
rawrows=W/f'updates/{BASE}_ROWS.json';rawrows.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',rawrows).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
block=f'''<!-- {BASE} -->
# 当前：新三目标B实际PASS，真实thread67beb；唯一freshC618待返；小窗口STOP及固定product障碍

同Goal ACTIVE，ledger420复用3现节点/0新行，146／37／Lean40、stage42／34、outside40／33、known43/main103_3/global0不变。新B608三精确tuple math/formal/bindingPASS/priorityUNKNOWN；真实MCPthread67beb729-7e25-457e-be3a-019fc820466d异A e4。生成footer自称b41f…错误，root处置拒用不加paidcall。唯一freshC已实际派cell618/storediagonal_reallocation_C3_review，thread/verdict待返须异真实A/B，未返不freeze，0新ZIP。

[q4小window](experiments/{ids[0]}.md)27..34全8cap被公开325Δ及q32fold阻断，.103912025CPU/5/3queries，严格STOP/0图。IQ23/8正确9954，35875/35可核Delormeq32+2copies归属，不冒Mizuno package；旧非record值/计数不变。

[现barrier节点](experiments/{ids[2]}.md)新增另一个固定接口：真实公开loopedGQ2×8/S8775/C325 uniformr，保mandatory源/clone边但任意F-F及非空helperbatch，hardX650、每pin2/6profile、650≤2(r+15)²排r0..3/cap27..30，r3差2。cap31/r4未排且未跑，不是globalN/当前三图Cscope；1tiny scalar0.0为低于计时分辨率，不当零成本，0source8775graph/field/BFS/Lean/solver。大窗口仍0生产/queue，当前三图交付后再选参数。

'''
p=W/'gap_map.md';assert BASE not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 实际独立B逐三目标PASS，唯一C618在途；小窗口停止引出更强source的局部路线障碍

本次只复用[7532机制](experiments/{ids[0]}.md)、[q8机制](experiments/{ids[1]}.md)、[现局部barrier节点](experiments/{ids[2]}.md)，ledger420/0新方法行，146／37／Lean40、stage42／34、outside40／33、known43/main103_3/global0不变。实际B608完整raw/footer三精确tuple math/formal/bindingPASS、priorityUNKNOWN已读；真实MCPstructuredContent.threadId=67beb729-7e25-457e-be3a-019fc820466d，与A e4不同。footer生成b41f…不是MCP身份，按rootdisposition拒用；数学判定不变、不重付费call、不把review开头措辞当新完整边表parse/BFS/Lean。唯一distinctfreshC实际已发618/storediagonal_reallocation_C3_review，thread/verdict未返必须异真实A/B，未返不freeze；旧C不继承。

新q4/G1 role复制窗口27..34候选290Δ−8全8cap已被明确公开正向配方阻断，CPU.103912025/5/一次3queries，0图严格STOP。27..32的公开q2×q8 product8775及325code复制给325Δ，33/34的q32fold给33825/34850。IQq23,d8合法n9954，旧11060对应非法d9不再用；35875/35的可核primary配方是Delorme1985q32base33825+2×1025，非新Mizuno D3package，旧已知非record数值与计数不变。当前35/20580节点本来已正确列Delorme，未重复改那行。有限作者索引缺条目不是无图证明，本停止结论依赖正向构造而非负检索。

这改变下一问题：不产更弱q4copies，针对更强公开S8775的实际conditional接口先纸面问helper增广。事前PRED及独立attack已读：loopedGQ2/8 degree-row3/9、absolute5/65，删productloops后C325各26degree、其26N分割U8450，uniformr令U在cap27+r饱和。hardX=(A减OA)×OB有650，任意freepin旧直达≤2、两mandatory步≤6；首helperpin已用free端1slot，至多r个Fpeer，覆盖≤6+2r；经另一helper只余两步每pin≤2。所有允许短路与双端成本分类、undirected求和给650≤2(r+15)²，r0..3 maxima450/512/578/648，cap30严格差2。任意helperbatch、重复copy/owner和F-F都已计；cap31/r4未排不等于可实现，只能在有具体joint pin/helper/peer规则时再考虑，0搜索/图任务。

新barrier是独立固定source接口，不把旧q8filledmatching条件自动套过来；不排删改mandatory、nonuniform/incompletecopy、不同code/source或globalN，且不在当前三图A/B/Cscope。唯一tiny整数检查time.process_time0.0低于分辨率，不当0真实成本；f9额外2/6纸面支持0工具，0S8775graph/field/BFS/Lean/solver/record。大84..98window仍0生产/queue，当前三图交付后再选，根状态/旧包未动。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'ActualB608threeexacttuplemath_formal_bindingPASSpriorityUNKNOWN/MCPthread67beb729distinctA_e4/generatedfooterb41fwrongrejected/noextracall/newparse. UniqueC618actualdispatchpendingthreadverdict/mustdifferactualA_B/nofreeze. Q4window27_34all8publicblockedSTOP/.103912025CPU3queries/IQ23_8=9954/35_35875Delormeq32+2copiesnotnewMizunopackage/countsunchanged. Separatefixedpublishedproduct2x8S8775C325barrierhardX650pin2_6/650<=2(r+15)^2/excludesr0_3cap27_30/r3short2/r4cap31notexcludednotrun/scalartime0.0belowresolutionnotzerocost/notglobalN/not3targetCscope. ledger420threeexistingrows146_37Lean40stage42_34unchanged/0newgraphs_mathruns_rootedits_frozenpacketwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{BASE}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_ACTUAL_B_C618_PENDING_Q4_ALL_BLOCKED_AND_SEPARATE_FIXED_PRODUCT_BARRIER_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=3,named_legal_graphs=146,legal_parameter_pairs=37,stage_graphs=42,stage_pairs=34,complete_formula_Lean=40,outside40_33=True,known43_main103_3_global0=True,new_graphs=0,new_Lean=0,new_frameworks=0,
    B_actual_status='SUCCESS',B_actual_MCP_thread=raw['threadId'],B_rejected_generated_footer_thread=footer['thread_id'],B_actual_shared_calls=1,three_precise_tuple_math_formal_binding_PASS=True,
    C3='CELL618_ACTUAL_DISPATCH_PENDING_THREAD_VERDICT',C_thread=None,new_ZIP=0,Q4window='ALL8_BLOCKED_STRICT_STOP_ZERO_GRAPH',Q4window_CPU=window['CPU_seconds'],IQ23_8_correct=9954,public35875_credit='Delorme1985q32plus2copies',
    new_local_barrier_scope='fixedgenuineq2xq8publishedinterface_uniformr_allmandatoryedges_arbitraryF_F_andnonemptyhelperbatch',barrier_excluded_caps=[27,28,29,30],cap31='NOT_EXCLUDED_NO_RUN',barrier_reported_scalar_CPU=0.0,barrier_scalar_below_resolution_not_zero_cost=True,barrier_in_three_target_review_scope=False,
    evidence_paths_checked=len(e),actual_helper_calls=f'research-wiki/updates/{BASE}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{BASE}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
