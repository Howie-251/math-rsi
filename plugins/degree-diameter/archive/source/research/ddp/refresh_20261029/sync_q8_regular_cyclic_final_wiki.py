"""Record completed cyclic finite exclusion and route-block gate; reviews stay pending."""
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


def read(relative):
    return json.loads((HERE / relative).read_text())


def rel(path):
    return str(path.relative_to(ROOT))


def update_variants(row, additions, paths):
    variants = {v['label']: v for v in row.get('variants', [])}
    variants.update({v['label']: v for v in additions})
    row['variants'] = list(variants.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))


before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 371
existing = {r['id']: r for r in before['rows']}
q8_id = 'ddp-q8-k64-cube-external2factor-13d3-20261029'
v4580_id = 'ddp-d13-v4580-current51457-fourguard-unknown-20261029'
rows = {key: copy.deepcopy(existing[key]['source_record']) for key in [q8_id, v4580_id]}
degree = read('q8_degree_budget_route_gate/LOCAL_CHECK.json')
formal = read('q8_cyclic_quotient_route_capacity/RESULT.json')
canonical = read('q8_cyclic_quotient_route_capacity/CANONICAL_RESULT.json')
voltage = read('q8_cyclic_quotient_route_capacity/VOLTAGE_RESULT.json')
blocks = read('d13_v4580_routeblock_proxy/RESULT.json')
assert degree['outside_bounds_by_root_extra_degree'] == {'0': 36, '1': 54}
assert formal['quotients'] == 213798 and formal['passed'] == 3189
assert canonical['canonical_quotients'] == 110
assert voltage['status'] == 'COMPLETE_CYCLIC_FAMILY_NO_HIT'
assert voltage['canonical_total'] == voltage['completed'] == 110
assert voltage['completed_labelled_quotients'] == 3189
assert voltage['counts']['parity_pass'] == 28
assert voltage['counts']['mod4_domain'] == 3104 and voltage['counts']['mod4_pass'] == 0
assert blocks['status'] == 'COMPLETE_OVERLAP_AWARE_WHOLE_ROUTE_BLOCK_NEGATIVE'
assert blocks['DP_states'] == 256 and blocks['DP_transitions'] == 1170
assert blocks['arbitrary_four_guard_R4_excluded'] is False

q8_dirs = ['q8_degree_budget_route_gate', 'q8_cyclic_quotient_route_capacity']
q8_paths = [rel(p) for directory in q8_dirs for p in sorted((HERE / directory).iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt'}]
block_paths = [rel(p) for p in sorted((HERE / 'd13_v4580_routeblock_proxy').iterdir())
               if p.is_file() and p.suffix in {'.md', '.json', '.py'}]

q8 = rows[q8_id]
q8['title'] = 'q8辅助图必二正则；全部C8对称共同电压域完整排除，非循环域仍开放'
q8['scope'] += '；一般H含指定8Q3且maxdegree5/D3必extra恰2regular，由outside≤18s+36<56(s≤1)推出；全部C8-deck-invariant2factor的标签商与共同电压域现已完整有限排除。'
q8['failure_or_result'] += '；后续完整标签商门213798→3189，再按48个cube自同构归110商；全部110共同电压逐位检验完成，20050 parity域仅28通过，3104 mod4域全失败，mod8域0。此确定性有限结果关闭原244轨道同一C8范围，未续旧SAT，未生成64辅助正例或1088主图。'
q8['lesson_and_restart_condition'] = '保留各SAT历史UNKNOWN，但其C8范围已被后续完整商/共同电压检验排除，不再派该范围的timer、seed、pi或电压续试。形式短路够多不保证同一电压同时取遍：所有剩余商已在mod4必要余类容量门失败。一般辅助必2regular，无独立非正则完成分支；下一入口须打破C8对称并提出具体共同覆盖规则。跨模审阅与独立mod4小核对待真实结果，不预记通过。'
q8['unclosed_gap'] = '一般非循环2factor辅助图仍开放，可含pencil内部extra；此前全cross-pencil模型UNKNOWN仍不能排一般非循环域。整个C8-deck-invariant范围已完整有限排除，不再列为UNKNOWN开放。无主1088图。'
q8['other_metrics'].update(auxiliary_extra_degree_exactly_two_necessary=True,
    degree_one_outside_upper_bound=54, outside_vertices_required=56,
    cyclic_deck_full_family_excluded=True, cyclic_quotients=213798,
    cyclic_formal_survivors=3189, cyclic_canonical_quotients=110,
    cyclic_voltage_completed_quotients=110, cyclic_voltage_parity_pass=28,
    cyclic_voltage_mod4_domain=3104, cyclic_voltage_mod4_pass=0,
    cyclic_voltage_mod8_domain=0, cyclic_voltage_lift_status=voltage['status'],
    cyclic_voltage_solver_calls=0, cyclic_voltage_CPU_seconds=voltage['CPU_seconds'],
    cyclic_formal_CPU_seconds=formal['CPU_seconds'], cyclic_canonical_CPU_seconds=canonical['CPU_seconds'],
    independent_mod4_verification_status='PENDING', new_cross_model_review_status='PENDING',
    new_cross_model_review_receipt_recorded=False, actual_main_graphs=0)
for variant in q8['variants']:
    if variant['label'] == 'cyclic_deck_invariant_all_extra_edge_orbits_20261029':
        variant.update(status='SUPERSEDED_BY_COMPLETE_FINITE_C8_EXCLUSION',
            original_solver_terminal_status='UNKNOWN', scope_closed=True,
            superseding_result='research/ddp/refresh_20261029/q8_cyclic_quotient_route_capacity/VOLTAGE_RESULT.json',
            superseding_reason='Same entire C8-invariant2factor scope exhausted by quotient and joint-voltage necessary gates; no SAT rerun.')
q8_variants = [
    dict(label='general8Q3_extra_degree_two_necessary_20261029',
         status='PAPER_PROOF_WITH_LOCAL_ARITHMETIC_CHECK',
         scope='Every simple64-vertex graph containing specified8Q3 withmaximumdegree5 anddiameter<=3, no symmetry or induced-pencil assumption.',
         implication='All extra degrees exactly2; no separate nonregular gadget-completion scope.',
         outside_bound='18*s+36', outside_required=56, s0_bound=36, s1_bound=54,
         local_CPU_seconds=degree['cpu_seconds'], full_graphs_generated=0, solver_calls=0,
         Lean_formalized=False, cross_model_review_status='PENDING'),
    dict(label='entire_cyclic_deck_twofactor_quotient_and_joint_voltage_exclusion_20261029',
         status='COMPLETE_CYCLIC_FAMILY_NO_HIT', labelled_quotients=213798,
         formal_capacity_rejected=210609, formal_capacity_survivors=3189,
         cube_automorphisms=48, canonical_quotients=110, completed=110,
         voltage_counts=voltage['counts'],
         reason='Every remaining common voltage fails necessary modulo4 residue multiplicity; no modulo8 case survives.',
         scope='Every C8-deck-translation-invariant extra2factor on8Q3, allowing same-pencil chords, same-label +/-d edges and halfturn matchings; full simple-degree legality included.',
         source_solver_reruns=0, solver_calls=0, actual64_positive_graphs=0,
         main1088_graphs=0, generic_noncyclic_twofactor_excluded=False,
         formal_gate_CPU_seconds=formal['CPU_seconds'], canonical_CPU_seconds=canonical['CPU_seconds'],
         voltage_CPU_seconds=voltage['CPU_seconds'],
         same_family_static_code_review='Completed separately without rerunning computation.',
         independent_mod4_verification_status='PENDING', cross_model_review_status='PENDING')]
update_variants(q8, q8_variants, q8_paths)

v4580 = rows[v4580_id]
v4580['title'] = 'Current51457 v4580：自然重叠整块充分域阴性，真正四guard R4仍UNKNOWN'
v4580['failure_or_result'] += '；新路线块13个B3中11非空，13057当前guard列产生9种整块mask；正确接受条件是≤4guards取得的完整块目标并集覆盖全部2755，而非所有11块各有负责人。256states/1170transitions完整失败，总CPU0.403699516；只闭该自然整块充分域，真正R4仍UNKNOWN。'
v4580['lesson_and_restart_condition'] += '；50828块21目标单guard最多18，且每目标都在其它块中，不能凭该块零完整支持排重叠联合。实际正确overlap验收也完整阴性，整块规则停止；一般四guard允许分裂目标，未被排除，不追加块细分或旧timer。'
v4580['unclosed_gap'] = '固定v4580/current51457真正<=4guard的完整R4覆盖仍UNKNOWN；closedB1强proxy与自然重叠whole-block充分规则已各完整阴性，均不是完整R4的必要条件。一般partial-star、其它mandatory与共同容量问题未排。'
v4580['other_metrics'].update(overlap_aware_whole_route_blocks_status=blocks['status'],
    whole_route_block_DP_states=256, whole_route_block_DP_transitions=1170,
    whole_route_block_CPU_seconds=blocks['CPU_seconds'], whole_route_block_new_graphs=0,
    unrestricted_four_guard_R4_excluded=False)
block_variant = dict(label='natural_overlap_aware_whole_route_block_proxy_v4580_20261029',
    status=blocks['status'], source_n=51457, source_m=324863, missing_targets=2755,
    guard_representatives=13057, guard_cap=4, local_radius3_expansions=13,
    nonempty_blocks=11, unique_nonzero_block_masks=9, useful_guards=53,
    acceptance='Union of actual targets in the complete route blocks covered by at most4 guards equals all2755 targets.',
    DP_states=256, DP_transitions=1170,
    initial_all11_block_ownership_model='Stricter condition; preserved as history, not used as natural-overlap conclusion.',
    hard_block=50828, hard_block_targets=21, maximum_single_guard_coverage=18,
    all_hard_block_targets_have_other_block_membership=True,
    all_coverable_blocks_union_equals_all2755=True,
    complete_graphs_generated=0, source_allroot_BFS=0, new_selected_R4_BFS=0, solver_calls=0,
    CPU_seconds=blocks['CPU_seconds'], corrected_DP_CPU_seconds=blocks['overlap_aware_corrected_DP_CPU_seconds'],
    stopped_no_refinement=True, unrestricted_four_guard_R4_excluded=False)
update_variants(v4580, [block_variant], block_paths)

report = '''# q8完整循环域排除与D13重叠整块检验

本批目标新图0，104/4、confirmed103/3、具体公式图Lean1保持。此处只汇总已保存的完成计算，跨模审阅及独立mod4小核对仍待真实回执。

一般辅助H含8个指定Q3且maxdegree5/D3时，extra必须恰二正则：若根extra度s≤1，所有至多3步外pencil目标数≤18s+36≤54<56。允许pencil内extra，无对称假设；该引理未Lean化。

对于完整C8 deck平移不变二因子，普通环/两端半周loop路径商的213798有标号范围全执行；形式相位门拒210609、留3189。48个cube自同构将其归110商。共同电压逐位检验110全部完成，20050 parity域中28通过，3104 mod4域全部失败，mod8域0。因此原244轨道SAT的UNKNOWN保留为历史返回，但相同整个C8范围已由后续有限检验排除，不再开放或续算。一般非循环二因子仍开放；主1088未生成。

D13 v4580将U=2755目标按r∈N(f)的B3分成13块、11非空。guard可覆盖的完整块mask共9种。初始全11块各有负责人条件过强，不能以50828块零整块支持直接结束自然联合，因为其它可覆盖块并集确实等于全部U。修正接受条件为≤4guards覆盖完整块的实际目标并集等于U，256状态/1170转移无接受状态，总0.403699516CPU。只闭自然整块充分域，真正四guard R4仍UNKNOWN，停止块细分。

全部源代码、输入和结果沿已有实验附加变体；无新method/claim。专家交付19:35快照保持原样，必要的新勘误由root补充。本次不重跑图/BFS/solver/Lean。
'''
report_path = HERE / 'Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    update_variants(row, [], [rel(report_path)])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / p).exists() for p in row['report_paths'])
pending = HERE / 'Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

marker = '<!-- Q8_REGULAR_FULL_C8_AND_D13_OVERLAP_20261029 -->'
comment = '''
## q8一般二正则必要条件与完整循环域排除

这是执行记录，不是新增人工原话。任何含指定8Q3、最大度5、D3辅助图的extra必二正则，由outside≤18s+36<56(s≤1)证明，不再单列非正则gadget完成问题。整个C8-deck-invariant二因子域已完成213798商→3189形式门保留→110 cubeAut规范商→110共同电压全执行；paritypass28、mod4域3104且pass0，故旧244轨道UNKNOWN的同一C8数学范围由此完整排除，不续该SAT。一般非循环二因子仍开放，未生成1088。

D13 v4580自然重叠整块规则已按“完整块的实际目标并集=全部2755”接受条件完整检查，256states/1170transitions无≤4解；初始11块逐块责任过强的结果只作历史。真实R4四guard仍UNKNOWN，不自动细分块或续旧timer。

跨模审阅与独立mod4小核对均待真实结果，不提前登记通过。数学104/4、confirmed103/3、Lean1和371账本行保持，无新图/方法/claim。专家19:35交付快照未改；root负责状态入口。[本轮现有证据汇总](../research/ddp/refresh_20261029/Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_REPORT.md)。
'''
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if marker not in comments.read_text():
    with comments.open('a') as output:
        output.write('\n\n' + marker + '\n' + screen(comment))
with (HERE / 'Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded general auxiliary exact-extra-degree lemma, completed full C8 joint-voltage exclusion, and corrected overlap-aware v4580 whole-block negative; existing two records only; external review and independent mod4 check pending.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 371
assert {r['id'] for r in after['rows']} == {r['id'] for r in before['rows']}
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_INCREMENTAL_COMPLETED_MATH_REVIEW_PENDING', updated_UTC=NOW,
    updated_existing_ids=list(rows), record_count_before=371, record_count_after=371,
    new_experiments=0, new_claims=0, valid_graph_examples=104, valid_parameter_pairs=4,
    confirmed_graph_examples=103, confirmed_parameter_pairs=3, complete_Lean_instances=1,
    new_graphs=0, main1088_graphs=0, extra_degree_two_necessary=True,
    full_C8_family_excluded=True, cyclic_canonical_completed=110,
    cyclic_mod4_pass=0, cyclic_original_SAT_terminal_result='UNKNOWN',
    general_noncyclic_factor_still_open=True, v4580_true_R4_still_UNKNOWN=True,
    cross_model_review_status='PENDING', independent_mod4_verification_status='PENDING',
    research_jobs_rerun=0, command=command, helper_stdout=result.stdout.strip(),
    final_query_helper='aris_repo/tools/research_wiki.py:rebuild_query_pack(research-wiki)',
    changed_wiki_paths=['research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md',
       *[existing[k]['wiki_path'] for k in rows], 'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md',
       'research-wiki/index.md', 'research-wiki/query_pack.md', 'research-wiki/log.md'])
receipt_path = HERE / 'Q8_REGULAR_CYCLIC_D13_BLOCK_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=rel(receipt_path), record_count=371,
    existing_records_updated=2, independent_mod4_check='PENDING', cross_model_review='PENDING'), ensure_ascii=False))
