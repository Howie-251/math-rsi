from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
B='Q8_REALLOCATION346516_ACCEPTED_GENERAL_PAPER_REVIEW_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
Q4=S+'retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation/'
Q8=S+'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/'
G=S+'retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md';I=S+'retained_edge_transfer/diagonal_fill_general_review/';P=S+'public_baseline_audit/DIAGONAL_FILL_REALLOCATION_TARGETED_QUERY_20261101.md'
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,144,36,37)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101']
rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
z=json.loads((R/Q8/'independent_acceptance/RESULT.json').read_text());t=json.loads((R/Q8/'independent_acceptance/TERMINAL.json').read_text());assert z['status']==t['status']=='PASS'
assert (z['actual_n'],z['actual_m'],z['max_degree'],z['exact_diameter'],z['changed_diag_roots_BFS'],z['hub_roots_BFS'],z['off4160_roots_BFS'],z['old_roots_BFS'])==(346516,14204970,82,3,65,1,0,0)
assert z['all4225_true_U_clone_neighborhoods_bound'] and z['hist_prediction_mismatches']==0
assert json.loads((R/I/'RESULT.json').read_text())['status']=='SUPPORTED_PAPER_PROOF_NO_GAP_FOUND'
general=dict(status='ROOT_ACCEPTED_PAPER_SUPPORTED_NOT_LEAN_OR_EXTERNAL_C',hypotheses='actualGQ(s,t),s,t>=2,actualspreadR=st+1,actualpartialovoidp;uniformintegerk>=1',
    n='delta*R^2+R+k*(pR+1)',m='delta*(delta*R^2+R)/2+k*(delta*pR+R-p)',maxdegree='delta+k',
    histogram={'delta+k':'delta*pR-p+R','delta':'delta*R^2-delta*pR+p+k*(pR-p)','delta-1':'k*p','R':'k'},
    old_U_only_projection_routes=True,same_center_multiple_clone_route='two steps through any old U neighbor',
    diagonal_own_and_other_fillers_covered=True,hub_collapse_hom_claimed=False,
    exact_D3='fixedoldUroot:|U|>delta^2+1 givesH-distance3 target; anynewclone2shortcutwouldgiveoldcentercommonneighbor;hubdoesnotmeetU',
    prefixes='modifiedclonesdirectlyfromH,thenhubs;allrouteinteriorsalreadyoldU/H',
    independent_review=I+'NOTE.md',root_note=G,small_scalar_experiments=0,new_graphs=0,new_Lean=0,new_frameworks=0,old_Q8_final_C_scope_extended=False)
new_review=dict(external_A='ONE_ACTUAL_DISPATCH_PENDING',handle='rootcell559/storediagonal_reallocation_A_review',
    scope='twooriginaltargets7532d26/346516d82mathandencoding;notfinalC/kernelPASS',external_B='NOT_DONE',external_fresh_C='NOT_DONE',
    concrete_Lean='IN_PROGRESS_NOT_COUNTED',Lean_budget_CPU=600,Lean_per_module_CPU=60,Lean_workers=1,first_cost_node_CPU=90,
    new_finite_scope='onlykeyspreadcoverandtwopointwitness670+670;nooldfield/projectionrerun',old7531_or_q8three_review_inherited=False)
for row in rows:
    m=row['other_metrics'];m['diagonal_fill_general_paper_review']=copy.deepcopy(general)
    m['diagonal_reallocation_two_targets_pending_proof_and_review']=copy.deepcopy(new_review)
    m['all_row_graph_instances_complete_Lean']=False
    m['new_reallocation_target_external_reviews_do_not_inherit_old_scopes']=True
    row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+[G,I+'NOTE.md',I+'RESULT.json',I+'TERMINAL.json',P]))
    row['lesson_and_restart_condition']+=' 通用纸面推导root及互补review支持实际partialovoid/任意uniformk；samecenter多copy两步、相邻center三步、diag自/他fillers与hub路线、四degreehist及Moore旧U witness均独立说明，尚非Lean/C范围。下一步是600CPU单worker/单module60/首90成本节点的新generic+两具体Lean，仅670+670关键spreadcover/witness，不重编旧field/projection。两原目标唯一A encoding/math cell559已发在途，不冒kernel或最终C通过；degree83k2仅公开门在途，0图，不计第146。'
q4=rows[0]['other_metrics'];q4['diagonal_fill_reallocation_prediction']['new_review_status']=copy.deepcopy(new_review)
g7532=next(g for g in q4['validated_graph_instances']if g['n']==7532)
g7532.update(best_located_public_lower_bound=7514,bounded_gain=18,public_comparison_status='EXCEEDS_SCOPED_BEST_LOCATED_GUARANTEE_BY18_PRIORITY_GLOBAL_UNKNOWN',external_A='CELL559_ACTUALLY_DISPATCHED_PENDING_MATH_ENCODING_ONLY',external_B='NOT_DONE',external_fresh_C='NOT_DONE',complete_concrete_Lean_status='IN_PROGRESS_NOT_COUNTED')
q4['diagonal_fill_reallocation_prediction']['concrete_Lean_status']='IN_PROGRESS_NOT_COUNTED'

row=rows[1];m=row['other_metrics'];p=m['diagonal_fill_reallocation_prediction']
p.update(status='ACTUAL_ROOT_MATHEMATICALLY_ACCEPTED_INDEPENDENT_PASS',actual_n=346516,actual_m=14204970,actual_max_degree=82,actual_exact_D=3,
    actual_degree_histogram=z['degree_histogram'],literal_H_source_edges_retained=13862745,actual_removed_edges=65,actual_added_edges=65,
    all4225_actual_U_neighborhoods_bound=True,actual_disjoint_U_pins=342160,actual_newroot_BFS=66,actual_changed_diagonal_BFS=65,actual_hub_BFS=1,
    actual_offdiagonal_BFS=0,actual_oldroot_BFS=0,measured_diagonal_hist=[1,80,5250,341185],measured_hub_hist=[1,65,5265,341185],
    offdiagonal_hist=[1,81,5329,341105],offdiagonal_hist_status='PREDICTED_NOT_MEASURED_THIS_RUN',measured_hist_mismatches=0,
    producer_CPU_seconds=.940117171,independent_CPU_seconds=t['total_CPU_seconds'],accepted_instances=1,new_accepted_graph_instances=1,
    new_Lean=0,concrete_Lean_status='IN_PROGRESS_NOT_COUNTED',new_review_status=copy.deepcopy(new_review),
    all_pairs_proof='H-Hretainsallsourceedges;allclones-U/clonesviaU-onlyendpointpaths;clones-fillerHpath/diagflagdetour;hubflagpaths;prefixoldinteriors',
    nonD2_actual_walk=[342290,80145,5833,0],evidence=Q8+'independent_acceptance/NOTE.md')
m['validated_graph_instances'].append(dict(Delta=82,D=3,n=346516,m=14204970,actual_diameter=3,mathematically_validated_complete_graph=True,
    complete_Lean_graph_instance=False,known_nonrecord=False,known_publicly_dominated=False,latest_global_record_confirmed=False,confirmed_publictable_improvement=False,
    best_located_public_lower_bound=346450,bounded_gain=66,public_comparison_status='EXCEEDS_SCOPED_BEST_LOCATED_GUARANTEE_BY66_PRIORITY_GLOBAL_UNKNOWN',
    graph_path=Q8+'graph_d82_D3_n346516.edges',degree_histogram=z['degree_histogram'],actual_newroot_BFS=66,actual_offdiagonal_BFS=0,actual_oldroot_BFS=0,
    all4225_actual_U_neighborhoods_bound=True,measured_histograms_all_match=True,offdiagonal_histogram_measured=False,all_pairs_old_only_U_H_prefix_proof=True,
    complete_concrete_Lean_status='IN_PROGRESS_NOT_COUNTED',external_A='CELL559_ACTUALLY_DISPATCHED_PENDING_MATH_ENCODING_ONLY',external_B='NOT_DONE',external_fresh_C='NOT_DONE',old_Q8_three_C_inherited=False,
    independent_acceptance=Q8+'independent_acceptance/RESULT.json'))
m['new_named_complete_graphs']=4
m['accepted_q8_terminal_graphs']=[327744,342290,346515,346516]
m['all_local_formal_processes_terminal']=False
m['all_local_formal_processes_scope']='oldthreeq8formalterminal;newreallocationgeneric+twooriginaltargetsactive,separate600CPUbudget'
m['completed_Lean_and_A_B_C_scope']='ONLYoldthreeoriginaltargets327744/342290/346515;notnew346516'
row['title']='q8三旧原目标全闭合/冻结；新346516重分配数学独验PASS，具体Lean与外审在途'
row['outcome_class']='OLD_Q8_THREE_COMPLETE_NEW346516_MATH_ACCEPTED_FORMAL_A_PENDING_NOT_INHERITED'
row['scope']+=' 新第四实例346516/14204970/max82/exactD3已独验/root数学接受；其具体Lean与A/B/C独立记账，原三target完整状态只适用旧三目标，冻结三图包不改。'
row['actual_D_scope']+=' 新346516用literal65删65添/完整H保边、4225NU绑定，actual66changedrootsBFS＋U/Hendpoint与prefix证明覆盖全部点对；off4160及old0BFS，不冒4225根本次全测。'
row['distance_text']+=' 第二规模实际346516/14204970/max82/exactD3：65删65添，H13862745全保，4225NU完整binding/342160disjointpins；hist65:1/80:65/81:4225/82:342225。只65diag+hub共66根actualBFS逐项match(1,80,5250,341185)/(1,65,5265,341185)，off4160和old根均0BFS；offhist(1,81,5329,341105)只是预测未本次测量。完整U/Hendpoint及prefix纸面证明补齐全点对，实际新根distance3walk342290—80145—5833—0。producer.940117171CPU/indep6.192139338CPU，新具体Lean/A/B/freshC未完成，不能继承原三target。'
new_evidence=[Q8+x for x in ['PARAMETERS.json','RESULT.json','TERMINAL.json','EDGE_DELTA.json','graph_d82_D3_n346516.edges','produce.cpp','run.py','independent_acceptance/NOTE.md','independent_acceptance/RESULT.json','independent_acceptance/TERMINAL.json','independent_acceptance/ALL_4225_TRUE_U_N_BINDINGS.tsv','independent_acceptance/EXACT_65_REMOVED_65_ADDED.tsv','independent_acceptance/ALL_66_CHANGED_ROOT_BFS.csv','independent_acceptance/NON_D2_ACTUAL_CHANGED_ROOT_WITNESS.json','independent_acceptance/INPUT_BINDING.json']]
row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+new_evidence))
assert all((R/x).is_file()for x in new_evidence+[G,I+'NOTE.md',I+'RESULT.json',I+'TERMINAL.json',P])
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
calls=[]
def call(*cmd):
    p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,145,36,37)
block=f'''<!-- {B} -->
# 当前：两张diagonal-fill新图已数学接受；Lean/A外审在途，未继承旧结论

同Goal ACTIVE，ledger420复用2现节点、0新行；145合法／36参数、stage41／33／Lean37，outside39／32、known43/main103_3/global0。旧三q8冻结包仍143／36／37快照，不改。

[q47532](experiments/{ids[0]}.md)与[q8346516](experiments/{ids[1]}.md)均实际数学PASS。后者346516/14204970/max82/exactD3，H13862745全保、65删65添、全部4225NU绑定；只65diag+hub66根actualBFS逐预测match，off4160/old0BFS，其余点对有NOTE完整U/H路线及prefix证明；producer.940117171/indep6.192139338CPU。offdiag距离分布仅预测，不能写成实测。

通用partialovoid/uniformk纸面推导由root及互补review支持，公式/四类度数/同center多copy/diag自他F/hub/Moore旧U witness已存两现节点，非新Lean或旧Cscope。600CPU单worker/每module60/首90成本点的新generic+两具体Lean在途；唯一两目标math/encoding A已发cell559/storediagonal_reallocation_A_review，尚未返回，B/freshC未做。degree83k2只公开门，0图；不计146，不展开梯子。以下保留历史。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 第二规模346516实际支持新路线规则；通用纸面证明与后续验收范围分离

本轮仅复用[7531/7532节点](experiments/{ids[0]}.md)、[q8节点](experiments/{ids[1]}.md)，ledger420，0新方法行。root已数学接受346516，使145合法／36参数、stage41／33；Lean仍37、outside39／32、known43/main103_3/global0。两新图7532和346516不继承旧7531或三q8的Lean/A/B/C；旧冻结三q8包维持143/36/37历史快照。

第二规模的具体预测经fresh实际检验支持：完整346516/14204970/max82/exactD3、65删65添/H13862745全保、4225个真实NU邻域全部绑定、342160不同U pins。degree65:1/80:65/81:4225/82:342225，65diag各(1,80,5250,341185)、hub(1,65,5265,341185)全部actualBFS逐项match；off4160预测(1,81,5329,341105)本次未测，不冒全4225根实测。old0/off4160BFS，NOTE用U-only端点替换、diag到自/他fillers与hub-flag路线/prefix证明完整覆盖剩余点对。实际distance3walk342290—80145—5833—0。producer.940117171、indep6.192139338CPU含compile，0旧field/projection重跑。

新增理解是mandatory clone-filler边确非所有三步路线所必需，省去后原U-only路线仍覆盖clone对、source保边仍覆盖H对，把释放fill度分配给hub同时覆盖全图；这改变生成，不能把它当固定邻接障碍反例。通用rootnote与独立paperreview具体核partialovoid、uniformk、四类degreehist、samecenter两步、adjacentcenter三步、Moore旧U pair永久无新2shortcut，不借hubcollapseHom；仅纸面SUPPORTED，未计新图/Lean/Ctarget。limitedpublicquery只继承7514/346450保证与+18/+66，负搜索不作原创性证据，exactpriority/全球UNKNOWN。

下一步只有600CPU/每module60/单worker/首90成本节点generic+两具体Lean，新增关键spreadcover和两点witness670+670，0旧field/projection续跑；唯一两原目标math/encoding A cell559/storediagonal_reallocation_A_review已发在途，非最终C/kernelPASS，B与distinctfreshC仍未做。degree83k2只f9公开竞争门，0图，不计146、不作为family完成。
''')
helper=R/'aris_repo/tools/research_wiki.py'
call(sys.executable,helper,'log',W,'Actual346516mathaccepted/14204970/cap82/exactD3;H13862745retained/65delete65add/full4225NUbinding/only66changedrootBFSmatched/off4160andold0BFS/U_Hendpointprefixproof. Producer.940117171CPU/indep6.192139338CPU.TwoNew7532_346516LeanandA_B_Cnotcompleted;singleAcell559pendingmathencoding/notfinalC. GeneralpartialovoiduniformkpaperSUPPORTED/formula_hist_MooreoldUpair/nographLeanCscope.600CPUoneworker60module90costnodegeneric+twotargetsinprogress/only670plus670newkeywitnesses.83k2publicgateonly0graph. Ledger420twoexistingrows145_36Lean37stage41_33/0reruns/rootedits/frozenpackunchanged.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_Q8_SECOND_SCALE_MATH_ACCEPTED_GENERAL_PAPER_SCOPE_AND_PENDING_NEW_PROOFS_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=2,
    named_legal_graphs=145,legal_parameter_pairs=36,stage_graphs=41,stage_pairs=33,complete_formula_Lean=37,outside_saved_main_pending_graphs=39,outside_saved_main_pending_pairs=32,
    known_publicly_dominated=43,saved_main_table_examples=103,saved_main_table_pairs=3,global_records_confirmed=0,new_graph_instances_counted=1,new_Lean=0,new_frameworks=0,
    graph346516=dict(status='ROOT_MATH_ACCEPTED_FRESH_INDEPENDENT_PASS',n=346516,m=14204970,Delta=82,D=3,full_NU_bindings=4225,actual_BFS_roots=66,actual_off_BFS_roots=0,actual_old_BFS_roots=0,off_histogram_measured=False,measured_hist_mismatches=0,producer_CPU=.940117171,independent_CPU=t['total_CPU_seconds']),
    two_new_targets_Lean='IN_PROGRESS_NOT_COUNTED',single_A='CELL559_ACTUAL_DISPATCH_PENDING_MATH_ENCODING_ONLY',new_B_finalC='NOT_DONE_NOT_INHERITED',generic_paper_review='SUPPORTED_NOT_KERNEL_OR_OLD_C_SCOPE',
    degree83k2='PUBLIC_GATE_ONLY_ZERO_GRAPH',new_evidence_paths_checked=len(new_evidence)+5,actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',query_current=True,
    math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_q8_packet_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
