"""Publish current literal families without repeating mathematical checks."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import json
import runpy
import shutil
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
BASELINE_CHECKED = json.loads((HERE/'BASELINES_REFRESH.json').read_text())['checked_UTC']
common = runpy.run_path(str(ROOT / 'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
data = json.loads((HERE / 'delivery/families.json').read_text())
f11, f12 = data['families']['11'], data['families']['12']
n11, n12 = f11['strongest_n'], f12['strongest_n']
examples = f11['example_count'] + f12['example_count']
edge12 = next(HERE.glob(f'*/graphs/graph_d12_D5_n{n12}.edges'))
assert edge12.exists()
native_path = HERE/'h9_d12_native_changed_base/RESULT.json'
native = json.loads(native_path.read_text()) if native_path.exists() else None
native_note = ''
if native is not None:
    assert not native.get('pending')
    native_note = (f"后续原生位传播生产批：{native.get('accepted_extensions',0)}个完整新点，"
                   f"最终{native['final_n']}；350项全部精确≤2anchor失败，0UNKNOWN、0未试，"
                   f"共{native['CPU_parent_and_all_children_seconds']:.3f} CPU秒。"
                   '42396基图的固定10pin池已无单点补全，同一base不重跑；更晚基图与其它生成规则仍不据此排除。'
                   '无新全源或外审。')
state = (f'当前数学最强：N(11,5)≥{n11}、N(12,5)≥{n12}，共{examples}个不同阶数完整例子，覆盖2个参数。'
         '37631/42377代表图此前全源通过；其后按一次新增degree与完整current-baseR4归纳接受，不重复全源/互审。'
         '完整参数及生成器在research/ddp/more_graphs_20261027/delivery/。完整Lean实例0，Goal ACTIVE，旧D2暂停。')

ledger_path = ROOT / 'research-wiki/DDP_METHOD_LEDGER.json'
ledger = json.loads(ledger_path.read_text())
rows = ledger['rows']
old = next(r for r in rows if r['id'] == 'ddp-h9-qline-d12-family-42377')
raw = copy.deepcopy(old['source_record'])
raw.update(title=f'完整新图族：(12,5)42343–{n12}，共{f12["example_count"]}个阶数',
    n=dict(actual=n12, hypothetical=None), actual_D=5, actual_graph_Delta=12,
    ordinary_bad_unordered_pairs=None,
    actual_D_scope='Every literal step has complete production degree/current-baseR4 coverage. Representative42377 has saved all-source BFS; later graphs accepted by induction without repeat BFS.',
    scope=f'Fixed literal extension sequence from public42342; retain all old edges, complete D5 graphs at every integer order42343..{n12}. Latest strongest not independently all-source rescanned.',
    failure_or_result=f'最强{n12}/m{f12["strongest_m"]}/max12/D5；{f12["example_count"]}个阶数，公开快照42342，提升{n12-42342}。包括完整Q-line和删除饱和pin后的子集邻域，各步完整R4遗漏0；同族不重审旧图。',
    positive_guarantees=['Each accepted full neighbor set has distinct vertices and free current degree slots.',
        'Complete R4 is checked in the actual immediately preceding graph, including all earlier additions.',
        'Retaining all old edges and adding this full neighbor set proves D<=5 inductively; the Moore D4 bound gives exactD5.',
        'Literal generator reproduces the current strongest edge set; representative42377 has the saved independent all-source check.'],
    unclosed_gap='Complete concrete Lean instances remain unfinished. Earlier failures are scoped to their actual bases; no family maximality claim.',
    lesson_and_restart_condition='UNKNOWN is not infeasible. Eight-pin sets plus four anchors produced complete graphs using greedy two-prefix/exact-two-tail search on the changed base. Changed base and changed algorithm effects are not separated; no old-base feasibility claim.')
raw['other_metrics'].update(example_orders=f12['example_orders'], example_count=f12['example_count'],
    strongest_n=n12, strongest_m=f12['strongest_m'], improvement=n12-42342,
    roots_checked=0, last_allsource_order=42377,
    prefix_validation='Complete current-base degree/R4 production induction; strongest does not have a new all-source scan.',
    latest_wholegraph_BFS_executed=False, prior_review_scope_examples=38,
    latest_examples_review_executed=False, source_graph_reverified=False,
    round2_frozen_scope=371, round2_hits=1, round2_exact_failures_at_recorded_base=311,
    round2_current_item_UNKNOWN=1, round2_unattempted=58,
    eightpin_constructive_scope=13, eightpin_constructive_hits=4,
    eightpin_constructive_degree_blocked=7, eightpin_constructive_no_hit=2,
    eightpin_constructive_CPU_seconds=10.39475236, unattempted_8pin=0)
raw['other_metrics'].update(failed_earlier_items_retried=True,
    original_7_retested=True,original_7_retested_indices=[2,3],
    accepted_in_last_batch=4,initial_global_batch_exact_failures=280,
    initial_global_batch_degree_rejected=55)
raw['other_metrics'].pop('rejected_at_recorded_base',None)
raw['other_metrics'].pop('degree_rejected',None)
if native is not None:
    raw['other_metrics'].update(native_changed_base_batch={k:v for k,v in native.items() if k not in ['rows','records','items']},
        accepted_in_last_batch=native.get('accepted_extensions',0),
        current42396_10pin_pool_closed=True,current42396_exact_two_failures=350,
        current42396_degree_blocked_10pin_sets=246)
    raw['lesson_and_restart_condition'] += ' Current42396 full596 ten-pin pool:246 degree-blocked and350 exact<=two-anchor failures. Do not repeat this same-base pool. Two remaining eight-pin cases are not excluded.'
raw['variants'] = [dict(order=n, D5_by_complete_induction=True, not_independent_method=True,
    allsource_BFS_here=n in [42343,42345,42377]) for n in f12['example_orders']]
for sub in ['h9_d12_changed_base_round2','h9_d12_eightpin_constructive','h9_d12_native_changed_base',
            'h9_d12_ninepin_saturated_deletion','h9_d12_ninepin_coreguard']:
    for name in ['REPORT.md','RESULT.json']:
        path = HERE / sub / name
        if path.exists() and str(path.relative_to(ROOT)) not in raw['report_paths']:
            raw['report_paths'].append(str(path.relative_to(ROOT)))
raw['report_paths'].append(str(edge12.relative_to(ROOT)))
for name in ['h9_baer_plane_pool/THEOREM.md','h9_baer_plane_pool/REPORT.md',
             'h9_baer_plane_extensions/REPORT.md','h9_baer_plane_extensions/RESULT.json',
             'h9_baer_plane_extensions/independent_first_new_root.json']:
    if (HERE/name).exists():
        raw['report_paths'].append(str((HERE/name).relative_to(ROOT)))
raw['report_paths'] = list(dict.fromkeys(raw['report_paths']))

negative = dict(id='ddp-h9-d11-ninepin-twoanchor-20261027',
    title='(11,5)删一Q-line pin再补两anchor：240个受控变体无图',
    family='H9 quadric-line extension', record_type='finite-controlled-variant-no-new-graph',
    target_Delta=11, target_D=5, savedL=37628, n=dict(actual=None,hypothetical=37632),
    actual_D=None, actual_graph_Delta=None, ordinary_bad_unordered_pairs=None,
    scope='Fixed current37631 graph,24 original ten-pin sets; delete one mandatory pin per set.240 distinct sets,30 degree-blocked,210 complete exact <=two eligible old-anchor checks.',
    failure_or_result='0新图。210个合法9pin集完整≤2anchor失败，无UNKNOWN、无未试；4.478133 CPU秒。没有把mandatory遗漏数当作整图坏对。',
    positive_guarantees=['For two-anchor search a missing pivot must be covered by at least one of the two anchors; all its eligible coverers were enumerated, with exact second-anchor intersection.'],
    unclosed_gap='This excludes only the240 saved deletions on current37631. Arbitrary nine-pin sets, rewiring and different bases remain untested.',
    lesson_and_restart_condition='Deleting one geometric pin and spending its degree slot on a second anchor does not help these concrete sets. Stop this frozen variant; do not enlarge by random seeds.',
    outcome_class='FIXED240_VARIANTS_NO_NEW_GRAPH',wiki_verdict='partial',
    other_metrics=dict(raw_variants=240,degree_blocked=30,exactly_processed=210,new_graphs_generated=0,
        CPU_seconds=4.478133,unknown_items=0,unattempted_items=0,family_excluded=False,
        source_reaudited=False,all_source_BFS_executed=0),
    report_paths=['research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/REPORT.md',
                  'research/ddp/more_graphs_20261027/h9_d11_ninepin_extensions/RESULT.json'])
new_records = [raw, negative]
stage_rows = HERE/'stage_baer_rows.json'
if stage_rows.exists():
    new_records.extend(json.loads(stage_rows.read_text())['rows'])
transfer_note = HERE/'metacyclic_d5_transfer/wiki_row_suggestion.json'
if transfer_note.exists():
    new_records.extend(json.loads(transfer_note.read_text())['rows'])

deleted_dir = HERE/'h9_d12_ninepin_saturated_deletion'
if (deleted_dir/'RESULT.json').exists():
    dr = json.loads((deleted_dir/'RESULT.json').read_text())
    r = copy.deepcopy(raw)
    r.update(id='ddp-h9-d12-ninepin-saturated-deletion-20261027',
        title='删除唯一饱和Q-line pin并补三anchor：完整42397图',
        record_type='controlled-subset-extension-production',n=dict(actual=42397,hypothetical=None),
        scope='Current42396,126 original ten-pin sets with exactlyone saturated pin; freeze first64,visit45 before production budget. Remove saturated pin,add at mostthree freeoldanchors; no assumption that ninepins retain geometric corecoverage.',
        failure_or_result='1完整图42397/m245877，pool43删13863，anchors3881/22612/41614；45visited=1hit+44limited，81未试，不判整族失败。32.002577父+child CPU，编译未单独计入。',
        actual_D_scope='Accepted by complete actual selectedR4 and currentdegree production induction from42396; no new allsourceBFS.',
        positive_guarantees=['Actual wholegraphR4 covered all42396 vertices, olddegrees remain<=12, newdegree12.','Deleted13863 remained full and was not reinserted.','Saved masks:3881 covers all39 missingcore vertices;22612 and41614 have7 and12 private-extra targets.'],
        lesson_and_restart_condition='FullQline containment is sufficient, not necessary. Removing a saturated pin can work with three anchors; actual global coverage decides. One large-hole case has a unique coreguard, so corehole count alone does not decide difficulty.',
        other_metrics=dict(new_graphs_generated=1,new_lower_bound_mathematically_verified=False,
            represented_in_main_family=True,actual_new_graph_order=42397,
            source_n=42396,deleted_saturated_pin=13863,raw_candidates=126,selected=64,
            visited=45,limited_unknown=44,unattempted_total=81,
            production_parent_and_child_CPU_seconds=32.002577,compile_CPU_separately_measured=False,
            missing_core_before_anchors=39,missing_extra_before_anchors=47,
            complete_selectedR4_missing=0,ordinary_allsource_BFS_executed=0,Lean_complete=False),
        variants=[dict(order=42397,D5_by_complete_induction=True,not_independent_method=True,
                       allsource_BFS_here=False)],
        report_paths=[str((deleted_dir/name).relative_to(ROOT)) for name in
            ['REPORT.md','RESULT.json','first_hit.json','anchor_complementarity.json','coreguard_prediction_check.json','generator_dry_run.json']])
    new_records.append(r)

rare_dir = HERE/'h9_d12_eightpin_rare_target'
if (rare_dir/'RESULT.json').exists():
    r = copy.deepcopy(negative)
    r.update(id='ddp-h9-d12-eightpin-rare-prefix-20261027',
        title='两项八pin稀有目标首选补全：限时UNKNOWN，0新图',target_Delta=12,savedL=42342,
        n=dict(actual=None,hypothetical=42397),scope='Fixedcurrent42396,pools103/577;firstmask mustcoverrarest missingtarget;32x16 bounded prefixes andexacttwo-tail,5CPU peritem.',
        failure_or_result='两项均到时UNKNOWN；10.3142父+child CPU，0图，不排除四anchor可行性。',
        positive_guarantees=['No same-base ten-pin pool repeated; no MIP or extra seed.'],
        unclosed_gap='Neither fullfour-anchor feasibility nor the selected32x16prefix class was exhausted.',
        lesson_and_restart_condition='Changing prefix bias did not produce a graph in the bounded experiment. Stop this run; do not renew the time limit without a different coverage rule.',
        outcome_class='TWO_BOUNDED_CASES_UNKNOWN_NO_NEW_GRAPH',
        other_metrics=dict(new_graphs_generated=0,limited_unknown=2,unattempted=0,
            general_four_anchor_family_excluded=False,allsource_BFS_executed=0),
        report_paths=[str((rare_dir/name).relative_to(ROOT)) for name in ['REPORT.md','RESULT.json']])
    new_records.append(r)

cross_dir = HERE/'h9_d11_cross_pin_anchor_block'
if (cross_dir/'RESULT.json').exists():
    r = copy.deepcopy(negative)
    r.update(id='ddp-h9-d11-cross-pin-block-20261027',
        title='N11交叉line-pin anchors块：21000选择全被实际degree阻断',
        n=dict(actual=None,hypothetical=37633),
        scope='21 unused ten-pin lines,pairwise disjoint,210 pairs and21000 ordered cross-pin choices; eachcrosspin would need two newedges.',
        failure_or_result='210不同pins全部olddegree10，新增两边会达12>11；legalchoices0，无R4/R2/BFS或新图。',
        positive_guarantees=['Only actual currentdegree was needed; no unnecessary coverage calculation.'],
        unclosed_gap='Only thiscross-pin rule oncurrent37631 isclosed; unrelated oldanchors orotherbases remain outside scope.',
        lesson_and_restart_condition='Mutual help cannot bypass oldendpoint degree budgets. Do not run distance tests on this fixed empty feasible domain.',
        outcome_class='FINITE_CROSS_PIN_RULE_DEGREE_INFEASIBLE',
        other_metrics=dict(new_graphs_generated=0,raw_pin_choices=21000,legal_choices=0,
            coverage_BFS_calls=0,allsource_BFS_executed=0),
        report_paths=[str((cross_dir/name).relative_to(ROOT)) for name in ['REPORT.md','RESULT.json']])
    new_records.append(r)

for sub in ['d4_source_transfer','d4_source_transfer/free_prime61_phase_pattern','d4_two_involution_transfer',
            'd4_source_transfer/nonfaithful_actions','d4_crt75_free_translation']:
    path=HERE/sub/'wiki_row_suggestion.json'
    if path.exists():
        new_records.extend(json.loads(path.read_text())['rows'])

guard_dir = HERE/'h9_d12_ninepin_coreguard'
if (guard_dir/'RESULT.json').exists():
    r = copy.deepcopy(negative)
    r.update(id='ddp-h9-d12-ninepin-coreguard-20261027',
        title='N12九pin先修核心再补外围：120项0图，预测被反驳',
        target_Delta=12,savedL=42342,n=dict(actual=None,hypothetical=42398),
        scope='Fixed42397,120 degreelegal saturatedpin deletions after skipping acceptedpool43 and5degreeblocked. Firstanchor mustcoverevery missingcore vertex<41356; remaining at mosttwoanchors coverextras.',
        failure_or_result='96项无单coreguard；24项有guard，其中19项全部guard+exacttwo尾穷尽无解、5项限时UNKNOWN。0图，120项全访问，计时22.6116父+child CPU，初始NumPyimport未计入。',
        positive_guarantees=['No-coreguard only rejects this restricted generationrule, not cooperative three-anchor corecoverage.','P at leastone completehit was actually tested and refuted.'],
        unclosed_gap='Five guarded cases remain time-limited; all-three-anchor feasibility is not excluded for any no-guard case.',
        lesson_and_restart_condition='The successful42397witness does not generalize to a productive coreguard-first batch. Stop thisrestrictedrule; do not renew a timer or declare the entire three-anchor family impossible.',
        outcome_class='RESTRICTED_COREGUARD_RULE_NO_HIT_FIVE_UNKNOWN',
        other_metrics=dict(new_graphs_generated=0,source_n=42397,scope_items=120,no_coreguard=96,
            exact_restricted_nohit=19,limited_unknown=5,prediction_supported=False,
            unattempted=0,all_three_anchor_family_excluded=False,allsource_BFS_executed=0),
        report_paths=[str((guard_dir/name).relative_to(ROOT)) for name in ['REPORT.md','RESULT.json']])
    new_records.append(r)

adj_dir = HERE/'h9_d12_adjacent_line_anchor_block'
if (adj_dir/'RESULT.json').exists():
    r = copy.deepcopy(negative)
    r.update(id='ddp-h9-d12-adjacent-line-anchor-block-20261027',
        title='N12相邻Q-line双点各加anchor：冻结32对精确无完整块',
        target_Delta=12,savedL=42342,n=dict(actual=None,hypothetical=42399),
        scope='Fixed42397;346 degreelegal tenpinlines,59322 degreecompatible pairs. Freeze32pairs by actualbuddy-root residualsupport before coupledoneanchor-per-newpoint check.',
        failure_or_result='32对全部精确无hit；全13895oldanchors及444077个a角色已作exactb交集，0候选图。其余59290兼容pair未算；native0.81731CPU秒。',
        positive_guarantees=['For adjacentnewz/w, exactnew-old distances are min(1+d_B(S,x),2+d_B(T,x)); bothrootcoverconditions and actualoldload constraints were included.'],
        unclosed_gap='Only32 frozenpairs closed. The rest of the compatiblepair family remains untested.',
        lesson_and_restart_condition='A buddyvertex can in principle replace an oldanchor through R3, but these selectedcoupled roles cannot be jointly realized. Stop the fixedbatch; no newseed or thirdpoint.',
        outcome_class='EXACT_FIXED32_COUPLED_PAIRS_NO_NEW_GRAPH',
        other_metrics=dict(new_graphs_generated=0,source_n=42397,degreecompatible_pairs=59322,
            exact_pairs_checked=32,unattempted_pairs=59290,general_family_excluded=False,
            native_CPU_seconds=.81731,allsource_BFS_executed=0),
        report_paths=[str((adj_dir/name).relative_to(ROOT)) for name in ['REPORT.md','RESULT.json']])
    new_records.append(r)
assert not common['capture'].screen(json.dumps(new_records,ensure_ascii=False))
replacement = {}
existing = {r['id']:r for r in rows}
written_ids = []
for r in new_records:
    normalized = common['normalize'](r)
    normalized['goal']['baseline_date'] = '2026-10-27'
    previous = existing.get(normalized['id'])
    if previous is not None and previous.get('source_record') == r:
        normalized = previous
    else:
        common['write_node'](normalized)
        written_ids.append(normalized['id'])
    replacement[normalized['id']] = normalized
rows = [replacement.pop(r['id'],r) for r in rows] + list(replacement.values())
ledger.update(updated_UTC=NOW,rows=rows,record_count=len(rows),new_lower_bounds=2,
    mathematical_new_lower_bounds=2,mathematically_improved_parameter_pairs=2,
    valid_new_graph_examples=examples,formally_completed_new_lower_bounds=0)
ledger['input_counts']['../more_graphs_20261027/wiki_rows.json'] = len(new_records)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
page = common['render'](rows).replace('## 家族目录',state+'\n\n## 家族目录',1)
assert not common['capture'].screen(page)
(ROOT/'research-wiki/DDP_METHOD_LEDGER.md').write_text(page)
(HERE/'wiki_rows.json').write_text(json.dumps(dict(updated_UTC=NOW,rows=[r['source_record'] for r in rows if r['id'] in {x['id'] for x in new_records}]),ensure_ascii=False,indent=2)+'\n')

for name in ['AGENTS.md','RESEARCH_BRIEF.md','context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
             'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md','research-wiki/gap_map.md']:
    path = ROOT/name
    text = path.read_text()
    import re
    text = re.sub(r'当前数学最强：N\(11,5\)≥\d+、N\(12,5\)≥\d+[^\n]*',state,text)
    text = text.replace('数学验收新下界1项，完整Lean仍0项。','数学验收改进参数2项，完整Lean仍0项。')
    if name.endswith('NEXT_SESSION.md'):
        if text.startswith('# 当前生产快照'):
            text = text.split('\n---\n',1)[1].lstrip()
        historical_banner='以下是较早快照与历史恢复安排；与上方当前快照冲突时不派发。'
        while text.startswith(historical_banner):
            text=text[len(historical_banner):].lstrip()
        text = f'# 当前生产快照 — {NOW}\n\n{state}\n\n真正新机制：13raw Baer PG2(F3) meets everyF9hyperplane by rank-nullity，折叠11pins+anchor41666产出42398/m245889，parent只一次freshnewroot检查0.296CPU、最远5；旧fullsource不重跑。第一个364flatplanes池410，实际364mandatorycore检查全通过，1hit/363coveragefail/46degreeblocked；完整literal已append旧58保留。另756nonflat F3planes池34cap0全extras失败，N11全1120F3singularplanes的Baerdegree池为空。这些均终态，勿重跑。\n\n当前新scope是h9_baer_nonstable_global_pool/：PAIRING.json已核所有实际π二点fibers为p/Frob3p；任何可把13raw折到≤12的非stable Q9plane必须含唯一F3singularline。全部3640lines每条6nonstableplane=21840，旧1120stable排除且不复跑。逐line eligible unsplit taupair必要数N11≥2/N12≥1可剪枝。完整推导见h9_baer_galois_plane_filter/THEOREM.md。pool/生产按各自实际RESULT与livehandle判断，不把派发当完成；新候选同Baer规则无需逐图外审或oldBFS。\n\n已闭且不自动恢复：两饱和删pin29有限前缀0图；D8xC2 fibre64Aut*15h的AAAA最多12/16，整个统一规则闭；Loz parallelprofile1/9/8/8的70699scope0图；Michel p43 canonical2与gauge后7,000,402项0图；S5/SL2(F5) degree4 Cayley全部29542项0图。N11全几何onefault17 exacttwo全失败，不与旧240混淆。具体范围见各REPORT/Wiki，均不外推一般图。旧N10MIP/1152repair/D2不重启。{native_note}\n\n---\n\n'+historical_banner+'\n\n'+text
    if name.endswith('RESEARCH_GOAL.md'):
        text = text.replace('实际分工：一代理完成42343后剩余六条Q-line的有限扩张；',
                            '历史分工（现已全部终态，勿据此派发）：一代理完成42343后剩余六条Q-line的有限扩张；')
    path.write_text(text)
comments = ROOT/'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md'
with comments.open('a') as stream:
    stream.write(f'\n\n## {NOW} 验证适量的实际执行结果\n\n{state}\n\n按最新trade-off复用旧图和未变覆盖代码，无新增全源BFS或互审。八pin四anchor规则命中4例，13项仅10.395CPU。{native_note} N11受控240变体完整终态4.478CPU、0图即停；C5四根迁移无图即停。结果与证据已追加唯一Wiki及原主family，未重导Wiki或完成Goal。\n')

# Keep proof text concise and current; the externally reviewed38 snapshot is separate.
proof = f'''# Two improved parameters, {examples} complete examples

N(11,5)≥{n11}; N(12,5)≥{n12}. The checked public source values are37628 and42342 (official D5 description checked{BASELINE_CHECKED}). These are lower-bound improvements, not optimality or public acceptance claims.

## Complete graph families

The literal family gives every order37629..{n11} at maximum degree11 and42343..{n12} at maximum degree12, all with exact diameter5. Different orders guarantee distinct graphs; these are two parameter families sharing one geometric mechanism. The complete base graphs belong to Dharunish Yugeswardeenoo; the partial-fold/duality foundation belongs to Rishabh Rajiv.

Keep every edge of the current graph B, and add z with the saved complete neighbor set S. Each neighbor has a free degree slot, |S|≤Δ, and the actual complete R4_B(S) covers every vertex of B. Thus every new-old pair has distance≤5; every old-old route is retained. Each step is checked in its actual earlier graph, so induction proves every prefix. Since each order exceeds Moore(11,4)=12222 or Moore(12,4)=17569, respectively, the diameter is exactly5. This does not infer prefix validity by deleting vertices from the largest graph.

Previously saved independent all-source checks cover37629,37631,42343,42345 and42377; the representative graphs have0 bad/unreachable pairs. Subsequent steps use one production degree+complete current-baseR4 check per new vertex, with no repeated wholegraph BFS, model review or Lean audit. The model review covers the earlier38 examples. Later unchanged-rule production is accepted according to the user's explicit trade-off.

## Latest concrete production

42391→42392: frozen371 changed-base ten-pin candidates,1 hit within82.003 production CPU seconds;311 exact failures at their recorded bases,1 UNKNOWN and58 unattempted. No claim of final-base maximality.

42392→42396:13 eight-pin candidates,4 hits,7 degree-blocked,2 bounded-search no-hits. Greedy first-two anchors followed by exact-two-tail completion cost10.39475236 CPU seconds for the entire batch. Each complete12-neighbor set passed actual full R4. The base also changed since the older MIP UNKNOWN; no old-base feasibility claim is made. The finite eight-pin production batch is complete.

{native_note}

Nine-pin saturated deletion produced42397 from42396. Omit the oldfullpin13863 and attach the newpoint to[60,3881,5499,11733,13135,22612,22626,28441,31353,34220,38043,41614]. Actual completeR4 verified all42396oldvertices. No full-line core guarantee was assumed. One anchor covers all39coreholes; the other two have7/12 privateextra targets. The oldbase42396ten-pin closure does not apply to newly changed bases. Related finite negative/UNKNOWN trials are saved separately, not promoted to whole-family impossibility.

The new Baer-plane mechanism produced42398:13raw PG2(F3) points in a totallysingular F9plane meet everypolarhyperplane because a mapF3^3->F9 has a nonzero kernel. The inherited H9polar-distance lemma gives completecoreR4 coverage for their foldedpins. The successful13rawpoints foldto11pins, plus oldanchor41666; fullactualR4 covers all42397oldvertices. A fresh independent edge-list check of the one newroot reachedall42398 at distance<=5; old-old routes are inherited, not rescanned. The complete step/witness is in families.json and h9_baer_plane_extensions/.

Strongest degree12 graph: {n12} vertices,{f12['strongest_m']} edges. All literal parameters and source references are in delivery/families.json; family_generator.py reproduces any saved prefix. This is a complete mathematical construction family. Concrete Lean graph instances remain0; generic extension/certificate-soundness theorems compile, but the final formal Goal remains active.
'''
(HERE/'FINAL_RESULTS_PROOF.md').write_text(proof)

readme = HERE/'delivery/README.md'
history = HERE/'delivery/README_history_57.md'
if not history.exists():
    shutil.copy2(readme,history)
readme.write_text(f'''# {examples}个完整图：当前确定性生成包

| 最大度 | 直径 | 完整例子的阶数 | 例子数 |
|---:|---:|---|---:|
| 11 | 5 | 37629至{n11}，每个整数 | {f11['example_count']} |
| 12 | 5 | 42343至{n12}，每个整数 | {f12['example_count']} |

数学最强N(11,5)≥{n11}、N(12,5)≥{n12}；对照{BASELINE_CHECKED}核对的公开快照37628/42342。不同阶数保证这些图不同，不能把例子数当独立方法数或最优值。完整Lean图实例仍0；Goal ACTIVE。

## 生成任意例子

在解压目录或项目root运行（仅Python标准库，无搜索/BFS）：

```bash
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order {n12} --output graph{n12}.edges
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 11 --order {n11} --output graph{n11}.edges
```

将order改成表内任意整数即可。输出第一行n m，其后每行u v一条无向边。若独立放置程序和families.json，可用`--source /path/to/deg12_diam5_n42342.txt`或degree11对应源文件。程序按字面步骤检查邻集、原度数与实际边数，无外部库或网络依赖。

families.json保存每步完整pins（全邻集）、mandatory_pins、anchors、原degree和证据路径。所有原图边保留，m等于原边数加已用步骤的实际邻集cardinality总和。最新强图边表在`../{edge12.relative_to(HERE)}`。

## 为什么是完整合法图

每次在实际更早图B中，对完整新点邻集S检查R4_B(S)=V(B)，并检查全部新增degree。保留旧边，故旧旧距离不增加，新旧距离≤5。每个步骤独立具备这个完整条件，归纳保证所有前缀，不是从最大图删点推断。

早期邻集包含完整Q-line像；42397步骤改为删去饱和pin13863、保留9pins并补3anchors。该子集不依赖“仍自动覆盖核心”的假设，实际完整R4为其证明。字面完整邻集是[60,3881,5499,11733,13135,22612,22626,28441,31353,34220,38043,41614]。

42398步骤使用新的Baer子平面邻域：13raw点折到11pins，再补anchor41666。它的完整邻集是[1928,2576,7337,8710,14217,14622,23929,30347,34888,35165,40153,41666]。rank-nullity保证core覆盖，实际selectedR4确认全部旧点覆盖；只对该新机制首点作了一次fresh-edge-list newroot独立检查，没有重算旧旧距离。Baer证明与生产见../h9_baer_plane_pool/THEOREM.md、../h9_baer_plane_extensions/REPORT.md。

阶数超过D4 Moore界（degree11为12222、degree12为17569），所以直径恰5。旧全源验收代表为37631/42377；其后的同族生产只验新增degree与完整coverage，不重复全源BFS/互审。旧Gemini审阅覆盖前38例，完整Lean仍未完成。

## 原作者与证据

两份完整基图属于Dharunish Yugeswardeenoo，partial-fold/duality基础归Rishabh Rajiv。原始来源[Zenodo23653049](https://zenodo.org/records/23653049)；原图保存于`research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt`及对应degree12文件。raw adjacency每行是vertex后跟全部邻居，不含n/m头。

本项目的新工作是这些明确增点、有限覆盖构造与可复现参数。source_urls和署名均保存在families.json。完整数学说明见`../FINAL_RESULTS_PROOF.md`，各生产批的REPORT/RESULT保存准确命中、限时未决、未试范围和成本。历史57例说明另存README_history_57.md；旧图与原证据保留，不重算。
''')

baseline = json.loads((HERE/'BASELINES_REFRESH.json').read_text())
for case in baseline['cases']:
    family = data['families'][str(case['Delta'])]
    case.update(new_best_verified=family['strongest_n'],
        improvement=family['strongest_n']-case['public_lower_bound'])
baseline.update(complete_graph_examples=examples, production_updated_UTC=NOW)
(HERE/'BASELINES_REFRESH.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2)+'\n')
summary = dict(updated_UTC=NOW,nodes_upserted=[r['id'] for r in new_records],record_count=len(rows),
    mathematically_improved_parameter_pairs=2,valid_new_graph_examples=examples,
    complete_Lean_instances=0,experiments_rerun=0,actually_written_nodes=written_ids)
(HERE/'WIKI_SYNC_RESULT.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
common['helper'].rebuild_index(str(ROOT/'research-wiki'))
common['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))

html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>更多新图：{examples}例</title><style>body{{max-width:1000px;margin:34px auto;padding:0 22px;font:17px/1.8 system-ui;color:#182839}}h1{{font-size:29px}}h2{{font-size:23px}}.result{{background:#e9f5ed;padding:17px;border-left:4px solid #23834c}}.note{{background:#edf3fa;padding:15px}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ccd8df;padding:9px;text-align:left}}pre{{white-space:pre-wrap;background:#f3f5f8;padding:14px}}a{{color:#155bb2}}</style></head><body>
<h1>{examples}个完整例子，两个参数</h1><p>更新：{NOW}。Goal ACTIVE，范围4≤Δ≤12、D∈{{3,4,5}}。</p>
<div class="result"><table><tr><th>参数</th><th>公开下界快照</th><th>本轮最强</th><th>完整阶数</th></tr><tr><td>(11,5)</td><td>37628</td><td><strong>{n11}（+{n11-37628}）</strong></td><td>37629–{n11}，共{f11['example_count']}例</td></tr><tr><td>(12,5)</td><td>42342</td><td><strong>{n12}（+{n12-42342}）</strong></td><td>42343–{n12}，共{f12['example_count']}例</td></tr></table></div>
<p>这些图全部简单连通、最大度11/12、直径恰5；每个不同阶数是一例。它们共享几何构造机制，不是{examples}种独立方法。最强{n12}图有{f12['strongest_m']}条边。</p>
<div class="note"><strong>按最新trade-off执行：</strong>旧基图与未变代码直接复用，新点只检查实际度数和对全部旧顶点的完整R4覆盖。后续生产没有重复全源BFS、外审或Lean审计。已保存37631/42377的代表全源记录。</div>
<h2>本次具体问题、预测与结果</h2><p>问题：之前四anchor求解返回UNKNOWN的八点邻域，能否用更直接的有限组合规则补全？预测至少一个邻域可以。现在先选两个覆盖较多目标的连接点，再精确找余下两个，最后检查完整旧图覆盖。</p>
<p><strong>预测得到支持：</strong>13项中4项产生42393–42396，7项被实际度数阻断，2项在有限搜索中未命中；整批约10.4 CPU秒。四次实际遗漏均为0。基图也已变化，不能断言这些邻域在原42377上就可行。UNKNOWN保留为未决，未命中也不扩大为全族不可能。</p>
<p>另一批只重看基图变化后的371个十点邻域，约82 CPU秒得到42392；311项在其记录基图下精确失败，1项UNKNOWN、58项未试即按预算停止。Δ11的删一pin＋两anchor受控240项在约4.48 CPU秒完整结束，无新图，未加时续修。</p>
<p>{native_note}</p>
<p><strong>本轮新规则：</strong>删去十pin邻域中唯一满度pin13863，用9个剩余pin加3个anchors，已得到42397点完整图。新增邻集对全部42396旧顶点R4覆盖遗漏0；没有假定不完整Q-line仍自动覆盖核心。此后若有新图，以顶部实际最强值为准。</p>
<p>保存mask显示：anchor3881盖全部39核心漏点，另22612/41614分别有7/12个独有外围目标。此前“大核心洞就没有单guard”的预测被pool196反驳：它有3376个核心洞，却有唯一guard42277。因而实测了coreguard先行的120项新批：96无guard、19受限尾部精确无解、5限时UNKNOWN，0图；“会产生新图”的预测未实现，这条受限规则已停，不能外推全部三anchor无解。</p>
<p>跨参数D4：原Loz相位规则在p61的8个faithful actions均无法盖phase10；11个非faithful actions中532组修好phase10，却全部在phase0/1/2之一失败。连同平凡action的容量界，这个固定profile全部20actions已关闭。改成两条直接phase10连接的特定规则也完整0图。都不外推其它phaseprofiles或CRT环；没有第三参数的完整图。N12相邻line块只精确查冻结32对，0图后停止。</p>
<p>随后把同一r2四逆对规则在所有可改善CRT模数75/93/123/155上的全connectedtranslation类补齐：75/93/123均没有薄层幸存，155由形式容量144&lt;155排除。这个76166类的有限scope已关闭，不沿最佳失败样本微调，也不把失败外推其它相位规则。</p>
<h2>新Baer子平面机制：已产出42398</h2><p>每个Baer子平面有13raw点。任意极化条件是F3上的三变量两方程，必有非零解，所以这些点碰到每个polarhyperplane，折叠邻域保证旧核心R4全覆盖。首次池在364个flatplanes里得到410个度数合法邻域，实际364次core检查均全覆盖；其中13raw折为11pins再加anchor41666，完整覆盖全部旧点，得到42398。</p>
<p>这张图已从完整边表独立重建，只核新root到全图最远5，约0.296CPU秒；旧旧由保留旧边与生成器一致性继承，没有重跑全源。另756个nonflat F3平面的34个cap0候选均漏extras，已停止。正在研究的Galoisplane筛选只保留理论上能发生fold碰撞的新plane，实际结果以该批终态为准。<a href="../research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md">新覆盖证明</a> · <a href="../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md">实际新图与独立新根证据</a></p>
<h2>结果文件与源码</h2><p><a href="../expert_review_current/MORE_GRAPHS_20261027.zip">完整ZIP</a> · <a href="../expert_review_current/MORE_GRAPHS_20261027.html.txt">HTML源码</a> · <a href="../research/ddp/more_graphs_20261027/delivery/families.json">全部字面参数</a> · <a href="../research/ddp/more_graphs_20261027/delivery/family_generator.py">统一生成器</a></p>
<pre>python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order {n12} --output graph{n12}.edges</pre>
<p>将order改为表中任意整数即可生成对应完整前缀。ZIP包含两份原作者图、两张最强图、完整参数、生成器与覆盖源码。<a href="../{edge12.relative_to(ROOT)}">{n12}完整边表</a> · <a href="../research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges">37631完整边表</a> · <a href="../research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md">数学说明</a> · <a href="../research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/REPORT.md">本次预测与实验</a></p>
<h2>证明、署名与剩余状态</h2><p>保留所有旧边，每次新点邻集在实际更早图上的R4覆盖全体旧点，故归纳保证D≤5；阶数大于D4 Moore界，故D恰5。没有从最大图删点推断前缀有效。</p>
<p>原作者Dharunish Yugeswardeenoo；partial-fold/duality基础Rishabh Rajiv。本项目提供这些明确增点与有限覆盖构造。<a href="https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html">官方D5说明</a>于{BASELINE_CHECKED}核对仍为37628/42342；不宣称最优值或已公开接收。Gemini审阅覆盖此前38例；完整实际图Lean实例0，已有通用引理保留，Goal继续。</p>
<p><a href="../research-wiki/DDP_METHOD_LEDGER.md">唯一Research Wiki账本</a> · <a href="../context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md">恢复入口</a></p></body></html>'''
progress = ROOT/'research/progress.html'
snapshot = HERE/'progress_52_snapshot.html'
if not snapshot.exists():
    shutil.copy2(progress,snapshot)
progress.write_text(html)
expert = ROOT/'expert_review_current'
expert.mkdir(exist_ok=True)
(expert/'MORE_GRAPHS_20261027.html').write_text(html)
(expert/'MORE_GRAPHS_20261027.html.txt').write_text(html)
# Reuse existing portable package entries, replace current files, add only the
# new production sources/evidence and strongest edge list. No audit is run.
archive = expert/'MORE_GRAPHS_20261027.zip'
with zipfile.ZipFile(archive) as oldzip:
    paths = {ROOT/name for name in oldzip.namelist()}
paths.update([edge12, HERE/'sync_production.py', HERE/'h9_d12_eightpin_extensions/cover.cpp'])
for sub in ['h9_d12_changed_base_round2','h9_d12_eightpin_constructive','h9_d11_ninepin_extensions',
            'h9_d12_native_changed_base','metacyclic_d5_transfer','h9_d12_ninepin_saturated_deletion',
            'h9_d12_eightpin_rare_target','h9_d11_cross_pin_anchor_block','h9_d12_ninepin_coreguard',
            'h9_d12_adjacent_line_anchor_block','d4_source_transfer',
            'd4_source_transfer/free_prime61_phase_pattern','d4_two_involution_transfer',
            'd4_source_transfer/nonfaithful_actions','d4_crt75_free_translation',
            'h9_baer_plane_pool','h9_baer_plane_extensions','h9_baer_nonflat_F3_pool',
            'h9_baer_nonflat_F3_extensions','h9_baer_galois_plane_filter',
            'h9_d11_single_fault_global_pool','h9_d11_single_fault_extensions',
            'h9_d12_eightpin_two_saturated_deletions','nonabelian16_fibre_preflight',
            'd4_parallel_phase_source','d4_michel684_prime43_transfer',
            'd4_michel684_prime43_transfer/free_projective_scope','small120_cayley_d4']:
    if not (HERE/sub).exists():
        continue
    for path in (HERE/sub).iterdir():
        if path.is_file() and path.suffix in ['.json','.py','.md','.cpp']:
            paths.add(path)
temporary = expert/'MORE_GRAPHS_20261027.next.zip'
with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as output:
    for path in sorted(paths):
        if path.exists():
            output.write(path,str(path.relative_to(ROOT)))
temporary.replace(archive)
downloads = Path('/mnt/data')
downloads.mkdir(exist_ok=True)
for suffix in ['html','html.txt','zip']:
    shutil.copy2(expert/f'MORE_GRAPHS_20261027.{suffix}',downloads/f'AR4MATH_MORE_GRAPHS.{suffix}')
print(json.dumps(summary,ensure_ascii=False))
