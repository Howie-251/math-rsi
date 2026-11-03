"""Persist one CM253 mechanism terminal and update its existing delivery pages."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,csv,io,json,re,runpy,time

START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='CM253_STAR_REPAIR_TERMINALS_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=S+'stale_record_transfer_d8D3/source253_fourcut_star254_gate/'
rid='ddp-stale-d8d3-cm253-star-and-fivecut-one-repair-coupled-no-20261101'

def read(p):return json.loads((R/p).read_text())

root=read(P+'ROOT_DISPOSITION.json');proof=(R/P/'FINAL_PROOF.md').read_text()
gate=read(P+'GATE_RESULT.json');repair=read(P+'REPAIR_RESULT.json')
coupled=read(P+'COUPLED_RESULT.json');terminal=read(P+'COUPLED_TERMINAL.json')
assert root['status'].startswith('ROOT_ACCEPTED') and len(proof)>2000
assert gate['all_four_classes_strict_three_edge_capacity_NO']
assert [r['distinct_normalized_path_obligations']for r in gate['profiles']]==[27]*4
assert [r['maximum_single_otheredge_hits']for r in gate['profiles']]==[6]*4
assert [r['three_otheredges_upper_bound']for r in gate['profiles']]==[18]*4
assert not repair['prediction_supported'] and not repair['all_four_classes_strict_capacity_NO']
assert [r['combined_capacity_upper_bound']for r in repair['profiles']]==[35]*4
assert [r['max_repair_hits']for r in repair['profiles']]==[11]*4
assert coupled['complete_global_coupling_scan'] and coupled['global_capacity_NO']
assert [r['repairs_checked']for r in coupled['profiles']]==[30378]*4
assert [r['legal_halfchoices_checked']for r in coupled['profiles']]==[1910136]*4
assert [r['maximum_base_hits']for r in coupled['profiles']]==[12]*4
assert [r['base_plus_two_fullcuts_upper']for r in coupled['profiles']]==[24]*4
assert coupled['selected_R_halfchoices']==coupled['actual_final_candidate_count']==0
assert coupled['newroot_BFS_count']==coupled['oldroot_BFS_count']==0
assert terminal['terminal'] and terminal['active_processes']==0
assert abs(coupled['wholecase_CPU_seconds']-3.686201072)<1e-10
assert coupled['source_D3_BFS_field_words_revalidation']==0
followup=read(S+'STALE_FOLLOWUP_ROUND_20261101.json')
tested=followup['shortlist_cells_tested_this_round']
assert len(tested)==12 and [8,3]in tested
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count']
records={r['id']:r for r in L['rows']};assert len(records)==before
assert rid not in records and not(W/'experiments'/f'{rid}.md').exists()
assert not any('cm253' in r['id']and('repair' in r['id']or'fourcut'in r['id'])for r in L['rows'])
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances',
 'saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs',
 'pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs',
 'known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)

names=['HISTORY_SOURCE_GATE.json','PRED.md','NOTE.md','TERMINAL.json','SCOPE_ATTACK.md',
 'PAPER_WITNESS_GATE.md','GATE_PRED.md','gate_once.py','GATE_ALL1012_WITNESS_PROJECTIONS.json',
 'GATE_RESULT.json','GATE_TERMINAL.json','GATE_NOTE.md','GATE_HANDLE.json',
 'PAPER_OLDOLD_REPAIR_GATE.md','REPAIR_PRED.md','repair_capacity_once.py',
 'REPAIR_RESULT.json','REPAIR_TERMINAL.json','REPAIR_NOTE.md','REPAIR_HANDLE.json',
 'COUPLED_PRED.md','run_coupled_once.py','coupled_once.cpp','COUPLED_INPUT.txt',
 'COUPLED_ALL_REPAIR_HALF_MAXIMA.tsv','COUPLED_CANDIDATE_STAGES.tsv',
 'COUPLED_NATIVE_RESULT.json','COUPLED_RESULT.json','COUPLED_TERMINAL.json',
 'COUPLED_NOTE.md','COUPLED_HANDLE.json','FINAL_PROOF.md','ROOT_DISPOSITION.json']
for i in range(4):
 names += [f'GATE_TYPE{i}_OBLIGATIONS_AND_CLASSES.json',f'GATE_TYPE{i}_ALL997_EDGE_MASKS.tsv',
  f'REPAIR_TYPE{i}_CLASSES_AND_WITNESSES.json',f'REPAIR_TYPE{i}_ALL_NONEDGE_MASKS.tsv']
paths=[P+x for x in names]
paths += ['research/ddp/breadth_20261027_wave10/degree_reduction_scout/'+x for x in
 ['screen.py','source253_to_degree7.json','source253_to_degree7.forced_edges.json']]
assert all((R/x).is_file()for x in paths)
raw=dict(id=rid,
 title='CM253→254：四cut八星27vs18；一repair独立35未排，完整耦合24<27关闭五cut规则',
 family='Cached unique-route obligations for local star and old-edge repair',
 idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',wiki_verdict='no',
 record_type='fixed_host_edge_edit_star_and_one_repair_experiment',
 target_Delta=8,target_D=3,savedL=253,
 baseline_date='Inherited cached primary CM253 by Comellas–Mitjana,1994-08; no new public search or source-D3 verification',
 n=dict(actual=None,hypothetical=254),actual_graph_Delta=None,actual_D=None,
 actual_D_scope='No254candidategraphorBFS. Strictnecessarycached-oldroutegatesexcludeexactlocalrules;noordinarybadpaircountoractualcandidate diameterwasmeasured.',
 ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,new_lower_bound=False,
 outcome_class=root['status'],
 scope='OnlyactualfixedCM253simple8regularD3source,RIGHTC11semidirect-action9C23/label23phase+normal. NumericalscopeA:deletefourvertex-disjointoldedgesandjoinonevertextoalleightendpoints. NumericalscopeB:deletefivevertex-disjointoldedges,addoneoriginal-source-nonedgeRbetweentwoomittedendpointsfromdifferentcuts,andjoinonevertextotheremainingeightendpoints;allotheroldedgesretained. PaperextensionA:deleteany<=5distinctoldedges,sharedendpointsallowed,andaddonevertexwithonlynewoldedgesatmaxdegree8,noaddedoldoldrepair. Notgeneral8D3,arbitraryonepointrewiring,multiplehelpersorallrepairpatterns.',
 distance_text='有效旧unique3缓存每edge一条，1012项按实际positive方向/整路反转/LEFT平移后，每firstclass27项不同义务，首中末各9；不是全部criticalmatrix。四cut纯星预测支持：全1012边滤首端点15余997，单边maxhit6，余三边18<27。改变为五cut＋一原非边repair后，四类各30378repair，maxrepair11/单vertexmax6，独立容量24+11=35≥27，容量不足预测被推翻，不能判NO或存在。随后绑定R与两halfcut邻端：四类各30378repair/1910136合法halfchoices完整，base=repairMask|V(a′)|V(b′)最多12；余两fullcut最多12，24<27，耦合预测支持，指定五cut一repair全NO。总7640544halfchoices是有限参数域，非独立图数；frozenR及firstargmax只为返回证据，0selected-R候选搜索/图/BFS。纸面directhit另排任意≤5distinctcuts可共享的纯星；不把最多10pin全星称合法max8图。累计3.686201072/20CPU，含read.8/reader.25及编译，sourceD3/unique3/field/旧degree-reduction重跑0。',
 lesson_and_restart_condition='STOPCM253localstar/fivecut-one-repairline. Independentrepaircapacity35wasnotacompatibleconstruction;couplingtherepairwiththetwoactualhalfcutneighboursloweredjointcapacityto12,showingexactlywhichindependentmaximacannotcoexist. Preservefirst/middle/lastwitnessrolesandvalid-subsetsemantics. DonotcontinueR2,morecut/repair/source/sameoldtimerautomatically. NextrootquestionchangesgenerationtotheC8semidirect-action3Z32order256Cayleyrecipe:historyreadcomplete;20CPUfinitewordgateauthorized,nographorresultclaimed.',
 restart_condition='Anewconcreteboundedroute-compensationmechanismoutsideclosedpure<=5deletionstarorclosedfive-disjointcuts/oneomitted-endpointrepairscope;neitherfailedoldtimernorindependentcapacityslackauthorizesanotherbatch.',
 unclosed_gap='Otherrepairplacementpatterns,multipleoldoldrepairs,morecuts,otherhosts,multiplehelpersandgeneralN(8,3)remainunexcluded. Direct256Cayleyquestionhasnogeneratedoracceptedgraphatthischeckpoint. No graph/parameter/Lean/independentmethodincrement;GoalACTIVE.',
 positive_guarantees=[
  'Inheritedcachedwitnessesareactualsourceunique3geodesics;eachlegitimateLEFTprojectionremainsanecessaryoldrouteobligation. PassingthissubsetwouldnotcertifyD3.',
  'First/middle/lastcutpositionsarepreserved:middlehitsetisoldpairendpoints;first/lastusefarclosedB1,notjustthefarendpoint.',
  'Repairmaskallowsallleglengthsplits0+2,2+0,1+1inGminusfirstcutandignoresothercuts,soitisasafenecessaryupperbound.',
  'A<=3oldoldroutecannotusebothnewstarandRbecauseRendpointsareomittedfromthestarpins;coupledbaseplusremainingfullcutmaskscontainsallpossibleobligationrepairs.',
  'Paperpure<=5cutextensionusesdirectnecessaryhitandincident-edgedominance;itdoesnotrequireadegree10fullstarasalegalmax8graph.'
 ],
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
  source_n=253,source_m=1012,source_degree=8,source_D3_inherited=True,
  source_RIGHT_recipe='C11semidirect-action9C23,h*s,label23phase+normal',
  cached_unique3_unordered_pairs_inherited=9108,cached_peredge_witness_records=1012,
  cached_unique3_status='INHERITED_NOT_REVALIDATED',canonical_obligations_per_class=[27]*4,
  canonical_first_middle_last_counts=[9,9,9],full_middlecritical_matrix_computed=False,
  early_full_middle_matching7_hypothesis='REFUTED_AT_LEAST_ONE_ON_PAPER_NOT_BY_PARTIAL_CACHE',
  paper_middle_matching7_refutation='InheritedVTdistance2dataforcenotrianglesandsome4cycle;acutonthe4cyclehasisolatedmiddlerowandcolumn',
  subset_middle_matching_sizes=[3]*4,
  complete_source_edge_domain=1012,filtered_first_incident_edges=15,eligible_otheredges=997,
  zero_mask_edges=[328]*4,edge_mask_classes=[166]*4,max_otheredge_hits=[6]*4,
  fourcut_otherthree_upper=[18]*4,fourcut_capacity_prediction_supported=True,
  repair_domain_per_class=[30378]*4,repair_mask_classes=[196]*4,repair_zero_masks=[28032]*4,
  max_repair_hits=[11]*4,max_vertex_hits=[6]*4,independent_star_upper=24,
  independent_repair_star_upper=[35]*4,independent_capacity_NO_prediction_supported=False,
  independent_upper_not_construction_or_NO=True,
  all_coupled_halfchoices_per_class=[1910136]*4,coupled_halfchoices_total=7640544,
  coupled_type_repair_total=121512,coupled_base_max=[12]*4,
  remaining_two_fullcuts_upper=12,coupled_total_upper=[24]*4,required_obligations=[27]*4,
  coupled_capacity_NO_prediction_supported=True,complete_global_coupled_scan=True,
  first_global_argmax=dict(type=0,repair=[5,37],half_neighbours=[211,79],base_hits=12),
  firstargmax_not_frozen_candidate_search=True,selected_R_halfchoices=0,
  actual_final_candidate_count=0,newroot_BFS_count=0,oldroot_BFS_count=0,
  candidate_field_names_with_minus1_are_unused_sentinels=True,
  paper_pure_star_extension='any<=5distinctolddeletions/sharedendpointsallowed/onevertexonlynewold/max8/nooldoldrepair',
  paper_pure_star_not_full10pin_legalstar_argument=True,
  source_literal_input_parses_by_stage=dict(gate=1,repair=1,coupled=1),
  source_D3_BFS_unique3_field_degree_reduction_revalidation=0,
  wholecase_CPU_seconds=3.686201072,wholecase_CPU_cap_seconds=20,
  reader_charge_CPU_seconds=.25,reader_charge_in_case_not_added_twice=True,
  all_processes_terminal=True,Lean_solver_paidreview_runs=0,
  next_question='C8semidirect-action3Z32/order256Cayleyhistoryreadcomplete;20CPUfinitewordgateauthorized,noactualgateorgraphresultclaimed',
  same_Goal='ACTIVE',old_N8_n61='PAUSED'),evidence_paths=paths)

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
records[rid]=n;L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[ROOT证据](../'+P+'ROOT_DISPOSITION.json) |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text()
needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' CM253局部星与一repair终态（一个实验节点）\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n四cut八星27vs18严格NO；加入一旧旧repair后独立35≥27，原容量不足预测被推翻，彼时OPEN保留为历史。实际耦合全部4×1910136半选择后base≤12，加余两完整边≤12，总24<27，指定五不交cut＋一原非边repair＋八星完整NO；没有进入候选或BFS。纸面directhit另排任意≤5distinctcuts可共享＋纯星，不用度10全端点星作max8合法图。停止CM局部线；不排其它repair/multiplehelpers/hosts/general8D3，不自动续。12格本轮新检验、老15格0新增达标图；全项目153/43/47和savedmain105/4/global0保持。下一order256Cayley排重只读已完成、20CPU有限wordgate已授权，但无actual结果。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新终态：CM253局部补点停止，改查256点Cayley连接规则\n\n旧1012逐边unique3证据正确按首中末投影，每类27义务。四cut八星的余三边≤18，预测支持。改变为五cut＋一原非边repair后独立上界24+11=35，容量不足预测被推翻；不能据此判NO或存在。再绑定同一repair与两halfcut邻端，四类各30378repair/1910136合法halfchoices全部完成，base≤12，再加余两fullcut≤12，24<27，耦合预测支持，指定全族严格NO。0实际254候选/图/BFS，首argmax只是容量返回证据。\n\n纸面directhit另排固定CM253任意≤5distinct旧边删除（可共享端点）＋单纯星；N须来自freedendpoints，不含oldoldrepair，不使用可能度10的全端点星作合法max8图。修复端点和星覆盖的独立最大不能同时实现，故暂停CM局部加点，不续R2/cut/repair/source梯。不排其它repair、多helper、其他host或一般8D3。累计3.686201072/20CPU，旧sourceD3/unique3/field/degree-reduction重跑0。\n\n12格本轮有新实际检验，15格老题仍0新达标图。'+str(before+1)+'条记录（非方法），153图／43参数／Lean47、savedmain105/4/global0保持。下一C8⋉3 Z32／256点Cayley排重只读完成、20CPU有限wordgate已授权，尚无实际结果或图。人工15格顶部、sameGoal ACTIVE、旧N8/n61暂停与人工反馈要求保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={};index_before=None
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre)
 text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;index_before=int(m[1])
  text=text[:m.start()]+f'## Experiments ({index_before+1})'+text[m.end():]
  pos=text.index('\n',m.start())+1;text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': oneCM253localedge-editexperiment. Fourcutstar27vs18NO;independentrepaircapacity35refutedNOguess;fullcoupled4x1910136halfchoicesbase12+12=24<27closesfive-disjointcuts/oneomitted-endpointnonedgeR/8star. Paperdirecthitclosesany<=5distinctcuts/sharedendpoints/purestarwithoutfull10pinlegalstarassumption. No graph/BFS/field/oldunique3/reviewrerun,case3.686201072/20CPU,153/43/47unchanged,human15top preserved,12cellsnewtested. Nextorder256Cayleyreadonlynotresult;no fullrebuild.')

# Rebuild the existing 15-row delivery from its one builder, never a second list.
builder=runpy.run_path(str(R/S/'build_stale_record_page.py'))
with contextlib.redirect_stdout(io.StringIO()):builder['build']()
candidate=read(S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json')
assert len(candidate['rows'])==15 and sum(r['active']for r in candidate['rows'])==12
cmrow=next(r for r in candidate['rows']if[r['Delta'],r['D']]==[8,3])
assert cmrow['active'] and P+'FINAL_PROOF.md'in cmrow['local_evidence']
assert (R/'research/stale_record_candidates.html').read_text()==(R/'research/stale_record_candidates.html.txt').read_text()
with(R/'research/stale_record_candidates.csv').open(encoding='utf-8-sig')as f:
 assert len(list(csv.DictReader(f)))==15

# Preserve the former current section as an explicitly dated historical snapshot.
progress=R/'research/progress.html';page=progress.read_text()
assert page==(R/'research/progress.html.txt').read_text()
old_section=re.search(r'<section id="stale-route-current">.*?</section>',page,re.S)
assert old_section
history=old_section.group().replace('id="stale-route-current"','id="stale-route-history-before-cm253"',1)
history='<details id="stale-route-history"><summary>前一轮进展快照：CM253当时尚未运行（保留历史）</summary>\n'+history+'\n</details>'
current='''<section id="stale-route-current">
<h2>当前结果：CM253局部补点已停止，下一步换连接规则</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中12格有本轮新检验，1250格另继承旧范围，老题仍0张新增达标图。</strong><p><a href="stale_record_candidates.html">15项问题、Moore差与实际方法范围</a> · <a href="stale_record_candidates.html.txt">HTML源码</a> · <a href="stale_record_candidates.csv">15行CSV</a>。公开年份与Moore余量是选题信息，不是可构造性保证。</p></div>
<p><strong>(8,3)，253→254：三次预测实际改变了检验。</strong>复用CM253源1012条旧边各一条unique3证据，保留首／中／末位置，归一化后每类27项旧路线义务。四条不交旧cut＋八星的余三边最多命中18，严格排除；没有生成254图。</p>
<p>随后实质改变规则：五条不交旧cut，一条原非边repair连接两个不接新星的端点，新星接余八端点。repair确能补11项旧路线；把星覆盖与repair独立取最大得到35≥27，推翻“这道独立容量已足够排除”的预测。35既不是存在性，也不是NO。</p>
<table><thead><tr><th>实际检验</th><th>完整域／上界</th><th>判断</th></tr></thead><tbody><tr><td>四cut纯星</td><td>27义务；余三边≤18</td><td>完整NO</td></tr><tr><td>五cut一repair，独立最大</td><td>星≤24、repair≤11，合计35</td><td>不足以排除，历史OPEN</td></tr><tr><td>绑定同一repair与两半删边</td><td>四类各30378 repair／1910136合法半选择；base≤12，余两完整边≤12，总24&lt;27</td><td>指定全族完整NO</td></tr></tbody></table>
<p>本次发现的障碍是：repair和星端口的单独最佳覆盖不能由同一组连接同时实现。完整耦合共7640544个半选择，非764万张图；首argmax仅作容量证据，候选阶段／新旧根BFS均0。累计3.686CPU/20，旧源D3、unique3、field与旧degree-reduction结论均未重跑。纸面direct hit界另排固定CM253任意至多五条旧边删除（可共享端点）＋单纯星；没有把最多十端点的全星当作合法8度图。不排多repair、其他源、多个helper或一般(8,3)。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/COUPLED_NOTE.md">具体问题、三次预测与完整域结果</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/FINAL_PROOF.md">完整范围证明</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/ROOT_DISPOSITION.json">实际终态处置</a>。</p>
<p><strong>下一步仍做(8,3)，但离开CM253局部加点。</strong>直接研究C8⋉<sub>3</sub> Z32的256点Cayley连接规则；只读排重门已完成，20CPU有限wordgate已获授权，尚无实际gate结果或256点候选。不继续CM253的R2、cut梯或旧timer。已有15格人工选题、先形成可检验直觉再构造的要求保留。</p>
<p>唯一Wiki现有LEDGERCOUNT条研究记录，记录数不是成果数。CM253流程已终态，Goal继续ACTIVE，旧N8/n61保持暂停；153／43／Lean47与全球优先权确认0均未变化。16416完整成果及专家包保留在下方，公开优先权与人工反馈继续分别记账。</p>
</section>'''.replace('LEDGERCOUNT',str(before+1))
page=page[:old_section.start()]+current+'\n'+history+page[old_section.end():]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page=re.sub(r'<p>更新 [^<]*</p>','<p>更新 '+stamp+'。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>',page,count=1)
progress.write_text(page);(R/'research/progress.html.txt').write_text(page)
assert '<details id="stale-route-history">'in page and '<strong>本轮0张新增图；仍153'in page

after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before+1 and len(after['rows'])==before+1
assert {k:after[k]for k in keys}==counts
modified=['research-wiki/DDP_METHOD_LEDGER.json','research-wiki/DDP_METHOD_LEDGER.md',n['wiki_path'],
 'research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md',
 'research-wiki/graph/edges.jsonl','research-wiki/log.md',S+'build_stale_record_page.py',
 S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json',
 'research/stale_record_candidates.csv','research/stale_record_candidates.html','research/stale_record_candidates.html.txt',
 'research/progress.html','research/progress.html.txt',str(rawpath.relative_to(R)),
 str((OUT/f'{LABEL}_NODE_CALLS.log').relative_to(R)),str((OUT/f'{LABEL}_RECEIPT.json').relative_to(R)),
 str(Path(__file__).relative_to(R))]
receipt=dict(status='PASS_ONE_CM253_TERMINAL_NODE_AND_EXISTING_DELIVERY_UPDATED',updated_UTC=NOW,
 records_before=before,records_after=before+1,records_added=1,new_experiment_id=rid,
 index_experiment_count_before=index_before,index_experiment_count_after=index_before+1,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 fourcut_capacity='27required_vs18upper_NO',independent_repair_capacity='35_NOT_SUFFICIENT_TO_EXCLUDE',
 complete_coupled_halfchoices=7640544,coupled_base_max_per_class=[12]*4,
 coupled_final_upper_per_class=[24]*4,required_per_class=[27]*4,
 five_disjointcut_one_repair_scope='COMPLETE_NO',paper_pure_at_most5_distinct_deletion_star_scope='COMPLETE_NO',
 not_general8D3_or_arbitrary_onepoint_NO=True,actual_candidates=0,candidate_BFS=0,
 case_CPU_seconds=3.686201072,case_CPU_cap_seconds=20,
 human_top_blocks_preserved_exact=preserved,prior_progress_snapshot_preserved=True,
 existing_shortlist_rows=15,newly_tested_shortlist_cells=12,shortlist_new_legal_graphs=0,
 builder_existing_outputs_updated=True,progress_html_and_source_identical=True,
 next_direct256='HISTORY_READ_COMPLETE_20CPU_FINITE_WORDGATE_AUTHORIZED_NO_ACTUAL_RESULT',
 full_index_query_rebuild_or_reimport=False,new_numeric_BFS_field_solver_Lean_review_hash_runs=0,
 root_STATE_ROUND_recovery_REPORT_modified=False,sameGoal='ACTIVE',old_N8_n61='PAUSED',
 modified_paths=modified,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
