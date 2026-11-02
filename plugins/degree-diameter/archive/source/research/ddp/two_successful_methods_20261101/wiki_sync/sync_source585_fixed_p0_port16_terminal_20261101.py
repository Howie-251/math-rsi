"""Persist one fixed-p0 port16 necessary-gate terminal, not a source-read node."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,csv,io,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='SOURCE585_FIXED_P0_PORT16_TERMINAL_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=S+'stale_record_transfer_d9D3/actual585_modified_edge_interface/'
rid='ddp-stale-d9d3-585-fixedp0-owner-avoiding-fourcorecuts-port16-no-20261101'
oldid='ddp-polarity585-all-preserved-edge-extensions-theorem-20261027'
def read(p):return json.loads((R/p).read_text())
root=read(P+'ROOT_DISPOSITION.json');result=read(P+'PORT16_RESULT.json')
term=read(P+'PORT16_TERMINAL.json');source=read(P+'SOURCE585_READ_GATE.json')
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_FIXED_P0_OWNER_AVOIDING_PROTOTYPE'
assert result['status']=='COMPLETE_NO_FIXED_P0_OWNER_AVOIDING_FOURCUT_STARPORT_PROTOTYPE'
assert result['p0_actual_vertex_label']==result['p0_cached_port_index']==0
assert result['source_core_edges_considered']==2080 and result['source_core_edges_with_p0_owner']==64
assert result['source_core_edges_with_p0_in_Cunion']==512
assert result['eligible_unrestricted_core_edges']==1568 and result['eligible_core_vertices']==448
assert result['eligible_degree_histogram']=={'7':448}
assert result['domain_count_prediction_1568_supported'] and result['domain_degree_prediction7_supported']
assert result['old_sigma_edges_retained_for_mixed_domain']==32
assert result['complete_all_four_old_candidate_evaluations']==0
assert result['dfs_nodes']==3697 and result['mixed_new_domain_exhausted']
assert not result['packing_hit'] and not result['CPU_cap_stop']
assert result['source_literal_parses']==1 and result['new_BFS_field_GQ_coreR2_matching_graph_solver_count']==0
assert term['terminal'] and term['active_processes']==0
assert abs(result['wholecase_CPU_seconds']-1.881081201)<1e-10
followup=read(S+'STALE_FOLLOWUP_ROUND_20261101.json')
assert len(followup['shortlist_cells_tested_this_round'])==13 and [9,3]in followup['shortlist_cells_tested_this_round']
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count']
records={r['id']:r for r in L['rows']};assert len(records)==before and oldid in records
assert rid not in records and not(W/'experiments'/f'{rid}.md').exists()
assert not any('585'in r['id']and'port16'in r['id']for r in L['rows'])
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances',
 'saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs',
 'pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs',
 'known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
names=['SOURCE585_READ_GATE.json','SOURCE585_READ_GATE.md','PRED.md','SOURCE585_FOURCUT_PAPER.md',
 'port16_packing_once.py','PORT16_ALL2080_CORE_EDGE_BINDINGS.tsv','PORT16_ELIGIBLE_EDGES.json',
 'PORT16_RESULT.json','PORT16_TERMINAL.json','PORT16_HANDLE.json','PORT16_NOTE.md','ROOT_DISPOSITION.json']
paths=[P+x for x in names]
paths += ['research/ddp/polarity585_replication/SOURCE_PARTITION_CHECK.json',
 'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json',
 'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/THEOREM.md',
 'research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/REPORT.md']
assert all((R/x).is_file()for x in paths)
raw=dict(id=rid,
 title='9D3 actual585固定p0、cut owners避p0：1568条不受sigma限制的core边，16端口分割完整NO',
 family='Forced owner matching and absolute-port partition after core-edge surgery',
 idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',wiki_verdict='no',
 record_type='fixed_source_fourcorecut_star_portmatching_necessary_partition_experiment',
 target_Delta=9,target_D=3,savedL=585,
 baseline_date='Inherited official Qprime8 polarity585 and cached Delorme1985 attribution; no new primary lookup/source-D3 validation',
 n=dict(actual=None,hypothetical=586),actual_graph_Delta=None,actual_D=None,
 actual_D_scope='No586candidategraphorBFS. Complete16-portnecessarypartitionNOexcludesonlyfixedactualp0owner-avoidingprototype;notanordinarybadpairmeasurementornumericaldiameterclaim.',
 ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,new_lower_bound=False,
 outcome_class=root['status'],
 scope='Fixedactual585/2600polarityquotientsource:65independentabsoluteverticesAdegree8,520coreBdegree9;notCayley. Fixp0=actualvertex0. Deletefourvertex-disjointoldB-Bedges,allendpointownersdifferentfromp0;addonevertexadjacenttoeightcoreendpointsandp0,andanyperfectmatchingonother64A. Nootheredits. Hypothetical586/2637all9regular. Coversallunrestrictedsinglecoreedgechoiceswithinthisprototype,notjustoldsigma32;onlyall-four-old-sigmasubdomaininherited. Excludesp0-ownercuts,otherp0,otherrewirings/general586or9D3fromtheNOclaim.',
 distance_text='继承实际源A-A唯一3路与Steiner3-(65,9,1)：每删core边的两个owner均非p0，旧ownerpair不能由z三步修复，故迫其成为新增A匹配边。匹配因此不能向新根C9并外补A；每cut两C9交2/并16，四16masks必须分割其余64A。域预测支持：全2080core边绑定，其中64有p0-owner，512的Cunion含p0（包含该64）；必要避p0过滤后1568eligible、448core均7度。保旧sigma32参与所有新旧混合，完整全四旧子域只继承、不重跑。3697DFS/3697失败状态、无预算截断、无partition，正向存在预测被推翻。maxvisiteddepth2只是exactcover运行记录，不是全域最大packing数。累计1.881081201/20CPU含read.800336324/prep.2/actual.880744877；0BFS/coreR2/匹配/586图/field/solver/Lean/外审。',
 lesson_and_restart_condition='STOPfixedp0actual0/allcutownersavoidp0prototype,notonlyoldsigmaedges. Droppingthesigmaselectionrestrictiondidnotremoveportpartitionbarrier:forcedownerpartnerscannotexpandnewrootportsoutsideoldCunion. Thegenerationrulemustchangebeforeanothernumericbatch. Nextonlypaper/interfaceallowingp0-ownercuts:theoldownerpairmayberepairedbyp0-z-v-A_vwithin3,andthefreeA_vmatecouldexpandcoverageoutsideU. Do notswapport1/sigma/seed,rebuildcoreR2,generate586orstartanotherpackingautomatically.',
 restart_condition='Aconcretepaper-supportedinterfaceoutsideowner-avoidingfixedp0scope,suchasactualp0-ownercutmatching-expansionroutes,followedbyanewexplicitboundeddecision;noreuseofoldtimerorautomaticp1/source/matchingladder.',
 unclosed_gap='p0-ownercuts,otherfixedp0choices,otherrewirings,oldoldrepairs,multiplehelpersandgeneral586/9D3remainOPEN. AnecessarypartitionhitwouldnotcertifycorecoverageoralloldoldD3,butactualgatehadnohit. Source-readisnotanotherexperimentnode;nonewgraph/parameter/Lean/independentmethodcount;GoalACTIVE.',
 positive_guarantees=[
  'Actualp0=vertex0isboundtocachedports[0];sourceisnonregular65deg8+520deg9,soCayleyorporttransitivityisnotassumed.',
  'Withinowner-avoidingprototype,uniqueoldA-A3routesforceM(owner(u))=owner(v)foreachcut;newrootR3onA={p0}unionU,notUunionarbitraryfreepartners.',
  'EachcutCunionhas16portsandfourmustpartition64whileavoidingp0;Cunioncontainsp0isasafenecessaryfilterevenwhenbothownersavoidp0.',
  'All32oldfixed-sigmaedgesremainavailableformixedsolutions;onlythecompleteall-four-oldsubdomainusesinheritedNO,nooldnumericreplay.',
  'DFSusesactualendpointsand64portmasks;complete3697-statefailureisnotinterpretedasmaximumgeneralpacking2.'
 ],
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
  source_n=585,source_m=2600,source_degree_histogram={'8':65,'9':520},source_D3_inherited=True,source_not_Cayley=True,
  source_read_not_separate_new_node=True,old_preserved_edge_NO_node=oldid,old_preserved_NO_repeated=False,
  p0_actual_vertex_label=0,p0_cached_port_index=0,hypothetical_order=586,hypothetical_edges=2637,hypothetical_degree=9,
  deleted_core_edges=4,newroot_corepins=8,newroot_absolute_pins=1,matching_other_absolute_vertices=64,
  owner_avoiding_is_scope_requirement=True,owner_pairs_forced_matching_within_scope=True,
  old_AA_unique3_and_Steiner='INHERITED_PAPER_NOT_RECOMPUTED',Cblock_size=9,cut_C_intersection=2,cut_C_union=16,
  newroot_absolute_condition='four16masksdisjointpartitionAminus{p0}',
  all_source_core_edges_bound=2080,core_edges_with_p0_owner=64,core_edges_Cunion_containing_p0=512,
  p0_owner_edges_are_subset_of_Cunion_containing_p0=True,necessary_eligible_domain=1568,
  eligible_core_vertices=448,eligible_degree_histogram={'7':448},domain_predictions_supported=[1568,448,7],
  old_sigma_edges_retained_for_mixed_domain=32,all_four_old_sigma_subdomain='INHERITED_COMPLETE_NO_NOT_REEXECUTED',
  old_all_four_candidate_evaluations=0,old_only_lastchoice_filter_visits=0,
  dfs_nodes=3697,failed_state_count=3697,memo_hits=0,mixed_new_domain_exhausted=True,
  max_visited_partial_depth=2,max_visited_depth_NOT_maximum_packing_claim=True,
  explicit_actual_vertex_overlap_rejections=0,actual_vertex_disjointness_checked=True,
  packing_positive_prediction_supported=False,packing_hit=False,CPU_cap_stop=False,first_unfinished_prefix=None,
  source_literal_input_parses=1,new_BFS_coreR2_matching_graph_field_GQ_solver_Lean_review_runs=0,
  actual_process_CPU_seconds=.880744877,prior_read_CPU_seconds=.800336324,new_preparation_CPU_seconds=.2,
  wholecase_CPU_seconds=1.881081201,wholecase_CPU_cap_seconds=20,all_processes_terminal=True,
  p0_owner_cut_scope='OPEN_NOT_TESTED',other_p0_scope='OPEN_NOT_TESTED',
  next_paper_interface='allowp0-ownercuts;oldownerpairp0-z-v-A_vrepairpermitsfreematecoverageoutsideU;notnewnumeric',
  shortlist_cells_newly_tested=13,shortlist_new_legal_graphs=0,same_Goal='ACTIVE',old_N8_n61='PAUSED'),
 evidence_paths=paths)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->')and LABEL not in text
 prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date'];assert n['id']==rid
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w')as log,contextlib.redirect_stdout(log):c['write_node'](n)
assert re.search(r'^verdict: no$',(W/'experiments'/f'{rid}.md').read_text(),re.M)
records[rid]=n
pointer=dict(id=rid,path=n['wiki_path'],root_disposition=P+'ROOT_DISPOSITION.json',
 scope='Differentoldedge-changingfixedactualp0owner-avoidingfourcorecutprototype',status='COMPLETE_NO',old_preserved_result_replayed=False)
records[oldid]['other_metrics']['later_changed_oldedge_port16_terminal']=pointer
records[oldid]['source_record'].setdefault('other_metrics',{})['later_changed_oldedge_port16_terminal']=pointer
oldfile=W/'experiments'/f'{oldid}.md';oldtext=oldfile.read_text();assert LABEL not in oldtext
oldtext+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 后续改旧边原型，原保边定理保留\n\n固定585源保边扩张全NO直接继承、0重跑。后续删四core边＋新星＋64A匹配在p0=actual0且所有cut owners避p0时，必要16端口分割也完整NO；这是不同scope，不扩大原定理。含p0-owner cuts及其他p0仍OPEN，下一仅paper/interface，无586候选。\n\n[新改边实验](./'+rid+'.md)；[实际处置](../../'+P+'ROOT_DISPOSITION.json)。\n'
oldfile.write_text(oldtext)
L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[ROOT证据](../'+P+'ROOT_DISPOSITION.json) |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' actual585固定p0 owner-avoiding四corecut必要门终态（一个节点）\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n第13格有本轮新检验，0新图。域数1568/448/degree7预测支持；全部2080边绑定，512含p0的Cunion由必要覆盖排除，其中64为p0-owner。3697DFS完整NO，旧sigma32保混合、只继承全四旧子域；访问深2不是最大packing2。新根A覆盖因强制owner匹配不能外扩；含p0-owner cut时p0-z-v-A_v三步可repair，M(O)可能新增端口，所以该scope仍OPEN。固定p0原型停止、不换p1/seed；下一仅该例外的paper/interface，无新数值。累计1.881081201/20CPU，0BFS/coreR2/匹配/586图/field/solver/Lean。153/43/47和savedmain105/4/global0保持。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新终态：585固定p0且cut owners避p0的原型完整NO，第13格新实测\n\n实际585非Cayley源分65deg8绝对点A与520deg9core，原保边扩张全NO继承。改变为四不交corecuts＋z接八core端点和p0=actual0＋其余64A任意匹配，限定cut owners都非p0。旧A-A唯一3路迫四ownerpairs被匹配，匹配不能向新根C9并外扩A；四个16端口mask必须分割其余64A。\n\n全2080core边绑定，64有p0-owner，512的Cunion含p0（包含该64）。安全必要过滤留下1568eligible、448core均7度，域预测支持；保32旧sigma边参与新旧混合，只继承全四旧子域NO。3697DFS完整穷尽、0partition/0预算截断，存在正预测被推翻；maxvisiteddepth2不是最大packing数。累计1.881081201/20CPU含read/prep，0新BFS/coreR2/匹配/586图/field/solver/Lean/外审。\n\n只排固定p0=0、owner-avoiding原型；p0-owner cuts仍OPEN：p0-z-v-A_v可三步修旧ownerpair，不再强制其mate，matching可能外扩U。其他p0/重连/一般586或9D3未排。不换p1/sigma/seed或续packing；下一仅include-p0-owner的paper/interface，不自动新数值。'+str(before+1)+'记录非方法，13格新实测、老15格0新达标图，153／43／Lean47及savedmain105/4/global0保持。人工15格顶块、sameGoal ACTIVE和旧N8/n61暂停保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={};index_before=None
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;index_before=int(m[1])
  text=text[:m.start()]+f'## Experiments ({index_before+1})'+text[m.end():]
  pos=text.index('\n',m.start())+1;text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': onechanged-oldedge585fixedactualp0=0owner-avoidingprototypeexperiment;notasourcereadnode. ForcedAAownerpairs implyM(O)=O,newrootAneedsfour16maskspartition64. All2080edgesbound,512Cunioncontains0(includes64owner0),eligible1568on448degree7prediction supported;3697DFScompleteNO,32oldsigmasedgeskeptmixed,allfour-oldNOinheritedwithoutreplay. maxvisiteddepth2notmaximumpacking2. p0-ownercuts remainOPEN,p0-z-v-A_vrepairpermitsfreemateexpansion. Nextonlypaper/interface,nop1/seed/numeric. Case1.881081201/20CPU,0graph/BFS/coreR2/field/solver/Lean/review,13cells,153/43/47unchanged,human15top exact,nofullrebuild.')

builder=runpy.run_path(str(R/S/'build_stale_record_page.py'))
with contextlib.redirect_stdout(io.StringIO()):builder['build']()
candidate=read(S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json')
assert len(candidate['rows'])==15 and sum(r['active']for r in candidate['rows'])==13
row=next(r for r in candidate['rows']if[r['Delta'],r['D']]==[9,3])
assert P+'PORT16_NOTE.md'in row['local_evidence'] and row['active']
assert (R/'research/stale_record_candidates.html').read_text()==(R/'research/stale_record_candidates.html.txt').read_text()
with(R/'research/stale_record_candidates.csv').open(encoding='utf-8-sig')as f:assert len(list(csv.DictReader(f)))==15

progress=R/'research/progress.html';page=progress.read_text();assert page==(R/'research/progress.html.txt').read_text()
old_section=re.search(r'<section id="stale-route-current">.*?</section>',page,re.S);assert old_section
history=old_section.group().replace('id="stale-route-current"','id="global256-before-port16"',1)
history='<details id="prior-global256-port16-interface"><summary>前一轮快照：256终态与当时585只读准备（保留历史）</summary>\n'+history+'\n</details>'
current='''<section id="stale-route-current">
<h2>当前结果：585源固定p0原型完整失败，p0-owner切边例外仍开放</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中13格有本轮新检验，老题仍0张新增达标图。</strong><p><a href="stale_record_candidates.html">15项问题、Moore差与实际方法范围</a> · <a href="stale_record_candidates.html.txt">HTML源码</a> · <a href="stale_record_candidates.csv">15行CSV</a>。第13格是(9,3)新有限门，不是第13张图。</p></div>
<p><strong>新规则从585源真实余度出发。</strong>实际极性源有65个8度绝对点A、520个9度core，非Cayley；原“保全部旧边任意扩张”NO直接继承。现删四条不交core边，新点z连八core端点及p0=实际顶点0，其余64A可任意完美匹配。此次只研究所有cut端点owner都不等于p0的原型，名义586点／2637边／全9度，未生成完整图。</p>
<p>旧A-A唯一三步路线使每条cut的两个owner必须被新增matching配成一对；新根经matching到达的伙伴因而已在八端点的C9并里。每cut给16个端口，四个16-mask必须互不相交并分割其余64A。放开旧fixed-sigma32边限制后，先预测更大域可能出现所需四块，同时预报eligible域1568边／448点均7度。</p>
<table><thead><tr><th>实际完整门</th><th>结果</th></tr></thead><tbody><tr><td>源2080条core边绑定</td><td>64条有p0-owner；512条C-union含p0，含前64条</td></tr><tr><td>必要避p0过滤域</td><td>1568条eligible、448core均7度，域数预测支持</td></tr><tr><td>四个16-mask精确分割</td><td>3697 DFS状态完整结束，0partition，无预算截断</td></tr></tbody></table>
<p>旧32条sigma边仍参与新旧混合，只继承完整“四条都旧sigma”子域NO。存在正预测被完整门推翻；最大访问深度2只是搜索记录，不是全域最大packing数。累计1.881CPU／20，含读取与准备；0新BFS、core-R2、匹配、586完整图、field、solver、Lean或外审，全部进程终态。</p>
<p><strong>停止范围：固定p0=0且owners避p0的原型。</strong>含p0-owner cuts仍OPEN，因为受损ownerpair可由p0–z–v–A_v三步修复，不必强迫A_v的mate；自由mate可能把新根覆盖扩到旧C9并外。下一仅分析这一变化的paper/interface，不换p1、seed或自动开新数值，不排其他p0、其它改边或一般586／(9,3)。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/PORT16_NOTE.md">预测、实际全域、成本与停止边界</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/SOURCE585_FOURCUT_PAPER.md">强制matching、16-mask门及p0-owner例外证明</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/PORT16_RESULT.json">实际结果</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/ROOT_DISPOSITION.json">ROOT终态处置</a>。</p>
<p>此前CM253局部手术与固定global256族的严格NO分别保留，不扩大范围。唯一Wiki现LEDGERCOUNT条研究记录，记录数不是独立方法或成果数。人工15格选题及先检验直觉再构造要求保留；Goal继续ACTIVE、旧N8/n61暂停。153／43／Lean47、全球优先权确认0与16416完整专家交付均未变化。</p>
</section>'''.replace('LEDGERCOUNT',str(before+1))
page=page[:old_section.start()]+current+'\n'+history+page[old_section.end():]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page=re.sub(r'<p>更新 [^<]*</p>','<p>更新 '+stamp+'。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>',page,count=1)
progress.write_text(page);(R/'research/progress.html.txt').write_text(page)
after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before+1 and len(after['rows'])==before+1
assert {k:after[k]for k in keys}==counts
modified=['research-wiki/DDP_METHOD_LEDGER.json','research-wiki/DDP_METHOD_LEDGER.md',n['wiki_path'],
 'research-wiki/experiments/'+oldid+'.md','research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md',
 'research-wiki/graph/edges.jsonl','research-wiki/log.md',S+'build_stale_record_page.py',
 S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json',
 'research/stale_record_candidates.csv','research/stale_record_candidates.html','research/stale_record_candidates.html.txt',
 'research/progress.html','research/progress.html.txt',str(rawpath.relative_to(R)),
 str((OUT/f'{LABEL}_NODE_CALLS.log').relative_to(R)),str((OUT/f'{LABEL}_RECEIPT.json').relative_to(R)),
 str(Path(__file__).relative_to(R))]
receipt=dict(status='PASS_ONE_FIXED_P0_OWNER_AVOIDING_PORT16_NODE_AND_EXISTING_DELIVERY_UPDATED',updated_UTC=NOW,
 records_before=before,records_after=before+1,records_added=1,new_experiment_id=rid,
 index_experiment_count_before=index_before,index_experiment_count_after=index_before+1,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 source_read_not_an_additional_node=True,p0_actual_vertex_label=0,
 source_core_edges_all_bound=2080,p0_owner_edges=64,Cunion_containing_p0_edges=512,
 necessary_eligible_edges=1568,eligible_vertices=448,eligible_degree7=True,domain_predictions_supported=True,
 DFS_nodes=3697,domain_complete_NO=True,packing_positive_prediction_supported=False,
 old_sigma32_mixed_retained=True,all_four_old_sigma_NO_inherited_not_rerun=True,
 max_visited_depth_NOT_maximum_packing_claim=True,p0_owner_cuts_status='OPEN_NOT_TESTED',other_p0_status='OPEN',
 actual_new_graphs=0,new_BFS_coreR2_matching_graph_field_solver_Lean_reviews=0,
 wholecase_CPU_seconds=1.881081201,wholecase_CPU_cap_seconds=20,
 human_top_blocks_preserved_exact=preserved,prior_progress_snapshots_preserved=True,
 existing_shortlist_rows=15,newly_tested_shortlist_cells=13,shortlist_new_legal_graphs=0,
 builder_existing_outputs_updated=True,progress_html_and_source_identical=True,
 next='INCLUDE_P0_OWNER_CUTS_PAPER_INTERFACE_ONLY_NO_NEW_NUMERIC',
 full_index_query_rebuild_or_reimport=False,sync_numeric_BFS_field_solver_Lean_review_hash_runs=0,
 root_STATE_ROUND_recovery_REPORT_modified=False,sameGoal='ACTIVE',old_N8_n61='PAUSED',
 modified_paths=modified,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
