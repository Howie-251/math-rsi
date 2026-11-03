"""One fixed global256 terminal; no word, parameter, graph or BFS rerun."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,csv,io,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='GLOBAL256_ALL_NORMALS_TERMINAL_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
P=S+'stale_record_transfer_d8D3/global_c8_z32_action3_256/'
rid='ddp-stale-d8d3-global-c8-action3-z32-fixed-phases-all-normals-no-20261101'
cmid='ddp-stale-d8d3-cm253-star-and-fivecut-one-repair-coupled-no-20261101'
def read(p):return json.loads((R/p).read_text())
root=read(P+'ROOT_DISPOSITION.json');result=read(P+'RESULT.json')
term=read(P+'TERMINAL.json');compat=read(P+'COMPATIBILITY.json')
assert root['status'].startswith('ROOT_ACCEPTED')
assert result['status']=='COMPLETE_NO_FIXED_GLOBAL256_ALL_NORMALS'
assert result['capacity_pass'] and result['connected_domain_complete']
assert result['normalized_representatives_visited']==61440 and result['disconnected_parity_skipped']==4096
assert result['connected_parameters_checked']==57344 and not result['full_hit'] and not result['CPU_cap_stop']
assert result['degree7_checked']==3072 and result['degree8_checked']==54272
forms=[r['distinct_coefficient_forms']for r in result['phases']]
single=[r['actual_full_cover_count']for r in result['phases']]
assert forms==[63,58,58,58,46,58,58,58] and single==[320,448,1344,672,256,672,1344,448]
assert all(r['maximum_actual_cover']==32 for r in result['phases'])
assert term['terminal'] and term['active_processes']==0
assert compat['source_rows_read_once']==57344 and compat['new_words_parameters_BFS_graphs']==0
assert compat['minimum_incompatible_size']==2 and compat['chosen_incompatible_phases']==[0,2]
assert compat['chosen_incompatible_simultaneous_full_count']==0
proper=compat['every_proper_subset_witness'];p0=next(r for r in proper if r['phases']==[0]);p2=next(r for r in proper if r['phases']==[2])
assert p0['simultaneous_full_count']==320 and p2['simultaneous_full_count']==1344
assert p0['actual_saved_witness']['normals']==[1,1,2,23]
assert p2['actual_saved_witness']['normals']==[1,0,2,10]
assert compat['terminal'] and compat['active_processes']==0
assert abs(compat['wholecase_CPU_seconds']-2.274279767)<1e-10
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count']
records={r['id']:r for r in L['rows']};assert len(records)==before
assert rid not in records and not(W/'experiments'/f'{rid}.md').exists() and cmid in records
assert not any('action3-z32'in r['id']and'all-normals'in r['id']for r in L['rows'])
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances',
 'saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs',
 'pending_outside_saved_table_graph_examples','pending_outside_saved_table_parameter_pairs',
 'known_publicly_dominated_graph_examples','known_publicly_dominated_also_saved_table_improvement_examples']
counts={k:L[k]for k in keys};assert tuple(counts[k]for k in keys[:5])==(153,43,47,105,4)
names=['GLOBAL256_SOURCE_GATE.md','PRED.md','PAPER_DOMAIN_REVIEW.md','run_once.py','gate.cpp',
 'ALL457_WORDS.tsv','DISTINCT_FORMS.tsv','ALL_NORMALIZED_CONNECTED_PARAMETERS.tsv',
 'NATIVE_RESULT.json','RESULT.json','TERMINAL.json','HANDLE.json','compatibility_once.py',
 'COMPATIBILITY.json','NOTE.md','ROOT_DISPOSITION.json']
paths=[P+x for x in names];assert all((R/x).is_file()for x in paths)
raw=dict(id=rid,
 title='8D3固定global256：全57344连通规范normal案NO；phase0与2各自可满但共同满0',
 family='Fixed semidirect cyclic-group Cayley short-word endpoint compatibility',
 idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',wiki_verdict='no',
 record_type='complete_fixed_global_Cayley_normal_parameter_word_gate_no_graph',
 target_Delta=8,target_D=3,savedL=253,
 baseline_date='Inherited CM253 public-main threshold1994; this is a new fixed global rule, not CM253 surgery or a public-source reproduction',
 n=dict(actual=None,hypothetical=256),actual_graph_Delta=None,actual_D=None,
 actual_D_scope='No256candidategraph,BFSorordinarybadpairmeasurement. Exactlength<=3wordendpointgateexcludesthefixedfamily;Cayleytranslationtransportsidentitycoverage,butnoactualsource/candidateBFSwasrun.',
 ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,new_lower_bound=False,
 scope='FixedRIGHTgroupC8actingby3onadditivecyclicZ32(notF32orF2^5),law(a,b)*(c,d)=(a+cmod8,b*3^c+dmod32). Fourpositivephasesfixed1/2/3/4,arbitraryfournormalresidues,withactualtrueinverseedges,maxdegree<=8. Allconnectedparameterscoveredbycommonoddunitnormalization;actualdegree7aliasesretained. Nototherphasepatterns,actions,groups,arbitrarygeneratorchoices,other256Cayleygraphs,CM253editsornonCayley/general8D3.',
 outcome_class=root['status'],
 distance_text='容量正预测支持：空词及8+56+392真实逆码NB短词共457，八phase不同Z32四变量形式63/58/58/58/46/58/58/58，均≥32。共同oddunit将firstodd归1得61440规范代表，4096对齐奇偶案由纸面连通iff排除，57344连通案逐全部八槽完整，degree7=3072/degree8=54272全部保留，无共同全满。单phase实际均能32，满槽参数数320/448/1344/672/256/672/1344/448。只后处理旧57344行得最小冲突大小2、首pair{0,2}共同满0；phase0首id855 b[1,1,2,23]覆盖[32,31,31,29,26,29,31,31]，phase2首id58 b[1,0,2,10]覆盖[27,29,32,32,29,32,32,29]。故不是路线形式或单槽容量不足，而是同一四normal不能兼容两槽。主批2.080238239/20CPU；只读compat.144041528+prep.05后同case累计2.274279767/20，0新参数/图/BFS/field/solver/Lean/外审。',
 lesson_and_restart_condition='STOPthiswholefixedgroup/action3/phases1234/allnormalfamily. Thecapacitypredictionwasusefulbutnotasufficiencyclaim;everyphasecanindividuallybefull,yetactualminimumincompatiblepair0/2alreadyhasnocommonparameter. Do notcontinueexistingnormals,seed,timerorautomaticallyswitchphase/action/group. Anyfuturequestionmustchangeactualrouteforms/constraintsoutsideclosedfamily,andhasnoresultorqueueclaimedhere. PreserveCM253purestar/repairNOasadistinctprecedingmechanism,notanotherinstanceofthisglobalgate.',
 restart_condition='AnewconcreteboundedquestionoutsidefixedC8/action3/Z32/phases1234normalfamily,chosenfromtheexisting15-cellprioritiesorstructuralroutechange;noneautomaticallylaunchedbythisterminal.',
 unclosed_gap='Othergroups/actions/phasepatterns,general256-vertexCayleygraphs,nonCayleyconstructionsandarbitrary(8,3)remainunexcluded. Finitephase0/2compatibilityNOisnotsymbolicimpossibilitytheoremforbroadergroupclasses. No newgraph/parameter/Lean/independentmethodcount;GoalACTIVE.',
 positive_guarantees=[
  'Thetrueinverseis(-a,-3^(-a)*b);noXORorfielddivisionisusedforcyclicZ32.',
  'Commonoddunitscalingisagroupautomorphism;firstoddnormalizationcoversallconnectedtuples,parityalignmentiffdisconnectedisprovedinPAPER_DOMAIN_REVIEW.',
  'Actualphase4inversealiasesb3=0/16givelegaldegree7cases;namedreducedwordendpointunionremainsexactactualR3,notan8degree-onlyrestriction.',
  'All57344parametershaveall8slotcoveragespersisted;compatibilityreadsoldrowsonceandtestsallphase-subsetfullcountswithoutre-evaluatingwordsorparameters.',
  'Minimumincompatiblepair0/2hasactualproper-subsetwitnesses;single-phasesufficiencyisnotmistakenforjointcoverage.'
 ],
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
  new_internal_rule_not_public_source_reproduction=True,hypothetical_order=256,hypothetical_public_main_margin=3,
  fixed_group='C8semidirectaction3additivecyclicZ32',fixed_positive_phases=[1,2,3,4],normal_modulus=32,
  normal_structure='cyclicring_notfield_or_binaryvectors',actual_inverse='(-a,-3^(-a)*b)',
  raw_named_reduced_word_count=457,distinct_coefficient_forms=forms,capacity_prediction_supported=True,
  normal_domain_complete_by_common_odd_unit=True,normalized_representatives_visited=61440,
  disconnected_parity_representatives_excluded=4096,connected_parameters_all8slots_checked=57344,
  connected_first_odd_position_counts=result['first_odd_counts'],
  actual_degree7_parameters=3072,actual_degree8_parameters=54272,
  phase4_inverse_alias_normals=[0,16],actual_degree7_not_discarded=True,
  full_hit=False,time_cap_stop=False,single_phase_maximums=[32]*8,single_phase_full_parameter_counts=single,
  compatibility_source_rows_read_once=57344,compatibility_new_word_parameter_evaluations=0,
  full_phase_mask_frequencies=[dict(mask=r['mask'],phases=r['phases'],count=r['count'])for r in compat['full_phase_mask_frequency']],
  minimum_incompatible_size=2,first_minimum_incompatible_phases=[0,2],
  first_pair_simultaneously_full_count=0,all_minimum_incompatible_pairs=compat['all_minimum_incompatible_phase_sets'],
  phase0_actual_saved_witness=p0['actual_saved_witness'],phase2_actual_saved_witness=p2['actual_saved_witness'],
  original_run_CPU_seconds=2.080238239,compatibility_actual_CPU_seconds=.144041528,
  compatibility_preparation_CPU_seconds=.05,wholecase_CPU_seconds=2.274279767,wholecase_CPU_cap_seconds=20,
  source_candidate_BFS_field_solver_Lean_review_runs=0,actual_graphs_generated=0,
  all_processes_terminal=True,complete_fixed_family_NO=True,
  preceding_distinct_CM253_mechanism_node=cmid,not_general256groups_or8D3_NO=True,
  next_question='9D3actual585native_slack_and_oldedgeedit_interface_READ_ONLY;inheritedpreservededgeNO,nocandidate586search',
  next_new_family_or_search='NOT_AUTOMATICALLY_DISPATCHED_BY_THIS_NODE',same_Goal='ACTIVE',old_N8_n61='PAUSED'),
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
pointer=dict(id=rid,path=n['wiki_path'],root_disposition=P+'ROOT_DISPOSITION.json',scope='DifferentglobalC8/action3/Z32/phases1234allnormalfamily',status='COMPLETE_NO',candidate_graphs=0)
records[cmid]['other_metrics']['subsequent_changed_global_rule_terminal']=pointer
records[cmid]['source_record']['other_metrics']['subsequent_changed_global_rule_terminal']=pointer
cmfile=W/'experiments'/f'{cmid}.md';cmtext=cmfile.read_text();assert LABEL not in cmtext
cmtext+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 后续独立全局规则已终态\n\n此前“256点规则只读／待有限门”现为历史：固定C8-action3/Z32/phases1,2,3,4的全normal族57344连通规范案完整NO，phase0与2分别可满但共满0。该规则不是CM253手术、没有新图。CM253两个原NO不重跑、不扩大。\n\n[后续全局实验节点](./'+rid+'.md)；[实际终态](../../'+P+'ROOT_DISPOSITION.json)。\n'
cmfile.write_text(cmtext)
L.update(rows=list(records.values()),record_count=before+1,updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[ROOT证据](../'+P+'ROOT_DISPOSITION.json) |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{before+1}条记录；不以此宣称{before+1}种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 全局256固定群／相位全normal终态（一个实验节点）\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n容量预测支持，但各phase可单独满不代表共享normal可共同满。457词/不同forms[63,58,58,58,46,58,58,58]；完整57344连通规范代表全部8槽，含degree7的3072案，0full。旧结果后处理最小冲突pair0/2、分别320/1344可满而共同0，两个actualwitness覆盖向量完整保存。累计2.274279767/20CPU，0图/BFS/field/solver/Lean/外审。停止固定group/action3/phases1234全normal族，不外推其他群/相位/一般8D3，不继续原参数或自动换族。与CM253局部手术分开，仍同8D3格，12格实测及153/43/47保持。下一仅只读9D3实际585的原生余度与删改旧边接口，保边全NO继承，不做586候选搜索或计新实测格。\n'
mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新终态：固定global256全normal族NO；phase0与2已有具体兼容冲突\n\n这是CM253手术以外的独立固定全局规则：C8以3作用循环加法Z32，positivephases1/2/3/4，四normal任意，真实逆配对。容量预测支持，八槽形式[63,58,58,58,46,58,58,58]均≥32。oddunit规范61440、奇偶断连排4096后57344连通案完整逐八槽，包括3072个degree7/54272个degree8；无共同全满。每槽单独都能32，不是单槽路线不足。\n\n只后处理旧57344行的满槽mask，最小不兼容大小2，首pair{0,2}共满0；phase0单满320，id855 b[1,1,2,23]覆盖[32,31,31,29,26,29,31,31]；phase2单满1344，id58 b[1,0,2,10]覆盖[27,29,32,32,29,32,32,29]。全结果和所有proper-subsetwitness已存。case累计2.274279767/20CPU，0新参数诊断/图/BFS/field/solver/Lean/外审，所有进程终态。\n\n停止固定group/action3/phases1234全normal族，不换seed/timer/phase/group自动续，不排其他256群、任意生成元或一般8D3。CM253原pure≤5cut与指定五cut一repairNO保历史互链，非本族；同8D3格不重复加实测格。'+str(before+1)+'条记录非方法，12格新实测、15老格0新达标图，153／43／Lean47及savedmain105/4/global0保持。下一仅只读9D3实际585原生余度/删改旧边接口，保边全NO继承、不做586候选搜索或冒第13格实测。人工15格顶块、sameGoal ACTIVE、旧N8/n61暂停保留。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={};index_before=None
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;index_before=int(m[1])
  text=text[:m.start()]+f'## Experiments ({index_before+1})'+text[m.end():]
  pos=text.index('\n',m.start())+1;text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': onefixedglobal256C8/action3/cyclicZ32/phases1234allnormalNOexperiment,not57344methods. Capacitypredictionpassesforms63/58/58/58/46/58/58/58;complete57344connectednormalizedall8slotcheckswith3072degree7retained. Oldrowscompatpostprocessminimumincompatiblepair0/2individually320/1344butjoint0,actualwitnessvectorssaved;no newparameterorwordevaluations. Case2.274279767/20CPU,0graph/BFS/field/solver/Lean/review. CM253priorlocalNOdistinctandpointerupdated,nooldreplay. Human15top exact,445expectedrecords/153/43/47unchanged,12cellsnot13,no automaticgroup/phase/timer.')

builder=runpy.run_path(str(R/S/'build_stale_record_page.py'))
with contextlib.redirect_stdout(io.StringIO()):builder['build']()
candidate=read(S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json')
assert len(candidate['rows'])==15 and sum(r['active']for r in candidate['rows'])==12
cmrow=next(r for r in candidate['rows']if[r['Delta'],r['D']]==[8,3])
assert P+'NOTE.md'in cmrow['local_evidence']
assert (R/'research/stale_record_candidates.html').read_text()==(R/'research/stale_record_candidates.html.txt').read_text()
with(R/'research/stale_record_candidates.csv').open(encoding='utf-8-sig')as f:assert len(list(csv.DictReader(f)))==15

progress=R/'research/progress.html';page=progress.read_text();assert page==(R/'research/progress.html.txt').read_text()
old_section=re.search(r'<section id="stale-route-current">.*?</section>',page,re.S);assert old_section
history=old_section.group().replace('id="stale-route-current"','id="cm253-prior-global256"',1)
history='<details id="cm253-before-global256-terminal"><summary>前一轮快照：CM253终态与当时待返回的256门（保留历史）</summary>\n'+history+'\n</details>'
current='''<section id="stale-route-current">
<h2>当前结果：256点固定Cayley规则完整失败，已定位两相位共享参数冲突</h2>
<div class="note"><strong>本轮0张新增图；仍153个合法版本／43组参数／47个具体Lean实例。15项老题中12格有本轮新检验，老题仍0张新增达标图。</strong><p><a href="stale_record_candidates.html">15项问题、Moore差与实际方法范围</a> · <a href="stale_record_candidates.html.txt">HTML源码</a> · <a href="stale_record_candidates.csv">15行CSV</a>。256规则仍是同一(8,3)格，不重复计为第13格。</p></div>
<p><strong>这次离开CM253局部手术，直接改变全局连接。</strong>固定群C8以乘3作用循环加法Z32，四正生成元phase为1、2、3、4，normal自由；Z32不是F32或二元向量空间。457个真实逆配对短词的八槽不同形式数为63／58／58／58／46／58／58／58，全部通过32的必要容量门，事前正预测获支持。</p>
<p>完整61440个共同奇单位规范代表中，4096个奇偶断连案由纸面条件排除；其余57344连通案逐全部八槽完成，包括3072个实际7度与54272个8度案，0共同全满。每个phase单独都确实能覆盖全部32个normal，失败原因是同一四normal无法同时满足不同槽。</p>
<table><thead><tr><th>要求</th><th>实际满足参数数</th><th>保存的参数例子与八槽覆盖</th></tr></thead><tbody><tr><td>phase0满32</td><td>320</td><td>id855，b=[1,1,2,23]；[32,31,31,29,26,29,31,31]</td></tr><tr><td>phase2满32</td><td>1344</td><td>id58，b=[1,0,2,10]；[27,29,32,32,29,32,32,29]</td></tr><tr><td>phase0与2同时满</td><td>0</td><td>最小不兼容集合大小为2，首对{0,2}</td></tr></tbody></table>
<p>这项兼容诊断只读取已有57344行一次，没有新词或参数评估。主批2.080CPU，加后处理0.144CPU与准备0.05后累计2.274CPU／20；0候选图、BFS、field、solver、Lean或外审，全部进程终态。停止本固定群／作用3／相位1–4的全normal族，不继续seed或timer、不自动换群或相位；不排其他256点群、任意生成元、非Cayley或一般(8,3)。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/NOTE.md">预测、完整域、结果与停止边界</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/COMPATIBILITY.json">完整满槽频率与最小冲突证据</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/PAPER_DOMAIN_REVIEW.md">规范域、连通性及7度情况的纸面核对</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/ROOT_DISPOSITION.json">实际终态处置</a>。</p>
<p><strong>此前CM253的结论保留，范围不合并。</strong>固定253源任意≤5删边＋纯星，以及指定五不交cut＋一原非边repair＋八星，均已完整关闭；后者独立容量35不足，实际耦合24&lt;27才完成排除。它是旧源局部改边，256是新的全局群连接，均没有产生新图。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/FINAL_PROOF.md">CM253完整范围证明</a>。</p>
<p><strong>下一问题转向本轮尚无新检验的(9,3)。</strong>只读实际585源的原生余度与删改旧边接口；原保边扩张全NO直接继承，不重跑。此时没有586候选、候选搜索或新的数值结论，不把接口读取计为第13格实测。</p>
<p>唯一Wiki现LEDGERCOUNT条研究记录，记录数不是独立方法或成果数。人工15格选题与先检验直觉再构造的要求保留；Goal继续ACTIVE，旧N8/n61暂停。153／43／Lean47及全球优先权确认0不变；16416完整成果、专家包与人工反馈状态在下方。</p>
</section>'''.replace('LEDGERCOUNT',str(before+1))
page=page[:old_section.start()]+current+'\n'+history+page[old_section.end():]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
page=re.sub(r'<p>更新 [^<]*</p>','<p>更新 '+stamp+'。同一Goal ACTIVE；旧D2/n61任务继续暂停。</p>',page,count=1)
progress.write_text(page);(R/'research/progress.html.txt').write_text(page)
after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before+1 and len(after['rows'])==before+1
assert {k:after[k]for k in keys}==counts
modified=['research-wiki/DDP_METHOD_LEDGER.json','research-wiki/DDP_METHOD_LEDGER.md',n['wiki_path'],
 'research-wiki/experiments/'+cmid+'.md','research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md',
 'research-wiki/graph/edges.jsonl','research-wiki/log.md',S+'build_stale_record_page.py',
 S+'public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json',
 'research/stale_record_candidates.csv','research/stale_record_candidates.html','research/stale_record_candidates.html.txt',
 'research/progress.html','research/progress.html.txt',str(rawpath.relative_to(R)),
 str((OUT/f'{LABEL}_NODE_CALLS.log').relative_to(R)),str((OUT/f'{LABEL}_RECEIPT.json').relative_to(R)),
 str(Path(__file__).relative_to(R))]
receipt=dict(status='PASS_ONE_FIXED_GLOBAL256_TERMINAL_NODE_AND_EXISTING_DELIVERY_UPDATED',updated_UTC=NOW,
 records_before=before,records_after=before+1,records_added=1,new_experiment_id=rid,
 index_experiment_count_before=index_before,index_experiment_count_after=index_before+1,
 graph_parameter_Lean_method_increments=[0,0,0,0],counts_unchanged=counts,
 raw_words=457,distinct_forms=forms,capacity_prediction_supported=True,
 connected_parameters_complete=57344,degree7_retained=3072,degree8=54272,
 all_parameters_all8slots_evaluated=True,full_hit=False,
 minimum_incompatible_phases=[0,2],phase0_single_full=320,phase2_single_full=1344,pair_common_full=0,
 phase0_actual_witness=p0['actual_saved_witness'],phase2_actual_witness=p2['actual_saved_witness'],
 compatibility_old_rows_only=True,new_parameter_or_word_evaluations_by_diagnostic=0,
 wholecase_CPU_seconds=2.274279767,wholecase_CPU_cap_seconds=20,
 fixed_global_family_only_not_general256_or8D3=True,CM253_scope_preserved_and_pointer_updated=True,
 human_top_blocks_preserved_exact=preserved,prior_progress_snapshots_preserved=True,
 existing_shortlist_rows=15,newly_tested_shortlist_cells=12,shortlist_new_legal_graphs=0,
 builder_existing_outputs_updated=True,progress_html_and_source_identical=True,
 full_index_query_rebuild_or_reimport=False,new_numeric_BFS_field_solver_Lean_review_hash_runs=0,
 root_STATE_ROUND_recovery_REPORT_modified=False,next9D3_585='READ_ONLY_INTERFACE_NOT_CANDIDATE_SEARCH_OR_NEW_TESTED_CELL',
 sameGoal='ACTIVE',old_N8_n61='PAUSED',
 modified_paths=modified,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
