"""One aggregate B research node; only existing accepted evidence, no math runs."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate'
st=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-binary-multiroute-packets-c30-insertion-c33-triangle-family-terminal-20261102';marker='<!-- BINARY_MULTIROUTE_PACKETS_AND_CONTROLLER_FAMILIES_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==455
assert not any(r['id']==slug or 'controller32_F2_multiroute_readgate' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
oldrows=copy.deepcopy(ledger['rows']);counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
root=json.loads((D/'ROOT_DISPOSITION.json').read_text());adj=json.loads((D/'adjacent_packet_controlled_test/RESULT.json').read_text());repair=json.loads((D/'conjugate_route_repair/RESULT.json').read_text());ins=json.loads((D/'typed_C30_to32_twochart_insertion/RESULT.json').read_text());cap=json.loads((D/'typed_C30_to32_twochart_insertion/BASE_CAPACITY_RESULT.json').read_text());surv=json.loads((D/'typed_C30_to32_twochart_insertion/CAPACITY_SURVIVOR_RESULT.json').read_text());tri=json.loads((D/'uniform_triangle_C33_C11/RESULT.json').read_text());proj=json.loads((D/'uniform_triangle_C33_C11/PROJECTION_POSTPROCESS.json').read_text())
assert root['case_CPU']==5.653785158 and root['all_numerics_terminal'] and not root['graph_generated']
assert ins['native']['raw_controllers_checked']==378450 and ins['native']['simple_controllers']==284310 and cap['survivors']==15 and surv['global_capacity_survivors']==[]
assert tri['normalized_parameters_checked']==100 and tri['all_self_controller_fibres_pass'] and proj['controller_D3_survivors']==0 and proj['maximum_of_min_type_reach']==32
oldbinary=next(r for r in ledger['rows'] if r['id']=='ddp-wave5-binary-route-chart3')
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
evidence=[]
for parent,names in [
(D,['ROOT_DISPOSITION.json','NOTE.md','READ_GATE.md','READ_GATE.json','EXISTING_C30_BINARY_CHART_INPUT.md','EXISTING_C30_BINARY_CHART_INPUT.json','CAYLEY32_QUOTIENT_GATE_PAPER.md','ADJACENT_BINARY_PENCIL_PAPER.md','C30_TO32_TWO_PORT_INSERTION_FAMILY_PAPER.md','CONTROLLER32_PACKET_PRUNING_PAPER.md','B_FAMILY_TERMINALS_SCOPE_ATTACK.md']),
(D/'adjacent_packet_controlled_test',['PRED.md','run_once.py','FROZEN_CONTROLLER_ROUTES.json','RESULT.json','TERMINAL.json']),
(D/'conjugate_route_repair',['PRED.md','run_once.py','RESULT.json','TERMINAL.json']),
(D/'typed_C30_to32_twochart_insertion',['PRED.md','run.cpp','run_once.py','INPUT_CONTROLLER.txt','ALL_INSERTION_RESULTS.tsv','RESULT.json','TERMINAL.json','BASE_CAPACITY_PRED.md','base_capacity.cpp','BASE_CAPACITY_RESULT.json','BASE_CAPACITY_EACH_PARAMETER.tsv','BASE_CAPACITY_SURVIVORS.tsv','CAPACITY_SURVIVOR_PRED.md','capacity_survivors_once.py','CAPACITY_SURVIVOR_RESULT.json','CAPACITY_POSTPROCESS_SCOPE_ATTACK.md']),
(D/'uniform_triangle_C33_C11',['PAPER_INTERFACE.md','PRED.md','run_once.py','ALL_PARAMETER_RESULTS.json','RESULT.json','TERMINAL.json','derive_projection_from_saved_rows.py','PROJECTION_POSTPROCESS.json'])]:
 for n in names:evidence.append(str((parent/n).relative_to(ROOT)))
assert all((ROOT/p).exists() for p in evidence)
raw={
'id':slug,'title':'F2³多路线B：真实三平面packet覆盖8；局部修复有代价，C30插点与C33三角两族已停',
'family':oldbinary['method_family'],'idea_family':'idea:ddp-open-parameter-construction-20261026','date':'2026-11-02','wiki_verdict':'partial',
'record_type':'controlled_binary_affine_route_packets_and_two_base_family_exclusion_research',
'target_Delta':8,'target_D':3,'savedL':253,'baseline_date':'Inherited main8D3=253; no new public comparison or graph claim',
'n':{'actual':None,'hypothetical':None},'intended_final_target':{'degree':8,'D':3,'controller_orders':[32,33],'conditional_lift_orders':[256,264]},
'actual_graph_Delta':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':3,'new_lower_bound':False,
'actual_D_scope':'LocalactualC30packet/imagechecksandbasecontrollercapacity/projectionexperimentsonly. No complete256/264targetgraph generated,graphBFS,Lean,ARISorsolver. C32insertionfamilyNOisanyuniform8fiber/atmost2outputspertypedstepliftunderitsfixedadjacency;C33specifiedbasefamilyitselfD>3 andanysurjectiveprojectedliftNO. NotgeneralC32/C33/8D3.',
'outcome_class':'LOCAL_MULTIROUTE_POSITIVE_TWO_SPECIFIC_CONTROLLER_FAMILIES_COMPLETE_NO_NO_TARGET_GRAPH',
'scope':'One B research chain,notindependentmethodorgraphcounts. Inherituniversal197568fourinverseglobalcharts/all36singlefullrankNOwithoutturningitintomultirouteNO. ActualC30adjacentpairpacket/control,one021conjugaterepair,fulltypedC30-to32twochartinsertiondomainthenordinarycapacityextension,anduniformthree-type/C11triangleC33familyarelinkedbychangedgenerationrules. C32strongNOonlyspecificsimpletypedinsertionswithuniform8fibres/everytypedstep<=2outputs/onlythatcontrolleradjacency;C33strongNOonlyp,q,rnonzero uniformthree-typeC11voltagebasefamilyandanysurjectiveprojectedlift(holdingallowed),notallC33. PaperCayley32NOonlytwoglobalinversepairs interface,notall4regularCayleyorallC32.',
'distance_text':'此前未知低秩actualroutes能否在同controllerpair补足：C30 0→18的ARC三rank2 packet对全部8sourcex并满8；合法COLLINEAR仅packet6/完整9routes7，真实逆均通过，非只x0。改唯一021的0→5 route使ARC4→R8且adj保8，但修4conjugates同时损4cyclic，goodword24→28预测反驳：两chart同24。按此改typedC30插两点，378450raw/284310simple两chart全在root30失败。ordinaryΣ2^l保存行门含backtracks给root30 min0:283388/min4:907/min8:15，反驳全root30不足预测；仅15追加root31后全部min0，关闭此族任意8fiber<=2choice lift，不能说907base本身D>3。再改三角拓扑C33/C11，p1/q,r非零100规范代表/1000raw，self fibres全通过但每参数至少一type三步reachable<33，projection0存活/max min32，关闭该base族所有projectedlifts。总5.653785158/30含初read1.6对计划1.5超.1原样继承；0完整目标图/参数/Lean。',
'lesson_and_restart_condition':'Inheritactualfourarccompleted-inverseadjacentpencilruleandtheneedforrealclosedroutepacketstocoverthesamefibre. Local021repairhasatradeoff,notglobalwordscoreimprovement. The15root30capacitysurvivorsrefutedanoverstrongpredictionandwerecheckedonlyatroot31;C33self-fibrecoverwassupportedbutbaseprojectionclosedallparameters. STOPbothspecificfamilies/matrixtuning;donotswapchartoncontrollersalreadyexcludedbycapacity/projection. NoautomaticC34/m12/field/chartladder.',
'restart_condition':'A future separatelyboundedquestionmustchangeactualcontrollertopology/interfaceoutsideclosedfamiliesandretaintrueinverse/actualendpointunions;notgeneralfieldorcontrollerscreening. Keepcontrolledpositivesandnegativeprojectionstrengthseparate.',
'unclosed_gap':'GeneralN(8,3),nonCayleyC32,otherC32/C33topologies,otherportinterfacesandmultirouteaffinemechanismsremainunexcluded. Do notgeneralizeC32min4casesasbaseD>3,norapplyC33arbitrary-liftstrengthtoC32. Cayley32paperisnotallinverse-closed4generatorinterfaces. Allcomplete-targetgraph/formal/globalrecordclaimsremainabsent. A4D5Hallnodeisalreadyupdatedelsewhere;new650readonlygateisnotthisnode. GoalACTIVE/oldN8n61PAUSED.',
'positive_guarantees':[
'Theactualthree-rank2packetisboundtoexistingC30pair0to18andall8sourcecoordinates,withfullforward/reversecontract;abstractx0pencilwasnotmistakenforanactualglobalgraph.',
'ActualC30pair0to5hasuniqueword021;therepairedRchartcovers8insteadof4thereandpreservesadjacent8,butfourimprovedandfourbrokenwordrankskeepbothgoodcounts24.',
'C32ordinarywalkcapacityusesalllengths0..3with2^lweightincludingcontrollerbacktracks;anyuniform8fibreliftlimitedtotwopointchoicespertypedstepcannotexceedit. The15necessarysurvivorsalonegetonefreshroot31query;root30notrepeated.',
'C33commonC11translationmakesthreetyperootssufficient;unitscalingnormalizesnonzeropto1,so100q/rrepresent1000rawnonzerotripleswithoutclaimingnonisomorphism. All100savedroot-tripletsneededforprojectiondeductionwerealreadycomputed.',
'Paperadjacentfourarcpencilrequiresactualcompletedreverseadjacency/outputoffsetcontract,notjustdirectionequality;itsgeneralformdoesnotrequireinvertibleA. Cayley32twoglobalinversepairsNo usesC2²kernel8/atmost5reachable,cyclic25<32;otherportinterfacesnotclosed.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,'single_aggregate_research_record':True,'old_universal_binary_chart_node':oldbinary['id'],'old_all36_single_rank3_NO_preserved':True,
'actual_adjacent_packet':{'controller_pair':[0,18],'all_actual_le3_routes':9,'ARC_three_packet_ranks':[2,2,2],'ARC_packet_counts_each_source':[z['packet_covered'] for z in adj['charts']['ARC']['source_rows']],'ARC_allroute_counts_each_source':[z['all_routes_covered'] for z in adj['charts']['ARC']['source_rows']],'COLLINEAR_packet_counts_each_source':[z['packet_covered'] for z in adj['charts']['COLLINEAR']['source_rows']],'COLLINEAR_allroute_counts_each_source':[z['all_routes_covered'] for z in adj['charts']['COLLINEAR']['source_rows']],'complete_inverse_both':True,'not_only_zero_source':True},
'conjugate_repair':{'pair':[0,5],'soleword':[0,2,1],'all8sources_ARCcoverage':4,'all8sources_Rcoverage':8,'adjacent_all8_preserved':True,'old_and_repaired_goodwords':[24,24],'prediction24to28':'REFUTED','improved_words':repair['improved_words'],'broken_words':repair['broken_words']},
'C32_insertion_family':{'generator':'C30typedA/Bpermutations; two distinctAdarttailsi<j,two distinctBdarttailsorderedk!=l; bothinsertnew30/31; simplequarticfilter','raw_parameter_configs':378450,'simple_configs':284310,'nonsimple_configs':94140,'configuration_counts_not_nonisomorphic_graph_counts':True,'two_fixed_charts':['ARC','R'],'chart_checked':[284310,284310],'allpoint_firstfails_root30':True,'ordinarycapacity_root30_hist':{'0':283388,'4':907,'8':15},'prediction_all_root30_capacity_fail':'REFUTED_BY15','only15_root31_queried':True,'all15_root31_minimum':0,'root31_firstbad_can_be4_while_minimum0':True,'global_capacity_survivors':0,'strong_NO_scope':'allthissimpletypedC30to32controllers;uniform8fibres;eachtypedstep<=2outputs;onlytheseprojectedtypededges;linearornonlinear/edge-local','not_proved_907_basegraphs_Dgreater3':True,'not_allowing_unbudgeted_extra_holding_or_nonadjacent_base_edges':True},
'C33_uniform_triangle_family':{'base':'(tau,j),tau0..2,j∈C11;A0j->1j->2j->0(j+p);B0j->2j,1j->0(j+q),2j->1(j+r);trueinverseports','parameters':'p,q,r allnonzero;unitnormalizep1','normalized_checked':100,'raw_nonzero_triples_represented':1000,'representatives_not_claimed_nonisomorphic':True,'all_self_controller_fibres_pass':True,'first_fibre_bad_is_projection_count_historical':43,'projection_postprocess_savedrows':100,'all3type_root_summaries_already_saved':True,'each_parameter_atleast_one_type_reach_less33':True,'some_type_roots_can_reach33':True,'maximum_of_min_three_type_reach':32,'controller_D3_survivors':0,'base_family_Dgreater3':True,'strong_NO_scope':'anysurjectiveprojectedliftwithnonemptybasefibres;holdingallowed;noedgesprojecttononadjacentbasevertices','not_generalC33_or_8D3':True},
'paper_filters':{'Cayley32_two_global_inverse_pairs':'STRICT_NO_ONLY_SPECIFIEDa±/b±INTERFACE','noncyclic_order32_quotient':'C2^2,kernel8,<=3reachablekernelatmost5','cycliccase_endpointupper':25,'not_all4regularCayley32_claim':True,'adjacent_fourarc_pencil':'threeactualrank2planescoverF2^3forallsourcesundercompletedreversecontract','true_reverse_more_than_direction_identity':True,'general_adjacent_pencil_does_not_require_Ainvertible':True},
'original_read_conservative_CPU':1.6,'original_read_planned_cap':1.5,'original_read_over_plan_preserved':.1,'whole_B_case_CPU':5.653785158,'B_case_cap':30,'all_numeric_stages_terminal':True,'full_target_graphs_generated':0,'graph_BFS_Lean_ARIS_solver':0,'controlled_binary_matrix_image_experiments_performed':True,'same_Goal':'ACTIVE','old_N8_n61':'PAUSED'
},'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];row['object_level']='controlled_route_packets_and_base_family_exclusions_no_complete_lift';assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'BINARY_MULTIROUTE_PACKETS_AND_CONTROLLER_FAMILIES_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'BINARY_MULTIROUTE_PACKETS_AND_CONTROLLER_FAMILIES_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'].append(row);ledger['record_count']=456;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n');node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} 二元多路线B：真实局部覆盖成立，两controller生成族已停止

C30 0→18实际ARC三rank2 packet对全部8x并满8，合法COLLINEAR仅6/完整9routes7；不是只查x0。针对唯一021把0→5的4改8、adj保8，但修4conjugates损4cyclic，goodword24→28预测被反驳，两chart同24。旧全36单rank3 NO不等于multiroute NO。

改typedC30插两点：378450raw/284310simple，两chart全失败。ordinaryΣ2^l保存行容量root30为283388 min0、907 min4、15 min8，反驳“root30全不足”；仅15再看root31全min0，关闭该插边族任何8fiber/每typedstep<=2输出lift。不能说907个base本身D>3。再改C33/C11三角：100规范/1000raw非零参数，self fibres全pass，但每项至少一type三步reach<33，projection0存活/max min32；故此base族D>3，任意surjective projectedlift也NO，强度不同于C32。

Cayley32两globalinversepairs paperNO、真实reverse/fourarc相邻pencil可继承，不扩一般C32/C33/8D3。B全case5.653785158/30，含初read1.6对计划1.5超.1原样继承；0完整目标图/参数/Lean/图BFS/ARIS/solver。455→456仅一个聚合研究记录，不数独立方法；153/43/47保持，人工top及所有旧455rows原样。A已另行原位完成不重复，新650只读门不混入。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert m;oldexp=int(m.group(1));text=text[:m.start(1)]+str(oldexp+1)+text[m.end(1):]
 (W/name).write_text(text);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} B聚合研究：局部多route互补与两种不同强度的族NO

| 研究／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (8,3)；L253；条件目标C32×8=256/C33×8=264，均无完整图 | ARC实际三rank2 packet全8x并满8；021局部4→8但goodword仍24。C32插边284310simple全被<=2choice/8fiber容量门排；C33/C11 100规范投影0存活，baseD>3。 | C32不等于每个baseD>3（907 min4），C33可排anysurjectiveprojectedlift；均仅指定族。原读超计划.1在总5.653785158/30内继承。[root终态](../{str((D/'ROOT_DISPOSITION.json').relative_to(ROOT))}) |

455→456一个研究记录，不是方法或新图数。局部同层/相邻覆盖认识真实改变了生成器，但不以局部成功结Goal；无完整图/参数/Lean/图BFS/ARIS/solver，153/43/47保持。STOP两个族和矩阵续调，一般8D3/其它controller拓扑仍未排；人工top保持，GoalACTIVE/旧N8n61暂停。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==456 and after['rows'][:-1]==oldrows;assert all(after[k]==v for k,v in counts.items())
receipt={'status':'PASS_ONE_BINARY_MULTIROUTE_CONTROLLED_PACKETS_AND_TWO_FAMILIES_RESEARCH_NODE','updated_UTC':now,'records_before':455,'records_after':456,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),'index_experiment_count_before':oldexp,'index_experiment_count_after':oldexp+1,'actual_ARC_packet_all8sources_union8':True,'legal_COLLINEAR_packet6_allroutes7':True,'021_local4to8_adj8_but_good24to28_refuted':True,'C32_raw':378450,'C32_simple':284310,'root30_capacity_histogram':{'0':283388,'4':907,'8':15},'root30_allfail_prediction_refuted_by15':True,'only15_root31_min0':True,'C32_strict_scope':'specificsimpletypedC30insertions;anyuniform8fiber/<=2outputspertypedsteplift','C32_907_not_claimed_baseDgreater3':True,'C33_norm':100,'C33_raw_represented':1000,'C33_self_fibres_allpass':True,'C33_projection_survivors':0,'C33_max_min_type_reach':32,'C33_strict_scope':'uniformthree-typeC11nonzero-voltagebasefamilyD>3;anysurjectiveprojectedlift','paper_Cayley32_and_trueinverse_pencil_scope_preserved':True,'whole_B_case_CPU':5.653785158,'B_casecap':30,'original_read1p6_over1p5_point1_preserved':True,'graph_parameter_Lean_method_increments':[0,0,0,0],'full_target_graph_BFS_Lean_ARIS_solver':0,'all_old455rows_preserved_exact':True,'A_node_not_redone':True,'new650_readgate_included':False,'human_top_blocks_preserved_exact':{p:True for p in files},'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']},'full_rebuild_reimport':False,'new_numeric_field_rank_word_solver_BFS_Lean_paid_hash_runs':0,'root_STATE_ROUND_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-st,'stop':True}
(S/'BINARY_MULTIROUTE_PACKETS_AND_CONTROLLER_FAMILIES_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
