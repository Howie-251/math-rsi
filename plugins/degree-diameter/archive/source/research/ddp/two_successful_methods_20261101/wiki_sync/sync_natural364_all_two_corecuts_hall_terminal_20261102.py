"""Upgrade one existing natural364 node: complete Hall architecture NO, add0."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib, copy, json, re, runpy, time

ROOT=Path(__file__).resolve().parents[4]
W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365'
G=D/'all_two_corecut_Hall_gate';F=D/'joint_fixed_first_P'
started=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d4d5-natural364-port-matching-two-core-cuts-star365-sample-20261101'
marker='<!-- NATURAL364_ALL_TWO_CORECUTS_HALL_TERMINAL_20261102 -->'
ledger_path=W/'DDP_METHOD_LEDGER.json'
ledger=json.loads(ledger_path.read_text())
assert ledger['record_count']==len(ledger['rows'])==455
positions=[i for i,row in enumerate(ledger['rows']) if row['id']==slug]
assert len(positions)==1
pos=positions[0];before=copy.deepcopy(ledger);old=copy.deepcopy(ledger['rows'][pos])
raw=copy.deepcopy(old['source_record']);historical=copy.deepcopy(raw)
assert raw['outcome_class']=='UNKNOWN_10000_SAMPLE_NO_HIT'
assert raw['other_metrics']['cumulative_charged_CPU_seconds']==1.537876879
assert raw['other_metrics']['distinct_configurations_finished']==10000
assert raw['other_metrics']['newroot_R5_passed']==0
assert 'all_two_corecuts_Hall_terminal_20261102' not in raw['other_metrics']
fixed=json.loads((F/'RESULT.json').read_text())
allowed=json.loads((F/'ALLOWED_MATCHING_MODEL.json').read_text())
result=json.loads((G/'RESULT.json').read_text())
disposition=json.loads((G/'ROOT_DISPOSITION.json').read_text())
assert fixed['status']=='COMPLETE_NO_FIXED_P_ALL_MATCHINGS_BY_HALL'
assert [fixed[k] for k in ['hard_owner_count','near_port_count','hard_neighbor_union_count']]==[24,1,1]
assert allowed['near_ports_dP_atmost1']==[126]
assert result['status']=='COMPLETE_NO_ALL_TWO_CORECUTS_ALL_PORTMATCHINGS_BY_HALL'
assert result['completed'] and result['actual_pairs_checked']==result['expected_pair_count']==196371
assert result['shared_pairs_excluded']==1764 and result['Hall_survivor_count']==0
assert result['minimum_Hall_deficit']==20
assert result['new_depth4_support_queries']==332 and result['reused_support_queries']==4
assert disposition['case_CPU']==3.913081991 and disposition['case_cap']==20
assert disposition['historical_sample_UNKNOWN_preserved']

common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md']
original={name:(W/name).read_text() for name in files}
human_end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
assert all(human_end in original[name] and marker not in original[name] for name in files)
human={name:text[:text.index(human_end)+len(human_end)] for name,text in original.items()}
old_index_count=re.search(r'^## Experiments \((\d+)\)',original['index.md'],re.M).group(1)
ledger_md_before=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in ledger_md_before

raw['title']='4D5 natural364→365：196371两corecut域Hall完整NO；原10000样本UNKNOWN保历史'
raw['record_type']='complete_fixed_source_necessary_Hall_exclusion'
raw['outcome_class']='COMPLETE_NO_ALL_TWO_CORECUTS_ALL_PORTMATCHINGS_BY_HALL'
raw['wiki_verdict']='no'
raw['actual_D_scope']='No graph produced; full196371cutpair necessary newroot Hall gate completes the exact architecture; no candidate oldroot or fullgraph diameter measurement.'
raw['scope']='Fixed naturalH3 polarity364/714 source only (28degree3ports/336degree4core), not publicregular364/728. Delete any two vertex-disjoint ORIGINAL core-core edges, connect their four endpoints to one new4star, add an arbitrary perfectmatching of all28oldports, and make no other edits. All196371 unordered eligible corecutpairs have hardbeta2owners>nearports; every matching is therefore excluded before candidate production. The original10000sample UNKNOWN remains historical, not retroactively exhaustive.'
raw['distance_text']='当前严格终态：原630core边的198135无序边对剔除1764共端点对，196371全部完成；每P的β2-hole owners为21..27、nearports为0..2，最小实际h−n=20，0Hall幸存。hard owner的mate必须注入near(P)，容量不够已拒全部matching，无需matching solver/365图/oldold检验。fixed首P先因24>1反驳jointM存在预测（near仅126）；随后完整域预测得到支持。新R4支持4缓存复用+332深4查询，不重sourceD5/旧28球。历史原10000案仍是样本UNKNOWN，全部新根失败、oldold0、费用1.537876879/20；首saved路径364–43–54–56–360–345–0长6保留。'
raw['unclosed_gap']='This exact fixedsource/two-disjoint-corecuts/28portperfectmatching/one4star architecture is now closed by the complete Hall gate. No claim about general365 graphs, publicregular364/728, thirdcut, extraoldoldrepair, differentstarneighbors or multiplehelpers. No actual candidate or diameter/badpair total is fabricated. The three nestedHall paper conditions are derived local newroot interfaces only, with no new numerical results or independent method/record count.'
raw['lesson_and_restart_condition']='The original independent shuffle sample failed but left the architecture UNKNOWN. Exact owner/tail geometry changed generation to coupled portmates, fixedP Hall24>1 refuted the first joint prediction, then a complete finite all-cutpair Hall gate supplied a strict architecture NO. Stop this exact rule without more seeds, matching enumeration, thirdcut or source replacement; a materially different separately authorized question must respect this closed scope. Three nestedHall inequalities are existing paper interfaces, not extra experiments or records.'
raw['restart_condition']='STOP exact architecture. No more samples, no all-portmatching solver, no fresh positive suite, no automatic thirdcut or otherhost. Only a separately authorized materially changed rule outside the stated closure can restart.'
raw['positive_guarantees']=[
'All cutendpoints lie inP, so a minimum sourceP-to-target path can restart at the downstreamP endpoint of any usedcut; hence dT(P,t)=dG(P,t).',
'Originalports have distance5 and their R2classes partition364. A simple z-root<=5path uses at most one newportmatching edge; a hole tail oflength<=2 cannot touchP and thus avoids the cuts.',
'Holeownerb requires dG(P,mate(b))+beta<=3. Allowed undirected edges need both directed thresholds; for beta2holes the mate is necessarily in near(P).',
'Each coreedge contributes at most one distinctnearport, otherwise two originalports would have distance<=3. Two cuts give near(P)<=2; the observed hard21..27 lower range comes from the complete finite source data, not a new abstract geometry theorem.',
'All196371 unordered disjoint originalcoreedge pairs were visited, using4saved plus332newcoreR4supports. Everypair violates the first Hall necessary inequality; no matching solver/graph/oldroot check is needed to reject it.',
'Historical10000sampleUNKNOWN, firstfailure and original1.537876879CPU remain fully preserved in historical_sample_record_before_full_Hall_20261102.',
'Three nestedHall local-paper inequalities can characterize the structured newroot matching interface; this complete numerical gate needed only the first. They do not certify oldoldD5 or create any new graph/method/record.'
]
metrics=raw['other_metrics']
metrics['historical_sample_record_before_full_Hall_20261102']=historical
metrics['historical_sample_status']='UNKNOWN_10000_SAMPLE_NO_HIT'
metrics['historical_sample_CPU_seconds']=1.537876879
metrics['historical_sample_cap_seconds']=20
metrics['complete_rule_exclusion']=True
metrics['cumulative_charged_CPU_seconds']=3.913081991
metrics['all_two_corecuts_Hall_terminal_20261102']={
 'status':result['status'],'root_status':disposition['status'],
 'fixedP_prediction':'anotherjointportmatchingcoversnewrootR5','fixedP_prediction_verdict':'REFUTED_COMPLETE_FIXED_P',
 'fixedP_holes':72,'fixedP_hard_beta2_owners':24,'fixedP_near_ports':[126],'fixedP_allowed_neighbor_union':[126],'fixedP_Hall_deficit':23,
 'full_domain_prediction':'everytwo-disjointoriginalcorecut P has hardbeta2owners>nearports','full_domain_prediction_verdict':'SUPPORTED_COMPLETE_DOMAIN',
 'original_core_edges':630,'all_unordered_edgepairs':198135,'shared_endpoint_pairs_excluded':1764,'eligible_pairs':196371,'pairs_checked':196371,'completed':True,
 'hard_range':[21,27],'near_range':[0,2],'minimum_Hall_deficit':20,'Hall_survivors':0,
 'new_depth4_core_supports':332,'previous_fixedP_core_supports_reused':4,'total_current_core_R4_supports':336,
 'source_D5_validation':0,'old28portballs_rerun':0,'matching_solver':0,'newcandidate_graph':0,'candidate_oldroot_BFS':0,'Lean':0,'ARIS':0,
 'numeric_native_CPU':result['actual_native_CPU'],'final_wholecase_CPU':3.913081991,'wholecase_cap':20,'timer_reset':False,
 'old_sample_metrics_preserved_as_history':True,'old_sample_was_not_exhaustive':True,
 'nested_Hall_paper_conditions_count':3,'nested_Hall_numeric_rows_tested':'only first necessary inequality used; no numerical second/third Hall experiment',
 'nested_Hall_paper':'JOINT_PORT_HALL_PAPER.md','nested_Hall_condition1':'|D_tau1|<=|F intersect N1|=|N1|',
 'nested_Hall_condition2':'|D_tau<=2|<=|F intersect N2|=|N2|','nested_Hall_condition3':'|D|<=|F intersect N3|; do not replace RHS by allN3 for sufficiency',
 'new_graph_parameter_Lean_method':[0,0,0,0],'terminal':True,'no_automatic_restart':True}

names=['JOINT_PORT_SCOPE_ATTACK.md','JOINT_PORT_HALL_PAPER.md',
 'joint_fixed_first_P/PRED.md','joint_fixed_first_P/run_once.py','joint_fixed_first_P/RESULT.json','joint_fixed_first_P/TERMINAL.json',
 'joint_fixed_first_P/ALLOWED_MATCHING_MODEL.json','joint_fixed_first_P/FOUR_CORE_R4_SUPPORTS.json','joint_fixed_first_P/HALL_CERTIFICATE.json',
 'all_two_corecut_Hall_gate/PRED.md','all_two_corecut_Hall_gate/run_once.py','all_two_corecut_Hall_gate/RESULT.json','all_two_corecut_Hall_gate/TERMINAL.json',
 'all_two_corecut_Hall_gate/SOURCE_SUPPORT_BINDING.json','all_two_corecut_Hall_gate/ALL_CUTPAIR_HALL_COUNTS.tsv',
 'all_two_corecut_Hall_gate/FINAL_PROOF.md','all_two_corecut_Hall_gate/ROOT_DISPOSITION.json']
newpaths=[str((D/name).relative_to(ROOT)) for name in names]
raw['evidence_paths']=list(dict.fromkeys(raw['evidence_paths']+newpaths))
assert all((ROOT/path).exists() for path in raw['evidence_paths'])
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date']
assert row['id']==slug and row['status']==result['status']
assert row['actual_order'] is None and row['actual_diameter'] is None
assert row['other_metrics']['historical_sample_record_before_full_Hall_20261102']==historical
assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'NATURAL364_ALL_TWO_CORECUTS_HALL_TERMINAL_20261102_ROW.json'
rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
nodepath=W/'experiments'/f'{slug}.md'
original_loader=helper._load_paper_frontmatter
# Existing helper otherwise preserves its old partial verdict; update only this node.
def target_meta(path):
 meta=original_loader(path)
 if Path(path).resolve()==nodepath.resolve():
  meta=dict(meta);meta['verdict']='no';meta['duration']='samecase3.913081991/20CPU; originalsample1.537876879 retained as history'
 return meta
helper._load_paper_frontmatter=target_meta
with (S/'NATURAL364_ALL_TWO_CORECUTS_HALL_TERMINAL_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):
 common['write_node'](row)
ledger['rows'][pos]=row;ledger['updated_UTC']=now
ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
node='experiments/'+slug+'.md'
proof=str((G/'FINAL_PROOF.md').relative_to(ROOT));paper=str((D/'JOINT_PORT_HALL_PAPER.md').relative_to(ROOT))
summary=f"""\n\n{marker}
### {now} natural364原节点终态升级：全部两corecut域Hall NO

原10000样本UNKNOWN及1.537876879/20CPU完整保为历史，不改写成当时已穷尽。后续固定首P联合matching预测被24hardowners对唯一nearport126反驳；随后完整196371个原core不交边对全部h>near，h21..27、near0..2、最小差20，0幸存。由mate注入必要条件，严格关闭固定自然364/714、任意两条不交原corecuts、28ports任意perfectmatching及四端点新星且无其它改动的架构。不是一般365图NO。

4个缓存R4＋332个新深4支持；sourceD5/旧28portballs/matching solver/365graph/oldroot BFS/Lean/ARIS均0，最终samecase3.913081991/20。三条nestedHall只链接已推导的局部newroot纸面接口；全域数值只需第一必要条件，0新增纪录或独立方法。当前全STOP，不加第三cut，不混入B只读题。

[原位canonical节点]({node})；[完整终态证明](../{proof})；[三条nestedHall纸面接口](../{paper})。455→455/add0，0图/参数/Lean/方法；人工顶块与其他454rows保持。

"""
for name in files:
 oldtext=original[name];cut=len(human[name]);newtext=oldtext[:cut]+summary+oldtext[cut:]
 (W/name).write_text(newtext)
 assert newtext.startswith(human[name]) and newtext.replace(summary,'',1)==oldtext
md_add=f"""\n\n{marker}
## {now} natural364原样本节点原位升级：完整两corecut域NO

[同一节点]({node})保原10000样本UNKNOWN/1.537876879CPU历史；固定P的jointM预测被24>1反驳，新全域预测由196371/196371支持：hard21..27、near0..2、min deficit20。只关natural364/714＋两原core不交cuts＋任意28portperfectmatching＋四端点新星，不排一般365、第三cut、repair、多helpers或publicregular364/728。

新支持4缓存+332深4；sourceD5/旧28球/matching/graph/oldroots/Lean/ARIS0，samecase3.913081991/20。三条nestedHall仅[局部paper接口](../{paper})，不是新数值/纪录/方法；[FINAL proof](../{proof})给当前严格范围。455→455/add0，0图/参数/Lean/方法，其他454rows/人工top保留，当前STOP。
"""
(W/'DDP_METHOD_LEDGER.md').write_text(ledger_md_before+md_add)
after=json.loads(ledger_path.read_text())
assert after['record_count']==len(after['rows'])==455
assert [r['id'] for r in after['rows']]==[r['id'] for r in before['rows']]
assert all(r==before['rows'][i] for i,r in enumerate(after['rows']) if i!=pos)
for key,value in before.items():
 if key not in {'updated_UTC','input_counts','rows'}:assert after[key]==value
for key,value in before['input_counts'].items():assert after['input_counts'][key]==value
updated=after['rows'][pos]
assert updated['source_record']['other_metrics']['historical_sample_record_before_full_Hall_20261102']==historical
assert updated['other_metrics']['cumulative_charged_CPU_seconds']==3.913081991
assert original_loader(nodepath)['verdict']=='no'
assert all((W/name).read_text().startswith(human[name]) for name in files)
new_index_count=re.search(r'^## Experiments \((\d+)\)',(W/'index.md').read_text(),re.M).group(1)
assert new_index_count==old_index_count
receipt={
 'status':'PASS_EXISTING_NATURAL364_NODE_UPSERT_COMPLETE_ALL_TWO_CORECUTS_HALL_NO',
 'updated_UTC':now,'records_before':455,'records_after':455,'records_added':0,'updated_id':slug,
 'canonical_node':str(nodepath.relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),
 'current_verdict':'no','current_scope':disposition['closed_scope'],'current_status':updated['status'],
 'old10000sample_UNKNOWN_preserved_complete':True,'old_sample_record_preserved_exact':True,
 'old_sample_CPU':1.537876879,'old_sample_cap':20,'final_samecase_CPU':3.913081991,'final_case_cap':20,
 'fixedP_prediction_refuted':{'hard':24,'near':1,'nearports':[126]},
 'full_domain_prediction_supported':{'eligible':196371,'visited':196371,'hard':[21,27],'near':[0,2],'minimum_deficit':20,'survivors':0},
 'R4_supports':{'cached':4,'new_depth4':332},
 'sourceD5_old28balls_matching_graph_oldroots_Lean_ARIS':[0,0,0,0,0,0,0],
 'nestedHall_conditions':3,'nestedHall_paper_only_no_new_records':True,
 'graph_parameter_Lean_method_increments':[0,0,0,0],
 'other454rows_preserved_field_for_field':True,'row_order_preserved':True,
 'human_top_blocks_preserved_exact':{name:True for name in files},'index_experiments_before':int(old_index_count),'index_experiments_after':int(new_index_count),
 'ledger_other_top_counts_preserved':True,'full_rebuild_reimport':False,'root_STATE_ROUND_pages_recovery_modified':False,'B_readgate_mixed_into_node':False,
 'modified_outputs':[str(nodepath.relative_to(ROOT))]+['research-wiki/'+n for n in ['DDP_METHOD_LEDGER.json','DDP_METHOD_LEDGER.md']+files]+[str(rowfile.relative_to(ROOT))],
 'sync_process_CPU_seconds':time.process_time()-started,'stop':True}
receipt_path=S/'NATURAL364_ALL_TWO_CORECUTS_HALL_TERMINAL_20261102_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
