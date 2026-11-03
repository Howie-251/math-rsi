from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';C=S+'reviews/DIAGONAL_REALLOCATION_THREE_TARGETS_FINAL_C_'
T=S+'retained_edge_transfer/polarity_product2_8_helper_barrier/';Z=T+'controlled_q2_square_clique5_230/'
B='DIAGONAL_FINAL_C_ACTUAL_CALIBRATION230_CAP31_PAPER_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101','ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101']
rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
c=json.loads((R/(C+'GEMINI_RAW.json')).read_text())['structuredContent'];assert c['status']=='SUCCESS' and c['threadId']=='53b69de0-5f49-43ba-b3ee-1b37db7c804a'
assert c['threadId']not in ['e4b6c102-1c55-4739-82e4-d281acc2e835','67beb729-7e25-457e-be3a-019fc820466d']
footer=next(json.loads(x)for x in re.findall(r'```json\s*([\s\S]*?)```',c['content'])if 'original_targets'in json.loads(x));targets=footer['original_targets']
assert {(x['Delta'],x['D'],x['n'],x['m'])for x in targets}=={(26,3,7532,97750),(82,3,346516,14204970),(83,3,350742,14547195)}
assert all(all(x[k]=='PASS'for k in ['math','formal','binding'])and x['priority']=='UNKNOWN'for x in targets)
z=json.loads((R/Z/'RESULT.json').read_text());zt=json.loads((R/Z/'TERMINAL.json').read_text());assert z['status']==zt['state']=='ALL_PREDECLARED_CALIBRATION_PREDICTIONS_PASS'
assert z['final']['n']==230 and z['final']['m']==1035 and z['final']['degree_histogram']=={'9':230} and z['final']['all_roots_eccentricity3']
assert z['prefix']['missed_within_radius3']==120 and z['portfolio_graph_increment']==z['new_parameter_increment']==z['Lean_increment']==0
finalC=dict(status='ACTUAL_SUCCESS_DISTINCT_FRESH_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',cell=618,actual_shared_calls=1,thread=c['threadId'],
    authoritative_metadata='MCPstructuredContent.threadId',actual_A_thread='e4b6c102-1c55-4739-82e4-d281acc2e835',actual_B_thread='67beb729-7e25-457e-be3a-019fc820466d',distinct_from_actual_A_B=True,
    target_verdicts=targets,priority='UNKNOWN',old_C_inherited=False,new_graph_field_BFS_Lean_solver_runs=0,
    excludes=['q4windowSTOP','q8futurewindow','product2x8helperbarrier','cap31rowrefinement','230calibration'],
    disposition_clarification='clone-to-other-fillerHpathmustexitthroughUonlyforlength<=3;longerwalksnotasserted',raw=C+'GEMINI_RAW.json',disposition=C+'DISPOSITION.md')
for r in rows[:2]:
    m=r['other_metrics'];m['diagonal_reallocation_fresh_C3_current_job']=copy.deepcopy(finalC);m['all_new_reallocation_three_final_reviews_complete']=True
    m['all_row_original_A_B_distinctfreshC_complete']=True
    m['diagonal_reallocation_two_targets_pending_proof_and_review'].update(external_fresh_C='ACTUAL_DISTINCTFRESH_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_fresh_C_thread=c['threadId'],final_reviews_complete=True)
    p=m['diagonal_fill_reallocation_prediction']['new_review_status'];p.update(external_fresh_C='ACTUAL_DISTINCTFRESH_THREE_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_fresh_C_thread=c['threadId'],final_reviews_complete=True)
    for g in m['validated_graph_instances']:
        if g['n']in [7532,346516,350742]:g.update(external_fresh_C='ACTUAL_SUCCESS_EXPLICIT_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_final_C_thread=c['threadId'],external_final_C_distinct_from_actual_A_B=True,external_B_C_complete=True,new_rule_external_A_B_C_complete=True,public_priority='UNKNOWN')
    r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+[C+'GEMINI_RAW.json',C+'DISPOSITION.md']))
    r['lesson_and_restart_condition']+=' 唯一finalC618已actualSUCCESS，真实thread53b69de0…异实际A e4与B67beb，三原目标逐math/formal/bindingPASS，priorityUNKNOWN。当前三具体图数学/独验/kernel/Audit/新A/B/freshC全部完成；新barrier/cap31/230只是另研究，不借C通过。root已授权一次新专家freeze尚未执行，未声称ZIP存在；本增量后停止Wiki写入等待实际冻结回执，不重生成图/运行核验，Goal仍ACTIVE。'
q4=rows[0];q4['title']='GQ(4,4)新7532具体kernel与A/B/distinctfreshC完成；精确优先权UNKNOWN'
q4['outcome_class']='OLD7531_AND_NEW7532_COMPLETE_MATH_KERNEL_A_B_DISTINCTFRESHC_PRIORITY_UNKNOWN'
q4['unclosed_gap']+=' 最新三图finalC逐原目标实际PASS；新7532数学/kernel/Audit/A/B/C均完成，精确公开priority与人工反馈仍待，不当Goal完成。'
q8=rows[1];m=q8['other_metrics'];m['degree83_multiplicity2_single_target'].update(external_fresh_C='ACTUAL_DISTINCTFRESH_ORIGINAL_MATH_FORMAL_BINDING_PASS',external_final_C_thread=c['threadId'],external_A_B_C_complete=True)
m['completed_Lean_and_A_B_C_scope']='all5q8rowinstancesconcreteLean_A_B_distinctfreshCcomplete;futurewindow_and_barrier_toy_NOT_Ctargets'
m['new_reallocation_three_expert_delivery'].update(status='ROOT_ONE_FREEZE_EXPLICITLY_AUTHORIZED_NOT_EXECUTED_A_B_C_KERNEL_ALL_COMPLETE',
    root_explicit_one_freeze_authorized=True,freeze_CPU_budget=90,freeze_compression_level=1,freeze_executed=False,new_ZIP_exists_claimed=False,
    snapshot=dict(named=146,parameters=37,Lean=40),remaining_gate='actualexecutionandreceiptbeforeclaimZIP',old_frozen_packets_modified=False)
q8['title']='新规则7532/346516/350742数学/kernel/A/B/独立freshC全完成，已授权一次freeze尚未执行'
q8['outcome_class']='THREE_NEW_RULE_ORIGINAL_TARGETS_MATH_KERNEL_A_B_DISTINCTFRESHC_PASS_EXPERT_FREEZE_AUTHORIZED_NOT_RUN'
q8['scope']+=' finalC618真实thread53b69de0…分别异A e4/B67beb，精确三tuple全部math/formal/bindingPASS，非globallynew证书。当前两新q8实例外审闭合；旁支toy/barrier/window不在该Cscope，0额外图。'
q8['distance_text']+=' finalC618实际SUCCESS，MCPthread53b69de0-5f49-43ba-b3ee-1b37db7c804a独立于真实A/B，一次sharedcall逐三目标math/formal/bindingPASS+priorityUNKNOWN。只适用既有7532/346516/350742，不覆盖窗口/barrier/230校准；root一次专家freeze授权已给但尚未执行，未宣称新ZIP已存在。'

bar=rows[2];m=bar['other_metrics']
m['joint_helper_controlled_230_calibration']=dict(status=z['status'],purpose='smalljointbatchroutecomplementaritycalibration_notrecordattempt',
    literal_factor='15rowsloopedrelationai/ui/vi;A^3=4A+Jverified225pairs;nogeometricisomorphismasserted',
    source_n=225,source_m=1000,source_degree_histogram={'8':25,'9':200},source_BFS_roots=0,
    helper_rule='5helpersK5;hiowns5absolutecentersintheithrow',final_n=230,final_m=1035,final_regular_degree=9,final_exact_D=3,
    actual_final_BFS_roots=230,all_final_hist_predictions_match=True,final_hist_classes=z['final']['histogram_classes'],
    controlled_prefix_n=226,controlled_prefix_m=1005,prefix_BFS_roots=1,prefix_hist=[1,5,40,60],prefix_reached=106,prefix_missed_within_R3=120,
    prefix_missing_is_not_disconnectedness_claim=True,joint_batch_does_not_have_valid_singlehelper_D3_prefix=True,
    actual_CPU_rusage=z['CPU_seconds_rusage'],CPU_budget=5,portfolio_graph_increment=0,parameter_increment=0,Lean_increment=0,
    current_three_target_C_scope=False,implies_product2x8_or_cap31_feasible=False,extra_independent_audit_or_formalization=False,
    PRED=Z+'PREDICTION_AND_SCOPE.md',RESULT=Z+'RESULT.json',TERMINAL=Z+'TERMINAL.json',proof=Z+'PROOF.md')
m['product2x8_cap31_row_concentration_paper']=dict(status='INDEPENDENT_PAPER_SUPPORTED_NECESSARY_EXISTENTIAL_ROW_CONCENTRATION_NOT_CAP31_EXCLUSION',
    same_fixed_mandatory_uniformr_product_interface=True,new_uniqueness='distinctabsoluteBeta_binB:unique3walkbyGQpoint_nonincidentpolarlineprojection;atmostoneb-neighborwithin2ofBeta',
    class_count=325,owned_row_classes='distinctbased(a,b)classes;repeatedcopiescountonce',light_helper='eachof5Arowshasfewerthan8distinctownedclasses',
    light_helper_necessary='325<=(r+1)*p_h+sum_{g~h}p_g',if_all_helpers_light='325<=(r+14)^2',r4_cap31_all_light_contradiction='325<=324false',
    exact_conclusion='atleastonehelperhasatleast8distinctbasedclassesinoneabsoluteArow',every_helper_heavy_claimed=False,
    cap31_impossible_claimed=False,concentrated_ownership_existence_claimed=False,
    all_light_0_4_5_5_5_for_every_helper_excluded=True,controller_generated=False,
    new_scalar_subset_graph_field_BFS_Lean_solver_or_paid_review_runs=0,current_three_target_C_scope=False,
    prediction=T+'CAP31_ROW_CONCENTRATION_PREDICTION.md',independent_NOTE=T+'CAP31_ROW_CONCENTRATION_INDEPENDENT_NOTE.md')
m['polarity_product2_8_fixed_mandatory_freeedge_helper_barrier']['r4_cap31']='NOT_EXCLUDED;NECESSARY_SOME_HELPER_SOME_ROW_GE8_DISTINCT_CLASSES;NO_SEARCH'
bar['scope']+=' 新230是另一个literal15×15小校准：K5helpers联合成功但单helperprefix失败，不外推8775/cap31。cap31另paperrefinement只推出存在某helper某Arow至少8distinctclasses，绝非每helper都heavy或31不可行，0枚举/solver/图。均不属三图Cscope。'
bar['distance_text']+=' 230校准全部事前预测实测PASS，.027416CPU，完整230/1035/9regular/exactD3及全230根三类hist，首helper226prefix只达106/漏120，不能借futureK5当有效D3单点prefix。另cap31 GQ三walk唯一性支持all-light求和325≤(r+14)^2，r4要求325≤324矛盾，故至少某helper某row≥8类；不排31、不宣所有helperheavy。0portfolio图/Lean增量，非当前三图Ctarget。'
bar['lesson_and_restart_condition']+=' 对照已具体区分joint和sequential：230的5helper分行pins经K5互补覆盖成功，而第一单点prefix漏120；不能把成功jointbatch硬改成每prefixD3。对真实product2×8/cap31，均匀轻分配每row<8全局不可能，下一具体规则必须容许至少一heavyrow并同时兑现B-factor覆盖和双端peer成本；尚未派集中8子集枚举/图/solver。小27..34推广仍STOP，大86/90/94/98仅候选未派，当前三图freeze完成后再选。'
te=[Z+x for x in ['PREDICTION_AND_SCOPE.md','RESULT.json','TERMINAL.json','PROOF.md','PARAMETERS.json','run_once.py','FINAL_ROOT_HISTOGRAMS.tsv','PREFIX_ROOT_DISTANCES.tsv']]+[T+'CAP31_ROW_CONCENTRATION_PREDICTION.md',T+'CAP31_ROW_CONCENTRATION_INDEPENDENT_NOTE.md']
bar['evidence_paths']=list(dict.fromkeys(bar['evidence_paths']+te));e=[C+'GEMINI_RAW.json',C+'DISPOSITION.md']+te;assert all((R/x).is_file()for x in e)
rawrows=W/f'updates/{B}_ROWS.json';rawrows.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',rawrows).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
block=f'''<!-- {B} -->
# 当前：三原目标finalC618实际PASS；一次freeze已授权尚未执行；230校准与cap31纸面另记

同Goal ACTIVE，ledger420复用3现节点/0新行，146／37／Lean40、stage42／34、outside40／33、known43/main103_3/global0不变。finalC618真实MCPthread53b69de0-5f49-43ba-b3ee-1b37db7c804a异A e4/B67beb，三原tuple7532/346516/350742逐math/formal/bindingPASS、priorityUNKNOWN；一个sharedfreshC非三calls/旧C继承。当前三完整图/kernel/Audit/A/B/C全部实际闭合。root已授权一次新专家freeze但未执行，不声称ZIP存在；本增量后停止Wiki写入，等实际freeze回执。

[现barrier节点](experiments/{ids[2]}.md)另存230controlled calibration全部预测实测PASS：.027416CPU，最终230/1035/9regular/exactD3、全230rootshist全match；单helper226prefix只达106/漏120，说明K5联合helper成功不等于逐单点D3prefix。0portfolio/参数/Lean增量，非Cscope。cap31paper支持仅“至少某helper某row≥8distinctclasses”，非排31/非每helperheavy；GQ3walk唯一性和all-light325≤324矛盾，0枚举/图/solver。小27..34复制STOP，86/90/94/98仅候选未派。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 唯一distinctfresh最终C实际三目标PASS；freeze已授权未执行，另存230与cap31认识

复用[7532](experiments/{ids[0]}.md)、[q8](experiments/{ids[1]}.md)、[现barrier](experiments/{ids[2]}.md)，ledger420/0新方法行，146图／37参数／Lean40、stage42／34、outside40／33、known43/main103_3/global0不变。C618完整raw及rootdisposition/逐图JSON实际读取：真实MCPthread53b69de0-5f49-43ba-b3ee-1b37db7c804a异A e4b6c102与实际B67beb729，三精确tuple各math/formal/bindingPASS+priorityUNKNOWN。C是一次sharedfreshcall，不继承旧C，不作全球优先权认证。root处置澄清diagclone到另一F的H路径首步必在U只对length≤3成立，正好是paper/kernel使用范围，无数学修复或extra paidcall。

三原目标本地数学、完整图、fresh独验、无用户前提具体Lean/Audit/绑定和新A/B/freshC现全部完成。root一次专家freeze授权已给、尚未执行，0新ZIP存在声明；本次Wiki后停止写入，待唯一freeze实际收据再收束。旧冻结包与根状态未改，Goal仍ACTIVE，公开priority及人工反馈未被数学PASS代替。

另一个真实小校准说明路线互补而非模板横扫：literal15relation每row3、A³=4A+J全225项验证，不假设已知GQ同构；其225source25个8N分割200noncenters。5helpers按Arow各接5绝对乘积并成K5，最终完整230/1035/9regular/exactD3，全230root普通BFS逐事前三类hist125×(1,9,48,172)、100×(1,9,46,174)、5×(1,9,60,160)全部PASS。首次只加helper0的226prefix root225得(1,5,40,60)，仅达106、R3漏120（不是断连声明），所以这是jointbatch成功，不能借futurehelper让每个单点prefix都满足D3。actualrusage.027416CPU/5，1prefix+230finalBFS，0source/旧图/field/Lean/solver/extraaudit。0portfolio图/参数/Lean，未被当前三图C审过，不外推真实2×8或31。

cap31新paper检查还具体改变下一代ownership：真实B里两个不同absolute的3walk由GQ点到非关联polarline唯一投影唯一，故一个异class pin在某class的8个老目标内最多盖1。若某helper每Arow均<8distinctbasedclasses，则325≤(r+1)p_h+Σ邻helper p_g；若全helper都如此，undirected双计数给325≤(r+14)²，r4/cap31成325≤324矛盾。因此只推出至少一个helper有某Arow≥8类，不能说每helperheavy、31排除或存在heavy方案；重复copies只算同class1次，所有双端peer成本仍需兑现。0新scalar/8-subset枚举/8775source/solver/Lean/外审。小q4推广27..34保持STOP；86/90/94/98仅未派候选，当前三图交付后再选择。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'ActualfinalC618SUCCESS/MCP53b69de0distinctactualA_e4andB67beb/threeexacttuplemath_formal_bindingPASS_priorityUNKNOWN/onefreshsharedcall/0reruns. ThreeoriginalsallmathkernelAuditsABCcomplete/rootONEfreezeauthorizedNOTexecuted/noZIProbabilityclaim/wikiwriteholdafterreceipt. Separate230calibrationallpredictionsPASS/.027416CPU/final230_1035_9D3all230roots/prefix226miss120/jointnotsequential/0portfolioLean/notCscope. Cap31papernecessaryEXISTSsomehelpersomerowGE8distinctclasses/notallheavy/not31exclusion/0runs. Small27_34STOP/86_90_94_98candidates0dispatch. ledger420threeexistingrows146_37Lean40stage42_34unchanged/0rootedits_frozenwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_ACTUAL_FINAL_C_THREE_ORIGINALS_SEPARATE230_CALIBRATION_CAP31_PAPER_WIKI_SYNC_WRITE_HOLD',updated_UTC=now,ledger_records=420,records_added=0,records_updated=3,named_legal_graphs=146,legal_parameter_pairs=37,stage_graphs=42,stage_pairs=34,complete_formula_Lean=40,outside40_33=True,known43_main103_3_global0=True,
    actual_final_C_status='SUCCESS',actual_C_MCP_thread=c['threadId'],C_distinct_actual_A_B=True,C_shared_calls=1,three_precise_tuple_math_formal_binding_PASS=True,priority='UNKNOWN',new_graphs=0,new_Lean=0,new_frameworks=0,
    one_freeze_explicitly_authorized=True,freeze_executed_by_this_agent=False,new_ZIP_exists_claimed=False,
    calibration230=dict(status=z['status'],n=230,m=1035,Delta=9,D=3,actual_final_BFS_roots=230,prefix226_missed_R3=120,CPU_rusage=z['CPU_seconds_rusage'],portfolio_increment=0,Lean_increment=0,in_three_target_C_scope=False),
    cap31_paper='EXISTS_SOME_HELPER_SOME_ROW_GE8_DISTINCT_CLASSES_NOT_CAP31_EXCLUSION',cap31_new_runs=0,cap31_in_C_scope=False,
    future_candidates_dispatched=0,evidence_paths_checked=len(e),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False,Wiki_writes_held_after_this_receipt_until_freeze_result=True)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
