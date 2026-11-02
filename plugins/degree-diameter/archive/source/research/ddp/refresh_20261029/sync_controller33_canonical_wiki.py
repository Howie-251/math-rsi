"""Record the completed canonical-label variant, preserving all previous results."""
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
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt'}]


canon_dir = HERE / 'controller33_canonical_labeling'
calibration = json.loads((canon_dir / 'RESULT.json').read_text())
certificate = json.loads((canon_dir / 'CERTIFICATE.json').read_text())
model = json.loads((canon_dir / 'solve/MODEL.json').read_text())
result = json.loads((canon_dir / 'solve/RESULT.json').read_text())
review_prefix = ROOT / 'reviews/ddp/controller33_canonical_labeling_20261029'
review = json.loads(review_prefix.with_suffix('.response.json').read_text())['structuredContent']
disposition_path = review_prefix.with_suffix('.DISPOSITION.md')
disposition = disposition_path.read_text()
assert calibration['status'] == 'PASS_ONE_SAVED_OBJECT' and calibration['objects_checked'] == 1
assert calibration['all_original_edges_preserved'] and calibration['literal_permutation_bijective']
assert certificate['m_sequence'] == [0, 0, 1, 1, 2, 2, 3, 4, 5, 5]
assert (model['all_variables'], model['clauses']) == (31845, 109466)
assert result['status'] == 'UNKNOWN' and result['solver_calls'] == 1 and result['running'] is False
assert review['status'] == 'SUCCESS' and review['model'] == 'gemini-3.8-flash-high'
assert review['effort'] == 'high' and review['threadId'] == 'e9d18b0f-308e-439e-8104-593218a29dd9'
assert '块两两配对' in disposition

old_validation_path = ROOT / 'research/ddp/second_mechanism/control_unrestricted_validation.json'
old_validation = json.loads(old_validation_path.read_text())
old31 = next(v for v in old_validation if v['order'] == 31)
bowtie_path = ROOT / 'research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.capacity.json'
old32 = json.loads(bowtie_path.read_text())
assert old31['zero_entries_A3'] == 4 and old32['exact_three_step_missing_ordered'] == 14
saved_other_objects = [
    dict(order=31, literal_path='research/ddp/second_mechanism/control_unrestricted_n31.edges',
         inherited_exact_three_step_missing_ordered=4,
         evidence=str(old_validation_path.relative_to(ROOT)), new_BFS_runs=0, new_A3_computations=0,
         hypothetical_F5_order=3875, full_lift_generated=False),
    dict(order=32, literal_path='research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.edges',
         inherited_exact_three_step_missing_ordered=14,
         evidence=str(bowtie_path.relative_to(ROOT)), new_BFS_runs=0, new_A3_computations=0,
         hypothetical_F5_order=4000, full_lift_generated=False,
         object_identity_note='This is bowtie32, not the distinct unrestricted32 saved object.')
]
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 371
ident = 'ddp-wave2-triangle-factor33-controller'
current = next(r for r in before['rows'] if r['id'] == ident)
row = copy.deepcopy(current['source_record'])
variant = dict(label='first_discovery_triangle_block_canonical_labeling_complete_model_20261029',
    status='UNKNOWN', controller_order=33, fixed_disjoint_triangles=11,
    target=dict(Delta=20, D=3, savedL=3750, baseline_scope='Local complete graph; latest global novelty pending'),
    conditional_full_lift_order=4125, controller_graphs_accepted=0, full_fiber_graphs_generated=0,
    labeling_preserves_candidate_isomorphism_classes=True,
    labeling_conditions='Forb>=1,m_b<3b; m_b nondecreasing with equalities allowed; edge(m_b,3b); rootblock unconstrained; compatible0-3/0-6.',
    mixed_vertex_proof='Local complete block-pairing argument in PROOF; no assumed block-cycle argument from reviewer.',
    prefix_encoding='Exact bidirectional Tseitin OR; not one-way counter prefixes.',
    calibration_objects=1, calibration_object='Saved old33 best controller',
    calibration_edges_preserved=66, calibration_m_sequence=certificate['m_sequence'],
    calibration_CPU_seconds=calibration['cpu_seconds'],
    general_theorem_follows_from_constructive_proof_not_single_sample=True,
    extra_edge_variables=495, all_variables=31845, clauses=109466,
    added_variables=165, added_clauses=1125,
    solver_calls=1, solver_wall_limit_seconds=90,
    child_CPU_seconds=result['child_CPU_seconds'], aggregate_CPU_seconds=result['aggregate_CPU_seconds'],
    original_full_model_UNKNOWN_preserved=True,
    new_same_family_canonical_model_not_old_timer_continuation=True,
    whole_controller_family_excluded=False, performance_improvement_proven=False,
    cross_model_review_status='SUCCESS_STATIC_SUPPORT',
    actual_reviewer_model=review['model'], actual_reviewer_effort=review['effort'],
    actual_review_threadId=review['threadId'],
    reviewer_mixed_block_cycle_paragraph_used_as_proof=False,
    inherited_other_literal_objects=saved_other_objects,
    running=False, automatic_timer_seed_or_further_symmetry_continuation=False)
variants = {v['label']: v for v in row.get('variants', [])}
variants[variant['label']] = variant
row['variants'] = list(variants.values())
row['title'] = '33点三角因子旧族：首次发现标号保全已证，原/规范完整模型均UNKNOWN'
row['scope'] += '；同族新增首次发现三角块标号WLOG：非根块最小外邻非降、早于本块、首触点为块首点，与0-3/0-6相容，双向prefix精确编码。保存best仅作一对象校准；一般保全来自构造证明。'
row['failure_or_result'] += '；规范模型31845变量/109466子句（新增165/1125）唯一90秒UNKNOWN，child90.006246CPU/aggregate90.199478735CPU，0控制器/0提升；Gemini静态支持标号与编码，不支持存在性或性能结论。另31 unrestricted与32 bowtie保存对象分别继承A3缺4/14有序槽，未重算或生成3875/4000。'
row['lesson_and_restart_condition'] = '原完整模型90秒UNKNOWN保留；新规范有一般保全证明与双向编码，属于改变表示后的独立有界模型，不是旧timer延长。两者均UNKNOWN，不能排整个33族或宣称规范实际加速。停止本批，不自动再加规范/seed/timer。31/32所选literal既存缺槽直接继承，不能混入另一unrestricted32或重新把读取旧失败计成新实验。'
row['unclosed_gap'] = '固定11K3+跨块二因子的完整33控制器存在性仍OPEN；原模型与保全规范模型均UNKNOWN。无4125图，未生成3875/4000；一般其他controller与非本规则纤维连接也未排。'
row['other_metrics'].update(current_complete_model_status='UNKNOWN_CANONICAL_TERMINAL',
    current_complete_model_running=False, canonical_labeling_proved=True,
    canonical_added_variables=165, canonical_added_clauses=1125,
    canonical_solver_calls=1, canonical_solver_CPU_seconds=result['child_CPU_seconds'],
    canonical_total_CPU_seconds=result['aggregate_CPU_seconds'],
    canonical_reviewer_status='SUCCESS_STATIC_SUPPORT',
    performance_improvement_proven=False, actual_lift4125_generated=False,
    inherited_selected31_A3_missing_ordered=4, inherited_selected32_bowtie_A3_missing_ordered=14)
review_paths = [str(review_prefix.with_suffix(s).relative_to(ROOT))
                for s in ['.prompt.md', '.response.json', '.DISPOSITION.md']]
new_paths = evidence(canon_dir) + evidence(canon_dir / 'solve') + review_paths
new_paths += [str(old_validation_path.relative_to(ROOT)), str(bowtie_path.relative_to(ROOT)),
              saved_other_objects[0]['literal_path'], saved_other_objects[1]['literal_path']]
row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + new_paths))

idea_path = WIKI / 'ideas/ddp-q3-three-step-plane-pencil31.md'
idea_marker = '<!-- DEGREE21_F5_UNEXECUTED_OPPORTUNITY_20261029 -->'
idea_note = '''
## 21度参数只作未执行机会

现有3750点F5公式图的最大度20，因此也满足21度上限，但它仍是同一张已记账图，不能据此增加实例、参数格或纪录计数。本轮两次primary定向查询没有给出可靠的(21,3)最新公开比较值，故该参数只保留为未执行机会：没有进行新的覆盖计算、构图或求解，没有认定新增下界。

下一步需先取得可引用的明确比较值，再决定是否有值得检验的连接规则；这里不建立新method、实验队列或另一个Goal。当前104/4、confirmed103/3、具体公式图Lean1保持，3750的最新全球纪录状态仍待定。
'''
idea_text = idea_path.read_text()
if idea_marker not in idea_text:
    anchor = '\n## Connections\n'
    assert anchor in idea_text
    idea_text = idea_text.replace(anchor, '\n\n' + idea_marker + '\n' + screen(idea_note) + anchor, 1)
    idea_path.write_text(idea_text)

report = '''# 首次发现三角块标号与规范共同路线模型终态

一般标号保全证明已经完成：任一合法连通33控制器同构类可取m_b<3b、m_b非降、首次触达在3b的代表，兼容0-3/0-6。mixed存在性使用本地两两配块论证，不采用外审不严谨的块环解释。旧best的66边与m=[0,0,1,1,2,2,3,4,5,5]单例重标证书仅校准实现，不代替一般证明。

精确双向prefix新增165变量/1125子句，得到31845变量/109466子句。唯一90秒调用UNKNOWN，child90.006246CPU/总90.199478735CPU，0控制器/0提升图。原495外边完整模型90秒UNKNOWN另保留；不把新编码称旧timer续时，也不声称已证明加速或整族无解。

实际Gemini回执SUCCESS/gemini-3.8-flash-high/high，thread e9d18b0f-308e-439e-8104-593218a29dd9，静态支持标号及编码；处置限定如上，不证明存在性或Lean。

31点继承second_mechanism/control_unrestricted_n31.edges的A3缺4有序槽。32点继承wave2/triangle_bowtie32_controller/best.edges及best.capacity.json的14个，而不是另一个unrestricted32对象。没有重跑BFS/A3，未生成3875/4000。

21度基线两次primary查询无可靠比较值，只在现有F5 idea记未执行机会，不计算或建新method。另一个successful_d5_cover_d6_capacity问题尚处oldscope检查/准备，没有在本批登记数值handle或实验结果。

账本371，数学104/4、confirmed103/3、具体公式图Lean1保持。root负责原状态与最终query，本writer未改专家包或root入口。
'''
report_path = HERE / 'CONTROLLER33_CANONICAL_WIKI_REPORT.md'
report_path.write_text(screen(report))
row['report_paths'] = list(dict.fromkeys(row['report_paths'] + [str(report_path.relative_to(ROOT))]))
assert all((ROOT / p).exists() for p in row['report_paths'])
screen(json.dumps(row, ensure_ascii=False))
pending = HERE / 'CONTROLLER33_CANONICAL_WIKI_ROWS.json'
pending.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

marker = '<!-- CONTROLLER33_CANONICAL_LABELING_TERMINAL_20261029 -->'
comment = '''
## 同一33控制器族的保全标号与真实规范模型终态

这是执行记录。首次发现三角块WLOG已证明并以旧best一对象校准，双向prefix新增165变量/1125子句；31845变量/109466子句唯一90秒UNKNOWN，90.006246 childCPU/90.199478735 aggregate，0控制器/0纤维图。原模型UNKNOWN保留；新编码不是旧timer续时，且不声称实际加速或33整族排除。

Gemini实际SUCCESS/high静态支持，thread e9d18b0f-308e-439e-8104-593218a29dd9；mixed存在性使用本地两两配块证明，不采用外审块环解释。旧31 unrestricted与32 bowtie所选literal分别继承A3缺4/14有序槽，无新BFS/矩阵计算、无3875/4000图。21度仅在现有F5 idea附未执行机会，无可靠比较值、计算或新method。另一个D5-cover/D6-capacity问题处检查准备，未登记数值启动。

371记录与104/4、confirmed103/3、Lean1不变，不新Goal或重导Wiki。[本轮实际证据](../research/ddp/refresh_20261029/CONTROLLER33_CANONICAL_WIKI_REPORT.md)。root负责最终状态及query。
'''
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if marker not in comments.read_text():
    with comments.open('a') as output:
        output.write('\n\n' + marker + '\n' + screen(comment))
with (HERE / 'CONTROLLER33_CANONICAL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded proven candidate-preserving first-discovery labels, actual canonical-model UNKNOWN and static review on existing33 record; inherited literal31/bowtie32 gaps; degree21 opportunity only in existing F5 idea. No new graph/method/claim; final query waits for root.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 371
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_CONTROLLER33_CANONICAL_EXISTING_VARIANT_QUERY_PENDING_ROOT',
    updated_UTC=NOW, updated_existing_experiment=ident, record_count=371,
    canonical_general_preservation_proof=True, calibration_objects=1,
    canonical_solver_status='UNKNOWN_TERMINAL', canonical_solver_calls=1,
    canonical_solver_child_CPU_seconds=result['child_CPU_seconds'],
    canonical_total_CPU_seconds=result['aggregate_CPU_seconds'],
    cross_model_review_status='SUCCESS_STATIC_SUPPORT', actual_reviewer_model=review['model'],
    actual_reviewer_effort=review['effort'], actual_review_threadId=review['threadId'],
    whole33_family_excluded=False, performance_improvement_proven=False,
    inherited31_literal=saved_other_objects[0]['literal_path'], inherited31_missing_ordered=4,
    inherited32_literal=saved_other_objects[1]['literal_path'], inherited32_missing_ordered=14,
    inherited_objects_recomputed=False, degree21_opportunity='UNEXECUTED_BASELINE_UNCONFIRMED',
    degree21_new_method=False, D5cover_D6capacity_numeric_start_recorded=False,
    new_graphs=0, new_claims=0, new_methods=0, research_jobs_rerun=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True, command=command, helper_stdout=run.stdout.strip(),
    changed_wiki_paths=['research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md',
        current['wiki_path'], str(idea_path.relative_to(ROOT)),
        'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md', 'research-wiki/index.md',
        'research-wiki/query_pack.md', 'research-wiki/log.md'])
receipt_path = HERE / 'CONTROLLER33_CANONICAL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=371, canonical_status='UNKNOWN', final_query='WAITING_FOR_ROOT'), ensure_ascii=False))
