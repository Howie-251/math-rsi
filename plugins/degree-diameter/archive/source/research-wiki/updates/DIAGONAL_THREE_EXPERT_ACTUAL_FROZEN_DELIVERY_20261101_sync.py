from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';E='expert_review_current/DIAGONAL_REALLOCATION_THREE_RESULTS_20261101';B='DIAGONAL_THREE_EXPERT_ACTUAL_FROZEN_DELIVERY_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
f=json.loads((R/(E+'_FREEZE_RECEIPT.json')).read_text());assert f['status']=='FROZEN_THREE_REALLOCATION_RESULTS_MATH_KERNEL_REVIEWS_PRIORITY_UNKNOWN'
assert (f['package_bytes'],f['package_entries'],f['raw_edge_files'],f['raw_bytes'])==(219512166,1439,7,761809181)
assert f['snapshot']==dict(named=146,parameters=37,Lean=40,stage_graphs=42,stage_parameters=34)
assert all(all(v[k]=='PASS'for k in ['math','formal','binding'])for v in f['three_original_math_formal_binding_verdicts'].values())
assert f['fresh_final_C_thread']=='53b69de0-5f49-43ba-b3ee-1b37db7c804a' and f['priority']=='UNKNOWN' and not f['global_record_certified']
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
ids=['ddp-gq44-ovoid-spread-immutable-full-neighborhood-clones-7531-d26-d3-20261101','ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101','ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101'];rows=[copy.deepcopy(next(x for x in L['rows']if x['id']==i)['source_record'])for i in ids]
delivery=dict(status=f['status'],snapshot=f['snapshot'],ZIP=f['ZIP'],ZIP_bytes=f['package_bytes'],ZIP_entries=f['package_entries'],raw_edge_files=7,raw_bytes=f['raw_bytes'],compression_level=1,
    actual_CPU_seconds=f['CPU_seconds'],CPU_budget=90,three_original_math_kernel_Audit_binding_A_B_distinctfreshC_complete=True,actual_final_C_thread=f['fresh_final_C_thread'],
    priority='UNKNOWN',global_record_certified=False,freeze_receipt=E+'_FREEZE_RECEIPT.json',freeze_executed=True,archive_immutable=True,
    new_barrier_calibration_refinement_entries=0,extra_metadata_check_provenance='rootacceptedf9onepostfreezeZIPmetadataread:matched/no_duplicate_or_partial/newresearchentries0',
    archive_opened_or_metadata_rechecked_by_this_sync=False,old_packets_modified=False,large_graph_BFS_Lean_solver_or_review_runs=0)
for r in rows:
    m=r['other_metrics'];m['diagonal_three_frozen_delivery_snapshot']=copy.deepcopy(delivery)
    r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+[f['ZIP'],E+'_FREEZE_RECEIPT.json']))
for r in rows[:2]:
    r['lesson_and_restart_condition']+=' 一次新专家freeze现actualSUCCESS，219512166B/1439entries/7raw761809181B/level1/7.761951546CPU，归档146/37/Lean40/stage42_34；三原图数学/kernel/Audit/A/B/distinctfreshC全完成，priorityUNKNOWN/globalfalse。新barrier/230/cap31refinement条目0，另研究未冒C审。只记录真实ZIP/receipt，不重复freeze/元数据检查/图核验，原包immutable；当前未派新搜索。'
q4=rows[0];q4['title']='GQ(4,4)新7532全部数学/kernel/A/B/freshC完成，三图专家包已实际冻结'
q4['outcome_class']='COMPLETE_MATH_KERNEL_A_B_FRESHC_AND_FROZEN_EXPERT_DELIVERY_PRIORITY_UNKNOWN'
q8=rows[1];m=q8['other_metrics'];m['new_reallocation_three_expert_delivery'].update(delivery)
m['new_reallocation_three_expert_delivery'].update(root_explicit_one_freeze_authorized=True,new_ZIP_exists_claimed=True,remaining_gate='noneforthisfrozendelivery;priorityandbroaderGoalnotcompleted')
q8['title']='新规则三原图完整验收/Lean/A/B/独立freshC与专家ZIP均完成，priorityUNKNOWN'
q8['outcome_class']='THREE_NEW_RULE_ORIGINAL_TARGETS_AND_EXPERT_FROZEN_DELIVERY_COMPLETE_PRIORITY_UNKNOWN'
q8['distance_text']+=' 唯一授权freeze实际SUCCESS：ZIP219512166字节/1439条目/7完整raw761809181字节/level1，实际7.761951546CPU<90；归档snapshot146/37/Lean40/stage42_34。f9仅一次metadata核对匹配、无duplicate/partial，旁支barrier/校准/refinement条目0；本同步不重开ZIP，不核图，不改归档。'
rows[2]['other_metrics']['diagonal_three_frozen_delivery_snapshot']['this_barrier_toy_cap31_research_in_archive_or_review_scope']=False
rows[2]['lesson_and_restart_condition']+=' 当前三图专家包已实际冻结，只有它的三原目标属于Cscope；新productbarrier/230calibration/cap31paper在该ZIP条目0。此处保存交付范围边界，不把旁支当已C审或已归档、不增任何图/Lean计数。'
e=[f['ZIP'],E+'_FREEZE_RECEIPT.json'];assert all((R/x).is_file()for x in e)
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,146,37,40)
block=f'''<!-- {B} -->
# 当前：三新原图专家包已实际冻结；146／37／Lean40，未派新搜索

同Goal ACTIVE，ledger420只复用3现节点/0新行，146合法／37参数、stage42／34、Lean40、outside40／33、known43/main103_3/global0不变。三原图7532/346516/350742数学/独验/具体kernel/Audit/绑定/新A/B/distinctfreshC实际齐，priorityUNKNOWN/globalfalse。

[实际ZIP](../{f['ZIP']})219512166B／1439entries／7raw761809181B，level1，7.761951546CPU<90；[FREEZE_RECEIPT](../{E}_FREEZE_RECEIPT.json)为146／37／Lean40/stage42_34不可变归档。f9一次metadata核对匹配/无duplicate或partial；新barrier、230校准、cap31refinement条目0且不属Cscope。本同步只读receipt、核两路径存在，未重开ZIP或重验图。小窗口停止、大窗口四候选仍未派；本回执后stop写入，旧包/根文件未改。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 唯一专家freeze实际完成，交付状态收束

原Wiki仅复用[7532机制](experiments/{ids[0]}.md)、[q8机制](experiments/{ids[1]}.md)、[现barrier范围](experiments/{ids[2]}.md)，ledger420/0新行，146／37／Lean40、stage42／34、outside40／33、known43/main103_3/global0不变。实际FREEZE_RECEIPT已读：[ZIP](../{f['ZIP']})219512166字节、1439entries、7raw761809181字节、level1、7.761951546CPU<90，snapshot146/37/Lean40/stage42_34。三原图数学/kernel/A/B/distinctfreshC皆完整，priorityUNKNOWN/globalfalse。归档本体不可变，旧冻结包未改。

f9额外仅一次archive metadata核对匹配，无duplicate/partial，新barrier/230校准/cap31refinement条目0；这三旁支不属本三图C审范围。此同步没有重开ZIP、重验图/field/BFS/Lean/solver或增加paidcall，只有实际receipt和路径链接/日志/query更新。未新增图、Lean或方法，不恢复小窗口，不派大窗口四候选或其他搜索。写完本实际receipt后停止写入；根STATE/REPORT/progress/恢复仍由root负责，Goal未标完成。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'ActualONEexpertfreezeSUCCESSDIAGONAL_REALLOCATION_THREE_RESULTS_20261101ZIP219512166B1439entries7raw761809181Blevel1CPU7.761951546under90snapshot146_37Lean40stage42_34;mathkernelABCcompletepriorityUNKNOWNglobalfalse. Rootacceptedf9oneZIPmetadatacheckmatchednoduplicatepartial/newbarrier_toy_refinemententries0notCscope. ThisWikiupdateonlyreadsactualreceipt/pathsexist/noarchiveopenorvalidation/freeze/paidcall. Ledger420threeexistingrowscountsunchanged/noqueuedsearch/rootownedoldfrozenuntouched/stopafterreceipt.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_THREE_EXPERT_ACTUAL_FROZEN_DELIVERY_MINIMAL_WIKI_SYNC_STOPPED',updated_UTC=now,ledger_records=420,records_added=0,records_updated=3,named_legal_graphs=146,legal_parameter_pairs=37,stage_graphs=42,stage_pairs=34,complete_formula_Lean=40,new_graphs=0,new_Lean=0,new_frameworks=0,
    actual_freeze_receipt=E+'_FREEZE_RECEIPT.json',ZIP=f['ZIP'],ZIP_bytes=f['package_bytes'],ZIP_entries=f['package_entries'],raw_files=7,raw_bytes=f['raw_bytes'],freeze_CPU=f['CPU_seconds'],priority='UNKNOWN',global_record_certified=False,
    new_barrier_calibration_refinement_archive_entries=0,receipt_read=True,paths_checked=2,archive_reopened_this_sync=False,actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_Lean_solver_review_or_freeze_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False,new_search_dispatched=False,writes_stopped_after_this_receipt=True)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
