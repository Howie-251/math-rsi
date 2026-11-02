"""One accepted graph version, one new paper boundary, two existing-node deltas."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time()
R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/'
OUT=R/S/'wiki_sync';LABEL='D16_16416_715_PACKING1250_DELTA_20261101'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
def evidence(p,names):
    paths=[p+n for n in names];assert all((R/x).is_file() for x in paths);return paths
def optional(p,names):return [p+n for n in names if(R/p/n).is_file()]
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count']
existing={n['id']:n for n in L['rows']};assert len(existing)==before
parent='ddp-d15-d4-current15552-source-gap-20261027'
conder='ddp-conder1250-edge-subdivision-two-cut-helper-family-20261027'
old715='ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101'
assert all(x in existing for x in [parent,conder,old715])
assert L['validated_named_graph_examples']==152 and L['validated_named_parameter_pairs']==43 and L['complete_Lean_graph_instances']==46
assert L['saved_main_table_improvement_graph_examples']==104 and L['saved_main_table_improvement_parameter_pairs']==4
assert L['pending_outside_saved_table_graph_examples']==45 and L['pending_outside_saved_table_parameter_pairs']==38
assert L['known_publicly_dominated_graph_examples']==43 and L['known_publicly_dominated_also_saved_table_improvement_examples']==40

BASE=S+'retained_edge_transfer/published_d15_15552_D4_source_gate/'
P=BASE+'degree16_plane864/';A=P+'independent_acceptance/'
g,gt,release=read(A+'RESULT.json'),read(A+'TERMINAL.json'),read(P+'ROOT_GRAPH_RELEASE.json')
assert g['status']=='PASS_COMPLETE_LITERAL_AND_ALL16416_FINAL_ROOTS_EXACT_D4'
assert release['status']=='ROOT_ACCEPTED_COMPLETE_16416_LITERAL_AND_ALLROOT_D4'
assert (g['n'],g['m'],g['Delta'],g['D'])==(16416,129240,16,4)
assert g['ordinary_final_graph_BFS_roots']==16416 and g['actual_allordered_pairs_reached_within4']==269485056
assert g['source_raw_parses']==g['candidate_parses']==1 and g['source_only_BFS_roots']==0
assert g['ordered_fullN_roles_bound']==864 and g['new_edges']==12924 and g['new_new_edges']==0
assert gt['all_processes_terminal'] and not gt['running'] and release['new_concrete_Lean_increment']==0
idG='ddp-d16d4-whole27-fulln-clone864-graph16416-20261101'
pathsG=evidence(P,['PRED.md','PROOF.md','RESULT.json','TERMINAL.json','ROOT_GRAPH_RELEASE.json','graph_d16_D4_n16416.edges','ALL864_ROLE_BINDINGS.tsv'])
pathsG+=evidence(A,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','verify.cpp','run_once.py','FROZEN_I32_INPUT.json','ALL864_ACTUAL_ROLE_BINDINGS.tsv','ACTUAL_SOURCE_CONTROLLER_PROJECTION.tsv','ALL16416_FINAL_ROOT_BFS.csv','ACTUAL_HISTOGRAM_DISTRIBUTIONS.csv','GENUINE_FOUR_WALK.json'])
pathsG+=evidence(S+'public_baseline_audit/',['D16_D4_PACK32_TARGET_20261101.json','D16_D4_PACK32_TARGET_20261101.md'])
instance=dict(Delta=16,D=4,n=16416,m=129240,actual_diameter=4,
    mathematically_validated_complete_graph=True,complete_Lean_graph_instance=False,
    confirmed_publictable_improvement=True,latest_global_record_confirmed=False,
    known_publicly_dominated=False,best_located_public_lower_bound=16384,bounded_gain=32,
    graph_path=P+'graph_d16_D4_n16416.edges',independent_result=A+'RESULT.json',ROOT_release=P+'ROOT_GRAPH_RELEASE.json',
    parent_experiment=parent,same_source_whole27_clone_mechanism=True,new_method=False,
    formal_status='PENDING_NEW_CONCRETE_I32_864_NOT_INHERITED_FROM16389',
    external_ARIS_AB_freshC='PENDING_NEW_SCOPE_NOT_INHERITED_FROM16389',global_priority='UNKNOWN')
rowG=dict(id=idG,title='16D4新版本16416：864个完整邻域clone，fresh全16416根exactD4通过；新Lean/ARIS待实际终态',
    family=existing[parent]['method_family'],idea_family=existing[parent]['idea_id'],date='2026-11-01',
    wiki_verdict='yes',record_type='accepted_graph_version_same_whole_plane_clone_mechanism',
    target_Delta=16,target_D=4,savedL=16384,baseline_date='2026-11-01 fresh Comellas main/URSA16384; bounded public search only',
    n=dict(actual=16416,hypothetical=None),actual_graph_Delta=16,actual_D=4,
    actual_D_scope='One complete new literal,all16416 final roots ordinaryBFS,all269485056 orderedpairs reached within4,eachroot eccentricity4;0 separate oldsource BFS',
    ordinary_bad_unordered_pairs=0,ordinary_bad_target_D=4,
    scope='Fixed original15552/116316 source,all oldedges retained. New frozenI32 controllers×27 W={x1=0} offsets give864 distinct ordered centers;newlabel15552+j. Clone each actual simpleN,0newnew,max oldpinload1. This new version is parented to the existing whole27 fullN mechanism;not a new construction framework or parameter. The old16389 graph remains legal,completeLean and exact A/B/freshC accepted. Its Lean or ARIS does not certify16416.',
    outcome_class='ROOT_ACCEPTED_NEW16416_LITERAL_ALLROOT_EXACT_D4_CONCRETE_LEAN_ARIS_PENDING',new_lower_bound=True,
    distance_text='独立重算864有序fullN，保116316旧边，12924新边/12924distinct pins/oldload1/newnew0；centerhist14:36/15:828，终图hist14:126/15:3924/16:12366，n16416/m129240/max16。唯一fresh全16416根（15552旧label+864新label）普通BFS：269485056有序对≤4、每root ecc4；oldR4实测13066..13242支持≥6966预测，187种distanceprofile。新根到ownoldcenter全2、其余863new全3或4。真实D4路径0–891–3726–907–1。source/candidate各parse1，sourceBFS0；11.414157660/120CPU。比最新所见主表/URSA16384+32、旧本地16389+27，globalpriorityUNKNOWN。',
    lesson_and_restart_condition='This round pairs one old715 structural question with one familiarD4 construction that produced a real accepted graph. It does not abandon the15oldcells or authorize33+packing/copy/field ladders. Stop production and all BFS after this exact acceptance. New concreteLean and ARIS remain pending and must be disposed on their actual newscope outputs.',
    restart_condition='Root-directed final formal/review work for this exact newversion; no repeatedBFS or automatic33+search.',
    unclosed_gap='Latest global priority/originality UNKNOWN;new concreteLean and newscopeARIS not yet accepted.',
    other_metrics=dict(validated_graph_instances=[instance],new_graphs=1,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
        new_lower_bound_mathematically_verified=True,mathematically_validated_complete_graph=True,
        parent_experiment_id=parent,previous_accepted_order=16389,previous_accepted_version_unchanged=True,
        source_n=15552,source_m=116316,source_reproduction_count_increment=0,all_oldedges_retained=116316,
        ordered_fullN_roles=864,new_edges=12924,new_new_edges=0,max_old_pin_load=1,
        center_degree_histogram=g['center_degree_histogram'],degree_histogram=g['degree_histogram'],
        source_raw_parses=1,candidate_parses=1,source_only_BFS_roots=0,final_graph_BFS_roots=16416,
        allorderedpairs_within4=269485056,everyroot_eccentricity=4,
        old_R4_prediction_min=6966,actual_old_R4_range=[13066,13242],root_prediction_mismatches=0,
        genuine_distance4_witness=release['genuine_distance4_witness'],
        independent_acceptance_CPU_seconds=gt['CPU_seconds'],independent_CPU_budget_seconds=120,
        main_URSA_order=16384,main_margin=32,prior_local_margin=27,
        complete_Lean_graph_instance=False,new_concrete_Lean_status='PENDING',
        new_scope_ARIS='PENDING_NOT_INHERITED_FROM16389',global_priority='UNKNOWN',global_record_certified=False),
    evidence_paths=pathsG)

Q=S+'stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/'
q,qt=read(Q+'RESULT.json'),read(Q+'TERMINAL.json')
assert q['status']=='SUPPORTED_MIN_H_DEGREE2_NO_MIN3_TIGHT_NECESSARY_CASES_ONLY'
assert q['paper_corollaries']['minimum_helper_degree_required']==3 and q['paper_corollaries']['min_degree_3_still_open']
assert q['old_source_CORE_design_BFS_rechecks']==q['H_graphs_generated']==q['solver_runs']==0
assert qt['stop'] and qt['active_processes']==0
id715='ddp-stale-d11d3-715-cross-oldclass-helper-min3-tight-route-tradeoff-20261101'
paths715=evidence(Q,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json'])+optional(Q,['ROOT_DISPOSITION.json'])
row715=dict(id=id715,title='11D3旧715允许跨旧class边：排helper最低度2，剩minimum3的两种极紧路线预算；未排一般mixedH',
    family='Retained-source helper routing',idea_family=existing[old715]['idea_id'],date='2026-11-01',
    wiki_verdict='partial',record_type='paper_necessary_route_capacity_boundary',
    target_Delta=11,target_D=3,savedL=715,baseline_date='2026-11-01 saved main715;source/core/design inherited',
    n=dict(actual=None,hypothetical=None),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='Paper route accounting and one small scalar integer-budget check;no H graph or candidate/BFS',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=3,
    scope='Retain all oldedges of actual715 P3/core source,but allow newold-old edges across eligible oldclasses,arbitrary finite helperH and helper-old spokes,max11/D3. Core520 stays saturated. Inherit accepted actualclass/core and Steiner moment inputs;no source/design revalidation. This enlarges the old fixed-induced strictNO scope and is not covered by that oldNO. No deletion/replacement or changedsource.',
    outcome_class='PARTIAL_CROSS_CLASS_SCOPE_MIN3_TWO_TIGHT_NECESSARY_CASES_STOP',new_lower_bound=False,
    distance_text='首次把h–ownpin–原P3邻居–crossedge路线、共享pin的helper reentry及center/leaf端口损耗一起计入。r=min degree_H，a=11−r：E≤3a+3b+a(10r−b)+3c+(a−1)s+a+3z。r2时≤159<195，排min2；继承moment加纸面partition边界排r0/1与r≥4。剩r=3恰8个不同class的leafpins，z=u=δ=0，只能(b,c,s)=(20,8,0)或(21,7,1)，邻helper度数和必须13或12；cycle和purecubicH不行。一般mixedH/min3仍UNKNOWN，0H枚举/0图，只有.022236/5CPU小整数预算核对，不是新source验收。',
    lesson_and_restart_condition='Stop this paper boundary,not generalmin3nonexistence. A future mixedH proposal must realize eight distinct leafpins and one of the two exact route/neighbor-degree cases while controlling overlap. Do not rerun oldfixed-inducedNO,cycle orpurecubicH;do not infer an arbitrary-helper-familyNO after crossclass edges are allowed. No Hsearch or newnumerical batch is authorized here.',
    restart_condition='A concrete mixedmin3H rule consistent with both core coverage and eligible endpoint route budgets,under a separate bounded computation decision.',
    unclosed_gap='Existence or impossibility for general mixedH with minimumdegree3 remains open;no completegraph candidate.',
    other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,
        parent_fixed_induced_node=old715,allows_cross_oldclass_edges=True,all_oldedges_retained=True,
        minimum_helper_degree_exact_necessary=3,own_leafpins_distinct_classes=8,
        necessary_b_c_s_cases=[[20,8,0],[21,7,1]],necessary_neighbor_helper_degree_sums=[13,12],
        minimum2_maximum_eligible_cover=159,required_eligible_vertices=195,
        centerpins_z=0,unused_leafslots_u=0,core_budget_excess_delta=0,
        pure_cubic_or_cycle_H_excluded=True,general_mixed_min3_H_excluded=False,
        H_graphs_generated=0,H_searches=0,source_core_design_BFS_rechecks=0,
        scalar_budget_check_CPU_seconds=qt['CPU_measured_process_seconds'],CPU_budget_seconds=5,
        source_facts_inherited_not_new_acceptance=True,terminal=True),evidence_paths=paths715)
rows=[rowG,row715];newids=[r['id'] for r in rows]
assert all(i not in existing and not(W/'experiments'/f'{i}.md').exists() for i in newids)

# Packing belongs to the already canonical source/whole-plane node,not a new method.
K=BASE+'controller_pack32_gate/';k,kt=read(K+'RESULT.json'),read(K+'TERMINAL.json')
assert k['status']=='FOUND_GE32_CONTROLLER_INTERFACE_ONLY' and k['actual_selected_count']==32
assert k['incumbent_binding']['integer_incumbent_valid'] and kt['all_processes_terminal']
packing=dict(status=k['status'],selected_count=32,selected_controllers=k['selected_controllers'],
    target_load_histogram=k['incumbent_binding']['target_load_histogram'],all192_target_rows_bound_once=True,
    old31_was_not_an_optimum=True,new32_is_not_an_optimum=True,objective='zero feasibility,sumx>=32',
    solver_optimal_label_is_not_cardinality_optimality=True,actual_solver_calls=1,
    cumulative_CPU_seconds=kt['cumulative_charged_CPU_seconds'],CPU_budget_seconds=45,
    fullplane_W='x1=0,27 offsets per selected controller',actual_resulting_graph_node=idG,
    new_method_increment=0,automatic33plus_or_field_search=False,terminal=True,
    evidence_paths=evidence(K,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json','MODEL.json','SELECTED_BLOCKS.json','TARGET_LOAD_BINDING.csv']))
T=S+'stale_record_transfer_d3D10/source1250_interface/';t,tt=read(T+'RESULT.json'),read(T+'TERMINAL.json')
assert t['bipartite'] is False and t['new_HTTP_downloads_raw_parses_degree_checks_2color_BFS_candidates']==0
assert t['existing_two_cut_scope']['anchored_objects']==5614 and tt['all_processes_terminal']
revisit=dict(status=t['status'],source='ConderC1250.2',source_n=1250,source_m=1875,
    actual_source_nonbipartite=True,new_source_acceptance=False,new_numeric_experiments=0,
    inherited_single_subdivision_all1875_by_edge_transitivity=True,inherited_anchor=[0,1],
    inherited_newroot_distance11_target1178=True,inherited_two_cut_5614_allfail=True,
    new_oldsource_D10_BFS_parses_degree_2color_HTTP=0,
    bipartite_automatic_coverage_lemma_premise_not_satisfied=True,
    genuine_three_cuts_or_repair='UNKNOWN_NOT_RUN',new_method_increment=0,
    stop='No rerun1875singleedges,old5614two-cutobjects oralternate source;no automatic threecut/repair batch',
    CPU_seconds=tt['total_charged_CPU_seconds'],CPU_budget_seconds=5,
    evidence_paths=evidence(T,['PRED.md','NOTE.md','RESULT.json','TERMINAL.json']))
upserts=[dict(id=parent,metric_key='controller_pack32_same_wholeplane_feasibility_terminal',metric=packing),
         dict(id=conder,metric_key='latest_source1250_readonly_revisit_and_STOP_20261101',metric=revisit)]
oldtexts={i:(W/'experiments'/f'{i}.md').read_text() for i in [parent,conder,old715]}
assert all(LABEL not in txt for txt in oldtexts.values())
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and END in text and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
mdpath=W/'DDP_METHOD_LEDGER.md';assert LABEL not in mdpath.read_text()
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
uppath=OUT/f'{LABEL}_UPSERTS.json';uppath.write_text(json.dumps(upserts,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
norm=[]
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):
    for r in rows:
        n=c['normalize'](r);n['goal']['baseline_date']=r['baseline_date'];c['write_node'](n);norm.append(n)
for u in upserts:
    old=existing[u['id']]
    for container in [old.setdefault('other_metrics',{}),old['source_record'].setdefault('other_metrics',{})]:container[u['metric_key']]=copy.deepcopy(u['metric'])
    for container in [old['evidence_paths'],old['source_record'].setdefault('evidence_paths',[])]:
        container.extend(p for p in u['metric']['evidence_paths'] if p not in container)
    old['updated_UTC']=NOW
parentdelta='旧16389原图、完整具体Lean及原目标A/B/distinctfreshC全部实际PASS保留，不由新版本覆盖。32整plane可行性已实际FOUND：32selected、192targetrows完整一次绑定、160load1/32load0；零目标sumx≥32的solver“optimal”只指可行门，31与32都不是最大packing证明，累计10.139132516/45CPU。它沿用同一source/whole27/fullN机制，0新方法，不自动搜33+。实际新864clone/16416版本已fresh全根验收，见['+idG+']('+idG+'.md)；该新版本的具体Lean和ARIS此刻仍待实际终态，不继承以上16389的完成状态。'
conderdelta='本轮仅回看既有ConderC1250.2来源/旧scope：实际nonbipartite，不能套bipartite自动细分覆盖。单细分anchor新根到1178距11、edgeVT覆盖全部1875旧边，以及5614两cut/相邻helper对象全首新根R10失败，均严格继承、0重跑。0新HTTP/rawparse/degree/2color/BFS/候选，.122109397/5CPU；不是新source验收或新方法。STOP以上exactscope；真正threegenuinecuts/repair仍UNKNOWN且未运行，不自动派发。原完整结论与证据保留。'
for rid,delta in [(parent,parentdelta),(conder,conderdelta)]:
    (W/'experiments'/f'{rid}.md').write_text(oldtexts[rid]+'\n\n<!-- '+LABEL+' -->\n## '+NOW+' 同机制最新增量，原验收历史保留\n\n'+delta+'\n')
(W/'experiments'/f'{old715}.md').write_text(oldtexts[old715]+'\n\n<!-- '+LABEL+' -->\n## 后续放开跨旧class边的范围（旧strictNO保持）\n\n以上strictNO保留旧诱导邻接，不含跨class新old-old边。新扩域得到minHdegree3及两种极紧必要参数，一般mixedmin3仍未排；不是把旧NO外推。见['+id715+']('+id715+'.md)。继承design/core不新验收，不跑Hsearch。\n')
update=dict(path='research-wiki/experiments/'+id715+'.md',date='2026-11-01',note='Cross-oldclass allowed enlarged scope has onlymin3/tightnecessarycases;oldfixedinducedNO preserved.')
for container in [existing[old715].setdefault('other_metrics',{}),existing[old715]['source_record'].setdefault('other_metrics',{})]:container.setdefault('later_scope_updates',[]).append(copy.deepcopy(update))
for n in norm:existing[n['id']]=n
L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW)
for key in ['validated_named_graph_examples','validated_graph_examples_including_novelty_pending']:L[key]=153
for key in ['saved_main_table_improvement_graph_examples','valid_new_graph_examples','confirmed_publictable_graph_examples']:L[key]=105
L['input_counts'][str(rawpath.relative_to(R))]=2;L['input_counts'][str(uppath.relative_to(R))]=2
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
def table(n):
    safe=c['safe'];return '| ['+safe(n['title'])+'](experiments/'+n['id']+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
md=mdpath.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,f'本页有{len(existing)}条记录；不以此宣称{len(existing)}种独立方法。',1)
top=re.search(r'^更新：[^\n]+',md,re.M);assert top
summary='更新：'+NOW+'。超过保存主表基线4参数／105例；数学合法共153例／43参数。已知被更大公开构造超过43例（其中40例同时超过保存主表）；保存主表外新颖性待核45例／38参数。完整具体公式图Lean46例；16416新实例Lean/ARIS待实际终态。以上主表计数不是全球纪录认证，全球确认0，旧11/12参数的全球状态不由此推定。'
md=md[:top.start()]+summary+md[top.end():]
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 一线老715新约束＋一线熟悉D4真实新图\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+'\n'.join(table(n) for n in norm)+'\n\n同机制packing32仅upsert[原source/whole27节点](experiments/'+parent+'.md)，不另计方法；[Conder1250旧节点](experiments/'+conder+'.md)仅加只读回看/STOP，不新计来源门。旧16389合法＋完整Lean/ABfreshC保留，16416只计mathactual，未借旧审查。图+1／参数0／Lean0／独立方法0；153/43/46，savedmain105/4，outside45/38，known43（overlap40），global0。同Goal ACTIVE、旧N8/n61暂停，15老格主线保留，不自动33+或放弃老题。\n';mdpath.write_text(md)
nav='<!-- '+LABEL+' -->\n### 2026-11-01 最新actual：16D4/16416新图独验通过；老715跨class路线边界推进\n\n同一Goal本轮两问题：一线老715＋一线熟悉D4。新16416/129240/max16/exactD4已root接受，864实际fullN、12924新边、116316旧边全保、newnew0/oldload1；唯一fresh全16416roots/269485056orderedpairs、sourceBFS0，11.414157660/120CPU。每根oldR4实测13066..13242支持≥6966预测。比当前所见main/URSA16384+32、旧local16389+27；globalpriorityUNKNOWN。此刻新concreteLean/ARIS仍PENDING，不继承旧16389完整Lean与ABfreshC；旧版本保持合法。packing32为同一whole27机制零目标可行门，10.139132516/45CPU、非optimum，不33+。\n\n715允许跨oldclass新边后，必须minHdegree3、8distinctclass leafpins，(b,c,s)仅20/8/0或21/7/1，邻helper degreesum13或12；cycle/purecubicH排，一般mixedmin3未排，0Hsearch/图；旧design继承。1250只读回看明确nonbip，继承全部1875single-subdivision和5614two-cut严格失败，0重跑；threegenuinecuts/repair UNKNOWN未运行。保留人工15老格（14十年以上＋1八年）＋Moore余量，不把熟悉图新版本冒新方法，不因老题难就弃线。\n\n现在actual153图／43参数／Lean46，savedmain105/4，outside45/38，known43（其中overlap40），全球确认0；新图+1、参数0、Lean0，旧N8/n61暂停、同Goal ACTIVE。\n\n'+ '；'.join('['+n['title']+'](experiments/'+n['id']+'.md)' for n in norm)+'；[同机制packing更新](experiments/'+parent+'.md)；[1250恢复STOP](experiments/'+conder+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
    path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
    if fn=='index.md':
        match=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert match
        text=text[:match.start()]+f'## Experiments ({int(match[1])+2})'+text[match.end():];pos=text.index('\n',match.start())+1
        text=text[:pos]+''.join('- `exp:'+n['id']+'` — '+n['title']+(' [yes]\n' if n['id']==idG else ' [partial]\n') for n in norm)+text[pos:]
    assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': canonical two newnodes only(one accepted16416 graphversion ofsamewhole27/fullN mechanism;one715enlargedcrossclasspaperboundary),upsertpacking32 inside existing15552/16389canonicalnode,no extra method;Conder1250readonlySTOP attached toexistingnode. Original16389math/Lean/ABfreshC preserved;new16416concreteLean/ARIS pendingnotinherited. Human15oldcells top preserved;counts153/43/46,savedmain105/4,outside45/38,known43overlap40/global0;no33plus,no repeatedBFS,no import/rebuild.')
after=read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count']==before+2 and after['validated_named_graph_examples']==153 and after['complete_Lean_graph_instances']==46
assert after['validated_named_parameter_pairs']==43 and after['saved_main_table_improvement_graph_examples']==105
assert after['known_publicly_dominated_graph_examples']==43 and after['pending_outside_saved_table_graph_examples']==45
receipt=dict(status='PASS_TWO_NEW_NODES_AND_TWO_EXISTING_MECHANISM_UPDATES',updated_UTC=NOW,
    records_before=before,records_after=after['record_count'],records_added=2,new_experiment_ids=newids,
    graph_increment=1,parameter_increment=0,Lean_increment=0,independent_method_increment=0,
    counts=dict(graphs=153,parameters=43,complete_Lean=46,savedmain_graphs=105,savedmain_parameters=4,
        outside_savedmain_graphs=45,outside_savedmain_parameters=38,known_publicly_dominated=43,
        dominated_also_savedmain=40,confirmed_global_records=0),
    packing_existing_canonical_node=parent,packing32_claimed_maximum=False,
    conder_existing_canonical_node=conder,conder_new_experiment_node=False,
    old16389_original_text_math_Lean_ARIS_preserved=True,new16416_Lean_and_ARIS_pending=True,
    old715_original_strict_scope_preserved=True,general_mixedmin3_H_excluded=False,
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    source_graph_BFS_solver_Lean_ARIS_remote_hash_runs=0,root_STATE_docs_HTML_REPORT_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True,sameGoal='ACTIVE',old_N8_n61='PAUSED',
    CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
