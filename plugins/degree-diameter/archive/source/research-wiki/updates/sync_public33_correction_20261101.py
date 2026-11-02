"""Upsert the public W(3,7)33 correction; read saved evidence, run no research."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import json
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[2]
W=ROOT/'research-wiki'
S='research/ddp/two_successful_methods_20261101/'
P=S+'public_baseline_audit/'
F=S+'affine_field_conditions/r7_fourbase_triangle_controller/'
REPORT=P+'W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101'
STEM='PUBLIC_W3F7_33_CORRECTION65_70_77_CRT_TRIANGLE_20261101'
NEW='ddp-public-w3f7-partial-ovoid33-primary-table5-corrects-65-70-77-comparison-20261101'
ID65='ddp-gq77-cubic-three-coset-partial-ovoid22-immutable-clones-161150-d65-d3-20261101'
ID70='ddp-gq77-cubic22-multiplicity6-immutable-clones-166650-d70-d3-20261101'
ID77='ddp-degree77-r7-f11-public-tallini15-gq7-generalduplication-169750-controller-threshold128-20261101'
ID33='ddp-r7-fourbase-triangle-m33-global2000000-unknown-cap-reached-20261101'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
l=json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
old={r['id']:r for r in l['rows']}
sources=[REPORT+'.md',REPORT+'.json',P+'w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf',P+'w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png',P+'w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png']
rows=[]
for rid,degree,baseline,deficit in [(ID65,65,161650,500),(ID70,70,169900,3250)]:
    r=copy.deepcopy(old[rid]['source_record'])
    m=r['other_metrics']
    m['historical_public_comparison_before_primary33']={
        'public_guarantee':r['savedL'],'baseline_date':r['baseline_date'],
        'candidate_gain':r['n']['actual']-r['savedL'],
        'status':'superseded by actually read 2007 Table5 W(7)33, not a graph failure'}
    r['savedL']=baseline
    r['baseline_date']='2026-11-01 corrected direct published-method guarantee using Cimrakova-Fack2007 Table5 W(7) partialovoid33; not a global table or separate published numeric edgefile'
    r['title']=f'{r["n"]["actual"]}/{degree}/D3完整合法／Lean与A/B/C保留；公开33点推论{baseline}已超过{deficit}'
    r['record_type']='complete_literal_graph_validated_known_publicly_dominated'
    r['outcome_class']='COMPLETE_LEGAL_UNCONDITIONAL_LEAN_A_B_FRESH_C_PASS_KNOWN_PUBLIC_METHOD_DERIVATION_DOMINATED'
    oldsentence=('仅超过bestlocated published160750保证400，全球/优先权仍未认证。' if degree==65 else 'best-located公开保证164500，优势2150；全球／首创未认证。')
    current=f'【当前公开比较更正】Cimráková–Fack2007 §4.3/Table5实际W(7)33点，经既有一般Delorme复制给{baseline}，本图低{deficit}；旧15点比较只历史。本图全部合法性、独验、具体Lean/Audit与A/B/freshC仍实际完成，未重验。'
    r['distance_text']=current+r['distance_text'].replace(oldsentence,'')
    r['unclosed_gap']=f'数学合法／独验／具体Lean和A/B/distinctfreshC全部PASS终态。当前已知被公开方法组合推论{baseline}超过{deficit}，不能继续称相对最新已读公开保证的改善；这不是找到了该数值独立边表或全球维护表。O22规则归属／优先权未认证。'+r['unclosed_gap'].split('新samecap门')[-1].split('published160750下')[0] if degree==65 else f'数学图／具体Lean／A/B/freshC完成；当前已知被公开已发表前提推论169900超过3250，旧+2150仅历史。O22规则来源／优先权及全球图最优未认证，不影响合法性。'
    r['lesson_and_restart_condition']+=' 当前primary33检验使竞争判断改变；不再以旧15点基线维持优越性。root另派公开33对象复现与filled160050邻域接口研究；未生产/计新图，不续m33竞争批次。'
    m.update(known_publicly_dominated=True,known_publicly_dominated_example_orders=[r['n']['actual']],current_public_guarantee=baseline,current_candidate_minus_public=-deficit,public_comparison_status='KNOWN_DOMINATED_BY_DIRECT_PUBLISHED_METHOD_COMPOSITION_NOT_GLOBAL_NUMERIC_TABLE',public33_source_report=REPORT+'.md')
    for g in m['validated_graph_instances']:
        g.update(known_nonrecord=True,known_publicly_dominated=True,best_located_public_lower_bound=baseline,public_comparison_status='KNOWN_PUBLIC_METHOD_DERIVATION_DOMINATED',bounded_gain=-deficit)
        assert g['mathematically_validated_complete_graph'] and g['complete_Lean_graph_instance']
    m['source_credit']=(m.get('source_credit','')+' Current comparator uses published Cimrakova-Fack2007 W(7)33, not only Tallini15; no local unpublished source used as public.').strip()
    r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+sources))
    rows.append(r)

r=copy.deepcopy(old[ID77]['source_record'])
r['title']='77度公开门已更正181450：primary W(7)33，H132目标少5758，原169750仅历史'
r['outcome_class']='CORRECTED_PUBLIC_GUARANTEE181450_H132_TARGET_PUBLICLY_DOMINATED'
r['distance_text']='此前Tallini15组合169750及Hmin128保留为检索历史。实际读Cimráková–Fack2007 p140 Table5：W(7)33点/#1，p131明确symplectic W(3,q)，非upper43或Q(4,7)partialovoid。当前160000+13*(33*50)=181450，条件175692少5758；1331H纯点数min137，7regular偶Hmin138，三baseevenm46/H138、四base3|m36/H144仅条件尺度，无新搜索授权。'
r['scope']='已读primary33计算例存在性＋继承公开GQ7/spread/一般§7复制的直接推论；没有独立公开181450数值边表或全球维护表。旧15门不再当前；合法PolarStar窗口原值保留，无重算。'
r['unclosed_gap']='H132/175692竞争目标已明确被更大公开方法推论阻断，不再只写partialovoid未穷尽。未认证全局图最优/优先权；无新controller/图。'
r['lesson_and_restart_condition']='针对明确25阈值的primary小q表找到33，实际停止m33作为新纪录目的的派发；转公开33对象的坐标复现及现有filled源连接接口小实验，复现不记新纪录。'
m=r['other_metrics'];m['historical_pre_primary33']={k:m[k] for k in ['best_located_derived_guarantee','public_partial_ovoid','centers','minimumH','minimum_threebase_evenH','minimum_threebase_evenm']}
m.update(best_located_derived_guarantee=181450,public_partial_ovoid=33,centers=1650,center_matching_edges=528,center_isolates=594,minimumH=137,minimum7regular_evenH=138,minimum_threebase_evenH=138,minimum_threebase_evenm=46,minimum_fourbase_H=144,minimum_fourbase_m=36,current_H132_target_minus_public=-5758,public33_source_report=REPORT+'.md')
r['positive_guarantees']=['2007原始计算表明确给W(7)33点，作者报告为穷尽最大及1等价类；本门只需要实际计算下界，未重跑该计算。','一般Delorme复制含matching新新边，使用原公开160000源和50spread，不用本地160050/O22。','本次推论不产独立公开数值边表，也不认证全局纪录；H阈值不证明controller存在。']
r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+sources));rows.append(r)

r=copy.deepcopy(old[ID33]['source_record'])
r['title']='四base m33：采样UNKNOWN／三固定CRT profiles严格无修复；目标被公开181450阻断'
r['outcome_class']='SAMPLED_UNKNOWN_THREE_FIXED_CRT_PROFILES_NO_REPAIR_H132_TARGET_PUBLICLY_DOMINATED'
r['distance_text']='【最新竞争状态】公开W(7)33推论181450超过条件175692共5758；原+5942仅当时15点检索历史。'+r['distance_text'].replace('首competitive m33/H132条件175692（对169750+5942）','当时按旧门选择m33/H132条件175692')
r['unclosed_gap']='原topology m33全族存在性未排；但其H132完整F11点数即使成功也已被公开181450阻断。三固定mod11 profile的phase修复已严格失败，其他quotient未排。triangle123受控单例成功修一桶却破坏其他类，0完整controller/图。'
r['lesson_and_restart_condition']='本次明确区分缺路线容量与共享相位不兼容：profile3六桶各仅2种形式，profile1/2各完整phase cube均无解、保首八类仅两同构相位仍缺03。改triangle123闭合可补23目标桶但使五个原满类失效，不能由总缺12→10自动续。更强公开181450现停止m33竞争派发；不据此判全部七port无望，不自动m36梯子。'
r['other_metrics'].update(historical_conditional_gain=5942,conditional_gain=-5758,current_public_guarantee=181450,competitive_batch_authorized=False,public_competition_stop=True,
    CRT_three_profiles={'status':'COMPLETE_NO_REPAIR_IN_THREE_FIXED_QUOTIENT_PROFILES','phase_assignments':39366,'simple_assignments':32805,'profile3_capacity_failing_buckets':6,'each_bad_bucket_distinct_functions':2,'profiles1_2_phase_cubes':2,'deep_phases_each':2,'deep_phase_pair_unit':23,'accounted_CPU_seconds':1.315583923,'whole_family_excluded':False},
    triangle123={'symbolic_status':'CAPACITY49_M33_SURVIVES','rule':'tau13=rho12+sigma23','symbolic_CPU_seconds':0.008868824000000004,'controlled_actual_status':'PREDICTED_23_BUCKET_REPAIRED_OTHER_COVERAGE_LOST_NOT_COMPLETE','controlled_changed_parameter':'sigma23:0->5 only','controlled_target_bucket':[5,16,27],'controlled_CPU_seconds':0.005179383000000003,'fully_repaired_classes':[[1,3],[2,3],[3,1],[3,2]],'newly_incomplete_classes':[[0,2],[1,1],[1,2],[2,0],[2,1]],'total_missing_before':12,'total_missing_after':10,'global_or_local_searches':0})
extra=[F+x for x in ['m33_crt_phase_repair/PRED.md','m33_crt_phase_repair/PROOF.md','m33_crt_phase_repair/RESULT.json','m33_crt_phase_repair/TERMINAL.json','m33_crt_phase_repair/INDEPENDENT_CRT_BUCKET_NOTE.md','triangle123_closure/PRED.md','triangle123_closure/PROOF.md','triangle123_closure/RESULT.json','triangle123_closure/CONTROLLED_TRIANGLE123_NOTE.md','triangle123_closure/CONTROLLED_TRIANGLE123_RESULT.json','triangle123_closure/CONTROLLED_TRIANGLE123_CLASS_COMPARISON.csv']]
r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+sources+extra));rows.append(r)

rows.append(dict(id=NEW,title='公开W(3,7)33点计算例纠正65／70／77比较：161650／169900／181450',family='Published-source comparison gate',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',target_Delta=None,target_D=3,savedL=None,baseline_date='2026-11-01 primary Table5 actually visually read, direct published-method consequence not independent numeric edgefile',record_type='published_source_baseline_correction',n=dict(actual=None,hypothetical=None),actual_graph_Delta=None,actual_D=None,actual_D_scope='文献存在性与旧已核复制接口的有限标量推论，0controller/完整图/BFS/Lean。',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,wiki_verdict='yes',outcome_class='PRIMARY_W3_F7_PARTIAL_OVOID33_FOUND_TWO_ACCEPTED_GRAPHS_PUBLICLY_DOMINATED_ONE_CONDITIONAL_TARGET_BLOCKED',distance_text='实际原PDF p131定义W(q)=symplectic W(3,q)，p140 §4.3 Table5 W(7)行33点/1等价类，作者报告穷尽计算，非upper43/Q4partialovoid。公开160000/64源×50spread，一般§7复制推161650/65、169900/70、181450/77；本地161150/166650差−500/−3250，条件175692差−5758。',scope='当前primary可核W(3,7)33计算下界，未复跑作者最大团计算或取到坐标；直接组合已发表机制而非独立公开数值图或全球维护表。旧图合法、Lean及A/B/C全部保持，全球纪录认证0。',positive_guarantees=['一次3query后沿明确primary引用打开出版社原始扫描PDF并实际视觉读表；不是从Ceria通用15/upper43推测。','Q(4,7)48点ovoid对偶成W(3,7)partialspread，不能错代；Wpartialovoid才对应Qpartialspread。','一般复制保留matching连接；不把本项目160050/O22当公开。'],unclosed_gap='公开33坐标复现及其对filled160050原N的load1接口在root授权新小批次准备/在途，未生产图、未计新记录；世界最优和原创优先权仍未认证。',lesson_and_restart_condition='25阈值检验发现33，使旧65/70竞争状态立即改为已被公开推论超过，并停止m33纪录目的续批。下一步从明确公开33原对象出发做坐标/接口复现；复现与新完整构造分账，不为文档同步计成果。',other_metrics=dict(new_named_complete_graphs=0,new_Lean_instances=0,new_frameworks=0,primary_partial_ovoid_lower_bound=33,published_computational_maximum_claim=33,inequivalent_maximum_objects=1,current_public_guarantees={'65,3':161650,'70,3':169900,'77,3':181450},local_differences={'65,3':-500,'70,3':-3250,'77,3_conditional':-5758},known_publicly_dominated_total=43,known_publicly_dominated_saved_table_overlap=40,pending_outside_saved_table_graphs=19,pending_outside_saved_table_pairs=14,named_legal_total=125,legal_pairs=20,phase_graphs=21,phase_pairs=17,complete_Lean_total=19,certified_global_records=0,primary_query_batches=1,queries=3,scalar_CPU_seconds=0.000007233999999998325,coordinate_reproduction_status='ROOT_AUTHORIZED_BOUNDED_PREPARATION_OR_IN_FLIGHT_NOT_COMPLETE_GRAPH',new_full_graphs=0,large_BFS_Lean_solver_runs=0),evidence_paths=sources))

for r in rows:
    assert all((ROOT/p).exists() for p in r['evidence_paths']),r['id']
raw=W/'updates'/f'{STEM}_ROWS.json';raw.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

# Keep old gate body and its original evidence; prepend an unmistakable current correction.
gates=[S+'retained_edge_transfer/opposite_gq77_spread64/partial_ovoid65_gate/REPORT.md',S+'retained_edge_transfer/opposite_gq77_spread64/partial_ovoid65_gate/cubic_coset22/PUBLIC_GATE.md',P+'DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md',P+'DEGREE77_R7_F11_TARGET_GATE_20261101.md']
marker='<!-- PUBLIC_W3F7_33_SUPERSEDES_TALLINI15_20261101 -->'
for name in gates:
    f=ROOT/name;t=f.read_text()
    if marker not in t:
        rel=Path(__import__('os').path.relpath(ROOT/(REPORT+'.md'),f.parent)).as_posix()
        f.write_text(f'{marker}\n> **当前公开比较已更正（2026-11-01）**：[原始33点证据与修订]({rel})实际读到Cimráková–Fack2007 p140 Table5的W(7)33点，公开一般复制保证65:161650／70:169900／77:181450。本地161150／166650分别少500／3250，条件175692少5758；图合法性与具体Lean/A/B/C不变。下文15点基线和正优势是保留历史，已被此处覆盖；不是独立公开数值边表／全球维护表。\n\n'+t)
json_gates=[P+'DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.json',P+'DEGREE77_R7_F11_TARGET_GATE_20261101.json']
for name in json_gates:
    f=ROOT/name;a=json.loads(f.read_text());degree=70 if 'DEGREE70' in name else 77
    cur=dict(status='SUPERSEDED_PREVIOUS_TALLINI15_COMPARISON_BY_ACTUALLY_READ_PRIMARY33',checked_UTC=now,Delta=degree,D=3,current_best_located_source_derived_guarantee=169900 if degree==70 else 181450,current_target_n=166650 if degree==70 else 175692,current_target_minus_guarantee=-3250 if degree==70 else -5758,source_report=REPORT+'.md',kind='direct_composition_of_published_mechanisms_not_separate_published_numeric_edgefile',global_record_or_priority_certified=False)
    a={'current_public_comparison':cur,'following_fields_are_preserved_historical_gate_snapshot':True,**{k:v for k,v in a.items() if k not in ['current_public_comparison','following_fields_are_preserved_historical_gate_snapshot']}}
    f.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')

cmd=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(raw)]
res=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
assert res.returncode==0,(res.stdout,res.stderr)
sync=json.loads(res.stdout)

intro=f'''<!-- {STEM} -->
# 当前：公开W(3,7)33点已找到；65／70及条件77的旧优势撤回

同Goal ACTIVE：125合法例／20参数、阶段21图／17参数，具体Lean19，ledger415。已知被更大公开推论超过43例（保存主表overlap仍40）；保存主表外待核19例／14参数，全球纪录认证0。旧65/70独验、Lean及A/B/freshC仍全部完整合法。

[原始33点证据](../{REPORT}.md)：Cimráková–Fack2007 p131明确W(q)=symplectic W(3,q)，p140 Table5 W(7)33点/#1。非理论upper43/Q(4,7)ovoid；公开160000源＋一般matching复制推65:161650、70:169900、77:181450。本地161150/166650分别少500/3250，条件H132/175692少5758；旧15基线仅历史，旧gate已顶注更正，非独立公开数值边表。

[m33局部终态](experiments/{ID33}.md)：200万样本UNKNOWN；三固定CRT profiles实际无phase修复，1.315584CPU。triangle123单例修23桶却破坏五原满类，0controller/图；m33不再派competitive批次、不自动m36。root另派公开33坐标复现≤30CPU及filled160050原N/load1接口小检验，未生成/验收图；复现不新纪录。冻结专家包不动，root另交勘误。以下保留历史。

'''
gap=W/'gap_map.md';text=gap.read_text()
if not text.startswith(f'<!-- {STEM} -->'):gap.write_text(intro+text)
human=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if f'<!-- {STEM} -->' not in human.read_text():
    with human.open('a') as f:
        f.write(f'''\n\n<!-- {STEM} -->
## 2026-11-01 公开33点结果纠正竞争判断，保留合法性与失败范围

本段为沿用既有人工要求的实际执行修订，不新增用户原话或第二计划。针对“公开partialovoid≥25会否阻断H132”这一明确预测，实际primary文献读表找到33：Cimráková–Fack2007 §4.3/Table5，p140 W(7)33点/#1，p131已核symplectic对象。[证据与比较](../{REPORT}.md)。Ceria通用15下界不能代表q7小参数计算最大；43只是上界；Q4的48点ovoid对应Wspread不是Wovoid。读表没有重跑作者搜索。

因此旧65/161150、70/166650的数学合法／具体Lean／A/B/freshC保持，但当前公开推论161650/169900分别超过500/3250；条件77/175692低于181450共5758。两旧图当前转已知公开支配，accepted125/20、阶段21/17、Lean19不变；knownpublicdominated41→43、savedoverlap40不变，outsidepending21/16→19/14。此公开推论不是单独找到数值edgefile或全球维护表；全球纪录认证0。四图冻结包不改，root另行显式勘误。

同一m33节点保存后续理解检验：三个固定mod11 profile中profile3六桶各仅2形式，phase怎样选都缺一相位；profile1/2分别完整3^9 cube无解（总39366phase/32805simple），保前八类仅两组unit23同构相位仍缺03，含编译1.315583923CPU。不是m33整族排除。triangle123闭合symbolic最小51→49，仍容m33；单受控sigma23:0→5确修23的三相位桶，13/23及反向补齐，却令02/11/12及反向五原满类失效。总缺12→10不自动续算，实际0controller/图/BFS/Lean。公开181450现在从竞争目的停止m33，不自动更大m梯子。

root下一具体动作是公开33对象坐标复现（≤30CPU、原400点输入）与filled160050源的fullN64/load1接口，均仅小对象，未完成前不记图或新纪录。此次方向改变由实际公开证据与覆盖对照推动，不以文件同步当数学成果。
''')

helper=ROOT/'aris_repo/tools/research_wiki.py';calls=[]
def call(*args):
    c=[sys.executable,str(helper),*args];r=subprocess.run(c,cwd=ROOT,text=True,capture_output=True)
    calls.append(dict(command=c,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr));assert r.returncode==0,calls[-1]
for rid in [ID65,ID70,ID77,ID33]:
    call('add_edge',str(W),'--from','exp:'+rid,'--to','exp:'+NEW,'--type','uses','--evidence','Current primary33 public comparison supersedes historical Tallini15 numeric claim; accepted graphs/proofs unchanged, m33 not competitive.')
call('log',str(W),'2026-11-01 actualprimaryCimrakovaFack2007Table5W7partialovoid33corrects65/70/77publicguarantees161650/169900/181450;legal125/20stage21_17Lean19unchanged,publicdominated43savedoverlap40outsidepending19/14globalrecords0. Existing65/70/77/m33updated+onepubliccorrectionnodeledger415;CRTthreefixedprofilesstrictclosed/triangle123controlledrepairwithlosssaved;noexperimentalrerun,newgraph0,frozenpacketuntouched.')
call('rebuild_index',str(W));call('rebuild_query_pack',str(W))
cp=W/'updates'/f'{STEM}_HELPER_CALLS.json';cp.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text())
expected={'record_count':415,'validated_named_graph_examples':125,'validated_named_parameter_pairs':20,'complete_Lean_graph_instances':19,'known_publicly_dominated_graph_examples':43,'known_publicly_dominated_also_saved_table_improvement_examples':40,'pending_outside_saved_table_graph_examples':19,'pending_outside_saved_table_parameter_pairs':14}
for k,v in expected.items():assert ledger[k]==v,(k,ledger[k],v)
evidence=set(x for r in rows for x in r['evidence_paths']);assert all((ROOT/x).exists() for x in evidence)
checked=0
for path in [W/'experiments'/f'{r["id"]}.md' for r in rows]+[ROOT/x for x in gates]:
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        link=unquote(link.strip('<>').split('#',1)[0])
        if not link or re.match(r'\w+://',link):continue
        assert (path.parent/link).exists(),(path,link);checked+=1
q=(W/'query_pack.md').read_text();assert 'ledger415' in q and '181450' in q and '43' in q
receipt=dict(updated_UTC=now,status='PASS_UNIQUE_WIKI_PUBLIC33_COMPARISON_CORRECTED_LEGALITY_RETAINED',ledger_records=415,records_added=1,records_updated=4,named_legal_graphs=125,legal_parameter_pairs=20,phase_graphs=21,phase_pairs=17,complete_formula_Lean=19,known_publicly_dominated=43,saved_table_dominated_overlap=40,pending_outside_saved_table_graphs=19,pending_outside_saved_table_pairs=14,certified_global_records=0,current_guarantees={'65,3':161650,'70,3':169900,'77,3':181450},new_graphs=0,new_Lean_instances=0,new_frameworks=0,canonical_upsert_command=cmd,canonical_upsert_stdout=sync,actual_helper_calls=str(cp.relative_to(ROOT)),resolved_evidence_paths=len(evidence),checked_local_markdown_links=checked,legacy_MD_gates_top_annotated=gates,legacy_JSON_gates_with_current_fields=json_gates,CRT_three_profiles_actual_complete=True,triangle123_controlled_prediction_supported_but_global_notcomplete=True,experiments_rerun=0,root_owned_files_modified=False,frozen_expert_packets_modified=False,query_current=True)
rp=W/'updates'/f'{STEM}_RECEIPT.json';rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
