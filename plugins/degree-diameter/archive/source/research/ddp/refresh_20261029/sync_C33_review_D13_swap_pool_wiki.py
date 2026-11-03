"""Record actual proof review and the two bounded core-swap outcomes."""
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


review_prefix = ROOT / 'reviews/ddp/controller33_capacity_phase_20261029'
review = json.loads(review_prefix.with_suffix('.response.json').read_text())['structuredContent']
assert (review['status'], review['model'], review['effort'], review['threadId']) == (
    'SUCCESS', 'gemini-3.8-flash-high', 'high', '18be21ce-985d-4053-9f3c-8764ade49697')
signature = load('d13_core_swap_extension_signature/RESULT.json')
assert signature['status'] == 'SPECIFIED_CORE_SWAP_HAS_NO_FULL_AUTOMORPHISM_EXTENSION'
witness = signature['first_multiplicity_mismatch']
assert witness['source_peripheral_vertices'] == [50629]
assert (witness['source_multiplicity'], witness['target_multiplicity']) == (1, 0)
pool = load('d13_core_swap_static_pool/RESULT.json')
assert pool['status'] == 'EXACT_POOL_MAXIMUM40'
assert pool['fully_covering_new_indices'] == [0, 8, 17]
assert pool['combinations_by_total'] == {'43': 1, '42': 43, '41': 903}
assert pool['tested_improving_combinations'] == pool['rejection_counts']['port_capacity'] == 947
assert pool['pool_maximum_added_vertices'] == 40
assert pool['multisource_R4_runs'] == 3 and pool['solver_calls'] == pool['new_graphs'] == 0
subset = load('d13_core_swap_static_pool/SUBSET_READOUT.json')
assert subset['rows'][0]['strict_old_supersets'] == [
    {'old_index': 37, 'old_added_vertex': 51454, 'released_ports': [50578]}]

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 372
ids = ['ddp-wave2-triangle-factor33-controller',
       'ddp-h9-d13-51417-source-binding-20261027',
       'ddp-d13-singlefault-star-family-51457-20261027']
existing = {r['id']: r for r in before['rows']}
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in ids}
paper_review = dict(
    status='SUCCESS_STATIC_MATH_PASS', actual_model=review['model'], effort=review['effort'],
    thread_id=review['threadId'], original_call_only=True, retried=False,
    proofs=['controller33_route_capacity/PROOF.md', 'controller33_C11_exact/DERIVATION_PACKAGE.md'],
    scope='Static review of two mathematical proofs only; does not certify enumeration code, CNF, solver results, Lean or a public record.',
    disposition='Moments are necessary conditions only; reviewer occasional sufficient-condition wording is not adopted.',
    response=str(review_prefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition_path=str(review_prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
row33 = rows[ids[0]]
for variant in row33['variants']:
    if variant.get('label') in {
        'C11_simultaneous_triangle_block_translation_complete_NB3_gate_20261029',
        'local_triangle_fourcycle_and_weighted_pair_NB3_capacity_20261029',
        'complete_common_NB3_model_with_local_capacity_cuts_20261029'}:
        variant['combined_external_review_status'] = 'SUCCESS_STATIC_MATH_PASS'
        variant.pop('combined_cross_model_review_status', None)
        variant['combined_paper_review'] = paper_review
row33['other_metrics']['combined_C11_capacity_external_review_status'] = 'SUCCESS_STATIC_MATH_PASS'
row33['other_metrics']['combined_C11_capacity_review_thread'] = review['threadId']
row33['unclosed_gap'] = row33['unclosed_gap'].replace(
    '联合Gemini外审仍pending；', '联合Gemini两份纸面证明实际PASS，矩只作必要条件；')
if '；联合Gemini两proof实际PASS' not in row33['failure_or_result']:
    row33['failure_or_result'] += '；联合Gemini两proof实际PASS，actual gemini-3.8-flash-high/high/thread18be21ce-985d-4053-9f3c-8764ade49697；仅数学静态支持，不能将枚举、CNF或UNKNOWN改写为已认证存在性。'
update(row33, [], [str(review_prefix.with_suffix(s).relative_to(ROOT))
                  for s in ['.prompt.md', '.response.json', '.DISPOSITION.md']])

rowaut = rows[ids[1]]
aut_variant = dict(
    label='specified_core_swap_full_extension_signature_multiplicity_gate_20261029',
    status=signature['status'], base_n=51417, base_m=324451,
    core_n=50554, peripheral_n=863, inherited_core_swap_pairs=17157,
    core_automorphism_rechecked=False, source_graph_reads=1,
    peripheral_signature_groups=843, signature_group_size_histogram=signature['signature_group_size_histogram'],
    compared_signature_groups=68, obstruction=witness,
    exclusion='This specified core involution cannot extend to a full-source automorphism, even with an arbitrary permutation of the863 peripheral vertices.',
    all_full_source_automorphisms_excluded=False,
    full_edge_automorphism_checks=0, BFS_calls=0, solver_calls=0, new_graphs=0,
    CPU_seconds=signature['CPU_seconds'])
update(rowaut, [aut_variant], evidence('d13_core_swap_extension_signature'))
if '；随后一次literal边表签名门' not in rowaut['scope']:
    rowaut['scope'] += '；随后一次literal边表签名门严格否定这个指定core involution的任意外围延拓，不否定其它全图自同构。'
if '；外围50629' not in rowaut['failure_or_result']:
    rowaut['failure_or_result'] += '；外围50629的core邻域签名原重数1，施该core swap后重数0，故即使外围任意置换也不能延拓这个core swap；一次source读、0BFS/solver、0.304361371CPU。'
rowaut['unclosed_gap'] = '指定core involution的全图延拓已由外围签名重数1≠0严格排除。其它全图自同构及其混合邻域池未排；另行固定外围guard的literal候选不是全图Aut，须实际验证覆盖，不能继承Aut结论。'
rowaut['other_metrics'].update(
    specified_core_swap_full_extension_excluded=True,
    specified_core_swap_extension_witness=50629,
    specified_core_swap_target_signature_multiplicity=0,
    full_Aut_nonexistence_proven=False)

rowpool = rows[ids[2]]
pool_variant = dict(
    label='fixed_peripheral_core_swap_three_new_sets_exact43_pool_max40_20261029',
    status=pool['status'],
    rule='Swap the saved core labels but retain literal peripheral guard IDs; not a full-source automorphism.',
    new_candidate_indices=[0, 8, 17], source_n=51417, source_m=324451,
    new_candidate_count=3, all_three_R4_cover_entire_B0=True,
    all_core_omissions=0, all_peripheral_omissions=0,
    R3_sizes=[11647, 11040, 11062], R4_sizes=[51417, 51417, 51417],
    all_old_new_and_new_new_set_distances_at_most=3,
    original40_balls_or_780_old_old_distances_recomputed=False,
    fixed_pool_size=43, each_member_at_most_once=True,
    improving_choices_by_total=pool['combinations_by_total'],
    tested_improving_choices=947, capacity_rejections=947, route_rejections=0,
    exact_pool_optimum=40, solver_calls=0,
    source_reads=1, new_multisource_R4_runs=3, source_D5_allroot_BFS=0,
    CPU_seconds=pool['CPU_seconds'], new_graphs=0,
    subset_readout='new index0 is oldS37 minus port50578; replacing that existing helper neighborhood preserves order and can release one old port.',
    subset_relation_old_added_vertex=51454, released_port=50578,
    same_order_rule_valid_but_new_edge_table_not_generated=True,
    general_neighborhood_or_modified_guard_excluded=False,
    repeated_new_set_multiplicity_outside_scope=True)
update(rowpool, [pool_variant], evidence('d13_core_swap_static_pool'))
if '；固定外围core-swap新增0/8/17' not in rowpool['scope']:
    rowpool['scope'] += '；固定外围core-swap新增0/8/17三邻域实际全B0R4覆盖并与old40兼容；仅old40+这3、每项至多一次的43池完整改进子集排除，max40。'
if '；三新邻域覆盖预测获支持' not in rowpool['failure_or_result']:
    rowpool['failure_or_result'] += '；三新邻域覆盖预测获支持，R3大小11647/11040/11062，R4均51417；947个≥41项组合（43:1/42:43/41:903）全部端口超载，路线均兼容，固定pool最优40。3次R4、0solver/新图、0.372726496CPU。new0=oldS37减50578是同阶合法邻域变化，可释放一端口但不增记构造。'
rowpool['lesson_and_restart_condition'] += '；本次覆盖可由显式literal新邻域取得，即使其来源core操作不能延拓全Aut；实际瓶颈是共同端口容量。停止这固定43个0/1邻域池，不再换subset；同阶子集替换释放端口是下一步可利用信息，不等于已经得到第41个helper。'
rowpool['unclosed_gap'] = '原40池、free-part合作clique池、以及原40+三个已认证core-swap新邻域的固定43个0/1池均闭合；不同邻域、额外guard、可复用端口变化或其它合作规则仍开放。没有输出新图或证明51457最大。'
rowpool['other_metrics'].update(
    fixed_peripheral_core_swap_new_R4_certificates=3,
    fixed43_pool_improving_combinations=947, fixed43_pool_optimum=40,
    fixed43_pool_all_improving_subsets_excluded=True,
    same_order_subset_variation_releases_port=50578,
    latest_new_graphs=0)

report = '''# C33实际外审与D13指定core-swap两种问题

原一次Gemini调用已真实SUCCESS，actualgemini-3.8-flash-high/high，thread18be21ce-985d-4053-9f3c-8764ade49697。两份纸面证明PASS：一般短圈/加权pair容量与C11相位矩障碍。矩方程只作必要条件，不采用回复偶发“充要”措辞；外审不认证枚举代码、CNF、Lean或公开纪录。cut模型依旧一次60秒UNKNOWN，0controller/提升。

指定core involution的全图延拓被外围50629严格否定：原core邻域签名重数1，变换后重数0，即使允许863外围任意置换也不可能。一次literal source读、0BFS/solver、0.304361371CPU。只排这个core swap，不排其它全图Aut。

分别把core labels交换而保留外围guard的三个literal新邻域0/8/17，实际3次多源R4均全覆盖B0，core/peripheral零缺项，与old40和彼此全set-distance≤3，0.372726496CPU。它们不依赖已否定的全Aut声明。原40加这3、每项至多一次的固定43池，全部947个≥41选择（1+43+903）均端口超载，路线均通过，故精确最优40，0solver/新图。其它邻域或重复新集不在排除范围。

保存集合读数另给new0=oldS37−50578：替换对应已有helper邻域可保同阶合法覆盖并释放一旧端口；未输出新边表、没有新增计数或下界。后续单端口规则和C31模型尚未据派发写成运行或终态。

复用三个既有行，ledger372、104/4、confirmed103/3、Lean1不变，最终query仍等待root最终状态。
'''
report_path = HERE / 'C33_REVIEW_D13_SWAP_POOL_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    update(row, [], [str(report_path.relative_to(ROOT))])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'C33_REVIEW_D13_SWAP_POOL_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- C33_REVIEW_D13_SWAP_POOL_COMPLETED_20261029 -->'
note = '''
## C33两份证明实际外审通过；D13三新邻域与共同容量区分

原一次Gemini实际SUCCESS/gemini-3.8-flash-high/high/thread18be21ce-985d-4053-9f3c-8764ade49697，两paperproof PASS；矩条件仅必要，不以外审覆盖cut UNKNOWN或认证CNF/Lean。此前pending以此回执为准。

指定core swap因外围50629签名重数1→0不能全图延拓，含任意外围置换；不排其它Aut。另一规则固定外围guard产生0/8/17三新literal邻域，实际R4全覆盖且old/new均路线兼容；固定43个0/1池947个改进选择全部端口阻断，max40。new0=oldS37−50578给同阶释放一端口的合法变化，未生成/增记新图。ledger372及104/4、confirmed103/3、Lean1不变。[真实证据与严格范围](../research/ddp/refresh_20261029/C33_REVIEW_D13_SWAP_POOL_WIKI_REPORT.md)。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:
        out.write('\n\n' + marker + '\n' + screen(note))
with (HERE / 'C33_REVIEW_D13_SWAP_POOL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded actualSUCCESS static two-proof Gemini review, specified core-swap full-extension signature obstruction, and actual3 R4-certified literal neighborhoods with exact43pool max40; no new method/graph; subsequent tasks not presumed running.')
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for key in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[key] == after[key]
receipt = dict(
    status='PASS_C33_ACTUAL_REVIEW_D13_SWAP_POOL_EXISTING_VARIANTS_PENDING_FINAL',
    updated_UTC=NOW, updated_existing_ids=ids, record_count=372,
    combined_static_proof_review=paper_review,
    specified_core_swap_extension='EXCLUDED_BY_SIGNATURE_MULTIPLICITY_1_TO_0',
    other_full_automorphisms_excluded=False, new_R4_covering_sets=3,
    fixed_pool_size=43, fixed_pool_optimum=40, tested_improving_combinations=947,
    all_rejections='port_capacity', actual_new_multisource_R4_runs=3,
    new_experiments=0, new_methods=0, new_claims=0, new_graphs=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3,
    complete_Lean_instances=1, future_one_port_or_C31_runs_recorded=False,
    final_query_rebuild_after_root_update_pending=True,
    command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'C33_REVIEW_D13_SWAP_POOL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
                     record_count=372, final_query='WAITING_FOR_ROOT_FINAL'), ensure_ascii=False))
