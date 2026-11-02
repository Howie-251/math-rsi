"""Existing N2/N3 mechanism node only; bounded targeted-repair terminal."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='N2_TARGETED_REPAIR_TERMINAL_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rid='ddp-stale-d4d3-messieres-n2n3-two-cut4star-source-comparison-20261101'
def read(p):return json.loads((R/p).read_text())
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
assert before==441 and rid in records
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
P=S+'stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/'
r,t,root=read(P+'RESULT.json'),read(P+'TERMINAL.json'),read(P+'ROOT_DISPOSITION.json')
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_SIX_N2_BASES_TARGETED_THREECUT_REPAIR42'
assert t['terminal'] and t['active_processes']==0 and r['six_base_domain_completed']
assert r['counts']['configurations_visited']==3048 and r['counts']['saved_pair_R3_passed']==426
assert r['counts']['newroot_R3_failed_after_saved_pair_repaired']==426
assert r['counts']['newroot_R3_passed_after_saved_pair_repaired']==r['counts']['final_oldlabel_BFS_roots']==0
assert not r['positive_prediction_supported'] and not r['cross_base_literal_deduplication']
raw=copy.deepcopy(records[rid]['source_record']);m=raw['other_metrics']
m['historical_changed_rule_pending_checkpoint']=copy.deepcopy(m['separate_changed_generation_scope'])
changed=dict(status=root['status'],terminal_result_received=True,root_reported_in_progress=False,
    source='N2only,sixsavednewrootPASS_oldoldFAILbasecases',
    base_configurations=[x['base_configuration']for x in r['per_base_counts']],
    rule='p in originalfourpins,thirdorientedsourceedge(a,b)outsidepins,p-aoriginalnonedge;deletea-b andstar-p,addp-a andstar-b',
    meaning='threeoriginalcutsplusoldoldrepair,maintains4regularity;differentfromoldtwo-cut4starfamily',
    parameter_configurations=3048,parameters_per_base=[x['variants']for x in r['per_base_counts']],
    cross_base_literal_deduplication=False,independent_or_nonisomorphic_graph_count_claimed=False,
    saved_pair_failed=2622,saved_pair_repaired=426,newroot_R3_fail_after_pair_repaired=426,
    joint_pair_repair_newroot_pass=0,final_oldlabel_BFS_roots=0,targeted_pair_BFS=3048,newroot_BFS=426,
    prediction='AtleastonevariantrepairssavedpairandpreservesnewrootR3',prediction_supported=False,
    first_concrete_tradeoff=root['first_concrete_tradeoff'],wholecase_CPU_seconds=root['wholecase_CPU_seconds'],
    CPU_budget_seconds=5,source_JSON_parses=1,source_D3_BFS_roots=0,old_two_cut_batch_repeated=False,
    scope=root['scope'],not_excluded=root['not_excluded'],all_processes_terminal=True,
    next='PAUSE_THIS_MINIMAL_STAR_AND_ONE_PORT_EXCHANGE_LINE_NO_N4_SECOND_REPAIR_OR_SEED')
m['separate_changed_generation_scope']=changed
m.update(targeted_repair_terminal=True,targeted_repair_joint_prediction_supported=False,
    targeted_repair_old_two_cut_batch_repeated=False,mechanism_line_paused=True,
    targeted_repair_parameter_configurations_not_independent_graphs=3048,
    new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0)
raw.update(title='4D3 N2/N3两cut对照＋N2定向三cut修补全终态：6150旧规则NO，3048修补参数无联合覆盖',
    outcome_class='ROOT_ACCEPTED_N2N3_TWO_CUT_AND_SIX_N2_TARGETED_THREECUT_REPAIR_FINITE_NO_LINE_PAUSED',
    scope='ScopeA:cachedliteralN2/N3,eachall3075unorderedpairsofdisjointoldedges,delete2edges/addone4star,completeNO. ScopeB:onlysixsavedN2newrootPASS_oldoldFAILbases;choosep in original4pins andorientedthirdoriginaledge(a,b)outsidepins withp-aoldnonedge,deletea-b andstar-p,addp-a andstar-b. All3048parameterconfigurations completed,withoutcross-base literaldeduplication;not3048independentgraphs. ScopeBcompleteNOonlyforthisboundedrule,notall3cutrepairs,otherbases/sources/repairpatterns/general4D3.',
    distance_text='旧A域N2/N3各3075全访：N2六次newrootR3pass全部oldoldfail、14candidate旧根，N3无pass；旧pair0→1 ONE_PIN由3变4，1.503331119/5CPU。新B域基于六个真实pass基例逐做一port交换/第三cut+oldoldrepair：3048参数（跨基例未去重），2622未修savedpair；426确实修好pair，却426全部newrootR3失败，joint0/finaloldrootstage0。联合预测被完整有限域反驳，不是旧pair毫无改善。首基例303第三cut0–18、删star–1、加1–0与star–18：旧0→1从4变1，但41→1新最短41–2–15–34–1长4。新case.249139578/5CPU、sourceJSONparse1/sourceD3BFS0/旧A域不重跑。',
    lesson_and_restart_condition='Pause the N1/N2/N3 minimalstar and one-local-port-exchange line. The targetedrepair really fixes426savedpairs but always losesnewrootcoverage in this exact domain,so preserve/repair routes must be designed jointly. No N4,secondrepair,seed or source/cut ladder. Next choose anotherparameter fromthe15oldcells or propose explicit simultaneousmulti-routecompensation before a new bounded experiment. General3cut/otherrepairs remain unexcluded,not automatically authorized.',
    restart_condition='Anotherparameter or a genuinely new interface with explicit simultaneous oldpair and newroot route compensation;no continuation of the closed two-cut or specified six-base repair domains.',
    unclosed_gap='General3cutrepairrules,otherbases/sources/repairpatterns and generalN(4,3) remain open. Both recorded finitebatches are terminal and paused;no accepted42graph or further experiment authorized.')
extra=[P+x for x in ['PRED.md','NOTE.md','run_once.py','RESULT.json','TERMINAL.json','ROOT_DISPOSITION.json','SIX_SAVED_BASES.json','ALL_ACTUAL_VARIANTS.tsv']]
assert all((R/x).is_file()for x in extra)
raw['evidence_paths'].extend(x for x in extra if x not in raw['evidence_paths'])
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    txt=(W/fn).read_text();assert txt.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in txt
    prefix[fn]=txt[:txt.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date']
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):c['write_node'](n)
records[rid]=n;L.update(rows=list(records.values()),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
mp=W/'DDP_METHOD_LEDGER.md';lines=mp.read_text().splitlines();idx=[i for i,line in enumerate(lines)if line.startswith('| [')and'(experiments/'+rid+'.md)'in line];assert len(idx)==1;lines[idx[0]]=table
md='\n'.join(lines)+'\n';md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 原N2/N3节点补定向修补完整终态（无新增记录）\n\n旧two-cut6150NO与新six-base第三cut/oldoldrepair3048参数域分别保留。新426案修好savedpair却全失newrootR3，联合预测失败、0joint、0finaloldrootstage；跨基例未去重，不称3048独立图。仅该修补域NO，不排全部3cut/general4D3。暂停minimalstar/one-port交换线，不N4/secondrepair/seed；下一换15格参数或先给明确多路线联合补偿。441条/153/43/47不变。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' N2修补批已终态：426修旧pair却全部丢新根覆盖，联合预测被推翻\n\n新six-base N2第三cut/oldoldrepair共3048参数配置全完成（跨基例未去重，非3048独立图）：2622没修savedpair、426修好却426newrootR3全部失败，0joint/0finaloldrootstage。首base303删第三oldedge0–18及star–1，加1–0/star–18，0→1由4变1，但41→1最短41–2–15–34–1长4。真实修补与覆盖互相牵制，不是旧pair没有改善；.249139578/5CPU，0sourceD3/旧two-cut重跑。\n\n旧N2/N3two-cut6150NO仍是独立已闭范围；新仅指定六基例/一pin替换/一oldoldrepair域NO，不排一般3cut、其他base/source/repair/general4D3。此前“新batch待终态”仅历史，所有本线批次已停止；暂停N1/N2/N3 minimalstar/one-port交换，不N4/第二repair/seed，下一按15格换参数或先提出明确多路线补偿。441记录、153图／43参数／Lean47、savedmain105/4/global0不变，sameGoal ACTIVE、旧N8/n61暂停和人工15格顶部保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;txt=path.read_text();assert txt.startswith(pre);at=len(pre);txt=txt[:at]+'\n\n'+nav+txt[at:]
    if fn=='index.md':txt=re.sub(r'^- `exp:'+re.escape(rid)+r'`[^\n]*','- `exp:'+rid+'` — '+n['title']+' [no]',txt,flags=re.M)
    assert txt[:at]==pre;path.write_text(txt);preserved[fn]=True
helper.append_log(str(W),LABEL+': existingN2N3nodeupsert only,separate3048parameter targetedthirdcutrepairterminal(duplicatesacrosssixbasesnotremoved,notindependentgraphcount),426oldpairrepairsallnewrootfail,jointpredictionrefuted. Old6150twocutNOscopepreserved,nogeneral3cutNO. Pendingcheckpointhistorical,allbatchesstopped,linepaused,noN4/secondrepair. Counts441,153/43/47unchanged,human15oldcells top preserved,no numeric/review/reimport.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before and {k:after[k]for k in keys}==counts
receipt=dict(status='PASS_EXISTING_N2N3_NODE_TARGETED_REPAIR_TERMINAL_DELTA',updated_UTC=NOW,
    records_before=before,records_after=before,records_added=0,updated_experiment_id=rid,
    graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
    old_two_cut_scope_preserved=True,targeted_repair_domain_parameters=3048,
    cross_base_literal_deduplication=False,independent_graph_count_claimed=False,
    saved_pair_repaired=426,newroot_failed_after_pair_repair=426,joint_pair_newroot_pass=0,
    final_oldroot_BFS=0,positive_joint_prediction_supported=False,
    not_a_general_threecut_or_general4D3_exclusion=True,pending_checkpoint_is_historical=True,
    all_recorded_batches_terminal=True,line_paused_no_N4_secondrepair_seed=True,
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    numeric_source_graph_BFS_Lean_solver_paidreview_hash_runs=0,
    root_STATE_HTML_REPORT_recovery_builder_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,
    CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
