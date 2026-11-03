from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
B='DEGREE83_ACCEPTED_K1_TWO_TARGETS_ACTUAL_A_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
D=S+'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity2_degree83/'
A=S+'reviews/DIAGONAL_REALLOCATION_TWO_TARGETS_A_';F=S+'retained_edge_transfer/diagonal_fill_reallocation_formalization/'
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,145,36,37)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101']
rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
z=json.loads((R/D/'independent_acceptance/RESULT.json').read_text());t=json.loads((R/D/'independent_acceptance/TERMINAL.json').read_text());a=json.loads((R/(A+'GEMINI_RAW.json')).read_text())['structuredContent'];c=json.loads((R/F/'CHECKPOINT.json').read_text())
assert z['status']==t['status']=='PASS' and (z['actual_n'],z['actual_m'],z['max_degree'],z['exact_diameter'])==(350742,14547195,83,3)
assert z['all8450_both_block_original_U_N_bindings'] and z['hist_mismatches']==0 and t['new_BFS_roots']==68
assert a['status']=='SUCCESS' and a['threadId']=='e4b6c102-1c55-4739-82e4-d281acc2e835'
actualA=dict(status='ACTUAL_SUCCESS_BOTH_K1_ORIGINAL_MATH_LITERAL_BINDING_PASS',thread=a['threadId'],actual_call='rootcell559',shared_call_count=1,
    targets=[[26,3,7532,97750],[82,3,346516,14204970]],formal='NOT_REVIEWED_PENDING',public_priority='UNKNOWN',final_C=False,
    corrections={'raw_oldU_pair_0_21':'producer evidence, not independent; fresh7532 independent witness7242-3145-1-0','old_Lean_reuse':'old certificate does not certify new targets; finitegeometry/generic reuse is legitimate'},
    degree83_inherited=False,k1_role_fullN_identity_added_after_dispatch_not_Acertified=True,raw=A+'GEMINI_RAW.json',disposition=A+'DISPOSITION.md')
for r in rows:
    m=r['other_metrics'];p=m['diagonal_fill_reallocation_prediction'];p['new_review_status'].update(external_A=actualA['status'],external_A_thread=a['threadId'],formal_A='NOT_REVIEWED_PENDING',external_B='NOT_DONE',external_fresh_C='NOT_DONE')
    m['diagonal_reallocation_two_targets_pending_proof_and_review'].update(external_A=actualA['status'],external_A_thread=a['threadId'],formal_A='NOT_REVIEWED_PENDING')
    m['diagonal_reallocation_two_k1_actual_A']=copy.deepcopy(actualA)
    m['diagonal_reallocation_generic_Lean_checkpoint']=dict(completed_modules=c['completed'],checkpoint_CPU=c['CPU_seconds'],checkpoint_status=c['status'],concrete_original_targets_closed=0,scope='genericmodulecheckpointsnotconcreteLeancompletion',receipt=F+'CHECKPOINT.json')
    for g in m['validated_graph_instances']:
        if g['n'] in [7532,346516]:g.update(external_A='ACTUAL_SUCCESS_MATH_LITERAL_BINDING_PASS_FORMAL_PENDING',external_A_thread=a['threadId'],external_A_formal='NOT_REVIEWED_PENDING',external_B='NOT_DONE',external_fresh_C='NOT_DONE')
    r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+[A+'GEMINI_RAW.json',A+'DISPOSITION.md',F+'CHECKPOINT.json',F+'HANDLE.json',F+'PRED.md']))
    r['lesson_and_restart_condition']+=' k1两原目标A559现实际SUCCESS，新thread e4b6c102…一个sharedcall分别math/literalbindingPASS、formal未审/PENDING、priorityUNKNOWN；raw误把producer[0,21]归独验已处置，实际fresh7532见证7242→0。此A不覆盖83或dispatch之后新增的k1-role简化。generic5module checkpoint PASS仍非两具体目标闭合，Lean37不变；83待parentclosed后另150CPU/每module60/单worker基于G1角色复制，不重编旧source。'
r=rows[1];m=r['other_metrics'];p=m['degree83_multiplicity2_single_target']
p.update(status='ROOT_MATHEMATICALLY_ACCEPTED_FRESH_INDEPENDENT_PASS',D=3,actual_exact_D=3,accepted_instances=1,mathematically_validated_complete_graph=True,
    independent_status='TERMINAL_PASS',independent_CPU_seconds=t['total_CPU_seconds'],full_both_block_NU_bindings=8450,actual_BFS_roots=68,actual_diagonal_BFS=65,actual_off_BFS=2,actual_hub_BFS=1,
    unmeasured_new_off_roots=4158,actual_old_BFS=0,measured_hist_mismatches=0,actual_same_center_distance2_checks=67,all4225_same_center_pairs_distance2_from_binding=True,
    actual_two_hub_distance=2,structural_hub_clone_nonD2=True,actual_hub_clone_walk=[350741,342225,5265,342290],
    independent_hist_distributions=z['hist_distributions'],all_pairs_and_two_prefix_proof=True,
    new_concrete_Lean='AUTHORIZED_AFTER_PARENT_CLOSED_NOT_COMPLETE',Lean_CPU_budget=150,Lean_per_module_CPU=60,Lean_workers=1,
    external_A='NOT_DONE_EXPLICIT_NEW_SCOPE_ONLY_AFTER_KERNEL',external_B='NOT_DONE',external_fresh_C='NOT_DONE',A559_inherited=False)
m['validated_graph_instances'].append(dict(Delta=83,D=3,n=350742,m=14547195,actual_diameter=3,mathematically_validated_complete_graph=True,complete_Lean_graph_instance=False,
    known_nonrecord=False,known_publicly_dominated=False,latest_global_record_confirmed=False,confirmed_publictable_improvement=False,best_located_public_lower_bound=350675,bounded_gain=67,
    public_comparison_status='EXCEEDS_SCOPED_BEST_LOCATED_GUARANTEE_BY67_GLOBAL_PRIORITY_UNKNOWN',graph_path=D+'graph_d83_D3_n350742.edges',degree_histogram=z['degree_histogram'],
    source_n=346516,source_all14204970_edges_retained=True,full_literal_NU_bindings=8450,actual_newroot_BFS=68,actual_oldroot_BFS=0,unmeasured_new_off_BFS=4158,
    allpairs_U_H_endpoint_proof=True,both_prefixes_proved=True,all4225_twin_distance2_from_binding=True,actual_twin_distance2_checks=67,actual_two_hub_distance=2,
    complete_concrete_Lean_status='PENDING_SEPARATE150CPU_AFTER_PARENT',external_A='NOT_DONE_NOT_A559_SCOPE',external_B='NOT_DONE',external_fresh_C='NOT_DONE',
    producer_CPU=3.493080617,independent_CPU=t['total_CPU_seconds'],independent_acceptance=D+'independent_acceptance/RESULT.json'))
m['new_named_complete_graphs']=5;m['accepted_q8_terminal_graphs']=[327744,342290,346515,346516,350742]
m['degree83_new_parameter_pair_accepted']=[83,3]
r['title']='q8三旧图全闭合/冻结；新346516与degree83/350742数学接受，具体Lean及后续外审待'
r['scope']+=' 唯一83/350742/14547195实例fresh独验并root接受，新增参数83；只这一k2图，不把所有k记为已生成。两k1A实际math/bindingPASS但formalPENDING，83A尚未明确新scope，三新图具体Lean/B/freshC均未完成。'
r['distance_text']+=' 唯一k2/83实际350742/14547195/max83/exactD3，parent346516全部14204970边保留，两个4225cloneblocks共8450NU绑定，degree65:2/80:130/81:8385/83:342225。68预选新根逐项match65diag(1,80,5251,345410)、2off(1,81,5330,345330)、hub(1,65,5266,345410)，其余4158newoff及old0BFS；完整U/Hendpoint及双prefix证明补齐全对。67samecenter实测距2/all4225由全绑定证明，双hub实测距2，hubclone结构无edge/commonneighbor且实际3walk350741—342225—5265—342290。producer3.493080617CPU/独验5.825614568CPU，83具体Lean和A/B/C未完成不继承k1A。'
e=[D+'independent_acceptance/'+x for x in ['NOTE.md','RESULT.json','TERMINAL.json','ALL_8450_BOTH_BLOCK_TRUE_U_N_BINDINGS.tsv','ALL_68_PRESELECTED_NEW_ROOT_BFS.csv','HUB_CLONE_STRUCTURE_WITNESS.json','NON_D2_ACTUAL_NEW_ROOT_WITNESS.json']]+[A+'GEMINI_RAW.json',A+'DISPOSITION.md',F+'CHECKPOINT.json',F+'HANDLE.json',F+'PRED.md']
assert all((R/x).is_file()for x in e);r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+e))
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,37)
block=f'''<!-- {B} -->
# 当前：唯一83度350742图已fresh接受，146／37／Lean37；两k1实际A math/bindingPASS

同Goal ACTIVE，ledger420复用2现节点/0新行；146合法／37参数、stage42／34、Lean37，outside40／33，known43/main103_3/global0；旧冻结三q8包不动。[q8节点](experiments/{ids[1]}.md)只新增实际83/350742/14547195实例，不冒所有k完成。

83保parent346516全部14204970边、8450两block NU绑定、68预选新根三类hist全match；67samecenter实测距2且全4225由binding证明，双hub距2、hubclone结构无1/2路+真实3路。4158newoff与old0BFS，用NOTE全端点/双prefix补足；producer3.493080617/独验5.825614568CPU。

两k1（[7532](experiments/{ids[0]}.md)/346516）唯一A559实际SUCCESS，新thread e4b6c102…分别math/literalbindingPASS，formalNOT_REVIEWED/PENDING，priorityUNKNOWN。原raw[0,21]归属已纠正，不重call；83A尚未做，待83kernel再同thread明确新scope一次，B3/freshC未派。generic5module PASS≠具体目标完成；原600CPU两k1与另150CPU/每module60/单worker83依赖parent闭合，Lean不提前计40。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 重复center与双hub预测实际通过：唯一83新参数接受；两k1数学A通过、formal待

现Wiki仅复用[7531/7532节点](experiments/{ids[0]}.md)、[q8节点](experiments/{ids[1]}.md)，ledger420/0新method行。root实际接受83/350742/14547195/max83/exactD3，146合法／37参数、stage42／34／Lean37，outside40／33、known43/main103_3/global0。接受的是唯一k2实体，不把uniformk纸面命题展开成不存在的图实例。

parent346516全部14204970边逐条保留、原H全保；8450行两cloneblocks NU完全绑定，真实degree65:2/80:130/81:8385/83:342225。68预选新根三类hist逐项支持：65diag(1,80,5251,345410)、2off(1,81,5330,345330)、hub(1,65,5266,345410)，mismatch0。67个clone根到firstcopy实测距2、全4225samecenter对由共同非空pin及无cloneedge证明；双hub距2；hubclone的F/U邻域分离排1/2路，实际hubwalk350741—342225—5265—342290为3。4158newoff/old0BFS，其余点对由NOTE完整U/Hendpoint与从H、从G1两种prefix证明覆盖；0抽样外推。producer3.493080617CPU、indep5.825614568CPU。该证据支持复制first-role G1规则，下一kernel可直接接已核FullNeighborhoodClones，非重开旧GQ有限检验。

两k1原目标唯一A559实际SUCCESS，thread e4b6c102-1c55-4739-82e4-d281acc2e835，一个sharedcall逐7532/346516的math及literalbindingPASS，formal未审/PENDING、priorityUNKNOWN；raw把producer[0,21]误称独验已root处置，fresh7532实际见证7242—3145—1—0。83不继承此A，待83实际kernel闭合后同thread仅一次明确新scope。B3及distinctfreshC尚未派，不调用补审。旧三q8冻结scope及ZIP均未改。

新generic CHECKPOINT实际Definitions/Walks/Geometry/Degree/Lower五module PASS，历史失败attempt保留；仅generic模块、两k1原目标/Audit仍未最终闭合，Lean37不变。原两k1总600CPU/单module60/单worker继续，另83150CPU/单module60/单worker授权依赖G1闭合后运行，不能提前记Lean40。当前无84+或allk实体授权，0旧field/projection/图BFS/Lean重跑来自本次同步。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Actualunique83/350742/14547195cap83exactD3accepted;parent346516all14204970edgesretained/8450NUbindings/68preselectedBFSallmatch/67twinsactualdistance2+all4225binding/twohubsdistance2/hubclone3walk/4158offandold0BFS/fullendpointandtwoprefixproof;producer3.493080617CPU/indep5.825614568CPU. K1twoA559actualSUCCESSthreade4b6c102mathbindingPASS/formalPENDING/priorityUNKNOWN/rootdispositionfixproducer0_21attribution;83A_notdone/B3freshCnotdispatched. Generic5modulePASSnotconcretetarget;600k1plusseparate15083CPUafterparent/noLean40. Ledger420twoexistingrows146_37Lean37stage42_34/0reruns/rootedits/frozenpackchanges.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_UNIQUE_DEGREE83_MATH_ACCEPTED_K1_ACTUAL_A_FORMAL_PENDING_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=146,legal_parameter_pairs=37,stage_graphs=42,stage_pairs=34,complete_formula_Lean=37,outside_pending_graphs=40,outside_pending_pairs=33,known_dominated=43,main_graphs=103,main_pairs=3,global_records=0,new_graphs=1,new_parameter_pairs=1,new_Lean=0,new_frameworks=0,
    degree83=dict(status='ROOT_MATH_ACCEPTED_FRESH_PASS',n=350742,m=14547195,Delta=83,D=3,full_NU_bindings=8450,actual_BFS_roots=68,unmeasured_new_off_roots=4158,old_BFS=0,samecenter_actual_distance2=67,samecenter_allbinding_proof=4225,producer_CPU=3.493080617,independent_CPU=t['total_CPU_seconds']),
    k1_A='ACTUAL_SUCCESS_MATH_BINDING_PASS_FORMAL_PENDING',k1_A_thread=a['threadId'],degree83_A='NOT_DONE_NOT_INHERITED',B3_freshC='NOT_DISPATCHED',generic_completed_modules=c['completed'],concrete_Lean_new_closed=0,
    evidence_paths_checked=len(e),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
