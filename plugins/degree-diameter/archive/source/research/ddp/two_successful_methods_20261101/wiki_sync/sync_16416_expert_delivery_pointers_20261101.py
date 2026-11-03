"""Delivery pointers only;one small existence check,no package or experiment rerun."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';OUT=R/'research/ddp/two_successful_methods_20261101/wiki_sync'
LABEL='D16_16416_PORTABLE_EXPERT_DELIVERY_POINTERS_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rid='ddp-d16d4-whole27-fulln-clone864-graph16416-20261101'
base='expert_review_current/D16_D4_16416_20261101'
links=dict(ZIP=base+'.zip',HTML=base+'.html',HTML_source=base+'.html.txt',Word=base+'.docx',
    README=base+'_files/README.md',reproduce=base+'_files/reproduce.py',pack_receipt=base+'_files/PACK_RECEIPT.json')
# One compact actual artifact-link check;do not openZIP or regenerate/revalidate contents.
missing=[p for p in links.values() if not(R/p).is_file()];assert not missing,missing
pack=json.loads((R/links['pack_receipt']).read_text())
assert pack['status']=='COMPLETE_ONE_PORTABLE_EXPERT_SOURCE_ZIP_ALL_THREE_NEW_SCOPE_REVIEWS_ACTUAL_PASS'
assert pack['archive']==links['ZIP'] and pack['ZIP_bytes']==2182955
assert pack['portable_replay_direct_byte_equal_to_accepted'] and pack['new_graph_replays']==1
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());before=L['record_count'];records={r['id']:r for r in L['rows']}
assert before==439 and tuple(L[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances'])==(153,43,47)
raw=copy.deepcopy(records[rid]['source_record']);assert raw['other_metrics']['complete_exact_scope_technical_reviews']
delivery=dict(status=pack['status'],links=links,ZIP_bytes=pack['ZIP_bytes'],
    project_local_Lean_import_closure_sources=79,direct_document_local_links=58,
    inherited_packager_actual_replays=1,inherited_portable_output_bytes=1375506,
    inherited_direct_byte_equal_to_accepted=True,new_replays_in_this_Wiki_delta=0,
    inherited_pack_CPU_seconds=pack['charged_CPU_seconds'],pack_CPU_budget_seconds=30,
    technical_A_B_distinctfreshC_complete=True,source_graph_BFS_Lean_reviews_repeated=0,
    human_expert_feedback='NOT_RECEIVED',Goal_complete=False,global_priority='UNKNOWN',
    URSA_report_gap_closed=False,old_packages_modified=False)
raw['other_metrics']['portable_expert_delivery']=delivery
raw['other_metrics']['human_expert_feedback']='NOT_RECEIVED'
raw['other_metrics']['Goal_complete']=False
raw['unclosed_gap']='Global priority/method originality UNKNOWN;URSA LA-UR-26-28353 report remains unlocated/unread. Human expert feedback has not been received,so Goal is not complete. Packing32 maximality is separately unproved;the technical suite and portable package are terminal.'
raw['evidence_paths'].extend(p for p in links.values() if p not in raw['evidence_paths'])
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
rowpath=OUT/f'{LABEL}_ROW.json';rowpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date']
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):c['write_node'](n)
records[rid]=n;L.update(rows=list(records.values()),updated_UTC=NOW);L['input_counts'][str(rowpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def mdlinks(prefix):
    labels={'ZIP':'专家ZIP','HTML':'HTML','HTML_source':'HTML原样源码','Word':'Word','README':'README','reproduce':'独立复现脚本','pack_receipt':'打包实际收据'}
    return ' · '.join('['+labels[k]+']('+prefix+p+')' for k,p in links.items())
node=W/'experiments'/f'{rid}.md'
node.write_text(node.read_text()+'\n\n<!-- '+LABEL+' -->\n## 便携专家交付\n\n'+mdlinks('../../')+'\n\n唯一新包2182955bytes，包含原source raw、新16416图、79个project-local Lean import closure和58条直接文档链接。包内standalone生成器仅由packager实际运行一次，重建1375506B并与accepted边表直接byteequal；这里继承该收据，0BFS/field/Lean/review或生成器重跑。打包1.286912953/30CPU，旧包未动。数学、kernel及新A/B/distinctfreshC技术审阅完整结束；globalpriority及URSA报告缺口仍UNKNOWN，人工专家反馈尚未收到，Goal保持ACTIVE不标完成。\n')
nav='<!-- '+LABEL+' -->\n### '+NOW+' 16416唯一便携专家包已实际完成\n\n'+mdlinks('../')+'\n\nZIP2182955bytes；actual三独立thread全PASS的HTML/txt/Word、原raw+新graph、79本地Lean imports/58directlinks齐。packager唯一standalone replay重建1375506B与accepted图直接byteequal，1.286912953/30CPU；本次只做一次links-exist小检查与加指针，0重复生成/BFS/field/Lean/付费或宽审计，旧包未动。439记录、153图／43参数／Lean47、savedmain105/4、global0不变，技术全complete。globalpriority/URSA报告缺口仍UNKNOWN；人工专家反馈未收，sameGoal ACTIVE，不宣Goal完成；15老格人工顶部与旧N8/n61暂停保留。\n\n[16416当前规范节点](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
    assert text[:at]==pre;path.write_text(text);preserved[fn]=True
mp=W/'DDP_METHOD_LEDGER.md';text=mp.read_text();assert LABEL not in text
mp.write_text(text+'\n\n<!-- '+LABEL+' -->\n## '+NOW+' 16416专家便携交付指针（计数不变）\n\n'+mdlinks('../')+'\n\n只为既有16416版本补实际交付入口，不加节点/图/参数/Lean/方法。technical reviews全终态；globalpriority/URSA报告缺口仍UNKNOWN，humanexpertfeedback未收、Goal ACTIVE。\n')
helper.append_log(str(W),LABEL+': existing16416node/recoveryentries only portableZIP,HTML/txt/Word,README/reproduce/PACK_RECEIPT pointers;one compact artifactexistencecheck,noZIPopen/replay/BFS/field/Lean/review/wideaudit. Counts439,153/43/47,savedmain105/4/global0unchanged,technicalcomplete,globalpriority/URSAreportgapUNKNOWN,humanexpertfeedbacknotreceived,sameGoalACTIVE,oldpackagesuntouched.')
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==before
assert tuple(after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples'])==(153,43,47,105)
receipt=dict(status='PASS_EXISTING16416_PORTABLE_EXPERT_DELIVERY_POINTERS_ONLY',updated_UTC=NOW,
    records_before=before,records_after=before,records_added=0,canonical_graph_node=rid,
    graph_parameter_Lean_method_increments=[0,0,0,0],artifact_links=links,artifact_link_exists_batch_count=1,
    missing_artifact_links=missing,ZIP_bytes_in_actual_pack_receipt=2182955,
    packager_replay_and_byte_equality_inherited=True,new_generator_BFS_field_Lean_paidreview_hash_runs=0,
    ZIP_content_wide_audit_or_repack_runs=0,old_packages_modified=False,
    counts=dict(graphs=153,parameters=43,Lean=47,savedmain_graphs=105,savedmain_parameters=4,global_confirmed=0),
    technical_suite_complete=True,human_expert_feedback='NOT_RECEIVED',Goal_complete=False,sameGoal='ACTIVE',
    global_priority='UNKNOWN',URSA_report_gap_closed=False,human_top_blocks_preserved_exact=preserved,
    full_index_query_rebuild=False,root_STATE_HTML_progress_REPORT_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
