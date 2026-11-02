"""One actual terminal experiment delta; no rebuild, reimport, or math computation."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,csv,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4]
W=ROOT/'research-wiki'; S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/thirdcut_route_repair1252'
started=time.process_time(); now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d3d10-conder1250-frozen4536-protected1178-thirdcut-pintransfer-complete-no-20261101'
marker='<!-- SOURCE1250_FROZEN_THIRDCUT_TERMINAL_20261101 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text()); before_count=ledger['record_count']
assert before_count==len(ledger['rows'])==449
assert not any(r['id']==slug or 'thirdcut_route_repair1252' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
result=json.loads((D/'RESULT.json').read_text()); terminal=json.loads((D/'TERMINAL.json').read_text())
assert result['status']=='COMPLETE_NO_FIXED_FROZEN_BASE_TRANSFER' and result['visited_configs']==result['domain_configs']==11178
assert result['P1_pilot_pass']==9 and result['P3_pilot_supported']==6 and result['both_newroot_pass']==0
rows=list(csv.DictReader((D/'CONFIG_RESULTS.tsv').open(),delimiter='\t'))
p=[r for r in rows if r['stage']=='A_SAVED_TARGET' and r['moved_pin']=='869']
assert [(int(r['config_id']),int(r['first_bad_target'])) for r in p]==[(10059,1057),(10629,1056),(10851,1057)]
oldnode='ddp-conder1250-edge-subdivision-two-cut-helper-family-20261027'
old=next(r for r in ledger['rows'] if r['id']==oldnode)
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
# Preserve the existing human entry byte for byte; the helper's global rebuilding is disabled.
files=['index.md','query_pack.md','gap_map.md']
original={f:(W/f).read_text() for f in files}
end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
human={f:s[:s.index(end)+len(end)] for f,s in original.items()}
counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
evidence_names=['READ_GATE.md','READ_GATE.json','FROZEN_BASE.json','PRED.md','THIRDCUT_ROUTE_PAPER.md','P3_ADDENDUM.md','THIRDCUT_SCOPE_ATTACK.md','PUBLIC_BASELINE_20261101.json','run_once.cpp','run_once.py','ACTUAL_DOMAIN.json','NUMERIC_RESULT.json','RESULT.json','TERMINAL.json','DRIVER_HANDLE.json','CONFIG_RESULTS.tsv','PILOT_PATHS.jsonl','FIRST_FAILURE.json','ROUTE_CLASS_SUMMARY.json','NOTE.md','INITIAL_PATH_FAILURE_run_once.py','INITIAL_PATH_FAILURE_RESULT.json','INITIAL_PATH_FAILURE_TERMINAL.json','INITIAL_PATH_FAILURE_NUMERIC_ERROR.txt']
evidence=[str((D/n).relative_to(ROOT)) for n in evidence_names]
assert all((ROOT/e).exists() for e in evidence)
if (D/'ROOT_DISPOSITION.json').exists(): evidence.append(str((D/'ROOT_DISPOSITION.json').relative_to(ROOT)))
raw={
'id':slug,
'title':'3D10 Conder1250固定object4536三cut修补：11178全新x失败；修1058又失旧覆盖',
'family':old['method_family'],
'idea_family':'idea:ddp-open-parameter-construction-20261026',
'date':'2026-11-01','wiki_verdict':'no',
'record_type':'fixed_existing_host_threecut_twohelper_route_repair_experiment',
'target_Delta':3,'target_D':10,'savedL':1250,
'baseline_date':'2026-11-01 primary desc_g10 checked by root; published1250 known2006-08-17; source validity inherited',
'n':{'actual':None,'hypothetical':1252},'actual_graph_Delta':3,'actual_D':None,
'actual_D_scope':'All11178 modified1252 cubic parameter-configurations fail the actual new-X R10 test. Each first failed-pair distance is stored; no global candidate exact diameter or old-source D10 revalidation is claimed.',
'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':10,'new_lower_bound':False,
'outcome_class':'COMPLETE_NO_FIXED_FROZEN4536_PROTECTED_X1178_THIRDCUT_PIN_TRANSFER',
'scope':'Fixed literal Conder1250; anchor(0,1), second edge id1515=(869,1178), old object4536 x1250 pins{0,1178}/y1251 pins{1,869}, x-y retained. Protect x-1178; move only p in{0,1,869}; third original edge(g,h) is vertex-disjoint from allfour basepins, either orientation, repair(p,h) must be an original-source nonedge. Delete the three source edges; replace the one helper-p spoke by helper-g and add repair p-h. Actual1865 thirdedges and11178 configurations fully tested, pilot9 not repeated. This is not all oldB bases, not whole threecut/repair family, not general3D10NO.',
'distance_text':'旧A唯一saved缺点1178由选base的x-1178直连保住；旧B object4536的saved缺点1058是本次pilot目标。P1九例全支持，新x/y到1058是1/2；P3移p0或p1六例x到withdrawnp均11。移p869三例x到869仍10，首缺点按id10059/10629/10851为1057/1056/1057，均距11，非皆1057。全11178中5454修好x到saved1058但全部NEW_X仍fail，P2存在both-newroot-pass被完整域反驳。0旧根候选BFS、0sourceD10复验；最终2.774601871/20CPU含首次路径错误、编译与root只读metadata.1。0新图/参数/Lean。',
'lesson_and_restart_condition':'STOP this frozen4536/protected1178 transfer domain. A short direct repair to saved1058 is insufficient: p0/p1 sacrifice the withdrawn-pin responsibility, while p869 preserves its own distance10 yet misses farther1056/1057 coverage. Old cached route869-1234-1057 is length2, not adjacency. Any later rule must address simultaneous replacement of lost coverage; no automatic newbase/seed/thirdcut timer.',
'restart_condition':'Only a newly authorized bounded structural question that compensates the lost route regions or changes the frozen base/operation; do not repeat this complete11178 domain.',
'unclosed_gap':'Other oldB objects, different protected pins, other threecut/repair operations, morehelpers and general(3,10) remain unexcluded. Old source validity/girth/source distances are inherited, not rechecked. No candidate passed bothnewroots, so oldold and global candidate diameter stages were not entered. Goal ACTIVE; oldN8n61 PAUSED.',
'positive_guarantees':[
'Frozen base selection inherits cached5614 oldB objects and chooses lexfirst secondedge containing1178 with x-pins{0,1178}; it does not choose by totalbadscore or rerun oldtwo-cutNO.',
'Actualmodified ordinaryBFS includes repair/helper mixed routes; protectedx1178 and pilot saved1058 are measured in all9 actual pilot graphs.',
'P3 is a conditional paper route implication under inherited literal source/girth/distances, separately supported by6of6 actual pilot measurements; it is not a new Lean theorem.',
'Full1865/11178/9 domain counts match preregistered predictions; fixed parameter domain completed with no budget cutoff. All configs fail NEW_X, not oldold.',
'First failure stores actual length11 path x-1058-933-635-274-146-82-34-18-6-2-0 with edge roles. Route tables describe first failures, not all missing-target sets.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,
'old_source_node':oldnode,'source_n':1250,'source_m':1875,'source_D10_inherited':True,'source_girth16_inherited':True,'source_parse_successes':1,'failed_source_open_attempts':1,'source_D10_validation_BFS':0,
'frozen_object_id':4536,'second_edge_id':1515,'anchor':[0,1],'second_edge':[869,1178],'x_pins':[0,1178],'y_pins':[1,869],'oldA_saved_target':1178,'oldB_saved_target':1058,'protected_edge':[1250,1178],'moved_pins':[0,1,869],
'eligible_thirdedges':1865,'legal_parameter_configs':11178,'visited_configs':11178,'configs_are_not_distinct_graph_count':True,'pilot_configs':9,'full_remainder_configs':11169,'pilot_configs_not_repeated':True,
'new_X_BFS':11178,'new_Y_BFS':9,'modified_oldroot_BFS':0,'bothnewroot_PASS':0,'saved1058_X_repaired_configs':5454,
'P1_verdict':'SUPPORTED_9_OF_9_ACTUAL_PILOTS','P2_verdict':'REFUTED_BY_COMPLETE_FIXED_DOMAIN_NO','P3_verdict':'SUPPORTED_6_OF_6_P0_P1_PILOTS',
'P3_withdrawn_distance_each':11,'p869_pilot_withdrawn_distance_each':10,'p869_pilot_ids':[10059,10629,10851],'p869_pilot_firstbad_targets':[1057,1056,1057],'p869_pilot_firstbad_distances':[11,11,11],
'cached_869_to1057_route':[869,1234,1057],'cached_route_is_direct_neighbor':False,
'conditional_paper_result':{'artifact':'P3_ADDENDUM.md','assumptions':'inherited fixed source/girth16/cached source distances; g outside oldJ X-R10, including g1058; move p0 or p1','conclusion':'new x to withdrawn p has distance at least11','not_general_threecut_NO':True},
'negative_Lean_requirement':{'required':False,'run':False,'new_Lean_graph_or_theorem_claim':False,'reason':'Completed finite counterexample gate plus conditional paper explanation; no successful new graph to formalize.'},
'initial_path_failure_preserved':True,'initial_path_failure_and_compile_CPU':2.282222419,'successful_native_actual_CPU':0.191383,'prior_local_terminal_CPU':2.674601871,'root_cached_metadata_query_charge':0.1,'final_case_CPU':2.774601871,'case_CPU_cap':20,'all_processes_terminal':True,'stopped_exact_scope':True,'same_Goal':'ACTIVE','old_N8_n61':'PAUSED'
},
'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date']
assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
(S/'SOURCE1250_FROZEN_THIRDCUT_TERMINAL_20261101_ROW.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
# Same existing API, only full-rebuild callbacks disabled for this one incremental write.
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'SOURCE1250_FROZEN_THIRDCUT_TERMINAL_20261101_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
 common['write_node'](row)
ledger['rows'].append(row);ledger['record_count']=len(ledger['rows']);ledger['updated_UTC']=now
ledger['input_counts'][str((S/'SOURCE1250_FROZEN_THIRDCUT_TERMINAL_20261101_ROW.json').relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} 1250→1252固定三cut修补域完整NO：修了saved缺点仍缺覆盖

以cached旧B object4536为唯一base，保x–1178，只移p0/1/869；实际1865第三边、11178合法参数配置全遍历，pilot9不重复。9例都修好saved1058并保住1178；P3移p0/p1六例withdrawn-pin距离均11。移p869三例withdrawn距离10，但首缺点依次1057/1056/1057距11；1057与869有旧二步路869–1234–1057，并非直接邻居。全域5454配置修好saved1058，仍11178全部NEW_X fail，bothpass0，旧根候选BFS0。存在bothnewroot-pass预测被推翻。

停止此冻结4536／保x1178 transfer域，其他base/三cut规则/一般3D10未排。P3为继承source/girth/distances的conditional paper，非新Lean定理；本负结果不新增或要求negative Lean。累计2.774601871/20CPU含路径错误/成功编译及root只读metadata.1。0新图／参数／Lean／独立方法；450条是实验记录。153图／43参数／Lean47、savedmain105/4/global0不变；sameGoal ACTIVE、旧N8/n61暂停。人工15格顶块原样保留。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name]; assert marker not in text
 cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  count=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert count
  old_exp=int(count.group(1));text=text[:count.start(1)]+str(old_exp+1)+text[count.end(1):]
 (W/name).write_text(text)
 assert (W/name).read_text()[:cut]==human[name]
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
append=f'''\n\n{marker}
## {now} 固定1250第三cut路线修补：完整11178域已停止

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (3,10)；L1250；候选1252未获合法D10 | 1865第三边／11178参数配置全部NEW_X fail，5454修saved1058但bothpass0；pilot9支持P1，p0/p1六例支持P3。p869首缺点1057/1056/1057，不是皆1057。 | 固定object4536／保x1178／三allowedpins域严格NO；其余三cut未排。修远点需同时补偿被撤走覆盖。 [实际终态](../{str((D/'NOTE.md').relative_to(ROOT))}) |

一个新实验记录，449→450，不是新方法或图。P3仅conditional paper；negative Lean不要求/未运行。总2.774601871/20CPU包含失败成本；旧single/twocut只继承，sourceD10 BFS0。153/43/47及savedmain105/4不变，Goal ACTIVE/旧N8n61暂停。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md+append)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==450
assert all(after[k]==v for k,v in counts.items())
assert all((ROOT/e).exists() for e in row['evidence_paths'])
assert (W/node).exists()
assert all((W/f).read_text().startswith(human[f]) for f in files)
receipt={'status':'PASS_ONE_FIXED_SOURCE1250_THIRDCUT_TERMINAL_NODE','updated_UTC':now,'records_before':before_count,'records_after':450,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str((S/'SOURCE1250_FROZEN_THIRDCUT_TERMINAL_20261101_ROW.json').relative_to(ROOT)),'index_experiment_count_before':old_exp,'index_experiment_count_after':old_exp+1,'graph_parameter_Lean_method_increments':[0,0,0,0],'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples']},'domain_complete':11178,'saved_target_repaired':5454,'pilots':9,'P3_conditional_paper_and_actual6of6':True,'p869_firstbad_correction':[1057,1056,1057],'NOTE_corrected_without_new_BFS':True,'final_case_CPU_including_root_cached_metadata':2.774601871,'raw_local_RESULT_TERMINAL_CPU_history_preserved':2.674601871,'conditional_paper_separate_from_new_Lean':True,'negative_Lean_required':False,'negative_Lean_run':False,'all_numeric_processes_terminal':True,'scope_stopped':'fixed object4536/protected x1178 three allowed pin transfer only','other_bases_threecut_general3D10_unexcluded':True,'human_top_blocks_preserved_exact':{f:True for f in files},'full_rebuild_reimport':False,'new_math_BFS_solver_field_Lean_ARIS_hash_runs':0,'root_STATE_ROUND_recovery_progress_builder_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-started,'root_disposition_file_present_when_written':(D/'ROOT_DISPOSITION.json').exists(),'stop':True}
(S/'SOURCE1250_FROZEN_THIRDCUT_TERMINAL_20261101_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
