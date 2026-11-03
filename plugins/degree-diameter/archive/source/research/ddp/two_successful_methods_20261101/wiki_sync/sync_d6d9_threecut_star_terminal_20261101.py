"""One terminal fixed-host pure-star experiment, using the existing Wiki API."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time

START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='D6D9_THREECUT_STAR_TERMINAL_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=S+'stale_record_transfer_d6D9/source_interface/threecut_star331388_gate/'
rid='ddp-stale-d6d9-fixed331387-at-most-threecuts-pure-star-complete-no-20261101'
oldids=[
 'ddp-stale-d6d9-331387-source-single-edge-subdivision-all-types-20261101',
 'ddp-stale-d6d9-f6959-primitive49-all-normal-remaining-batch-terminal-20261101']

def read(p):return json.loads((R/p).read_text())

root=read(P+'ROOT_DISPOSITION.json');profile=read(P+'PROFILE_RESULT.json')
old=read(P+'OLD_RESULT.json');term=read(P+'OLD_TERMINAL.json')
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_FIXED331387_PURE_ONEPOINT_STAR_WITH_AT_MOST_THREE_OLD_DELETIONS'
assert root['all_numeric_processes_terminal'] and term['terminal'] and term['active_processes']==0
assert root['target']==[6,9,331388] and root['wholecase_CPU_seconds']==4.575818955
assert root['prediction1_phase_empty_shortcut']['tested_complete_phase_domain']==64827
assert not root['prediction1_phase_empty_shortcut']['prediction_supported']
assert root['prediction2_mandatory_middle_geodesics']['critical_pair_counts']==[32,21,32]
assert root['prediction2_mandatory_middle_geodesics']['prediction_supported']
b=root['prediction3_old_route_coverage_barrier']
assert b['all_positive_edges_scanned_per_firsttype']==994161
assert b['eligible_after_firstendpoints_removed']==994150
assert b['max_one_otheredge_hits']==[11,7,12] and b['required']==[32,21,32]
assert b['all_types_NO'] and b['maskpair_OR_checks']==b['representative_checks']==0
assert old['raw']['all_three_firsttypes_NO'] and old['raw']['barrier_prediction_supported']
assert profile['new_question_identity_R8_support_BFS_roots']==1
assert root['source_D9_validity_BFS']==root['old_single_subdivision_queries_repeated']==0
assert root['shortest_count_DP_exports']==1 and root['new_candidate_graphs']==0

L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count']
records={r['id']:r for r in L['rows']};assert len(records)==before
assert rid not in records and not(W/'experiments'/f'{rid}.md').exists()
assert all(x in records for x in oldids)
assert not any('threecut' in r['id'] and r['goal']['Delta']==6 for r in L['rows'])
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances',
 'saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs',
 'pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs',
 'known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)

names=['PRED.md','NOTE.md','HISTORY_SOURCE_GATE.json','TERMINAL.json','PAPER_INTERFACE.md',
 'PAPER_SEAM_VERIFIER.md','PROFILE_PRED.md','profile_run_once.py','profile_once.cpp',
 'PROFILE_INPUT_BINDING.json','PROFILE_DATA_SCHEMA.json','PROFILE_IDENTITY_DISTANCE.u8',
 'PROFILE_IDENTITY_SHORTEST_COUNTS.u32','PROFILE_M_TYPE0_LABELS.u32','PROFILE_M_TYPE1_LABELS.u32',
 'PROFILE_M_TYPE2_LABELS.u32','PROFILE_CRITICAL_TYPE0.u64','PROFILE_CRITICAL_TYPE1.u64',
 'PROFILE_CRITICAL_TYPE2.u64','PROFILE_SPHERE4_LABELS.u32','PROFILE_SPHERE4_PATHS.json',
 'PROFILE_ALL_PHASE_TUPLES.tsv','PROFILE_RAW_RESULT.json','PROFILE_RESULT.json',
 'PROFILE_TERMINAL.json','PROFILE_HANDLE.json','PROFILE_NOTE.md','OLD_PRED.md',
 'PAPER_OLD_OBLIGATION_GATE.md','old_run_once.py','old_obligation_once.cpp',
 'OLD_INPUT_BINDING.json','OLD_CACHED_SPHERE4_PATHS.u32','OLD_TYPE0_MASK_CLASSES.tsv',
 'OLD_TYPE1_MASK_CLASSES.tsv','OLD_TYPE2_MASK_CLASSES.tsv','OLD_RAW_RESULT.json',
 'OLD_NEGATIVE_CERTIFICATE.json','OLD_RESULT.json','OLD_TERMINAL.json','OLD_HANDLE.json',
 'OLD_NOTE.md','FINAL_PROOF.md','FINAL_NOTE.md','ROOT_DISPOSITION.json']
paths=[P+x for x in names];assert all((R/x).is_file()for x in paths)
raw=dict(id=rid,
 title='6D9固定331387源：三删边六星的旧路线容量障碍；纸面推广排尽至多三任意删边纯星',
 family='Pure-star extension by old-edge deletion',idea_family='idea:ddp-open-parameter-construction-20261026',
 date='2026-11-01',wiki_verdict='no',record_type='fixed_host_edge_edit_pure_star_experiment_with_paper_dominance',
 target_Delta=6,target_D=9,savedL=331387,
 baseline_date='Inherited primary Rodriguez–Canale331387 communicated2012-08-20; no new public search or source-D9 validation',
 n=dict(actual=None,hypothetical=331388),actual_graph_Delta=None,actual_D=None,
 actual_D_scope='No331388candidategraphwasgenerated. Completecritical-oldpairgateandpaperdominanceexcludeD<=9fortheexactpure-star editfamily;itsfullstarhasacertifiedoldpairatdistance10,notanallpairdiametermeasurement.',
 ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=9,new_lower_bound=False,
 scope='FixedactualRodriguez–Canale331387/994161simple6regularD9host,boundRIGHTCayleyC49semidirectF6763andlefttranslations. Numericgateclosesallthreevertex-disjointoldedgecutsplusonesix-endpointstar,includingallnormal/phaseplacements. Paperdominanceextendstoeverysetofatmostthreedistinctoldedge deletions,sharedendpointsallowed,andoneaddedvertexwitharbitraryneighborhoodamongthefreedendpoints;allremainingoldedgesretained,noaddedoldoldrepair,nootheredits. Notgeneral6D9orarbitraryonepointrewiring.',
 outcome_class=root['status'],
 distance_text='三阶段预测有明确分工：相位shortcut被推翻，3个缺集相位支持均49，64827相位组合无空交；该中间结果单独没有排normal错开。随后实际共享d/c给出三类32/21/32个旧点对，其全部9-geodesics穿过首cut，支持middlemandatory预测。每类完整扫描994161条源边，去碰首端点11条后994150候选；mask类431/203/419，单额外边最多命中11/7/12项，两边上界22/14/24严格小于32/21/32，至少10/7/8项未补。容量障碍预测支持，0maskpairOR/0实际12代表检查，非抽样失败。纸面支配把同界推广到过滤11边，再由全端点星支配子星，排任意≤3distinctcuts（可共享）纯星；全星max6且某旧pair距离恰10。累计4.575818955/20CPU；因旧d/M未存，新问题supportBFS1/shortestcountDP1必要且完整保存，sourceD9validityBFS0/旧single查询0/F6959重验0/候选图0。',
 lesson_and_restart_condition='STOPthewholefixed331387hostpure-starwith<=3olddeletions,notjustaparticularphase/normalplacement. Thephaseprojectionshortcutfailedtodecidefullnormalintersection,butcriticaloldroutesprovidedastrongercompleteobstructionbeforecandidate generation. Extraedgesmustrepairdistinctmandatoryoldpairs,notmerelycoverthenewrootorloweraggregatebadpairs. Apossiblepurestarsuccessmustdelete>=4oldedges,orchangeallowedrule(e.g.oldoldrepair),hostorhelpercount;noneisautomaticallyauthorized. Nextrootquestionisonly8D3/253source-readinterface,notanexperimentresult.',
 restart_condition='Aconcreteboundedquestionoutsidefixed-host<=3deletionpurestar,suchasoldoldrepair,>=4cuts,otherhostormultiplehelpers;currentNOisnotpermissiontoautostartanyofthese. Do notrerunphase/normaloffsets,firsttriples,oldsingle-subdivision,F6959familyorunusedfullseamverifier.',
 unclosed_gap='>=4cuts,addedoldoldrepairs,oldvertexdeletion,multiplehelpers,otherhostsandarbitraryonepointextensions/generalN(6,9)remainunexcluded. Noacceptednewgraph/parameter/Lean,notanindependentmethodincrement;GoalACTIVEandhumanfeedbackstillrequired.',
 positive_guarantees=[
  'DeletingonlyedgesinsidepinsetPpreservesnearestP-distance:d_(G-F)(P,v)=d_G(P,v);translatedendpoint-R8missingintersectionemptyiffnewrootR9coversall.',
  'All32/21/32certifiedcriticalpairshaveallsource9-geodesicsthroughthechosenfirstcut;fourotherpinsmusthitB3ofatleastoneend.',
  'Completeedge-hitcardinalityboundsettlesallnormal/phasechoiceswithoutmaskpairOR,12representativechecks,candidategraphorBFS.',
  'Filteredincidentedgesaredominatedbyeligibleedges;fullfreed-endpointstarismaxdegree6anddominatesanyneighborhoodsubset,extendingNOtosharedcutsandnonregularfinalgraphs.'
 ],
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
  source_n=331387,source_m=994161,source_degree=6,source_D9_inherited=True,
  source_RIGHT_binding=root['source_RIGHT_binding'],source_not_new_portfolio_graph=True,
  hypothetical_three_disjointcut_order=331388,hypothetical_edges=994164,hypothetical_all_regular_degree=6,
  phase_projection_domains=64827,missing_phase_supports=[49,49,49],empty_phase_projection_intersections=0,
  phase_shortcut_prediction_supported=False,normal_offsets_after_phase_alone='HISTORICALLY_OPEN_SUPERSEDED_BY_FINAL_OLD_ROUTE_NO',
  critical_oldpairs=[32,21,32],middle_mandatory_geodesic_prediction_supported=True,
  complete_edges_scanned_per_firsttype=994161,first_endpoints_incident_edges_filtered=11,
  eligible_edges_per_firsttype=994150,mask_classes=[431,203,419],
  zero_mask_edges=[940914,956564,939533],max_other_edge_hits=[11,7,12],
  two_other_edges_hit_upper=[22,14,24],unavoidably_unrepaired_at_least=[10,7,8],
  old_route_barrier_prediction_supported=True,complete_numeric_three_disjointcut_NO=True,
  maskpair_OR_checks=0,actual_representative_edgepair_checks=0,
  paper_extension='anyatmost3distinctcuts,sharedendpointsallowed,arbitrarynewneighborhoodsubsetoffreedendpoints,purestaronly',
  paper_full_star_max_degree=6,paper_failed_oldpair_distance=10,paper_not_Lean=True,
  new_question_support_BFS_roots=1,new_question_shortest_count_DP_exports=1,
  source_D9_validity_BFS_roots=0,old_single_subdivision_queries_repeated=0,
  old_obligation_additional_BFS_DP=0,source_field_or_F6959_rechecks=0,
  full_seam_verifier_executed=False,candidate_graphs_generated=0,
  wholecase_CPU_seconds=4.575818955,wholecase_CPU_cap_seconds=20,all_numeric_processes_terminal=True,
  complete_scoped_NO=True,not_general_6D9_or_arbitrary_onepoint_NO=True,
  inherited_stopped_history_node_ids=oldids,
  next_readonly_question='8D3/253sourceinterface;notanactualresultornumericcontinuation'),
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

history_note='后续独立scope已关闭：固定actual331387源至多三distinct旧边删除（可共享端点）＋一点连接任意获释端点的纯star完整NO；不得据此扩大旧F6959或single范围。旧singleNo/F6959normalNo均未重跑，保留历史；详见新机制节点与FINAL_PROOF。'
for oid in oldids:
 r=records[oid];pointer=dict(id=rid,path=n['wiki_path'],proof=P+'FINAL_PROOF.md',note=history_note,
  independent_oldedge_edit_scope=True,old_result_replayed=False,new_graph_parameter_Lean_method_increment=[0,0,0,0])
 r['other_metrics']['later_fixed_host_pure_star_terminal']=pointer
 r['source_record'].setdefault('other_metrics',{})['later_fixed_host_pure_star_terminal']=pointer
 path=W/'experiments'/f'{oid}.md';text=path.read_text();assert LABEL not in text
 text+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 后续固定源纯星范围（原历史不改）\n\n'+history_note+'\n\n[新scope实验](./'+rid+'.md)；[完整纸面证明](../../'+P+'FINAL_PROOF.md)；[ROOT处置](../../'+P+'ROOT_DISPOSITION.json)。这一链接不重计旧结论为新成果。\n'
 path.write_text(text)
L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[ROOT证据](../'+P+'ROOT_DISPOSITION.json) |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text()
needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 固定331387源≤3删边纯星完整NO（一个实验节点）\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n相位shortcut被64827无空交推翻，但当时normal仍开放；随后mandatory旧pair32/21/32及全边命中上界11/7/12完成不同、更强的NO。完整扫描每类994161边/filter994150，2max22/14/24不足，实际0OR/0代表检查。纸面支配统一覆盖任意≤3distinctcuts可共享＋任意freed-endpoint子星，无oldoldrepair。停止这一固定源纯星全范围；>=4cuts/oldoldrepair/otherhosts/多helper及一般6D9未排、不自动启动。累计4.575818955/20CPU，新问题supportBFS1/DP1，sourceD9有效性BFS0/旧single及F6959重跑0/图0。旧两NO节点互链保历史；153/43/47、savedmain105/4/global0保持。下一8D3/253仅只读接口，不登记结果。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新终态：固定331387源至多三删边纯star完整NO\n\n三预测链：相位shortcut被推翻（3M各覆盖全49相位，64827组合无空交），此项单独仍留normal开放；实际middlemandatory旧pair32/21/32支持。随后每首类型完整扫994161旧边、过滤碰首端点11条余994150，单额外边最多命中11/7/12，两个上界22/14/24小于所需32/21/32，严格NO；实际0maskpairOR/0十二代表检查，非样本失败。\n\n纸面支配把同界推广到过滤边，再由全星支配子星，关闭固定源任意≤3distinct旧边删除（可共享端点）＋一点连接任意freed-endpoint子集的纯star。全星max6且有旧pair距离恰10。无oldoldrepair；不是一般6D9或任意单点NO。>=4cuts/oldoldrepair/otherhosts/多helper未排且不自动启动。旧singleNo与F6959normalNo保历史互链，均0重跑。\n\n累计4.575818955/20CPU，新问题supportBFS1/DP1（旧d/M未保存所以必要），sourceD9validityBFS0/旧single查询0/F6959重验0/候选图0。停止该固定源≤3cuts纯星族，不续normaloffsets、triples或未执行fullseam。下一root问题8D3/253仅只读source接口，不算结果。'+str(before+1)+'条实验等记录（非独立方法），153图／43参数／Lean47、savedmain105/4/global0不变。人工15格顶部、sameGoal ACTIVE与旧N8/n61暂停保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={};index_before=None;index_after=None
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre)
 text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m
  index_before=int(m[1]);index_after=index_before+1
  text=text[:m.start()]+f'## Experiments ({index_after})'+text[m.end():]
  pos=text.index('\n',m.start())+1
  text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': onefixedhostoldedge-editexperimentnode,notindependentmethod/graph. Phaseprojectionshortcutrefuted64827/full49,normalsformerlyopen;mandatoryoldpairs32/21/32supported,complete994161-edgehitbound11/7/12gives22/14/24insufficient,0OR/representativechecks. Paperdominanceclosesany<=3distinctcuts/sharedpins/purestarfreedendpointsubset,nooldoldrepair. ScopeNOTgeneral6D9/arbitraryonepoint;stopandpreserveoldsingle/F6959NOhistorywithoutreplay. Case4.575818955/20CPU,supportBFS1/DP1fornewdata,sourceD9validationBFS0,0newgraph. Human15oldcells top preserved,153/43/47 unchanged,next8D3/253read-onlynotresult.')
after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before+1 and len(after['rows'])==before+1
assert {k:after[k]for k in keys}==counts
assert all((R/p).is_file()for p in paths)
receipt=dict(status='PASS_ONE_FIXED331387_AT_MOST_THREECUT_PURE_STAR_TERMINAL_NODE',updated_UTC=NOW,
 records_before=before,records_after=before+1,records_added=1,new_experiment_id=rid,
 index_experiment_count_before=index_before,index_experiment_count_after=index_after,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 phase_shortcut_prediction_supported=False,phase_alone_historical_normal_open_preserved=True,
 mandatory_middle_pairs_prediction_supported=True,critical_oldpair_counts=[32,21,32],
 old_route_hit_bound_prediction_supported=True,all_source_edges_scanned_per_type=994161,
 filtered_eligible_per_type=994150,max_otheredge_hits=[11,7,12],two_max=[22,14,24],
 maskpair_OR_checks=0,representative_checks=0,
 numeric_scope='allfixed331387threevertex-disjointcutsplus6star/allnormalphase',
 paper_scope='fixed331387any<=3distinctcuts/sharedendpoints/arbitraryfreed-endpointnewneighborhood/purestar/nooldoldrepair',
 not_general_6D9_or_arbitrary_onepoint_NO=True,old_history_nodes_linked=oldids,old_conclusions_replayed=False,
 new_question_support_BFS_roots=1,new_question_DP_exports=1,source_D9validity_BFS=0,
 old_single_queries=0,F6959_rechecks=0,candidate_graphs=0,
 wholecase_CPU_seconds=4.575818955,wholecase_CPU_cap_seconds=20,
 human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
 sync_numerical_source_graph_BFS_Lean_solver_paidreview_hash_runs=0,
 root_STATE_HTML_REPORT_recovery_builder_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,
 sameGoal='ACTIVE',old_N8_n61='PAUSED',next_readonly8D3_253_not_result=True,
 CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
