"""Record completed C11 route obstruction and local budgets without dispatch claims."""
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


def load(relative):
    return json.loads((HERE / relative).read_text())


def evidence(name):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / name).iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt'}]


def extend(row, additions, paths):
    variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
    variants.update({v['label']: v for v in additions})
    row['variants'] = list(variants.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))


c11 = load('controller33_C11_exact/RESULT.json')
prediction = load('controller33_C11_exact/PREDICTION_CHECK.json')
budget = load('controller33_route_capacity/RESULT.json')
aut = load('d13_B0_full_automorphism_gate/RESULT.json')
assert c11['status'] == 'ALL_1800_C11_SETTINGS_REJECTED'
assert c11['counts_by_type'] == dict(three_loops=125, loop_and_double=675, triangle=1000)
assert c11['settings_tested'] == 1800 and c11['representative_NB3_root_tests'] == 5400
assert [p['next_label_missing_nonadjacent_phases'] for p in prediction] == [[], [7], [7, 9]]
assert budget['status'] == 'SINGLE_SAVED_PAIR_STATISTIC_COMPLETE'
assert budget['prediction'] == 'REFUTED_SAVED_BEST_PASSES_THESE_NECESSARY_GATES'
assert aut['status'] == 'PERIPHERAL_BINDING_MISSING_IN_BOUNDED_READ_SCOPE'
assert aut['source_files_read'] == 5 and aut['source_graph_reads'] == aut['full_edge_set_checks'] == 0
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 372
existing = {r['id']: r for r in before['rows']}
id33 = 'ddp-wave2-triangle-factor33-controller'
idaut = 'ddp-h9-d13-51417-source-binding-20261027'
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in [id33, idaut]}

c11_variant = dict(label='C11_simultaneous_triangle_block_translation_complete_NB3_gate_20261029',
    status=c11['status'], controller_order=33, fixed_disjoint_K3=11,
    exact_scope='C11 simultaneous triangle-block translation; disjoint simple cross-block2factor; prescribed nonneighbor NB3 route condition.',
    legal_settings_by_quotient_type=c11['counts_by_type'], legal_settings_tested=1800,
    representative_NB3_root_tests=5400, actual_33_adjacencies_constructed=1800,
    valid_controllers=0, complete4125_graphs=0,
    CPU_seconds=c11['CPU_seconds'], solver_calls=0, large_graph_BFS=0,
    prediction=dict(shifts=[1, 3, 5], all_same_label_targets_covered=True,
        zero_to_one_all_nonadjacent_phases_covered=True,
        one_to_two_missing_phases=[7], two_to_zero_missing_phases=[7, 9], verdict='SUPPORTED'),
    paper_obstruction='Three-label triangle has10 NB3 phases covering9 required residues; firstmoment makes repeated residue6a, secondmoment forcesa²=b²+c², cyclic neighboring direction forcesb²=c²+a², contradictionc=0.',
    loop_types_obstruction='Atmost6 route phases for8 same-label nonneighbor targets.',
    paper_derivation='research/ddp/refresh_20261029/controller33_C11_exact/DERIVATION_PACKAGE.md',
    ordinary_D3_family_excluded=False, general33_controller_family_excluded=False,
    arbitrary_F5_lift_family_excluded=False, same_family_static_attack='PASS reported by assigned mathematical reviewer',
    combined_cross_model_review_status='PENDING', Lean_formalized=False,
    same_C11_parameters_or_subgroup_ladder_continuation=False)
observations = []
for o in budget['observations']:
    observations.append(dict(name=o['name'], n=o['n'], triangles=o['triangles_total'],
        fourcycles=o['fourcycles_total'], t_plus_q_histogram=o['sum_t_c4_histogram'],
        weighted_pair_sum_histogram=o['weighted_pair_sum_histogram'],
        missing_nonadjacent_ordered_pairs=o['actual_missing_nonadjacent_ordered_pairs'],
        necessary_gate_violation_counts={k: len(v) for k, v in o['C33_restriction_violations'].items()}))
budget_variant = dict(label='local_triangle_fourcycle_and_weighted_pair_NB3_capacity_20261029',
    status='PAPER_NECESSARY_CONSTRAINTS_AND_ONE_SAVED_PAIR_STATISTIC',
    scope='Simple4regular fixed triangle-factor controller; every distinct nonneighbor pair has exact NB3 route.',
    definitions='t(v):all triangles atv; q(v):all simple4cycles atv, chords allowed.',
    exact_identity='D(v)-M(v)=41-n-2(t(v)+q(v))',
    C33_necessary_bound='t(v)+q(v)<=4', C30_comparison_bound=5,
    block_pair_necessary_rules=['m_AB<=3', 'm_AB=3 edges form a perfect matching',
        'blockpairs withmultiplicity3 forma matching'],
    weighted_pair_lower_bound='L(v) counts2F triangles plus2F4cycles and satisfiesL(v)<=3.',
    pair_weights='Disjoint edgepair:weight1 onfourends; shared-end pair:weight2 onsharedend andother twoends,weight1 onopposite trianglethird point.',
    complete_t_plus_q_not_equivalent_to_weighted_lower_bound=True,
    observations=observations, test_prediction=budget['prediction'],
    result_interpretation='SavedfailedC33best passes all necessary cuts yet still misses28 targets; cuts are not a full characterization.',
    CPU_seconds=budget['CPU_seconds'], new_controllers=0, optimization_proposals=0,
    BFS_calls=0, solver_calls=0, C11_cases_repeated=0,
    later_full_cut_model_dispatch_recorded=False,
    performance_or_solver_acceleration_proven=False, combined_cross_model_review_status='PENDING')
row33 = rows[id33]
extend(row33, [c11_variant, budget_variant],
       evidence('controller33_C11_exact') + evidence('controller33_route_capacity'))
row33['scope'] += '；同族C11同时块平移合法子域1800设置已完整NB3门排除；新增纸面短圈/块对容量推导与一对保存C30/C33统计，尚不把后续完整cut模型派发冒已运行。'
row33['failure_or_result'] += '；C11 125/675/1000共1800全拒，5400代表NB3测试，0.103882965CPU。预测(1,3,5)同label和0→1覆盖支持，另方向缺7及7/9；共享相位一/二次矩给整子域纸面矛盾。新t+q≤4/m≤3/matching/L≤3必要门并未拒保存best（仍缺28），一对旧对象统计0.178825762CPU、0BFS/solver。'
row33['lesson_and_restart_condition'] += '；停止整个精确定义C11子域，不再调其位移或开对称群梯子。后续仍保留非循环外边共同自由，短圈预算可作为等价完整模型的早传播条件，但保存best通过这些必要门，不宣称它们充分或实际加速。'
row33['unclosed_gap'] = '一般非对称33固定三角因子控制器仍开放；旧原/规范完整模型UNKNOWN不变。已闭C11仅针对规定NB3迁移规则，不是一般D3或所有F5图不可能。后续cut模型须等真实handle/RESULT记账；联合外审pending。'
row33['other_metrics'].update(C11_complete_settings=1800, C11_representative_NB3_tests=5400,
    C11_route_rule_scope_excluded=True, general33_family_excluded=False,
    local_capacity_saved_pair_statistic_complete=True,
    local_capacity_saved_best_rejected=False, later_full_cut_model_run_recorded=False,
    combined_C11_capacity_external_review_status='PENDING')

rowaut = rows[idaut]
aut_variant = dict(label='originalB0_full_automorphism_transport_bounded_input_gate_20261029',
    status=aut['status'], base_n=51417, base_m=324451,
    core_n=50554, peripheral_n=863,
    certified_operation='simultaneous swap ofsavedcore splitpairs only; phi=tau²',
    whole_source_peripheral_permutation_available=False,
    source_files_read=5, source_graph_reads=0, full_edge_set_checks=0,
    BFS_runs=0, transported_neighborhoods=0, solver_calls=0,
    automorphism_nonexistence_claimed=False,
    original40_Aut_image_pool_excluded=False,
    restart_requires='An explicit compatible peripheral-image permutation and full source automorphism binding, or a separately justified alternative action.')
extend(rowaut, [aut_variant], evidence('d13_B0_full_automorphism_gate'))
rowaut['scope'] += '；后续原B0全图Aut搬运40邻域入口仅完成5文件读取门：已证操作只到50554core，863外围无绑定，未验任何全图置换或生成imagepool。'
rowaut['failure_or_result'] += '；full-Aut输入门为PERIPHERAL_BINDING_MISSING，0source边表读/edgecheck/BFS/solver；这是所需置换未提供，不是无非平凡Aut或Aut-image池无解。'
rowaut['lesson_and_restart_condition'] += '；不能把core phi=tau²外推到外围或任意固定863外围。旧wholeclass几何pool、max40 multiplicity和P40clique不包含新Aut-image邻域池；须有显式全图绑定才可搬运原B0完整覆盖。'
rowaut['other_metrics'].update(full_source_Aut_bound=False, full_Aut_gate_completed_as_read_only=True,
    full_Aut_gate_edge_checks=0, full_Aut_nonexistence_proven=False)

report = '''# C11共同路线子域排除与全图自同构输入门

已实际完成C11子域125/675/1000共1800合法设置，5400个代表NB3门全部拒，0.103882965CPU，0主图/solver。预测(1,3,5)同label及0→1覆盖支持，而1→2缺7、2→0缺7/9；纸面一/二次矩说明共享边相位条件不能循环同时满足。只排C11同时块平移下规定NB3迁移条件，不排一般33控制器、普通D3或任意F5提升。

局部短圈必要条件已推导：t+q≤4，块对m≤3且m=3为perfectmatching，三重块对成matching，2F edge-pair加权L≤3。纸面对完整覆盖是必要推论，不是充分条件。唯一保存C30成功/C33失败对象统计0.178825762CPU，失败best通过这些门却仍缺28，原预测被反驳；未生成新controller或求解。后续cut模型当前未在本记录登记真实运行，等根代理实际handle/RESULT。

原51417全图Aut搬运40邻域只完成5文件输入门。phi=tau²仅绑定50554core，863外围没有给出兼容置换；0source边读/edgecheck/BFS/图。停止这个未绑定入口，不宣称无Aut或Aut-image整族排除。

现有两个source/controller条目附变体，ledger372，104/4、confirmed103/3、Lean1不变。联合Gemini审阅pending，same-family数学静态攻击通过不等同新外审或Lean。root最终状态后最后query；未改原Goal、root入口或专家交付。
'''
report_path = HERE / 'C11_CAPACITY_AUTGATE_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    extend(row, [], [str(report_path.relative_to(ROOT))])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'C11_CAPACITY_AUTGATE_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- C11_CAPACITY_AUTGATE_COMPLETED_20261029 -->'
note = '''
## 同一33机制的C11子域终态和D13全Aut输入门

这是执行记录。C11同时块平移子域1800合法设置（125/675/1000）全NB3失败，5400代表测试，0.103882965CPU。事前(1,3,5)局部路线预测支持，但另方向漏7/7,9；纸面矩条件解释共享位移不能共同覆盖。仅排此规定NB3规则的C11子域，不排普通D3或一般33，停止同域调参和对称模板梯子。

短圈必要t+q≤4、块对m≤3/三边matching、三重块对matching、加权L≤3已推导；保存best虽缺28路线却通过这些门，故它们非充分判据。唯一C30/旧best统计完成，0新图/BFS/solver。后续完整cut模型待真实回执，不把准备记运行；联合外审尚pending。

原51417全图Aut搬运入口5文件读取仅确认core involution，外围863缺兼容置换；0边表/edgecheck/BFS/图，不登记无Aut或整族排除。两个existing行加变体，ledger372及104/4、confirmed103/3、Lean1保持，root最终同步后再query。[本轮已完成证据](../research/ddp/refresh_20261029/C11_CAPACITY_AUTGATE_WIKI_REPORT.md)。
'''
if marker not in comments.read_text():
    with comments.open('a') as output:
        output.write('\n\n' + marker + '\n' + screen(note))
with (HERE / 'C11_CAPACITY_AUTGATE_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded completed1800 C11 NB3 gate and moment obstruction, necessary local route budgets/saved-pair counterexample, and bounded full-Aut input gap on two existing rows; no new method/claim; future cut solver and combined review not presumed.')
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_C11_LOCAL_CAPACITY_AUTGATE_EXISTING_VARIANTS_PENDING_FINAL',
    updated_UTC=NOW, updated_existing_ids=list(rows), record_count=372,
    C11_legal_settings=1800, C11_representative_NB3_tests=5400,
    C11_CPU_seconds=c11['CPU_seconds'], C11_exact_route_rule_excluded=True,
    ordinary_D3_or_general33_excluded=False,
    local_budget_prediction='REFUTED_SAVED_BEST_PASSES', local_budget_BFS_or_solver=0,
    full_Aut_gate='PERIPHERAL_BINDING_MISSING', full_Aut_nonexistence_proven=False,
    future_cut_numerical_launch_recorded=False, combined_external_review_status='PENDING',
    new_experiments=0, new_methods=0, new_claims=0, new_graphs=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True, command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'C11_CAPACITY_AUTGATE_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=372, final_query='WAITING_FOR_ROOT_FINAL'), ensure_ascii=False))
