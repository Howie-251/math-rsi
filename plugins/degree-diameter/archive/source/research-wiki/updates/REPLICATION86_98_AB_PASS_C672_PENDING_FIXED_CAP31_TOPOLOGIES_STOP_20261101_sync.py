from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';V=S+'reviews/';T=S+'retained_edge_transfer/polarity_product2_8_helper_barrier/';E='expert_review_current/REPLICATION86_98_TWO_RESULTS_20261101'
B='REPLICATION86_98_AB_PASS_C672_PENDING_FIXED_CAP31_TOPOLOGIES_STOP_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
ids=['ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101','ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
expected={(86,3,363420,15573870),(98,3,414132,19680570)};reviews={}
for kind,thread,cell in [('A','e4b6c102-1c55-4739-82e4-d281acc2e835',655),('B','5da20cd4-ab3f-4327-9df5-8d0e80d7eee3',663)]:
    stem=V+f'REPLICATION86_98_{kind}_';x=json.loads((R/(stem+'GEMINI_RAW.json')).read_text())['structuredContent'];assert x['status']=='SUCCESS' and x['threadId']==thread
    ts=next(json.loads(z)['targets']for z in re.findall(r'```json\s*([\s\S]*?)```',x['content'])if 'targets'in json.loads(z));assert {(z['Delta'],z['D'],z['n'],z['m'])for z in ts}==expected
    assert all(all(z[k]=='PASS'for k in ['math','formal','binding'])and z['priority']=='UNKNOWN'for z in ts)
    reviews[kind]=dict(status='ACTUAL_SUCCESS_TWO_EXPLICIT_ORIGINAL_MATH_FORMAL_BINDING_PASS',cell=cell,thread=thread,actual_shared_calls=1,targets=ts,priority='UNKNOWN',raw=stem+'GEMINI_RAW.json',disposition=stem+'DISPOSITION.md',old_case_PASS_inherited=False)
c=json.loads((R/(V+'REPLICATION86_98_FINAL_C_REQUEST.json')).read_text());assert c['status']=='ACTUALLY_DISPATCHED_DISTINCT_FRESH_FINAL_C_PENDING' and c['cell_id']=='672'
draft=json.loads((R/(E+'_DRAFT_RECEIPT.json')).read_text());assert draft['status']=='UNFROZEN_TWO_TARGET_EXPERT_DRAFT_C_PENDING' and not draft['delivery_ZIP_created']
k=json.loads((R/T/'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_RESULT.json').read_text());kt=json.loads((R/T/'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_TERMINAL.json').read_text());n=json.loads((R/T/'NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_RESULT.json').read_text());nt=json.loads((R/T/'NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_TERMINAL.json').read_text())
assert k['status']=='SUPPORTED_CLIQUE_HELPER_CAP31_IMPOSSIBILITY_IN_FIXED_MODEL' and k['maximum_free_target_capacity']==1620 and k['free_targets']==1625
assert n['status']=='SUPPORTED_FIXED_LITERAL_CAP31_BALANCED_KTT_EXCLUSION_WITH_PLAIN_PROOF' and n['min_degree_allowed']==list(range(9,17))
q8=rows[0];m=q8['other_metrics'];batch=m['replication86_98_actual_batch'];batch.update(A=reviews['A'],B=reviews['B'],distinctfreshC=dict(status='ACTUAL_ONE_FRESH_CALL_C672_LIVE_PENDING_NO_VERDICT',cell=672,store='endpoint86_98_C_actual',actual_shared_calls=1,thread=None,request=V+'REPLICATION86_98_FINAL_C_REQUEST.json',must_differ_from_actual_A_B=[reviews['A']['thread'],reviews['B']['thread']],paid_retry=False,old_case_C_inherited=False))
for g in m['validated_graph_instances']:
    if g['n']in [363420,414132]:g.update(external_A='ACTUAL_SUCCESS_NEW_SCOPE_MATH_FORMAL_BINDING_PASS',external_A_thread=reviews['A']['thread'],external_B='ACTUAL_SUCCESS_NEW_SCOPE_MATH_FORMAL_BINDING_PASS',external_B_thread=reviews['B']['thread'],external_fresh_C='CELL672_ACTUAL_LIVE_PENDING_NO_VERDICT',external_B_C_complete=False,priority='UNKNOWN')
m['all_row_original_A_B_distinctfreshC_complete']=False
m['completed_Lean_and_A_B_C_scope']='all7q8rowinstanceskernelcomplete;old5reviewscomplete;new86_98A_BactualPASS_C672livepending'
m['replication86_98_two_expert_DRAFT']=dict(status=draft['status'],snapshot=draft['snapshot'],prior_frozen_snapshot=draft['prior_frozen_snapshot'],HTML=E+'.html',source=E+'.html.txt',Word=E+'.docx',
    HTML_and_source_bytes=22215,Word_bytes=8334,selected_local_paths=79,missing_local_paths=0,actual_prepare_CPU=draft['CPU_seconds'],HTML_source_byte_identical=True,Word_XML_parsed=True,
    new_ZIP=False,freeze_performed=False,not_part_of_old146_snapshot=True,receipt=E+'_DRAFT_RECEIPT.json',extra_render_or_link_recheck_this_sync=False)
m['replication86_98_AB_disposition_clarifications']=dict(A_pin_union='342225oldHpins=342160rawUplus65fillers;notonlyrawU',B_axioms='standard3axioms_notaxiomfree',B_fresh_CPU='canonical9.484730169includescompilewrapper;internal7.89628notfulltotal',extra_paid_call=False)
q8['title']='86/363420与98/414132数学/kernel/A/B实际PASS；唯一freshC672在途，轻量专家DRAFT无ZIP'
q8['outcome_class']='NEW86_98_KERNEL_A_B_ACTUAL_PASS_FRESH_C_LIVE_PENDING_DRAFT_ONLY'
q8['scope']+=' 两新tuple A655与独立B663已实际逐math/formal/bindingPASS，A e4/B5da不同；唯一distinctfreshC672 live待返、不retry/不继承旧C。轻量DRAFT148/39/42与旧146snapshot冻包分离，0新ZIP。'
q8['distance_text']+=' A655同e4新scope与B663真实5da20cd4-ab3f-4327-9df5-8d0e80d7eee3各一次sharedcall，两精确tuple三facet全PASS/priorityUNKNOWN；C672/storeendpoint86_98_C_actual实际live待返回，不能先PASS。专家HTML/txt各22215B、Word8334B、79selectedpaths存在、.013449846CPU，0ZIP，不重做prepare/验证。'
q8['lesson_and_restart_condition']+=' 两图只剩唯一freshC实际判定及后续明确交付动作，不重试call或继承旧scope；新轻量DRAFT不修改旧146/37/40冻结包。小参数研究已按真实路线证明停止两个固定helper拓扑，未派另一模板solver，保留unbalanced/一般nonclique开放，重启需要具体joint pin/freepeer规则。'
bar=rows[1];m=bar['other_metrics'];m['clique_helper_free_target_prediction']=dict(status=k['status'],r=4,cap=31,classes=325,free_targets=1625,all_nonempty_clique_sizes_excluded=True,
    maximizing_Kt=14,maximum_class_capacity=324,maximum_free_target_capacity=1620,shortfall=5,arbitrary_F_F_allowed=True,mandatory_edges_preserved=True,
    fixed_source='publishedproduct2x8interface',source_generated=False,CPU=kt['CPU_seconds_rusage'],CPU_budget=2,tiny_scalar_runs=1,old_r0_3_exclusions_not_new=True,
    nonclique_excluded=False,portfolio_or_Lean_increment=0,in_two_target_C_scope=False,NOTE=T+'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_NOTE.md',RESULT=T+'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_RESULT.json',TERMINAL=T+'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_TERMINAL.json')
m['nonclique_repair_profile_fixed_balanced_Ktt']=dict(status=n['status'],scope='fixedliteral15xgenuine585/r4/fullmandatory/cap31/arbitraryF_F',inherited_literal15_g_profile=[5,4,1,0,0,0],
    minimum_helper_degree_necessary_range=[9,16],every_helper_degree_at_most16_claimed=False,
    balanced_Ktt_all_t_excluded=True,F_gate_surviving_t=list(range(8,20)),whole_N_old_targets_per_class=26,
    proof_steps='whole26Nsaveclassrequiresrow>=8distinctpinsandcolumn>=2;twoheavyrowcharge;two-partpinunionintersectiondeductedatleasttwiceperclass',
    closest_t=13,closest_left=3900,closest_right_upper=3809,closest_shortfall=91,
    actual_CPU_total=nt['total_CPU_seconds'],CPU_budget=2,scalar_runs=1,source_or_table_or_BFS_solver_Lean_runs=0,
    old585_Steiner_32subsets_or_toy_retests=0,portfolio_or_Lean_increment=0,in_new_two_target_C_scope=False,
    still_open=['unbalancedbipartitehelpers','arbitrarynoncliquehelpers','changedsource','changedmandatoryedges'],
    NOTE=T+'NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_NOTE.md',RESULT=T+'NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_RESULT.json',TERMINAL=T+'NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_TERMINAL.json')
m['inherited585_Steiner_row_residual_product_application']=dict(status='OLD20261027_DATA_NEW_PRODUCT_ROUTE_APPLICATION_NOT_FIRST72_9_1_DISCOVERY',
    inherited_design='Steiner3-(65,9,1)',old_point_pair_triple=[72,9,1],U='72t-9C(t,2)+C(t,3)',
    own_counts=[8,9,10,11,12],missed_target_lower=[140,112,85,58,30],external_class_lower=[18,14,11,8,4],
    actual_saved585_only=True,old_max9_all_preserved_extensions_remains_closed=True,old_source_or_Steiner_retests=0,cap31_excluded_by_this_alone=False,NOTE=T+'CAP31_INHERITED_STEINER_ROW_RESIDUAL.md')
m['two_fixed_cap31_helper_topologies_stop']=dict(clique='STRICT_STOP',balanced_Ktt='STRICT_STOP',arbitrary_nonclique_excluded=False,unbalanced_excluded=False,
    no_new_template_solver_dispatched=True,restart_requires='actualjointpin_freepeer_connectionrule_notcapacitynumbers')
bar['title']='固定cap31产品helper：clique与balanced K(t,t)全停；其他nonclique开放，旧585证据继承'
bar['outcome_class']='SCOPED_FIXED_CAP31_CLIQUE_AND_BALANCED_KTT_PAPER_EXCLUSIONS_SUPPORTED_NO_GRAPH_LEAN'
bar['scope']+=' 最新cap31全clique排除与fixedliteral15×genuine585的balancedK(t,t)全t排除分别独立纸面SUPPORTED，均保完整mandatory且允许任意F-F；一般nonclique/unbalanced未排。minimum helperdegree需9..16不表示每个degree≤16。'
bar['distance_text']+=' clique新目标F1625，最优Kt14上界1620差5，.000053CPU/2一次tiny。balancedKtt的F界余t8..19，whole26N/rowcol条件及左右part交集至少双收费全排，最近t13为3900>3809差91；minimum helperdegree必要9..16，非所有helperdegree≤16。唯一.011899883CPU/2，0source/table/BFS/solver/Lean/old585或q2子集重跑。旧72/9/1 credit20261027不变，actual585行8..12的外援类18/14/11/8/4来自继承强界应用，不新发现。'
bar['lesson_and_restart_condition']+=' root据两个真实proof STOP全clique与balancedKt,t，不继续模板化solver。任意nonclique及unbalanced依旧开放；只有具体jointpin/freepeer规则才重启，不能因容量数还有余就发一轮拓扑筛选。这些paper结果/小scalar不在86/98两目标Cscope，无新图/Lean计数。'
e=[V+f'REPLICATION86_98_{x}_{y}'for x in ['A','B']for y in ['GEMINI_RAW.json','DISPOSITION.md']]+[V+'REPLICATION86_98_FINAL_C_REQUEST.json',E+'.html',E+'.html.txt',E+'.docx',E+'_DRAFT_RECEIPT.json']
te=[T+x for x in ['CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_NOTE.md','CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_RESULT.json','CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_TERMINAL.json','CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_SCALAR.py','NONCLIQUE_REPAIR_PROFILE_PREDICTION.md','NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_NOTE.md','NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_RESULT.json','NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_TERMINAL.json','NONCLIQUE_REPAIR_PROFILE_INDEPENDENT_scalar.py','CAP31_INHERITED_STEINER_ROW_RESIDUAL.md']]
assert all((R/x).is_file()for x in e+te);q8['evidence_paths']=list(dict.fromkeys(q8['evidence_paths']+e));bar['evidence_paths']=list(dict.fromkeys(bar['evidence_paths']+te))
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
block=f'''<!-- {B} -->
# 当前：86/98新A/B两tuple三facet实际PASS，唯一C672 live待返；两个固定cap31 helper拓扑STOP

同Goal ACTIVE，ledger420复用[q8](experiments/{ids[0]}.md)+[barrier](experiments/{ids[1]}.md)两现节点/0新行；148／39／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。A655真实e4及B663真实5da20cd4-ab3f-4327-9df5-8d0e80d7eee3分别一次明确新scope，两精确tuple各math/formal/bindingPASS/priorityUNKNOWN。唯一distinctfreshC672/storeendpoint86_98_C_actual已实际live，thread/verdict待返，不retry/不继承旧C/不提前PASS。轻量专家DRAFT HTML/txt22215B、Word8334B、79paths存在、.013449846CPU，0ZIP，旧146snapshot包不动。

clique cap31独立SUPPORTED：F1625最优Kt14最多1620，含任意F-F、.000053CPU。fixedliteral15×genuine585/r4/fullmandatory模型的balancedKt,t亦全t纸面关闭，F界余8..19经whole26N/rowcol和两part交集扣重全排；最近t13差91，唯一.011899883CPU。minimum helperdegree需9..16，非各degree≤16；unbalanced/任意nonclique未排。旧58572/9/1继承，row8..12需外援18/14/11/8/4是旧证据product应用。两固定拓扑STOP，不发另一模板solver，重启需actualjointpin/freepeer规则；所有小分析非新两图Cscope，0新图/Lean。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 两新端点A/B实际PASS、唯一C672在途；clique与balancedKtt停止，其他nonclique仍开放

仅复用[q8机制](experiments/{ids[0]}.md)、[现barrier](experiments/{ids[1]}.md)，ledger420/0新行，148图／39参数／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。已实读两newscope A655/B663 raw逐tupleJSON及rootdisposition：A e4b6c102、B5da20cd4-ab3f-4327-9df5-8d0e80d7eee3不同，各一次sharedcall明确86/363420与98/414132，math/formal/binding全PASS+priorityUNKNOWN。A旧pinunion措辞改为oldH内342160rawU+65fillers，B“noaxioms”仅指无额外未证axioms仍std3，7.89628是内部validator非canonicalfresh9.484730169CPU。0额外parse/数学/编译/paidcall。唯一freshC672/storeendpoint86_98_C_actual实际live，REQUEST已存cell，thread/verdict待返不重试、不继承旧C。轻量新DRAFT实有HTML/txt各22215B、Word8334B、79selectedpaths存在/.013449846CPU，0ZIP，不属旧146/37/40归档，未重复渲染/核links。

新clique-free-target预测已独立SUPPORTED：固定productsource/r4/fullmandatory且任意F-F，所有K_t在cap31只达≤1620free targets<1625，最优t14差5。唯一tiny scalar.000053CPU/2，0S8775/field/BFS/solver/Lean；旧r0..3排除不当新认识。新NONCLIQUE_REPAIR_PROFILE亦独立SUPPORTED，范围限定fixedliteral15×genuine585。继承q2g(0..5)=(5,4,1,0,0,0)给对minimum-helperdegree顶点325≤(d+6)(31−d)，minimum degree必须9..16，并非每helperdegree≤16。balancedK(t,t) F目标上界先留t8..19；完整26N若ownsuffix已全盖必须row≥8distinct且column≥2，p≤23下heavyrow收费，再对两part pinunion交集每class至少双扣，十二t全违全局必要式，最近t13是3900>3809差91。actualpins无需均匀/classdistinct，多owner与Fpeer双端成本均计。唯一.011899883CPU/2，无source/table/BFS/solver/旧32subset/toy/585/Steiner重跑。

旧585设计72/9/1仍credit20261027，CAP31_INHERITED_STEINER_ROW_RESIDUAL给actualsaved585的row8..12外援类下界18/14/11/8/4；这是旧Bonferroni证据的新product路线应用，旧max9保边排除继续closed，不复现。不把这些局部结果扩成cap31一般上界；unbalanced bipartite、其他任意nonclique、改源/mandatory仍开放。root停止这两个固定拓扑，不发另一模板solver；再启必须actualjointpin/freepeer连接规则，不只容量数字。所有小分析不属于新两图Cscope，无图/参数/Lean增量，根状态/冻结包未改。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Actualnew86_98A655e4andB6635da20cd4twoprecisetuplemathformalbindingPASSpriorityUNKNOWN/onecallseach;uniqueC672actualLIVEpending/noRetry/noOldCinherit. LightweightDRAFThtmltxt22215Word833479paths.013449846CPU0ZIPnotold146snapshot. Localfixedcap31cliqueKtallSTOP1620<1625bestt14/.000053CPU;balancedKttallSTOP/Fsurvivors8_19/whole26Nrowcol_twopartintersectionproof/closestt13gap91/.011899883CPU. MINhelperdegree9_16NOTallDeg<=16/unbalanced_generalnoncliqueOPEN. Old58572_9_1inherited/residual18_14_11_8_4notnewdiscovery/0oldretest. NoanotherTemplateSolver_actualjointRuleRequired. ledger420twoexistingrows148_39Lean42stage44_36unchanged/0newmathruns_rootedits_frozenwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_NEW86_98_ACTUAL_A_B_C672_PENDING_AND_TWO_FIXED_CAP31_TOPOLOGIES_STOP_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=148,legal_parameter_pairs=39,stage_graphs=44,stage_pairs=36,complete_formula_Lean=42,outside42_35=True,known43_main103_3_global0=True,new_graphs=0,new_Lean=0,new_frameworks=0,
    A_actual_thread=reviews['A']['thread'],B_actual_thread=reviews['B']['thread'],both_new_precise_tuples_math_formal_binding_PASS=True,C672='ACTUAL_LIVE_PENDING_NOT_PASS',C_thread=None,new_DRAFT=True,new_ZIP=0,
    clique_cap31='STRICT_FIXED_MODEL_STOP',clique_best1620_of1625=True,clique_CPU=kt['CPU_seconds_rusage'],balanced_Ktt='STRICT_FIXED_LITERAL_MODEL_ALL_T_STOP',minimum_helper_degree_range=[9,16],all_helper_degree_le16_claimed=False,balanced_closest_gap=91,balanced_CPU=nt['total_CPU_seconds'],unbalanced_or_arbitrary_nonclique_excluded=False,
    old58572_9_1_inherited=True,all_small_analyses_in_two_target_C_scope=False,evidence_paths_checked=len(e)+len(te),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
