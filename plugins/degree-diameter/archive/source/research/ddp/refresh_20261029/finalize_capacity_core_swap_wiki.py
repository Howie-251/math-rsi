"""Finalize the completed route-capacity/core-swap turn in the existing Wiki."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ROOT_STATE_UTC = '2026-10-29 22:34:04 UTC'


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
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / folder).iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.py'}]


def update(row, additions, paths):
    variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
    variants.update({v['label']: v for v in additions})
    row['variants'] = list(variants.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))


root_paths = [ROOT / 'AGENTS.md', ROOT / 'RESEARCH_BRIEF.md',
              ROOT / 'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
              ROOT / 'research/progress.html',
              ROOT / 'expert_review_current/EXPERT_HANDOFF_20261029.md',
              ROOT / 'expert_review_current/build_handoff_20261029.py']
root_before = {p: p.read_bytes() for p in root_paths}
brief = (ROOT / 'RESEARCH_BRIEF.md').read_text()
assert '22:34:04' in brief and '全部数值与外审已终态' in brief
turn = load('C33_CAPACITY_CORE_SWAP_TURN_RESULT.json')
assert turn['status'] == 'ROUTE_CAPACITY_CORE_SWAP_BATCH_COMPLETE_NO_NEW_RECORD'
assert turn['all_numerical_work_terminal'] is True and turn['pending'] == []
assert turn['accepted_totals'] == dict(
    legal_instances=104, parameter_pairs=4, confirmed_main_table_instances=103,
    confirmed_main_table_pairs=3, concrete_formula_Lean_instances=1,
    d20_D3_latest_global_novelty='pending')
chain = load('controller31_chain_full/RESULT.json')
model = load('controller31_chain_full/MODEL.json')
assert chain['status'] == 'UNKNOWN' and chain['running'] is False and chain['solver_calls'] == 1
assert chain['valid_controllers'] == chain['complete3875_graphs'] == 0
assert (model['extra_edge_variables'], model['all_variables'], model['clauses']) == (380, 21722, 74336)
assert model['fixed_internal_edges'] == 33 and model['C33_capacity_cuts'] is False
multiplicity = load('d13_core_swap_static_pool/MULTIPLICITY_LIFT_CHECK.json')
assert multiplicity['status'] == 'FULL_MULTIPLICITY_MAXIMUM_EXACTLY40'
assert multiplicity['all43_upper_bounds_one'] is True
private_witnesses = {
    str(r['candidate_index']): r['minimum_spare_witnesses'][0]['vertex']
    for r in multiplicity['new_set_checks']}
assert private_witnesses == {'0': 7030, '8': 12230, '17': 14782}
release = load('d13_single_port_release_provider_gate/RESULT.json')
assert release['status'] == 'STRICT_EXCLUSION_BY_UNCHANGED_POOL_AND_EDGE_DELETION_MONOTONICITY'
assert release['running'] is False and release['pending'] == []
assert (release['old_port_degree'], release['new_port_degree'],
        release['old_port_capacity'], release['new_port_capacity']) == (11, 10, 2, 3)
assert release['pool_memberships_changed'] == release['new_port_radius4_BFS'] == 0
assert release['source_edge_reads'] == release['solver_calls'] == release['complete_graphs_exported'] == 0
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 372
existing = {r['id']: r for r in before['rows']}
ids = ['ddp-m3-control31-joint-boundary-20261026',
       'ddp-d13-singlefault-star-family-51457-20261027']
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in ids}
experiment_names_before = sorted(p.name for p in (WIKI / 'experiments').glob('*.md'))
claim_names_before = sorted(p.name for p in (WIKI / 'claims').glob('*.md'))

row31 = rows[ids[0]]
chain_variant = dict(
    label='same_overlap_chain_motif_full380_external_edge_model_F5_20261029',
    status='UNKNOWN_TERMINAL', controller_order=31,
    source_literal='research/ddp/second_mechanism/control_unrestricted_n31.edges',
    inherited_source_A3_missing_ordered=4,
    interpretation='Same overlapping-triangle controller mechanism; old88-position fixed46-edge model remains a smaller historical raw-UNSAT scope.',
    motif='Seven-vertex three-triangle chain plus eight disjoint K3 blocks.',
    motif_fixed_edges=33, old_fixed_edges=46, released_old_fixed_edges=13,
    full_legal_external_edge_variables=380, selected_external_edges=29,
    expected_controller_edges=62, all_variables=21722, clauses=74336,
    route_condition=model['route_condition'],
    labeling='Only eight additional K3 blocks use first-discovery parent labels; initial seven motif labels fixed.',
    C33_triangle_factor_capacity_cuts_imported=False,
    intended_F5_target=dict(Delta=20, D=3, conditional_order=3875, graph_generated=False),
    solver_calls=1, solver_option='-t90',
    solver_CPU_seconds=chain['child_CPU_seconds'],
    preparation_CPU_seconds=chain['preparation_CPU_seconds'],
    aggregate_CPU_seconds=chain['aggregate_CPU_seconds'],
    aggregate_CPU_budget=110, running=False,
    valid_controllers=0, complete3875_graphs=0,
    old_timer_continued=False, general31_family_excluded=False,
    old88_raw_UNSAT_promoted_to_certificate=False, order_or_seed_ladder_continuation=False)
update(row31, [chain_variant], evidence('controller31_chain_full'))
row31['scope_closed_or_remaining_raw'] = (
    '历史88位置、46固定边联合模型的rawUNSAT仅限旧局部域且未认证。'
    '本轮保留同一7点三三角链+8K3 motif但只固定33内边，释放13旧固定外边，允许全部380合法外边；'
    '21722变量/74336子句单次90秒UNKNOWN，不排此更大域或一般31控制器。')
row31['metrics_raw'] = row31['metrics_raw'].split('；20261029完整380')[0] + (
    '；20261029完整380外边模型21722变量/74336子句，child90.006668CPU、准备0.122005083CPU、总90.148101772CPU，'
    '唯一-t90 UNKNOWN，0控制器/0个3875图。')
row31['distance_text'] = row31['metrics_raw']
row31['outcome_class'] = 'UNKNOWN_FULL_CHAIN380_OLD88_RAW_UNSAT_UNCERTIFIED'
row31['unclosed_gap'] = '原88局部rawUNSAT不外推新380域；新更大完整域UNKNOWN，F5条件目标3875未生成。旧F3条件目标837仍仅历史，不与新F5混算。'
row31['lesson_and_restart_condition'] = (
    '新模型实际改变旧固定46边的承重路由，满足历史重启条件；'
    '但单次90秒仍UNKNOWN，停止本批，不延长timer或恢复旧交换，不开31/32阶数梯子。'
    '重叠motif不是C33不交三角因子，不移植其局部容量cuts。')
row31['restart_condition'] = 'Further work requires a concrete new shared-route or variable-representation rule; no authorized restart of this timer or an order/seed ladder.'
row31['other_metrics'] = dict(
    full_chain_external_variables=380, full_chain_fixed_motif_edges=33,
    old_boundary_fixed_edges=46, full_chain_CNF_variables=21722,
    full_chain_CNF_clauses=74336, full_chain_solver_status='UNKNOWN',
    full_chain_solver_calls=1, full_chain_solver_CPU_seconds=chain['child_CPU_seconds'],
    full_chain_total_CPU_seconds=chain['aggregate_CPU_seconds'],
    valid_controllers=0, complete3875_graphs=0,
    general31_family_excluded=False, old_raw_UNSAT_certified=False)

rowpool = rows[ids[1]]
variants = {v.get('label', v.get('name')): v for v in rowpool['variants']}
pool_label = 'fixed_peripheral_core_swap_three_new_sets_exact43_pool_max40_20261029'
pool_variant = variants[pool_label]
pool_variant['repeated_new_set_multiplicity_outside_scope'] = False
pool_variant['arbitrary_integer_multiplicity_status'] = multiplicity['status']
pool_variant['all43_individual_integer_upper_bounds'] = 1
pool_variant['new_capacity1_witnesses'] = private_witnesses
pool_variant['multiplicity_extra_graph_reads'] = 0
pool_variant['multiplicity_extra_BFS_or_solver'] = 0
pool_variant['exact_integer_multiplicity_optimum'] = 40
pool_variant['subset_readout'] = (
    'new0=oldS37 minus50578 gives a same-order legal edge deletion;50578 was already free with degree11/cap2, becomes degree10/cap3, so fixedP40 is unchanged.')
release_variant = dict(
    label='single_port50578_edge_deletion_unchanged_P40_provider_chain_20261029',
    status=release['status'], source_n=51457, source_m=324863,
    modified_source_n=51457, modified_source_m=324862,
    deleted_edge=[51454, 50578],
    legal_D_le5_inherited_from='Actual independently covered compatible candidate0 replacing oldS37 in the static40 certificate.',
    new_complete_edge_table_generated=False, same_order_new_record=False,
    old_port_degree=11, new_port_degree=10, old_port_capacity=2, new_port_capacity=3,
    originally_newly_free_port_assumption_refuted=True,
    fixed_P40_membership_changes=0, all_radius_balls_only_shrink_under_deletion=True,
    inherited_provider_elimination_rounds=[39, 1], final_active=[],
    fixed_P40_nonempty_clique_family_excluded=True,
    fixed_P40_other_helper_topologies_cannot_improve_clique=True,
    original_planned_oneB4_run_executed=False,
    source_edge_reads=0, new_port_radius4_BFS=0, new_radius3_BFS=0,
    old40_ball_recomputations=0, source_D5_BFS=0, solver_calls=0,
    complete_graphs_exported=0, general_changed_Pi_or_other_releases_excluded=False,
    running=False, pending=[])
rowpool['variants'] = list(variants.values())
update(rowpool, [release_variant],
       evidence('d13_single_port_release_provider_gate')
       + ['research/ddp/refresh_20261029/d13_core_swap_static_pool/MULTIPLICITY_LIFT_CHECK.json'])
if '；43池整数重数' not in rowpool['scope']:
    rowpool['scope'] += '；43池整数重数由全部单项上界1提升为同一max40；50578同阶删边后的原P40池也由单调继承排除，未做原拟oneB4球。'
if '；新组容量1见证' not in rowpool['failure_or_result']:
    rowpool['failure_or_result'] += (
        '；新组容量1见证7030/12230/14782结合旧40证书，使完整整数重数仍max40，0新增读图/BFS/solver。'
        '50578原degree11/cap2而非新增free，删51454—50578后degree10/cap3，40个P_i不变；'
        '删边只能缩球，旧39+1空provider链直接继承，0新边表读/球/solver/导图。')
rowpool['unclosed_gap'] = (
    '固定43邻域池包含任意非负整数重数的最优40已严格证明；'
    '指定删边G−{51454,50578}上未改变P40的所有非空clique子族也排除。'
    '改变容量1端口冲突的新邻域、改变P_i或其它新增路线仍开放；未证明51457最大。')
rowpool['lesson_and_restart_condition'] += (
    '；缓存纠正50578原本已有余度2，故释放这一端口没有新增挂接点；'
    '原计划oneB4没有执行，改用删边球单调性直接继承旧provider反例。'
    '要改变当前障碍须改变容量1端口共享或产生真正新增路线，不能只释放已有free端口。')
rowpool['other_metrics'].update(
    fixed43_integer_multiplicity_optimum=40,
    fixed43_all_individual_multiplicity_upper_bounds_one=True,
    fixed43_new_capacity1_witnesses=[7030, 12230, 14782],
    port50578_old_degree=11, port50578_old_capacity=2,
    port50578_after_deletion_degree=10, port50578_after_deletion_capacity=3,
    single_port_release_fixed_pool_memberships_changed=0,
    single_port_release_provider_chain_inherited=True,
    original_planned_oneB4_run_executed=False,
    single_port_release_new_BFS_or_solver=0)

report = '''# 本轮共同路线与端口容量：Wiki最终同步

root原AGENTS/NEXT/BRIEF/progress已于2026-10-29 22:34:04 UTC同步。本轮权威是C33_CAPACITY_CORE_SWAP_TURN_RESULT.json和CAPACITY_AND_CORE_SWAP_TURN.md，所有数值与外审已终态，无后台待收项。

C31沿用原31控制器/共同端口行：旧88位置、46固定边rawUNSAT未认证且仅局部。新模型保同一三triangle链+8K3，只固定33内边，释放13旧固定外边，覆盖380全部合法外边。21722变量/74336子句唯一-t90 UNKNOWN，child90.006668CPU、准备0.122005083CPU、总90.148101772CPU，0controller/0个3875图；未搬C33不交三角因子的cuts，不续timer/阶数梯子。

D13固定43邻域池的完整整数重数上限仍40：三新组各含原容量1端口7030、12230、14782，因此每组重复最多1，旧40单项上界1继承；先前947个0/1改进选择排除于是覆盖完整重数模型。此补充0新读图/BFS/solver/packing。

同阶删除51454—50578由已证candidate0替换S37保持D≤5，但缓存明确50578原degree11/cap2，本来就在P37；删除后degree10/cap3，40个P_i全部不变。删边球只缩小，旧provider链39+1直接继承，严格排原P40所有非空clique选择；其它helper内部图不比clique有更多路线。原拟一次50578半径4没有执行，实际0source读/新球/solver/完整边表导出。不是新下界或新增计数。

C11完整规定NB3子域排除及C33容量两份纸面证明已实际GeminiSUCCESS/PASS；矩只必要、不以审阅认证CNF/数值/Lean/novelty。C33 cut60秒UNKNOWN依旧保留，一般C31/C33未排。指定core swap延拓排除不外推其它Aut。

两个已有实验行追加/更正变体，ledger372未增方法或记录；合法104例/4参数、confirmed103例/3参数、具体公式Lean1不变，3750最新全球纪录仍pending。21:55专家包保留原快照、不重打包。最后canonical index/query在root状态之后重建，当前恢复入口指向本轮最新batch。
'''
report_path = HERE / 'CAPACITY_CORE_SWAP_FINAL_WIKI_REPORT.md'
report_path.write_text(screen(report))
turn_paths = ['research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json',
              'research/ddp/refresh_20261029/CAPACITY_AND_CORE_SWAP_TURN.md',
              str(report_path.relative_to(ROOT))]
for row in rows.values():
    update(row, [], turn_paths)
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'CAPACITY_CORE_SWAP_FINAL_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- CAPACITY_CORE_SWAP_FINAL_20261029 -->'
note = f'''
## {NOW} 本轮实际终态与最终恢复入口

root于22:34:04 UTC完成原状态同步，全部数值/外审终态。C31旧88rawUNSAT与新380完整挂接域分开：新21722/74336唯一90秒UNKNOWN，总90.148101772CPU，0controller/3875，不续。D13三新组各有容量1见证7030/12230/14782，固定43完整整数重数max40。50578原已degree11/cap2并在P37，删边后只是cap3，P40不变；球缩小使旧39+1空provider链零新球继承，原拟oneB4未执行。

本轮恢复应读[权威终态](../research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json)及[实际推导与决策](../research/ddp/refresh_20261029/CAPACITY_AND_CORE_SWAP_TURN.md)，不是重启旧窗口。C11矩排除/Gemini真实PASS限纸面与规定NB3域，一般31/33仍开放。ledger372、104/4、confirmed103/3、Lean1不变；21:55专家交付保持带时间戳快照，不因本批负试重打包。[最终同步回执说明](../research/ddp/refresh_20261029/CAPACITY_CORE_SWAP_FINAL_WIKI_REPORT.md)。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:
        out.write('\n\n' + marker + '\n' + screen(note))
gap_path = WIKI / 'gap_map.md'
gap = gap_path.read_text()
assert '账本现372条实验／来源记录' in gap[:1800]
gap_marker = '<!-- CAPACITY_CORE_SWAP_LATEST_BATCH_20261029 -->'
gap_note = f'''{gap_marker}
最新研究批次已收束（root22:34:04 UTC）：[权威终态](../research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json)／[推导与下一步依据](../research/ddp/refresh_20261029/CAPACITY_AND_CORE_SWAP_TURN.md)。C11规定NB3平移域1800整域矩排除；C33容量cut与C31完整380挂接均单次UNKNOWN，0新图。D13指定core-swap延拓无解，三个literal新R4覆盖集真实有效但固定43完整重数max40；50578原已free，删边后P40不变，provider排除零新球继承。一般控制器/新邻域仍开放。21:55专家包只是早先快照；恢复以本批与当前brief/progress为准。
'''
if gap_marker not in gap:
    anchor = '<!-- EXPERT_HANDOFF_2155_DELIVERY_INDEX_20261029 -->'
    assert anchor in gap
    gap = gap.replace(anchor, screen(gap_note) + '\n\n' + anchor, 1)
    gap_path.write_text(gap)

with (HERE / 'CAPACITY_CORE_SWAP_FINAL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Final completed capacity/core-swap batch synchronized after root22:34:04: existing C31 larger380 fullmodel UNKNOWN; fixed43 arbitrary multiplicity max40; unchangedP40 edge-deletion provider inheritance with0newBFS. All numerical/review terminal; ledger372,104/4,confirmed103/3,Lean1 unchanged; expert21:55 snapshot preserved.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for key in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[key] == after[key]
assert sorted(p.name for p in (WIKI / 'experiments').glob('*.md')) == experiment_names_before
assert sorted(p.name for p in (WIKI / 'claims').glob('*.md')) == claim_names_before
assert all(p.read_bytes() == value for p, value in root_before.items())
query = (WIKI / 'query_pack.md').read_text()
assert len(query) <= 8000
assert 'C33_CAPACITY_CORE_SWAP_TURN_RESULT.json' in query
receipt = dict(
    status='PASS_CAPACITY_CORE_SWAP_ALL_TERMINAL_FINAL_QUERY_REBUILT',
    updated_UTC=NOW, root_state_update_UTC=ROOT_STATE_UTC,
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    final_query_rebuild_after_root_update_pending=False,
    query_chars=len(query), canonical_helper='aris_repo/tools/research_wiki.py',
    latest_batch='research/ddp/refresh_20261029/C33_CAPACITY_CORE_SWAP_TURN_RESULT.json',
    updated_existing_ids=ids, record_count=372,
    C31_status='UNKNOWN', C31_primary_external_variables=380,
    C31_CNF_variables=21722, C31_clauses=74336,
    C31_solver_calls=1, C31_aggregate_CPU_seconds=chain['aggregate_CPU_seconds'],
    C31_controllers=0, complete3875_graphs=0,
    fixed43_integer_multiplicity_optimum=40,
    new_capacity1_witnesses=private_witnesses,
    original_planned_oneB4_run_executed=False,
    single_port_release_new_source_reads_BFS_solver=0,
    external_review_status='ACTUAL_SUCCESS_STATIC_TWO_PROOF_PASS',
    all_numerical_work_terminal=True, pending=[],
    new_experiments=0, new_methods=0, new_claims=0, new_graphs=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103,
    confirmed_pairs=3, complete_Lean_instances=1,
    root_and_expert_files_unchanged=True, expert_snapshot_preserved='21:55 UTC',
    command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'CAPACITY_CORE_SWAP_FINAL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
                     record_count=372, query_chars=len(query),
                     final_query='COMPLETE_AFTER_ROOT_STATE'), ensure_ascii=False))
