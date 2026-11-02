"""Capture the two actual new generative experiments; leave final query pending."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'aris_repo/tools' / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


helper, capture = module('research_wiki'), module('capture_filter')


def screen(text):
    assert not capture.screen(text), capture.screen(text)
    return text


def load(relative):
    return json.loads((HERE / relative).read_text())


def evidence(folder):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / folder).rglob('*'))
            if p.is_file() and p.suffix in {'.md', '.json', '.py', '.cpp'}
            and '__pycache__' not in p.parts]


hyper = load('f5_induced_hyperplane3000/RESULT.json')
transversal = load('f5_induced_transversal_deletion/RESULT.json')
closure_model = load('f5_induced_retention_closure/MODEL.json')
closure = load('f5_induced_retention_closure/CEGIS_TERMINAL.json')
gate = load('d14_D5_K2_route_gate/RESULT.json')
k2model = load('d14_D5_K2_route_gate/K2_model/MODEL.json')
greedy = load('d14_D5_K2_route_gate/K2_model/GREEDY_CONTROL.json')
assert (hyper['n'], hyper['m'], hyper['degree_histogram']) == (3000, 24000, {'16': 3000})
assert hyper['root_R3_size'] == 2231 and hyper['root_R3_missing'] == 769
assert hyper['bad_pair_old_ids'] == [1, 626] and hyper['bad_pair_induced_distance'] == 4
assert hyper['global_diameter_computed'] is hyper['global_bad_pair_count_computed'] is False
assert closure['status'] == 'UNKNOWN' and closure['actual_solver_calls'] == 1
assert closure['running'] is False and closure['pending'] == []
assert (closure_model['variables'], closure_model['clauses']) == (300221, 1170873)
assert closure_model['closure_clauses'] == 32250
assert closure_model['equivalent_uncompressed_intermediate_implications'] == 4031250
assert gate['completed_R3_roots'] == 3685 and gate['zero_R3_provider_targets'] == 0
assert (gate['minimum_R3_provider_count'], gate['maximum_R3_provider_count']) == (25, 119)
assert gate['new_R4_runs'] == 0
assert (k2model['selector_variables'], k2model['all_variables'],
        k2model['initial_total_clauses']) == (7370, 103180, 203308)
assert greedy['root_missing_counts'] == [3881, 3559]
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
existing_ids = {r['id'] for r in before['rows']}
ids = ['ddp-f5-literal3750-induced-retention-max16-d3-20261029',
       'ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029']
assert before['record_count'] == len(before['rows'])
new_rows = sum(identifier not in existing_ids for identifier in ids)
assert before['record_count'] in {372, 374}

f5 = dict(
    id=ids[0], title='LiteralF5 induced vertex retention: failed3000/16regular control, transversal obstruction and general closure UNKNOWN',
    family='four-label affine route-chart lifts',
    idea_family='idea:ddp-q3-three-step-plane-pencil31',
    record_type='complete-failed-induced-graph-and-general-retention-necessary-model',
    target_Delta=16, target_D=3, savedL=1920, baseline_date='2026-10-26',
    n=dict(actual=3000, hypothetical=None), actual_graph_Delta=16,
    actual_D=None,
    actual_D_scope='One induced-root BFS reaches distance5; global diameter and global unordered bad-pair total were not measured.',
    ordinary_bad_unordered_pairs=None, outcome_class='FAILED_FIXED_GRAPH_TRANSVERSAL_PAPER_EXCLUDED_GENERAL_RETENTION_UNKNOWN',
    scope='Fixed literal3750/37500 source: retain arbitrary vertices and all induced edges, seek>=1921 vertices with maximumdegree16 andD3. This differs from keeping all3750 vertices and deleting edges. A single3000-point hyperplane rule was generated and failed; the broader four-direction transversal deletion family is paper-excluded. General arbitrary-retention necessary closure model is UNKNOWN, not excluded.',
    failure_or_result='One complete3000/24000/16regular induced graph: old1→626 distance4, rootR3=2231/missing769; root distance5 count2, globalD/badpairsnull. General300221vars/1170873clauses model single15-second round UNKNOWN,0SAT candidates/0exactcuts.',
    positive_guarantees=[
        'The failed3000-point graph and old-label map are saved; no failure inferred solely from a score.',
        'General3750 keep-variable model preserves every candidate satisfying inducedD3/max16/order>=1921; its current closure constraints are only necessary.',
        'Old pure-edge criticality does not exclude vertex retention; removed endpoint obligations can disappear.'],
    other_metrics=dict(
        source_n=3750, source_m=37500, source_degree=20, source_D=3,
        source_literal='research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges',
        actual_failed_graph_n=3000, actual_failed_graph_m=24000,
        actual_failed_graph_degree=16, actual_failed_graphs_generated=1,
        actual_failed_graph_root_BFS=1, actual_failed_graph_root_R3_size=2231,
        actual_failed_graph_root_R3_missing=769,
        actual_failed_graph_root_distance5_vertices=2,
        actual_failed_graph_global_D_computed=False,
        actual_failed_graph_global_bad_pairs_computed=False,
        actual_failed_graph_CPU_seconds=hyper['CPU_seconds'],
        general_keep_variables=3750, general_minimum_order=1921,
        general_closure_all_variables=300221, general_closure_clauses=1170873,
        compressed_unique_route_clauses=32250, equivalent_intermediate_implications=4031250,
        closure_solver_status='UNKNOWN', closure_solver_calls=1,
        closure_solver_CPU_seconds=closure['solver_CPU_seconds'],
        closure_total_CPU_seconds=closure['total_CPU_seconds_including_prior_preparation'],
        closure_new_candidates=0, closure_actual_bad_pair_cuts=0,
        closure_running=False, general_induced_family_excluded=False,
        new_record=False, cross_model_transversal_review_status='PENDING'),
    variants=[
        dict(label='one_literal_four_direction_hyperplane_3000_control_20261029',
             status=hyper['status'], n=3000, m=24000, degree=16,
             old_unique_path=[1,2250,3625,626], removed_internal_vertices=[2250,3625],
             induced_counterexample_distance=4, actual_one_root_distance_histogram=hyper['root_distance_histogram'],
             old_source_BFS_runs=0, induced_BFS_roots=1, CPU_seconds=hyper['CPU_seconds'],
             theoretical_fiber0_to5_bad_unordered_lower_bound=2000,
             theoretical_lower_bound_is_global_measurement=False),
        dict(label='full_four_direction_transversal_vertex_deletion_paper_obstruction_20261029',
             status=transversal['status'],
             scope='Delete exactlyone point from every affine line in each of thefour prescribed directions in each fiber; nonlinear and fiber-dependent deletion allowed.',
             conditional_retained_n=3000, conditional_degree=16,
             unique_controller_path=[0,18,29,5],
             every_retained_fiber5_target_bad_fiber0_sources_at_least=20,
             theoretical_bad_unordered_pairs_lower_bound=2000,
             graph_enumeration_BFS_solver=0, general_arbitrary_retention_excluded=False,
             cross_model_review_status='PENDING'),
        dict(label='all3750_keep_variables_conditional_degree16_unique_geodesic_closure_20261029',
             status='UNKNOWN_TERMINAL', all_variables=300221, clauses=1170873,
             keep_variables=3750, minimum_order=1921, retained_center_maximum_degree=16,
             closure_compressed_clauses=32250, equivalent_intermediate_implications=4031250,
             exact_short_path_CEGIS_refinement_available=True,
             actual_exact_bad_pair_cuts=0, actual_solver_calls=1,
             solver_CPU_seconds=closure['solver_CPU_seconds'],
             total_CPU_seconds_including_preparation=closure['total_CPU_seconds_including_prior_preparation'],
             solver_returncode=closure['rounds'][0]['solver']['returncode'],
             observation_timeout=closure['rounds'][0]['solver']['observation_timeout'],
             actual_SAT_candidates=0, necessary_model_only=True,
             full_induced_D3_hit_requires_actual_check=True,
             running=False, automatic_resume_allowed=False, pending=[])],
    lesson_and_restart_condition='The controlled deletion keeps degree16 exactly but destroys a unique old3path, explaining a concrete miss. Uniform transversal deletion conflicts with endpoint-retention closure. General retention must coordinate unequal fiber sizes and line deletions with conditional degree and shared-route closure; current necessary model UNKNOWN does not exclude it. Stop this bounded batch rather than extend timer or repeat the same hyperplane.',
    unclosed_gap='Arbitrary>=1921-point max16/D3 induced subgraph of this literal3750 source remains open. Transversal paper proof review pending; no new valid graph or bound.',
    report_paths=evidence('f5_induced_hyperplane3000')+evidence('f5_induced_transversal_deletion')+evidence('f5_induced_retention_closure')
        + ['research/ddp/refresh_20261029/f5_induced_hyperplane3000/induced_n3000_d16.edges'])

k2dir = HERE / 'd14_D5_K2_route_gate/K2_model'
k2terminal = k2dir / 'SOLVER_TERMINAL.json'
k2handle = k2dir / 'HANDLE.json'
if k2terminal.exists():
    state = json.loads(k2terminal.read_text())
    numerical_status = state['status']
    running = False
    solver_calls = state['solver_calls']
elif k2handle.exists():
    state = json.loads(k2handle.read_text())
    numerical_status = state['status']
    running = numerical_status == 'RUNNING_SOLE_K2_CEGIS_BATCH'
    solver_calls = None
else:
    state = None
    numerical_status = 'K2_CNF_PREPARED_NOT_SOLVED'
    running = False
    solver_calls = 0
k2 = dict(
    id=ids[1], title='Literal94186 allfree K2 cooperation: newR3 gate, onegreedy control and bounded exact two-root selector model',
    family='fixed-source spare-neighbor route cover', idea_family='idea:ddp-breadth-20261027',
    record_type='fixed-source-two-helper-K2-cooperative-cover',
    target_Delta=14, target_D=5, savedL=94186, baseline_date='2026-10-27',
    n=dict(actual=None,hypothetical=94188), actual_graph_Delta=None, actual_D=None,
    ordinary_bad_unordered_pairs=None, outcome_class=numerical_status,
    scope='Fixed literal94186 source and alloldedges retained. Add adjacenthelpersy,z with <=13distinctoldfreepins on eachside, jointportusage<=oldspare. Exact two-root conditions R4(A)unionR3(B)=V and R4(B)unionR3(A)=V. All3685 oldfreevertices allowed, not the prior singlehelper<=14model or D13fixedP40pool.',
    failure_or_result='All3685newR3balls completed once, oldR4reused; eachtarget25..119R3providers andT0empty, so necessary routegate doesnot reject. One13+13greedy control misses3881/3559oldtargets, not a graphbadpaircount. Initial338targets/676rows selectorCNF has7370primary/103180totalvariables/203308clauses; current actualnumericalstate='+numerical_status+'.',
    positive_guarantees=[
        'FullnewR3cache uses the exact oldfreevertex roworder; oldR4/sourceD5not recomputed.',
        'Jointcapacity correctly permits sharedpins only at the15oldspare2vertices.',
        'Initialcoverage rows preserve allfeasibleK2choices; SATrequires all94186targets on bothsides before a construction claim.'],
    other_metrics=dict(
        source_n=94186, source_m=657452, oldfree_count=3685,
        oldcapacity1_ports=3670, oldcapacity2_ports=15,
        completed_new_R3_roots=3685, source_reads=1, old_R4_cache_reads=1,
        old_R4_recomputed=0, source_D5_BFS=0,
        R3_provider_minimum=25, R3_provider_maximum=119, zero_R3_provider_targets=0,
        opposition_edges=0, route_gate_CPU_seconds=gate['aggregate_CPU_seconds'],
        greedy_calls=1, greedy_pins_per_side=[13,13],
        greedy_two_root_missing=[3881,3559], greedy_single_R4_missing=[5157,4654],
        greedy_legacy9754_missing=[445,323], graphs_generated=0,
        selectors=7370, all_variables=103180, initial_clauses=203308,
        initial_targets=338, initial_two_side_rows=676, full_target_system_initially=False,
        gate_and_prepare_CPU_seconds=k2model['gate_and_prepare_CPU_seconds'],
        current_numerical_status=numerical_status, current_running=running,
        solver_calls_at_snapshot=solver_calls,
        fixed_K2_family_excluded=False, new_complete_94187_or94188_graphs=0),
    variants=[
        dict(label='allfree_R3_provider_capacity_gate_and_one13plus13_greedy_20261029',
             status=gate['status'], newR3roots=3685, oldR4recomputed=0,
             minproviders=25,maxproviders=119,T0size=0,opposition_edges=0,
             gate_CPU_seconds=gate['aggregate_CPU_seconds'],
             greedy_root_missing=[3881,3559], greedy_single_helper_full=[False,False],
             greedy_restarts=0,local_swaps=0,graphs_exported=0),
        dict(label='all3685_joint_capacity_exact_two_root_K2_CEGIS_model_20261029',
             status=numerical_status, initial_selectors=7370,
             initial_all_variables=103180,initial_clauses=203308,
             initial_targets=338,initial_rows=676,full_target_system_initially=False,
             own_and_opposite_radii=[4,3],side_pin_limit=13,
             route_conditions=['R4(A) union R3(B)=V','R4(B) union R3(A)=V'],
             actual_state_file=str((k2terminal if k2terminal.exists() else k2handle).relative_to(ROOT)) if state is not None else None,
             actual_state=state, running=running,solver_calls_at_snapshot=solver_calls,
             maximum_calls=6,per_round_solver_window_seconds=15,
             shared_solver_CPU_budget=60,whole_batch_CPU_budget=90,
             SAT_only_refinement=True,first_UNKNOWN_stops=True)],
    lesson_and_restart_condition='Coverage sources must complement acrossbothhelperroots while sharing mostcapacity1ports. T0empty rules out the proposed zero-R3-provider obstruction but proves neither feasibility nor supportindependence. The onegreedy control fails on actualfullmasks; use the explicit jointselector model, not anothergreedyseed or the oldsinglehelperMIP. Continue only within the existing boundedbatch and actualterminal policy.',
    unclosed_gap='AllfreeK2jointcover existence unresolved; initial338targets are only a necessary subsystem. No fullgraph or singlehelperhit has been produced; current state='+numerical_status+'.',
    report_paths=evidence('d14_D5_K2_route_gate')+[
        'research/ddp/refresh_20261029/d14_D5_K2_route_gate/allfree_R3.u64le.bin'])
rows = [f5,k2]
report = f'''# 顶点保留与相邻双helper：实际新增研究问题

3750源顶点删减与旧保全部顶点的纯删边严格不同。唯一完整3000/24000/16regular控制图已失败：old1→626实际距离4，一根R3覆盖2231/漏769，该根还有2点距离5；全图D/坏对未算。逐fiber四方向transversal整域另有唯一三步路线纸面排除、理论至少2000跨fiber坏对，不是实测全图统计，外审pending。任意3750keep的300221/1170873必要闭包模型已实际一轮15秒UNKNOWN，总17.651953418CPU，0候选/精确cuts，不误记仍运行或整族排除。

94186源K2规则是all3685freepoints的联合两rootcover。新3685个R3球只算一次，旧R4直接复用；R3provider25..119、T0空。唯一13+13greedy两root仍缺3881/3559，未生成候选或singlehelper图。初始338target/676row共同容量CNF7370selectors/103180vars/203308clauses；本次读取实际状态为{numerical_status}，只按真实handle/终态记录，不把计划启动当已运行。

为这两个不同的generative问题新增2条aggregateexperiment，复用既有source/idea；实验记录数不是独立方法数。合法图仍104/4、confirmed103/3、Lean1，无新下界。root/progress/专家快照未改，最终query等待本轮真实收束和root状态。
'''
report_path = HERE / 'INDUCED_K2_INITIAL_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows:
    row['report_paths'] = list(dict.fromkeys(row['report_paths'] + [str(report_path.relative_to(ROOT))]))
    screen(json.dumps(row,ensure_ascii=False))
    assert all((ROOT/p).exists() for p in row['report_paths'])
pending = HERE / 'INDUCED_K2_INITIAL_WIKI_ROWS.json'
pending.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
command = [sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run = subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after = json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == before['record_count']+new_rows == 374
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key] == after[key]
gap_path = WIKI/'gap_map.md'
gap = gap_path.read_text()
if '账本现372条实验／来源记录' in gap[:1800]:
    gap = gap.replace('账本现372条实验／来源记录','账本现374条实验／来源记录',1)
    gap_path.write_text(gap)
comments = WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- INDUCED_K2_GENERATIVE_EXPERIMENTS_20261029 -->'
note = f'''
## {NOW} 顶点保留与K2联合覆盖开始按实际对象记账

实际3000/16regular诱导图失败和transversal纸面子域排除，与一般顶点保留closureUNKNOWN分开。K2的3685新R3/旧R4复用、唯一greedy失败与338target初始联合CNF分开，当前实际状态{numerical_status}。两个aggregate实验复用既有idea，账本374不是独立方法数；104/4、confirmed103/3、Lean1保持。外审及余下求解只据真实后续回执更新，最终query待root。[实际范围与证据](../research/ddp/refresh_20261029/INDUCED_K2_INITIAL_WIKI_REPORT.md)。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:out.write('\n\n'+marker+'\n'+screen(note))
with (HERE/'INDUCED_K2_INITIAL_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Recorded two actual generative experiments: fixedF5 induced-retention failed3000control/transversalpaper/generalclosureUNKNOWN, and literal94186 allfreeK2 jointcover newR3/onegreedy/actualmodelstate. Ledger374 experiment/source records, no independentmethod-count or validgraph increase; finalquery pendingroot.')
receipt=dict(status='PASS_INDUCED_K2_TWO_AGGREGATE_EXPERIMENTS_PENDING_FINAL',
    updated_UTC=NOW,record_count=374,new_experiments=new_rows,new_independent_methods_claimed=0,
    experiment_ids=ids,F5_closure_status='UNKNOWN_TERMINAL',F5_failed_complete_graphs=1,
    F5_closure_solver_calls=1,F5_transversal_external_review='PENDING',
    D14_K2_actual_status=numerical_status,D14_K2_running=running,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,complete_Lean_instances=1,
    new_valid_graphs=0,new_lower_bounds=0,final_query_rebuild_after_root_update_pending=True,
    command=command,helper_stdout=run.stdout.strip())
receipt_path=HERE/'INDUCED_K2_INITIAL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(receipt_path.relative_to(ROOT)),
                     record_count=374,K2_status=numerical_status,final_query='WAITING_FOR_ROOT_FINAL'),ensure_ascii=False))
