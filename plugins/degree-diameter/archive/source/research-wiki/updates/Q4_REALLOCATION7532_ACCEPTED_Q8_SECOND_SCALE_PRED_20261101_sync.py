from pathlib import Path
from datetime import datetime, timezone
import copy, json, subprocess, sys

R = Path(__file__).resolve().parents[2]
W = R / 'research-wiki'
S = 'research/ddp/two_successful_methods_20261101/'
Q4 = S + 'retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation/'
Q8 = S + 'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/'
B = 'Q4_REALLOCATION7532_ACCEPTED_Q8_SECOND_SCALE_PRED_20261101'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ledger = json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
assert (ledger['record_count'], ledger['validated_named_graph_examples'], ledger['validated_named_parameter_pairs'], ledger['complete_Lean_graph_instances']) == (420,143,36,37)
ids = ['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101', 'ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101']
rows = [copy.deepcopy(next(x for x in ledger['rows'] if x['id']==i)['source_record']) for i in ids]
result = json.loads((R/Q4/'independent_acceptance/RESULT.json').read_text())
terminal = json.loads((R/Q4/'independent_acceptance/TERMINAL.json').read_text())
assert result['status'] == terminal['status'] == 'PASS'
assert (result['actual_order'],result['actual_edges'],result['max_degree'],result['exact_diameter'],result['new_roots_BFS'],result['old_roots_BFS']) == (7532,97750,26,3,290,0)
assert result['all_hist_predictions_match'] and result['literal_delta_PASS'] and result['all289_clone_bindings_PASS']

r=rows[0]; m=r['other_metrics']; p=m['diagonal_fill_reallocation_prediction']
p.update(status='ACTUAL_ROOT_MATHEMATICALLY_ACCEPTED_INDEPENDENT_PASS', predictions_verified=True,
         actual_n=7532, actual_m=97750, actual_max_degree=26, actual_exact_D=3,
         actual_degree_histogram=result['degree_histogram'], literal_removed_edges=17, literal_added_edges=17,
         literal_H_edges_retained=90525, all289_original_U_neighborhood_bindings_PASS=True,
         ordinary_new_root_BFS=290, old_root_BFS=0, all_three_histogram_classes_match=True,
         producer_CPU_seconds=0.195131966, independent_CPU_seconds=terminal['total_CPU_seconds'],
         new_mathematically_accepted_graphs=1, new_concrete_Lean=0, new_external_reviews=0,
         concrete_Lean_status='NOT_DONE_FOR7532', external_A='NOT_DONE_FOR7532', external_B='NOT_DONE_FOR7532', external_fresh_C='NOT_DONE_FOR7532',
         old7531_or_q8_reviews_inherited=False,
         all_pair_proof='All90525 H edges retained gives old-old D<=3; all290 new roots actual ordinary BFS cover all7532 targets. Old-only U/flag routes also prove modified-clone prefixes; hub last.',
         evidence=[Q4+'PREDICTION_AND_SCOPE.md',Q4+'independent_acceptance/NOTE.md',Q4+'independent_acceptance/RESULT.json',Q4+'independent_acceptance/TERMINAL.json'])
m['validated_graph_instances'].append(dict(Delta=26,D=3,n=7532,m=97750,actual_diameter=3,mathematically_validated_complete_graph=True,
    complete_Lean_graph_instance=False,known_nonrecord=False,latest_global_record_confirmed=False,confirmed_publictable_improvement=False,
    public_comparison_status='PRIORITY_AND_LATEST_GLOBAL_UNKNOWN; sameparameter7514publicmechanismgate inherited, no new public search',
    external_A='NOT_DONE',external_B='NOT_DONE',external_fresh_C='NOT_DONE',
    actual_newroot_BFS=290,actual_oldroot_BFS=0,independent_acceptance=Q4+'independent_acceptance/RESULT.json'))
m['new_named_complete_graphs']=2
r['title']='GQ(4,4)原邻域7531及diagonal-fill重分配7532：后者数学独验PASS，Lean/外审未做'
r['record_type']='complete_literal_graph_family_global_novelty_pending'
r['outcome_class']='OLD7531_LEAN_A_B_C_COMPLETE_NEW7532_MATH_ACCEPTED_LEAN_REVIEWS_NOT_DONE'
r['scope'] += ' 新7532实例从同一H直接生成modified clones再hub；保全部H旧边，改变旧7531的17条mandatory clone-filler边，因此超出固定旧邻接障碍。新7532不继承原7531或q8的Lean/外审。'
r['actual_D_scope'] += ' 新7532由独验全部290新根普通BFS加H-H保边覆盖全点对，exactD3新根见证7242—3145—1—0；0旧根BFS。'
r['distance_text'] += ' 新7532/97750/max26/exactD3已root数学接受：H90525旧边全保，字面17删17添，全289 N_U逐项绑定、7208不同U pins；degree17:1/24:17/25:289/26:7225。290新根逐三类预测全match：17×(1,24,418,7089)、272×(1,25,441,7065)、hub(1,17,425,7089)；0旧根BFS。producer0.195131966CPU、独验1.189883820CPU。具体7532Lean/A/B/freshC均未做，未继承旧图。'
r['unclosed_gap']=r['unclosed_gap'].replace(' 新diagonal_fill_reallocation目前只登记事前预测，尚未root数学验收/未计数；完整root返回后另记实际预测是否命中。',' 新7532已数学接受且三类预测全命中；其具体Lean与A/B/freshC尚未做，旧7531全部完成状态只适用原7531。精确公开优先权与最新全球状态仍UNKNOWN。')
r['lesson_and_restart_condition'] += ' 实际7532支持“原U内点路线足够、释放diagonal filler负载交给hub”的具体预测；仅保H边而改变mandatory clone边成功，不能据此反驳固定mandatory边障碍。下一次仅据此做q8同规则第二规模测试，未自动扫参数。'
new_evidence=[Q4+x for x in ['PARAMETERS.json','RESULT.json','TERMINAL.json','EDGE_DELTA.json','graph_d26_D3_n7532.edges','produce.py','independent_acceptance/NOTE.md','independent_acceptance/RESULT.json','independent_acceptance/TERMINAL.json','independent_acceptance/ALL_289_CLONE_BINDINGS.tsv','independent_acceptance/ALL_290_NEW_ROOT_BFS.tsv','independent_acceptance/EXACT_LITERAL_DELTA.json','independent_acceptance/NON_D2_ACTUAL_NEW_ROOT_WITNESS.json']]
r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+new_evidence))

r=rows[1]
r['other_metrics']['diagonal_fill_reallocation_prediction']=dict(
    status='SECOND_SCALE_PREDICTION_NOT_ACCEPTED', prior_small_actual_PASS=[26,3,7532,97750],
    source_H_n=342290, source_H_m=13862745, classical_U_n=342225,
    old_complete_graph_n=346515, all_H_source_edges_retained=True,
    omitted_diagonal_clone_filler_edges=65, hub_label=346515, hub_filler_edges_added=65,
    expected_n=346516, expected_m=14204970, expected_max_degree=82, expected_exact_D=3,
    expected_degree_histogram={'65':1,'80':65,'81':4225,'82':342225},
    predicted_newroot_histograms=[dict(kind='modified_diagonal',count=65,hist=[1,80,5250,341185]),dict(kind='offdiagonal',count=4160,hist=[1,81,5329,341105]),dict(kind='hub',count=1,hist=[1,65,5265,341185])],
    producer_CPU_budget=30, independent_CPU_budget=40, planned_actual_BFS_roots=66,
    actual_BFS_scope='only65 modified diagonal clones plus hub; unchanged4160 inherit old-only paper routes, no repeatBFS',
    status_does_not_inherit_q8_three_Lean_or_reviews=True, new_accepted_graph_instances=0, new_Lean=0,
    public_priority='UNKNOWN', automatic_next_parameter_ladder=False,evidence=Q8+'PREDICTION_AND_SCOPE.md')
r['lesson_and_restart_condition'] += ' q4实际7532三类新根全命中后才授权q8第二规模同规则测试：省65条diagonalclone→fill边、hub连65fillers，保H全部13862745边，预测346516/14204970/Δ82D3；仅changed65+hub做新BFS，producer30CPU/独验40CPU。它是待验预测，不加第145图、不继承本节点三旧原目标Lean/Cscope；冻结三图包不改。'
r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+[Q8+'PREDICTION_AND_SCOPE.md']))
assert all((R/p).is_file() for p in new_evidence+[Q8+'PREDICTION_AND_SCOPE.md'])
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
calls=[]
def call(*cmd):
    p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True)
    calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
    assert p.returncode==0,(cmd,p.stderr,p.stdout)
    return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,144,36,37)
block=f'''<!-- {B} -->
# 当前：7532新规则数学独验PASS；q8同规则第二规模346516仅预测

同Goal ACTIVE，ledger420复用2现节点、0新行；144合法／36参数、stage40／33、Lean37，known43/main103_3/global0不变。旧三q8冻结包仍143／36／37历史快照，不改。

[q4重分配7532实际验收](experiments/{ids[0]}.md)：保7242源H全部90525边，旧7531的17条diagclone→filler边改为hub→filler；实际7532/97750/Δ26/exactD3。全289 N_U绑定、literal17删17添及290新根逐三类预测全部PASS；0旧根BFS，producer0.195131966/独验1.189883820CPU。旧旧点对继承H，全新根BFS覆盖其余全部点对；7532具体Lean/A/B/freshC未做，不继承7531或q8旧结论。

[q8第二规模预测](experiments/{ids[1]}.md)：同规则省65条diagclone→fill边、hub连65fillers且保H全部13862745边，预测346516/14204970/Δ82D3；producer≤30CPU、freshindep≤40CPU，只65changed+hub新BFS。尚未实际验收，不计第145图/Lean/新Ctarget。以下保留原预测与障碍历史。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 新连接规则7532实际支持；转同规则q8第二规模预测

本轮唯一Wiki最小增量复用[原7531节点](experiments/{ids[0]}.md)和[q8节点](experiments/{ids[1]}.md)，ledger420/0新方法行。root数学接受7532使144合法／36参数、stage40／33；Lean仍37，known43/main103_3/global0不变。旧7531合法及Lean/A/B/C仍保留，新增7532只有数学及fresh独验PASS，不继承那些完成状态。

此前问题是fixed mandatory clone边的饱和障碍；实际改变生成仅保H源90525边、让289clones用原U邻域、省17diagclone-fill边并让hub接17fillers。事前三类预测经全部290新根普通BFS逐项支持：17diag(1,24,418,7089)、272offdiag(1,25,441,7065)、hub(1,17,425,7089)，0偏差。全289 N_U字面绑定、7208differentpins与literal17删17添PASS，degree17:1/24:17/25:289/26:7225，完整7532/97750/exactD3。H-H对继承保边源，所有剩余对被全新根BFS覆盖；纸面old-only U/flag路线同时解释每modified-cloneprefix及hub最后规则。producer0.195131966、freshindep1.189883820CPU，0旧根/field/solver/Lean。实际新根见证7242—3145—1—0距离3。新图不是原7531保全边单点append，未推翻固定旧邻接障碍。

据此只做有依据的第二规模检验：q8原342290源H、4225原U-neighborhoodclones，省65diagclone-fill边并加hub连65fillers；预测346516/14204970/Δ82D3，degree65:1/80:65/81:4225/82:342225。diag65预测(1,80,5250,341185)、offdiag4160预测(1,81,5329,341105)、hub(1,65,5265,341185)。producer30CPU、独验40CPU，仅changed65+hub普通BFS，unchangedoffdiag用old-only路线继承，0旧root/field/Lean。尚无root验收，不计145，0新Lean/reviewscope；既有三q8冻结包保持143/36/37快照，公开精确优先权仍UNKNOWN，不把smallPASS当大规模已PASS。
''')
helper=R/'aris_repo/tools/research_wiki.py'
call(sys.executable,helper,'log',W,'Actual7532accepted:7532/97750/cap26/exactD3;allH90525edgesretained;literal17delete17add;289NUbindings;all290newrootBFSthreeclasspredictionsPASS;oldroot0;producer.195131966CPU/independent1.189883820CPU.New7532Lean_A_B_Cnotdone/notinherited.Q8secondscale346516/14204970cap82predictiononly:65delete65add,30producer40indepCPU,only66BFSplanned/notaccepted/no145.FrozenQ8untouched.Ledger420twoexistingrows144_36Lean37stage40_33;0mathreruns/rootfileedits.')
call(sys.executable,helper,'rebuild_index',W)
call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_Q4_REALLOCATION7532_MATH_ACCEPTED_Q8_SECOND_SCALE_PREDICTION_ONLY_WIKI_SYNC',updated_UTC=now,
    ledger_records=420,records_added=0,records_updated=2,named_legal_graphs=144,legal_parameter_pairs=36,stage_graphs=40,stage_pairs=33,complete_formula_Lean=37,
    new_graph_instances_counted=1,new_Lean=0,new_frameworks=0,known_publicly_dominated=43,saved_main_table_examples=103,saved_main_table_pairs=3,global_records_confirmed=0,
    outside_saved_main_pending_graphs=38,outside_saved_main_pending_pairs=32,
    graph7532=dict(status='ROOT_MATH_ACCEPTED_FRESH_INDEPENDENT_PASS',n=7532,m=97750,Delta=26,D=3,actual_newroot_BFS=290,oldroot_BFS=0,prediction_mismatches=0,
        producer_CPU=.195131966,independent_CPU=terminal['total_CPU_seconds'],concrete_Lean=False,external_A_B_C='NOT_DONE_NOT_INHERITED'),
    candidate346516=dict(status='PREDICTION_NOT_ACCEPTED',expected_n=346516,expected_m=14204970,Delta=82,D=3,accepted_instances=0,producer_CPU_budget=30,independent_CPU_budget=40,planned_newroot_BFS=66),
    new_evidence_paths_checked=len(new_evidence)+1,actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',query_current=True,
    math_BFS_solver_Lean_runs_this_sync=0,root_owned_files_modified=False,frozen_q8_packet_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
