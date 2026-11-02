"""Existing585-node terminal upsert; root alone builds the15-row outputs."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='SOURCE585_K1_WHOLE_FIXED_P0_TERMINAL_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=S+'stale_record_transfer_d9D3/actual585_modified_edge_interface/'
rid='ddp-stale-d9d3-585-fixedp0-owner-avoiding-fourcorecuts-port16-no-20261101'
def read(p):return json.loads((R/p).read_text())
root=read(P+'ROOT_DISPOSITION.json');roottext=json.dumps(root)
assert '2.736357397'in roottext and '3200'in roottext
k1=read(P+'K1_RESULT.json');term=read(P+'K1_TERMINAL.json')
assert k1['status']=='COMPLETE_NO_FIXED_P0_K1_PROTOTYPE_BY_NEWROOT_OBLIGATION'
assert k1['owner_edge_domain']==k1['completed_owner_domains']==64 and k1['far_edge_domain']==1568
assert k1['full_k1_domain_exhausted'] and k1['DFS_nodes']==3200
assert k1['necessary_port_packings']==k1['core_failed_packings']==0
assert not k1['CPU_cap_stop'] and not k1['all_newroot_cover_pass']
assert k1['source_literal_parse_count']==k1['new_question_core_R2_support_builds']==0
assert term['terminal'] and term['active_processes']==0
assert abs(k1['wholecase_CPU_seconds']-2.736357397)<1e-10
assert (R/P/'K1_NOTE.md').is_file() and (R/P/'K1_SCOPE_ATTACK.md').is_file()
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={r['id']:r for r in L['rows']}
assert len(records)==before and rid in records
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances',
 'saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs',
 'pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs',
 'known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
generated=['research/stale_record_candidates.csv','research/stale_record_candidates.html','research/stale_record_candidates.html.txt',
 S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json']
generated_mtime={p:(R/p).stat().st_mtime_ns for p in generated}
portfiles=['PORT16_RESULT.json','PORT16_TERMINAL.json']
port_mtime={p:(R/P/p).stat().st_mtime_ns for p in portfiles}
raw=copy.deepcopy(records[rid]['source_record']);m=raw['other_metrics']
m['before_K1_terminal_checkpoint']=dict(title=raw['title'],status=raw['outcome_class'],scope=raw['scope'],
 distance_text=raw['distance_text'],k1_status=m['p0_owner_cut_scope'],next_interface=m['next_paper_interface'])
m['owner_p0_paper_followup']['as_of_paper_checkpoint_only']=True
m['owner_p0_paper_followup']['k1_unmeasured_status_superseded_by']='K1_RESULT.json complete portpacking NO'
m['K1_actual_terminal']=dict(status=k1['status'],owner_edge_domain=64,far_edge_domain=1568,
 completed_owner_domains=64,DFS_nodes=3200,full_k1_domain_exhausted=True,necessary_port_packings=0,
 P1_positive_portpacking_prediction='REFUTED_BY_COMPLETE_FINITE_GATE',P2_core_coverage_prediction='NOT_ENTERED_NOT_TESTED',
 core_failed_packings=0,all_newroot_cover_pass=False,CPU_cap_stop=False,first_unfinished_prefix=None,
 actual_source_parses=0,new_core_R2_support_builds=0,new_BFS_matching_graph_field_solver_Lean_review_runs=0,
 all_owner_masks_65bit_bound=True,one_omitted_point_branch_complete=True,
 old_sigma_far_edges_retained=True,no_failed_state_memo=True,scope_attack=P+'K1_SCOPE_ATTACK.md',
 prior_case_CPU_seconds=1.881081201,new_preparation_CPU_seconds=.2,independent_reader_CPU_seconds=.3,
 actual_process_CPU_seconds=.355276196,wholecase_CPU_seconds=2.736357397,wholecase_CPU_cap_seconds=20,
 terminal=True)
m.update(p0_owner_cut_scope='k=1 COMPLETE_NUMERIC_PORTPACKING_NO; k>=2 COMPLETE_PAPER_NO',
 next_paper_interface='STOPwholefixedp0fourmatching-corecut/starport/64Aperfectmatchingrule;next10D3actual650FPtransfer45CPUscopeauthorized_noactualhandleorresultreported',
 whole_fixed_p0_prototype_status='COMPLETE_NO_K0_NUMERIC_PLUS_K_GE2_PAPER_PLUS_K1_NUMERIC',
 wholecase_CPU_seconds=2.736357397,wholecase_CPU_cap_seconds=20,
 next_question='10D3actual650FP-transfer45CPUbatchauthorized;noactualHANDLEorresultreported',
 shortlist_cells_newly_tested=13,new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,
 new_independent_method_claims=0,all_processes_terminal=True)
raw.update(record_type='fixed_host_complete_four_matching_corecut_starport_portmatching_experiment',title='9D3 actual585固定p0四matching-corecut／星／64A匹配规则完整NO：k0、k1数值＋k≥2纸面',
 outcome_class='COMPLETE_NO_FIXED_P0_ALL_FOUR_DISJOINT_CORECUT_STARPORT_MATCHING_RULE',
 scope='Fixedactual585/2600polaritysourcewith65degree8absoluteAand520degree9coreB;fixedp0=actualvertex0. DeleteANYfourvertex-disjointoldB-Bedges,addonezadjacenttoeightcutcoreendpointsandp0,addANYperfectmatchingonAminus{p0},andmakeNOotheredits. Hypothetical586/2637all9regular. Classificationk=numberofcutswithp0-ownerendpoint: k0closedbyoriginalPORT16numericNO,k>=2byderived-affine-planepaperNO,k1bycompleteK1portpackingNO. Nototherp0,nonmatchingcuts,additionaloldoldrepair,multiplehelpers,otherstarneighbourhoods,arbitrary585rewiringor general586/9D3.',
 actual_D_scope='No586candidategraphorordinaryBFS/diametermeasurement. The wholefixedp0prototypeisexcludedbynecessarynewroot-Aobligations;K1hadzeroportpackings,soP2/corestagewasNOT_ENTERED,notcorefailed.',
 distance_text='k0继承实际1568eligible/448degree7/3697DFS完整NO，不重跑。后续derived affine plane给k≥2的U≤63-k、自由mate外扩≤k，R3新根A≤63<65，paperNO。最后k1以65bit真实label域完整查64owner/1568far，MRV含唯一omit分支并保真实endpoint互斥、不做failed-state memo；64域全部完成、3200DFS、端口packing0，P1被推翻，P2/corestage未进入而非corefail。K1未再parse literal、构coreR2、BFS、匹配或586图。因k0/k1/k≥2穷尽四cut，合并严格关闭fixedp0=0整个四不交corecut＋八core/p0星＋其余64A任意perfectmatching规则。累计2.736357397/20CPU=旧1.881081201+prep.2+reader.3+actual.355276196。',
 lesson_and_restart_condition='STOPtheentirefixedactualp0=0fourvertex-disjointcorecut/8core+p0star/arbitrary64Aperfectmatchingprototype. Releasingoneownerpairfromforcedmatchingwasagenuinenewroutepossibility,butitscompleteone-holeportpartitiondomainhasnohit;do notattributeit tocore/oldolddamage. k0numerical,k>=2paperandk1numericalclosuresarecomplementaryandallhistoricalrecordsremain. No p1/sigma/seed,morecuts,coreR2,remainingmatchingor586productionautomatically. Next10D3actual650FP-transfer45CPUbatchisauthorized,butnoactualHANDLEorresultisreportedhere;donotclaimrunningorPASS.',
 restart_condition='Anewconcreteboundedquestionoutsidefixedp0/fourmatching-corecut/thisstar-neighbourhood/64Amatchingrule. Otherp0aloneisnotpermissionforaparameterladder;next650batchisauthorizedwith45CPUandnofreshactualHANDLE/resultreportedinthisupdate.',
 unclosed_gap='Otherp0choices,nonmatchingcorecuts,additionaloldoldrepairs,multiplehelpers,othernewrootneighbourhoods,arbitrary585rewiringandgeneral586/9D3remainOPEN. Theacceptednegativeconcernsonlytheexplicitfixedp0prototype;nofull586graph,corefailuremeasurement,Leanorpriorityclaim. Same446ledger/13testedcells/153graphs/43parameters/Lean47;GoalACTIVE.')
raw['positive_guarantees']=[s.replace('Foruntestedk1,','Forhypotheticalk1portpacking,')for s in raw['positive_guarantees']]
raw['positive_guarantees'].extend([
 'K1MRVbrancheseachcoveringfar edgeandtheuniqueomitchoice;all64ownerchoicesand1568far edgesareincluded,withactualcorelabeldisjointnessandnoinappropriateoldsigmaprune.',
 'K1portpackings0meanscoreR2/sourceparseP2neverentered. Thecodeexplicitlykeepsnewrootpassseparatefromfullmatching/oldoldD3,butthatbranchwasnotexecuted.',
 'Forfixedp0samefourdisjointcutsrule,k0,k1andk>=2exhaustthepossibleowner-cutcounts,so theiracceptednecessaryNOsclosethewholeprototype.'
])
names=['K1_PRED.md','K1_once.py','K1_DOMAIN.json','K1_OWNER_DOMAIN_STAGES.tsv','K1_ALL_PACKING_CORE_STAGES.tsv',
 'K1_RESULT.json','K1_TERMINAL.json','K1_HANDLE.json','K1_NOTE.md','K1_SCOPE_ATTACK.md','K1_MATCHING_INTERFACE_PAPER.md']
newpaths=[P+x for x in names];assert all((R/p).is_file()for p in newpaths)
raw['evidence_paths'].extend(p for p in newpaths if p not in raw['evidence_paths'])
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in text
 prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
edges_mtime=(W/'graph/edges.jsonl').stat().st_mtime_ns
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date'];assert n['id']==rid
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):c['write_node'](n)
records[rid]=n;L.update(rows=list(records.values()),updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[K1终态](../'+P+'K1_NOTE.md) |'
mp=W/'DDP_METHOD_LEDGER.md';lines=mp.read_text().splitlines()
ix=[i for i,line in enumerate(lines)if line.startswith('| [')and'(experiments/'+rid+'.md)'in line];assert len(ix)==1
lines[ix[0]]=table;md='\n'.join(lines)+'\n'
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 同585节点闭合固定p0整个四matching-corecut原型\n\n不加node/方法/图。k1实际64owner/1568far、3200DFS完整、0端口packing，P1 refuted；P2/corestage NOT_ENTERED，0新literalparse/coreR2/BFS/匹配/586图。k0旧PORT16实际NO、k≥2derived-affine-paperNO与k1实际NO合并，严格关闭fixedactualp0=0四不交corecut＋八core/p0星＋其余64A任意匹配规则。累计2.736357397/20CPU，reader.3只计一次。其它p0、非matchingcuts、额外oldold、多helper、其它星形和一般9D3未排。不换p1/sigma/seed/续timer；下一10D3 actual650 FP-transfer固定45CPU批次已授权，尚无reported实际HANDLE/结果，不冒running或PASS。446与13格、153/43/47/savedmain105/4/global0不变。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 585固定p0四cut完整闭合：k1实际无端口packing，非corefail\n\n最后k1接口实际完整检验64owner/1568far，65位label与唯一漏点分支齐，3200DFS、全部64域完成、端口packing0、无预算截断。P1存在预测被推翻；P2/corestage NOT_ENTERED，不称corefail。新literalparse/coreR2/BFS/匹配/586图均0；case累计2.736357397/20CPU含旧1.881081201、prep.2、scope-reader.3与actual.355276196。\n\nk0原数值NO、k≥2derived-affine-paperNO及k1新数值NO穷尽k，关闭fixedp0=actual0整个四顶点不交corecut／八core+p0星／其他64A任意perfectmatching规则。旧PORT16/paper/读scope回执保留、不重跑。其它p0、非matchingcuts、额外旧旧补边、多helper、其他星邻域/一般586或9D3未排。停止此机制，不换p1/sigma/seed或自动586生产。\n\n下一10D3 actual650 FP-transfer固定45CPU批次已授权，尚无reported实际HANDLE/结果，不写running/PASS，也不计第14格。原585node原位更新，'+str(before)+'记录与13格新实测／老15格0新达标图、153图／43参数／Lean47、savedmain105/4/global0保持。人工15格顶部、sameGoal ACTIVE与旧N8/n61暂停保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':text=re.sub(r'^- `exp:'+re.escape(rid)+r'`[^\n]*','- `exp:'+rid+'` — '+n['title']+' [no]',text,flags=re.M)
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': existing585nodewholefixedactualp0prototypeNO,k0numeric+k>=2paper+k1numeric. K1all64owner/1568far3200DFScomplete0portpackings;P1refuted,P2/coreNOT_ENTERED,notcorefail,0sourceparse/coreR2/BFS/matching/graph. Case2.736357397/20CPUincludesreader.3once. Otherp0/nonmatchingcuts/additionaloldold/multiplehelpers/general9D3OPEN,next10D3actual650FPtransfer45CPUauthorizedbutnoactualHANDLE/resultreported. No node/graph/parameter/Lean/method increment,446/13cells/153/43/47unchanged,human15top exact. Buildereditednotbuilt,rootownsone15rowbuild.')

progress=R/'research/progress.html';page=progress.read_text();assert page==(R/'research/progress.html.txt').read_text()
old_section=re.search(r'<section id="stale-route-current">.*?</section>',page,re.S);assert old_section
history=old_section.group().replace('id="stale-route-current"','id="585-before-k1-terminal"',1)
history='<details id="585-before-k1-terminal-history"><summary>前一轮快照：k≥2纸面NO与当时尚未测试的k=1接口（保留历史）</summary>\n'+history+'\n</details>'
current='''<section id="stale-route-current">
<h2>当前结果：585固定p0四cut原型完整闭合，没有586图</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中13格有本轮新检验，老题仍0张新增达标图。</strong><p><a href="stale_record_candidates.html">15项问题、Moore差与实际方法范围</a> · <a href="stale_record_candidates.html.txt">HTML源码</a> · <a href="stale_record_candidates.csv">15行CSV</a>。k1仍是同一(9,3)机制，不新增节点或第14格。</p></div>
<p>固定实际p0=0的规则为：删四条顶点不交core边，新点z连八core端点与p0，其余64个绝对点A可任意perfectmatching，不作其它改动。令k为含p0-owner的cut数。最后未决的k=1现已实际完整测试，因而可与此前两范围合并：</p>
<table><thead><tr><th>子范围</th><th>证据</th><th>终态</th></tr></thead><tbody><tr><td>k=0</td><td>1568eligible边、3697DFS；四16-mask不能分割64A</td><td>旧数值NO，未重跑</td></tr><tr><td>k≥2</td><td>derived affine plane：U≤63−k、自由mate≤k，新根A覆盖≤63&lt;65</td><td>纸面NO</td></tr><tr><td>k=1</td><td>全64owner／1568far，3200DFS，0端口packing</td><td>新数值NO</td></tr></tbody></table>
<p><strong>k1的实际反馈：</strong>65位mask包含p0真实位，MRV允许唯一漏点，全部64个owner域结束且无预算截断；保留旧sigma far边参与混合，不使用可能合并不同core pins的失败memo。存在端口packing的P1被推翻。P2的core覆盖阶段完全未进入，不能说成corefail；因此没有再读取literal、生成core-R2支持或执行BFS、匹配、586图。</p>
<p>累计2.736CPU／20，包含旧1.881、准备0.20、独立scope-reader0.30及新进程0.355。结论严格关闭<strong>fixed p0=0、四matching-corecut、八core+p0星、其他64A任意匹配</strong>这一整个规则；不是一般585重连或586／(9,3)无解。其它p0、非matching cuts、额外旧旧补边、多helper或其它新根邻域均未排，不自动换p1、sigma、seed或续算。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/K1_NOTE.md">k1预测、完整域、实际反馈与成本</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/K1_SCOPE_ATTACK.md">独立只读范围攻击</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/OWNER_P0_NEXT_INTERFACE.md">此前k≥2证明与k1必要接口历史</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/ROOT_DISPOSITION.json">ROOT完整scope处置</a>。</p>
<p><strong>下一转(10,3) actual650的FP-transfer。</strong>已授权固定45CPU的一次模型／冻结oneprototype与15配对检验；尚无reported实际运行句柄或结果，不标running、PASS或第14格。另一路只读已接受16D4的false-twin中心packing接口，没有新数值。CM253及global256旧范围分别保留。唯一Wiki仍LEDGERCOUNT条研究记录，Goal继续ACTIVE、旧N8/n61暂停；人工意见历史、153／43／Lean47、全球优先权确认0与16416完整专家交付均未改变。</p>
</section>'''.replace('LEDGERCOUNT',str(before))
page=page[:old_section.start()]+current+'\n'+history+page[old_section.end():]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page=re.sub(r'<p>更新 [^<]*</p>','<p>更新 '+stamp+'。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>',page,count=1)
progress.write_text(page);(R/'research/progress.html.txt').write_text(page)
assert {p:(R/p).stat().st_mtime_ns for p in generated}==generated_mtime
assert {p:(R/P/p).stat().st_mtime_ns for p in portfiles}==port_mtime
after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before and len(after['rows'])==before and {k:after[k]for k in keys}==counts
modified=['research-wiki/DDP_METHOD_LEDGER.json','research-wiki/DDP_METHOD_LEDGER.md',n['wiki_path'],
 'research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md','research-wiki/log.md',
 S+'build_stale_record_page.py','research/progress.html','research/progress.html.txt',
 str(rawpath.relative_to(R)),str((OUT/f'{LABEL}_NODE_CALLS.log').relative_to(R)),
 str((OUT/f'{LABEL}_RECEIPT.json').relative_to(R)),str(Path(__file__).relative_to(R))]
if (W/'graph/edges.jsonl').stat().st_mtime_ns!=edges_mtime:modified.append('research-wiki/graph/edges.jsonl')
receipt=dict(status='PASS_EXISTING_585_NODE_K1_COMPLETE_NO_CLOSES_WHOLE_FIXED_P0_PROTOTYPE',updated_UTC=NOW,
 records_before=before,records_after=before,records_added=0,updated_experiment_id=rid,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 k0='OLD_PORT16_NUMERIC_NO_NOT_RERUN',k_ge2='DERIVED_AFFINE_PAPER_NO',k1='COMPLETE_NUMERIC_PORTPACKING_NO',
 K1_owner_domains_complete=64,K1_far_domain=1568,K1_DFS_nodes=3200,K1_portpackings=0,
 P1_positive_portpacking_prediction='REFUTED',P2_core_prediction='NOT_ENTERED_NOT_TESTED',core_failed_packings=0,
 K1_source_parses=0,K1_core_R2_support_builds=0,
 whole_fixed_p0_rule='FOUR_VERTEX_DISJOINT_CORECUTS_8CORE_PLUS_P0_STAR_ANY_OTHER64A_PERFECTMATCHING_COMPLETE_NO',
 outside_scope='otherp0/nonmatchingcuts/extraoldold/multiplehelpers/otherpins/general586or9D3OPEN',
 wholecase_CPU_seconds=2.736357397,wholecase_CPU_cap_seconds=20,scope_reader_charge_once=.3,
 human_top_blocks_preserved_exact=preserved,prior_progress_snapshots_preserved=True,
 shortlist_newly_tested_cells=13,shortlist_new_legal_graphs=0,original_PORT16_files_unchanged=True,
 builder_edited_only_NOT_BUILT=True,existing_candidates_HTML_CSV_JSON_not_modified_by_this_sync=True,
 root_to_do_one_existing_15row_build=True,progress_html_and_source_identical=True,
 next10D3_actual650='FIXED45CPU_BATCH_AUTHORIZED_NO_ACTUAL_HANDLE_OR_RESULT_REPORTED',
 full_index_query_rebuild_or_reimport=False,new_numeric_BFS_field_solver_Lean_review_hash_runs=0,
 root_STATE_ROUND_recovery_REPORT_modified=False,sameGoal='ACTIVE',old_N8_n61='PAUSED',
 modified_paths=modified,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
