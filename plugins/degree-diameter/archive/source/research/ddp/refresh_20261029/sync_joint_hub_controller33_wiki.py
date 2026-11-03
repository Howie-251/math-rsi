"""Update actual hub UNKNOWN and the saved handle/result of the existing33 family."""
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


def evidence(directory):
    return [str(p.relative_to(ROOT)) for p in sorted(directory.iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt', '.tsv'}]


def extend(row, additions, paths):
    variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
    variants.update({v['label']: v for v in additions})
    row['variants'] = list(variants.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))


joint_dir = HERE / 'd13_D4_joint_matching_hub'
joint = json.loads((joint_dir / 'RESULT.json').read_text())
joint_model = json.loads((joint_dir / 'MODEL.json').read_text())
assert joint['status'] == 'UNKNOWN' and joint['solver_rounds'] == 1
assert joint['actual_candidate_checks'] == joint['exact_old_pair_cuts'] == 0
assert joint['running'] is False and joint_model['matching_selectors'] == 3402
c33_dir = HERE / 'controller33_full_triangle_factor'
c33_model = json.loads((c33_dir / 'MODEL.json').read_text())
c33_handle = json.loads((c33_dir / 'HANDLE.json').read_text())
c33_result_path = c33_dir / 'RESULT.json'
c33_result = json.loads(c33_result_path.read_text()) if c33_result_path.exists() else None
c33_status = c33_result['status'] if c33_result else 'RUNNING_HANDLE_RECORDED'
assert c33_result or (c33_handle['status'] == 'RUNNING' and c33_handle['pid'] == 2412361)
assert (c33_model['extra_edge_variables'], c33_model['all_variables'], c33_model['clauses']) == (495, 31680, 108341)
old33_path = ROOT / 'research/ddp/breadth_20261027_wave2/triangle_factor33_controller/production_terminal.json'
old33 = json.loads(old33_path.read_text())
assert old33['exact_all_root_capacity_scores'] == 606948 and old33['proposals'] == 800000

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 371
existing = {r['id']: r for r in before['rows']}
id13 = 'ddp-d13-d4-current6804-source-20261027'
id33 = 'ddp-wave2-triangle-factor33-controller'
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in [id13, id33]}
row13, row33 = rows[id13], rows[id33]
joint_variant = dict(label='arbitrary_at_most6_central_matching_hub_joint_selection_question_20261029',
    status='UNKNOWN', record_type='completed_bounded_full_selector_necessary_model',
    source_n=6804, maximum_selected_matching_edges=6, matching_selectors=3402,
    complete_selector_scope=True, full_D4_conditions_encoded=False,
    target_R3_cover_clauses=6804, cover_literals=9221688, C2_variables=6804,
    C2_equivalence_selector_incidence=950292, representative_support_roots=81,
    representative_critical_pairs=13230, expanded_critical_implication_cuts=1111320,
    variables=30618, clauses=2119435, literals=14407522,
    solver_rounds=1, solver_exit_code=0, solver_aggregate_CPU_seconds=joint['solver_aggregate_cpu_seconds'],
    aggregate_CPU_seconds=joint['aggregate_cpu_seconds'], actual_candidate_checks=0,
    generated_candidate_graphs=0, exact_old_pair_CEG_cuts=0, selected_matching_solution_returned=False,
    running=False, solver_handle_recorded=True, mathematical_exclusion_recorded=False,
    scope_note='All3402 central matching selectors and<=6 budget, with complete endpointR3 and proved necessary C2 implications; not a complete old-old distance model.',
    stopped_no_automatic_timer_continuation=True)
extend(row13, [joint_variant], evidence(joint_dir))
row13['title'] = '(13,4)6804源：完整<=6中央匹配hub模型UNKNOWN，split与固定小域已闭'
row13['scope'] = row13['scope'].replace('一般任意<=6中央匹配选择只记准备问题，未登记实际求解。',
    '任意<=6中央匹配完整选择器必要模型已实际唯一调用UNKNOWN，不是整族排除。')
row13['failure_or_result'] += '；完整3402选择器/<=6中央边模型30618变量/2119435子句唯一60秒调用UNKNOWN，solver60.029439CPU/总62.967105CPU，round1，无SAT选择/候选/旧pair反例cut；已停止，不继续写prep或running。'
row13['lesson_and_restart_condition'] = row13['lesson_and_restart_condition'].replace(
    '任意<=6中央M共同覆盖是新准备问题，不冒RUNNING或已有实验结果。',
    '任意<=6中央M共同覆盖模型已有一次真实UNKNOWN，无候选；停止该批，不自动续timer或下一CEG轮，不将必要条件建模完整误当真正D4整族排除。')
row13['other_metrics'].update(arbitrary_joint_matching_question_status='UNKNOWN_TERMINAL',
    arbitrary_joint_matching_solver_calls_recorded=1,
    arbitrary_joint_matching_solver_CPU_seconds=joint['solver_aggregate_cpu_seconds'],
    arbitrary_joint_matching_total_CPU_seconds=joint['aggregate_cpu_seconds'],
    arbitrary_joint_matching_actual_candidate_checks=0, arbitrary_joint_matching_CEG_cuts=0)

variant33 = dict(label='full495_cross_triangle_2factor_common_NB3_model_F5_20261029',
    status=c33_status, controller_order=33, fixed_triangles=11,
    target=dict(Delta=20, D=3, savedL=3750, baseline_scope='local complete graph, global latest novelty pending'),
    hypothetical_lift_order=4125, fiber='F5^3', fiber_size=125,
    fixed_source_matrices='research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json',
    extra_edge_variables=495, all_variables=31680, clauses=108341,
    fixed_external_edges=[[0, 3], [0, 6]],
    condition='Each pair is adjacent or has an exact3walk; fixed triangles supply self returns.',
    solver_wall_limit_seconds=90,
    old_finite_profile_proposals=800000, old_exact_capacity_scores=606948,
    inherited_saved_best_nonadjacent_ordered_pairs_without_NB3=28,
    old_finite_profile_excludes_whole_family=False,
    first_complete_joint_route_model_on_existing_family=True, first_discovery_of_family=False,
    controller_graphs_accepted=0, full4125_graphs_generated=0,
    model_CPU_seconds=c33_model['encoding_CPU_seconds'])
if c33_result:
    variant33['terminal_result'] = c33_result
    variant33['running'] = False
else:
    variant33.update(running=True, actual_solver_pid=c33_handle['pid'],
                     actual_command=c33_handle['command'], actual_exec_session=37376)
extend(row33, [variant33], evidence(c33_dir) + [str(old33_path.relative_to(ROOT))])
row33['title'] = '33点三角因子旧族：有限profile失败；完整495外边共同路线模型' + c33_status
row33['scope'] += '；继承8起点80万提案/606948完整容量评分的有限profile，保存best新F5门仍缺28个非邻有序NB3路线；未排整个族。后续同族首次完整495外边模型结合已成功F5四矩阵，而非首次发现该族。'
row33['failure_or_result'] += '；新模型495主变量/31680总变量/108341子句，solver -t90，当前实际保存状态' + c33_status + '；尚无被接受的33控制器或完整4125图。'
row33['lesson_and_restart_condition'] = '不重复旧profile606948评分或attachment80+160切片；新完整共同连接模型确实释放全部495外边。当前状态按实际HANDLE/RESULT记录，不按旧有限失败排整族，不按少缺几个控制器点对延长timer。完整合法控制器命中后仍须生成完整F5提升并验收；条件性4125不能计图。'
row33['unclosed_gap'] = '旧profile只闭有限样本；当前完整模型状态为' + c33_status + '，不据此声称33控制器族或20D3原题无解。尚无完整4125点图。'
row33['other_metrics'].update(old_proposals=800000, old_exact_all_root_capacity_scores=606948,
    old_saved_best_NB3_gaps=28, current_complete_model_status=c33_status,
    current_complete_model_running=not bool(c33_result), actual_lift4125_generated=False)

gap_map = WIKI / 'gap_map.md'
gap_text = gap_map.read_text()
old_count = '账本现368条实验／来源记录'
if old_count in gap_text:
    gap_map.write_text(gap_text.replace(old_count, '账本现371条实验／来源记录', 1))
else:
    assert '账本现371条实验／来源记录' in gap_text[:1800]

report = ('# 完整中央matching模型终态与33控制器模型状态\n\n'
    '6804全部3402中央matching选择器、最多6边的唯一有界必要模型已终态UNKNOWN：round1，solver60.029439CPU、总62.967105CPU，0SAT选择、0候选检查、0旧pair反例cut。停止，不续timer；不排这个完整选择域。\n\n'
    '33点11三角形+任意外部二因子是已有旧族，旧800000提案/606948评分与best28个非邻NB3缺口保留，不冒整体排除。'
    '本次同族首次完整495外边/31680总变量/108341子句共同路线模型，结合后来成功的F5证书，条件目标33×125=4125/degree20/D3。'
    '当前实际保存状态：' + c33_status + '。' +
    ('真实HANDLE记录PID2412361/session37376/-t90；此writer没有poll求解器。\n\n' if not c33_result else '按已存在RESULT记录终态，此writer没有poll求解器。\n\n') +
    '104/4、confirmed103/3、Lean1与371账本记录保持，无被接受的新33控制器或4125图。仅把gap_map顶部旧账本数368改为371，没有重写策略。'
    '两个既有source/controller节点追加变体，不新建方法、Wiki或Goal；root负责最终结果与最后query。\n')
report_path = HERE / 'JOINT_HUB_CONTROLLER33_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    extend(row, [], [str(report_path.relative_to(ROOT))])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'JOINT_HUB_CONTROLLER33_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
s = comments.read_text()
old = '任意<=6中央matching共同覆盖选择器是新准备问题，暂无真实solverhandle/终态，不标RUNNING；待实际RESULT后再记实验。'
new = '后续任意<=6中央matching完整选择器模型已实际一次UNKNOWN终态：60.029439 solverCPU/总62.967105，round1，0选择/候选/反例cut；不再记准备或RUNNING，不续timer，不排整个matching hub域。'
assert old in s
s = s.replace(old, new, 1)
marker = '<!-- JOINT_HUB_UNKNOWN_CONTROLLER33_FULL_MODEL_20261029 -->'
if marker not in s:
    s += '\n\n' + marker + '\n## 同族完整33控制器模型的实际状态\n\n这是执行记录。旧33族有限profile为80万提案、606948评分，best仍缺28个非邻有序NB3路线；不是完整族排除。本次首次完整495外边共同路线模型结合成功F5证书，条件目标4125/20/D3，实际状态' + c33_status + '。'
    s += ('已保存真实PID2412361/session37376及90秒调用；没有把模型准备冒实际图。\n\n' if not c33_result else '以已存RESULT终态为准，不从旧profile推出。\n\n')
    s += '完整hub D4批已停，104/4、confirmed103/3、Lean1及371记录不变。gap_map顶部账本数已校正371，策略原文保留。root负责最终回执及query。[实际模型证据](../research/ddp/refresh_20261029/JOINT_HUB_CONTROLLER33_WIKI_REPORT.md)。\n'
comments.write_text(screen(s))
with (HERE / 'JOINT_HUB_CONTROLLER33_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Updated actual complete matching selector UNKNOWN and saved full33-family handle/result on existing records; corrected gap_map top ledger count368 to371 only; no new graph or method; final query waits for root.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 371
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_JOINT_UNKNOWN_CONTROLLER33_STATUS_QUERY_PENDING_ROOT',
    updated_UTC=NOW, updated_existing_ids=list(rows), record_count=371,
    joint_matching_status='UNKNOWN_TERMINAL', joint_solver_rounds=1,
    joint_solver_CPU_seconds=joint['solver_aggregate_cpu_seconds'], joint_total_CPU_seconds=joint['aggregate_cpu_seconds'],
    joint_actual_candidates=0, joint_CEG_cuts=0,
    controller33_status=c33_status, controller33_terminal_result_exists=bool(c33_result),
    controller33_old_family_not_new_discovery=True, solver_polled_by_writer=False,
    gap_map_count_correction='368->371', gap_strategy_rewritten=False,
    new_methods=0, new_claims=0, new_graphs=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True, command=command, helper_stdout=result.stdout.strip())
receipt_path = HERE / 'JOINT_HUB_CONTROLLER33_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=371, controller33=c33_status), ensure_ascii=False))
