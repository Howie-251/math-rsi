"""Record completed hub/split gates as variants of the two existing source records."""
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


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'aris_repo/tools' / (name + '.py'))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


helper = module('research_wiki')
capture = module('capture_filter')


def screen(text):
    assert not capture.screen(text), capture.screen(text)
    return text


def read(path):
    return json.loads((HERE / path).read_text())


def paths(directory):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / directory).iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt'}]


def extend(row, additions, evidence):
    variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
    variants.update({v['label']: v for v in additions})
    row['variants'] = list(variants.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + evidence))


hub13 = read('d13_D4_six_matching_hub/RESULT.json')
line13 = read('d13_D4_six_matching_hub/one_line_edge_extension/RESULT.json')
split13 = read('d13_D4_vertex_split_geodesic/RESULT.json')
hub14 = read('d14_D4_seven_plain_hub/RESULT.json')
split14 = read('d14_D4_vertex_split_geodesic/RESULT.json')
terminal14hub = read('d14_D4_seven_plain_hub/TERMINAL.json')
terminal14split = read('d14_D4_vertex_split_geodesic/TERMINAL.json')
assert hub13['status'] == 'REJECTED_NEW_ROOT_DISTANCE_GATE' and hub13['t_max'] == 4
assert hub13['vertices_with_t_greater_than_3'] == 312
assert line13['q_evaluated'] == line13['raw_line_edges'] == 144 and line13['passing_q'] == 0
assert split13['representative_roots_completed'] == split13['roots_rejected_by_singleton'] == 81
assert split14['representative_roots_completed'] == split14['singleton_rejected_roots'] == 81
assert hub14['endpoint_R3_missing'] == 479 and hub14['candidate9721_graph_generated'] is False

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 371
existing = {r['id']: r for r in before['rows']}
id13 = 'ddp-d13-d4-current6804-source-20261027'
id14 = 'ddp-d14-d4-current9720-recipe-regularity-spare-screen-20261027'
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in [id13, id14]}
row13, row14 = rows[id13], rows[id14]

split_lemma = ('For old distance4 target t, every <=4 path from either split side must avoid the new internal split edge; '
               'otherwise contraction gives an old path<=3. Thus all old geodesic first-neighbor supports must meet both color classes; a singleton rejects every partition.')
hub_lemma = ('If all removed edges have both endpoints in T, d_(G-M)(x,T)=d_G(x,T): a shortest path to T cannot use a removed edge before reaching T. '
             'A new hub joined only to T has distance1+d_G(x,T). This says nothing by itself about old-old candidate distances.')
variant13hub = dict(label='fixed_six_central_matching_edges_common_hub_20261029',
    status=hub13['status'], source_n=6804, source_m=44226, source_degree=13,
    proposed_n=6805, removed_matching_edges=6, endpoints=12,
    fixed_fiber=[0, 0, 2, 0], fixed_fiber_code=18, t_max=4,
    distance_histogram=hub13['distance_histogram'], missing_R3=312,
    witness=22, witness_distance_to_T=4, prospective_hub_distance=5,
    shortest_path_to_T=hub13['first_failure_shortest_path_to_T'],
    exact_scope='Only the frozen a^k orbit, xstar and six central matching edges.',
    source_multisource_BFS=1, source_allroot_revalidation=0,
    candidate_graphs_generated=0, candidate_BFS=0, old_old_candidate_distances_checked=False,
    CPU_seconds=hub13['cpu_seconds'], hub_distance_lemma=hub_lemma)
variant13line = dict(label='fixed_six_matching_hub_one_additional_line_edge_all144_20261029',
    status=line13['status'], fixed_matching_unchanged=True,
    raw_T_to_external_line_edges=144, distinct_external_q=144, completed=144, passing=0,
    existing_R3_gaps=312, maximum_gaps_covered_by_one_q=81, minimum_gaps_remaining=231,
    source_radius3_checks=144, original_multisource_BFS_repeated=0,
    candidate_graphs_generated=0, candidate_BFS=0, CPU_seconds=line13['cpu_seconds'],
    exact_scope='Keep frozen M6; delete one additional original line edge v-q withv inT,q outsideT, and joinq to same hub. No otherM or second line edge.',
    other_matching_hubs_excluded=False)
variant13split = dict(label='all_current6804_adjacent_single_vertex_splits_geodesic_singletons_20261029',
    status=split13['status'], source_n=6804, source_degree=13,
    representative_roots=81, completed=81, singleton_rejections=81,
    literal_roots_covered_by_left_controller_action=6804,
    singleton_targets_per_root_min=1080, singleton_targets_per_root_max=1121,
    example=dict(root=0, target=19, sole_first_neighbor=3411, path=[0, 3411, 1164, 4605, 19]),
    partition_assignment_domain_if_needed=4096, actual_partition_assignments_tested=0,
    geodesic_support_BFS=81, candidate_graphs_generated=0, candidate_BFS=0,
    CPU_seconds=split13['cpu_seconds'], split_lemma=split_lemma,
    exact_scope='Retain allG-v edges; partition all13 oldneighbors between two adjacent split vertices. Currentliteral source only.',
    other_sources_or_multi_vertex_edits_excluded=False)
pending_joint = dict(label='arbitrary_at_most6_central_matching_hub_joint_selection_question_20261029',
    status='PREPARATION_ONLY_NO_REAL_SOLVER_HANDLE',
    record_type='pending_mathematical_question',
    question='Can atmost6 arbitrarily selected existing central matching edges provide endpointsT whose closedR3 union covers all6804 oldvertices?',
    source_n=6804, selector_domain='Existing3402 central matching edges; eventual exact input must be bound by producer.',
    arbitrary_matching_selection_differs_from_closed_literal_M6=True,
    numerical_experiment_started=False, solver_handle_recorded=False, solver_calls_recorded=0,
    mathematical_result_recorded=False, old_old_candidate_D4_checked=False,
    caution='A coverage-positive selection alone is not a valid new graph; changed old-old distances still require complete checking.')
row13['title'] = '(13,4)6804源：固定hub与144单线补边失败，全部相邻单点split排除'
row13['scope'] += '；追加固定六中央匹配边共hub、固定M6加一条T到外部线边全144项，以及81代表覆盖全源的相邻单点split首步门。一般任意<=6中央匹配选择只记准备问题，未登记实际求解。'
row13['failure_or_result'] += '；固定M6端点R3漏312/tmax4，首22距拟hub5；其单额外线边完整144全失败、单q至多补81/312；81fiber代表全部有singleton geodesic支持，故当前6804源全部相邻单点split失败，无需枚4096划分。0新图。'
row13['lesson_and_restart_condition'] += '；固定M和单线补端点域停止，不据局部少缺项换seed。相邻split的singleton是整root全部划分障碍，由left controllerAut覆盖所有6804顶点。其它matching hub与多点改造仍开放；任意<=6中央M共同覆盖是新准备问题，不冒RUNNING或已有实验结果。'
row13['unclosed_gap'] = '保边append已因全正则阻断；本固定hub/单线域与全部当前source相邻单点split已按精确范围关闭。其它matching选择、其它改边、多点改造和一般(13,4)仍开放。'
row13['other_metrics'].update(fixed6_hub_new_root_gate='FAILED_312_GAPS',
    fixed6_one_line144_pass=0, all_current_adjacent_vertex_splits_excluded=True,
    adjacent_split_representatives_completed=81, new_graphs=0,
    arbitrary_joint_matching_question_status='PREPARATION_ONLY_NO_REAL_SOLVER_HANDLE',
    arbitrary_joint_matching_solver_calls_recorded=0)
extend(row13, [variant13hub, variant13line, variant13split, pending_joint],
       paths('d13_D4_six_matching_hub') + paths('d13_D4_six_matching_hub/one_line_edge_extension') + paths('d13_D4_vertex_split_geodesic'))

variant14hub = dict(label='fixed_seven_plain_matching_edges_common_hub_20261029',
    status=hub14['status'], source_n=9720, source_m=68040, source_degree=14,
    proposed_n=9721, proposed_m=68047, removed_edges=7, distinct_endpoints=14,
    B_order=6, A_outside_B_subgroup=True, fixed_fiber=[1, 0, 1, 1],
    endpoint_R3_covered=9241, endpoint_R3_missing=479, witness=1,
    witness_coordinates='(I,0,(1,0,0,0))', prospective_hub_distance_lower_bound=5,
    modified_old_multisource_R3_BFS=1, source_D4_revalidation=0,
    candidate_graphs_generated=0, candidate_BFS=0,
    native_CPU_seconds=hub14['CPU_seconds'],
    aggregate_prepare_compile_native_CPU_seconds=terminal14hub['aggregate_preparation_compile_native_CPU_seconds'],
    exact_scope='Only frozen B^k phase0-to1 sixplain edges plus A phase2-to3 oneplain edge, all atfixed xstar.',
    other_matching_hubs_excluded=False, hub_distance_lemma=hub_lemma)
variant14split = dict(label='all_current9720_adjacent_single_vertex_splits_geodesic_singletons_20261029',
    status=split14['status'], source_n=9720, source_degree=14,
    representative_roots=81, completed=81, singleton_rejections=81,
    literal_roots_covered_by_left_controller_action=9720,
    example=dict(root=0, target=83, sole_first_neighbor=398),
    partition_assignment_domain_if_needed=8192, actual_partition_assignments_tested=0,
    geodesic_support_BFS=81, source_D4_revalidation=False,
    candidate_graphs_generated=0, candidate_BFS=0,
    native_CPU_seconds=split14['CPU_seconds'],
    aggregate_prepare_compile_native_CPU_seconds=terminal14split['aggregate_preparation_compile_native_CPU_seconds'],
    split_lemma=split_lemma,
    exact_scope='Retain allG-v edges; partition all14 oldneighbors between two adjacent split vertices. Currentliteral source only.',
    other_sources_or_multi_vertex_edits_excluded=False)
row14['title'] = '(14,4)9720源：唯一7plain边共hub失败，全部相邻单点split排除'
row14['scope'] += '；后续唯一7plain匹配边共hub及81fiber代表的全部相邻singlevertexsplit geodesic gate按明确范围执行；不同于旧保边append或controller迁移。'
row14['failure_or_result'] += '；7真实plain边/14互异端点通过，删边后T的R3仅9241/9720、漏479，首label1使拟hub距至少5，未生成9721图。随后81代表全部有distance4目标singleton首步支持，由left controllerAut排当前9720源全部相邻单点split；0划分枚举/候选图/oldold验收。'
row14['lesson_and_restart_condition'] += '；固定7边共hub规则已停，不换coset/xstar。当前源相邻单点split已被全81代表singleton门排除，不能再试另一根或邻居划分。其它matching hub、其它源或多点改造未排。'
row14['unclosed_gap'] = '此全正则源保边append、固定7plain-edge hub和全部相邻singlevertexsplit各已关闭。其它matching hub、额外改边、多点改造及一般(14,4)仍开放。'
row14['other_metrics'].update(fixed7_hub_R3_missing=479,
    all_current_adjacent_vertex_splits_excluded=True, adjacent_split_representatives_completed=81,
    new_graphs=0, old_old_candidate_BFS=0)
extend(row14, [variant14hub, variant14split],
       paths('d14_D4_seven_plain_hub') + paths('d14_D4_vertex_split_geodesic'))

report = '''# 两个已知源的共同hub与相邻split终态

数学合法实例104/4、confirmed主表103/3、具体公式图Lean1不变。本批未产生新图；全部已完成结果只附加到原6804/9720 source方法节点，不新增方法或claim。

6804固定六中央匹配边的12端点R3漏312、tmax4，首22距拟hub5。固定这个M6再加入一条T到外部的原线边，全144项都不能补齐312缺口，最多补81、至少留231。两个域均停止，不排其它M。

9720固定七plain边的14端点合法，但其R3只覆9241、漏479，首label1距拟hub至少5；唯一组合停止，无候选图或旧点对验收。

对相邻单点split，旧distance4目标的全部geodesic首步支持必须跨两色；使用split内部边的短路收缩后会给旧长度<=3矛盾。6804和9720各81fiber代表全有singleton支持，再以左controller作用分别覆盖全部6804/9720顶点。因此两个当前source的整个相邻split规则关闭；4096/8192仅为本来无singleton时才测试的划分域，实际枚举0。

新问题是从6804现有中央匹配中任意选择至多6条，联合保证端点R3覆盖；当前只作准备记录，没有真实solverhandle或结果，不标RUNNING。即使将来端点覆盖命中，也还须检验变更后的全部旧点对D4。没有因此排除整个13D4/14D4或多点改造。

根状态与最终query由root随后确认，本次不改AGENTS/NEXT/BRIEF/progress或专家交付，不重导Wiki。
'''
report_path = HERE / 'HUB_SPLIT_COMPLETED_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    extend(row, [], [str(report_path.relative_to(ROOT))])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'HUB_SPLIT_COMPLETED_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

marker = '<!-- HUB_SPLIT_TWO_SOURCES_COMPLETED_20261029 -->'
comment = '''
## 两个source的共同hub与相邻单点split实际终态

这是执行记录，不是新人工原话。6804固定M6共hub的端点R3漏312；同M6仅加一条T到外部line边完整144项全失败，最多补81。9720唯一7plain边共hub端点R3漏479，首label1使拟hub距离至少5。均未生成新图或检验候选旧点对，不排其它matching hub。

6804与9720各81代表都出现旧distance4目标的singleton最短路首步支持，左controllerAut覆盖全部source，因此当前两个source的相邻单点split整域关闭。4096/8192划分实际均未枚举，不能冒已验图数。不外推多点改造、额外重连或其它源。

任意<=6中央matching共同覆盖选择器是新准备问题，暂无真实solverhandle/终态，不标RUNNING；待实际RESULT后再记实验。104/4、confirmed103/3、Lean1与371账本记录不变。旧D2继续暂停，root负责原状态及最终query。[本轮完成证据汇总](../research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md)。
'''
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if marker not in comments.read_text():
    with comments.open('a') as output:
        output.write('\n\n' + marker + '\n' + screen(comment))
with (HERE / 'HUB_SPLIT_COMPLETED_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded completed fixed hubs, complete144 one-line extension negative and both fixed-source adjacent split exclusions on two existing records; arbitrary matching selection preparation only, no real solver handle; final query waits for root.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 371
assert {r['id'] for r in after['rows']} == {r['id'] for r in before['rows']}
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
q8 = next(r for r in after['rows'] if r['id'] == 'ddp-q8-k64-cube-external2factor-13d3-20261029')
assert q8['other_metrics']['new_cross_model_review_status'] == 'SUCCESS_SUPPORT'
receipt = dict(status='PASS_HUB_SPLIT_EXISTING_VARIANTS_QUERY_PENDING_ROOT',
    updated_UTC=NOW, updated_existing_ids=list(rows), record_count_before=371, record_count_after=371,
    fixed_literal_hubs_failed=2, fixed6804_one_line_extensions_completed=144, one_line_passes=0,
    complete_source_adjacent_splits_excluded=[6804, 9720], representative_roots_each=81,
    actual_partition_assignments_tested=0, other_matching_hubs_excluded=False,
    multi_vertex_changes_excluded=False, new_graphs=0, new_claims=0, new_methods=0,
    arbitrary_joint_matching_status='PREPARATION_ONLY_NO_REAL_SOLVER_HANDLE',
    arbitrary_joint_matching_solver_calls_recorded=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    q8_final_PASS_preserved=True, research_jobs_rerun=0, final_query_rebuild_after_root_update_pending=True,
    command=command, helper_stdout=result.stdout.strip(),
    changed_wiki_paths=['research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md',
        *[existing[k]['wiki_path'] for k in rows], 'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md',
        'research-wiki/index.md', 'research-wiki/query_pack.md', 'research-wiki/log.md'])
receipt_path = HERE / 'HUB_SPLIT_COMPLETED_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=371, updated_existing_records=2, final_query='WAITING_FOR_ROOT'), ensure_ascii=False))
