"""One Loz1100 right-matching terminal record; no source/model/numeric execution."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200'
st=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-d9d4-two-loz1100-all-right-matchings2200-complete-no-20261102';marker='<!-- LOZ1100_ALL_RIGHTMATCHINGS_TERMINAL_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==454
assert not any(r['id']==slug or 'two1100_right_matching2200' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
oldrows=copy.deepcopy(ledger['rows']);counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
root=json.loads((D/'ROOT_DISPOSITION.json').read_text());r=json.loads((D/'RESULT.json').read_text());gate=json.loads((D/'READ_GATE.json').read_text());capacity=json.loads((D/'PHASE_CAPACITY.json').read_text());maxima=json.loads((D/'PHASE_ACTUAL_MAXIMA.json').read_text())
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_ALL1100_RIGHTMATCHINGS_STOP' and r['checked_t']==r['full_domain_size']==1100 and r['hit_t'] is None
assert r['capacity_P1_supported'] is False and r['full_cover_P2_supported'] is False
assert capacity['B_sizes']==[1,9,65,426] and min(capacity['relative_phase_upper_bounds'])==66 and maxima['maxima'][10]==43 and maxima['first_max_witness_t'][10]==115
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
names=['ROOT_DISPOSITION.json','NOTE.md','READ_GATE.md','READ_GATE.json','PAPER_INTERFACE.md','PRED.md','run_once.py','PHASE_CAPACITY.json','PHASE_ACTUAL_MAXIMA.json','ALL_T_RESULTS.tsv','RESULT.json','TERMINAL.json','ATTEMPT.json']
evidence=[str((D/p).relative_to(ROOT)) for p in names]
evidence += [gate['source']['recipe_input'],gate['saved_actual_support']['boundary_cache'],gate['saved_actual_support']['boundary_csv']]
assert all((ROOT/p).exists() for p in evidence)
raw={
'id':slug,'title':'9D4两Loz1100全1100右匹配NO：phase10有66端点对条目却最多43/55，真实重复覆盖受限',
'family':'Two-copy matching extension on a published Cayley source','idea_family':'idea:ddp-open-parameter-construction-20261026','date':'2026-11-02','wiki_verdict':'no',
'record_type':'fixed_Loz1100_two_copy_rightmatching_complete_endpoint_experiment_outside_stale15',
'target_Delta':9,'target_D':4,'savedL':1768,'baseline_date':'Parent currentprimarymain9D4=1768 inherited; no fresh search here',
'n':{'actual':None,'hypothetical':2200},'actual_graph_Delta':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':4,'new_lower_bound':False,
'actual_D_scope':'No2200candidategraph/fresh/BFS/Lean/ARIS. Complete1100rightt-domainactualcrossendpointsetsallfailD4; 2200/9900/degree9andmainmargin432areconditionalonly,notconstructionresults.',
'outcome_class':'ROOT_ACCEPTED_COMPLETE_NO_FIXED_LOZ1100_ALL_RIGHTMATCHINGS_STOP',
'scope':'FixedLoz1100RIGHT-lawCayleysource:H=C20 rightaction2 Z55,(j,x)(k,v)=(j+k mod20,x*2^k+v mod55),label55j+x,fixedS8. Preservebothsourcecopiesall8800oldedges;addone1100edgeperfectmatchingM_t(h)=h*t,all1100t. ThisisexhaustiveleftH-equivariantmatchingdomainonthissource,notarbitrarypointmatching/sourceedits/otherS/host/general9D4. Olderadjacentsingle-split1101andordinary5cover5500NOaredistinctscopesnotrerun. This9D4cellisnotinthe15stale-celllistanddoesnotincreaseitsvisitedcellcount.',
'distance_text':'P1预测某phase可用old-leg endpoint-pair容量<55，被实际全部phase最小66>=55反驳；容量通过不代表pointcover。P2预测存在真实fullU_t，也被全部1100t无hit反驳。闭球B0/B1/B2/B3 sizes1/9/65/426，B3直接取旧674个distance4边界标签补集，不重源R4/D4BFS；精确U_t=union_(a=0..3)B_a*t*B_(3-a)。relativephase10每t的候选端点对条目66，真实最多43/55，首max t115=(2,5)，故映像至少23重复/至少12缺点；66不是独立NB路线数。四phase可局部满55仍救不了phase10。native.795619759，总1.695619759/10CPU含read/prep/root，0新图/参数/Lean。',
'lesson_and_restart_condition':'STOPthisfixedLoz1100/allrightmatchingruleandcopy-rightmatchingladder. Hereunlikethe672source,rawsingle-phasecapacitydoesnotexclude;actualendpointcollisionsdo. Relativephase10failsforeveryt,sootherfourlocallyfullphasescannotcompensateandtotalbadscoretuningisnotjustified. PreserveP1/P2refutationsandspecificphasewitnessratherthanclaimnecessarycapacitysuccessasgraphprogress.',
'restart_condition':'Onlyanewauthorizedboundedstructuralquestionwithmeaningfullychangededge/matchingruleorhost;noautomaticotherS/source/action/twindow/solverladder. New4D5readgateisaseparateunrunquestionandnotthisrecord.',
'unclosed_gap':'Arbitrarynon-equivariantmatching,oldedgechanges,othergenerators/hosts/helpersandgeneral9D4remainunexcluded. Target2200hasnotbeenconstructedandmain1768isnotimprovedhere. Endpointpairmultiplicity66isnotindependentNBroutecount. Thisisoutsideold15cells;noold-cellcountincrement. GoalACTIVE/oldN8n61PAUSED.',
'positive_guarantees':[
'B3reuseisexactlysavedR4boundary674-labelcomplementin0..1099,ofsize426;onlyB0/B1/B2newfinitequery. NooldsourceD4/R4BFSvalidationrerun.',
'Closedballfour-termunion isequaltoexact-lengthsum<=3endpointunion;B0self/B1identityinclusionandnoncommutativeprefix*t*suffixorderarepreserved.',
'Atmost4crosscopywalksreducebyimmediatematchingbacktracktoonecross;commonleftHpreservesrightsourceedgesandM_t,soidentityU_ttestsallcrosspairs. SourceD4samecopypathsareinheritedandoldedgespreserved.',
'All1100twereactuallyvisitedonce,andall20phaseactualmaximaarefromthesamerun,notasecondUtpostprocessorparametersearch. P1andP2arebothhonestlyrefuted.',
'Phase10actualmax43/55atfirstt115with66rawpairentriesmakescollisionandmissing-pointobstructionsconcrete. FourlocalfullphasewitnessesarenotwholeU_tsuccess.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,'outside_stale15':True,'old_stale_cell_count_increment':0,
'source':{'n':1100,'m':4400,'degree':8,'D4':'inherited','law':gate['source']['law'],'label':gate['source']['label'],'positive_generators':gate['source']['positive_generators'],'inverse_generators':gate['source']['inverse_generators'],'oldsource_D4_BFS_reruns':0},
'hypothetical_only':{'n':2200,'m':9900,'maxdegree':9,'main_baseline':1768,'conditional_margin':432,'actual_graph':False},
'old_ball_interface':{'B_sizes':[1,9,65,426],'saved_distance4_boundary_count':674,'B3_complement_size':426,'source_R3_reused':True,'source_R4_BFS_reruns':0,'closed_four_terms_exact':True},
'complete_rightmatching_domain':{'size':1100,'actual_checked':1100,'fullUt_hits':0,'identityroot_via_common_leftH':True,'scope_not_arbitrarymatching':True},
'P1':{'prediction':'somephaseendpointpaircapacity<55','actual_min_capacity':66,'needed':55,'verdict':'REFUTED','all20_raw_capacities':capacity['relative_phase_upper_bounds']},
'P2':{'prediction':'atleastoneactualfullUt','actualhits':0,'verdict':'REFUTED_COMPLETE_DOMAIN'},
'phase10_bottleneck':{'raw_endpointpair_occurrences':66,'not_independent_NB_route_count':True,'actual_max_distinct_targets':43,'target_phase_size':55,'min_duplicate_images':23,'min_missing_targets':12,'firstmax_t_label':115,'firstmax_t_coordinates':[2,5]},
'allphase_actual_maxima':maxima['maxima'],'allphase_full55_t_counts':maxima['full55_parameter_counts'],'locally_full_phases':[4,7,13,16],'local_full_phases_not_global_repair':True,
'native_CPU':.795619759,'read_prep_charge':.8,'pre_root_CPU':1.595619759,'root_disposition_charge':.1,'final_case_CPU':1.695619759,'case_CPU_cap':10,'all_processes_terminal':True,'candidate_BFS_fresh_Lean_ARIS':0,'old_split_ordinary5cover_NO_notrerun':True,'no_automatic_otherS_source_or_twindow':True,'negative_Lean_required':False,'same_Goal':'ACTIVE','old_N8_n61':'PAUSED'
},'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'LOZ1100_ALL_RIGHTMATCHINGS_TERMINAL_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'LOZ1100_ALL_RIGHTMATCHINGS_TERMINAL_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'].append(row);ledger['record_count']=455;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n');node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} Loz1100全rightmatching NO：容量未排，phase10真实端点重复已排

两copy目标2200/9900/degree9相对main1768仅条件，无新图。本格是15老格外补充，不增oldcell计数。P1“某phase容量<55”被min66>=55反驳；P2“有fullU_t”被实际1100/1100参数无hit反驳。B3复用旧674个R4边界的补集426，closedball四项式/onecross/commonleftH给exactcross门，无源D4/BFS复验。

relativephase10每t有66个raw endpointpair条目却最多43/55（首t115=(2,5)），至少23映像重复/12缺点；66不是独立NB路线数。四phase可局部满也不能修该槽。只排固定Loz1100全部leftH-equivariantM_t(h)=h*t，不排任意matching/改旧边/general9D4。native.795619759、read/prep/root均纳final1.695619759/10CPU，STOP不换S/host/t梯。

454→455一个实验，0图/参数/Lean/fresh/ARIS，153/43/47与savedmain105/4/global0保持；旧454rows及人工15格top原文保留。GoalACTIVE/旧N8n61暂停，4D5只读门不混入。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert m;oldexp=int(m.group(1));text=text[:m.start(1)]+str(oldexp+1)+text[m.end(1):]
 (W/name).write_text(text);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} 15老格外9D4补充：Loz1100全1100rightmatching NO

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (9,4)；L1768；2200条件目标，无新图 | P1被mincapacity66>=55反驳，P2被全1100无fullUt反驳。phase10 raw66端点对映像max43/55，至少23重复/12缺点；非独立NB路线数。 | B3=旧674边界补集426复用，不重sourceD4/BFS；closedball四项/onecross/leftH给exact固定域。final1.695619759/10，STOP。[root终态](../{str((D/'ROOT_DISPOSITION.json').relative_to(ROOT))}) |

454→455一个实验，不增old15cell数；四局部满phase不能补phase10，其他matching/oldedge/host/general9D4未排。0新图/参数/Lean/fresh/ARIS，153/43/47保持，4D5读取不计此节点。人工top保持，GoalACTIVE/旧N8n61暂停。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==455 and after['rows'][:-1]==oldrows;assert all(after[k]==v for k,v in counts.items())
receipt={'status':'PASS_ONE_LOZ1100_FULL_RIGHTMATCHING_ENDPOINT_COLLISION_TERMINAL_NODE','updated_UTC':now,'records_before':454,'records_after':455,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),'index_experiment_count_before':oldexp,'index_experiment_count_after':oldexp+1,'full_rightmatching_domain_checked':1100,'fullUt_hits':0,'P1_capacity_short_prediction':'REFUTED_MIN66_AT_LEAST55','P2_fullUt_exists_prediction':'REFUTED_NO_HIT_ALL1100','phase10_raw_endpointpair_entries':66,'phase10_actual_max':43,'phase_size':55,'duplicate_images_atleast':23,'missing_targets_atleast':12,'raw66_not_independent_NB_routes':True,'B3_reused_size':426,'old_saved_R4_boundary_size':674,'source_D4_BFS_reruns':0,'final_case_CPU':1.695619759,'casecap':10,'outside_stale15':True,'oldcell_count_increment':0,'graph_parameter_Lean_method_increments':[0,0,0,0],'candidate_BFS_fresh_Lean_ARIS':0,'all_old454rows_preserved_exact':True,'human_top_blocks_preserved_exact':{p:True for p in files},'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']},'4D5_readgate_included':False,'full_rebuild_reimport':False,'new_math_solver_BFS_Lean_paid_hash_runs':0,'root_STATE_ROUND_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-st,'stop':True}
(S/'LOZ1100_ALL_RIGHTMATCHINGS_TERMINAL_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
