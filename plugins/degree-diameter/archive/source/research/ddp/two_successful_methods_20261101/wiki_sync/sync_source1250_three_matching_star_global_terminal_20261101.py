"""One fixed+global three-cut K1,3 experiment delta; no rebuild or math runs."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/threecut_fourhelper_star1254';G=D/'global_three_matching_gate'
start=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d3d10-conder1250-three-matching-cuts-fourhelper-star-global-no-20261101'
marker='<!-- SOURCE1250_THREE_MATCHING_STAR_GLOBAL_TERMINAL_20261101 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==450
assert not any(r['id']==slug or 'threecut_fourhelper_star1254' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
f=json.loads((D/'RESULT.json').read_text());g=json.loads((G/'RESULT.json').read_text())
assert f['visited_configs']==f['domain_configs']==1865 and f['newroot_firstfails_centre_L0_L1_L2']==[1865,0,0,0]
assert g['checked_matching_pairs']==g['domain_matching_pairs']==1743779 and g['eligible_other_edges']==1870
assert g['stage_firstfails_centre_L0_L1_L2']==[1743779,0,0,0] and g['all_four_exact_gate_pass']==0
assert g['starline_cumulative_CPU']==3.611239973 and g['actual_newroot_BFS']==g['modified_oldroot_BFS']==0
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
old='ddp-conder1250-edge-subdivision-two-cut-helper-family-20261027';oldrow=next(r for r in ledger['rows'] if r['id']==old)
fixed_evidence=['HISTORY_SCOPE.json','PRED.md','STAR_ROUTE_PAPER.md','STAR_SCOPE_ATTACK.md','GLOBAL_DOMAIN_PAPER.md','GLOBAL_SCOPE_ATTACK.md','run_once.cpp','run_once.py','ACTUAL_DOMAIN.json','CONFIG_RESULTS.tsv','FIRST_FAILURE.json','FIRST_CENTRE_FAILURE.json','ROUTE_CLASS_SUMMARY.json','RESULT.json','TERMINAL.json','NOTE.md','ROOT_DISPOSITION.json']
global_evidence=['PRED.md','run_once.cpp','run_once.py','ACTUAL_DOMAIN.json','BALL_SCHEMA.json','SOURCE_R7_R8_R9.bits','SAVED_FIXED_SAMPLE_DP_COMPARISON.json','PER_FIRST_EDGE_STAGE_COUNTS.tsv','STAGE_FIRST_FAILURES.json','RESULT.json','TERMINAL.json','NOTE.md','DRIVER_HANDLE.json','COMPILE.log','RUN.log']
evidence=[str((D/p).relative_to(ROOT)) for p in fixed_evidence]+[str((G/p).relative_to(ROOT)) for p in global_evidence];assert all((ROOT/p).exists() for p in evidence)
raw={
'id':slug,'title':'3D10 Conder1250三matching-cut四helper星：固定1865及全1743779均centre失败，整同源规则NO',
'family':oldrow['method_family'],'idea_family':'idea:ddp-open-parameter-construction-20261026','date':'2026-11-01','wiki_verdict':'no',
'record_type':'fixed_existing_host_three_matchingcuts_fourhelper_star_complete_experiment',
'target_Delta':3,'target_D':10,'savedL':1250,'baseline_date':'2026-11-01 root checkedprimary1250/known2006-08-17; notnewrecordclaim',
'n':{'actual':None,'hypothetical':1254},'actual_graph_Delta':3,'actual_D':None,'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':10,'new_lower_bound':False,
'actual_D_scope':'Fixed1865 actualmodified candidate centre eccentricities11:1588/12:277 only, not global candidate diameters. Global1743779 exactcentrecoverage gates allfail; no actualglobalcandidate or leaf/oldold BFS. No1254 D10 acceptedgraph.',
'outcome_class':'COMPLETE_NO_FIXED_SOURCE_ALL_THREE_MATCHING_CUT_FOURHELPER_K13',
'scope':'Literal Conder1250source. Delete3vertex-disjoint originaledges; whole eachcut endpointpair goes toone degree3leaf; threeleaves joinonecentre K1,3, preservingall6endpointspokes; nooldrepair. Fixedcuts(0,1)/(869,1178) with1865thirdedges firstcompleteNO. Then one newglobalanchoredgate e0=(0,1), e1<e2 disjointfromanchorandeachother:1870otheredges/1743779matchingpairs, completeallcentreNO. Inherited sourceedge-transitivity plusstarleafpermutation makesanchored domaincoverthissourceall3matchingcuts, notcandidateVT. Notallfourhelper topologies, otherhosts, overlappingcuts, general3D10, oroldpin-transfer rule.',
'distance_text':'为补前轮withdrawn-pin责任而保留全部六spokes，固定1865候选各有L0-C-L1-1178长度3实际walk（未称leaf最短路BFS），但全部centreR10fail；首cut(2,6)的C→886最短11。继而root提出weighted-lastcut精确G公式，独立paper纠正初版过强的“weightedminimum不能整体替G”；逐Pi的dT=dG仍不成立。新sourceR0..9 DP保存R7/8/9，完整1743779配置均centre endpointR8并不全；leaf三个exact门NOT_ENTERED，不称allleaf失败。0globalcandidate/newrootBFS/oldrootBFS，整同源3matchingcut/K1,3规则严格NO。starline3.611239973/30CPU含fixed1.916663729，0新图/参数/Lean。',
'lesson_and_restart_condition':'STOPthissourcewholethree-matching-cutK1,3rule. Preservingendpointresponsibilitydoesnotrepairthecentre two-stepaccesscost: allsix-endpointR8unionsmissatleastonetarget. Theformulaimprovement changedactualresearchfromfixed1865ordinarycandidateBFS tocomplete1743779exactbitsetdomain, ratherthanseed/timerextensions. Do notrepeatfixed/globaldomains ortransferthenegativetootherhelper topologies.',
'restart_condition':'A newly authorized bounded structural question that changeshelper topology/routecost,cutcontract,hostorothermeaningfulrule; noautomaticfourthcut/newsource/anchor/seed.',
'unclosed_gap':'Otherfourhelper topologies, nonmatchingcuts, extraoldoldrepair, otherhosts/morehelpers/general3D10remainunexcluded. Leafgates were not entered; their individual failure is not measured. Oldold distances remain a separate requirement foranyfuture gatepasser. No newLean graph/theorem orglobalrecord claim; sameGoalACTIVE/oldN8n61PAUSED.',
'positive_guarantees':[
'Allsixcutendpointsretainspokes; n1254/m1881/cubic followsactualinput/editbinding. Thischangespreviouspin-transfer operation ratherthanrepeatingits11178NO.',
'OriginalweightedTdistanceformula remainscorrect. Rootlastcutargument andtwoindependentpaperreaders establishwholeweightedGminimum equality; neverclaimseachindividualdT(Pi)=dG(Pi).',
'Exactcentre cover=E0R8|E1R8|E2R8; leafi cover=EiR9|otherEjR7|otherEkR7. Globalnegativeusesonlycentre exactformulawhichwasactuallyevaluatedforall1743779.',
'AnchorcompletenessusesoldsourceedgeVTandstarleafpermutation, notmodifiedcandidatevertex-transitivity. e1<e2,matchingconstraints,closedballradiiandlastword34bitsareexplicitlybound.',
'NewcoverageDPisnotoldsourceD10validityBFS; savedfixedtarget886 sourceR8countercheckusedcachedcasewithoutrepeatingitscandidateBFS.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,'single_experiment_record_for_fixed_and_global':True,
'source_node':old,'prior_distinct_pin_transfer_node':'ddp-stale-d3d10-conder1250-frozen4536-protected1178-thirdcut-pintransfer-complete-no-20261101','source_n':1250,'source_m':1875,'source_D10_inherited':True,'source_edge_transitivity_inherited':True,
'fixed_gate':{'configs':1865,'P1_explicit_walk':[1250,1253,1251,1178],'P1_walks_verified':1865,'P1_not_leaf_shortest_BFS':True,'newroot_calls_C_L0_L1_L2':[1865,0,0,0],'firstfails_C_L0_L1_L2':[1865,0,0,0],'centre_ecc_hist':{'11':1588,'12':277},'source_parse_count':1,'sourceD10validationBFS':0,'case_CPU':1.916663729},
'paper_correction_history':{'initial_correct_T_formula':True,'initial_overclaim':'IndividualPiT/Gdistancecannotbeassumedunchanged;initialpaperincorrectlyextendedthiscautiontothewholeweightedminimum.','corrected_result':'min_j(wj+dT(Pj,t))=min_j(wj+dG(Pj,t)),weightsown1/other3;centredistance2+dG(all6endpoints,t).','individual_Pi_T_equals_G_claim':False,'correction_before_global_numeric':True,'two_independent_paper_readers':True},
'global_gate':{'eligible_other_edges':1870,'matchingpairs':1743779,'checked_matchingpairs':1743779,'stagecalls_C_L0_L1_L2':[1743779,0,0,0],'firstfails_C_L0_L1_L2':[1743779,0,0,0],'leaf_stages':'NOT_ENTERED','all_four_gate_pass':0,'actual_newroot_BFS':0,'modified_oldroot_BFS':0,'candidate_graphs_generated':0,'source_parse_count':1,'sourceD10validationBFS':0,'DP_closedball_radii':[0,1,2,3,4,5,6,7,8,9],'persisted_radii':[7,8,9],'persisted_bytes':600000,'DP_word_OR_operations':675000,'edgeunion_word_OR_operations':112500,'coverage_word_visits':24513703,'tailword_usedbits':34,'cursor_e1_e2':[-1,-1],'firstgate_counterexample':{'edge_ids':[0,5,7],'target':1057},'savedfixedsample_target886_sourceR8missing':True},
'line_source_parse_count':2,'line_sourceD10validationBFS':0,'fixed_CPU_inherited':1.916663729,'global_compile_CPU':1.052862,'global_native_actual_CPU':.039517,'starline_cumulative_CPU':3.611239973,'starline_CPU_cap':30,'no_timer_reset':True,'all_processes_terminal':True,'whole_same_source_star_rule_stopped':True,
'negative_Lean_requirement':{'required':False,'run':False,'new_Lean_graph_or_theorem_claim':False,'paper_scope':'inheritedconcretesource+matchingcuts+wholepairs-to-leaf+K1,3 exactdistancelemma'},'same_Goal':'ACTIVE','old_N8_n61':'PAUSED'
},'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'SOURCE1250_THREE_MATCHING_STAR_GLOBAL_TERMINAL_20261101_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'SOURCE1250_THREE_MATCHING_STAR_GLOBAL_TERMINAL_20261101_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'].append(row);ledger['record_count']=451;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} 1250三matching-cut／四helper星全同源规则已NO

为保住端点责任改用四helper K1,3：固定两cut的1865候选都保L0–C–L1–1178长度3实际walk，却1865全centre失败。随后weighted-lastcut纸面纠正初版过强论述：整体weighted minimum可精确用G，不能宣称各Pi逐项T=G。由此新全域门anchor0–1、1870其他边、1743779匹配对完整，全部centre端点R8并仍缺点；leaf三门NOT_ENTERED/0，不称其均失败。0globalcandidate/BFS/oldold验收；新sourceR7/8/9搜索DP已存，0sourceD10复验。

整同源三matchingcut／完整端点分leaf／K1,3规则STOP，其他helper拓扑/host/一般3D10未排。一个记录合并fixed+global，450→451，不拆方法，starline3.611239973/30CPU继承fixed成本。0新图/参数/Lean；153/43/47、savedmain105/4/global0保持。人工15格顶块逐字保留，sameGoal ACTIVE、旧N8n61暂停。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert m;oldexp=int(m.group(1));text=text[:m.start(1)]+str(oldexp+1)+text[m.end(1):]
 (W/name).write_text(text);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} 同源全部三matchingcuts／四helper星严格NO

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (3,10)；L1250；目标1254，未得合法D10图 | 固定1865实际centre fail；global1743779 exactcentre fail。leaf/候选BFS/oldold全NOT_ENTERED，非各leaf失败。 | weighted-lastcut整体G公式纠正初版过强保守结论；各Pi逐项T=G未声称。源edgeVT+leaf置换保证全域；只排同源三matchingcut/K1,3。[实际终态](../{str((G/'NOTE.md').relative_to(ROOT))}) |

一个实验记录450→451，fixed/global不拆节点。新sourceR7/8/9 DP为搜索数据而非旧D10验收；starline3.611239973/30含原fixed1.916663729。0新图/参数/Lean/独立方法，153/43/47保持；其他拓扑/host/一般3D10未排，已停不续。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==451;assert all(after[k]==v for k,v in counts.items());assert (W/node).exists();assert all((ROOT/p).exists() for p in row['evidence_paths'])
receipt={'status':'PASS_ONE_SOURCE1250_THREE_MATCHING_STAR_FIXED_PLUS_GLOBAL_TERMINAL_NODE','updated_UTC':now,'records_before':450,'records_after':451,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'fixed_and_global_same_one_node':True,'index_experiment_count_before':oldexp,'index_experiment_count_after':oldexp+1,'graph_parameter_Lean_method_increments':[0,0,0,0],'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples']},'fixed_configs':1865,'global_matchingpairs':1743779,'all_global_centre_fail':1743779,'leaf_stages':'NOT_ENTERED_NOT_FAILURE_CLAIMS','global_graph_BFS_count':0,'sourceD10validation_BFS':0,'new_R7_R8_R9_DP_retained':True,'weighted_lastcut_correction_recorded':True,'individual_Pi_T_equals_G_claim':False,'starline_cumulative_CPU':3.611239973,'starline_CPU_cap':30,'negative_Lean_required':False,'all_processes_terminal':True,'whole_same_source_K13_matching_rule_stopped':True,'general3D10_other_topologies_unexcluded':True,'human_top_blocks_preserved_exact':{name:True for name in files},'full_rebuild_reimport':False,'new_math_BFS_solver_field_Lean_ARIS_hash_runs':0,'root_STATE_ROUND_recovery_progress_builder_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-start,'row_path':str(rowfile.relative_to(ROOT)),'ROOT_disposition_link':str((D/'ROOT_DISPOSITION.json').relative_to(ROOT)),'stop':True}
(S/'SOURCE1250_THREE_MATCHING_STAR_GLOBAL_TERMINAL_20261101_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
