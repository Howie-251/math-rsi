"""One two6804-matching terminal problem record; minimal Wiki delta only."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608'
st=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-d14d4-two6804-only-cross-arbitrary-matching-point-overlap-complete-no-20261102'
marker='<!-- TWO6804_ANY_MATCHING_POINT_OVERLAP_TERMINAL_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==451
assert not any(r['id']==slug or 'two6804_matching13608' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
root=json.loads((D/'ROOT_DISPOSITION.json').read_text());r=json.loads((D/'OVERLAP_RESULT.json').read_text());ordinary=json.loads((D/'PHASE_CAPACITY_RESULT.json').read_text());nb=json.loads((D/'NB_PHASE_CAPACITY_RESULT.json').read_text())
assert root['status']=='ROOT_ACCEPTED_NO_ANY_ONLY_CROSS_PERFECT_MATCHING_TWO6804_D4'
assert (r['B2max'],r['S2max'],r['B3max_all6804'],r['S3max_all6804'],r['raw_union_upper'],r['witness_L'],r['witness_union_upper'])==(154,140,1588,1434,6984,260,6724)
assert ordinary['status']=='FEASIBLE_PHASE_PERMUTATION_CAPACITY_ONLY' and ordinary['minimum_capacity']==573
assert nb['status']=='UNKNOWN_NB_PHASE_CAPACITY' and nb['raw']['nodes']==4112 and nb['permutation'] is None
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
sourceid='ddp-d13-d4-current6804-source-20261027';oldrow=next(x for x in ledger['rows'] if x['id']==sourceid)
evidence_names=['ROOT_DISPOSITION.json','NOTE.md','FINAL_MATCHING_DISPOSITION_NOTE.md','POINT_BALL_OVERLAP_PAPER.md','CONSTANT_PHASE_PRED.md','CONSTANT_PHASE_PAPER.md','CONSTANT_PHASE_RESULT.json','PHASE_PERMUTATION_PRED.md','PHASE_PERMUTATION_CAPACITY_PAPER.md','PHASE_PERMUTATION_SCOPE_ATTACK.md','run_phase_permutation_once.py','PHASE_CAPACITY_MODEL.json','PHASE_CAPACITY_RESULT.json','PHASE_CAPACITY_TERMINAL.json','ORDINARY_PI_NB_CHECK.json','NONBACKTRACKING_PRED.md','NONBACKTRACKING_CAPACITY_PAPER.md','run_phase_nb_once.py','NB_PHASE_CAPACITY_MODEL.json','NB_PHASE_CAPACITY_RESULT.json','NB_PHASE_CAPACITY_TERMINAL.json','NB_PHASE_SOLVER_STDOUT.log','OVERLAP_PRED.md','overlap_gate.cpp','OVERLAP_RESULT.json','OVERLAP_CHILD_RESULT.json','OVERLAP_SHELL_PROFILES.tsv','OVERLAP_ROOT_RESULTS.tsv','FIRST81_OVERLAP_RESULT.json','FIRST81_OVERLAP_SHELL_PROFILES.tsv','FIRST81_OVERLAP_ROOT_RESULTS.tsv','INITIAL_FORMAT_FAILURE_OVERLAP_RESULT.json','INITIAL_FORMAT_FAILURE_overlap_gate.cpp']
evidence=[str((D/p).relative_to(ROOT)) for p in evidence_names];assert all((ROOT/p).exists() for p in evidence)
raw={
'id':slug,'title':'14D4两份6804只加跨副本matching：相位容量到实际点球，任意全/部分matching均NO',
'family':'Two-copy retained-edge matching extension with exact point-ball overlap',
'idea_family':'idea:ddp-open-parameter-construction-20261026','date':'2026-11-02','wiki_verdict':'no',
'record_type':'fixed_twocopy_crossmatching_route_capacity_and_point_overlap_experiment',
'target_Delta':14,'target_D':4,'savedL':9720,'baseline_date':'2026-11-01 root primary14D4 main9720;13608hypotheticalonly',
'n':{'actual':None,'hypothetical':13608},'actual_graph_Delta':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':4,'new_lower_bound':False,
'actual_D_scope':'No13608graphwasgenerated/accepted. CompleteproofexcludesD<=4foronly-cross arbitraryperfectmatching(andpartialmatchingbycompletion)ontwoexact6804sourcecopies. Existing13regularsourceD4isnotneededforthisnegativeproof; sourceD4validityBFS0.',
'outcome_class':'COMPLETE_NO_FIXED_TWO6804_ONLY_CROSS_ARBITRARY_PERFECT_OR_PARTIAL_MATCHING_D4',
'scope':'Two copies of actualsimple13regular6804/44226 literal; preservealloldedgesandaddonlycrossedgeswithcrossdegree<=1. Anyfullpoint-perfectmatchingM, no phase/fibre/affine/group/Aut restriction; partialcrossmatchingsalsoNObymonotonecompletiononequalcopies. Excludesonlythishost/rule,notgeneral14D4,otherhosts,oldoldcopy-internaladditions,oldedgerewiring,multi-crossdegreeorhelpervertices. Constantphase/ordinarypi/NB/pointoverlapareoneproblemrecord,notfourmethods.',
'distance_text':'恒定phaseoffset族328<567先严格NO；改任意12phase排列，普通walk容量实际min573仅necessaryfeasible。其同π扣nonbacktracking折返后min547<567，被反驳；唯一新NB模型8秒4112nodes无incumbent，UNKNOWN而非INFEASIBLE。于是改查actualpoint球重复覆盖，旧uniform6860前提被literal反驳：全部6804新R2/R3 maxima B2=154/S2=140/B3=1588/S3=1434，安全未扣重U=6984。只取y0，对6803个z!=0交集13最小项各20/总260；任意M取u=M^-1(0)，跨copyR4覆盖<=6984-260=6724<6804，至少80漏点，整任意pointmatching族严格NO。无Aut/相位/源D4假设，partialmatching可补全亦NO。13.170781895/15CPU含格式失败和81→全6804扩域，0新图/参数/Lean。',
'lesson_and_restart_condition':'STOPthis two6804 retained-oldedges only-crossmatching mechanism. Ordinarywalkcapacitysuccessdidnotbecomepointcoverage; exactNBrefutedtheordinarywitness, thenfiniteactualballoverlapclosedallpointmatchingsbeyondphaseconstraints. Uniformroot0profilewasrefutedratherthanforcedontoallroots; actualmaximaandonepreimagewitnessremovedAut/uniform assumptions. Noadditionalphase/fibre/permutation/NBsolver/copy/degreewindow. KeepNBnecessary-modelUNKNOWNdistinctfromstrongeractualgraph-familyNO.',
'restart_condition':'Onlyanewboundedstructuralquestionthatchangeshost,allowableoldoldedges/rewiring,crossdegreeorhelperrules; do not resume theclosedonly-crosspointmatching line or oldNBtimer.',
'unclosed_gap':'General14D4andother13608constructionsremainunexcluded. NBphasecapacitymodelitselfremainsUNKNOWNnotINFEASIBLE; strongerpointgraphNOdoesnotchangethatsolverreturn. One y suffices; all-yLminnotmeasured. No13608graphacceptance,formalgraphwitnessornewglobalrecord. New3645readinheritsoldNOand8D4K19readpreparationarenotnewexperimentnodeshere.',
'positive_guarantees':[
'For<=4crosscopywalks,3crossesforceamatchingbacktrack,soone-cross exactunion is union_a0..3 union_xinSa(u) B_(3-a)(M(x)); shortest-prefixshellsensureallallowedroutesincluded.',
'All6804actualclosedR2/R3shellprofiles provide globalmaxima154/140/1588/1434; formeruniformroot0profile and6860 predictionarefalseassumptionsnotusedinthefinalproof.',
'Forfixedy0,13imagesofN(M^-1(0))are13distinctactualcentresdifferentfrom0. TheirB3(0)/B2(z)intersectionssumatleastthe13smallest260, safelydeductedwithoutovercountingA0.',
'SurjectivitysuppliesrootM^-1(0)forallM; one y0witness suffices, notall-yLmin. No sourceAut/phase/affine matchingor inheritedsourceD4assumption.',
'Partialonly-crossmatchingcanbecompletedtoperfectmatchingbetweenunusedvertices; additioncannotincreasedistances,soD4partialwouldcontradictfullNO. Doesnotallowadditionalcopy-internaloldoldedges.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,'single_record_for_four_adaptive_stages':True,'source_node':sourceid,'source_n':6804,'source_m':44226,'source_degree':13,'target_hypothetical_n':13608,'sourceD4_needed_for_negative_proof':False,
'constantphase':{'verdict':'STRICT_NO_FIXED_PHASE_OFFSET_ALL_FIBRE_BIJECTIONS','capacity_upper':328,'phase_targets':567,'deficit':239},
'ordinary_phase_pi':{'status':'FEASIBLE_NECESSARY_CAPACITY_ONLY','permutation':ordinary['permutation'],'minimum':573,'pointgraph_generated':False},
'ordinary_pi_NB_check':{'status':'REFUTED_SAME_ORDINARY_PI','minimum':547,'needed':567,'failedslots':8},
'NB_model':{'rawstatus':'UNKNOWN_TIME_LIMIT_NOT_INFEASIBLE','configured_seconds':8,'nodes':4112,'incumbent':None,'model_feasibility_verdict_unchanged':True,'stopped_after_stronger_pointfamily_NO':True},
'old_uniform_profile_claim':{'profile':[1,13,138,1400,5252],'scope':'root0only_notuniform','actual_literal_refuted':True,'old_raw_upper6860_not_used':True,'first81_then_all6804_corrective_extension_preserved':True},
'actual_point_overlap':{'new_query_roots_R2_R3':6804,'B2max':154,'S2max':140,'B3max':1588,'S3max':1434,'B1':14,'raw_union_upper':6984,'threshold_for_one_witness':181,'y_witness':0,'actual_z_checked':6803,'thirteen_smallest_intersections':[20]*13,'thirteen_distinct_centres':[1142,1171,1708,1709,1710,1711,1722,1724,1731,1732,1743,1745,1747],'mandatory_overlap':260,'cross_R4_cover_upper':6724,'target_count':6804,'missing_targets_at_Minverse0_atleast':80,'all_y_Lmin_claimed':False,'source_Aut_phase_affine_D4_assumptions_needed':False,'partial_crossmatching_corollary':True},
'proof_query_vs_validation':{'new_coverage_R1_R2_R3_support':True,'sourceD4validationBFS':0,'field_Lean_ARIS':0,'final_literal_parse_count':1,'format_failure_preserved':True,'first81_support_preserved':True},
'cumulative_line_CPU':13.170781895,'line_CPU_cap':15,'all_processes_terminal':True,'no_timer_reset':True,'negative_Lean_required':False,'negative_Lean_run':False,'whole_only_cross_matching_line_stopped':True,'same_Goal':'ACTIVE','old_N8_n61':'PAUSED'
},'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'TWO6804_ANY_MATCHING_POINT_OVERLAP_TERMINAL_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'TWO6804_ANY_MATCHING_POINT_OVERLAP_TERMINAL_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
node='experiments/'+slug+'.md'
# Minimal backlink/correction on the existing source node; no second record or history replacement.
sourcepath=ROOT/oldrow['wiki_path'];sourcemarker='<!-- TWO6804_POINT_OVERLAP_FOLLOWUP_20261102 -->';sourcebefore=sourcepath.read_text();assert sourcemarker not in sourcebefore
sourcepath.write_text(sourcebefore+f'''\n\n{sourcemarker}
## 2026-11-02 两副本only-crossmatching后续与profile更正

[实际point-overlap终态]({slug}.md)：固定source两copy保全部旧边，只加任意全/部分crossmatching均不能D4。全6804新R2/R3给B2max154/S2max140/B3max1588/S3max1434；旧root0的(1,13,138,1400,5252)不能当uniform，6860旧预测不用于证明。正确6984−260=6724<6804。此后续不依赖sourceAut/源D4假设，不覆盖本节点旧hub/split/允许oldold操作的全部范围；旧UNKNOWN原样保留。无新source验收/图/Lean。
''')
back={'experiment_id':slug,'wiki_path':str((W/node).relative_to(ROOT)),'only_crossmatching_scope_NO':True,'old_source_uniform_profile_refuted':True,'actual_maxima':[154,140,1588,1434],'old_hub_UNKNOWN_not_overwritten':True}
oldrow['other_metrics']['two_copy_point_overlap_followup_20261102']=copy.deepcopy(back)
oldrow['source_record'].setdefault('other_metrics',{})['two_copy_point_overlap_followup_20261102']=copy.deepcopy(back)
ledger['rows'].append(row);ledger['record_count']=452;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
summary=f'''\n\n{marker}
### {now} 两份6804＋任意only-crossmatching整族NO，NB必要模型仍UNKNOWN

一个问题沿constantphase→ordinaryπ→NB→actualpoint球重叠推进，不拆四节点。328<567关恒定phase；普通π容量min573只是necessary可行，同π的NB最小547被反驳；唯一8秒NB模型4112nodes无incumbent，仍UNKNOWN，不能改写INFEASIBLE。

旧uniform6860被literal反驳；由81扩全部6804的新R2/R3最大B2=154/S2=140/B3=1588/S3=1434，正确U=6984。y0对6803个其他球心的13最小交集各20/总260；任意M取u=M^-1(0)，跨R4至多6724<6804，至少80漏点。保两actual6804源全部旧边、只加任意point-perfectmatching严格NO；partialcrossmatching可补全也NO。无需phase/affine/Aut/sourceD4假设；不排copy内oldold加边/改旧边/其他host/一般14D4。

line13.170781895/15CPU含格式错误和81→all6804修正，全部terminal。451→452一个实验，0新图/参数/Lean/独立方法；153/43/47、savedmain105/4/global0保持。sourceD4验证BFS0；人工15格top逐字保留、sameGoal ACTIVE/旧N8n61暂停。不续NBsolver/phase/permutation/copy梯；3645旧No读门与K19读准备不另计节点。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert m;oldexp=int(m.group(1));text=text[:m.start(1)]+str(oldexp+1)+text[m.end(1):]
 (W/name).write_text(text);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} 两6804任意only-crossmatching实际点覆盖NO

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (14,4)；主表L9720；13608仅目标，无图 | 恒phase328<567；普通π容量573仅可行、同πNB547被反驳；NB8秒4112nodes UNKNOWN仍保留。实际max球U6984减必然重复260得6724<6804，任意M至少漏80。 | 只排两actual6804保全旧边/only-crossdegree<=1的全或partialmatching。uniform6860已反驳不用，源D4/Aut/phase均无需。[最终实际证明](../{str((D/'FINAL_MATCHING_DISPOSITION_NOTE.md').relative_to(ROOT))}) |

451→452一个问题记录，不拆四方法；旧source节点仅backlink与uniform更正，旧hub UNKNOWN不覆盖。line13.170781895/15CPU保所有失败/扩scope；0sourceD4验证BFS/新图/参数/Lean，153/43/47不变。此only-crossmatching线STOP，其他oldold规则/host/一般14D4不排。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==452;assert all(after[k]==v for k,v in counts.items());assert (W/node).exists();assert sourcepath.read_text().startswith(sourcebefore)
receipt={'status':'PASS_ONE_TWO6804_ANY_MATCHING_POINT_OVERLAP_TERMINAL_NODE','updated_UTC':now,'records_before':451,'records_after':452,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'constantphase_ordinarypi_NB_pointoverlap_one_problem_node':True,'existing_source_node_minimal_backlink':sourceid,'old_source_status_hub_UNKNOWN_history_preserved':True,'index_experiment_count_before':oldexp,'index_experiment_count_after':oldexp+1,'graph_parameter_Lean_method_increments':[0,0,0,0],'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs','pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs','known_publicly_dominated_graph_examples']},'strongest_scope':'twoactual6804/alloldedgespreserved/onlycrossdegree<=1/arbitrarypointfullorpartialmatching','actual_maxima_B2_S2_B3_S3':[154,140,1588,1434],'uniform6860_refuted_not_used':True,'raw_union_upper':6984,'one_y0_witness':True,'other_z_count':6803,'thirteen_minimum_intersections':[20]*13,'mandatory_overlap':260,'cross_cover_upper':6724,'needed':6804,'NB_model_status':'UNKNOWN_NOT_INFEASIBLE_8SEC_4112NODES','NB_model_no_incumbent_preserved':True,'source_D4_or_Aut_phase_affine_assumptions_not_used':True,'sourceD4validation_BFS':0,'line_CPU':13.170781895,'line_CPU_cap':15,'all_processes_terminal':True,'human_top_blocks_preserved_exact':{p:True for p in files},'full_rebuild_reimport':False,'new_math_BFS_solver_field_Lean_ARIS_hash_runs':0,'root_STATE_ROUND_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-st,'row_path':str(rowfile.relative_to(ROOT)),'stop':True}
(S/'TWO6804_ANY_MATCHING_POINT_OVERLAP_TERMINAL_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
