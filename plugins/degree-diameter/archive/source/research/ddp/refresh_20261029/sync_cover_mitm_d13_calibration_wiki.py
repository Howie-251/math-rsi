"""Record completed new certificates and exact preprocessing, with no rerun."""
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


def evidence(directory):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / directory).iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt'}]


def extend(row, additions, paths):
    variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
    variants.update({v['label']: v for v in additions})
    row['variants'] = list(variants.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))


mitm = read('successful_d5_cover_d6_capacity/independent_witnesses/RESULT.json')
calibration = read('d13_D5_static_pool_calibration/RESULT.json')
multiplicity = read('d13_D5_static_pool_calibration/MULTIPLICITY_RESULT.json')
dominance = read('d13_v4580_column_dominance/RESULT.json')
assert mitm['status'] == 'ALL_SIX_WITNESSES_MATCH' and mitm['witness_pairs'] == 6
assert mitm['source_reads'] == 3 and mitm['graph_BFS'] == mitm['DP_repeats'] == 0
assert len(calibration['sets']) == 40 and calibration['failed_sets'] == 0
assert calibration['unordered_pair_count'] == 780 and calibration['incompatible_pairs'] == 0
assert calibration['port_overloads'] == 0
assert multiplicity['status'] == 'MAXIMUM_EXACTLY40' and multiplicity['upper_bound_histogram'] == {'1': 40}
assert dominance['status'] == 'COMPLETE_STRICT_COLUMN_DOMINANCE' and dominance['complete']
assert (dominance['input_columns'], dominance['retained_count'], dominance['removed_count']) == (13057, 12961, 96)
assert dominance['exact_witness_checks'] == 96 and dominance['solver_calls'] == 0

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 372
existing = {r['id']: r for r in before['rows']}
cover_id = 'ddp-successful-d5-sources-ordinary-cover-route-capacity-20261029'
family_id = 'ddp-d13-singlefault-star-family-51457-20261027'
guard_id = 'ddp-d13-v4580-current51457-fourguard-unknown-20261029'
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in [cover_id, family_id, guard_id]}

cover = rows[cover_id]
cover['other_metrics'].update(independent_MITM_status='PASS_ALL_SIX_WITNESSES_MATCH',
    independent_MITM_witness_pairs=6, independent_explicit_NB_walks=17,
    independent_MITM_source_reads=3, independent_MITM_CPU_seconds=mitm['CPU_seconds'],
    independent_MITM_BFS=0, independent_MITM_DP_repeats=0)
cover['failure_or_result'] += '；独立MITM对6具体pair分别列尽17条NB短walk，全部匹配4/8/2和1/1/1，0.245694CPU，三source各独立读1次，无BFS或DP重跑；PREFIX_SCOPE_PROOF正式保存103prefix+3原base扩展。'
cover['unclosed_gap'] = '数量已获独立六pair显式MITM核对。只关闭这些base/prefix的指定ordinary-cover域；改边、branched/non-cover映射、其它基图和一般D6格仍开放，无新图或Lean定理。'
for variant in cover['variants']:
    variant.update(independent_witness_status='PASS_MITM_EXPLICIT_WALKS',
                   independent_witness_scope='Only the statedR6 pair and statedroot0 R5 pair; no extra roots or full-source BFS.')
extend(cover, [], evidence('successful_d5_cover_d6_capacity/independent_witnesses') +
       ['research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREFIX_SCOPE_PROOF.md'])

family = rows[family_id]
calibration_variant = dict(label='all40_neighborhoods_original_B0_static_pool_calibrated_20261029',
    status='COMPLETE40_STATIC_COVERING_COMPATIBLE_SETS',
    final_source_n=51457, final_source_m=324863, original_B0_n=51417, original_B0_m=324451,
    literal_neighborhoods=40, B0_radius4_covering_sets=40, failed_sets=0,
    unordered_pair_distances_checked=780, incompatible_pairs=0,
    pair_distance_histogram=calibration['pair_distance_histogram'],
    new_old_edges=412, new_new_edges=0, distinct_used_ports=397,
    port_usage_histogram=calibration['usage_histogram'], port_overloads=0,
    source_reads=1, multisource_radius4_certificate_searches=40,
    source_diameter_BFS_revalidation=0, new_graphs=0,
    worker_CPU_seconds=calibration['worker_cpu_seconds'],
    aggregate_compile_run_CPU_seconds=calibration['aggregate_cpu_seconds'],
    static_joint_incumbent_available=True,
    arbitrary_order_or_subsets_valid=True,
    certificate='EachS_i closedR4 coversB0; everyset-pair hasd_B0<=3; originalport capacities respected.',
    greater_than40_joint_sets_asserted=False)
multiplicity_variant = dict(label='exact40_static_neighborhood_multiplicity_pool_maximum40_20261029',
    status='MAXIMUM_EXACTLY40', fixed_neighborhood_pool=40,
    individual_multiplicity_upper_bound_histogram={'1': 40}, incumbent_total=40,
    sum_upper_bounds=40, proof='EveryS_i contains an originalB0 port withspare1, hence multiplicity_i<=1; all40 unit copies are feasible.',
    numerical_optimization_calls=0, solver_calls=0, graph_reads=0, BFS_runs=0, new_graphs=0,
    CPU_seconds=multiplicity['cpu_seconds'],
    excluded_scope='Only multiplicities of these exact40 independently covering neighborhoods, even after reallocating other members.',
    larger_or_changed_neighborhood_pools_excluded=False)
for variant in family.get('variants', []):
    if variant.get('label') == 'actual_final_capacity_of_old51_failed_prototypes_20261029':
        variant.update(joint_static_original_base_cover_pool_available=True,
            previous_read_had_not_established_static_pool=True,
            superseding_static_calibration='research/ddp/refresh_20261029/d13_D5_static_pool_calibration/REPORT.md')
extend(family, [calibration_variant, multiplicity_variant], evidence('d13_D5_static_pool_calibration'))
family['scope'] += '；后续仅从final literal恢复原B0和40个S，实际认证全部40 B0R4dom、780pair≤3与原capacity；固定40池每组spare1见证使multiplicity_i≤1，因此最优40。'
family['failure_or_result'] += '；新静态校准40/40独立覆盖原B0、780/780兼容、397ports/412usage且0超载；0.767456CPU。保存数据上每组原spare1，使固定40pool max40，额外0.001134505CPU/0图读/BFS/solver。不是第41张图。'
family['lesson_and_restart_condition'] += '；此前动态R4证书不能倒推静态B0覆盖，这次以40次原base多源R4实际补足了该证据。任意顺序/子集现有40可保D5，但这个固定multiplicity pool不能>40，停止重复复制/重排同40。若改生成规则须引入真正不同的邻域或合作连接；新free-part clique池尚未在本记录登记数值运行或结果。'
family['unclosed_gap'] = '全source构造最大性未证；仅固定40静态邻域及其multiplicity的最优值为40。更大/不同邻域池、current40 free-part合作clique及其它连接规则仍未因此排除。'
family['other_metrics'].update(static_original_B0_all40_domination_certified=True,
    static_pair_compatibility_count=780, static_port_overloads=0,
    fixed40_multiplicity_optimum=40, changed_pool_or_cooperative_rule_excluded=False,
    current40_free_part_clique_numerical_result_recorded=False)

guard = rows[guard_id]
dominance_variant = dict(label='complete2755_target_strict_column_dominance_13057_to12961_20261029',
    status='COMPLETE_STRICT_COLUMN_DOMINANCE', source_n=51457, prototype=4580,
    mandatory_count=9, guard_budget=4, unit_cost=True, conflicts=False,
    complete_targets=2755, input_unique_columns=13057, processed_columns=13057,
    retained_inclusion_maximal_columns=12961, removed_columns=96, removed_fraction_about='0.74%',
    exact_saved_superset_witness_checks=96,
    equivalence='Everydeleted guard can be replaced by a retainedproper superset atunit cost; ifalreadyselected, dropdeletedguard. Retained solutionsareoriginalsolutions.',
    actual_cover_existence_decided=False, source_graph_reads=0, new_balls=0,
    solver_calls=0, new_graphs=0, worker_CPU_seconds=dominance['worker_cpu_seconds'],
    aggregate_compile_run_CPU_seconds=dominance['aggregate_cpu_seconds'],
    stopped_no_solver_due_small_reduction=True)
extend(guard, [dominance_variant], evidence('d13_v4580_column_dominance'))
guard['failure_or_result'] += '；全部2755-target guard列的严格包含过滤完成，13057→12961，仅删96约0.74%；96个保留superset见证全精确校验，0.768575CPU，0图读/新球/solver。原四guard存在性仍UNKNOWN。'
guard['scope'] += '；后续只做全列严格dominance等价预处理，没有重启原SAT/LP或变更目标/eligibility。'
guard['lesson_and_restart_condition'] += '；完整strict dominance缩减不足1%，不构成续算理由，本批停止，无新solver。原真正四guard问题保持UNKNOWN；不能将等价预处理当阴性证明。'
guard['other_metrics'].update(strict_dominance_complete=True, strict_dominance_retained_columns=12961,
    strict_dominance_removed_columns=96, strict_dominance_superset_checks=96,
    strict_dominance_new_solver_calls=0, actual_four_guard_R4_existence_status='UNKNOWN')

report = '''# 普通cover显式见证通过与D13静态池和列包含结果

普通cover聚合实验的独立状态已由pending改PASS：三source独立读各1次，MITM完整列六pair共17条短walk，4/8/2与1/1/1全匹配，CPU0.245694，0BFS/生产DP重跑。PREFIX_SCOPE_PROOF正式说明103prefix+3publicbase的单调继承，无106图新算。

D13原40邻域已实际全通过B0R4dom、780pair兼容和397port/412usage容量检验，0超载，编译+运行0.767456CPU。这个新静态证书使任意顺序/子集的40邻域可用于静态joint incumbent；每个S_i又有原spare1端点，故固定40池每种multiplicity≤1，max40由现有全1 incumbent达到。multiplicity检查0.001134505CPU、0图读/BFS/solver，只闭这个确切池。

v4580完整2755-target的strict column dominance精确13057→12961，删96约0.74%，96个保留superset见证全部核验；编译+执行0.768575CPU，0图读/新球/solver。预处理保全<=4 unitcost cover存在性，但未决定它，故仍UNKNOWN；缩减不足而停止，不续旧timer。

新的current40 free-part clique合作规则尚未在本文登记真实RESULT或数值运行，不能把准备当实验。其是否能共同补current51457覆盖，仍待具体实际结果。没有把固定40 multiplicity max40外推到不同邻域池。

本次只改三个现有条目，账本372，构造104/4、confirmed103/3、Lean1不变；无新method/claim/图。root负责最终状态及最后query，不改专家包或root入口。
'''
report_path = HERE / 'COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    extend(row, [], [str(report_path.relative_to(ROOT))])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'COVER_MITM_D13_CALIBRATION_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

prior_report = HERE / 'SUCCESSFUL_D5_COVER_WIKI_REPORT.md'
text = prior_report.read_text()
text = text.replace('独立6具体pair的MITM证据核对仍pending，结果后续另同步。',
    '独立6具体pair的MITM证据核对现已PASS，完整17条NB走步逐组匹配，另0.245694CPU，无BFS/DP重跑。')
prior_report.write_text(text)
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
s = comments.read_text().replace('独立6pair MITM仍待实际回执。',
    '独立6pair MITM已实际PASS，17条全短walk匹配，0.245694CPU，无BFS/DP重跑。', 1)
marker = '<!-- COVER_MITM_D13_STATIC_CALIBRATION_DOMINANCE_20261029 -->'
if marker not in s:
    s += '\n\n' + marker + '''
## 六pair独立见证通过及D13实际静态池和dominance

这是执行记录。ordinarycover聚合行独立MITM已PASS，6pair完整17条NB walk全部匹配，PREFIX_SCOPE_PROOF说明106个base/prefix的静态继承。三final图独立读各1次、0.245694CPU、0BFS/DP重跑。

现有D13四十邻域在原B0上40/40 R4全覆、780/780 pair≤3、0容量超载，编译+执行0.767456CPU；每组原spare1见证给multiplicity_i≤1，固定40pool max40，非一般新邻域池上界。v4580全列dominance 13057→12961仅删96，superset见证96全核验，0.768575CPU、0新solver；四guard实际问题仍UNKNOWN而本预处理停止。

current40 free-part clique合作池待实际RESULT才登记数值，不将准备冒运行。三个既有条目追加变体，ledger372与104/4、confirmed103/3、Lean1保持。[新证据汇总](../research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md)。root最终更新后再最后query。
'''
comments.write_text(screen(s))
with (HERE / 'COVER_MITM_D13_CALIBRATION_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Confirmed six explicit MITM witnesses and106-prefix proof on cover aggregate; added actual40 static calibration/max40 multiplicity and exact negligible v4580 dominance to existing source rows. Ledger372 and graph counters unchanged; cooperative clique awaits actual result; final query waits for root.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
cover_receipt_path = HERE / 'SUCCESSFUL_D5_COVER_WIKI_RECEIPT.json'
cover_receipt = json.loads(cover_receipt_path.read_text())
cover_receipt.update(status='PASS_AGGREGATE_MITM_CONFIRMED_QUERY_PENDING_ROOT',
    independent_MITM_status='ALL_SIX_WITNESSES_MATCH', independent_MITM_pairs=6,
    independent_explicit_walks=17, independent_MITM_CPU_seconds=mitm['CPU_seconds'],
    independent_MITM_BFS=0, independent_MITM_DP_repeats=0,
    prefix_scope_proof='research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREFIX_SCOPE_PROOF.md')
cover_receipt_path.write_text(json.dumps(cover_receipt, ensure_ascii=False, indent=2) + '\n')
receipt = dict(status='PASS_COVER_MITM_STATIC40_DOMINANCE_EXISTING_ROWS_QUERY_PENDING_ROOT',
    updated_UTC=NOW, updated_existing_ids=list(rows), record_count=372,
    MITM_status='ALL_SIX_WITNESSES_MATCH', MITM_pairs=6, MITM_walks=17, MITM_CPU_seconds=mitm['CPU_seconds'],
    logical_prefix_scope=106, static40_R4_covering_sets=40, static40_pair_compatibilities=780,
    static40_capacity_overloads=0, static40_multiplicity_optimum=40,
    dominance_input=13057, dominance_retained=12961, dominance_removed=96, dominance_witness_checks=96,
    actual_four_guard_R4_status='UNKNOWN', new_solver_calls=0,
    current40_cooperative_clique_numerical_result_recorded=False,
    new_experiments=0, new_methods=0, new_claims=0, new_graphs=0, research_jobs_rerun=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True, command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'COVER_MITM_D13_CALIBRATION_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=372, MITM='PASS', final_query='WAITING_FOR_ROOT'), ensure_ascii=False))
