"""Upsert only the existing585 node and progress; leave the15-row build to root."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='OWNER_P0_PAPER_INTERFACE_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=S+'stale_record_transfer_d9D3/actual585_modified_edge_interface/'
rid='ddp-stale-d9d3-585-fixedp0-owner-avoiding-fourcorecuts-port16-no-20261101'
def read(p):return json.loads((R/p).read_text())
root=read(P+'ROOT_DISPOSITION.json');paper=(R/P/'OWNER_P0_NEXT_INTERFACE.md').read_text()
assert root['paper_followup']['status']=='ROOT_READ_ACCEPTED_PAPER_NO_K_GE2_AND_K1_NECESSARY_INTERFACE'
assert root['paper_followup']['k1_status']=='NOT_NUMERICALLY_TESTED_NECESSARY_PORT_INTERFACE_ONLY'
assert len(paper)>2000
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
raw=copy.deepcopy(records[rid]['source_record']);m=raw['other_metrics']
m['pre_owner_p0_paper_checkpoint']=dict(title=raw['title'],status=raw['outcome_class'],
 original_numeric_scope=raw['scope'],p0_owner_cut_status=m['p0_owner_cut_scope'],
 next_paper_interface=m['next_paper_interface'],numeric_result_unchanged=True)
m['owner_p0_paper_followup']=dict(status=root['paper_followup']['status'],fixed_p0_actual_vertex=0,
 k='numberof4cutswithap0-ownerendpoint',derived_design='2-(64,8,1)affineplaneorder8',
 parallel_class='eightC(neighboursofp0)minus{p0},pairwisedisjointpartition64',
 two_p0_owner_cut_masks_intersect_at_least=3,k_ge2_U_upper='63-k',
 k_ge2_new_matching_targets_outside_U_upper='k',k_ge2_newroot_A_target_upper=63,
 required_A_targets=65,k_ge2_scope='COMPLETE_PAPER_NO',
 k0_scope='INHERITED_PORT16_COMPLETE_NUMERIC_NO_NOT_RERUN',
 k1_scope='NOT_NUMERICALLY_TESTED_NECESSARY_INTERFACE_ONLY',
 k1_necessary='fouractual16maskspairwisedisjoint,union64containsp0;onlymissingA=tmatchedtothefreeowner a;other3cutownerpairsforced',
 k1_actual_vertex_disjointness_still_required=True,k1_matching_extension_remaining_A=56,
 matching_extension_not_full_graph_D3=True,newroot_core_or_oldold_D3_guarantee=False,
 new_numeric_BFS_field_matching_graph_Lean_solver_review_runs=0)
m['p0_owner_cut_scope']='k>=2 COMPLETE_PAPER_NO; k=1 NOT_NUMERICALLY_TESTED'
m['next_paper_interface']='k=1only:onep0-ownercut16maskandthreeactualnonownercut16masksdisjoint,saveuniqueomittedt/freeowner-mate,notnewnumeric'
m['paper_extension_not_separate_method_or_node']=True
raw.update(title='9D3固定p0四corecut：k=0完整数值NO，k≥2纸面NO；仅k=1必要接口未测',
 outcome_class='FIXED_P0_K0_NUMERIC_NO_K_GE2_PAPER_NO_K1_NOT_TESTED',
 scope=raw['scope']+' Paperfollowupadditionallyclosesk>=2p0-ownercutsinthe SAMEfixedp0fourdisjointcorecut/8core+p0star/64Amatchingrule. k=1isexplicitlyunclosedandhasnoremainingnumericresult;notallfourcutNO.',
 distance_text=raw['distance_text']+' 后续纸面继承Steiner3-(65,9,1)，在p0导出2-(64,8,1) affine plane。两条p0-owner cuts的16mask相交至少3，k≥2时四mask并U≤63-k；至多k个自由mate能在U外补点，故新根A覆盖≤63<65，严格NO，无新计算。k=1仅剩必要接口：四16mask互不交/并64含p0，唯一漏A点t须配自由owner a，其余三cutownerpairs强制；剩56A可延拓匹配但不保证core或旧旧D3，数值未测。',
 lesson_and_restart_condition='Forfixedactualp0=0,k0owner-avoidingprototypeclosedbyoriginalfinitePORT16gate;paperthenclosesallk>=2p0-owner-cutcasesbyderived-affine-lineoverlapandfree-matecapacity. Onlyk=1remainsanuntestednecessaryportinterface. Itmustuseoneactualp0-ownercutandthreeactualnon-ownercutswithfourdisjoint16masks,union64includingp0,andfreeowneramatchedtotheuniquemissingt. Matchingextensionispossiblebutdoesnotcertifycoreoroldoldcoverage. Preserveoldnumericdataandcost,no p1/sigma/seed/packingrerun. No nextnumericbudgetorsearchiscreatedbythispaperupdate.',
 restart_condition='Onlyanexplicitlyselectedboundedquestionfortheuntestedk1interface,withactualcutlabels/missingt/forcedownerpairs;noautomaticnewnumeric,coreR2,BFS,matchingor586production.',
 unclosed_gap='Forfixedp0=0samefourcorecutstarportmatchingmechanism,k=1aloneisNOT_NUMERICALLY_TESTED;itsmaskinterfaceisnecessarynotfull586D3. Otherp0,otherrewirings/repair,multiplehelpers,general586/9D3remainunexcluded. k>=2isnowpaperNOandmustnotbereportedasstillwhollyOPEN. No graph/parameter/Lean/method/nodeincrement;GoalACTIVE.')
raw['positive_guarantees'].extend([
 'Steiner3-(65,9,1)derivedatp0gives2-(64,8,1)affineplane;theeightC(neighboursofp0)minuspointblocksformaparallelclass.',
 'Twoactualp0-owner-cut16masksintersectatleast3;for2<=k<=4,theirfullU<=63-kandatmostkfree-mateextrasgive<=63A,strictlybelow65.',
 'Foruntestedk1,fourdisjoint16masksautomaticallyexcludeownercollisions,uniquemissingtcanbematchedtothefreeownera,and56remainingAadmitamatchingextension;noneofthisestablishescore/oldoldD3.'
])
newpath=P+'OWNER_P0_NEXT_INTERFACE.md';assert newpath not in raw['evidence_paths'];raw['evidence_paths'].append(newpath)
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
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[paper证据](../'+newpath+') |'
mp=W/'DDP_METHOD_LEDGER.md';lines=mp.read_text().splitlines()
ix=[i for i,line in enumerate(lines)if line.startswith('| [')and'(experiments/'+rid+'.md)'in line];assert len(ix)==1
lines[ix[0]]=table;md='\n'.join(lines)+'\n'
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 原585节点纸面增量：k≥2排除，仅k=1接口未测\n\n不新增记录或方法。固定p0=actual0，在原四corecut／八core+p0星／其余64A匹配机制中，k表示p0-owner cuts数。k=0原PORT16数值NO完整继承；新derived affine plane令k≥2时U≤63-k、自由mate新增≤k，R3新根A≤63<65，故paperNO。k=1必须四16mask两两不交/并64含p0，唯一漏点t与自由owner匹配、另三ownerpairsforced；只是必要端口接口，matching可延拓不保证core或旧旧D3，尚无数值。旧PORT16_RESULT/CPU不改，446及153/43/47、13格0新达标图保持。不自动数值或586图。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 585同一节点的纸面收束：k0数值NO，k≥2纸面NO，仅k1未测\n\n固定p0=actual0，仍四条不交corecuts＋八core/p0星＋其余64A匹配，k为p0-owner cut数。继承Steiner3-(65,9,1)在p0导出2-(64,8,1) affine plane；八条L_u成parallelclass。两条p0-owner cuts的D-mask至少交3，k≥2时U≤63-k，至多k个free-mates外扩，故新根A覆盖≤63<65，完整paperNO。\n\nk0 PORT16原数值NO/1568eligible/3697DFS不重跑；仅k1未执行数值。必要形状为四actual16mask互不交、union64含p0，唯一漏A=t匹配freeowner a，其余三ownerpairsforced；剩56A可延拓matching，不保证新根core或oldoldD3。下一只能基于该k1接口另作明确选择，无新数值授权/候选/586图。其他p0/改边/一般9D3未排。\n\n原节点原位更新，不加row，'+str(before)+'记录及153图／43参数／Lean47、13格新实测／老15格0新达标图、savedmain105/4/global0不变。人工15格顶部、sameGoal ACTIVE、旧N8/n61暂停保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':text=re.sub(r'^- `exp:'+re.escape(rid)+r'`[^\n]*','- `exp:'+rid+'` — '+n['title']+' [no; k1 untested]',text,flags=re.M)
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': existing585nodepaperupsert,norow/method/graph. k0PORT16NOinheritedunchanged;derived2-(64,8,1)affineplaneandtwoownerp0cutsintersection>=3giveU<=63-k/freeextras<=k/newrootA<=63for k>=2,completepaperNO. Onlyk1necessaryfourdisjoint16masksunion64includingp0,uniquemissingtmatchedfreeowner,3forcedpairs;matchingextensionnotcore/oldoldD3. No numeric/graph/BFS/field/review,446/153/43/47/13cellsunchanged. Human15top exact;buildereditedonlyNOTBUILT,root ownsone15-rowbuild.')

progress=R/'research/progress.html';page=progress.read_text();assert page==(R/'research/progress.html.txt').read_text()
old_section=re.search(r'<section id="stale-route-current">.*?</section>',page,re.S);assert old_section
history=old_section.group().replace('id="stale-route-current"','id="port16-before-owner-paper"',1)
history='<details id="port16-before-owner-paper-history"><summary>前一轮快照：PORT16数值NO与当时尚待分析的p0-owner例外（保留历史）</summary>\n'+history+'\n</details>'
current='''<section id="stale-route-current">
<h2>当前结果：585固定p0四cut仅剩k=1接口未测，尚无586图</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中13格有本轮新检验，老题仍0张新增达标图。</strong><p><a href="stale_record_candidates.html">15项问题、Moore差与实际方法范围</a> · <a href="stale_record_candidates.html.txt">HTML源码</a> · <a href="stale_record_candidates.csv">15行CSV</a>。本次是同一585节点的纸面增量，不增加实测格或图。</p></div>
<p>固定实际p0=0：删四条不交core边，新点z接八core端点与p0，其他64个绝对点A加任意perfectmatching。令k为具有p0-owner端点的cut数量。原“全部owners避p0”就是k=0；其1568条eligible边、3697个DFS状态的完整NO已保存，不重跑。</p>
<table><thead><tr><th>子范围</th><th>证据</th><th>当前状态</th></tr></thead><tbody><tr><td>k=0</td><td>原完整16端口分割门</td><td>数值NO</td></tr><tr><td>k≥2</td><td>derived affine plane：U≤63−k，matching在U外至多补k，新根A覆盖≤63&lt;65</td><td>纸面NO</td></tr><tr><td>k=1</td><td>四16-mask不交、并64含p0；唯一漏点t须配自由owner，另三ownerpairs forced</td><td>必要接口，未执行数值</td></tr></tbody></table>
<p><strong>为什么k≥2也失败：</strong>继承Steiner 3-(65,9,1)，在p0导出2-(64,8,1) affine plane。p0的八个core邻点给一组parallel lines；两条p0-owner cuts除共同p0外还强制两个不同交点，因此D-mask交至少3。由此旧端口并的亏损至少大到matching的最多k个自由mate也补不回。这是纸面推导，未新建域坐标、枚举或BFS。</p>
<p><strong>k=1尚未判定。</strong>必须保存一条真实p0-owner cut与三条真实非owner cut，四个16-mask两两不交、共覆盖64个A且含p0；唯一遗漏绝对点t匹配该自由owner a，其余三cut ownerpairs仍被迫匹配。剩56A可以延拓matching，但这只解决端口层的必要条件，不保证新根到core或全部旧点对D3，也没有586候选图。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/OWNER_P0_NEXT_INTERFACE.md">derived affine plane、k≥2证明与k=1必要接口</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/PORT16_NOTE.md">原k=0数值结果与成本</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/ROOT_DISPOSITION.json">ROOT处置及paper补充</a>。</p>
<p>下一只围绕k=1接口作选择；没有新增数值授权，不换p1／sigma／seed或自动重建core-R2、匹配、586图。原PORT16累计1.881CPU／20保持。其他p0、其它改边及一般586／(9,3)未排；CM253与global256的旧严格范围继续保留。唯一Wiki仍LEDGERCOUNT条，Goal继续ACTIVE，旧N8/n61暂停；人工意见历史、153／43／Lean47及16416完整专家交付保留。</p>
</section>'''.replace('LEDGERCOUNT',str(before))
page=page[:old_section.start()]+current+'\n'+history+page[old_section.end():]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page=re.sub(r'<p>更新 [^<]*</p>','<p>更新 '+stamp+'。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>',page,count=1)
progress.write_text(page);(R/'research/progress.html.txt').write_text(page)
assert {p:(R/p).stat().st_mtime_ns for p in generated}==generated_mtime
after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before and len(after['rows'])==before and {k:after[k]for k in keys}==counts
modified=['research-wiki/DDP_METHOD_LEDGER.json','research-wiki/DDP_METHOD_LEDGER.md',n['wiki_path'],
 'research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md','research-wiki/log.md',
 S+'build_stale_record_page.py','research/progress.html','research/progress.html.txt',
 str(rawpath.relative_to(R)),str((OUT/f'{LABEL}_NODE_CALLS.log').relative_to(R)),
 str((OUT/f'{LABEL}_RECEIPT.json').relative_to(R)),str(Path(__file__).relative_to(R))]
if (W/'graph/edges.jsonl').stat().st_mtime_ns!=edges_mtime:modified.append('research-wiki/graph/edges.jsonl')
receipt=dict(status='PASS_EXISTING_585_NODE_PAPER_K_GE2_NO_K1_INTERFACE_UNTESTED',updated_UTC=NOW,
 records_before=before,records_after=before,records_added=0,updated_experiment_id=rid,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 k0='ORIGINAL_PORT16_NUMERIC_NO_UNCHANGED_NOT_RERUN',k_ge2='ROOT_ACCEPTED_COMPLETE_PAPER_NO',
 k_ge2_U_upper='63-k',k_ge2_free_mates_upper='k',k_ge2_newroot_A_upper=63,required_A=65,
 k1='NOT_NUMERICALLY_TESTED_NECESSARY_INTERFACE_ONLY',
 k1_matching_extension_NOT_graph_D3=True,original_PORT16_files_unchanged=True,
 human_top_blocks_preserved_exact=preserved,prior_progress_snapshots_preserved=True,
 shortlist_newly_tested_cells=13,shortlist_new_legal_graphs=0,
 builder_edited_only_NOT_BUILT=True,existing_candidates_HTML_CSV_JSON_not_modified_by_this_sync=True,
 root_to_do_one_existing_15row_build=True,progress_html_and_source_identical=True,
 full_index_query_rebuild_or_reimport=False,new_numeric_BFS_field_solver_Lean_review_hash_runs=0,
 root_STATE_ROUND_recovery_REPORT_modified=False,sameGoal='ACTIVE',old_N8_n61='PAUSED',
 modified_paths=modified,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
