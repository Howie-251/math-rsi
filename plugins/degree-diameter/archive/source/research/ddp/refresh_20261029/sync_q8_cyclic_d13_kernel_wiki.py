"""Incrementally record completed cyclic auxiliary and strong-proxy work; no research runs."""
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


def read(relative):
    return json.loads((HERE / relative).read_text())


def rel(path):
    return str(path.relative_to(ROOT))


def screen(text):
    assert not capture.screen(text), capture.screen(text)
    return text


def extend(row, variants, paths):
    old = {v['label']: v for v in row.get('variants', [])}
    old.update({v['label']: v for v in variants})
    row['variants'] = list(old.values())
    row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))


before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 371
records = {r['id']: r for r in before['rows']}
q8_id = 'ddp-q8-k64-cube-external2factor-13d3-20261029'
d13_id = 'ddp-d13-singlefault-star-family-51457-20261027'
v4580_id = 'ddp-d13-v4580-current51457-fourguard-unknown-20261029'
rows = {key: copy.deepcopy(records[key]['source_record']) for key in [q8_id, d13_id, v4580_id]}
twist = read('q8_cyclic_gadget_construction/pi_twist_obstruction/RESULT.json')
half = read('q8_cyclic_halfturn_repair/RESULT.json')
orbit = read('q8_cyclic_orbit_sat/RESULT.json')
model = read('q8_cyclic_orbit_sat/MODEL.json')
kernel = read('d13_remaining_strong_proxy_kernel/RESULT.json')
assert twist['ordered_pairs_checked'] == 441 and twist['full_pairs'] == 18
assert half['tested_cases'] == half['frozen_cases'] == 14406 and half['main1088_graphs'] == 0
assert orbit['status'] == 'UNKNOWN' and orbit['solver_calls'] == 1
assert model['extra_edge_orbit_variables'] == 244 and model['all_variables'] == 24428 and model['clauses'] == 86597
assert kernel['visited'] == kernel['frozen_count'] == 38 and kernel['unattempted'] == 0
kernel_counts = kernel['row_status_counts']
assert kernel_counts == {'REUSED_PROVED_STRONG_LOWER_BOUND_EXCEEDS_BUDGET': 1,
                         'STRONG_CERTIFICATE_IMPOSSIBLE_ZERO_SUPPORT': 6,
                         'EXACT_NO_STRONG_CERTIFICATE_WITHIN_ACTUAL_BUDGET': 31}

q8_dirs = ['q8_cyclic_gadget_construction', 'q8_cyclic_gadget_construction/pi_twist_obstruction',
           'q8_cyclic_halfturn_repair', 'q8_cyclic_orbit_sat']
q8_paths = [rel(p) for directory in q8_dirs for p in sorted((HERE / directory).iterdir())
            if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp'}]
kernel_paths = [rel(p) for p in sorted((HERE / 'd13_remaining_strong_proxy_kernel').iterdir())
                if p.is_file() and p.suffix in {'.md', '.json', '.py'}]
q8_variants = [
    dict(label='fixed_pi_twist_all_Z8_voltages_halfturn_obstruction_20261029',
         status='COMPLETE_FIXED_PI_FAMILY_EXCLUSION', pi=[3, 4, 7, 0, 1, 6, 5, 2],
         scope='Z8 deck with fixed Q3 and sigma(a,l)=(a+delta_l,pi(l)), arbitrary delta in Z8^8; includes degenerate settings.',
         finite_sumset_pairs=441, full_sumset_pairs=18,
         reason='All-antipode coverage forces step1/step3 three-term AP sets, excluding every same-label halfturn phase4 short word.',
         delta_assignments_enumerated=0, graphs_enumerated_for_proof=0,
         finite_lemma_CPU_seconds=twist['CPU_seconds'], Lean_formalized=False,
         positive_auxiliary_graphs=0, main1088_graphs=0),
    dict(label='three_cycle_halfturn4_repair_14406_20261029',
         status=half['status'], pi=[1, 3, 6, 0, 5, 7, 2, 4],
         scope='Frozen7^4*6 legal5regular auxiliary graphs; three cycle-voltage sums fixed4; only stated nonzero domain.',
         prediction_supported='Every same-label halfturn phase4 is reached within3; first candidate covers all same-label phases.',
         full_D3_prediction='REFUTED_WITHIN_FROZEN_FAMILY', candidates=14406, first_root_R3_failures=14406,
         unattempted=0, CPU_seconds=half['CPU_seconds'], positive_auxiliary_graphs=0, main1088_graphs=0),
    dict(label='cyclic_deck_invariant_all_extra_edge_orbits_20261029', status='UNKNOWN',
         scope='All deck-translation-invariant2factors added to8Q3; permits internal-pencil chords and same-label halfturn matching; cyclic symmetry is a restriction, not WLOG for all K64.',
         extra_edge_orbit_variables=244, all_variables=24428, clauses=86597,
         degree_occurrences_per_label=60, repeated_orbit_variables_retained=True,
         R2_pair_orbits=256, crosspencil_R3_pair_orbits=228,
         solver_calls=1, solver_wall_limit_seconds=120,
         aggregate_CPU_seconds=orbit['aggregate_CPU_seconds'], positive_auxiliary_graphs=0, main1088_graphs=0,
         numerical_job_terminal=True, scope_closed=False,
         review_scope='Same-family static code audit only; no new cross-model review receipt recorded.')
]
q8 = rows[q8_id]
q8['title'] = 'q8辅助K64：固定pi整族障碍、半周修复14406失败、循环轨道模型UNKNOWN'
q8['scope'] += '；后续固定pi_twist全Z8电压族由短字/441和集表排除；三循环半周4新规则只闭冻结14406域；完整cyclic-deck-invariant额外2factor域一次120秒UNKNOWN。'
q8['failure_or_result'] += '；新pi_twist具体候选反极点全覆盖仍漏同标签半周，随后证明该固定pi任意delta均不能D3；改三循环闭环电压4确实修半周，但14406个合法5regular辅助图全首rootR3失败；244轨道/24428变量/86597子句模型120秒UNKNOWN、120.171136075CPU。主1088始终0。'
q8['lesson_and_restart_condition'] = '区分缺某一类路线与共同实现：修复全部半周或全部反极点仍未给全D3。固定pi与冻结14406域停止；cyclic域和全cross-pencil域UNKNOWN仍开放，不自动续timer/seed。任何后续须改变具体连接规则或给出能减少不确定性的路线条件，不以少量root覆盖增加续算。'
q8['unclosed_gap'] = '一般8Q3+maxdegree5/D3辅助图仍开放；完整cross-pencil域与cyclic-deck域均UNKNOWN，不宣称不存在或已生成1088。无新跨模型审阅回执，不声称本轮Gemini通过。'
q8['other_metrics'].update(cyclic_fixed_pi_family_excluded=True, cyclic_halfturn_candidates=14406,
                         cyclic_halfturn_root0_failures=14406, cyclic_orbit_solver_status='UNKNOWN',
                         cyclic_orbit_variables=244, cyclic_orbit_all_variables=24428,
                         cyclic_orbit_clauses=86597, cyclic_orbit_solver_calls=1,
                         cyclic_orbit_CPU_seconds=orbit['aggregate_CPU_seconds'], actual_main_graphs=0,
                         all_numerical_jobs_terminal=True, new_cross_model_review_receipt_recorded=False)
extend(q8, q8_variants, q8_paths)

kernel_variant = dict(label='current51457_fixed38_complete_closedB1_strong_proxy_kernel_20261029',
    status=kernel['status'], source_n=51457, source_m=324863,
    certificate='P=N_current(v) minus unique saturated neighbor f; N_current(f) subset closedB1(P union A), with actual free P and |A|<=13-|P|.',
    frozen_prototypes=38, visited=38, unattempted=0, reused_proved_no=1, zero_support=6,
    exact_DP_no_within_actual_budget=31, CPU_seconds=0.290099301,
    current_new_neighbors_retained_for_prototypes=[50589, 50627],
    new_graphs=0, graph_BFS_runs=0, solver_calls=0,
    scope_excluded='Only this strong one-step proxy certificate on the frozen38 actual current neighborhoods and budgets.',
    actual_R4_model_excluded=False, numerical_job_terminal=True)
d13 = rows[d13_id]
d13['lesson_and_restart_condition'] += '；20261029当前51457的38个still-free项完整强proxy kernel已全部阴性：6零支持、31实际预算DP无解、1复用旧强下界；只闭N(f)⊆closedB1(P∪A)证书，不排一般R4。'
d13['other_metrics'].update(current_fixed38_strong_proxy_complete=True,
                            current_fixed38_strong_proxy_hits=0,
                            current_fixed38_actual_R4_excluded=False)
extend(d13, [kernel_variant], kernel_paths)
v4580 = rows[v4580_id]
v4580['failure_or_result'] += '；后续38池强proxy kernel中v4580只复用已证明至少5guards的强证书下界，未重跑该单例DP；完整R4仍UNKNOWN。'
extend(v4580, [dict(label='fixed38_pool_v4580_reuse_20261029',
                   status='REUSED_PROVED_STRONG_LOWER_BOUND_EXCEEDS_BUDGET',
                   available_guard_budget=4, strong_guard_lower_bound=5,
                   new_v4580_DP_runs=0, actual_R4_model_excluded=False,
                   related_existing_experiment='exp:' + d13_id)], kernel_paths)

report = '''# q8循环辅助图与当前D13强代理检验

本轮已完成，目标新图0，主1088未生成；数学合法实例104/4、confirmed主表103/3、具体公式图Lean1保持。

固定pi_twist的反极点覆盖预测得到一个具体64点图支持，但该图仍漏同标签phase4。完整441项和集表配合全部短字分类表明：若全部反极点可达，则每个同标签半周不可达。因此这一固定pi、全部Z8电压范围已停止；没有枚举delta图，也没有外推其它pi。

为新增三步闭字而改pi为(013)(457)(26)，令三个闭环电压均为4，半周路线预测确实支持，首候选还覆盖全部同标签phase。但完整冻结的14406个合法5regular辅助图仍全部首rootR3失败，停止该规则域。

随后不再预选pi，而对完整cyclic-deck-invariant额外2factor联合编码：244无向边轨道、24428总变量、86597子句，保留每label60个邻居出现次数。唯一120秒调用UNKNOWN，120.171136075CPU，无候选；该对称域及一般辅助图均未排除。没有新的跨模型审阅回执，不声明Gemini通过。

D13 actual51457剩余38个原mandatory仍free的prototype，当前P采用实际全邻接，完整强证书kernel得到6零支持、31实际预算DP无解、1旧强下界复用；合38、0.290099301CPU、0构图/graph BFS/solver。只排N(f)⊆closedB1(P∪A)强规则，不排真正R4覆盖；v4580 SAT和LP仍UNKNOWN。

用户本次先要专家交付。现有expert_review_current/EXPERT_HANDOFF_20261029.md正在按上述终态更新，旧稿“尚未完成闭字分析”等表述将由root修订。交付整理不是新增数学成果；旧D2继续暂停，不重导Wiki或创建第二计划。
'''
report_path = HERE / 'Q8_CYCLIC_D13_KERNEL_WIKI_REPORT.md'
report_path.write_text(screen(report))
for row in rows.values():
    extend(row, [], [rel(report_path)])
    screen(json.dumps(row, ensure_ascii=False))
    assert all((ROOT / path).exists() for path in row['report_paths'])
pending = HERE / 'Q8_CYCLIC_D13_KERNEL_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

marker = '<!-- Q8_CYCLIC_D13_KERNEL_EXPERT_HANDOFF_20261029 -->'
comment = '''
## 本轮循环辅助与强代理终态及专家交付更新

用户本次原话：“现在先帮我写一个可以给专家看的交付文档看看，给专家看看要怎么分析”。现有专家稿仍为[EXPERT_HANDOFF_20261029.md](../expert_review_current/EXPERT_HANDOFF_20261029.md)，正在修订并补齐最新源码和证据；不新增第二套研究计划。

以下是执行结果记录：固定q8 pi_twist全部delta由441和集证书与短字分类排除；改三循环闭环电压4确实补半周，但14406项完整冻结域全失败；244轨道/24428变量/86597子句模型唯一120秒UNKNOWN，主1088未生成。D13当前51457的38项强proxy kernel完整阴性，6零支持/31实际预算DP/1复用，未排一般R4。所有数值终态，不自动续timer或已闭电压域。新q8跨模审阅回执未记录，不宣称通过。

数学计数104/4、confirmed103/3、具体公式图Lean1不变。旧D2继续暂停，材料整理不算新图、方法或Goal完成。账本仍371条来源/实验/变体记录。[本轮证据汇总](../research/ddp/refresh_20261029/Q8_CYCLIC_D13_KERNEL_WIKI_REPORT.md)。
'''
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if marker not in comments.read_text():
    with comments.open('a') as output:
        output.write('\n\n' + marker + '\n' + screen(comment))
with (HERE / 'Q8_CYCLIC_D13_KERNEL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded terminal q8 cyclic variants and fixed38 current51457 strong proxy kernel; updated existing three experiments only; expert handoff revision requested; no new target graph or claim.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert len(after['rows']) == after['record_count'] == 371
assert {r['id'] for r in before['rows']} == {r['id'] for r in after['rows']}
for field in ['confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs',
              'validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_INCREMENTAL_EXISTING_THREE_RECORDS', updated_UTC=NOW,
               record_count_before=371, record_count_after=371,
               updated_existing_ids=list(rows), new_experiments=0, new_claims=0,
               valid_graph_examples=104, valid_parameter_pairs=4,
               confirmed_graph_examples=103, confirmed_parameter_pairs=3,
               complete_Lean_instances=1, new_target_graphs=0, main1088_graphs=0,
               fixed_pi_family_excluded=True, halfturn_frozen_candidates=14406,
               cyclic_orbit_solver_result='UNKNOWN', fixed38_strong_kernel_result='NO_HIT',
               actual_R4_excluded=False, new_cross_model_review_receipt_recorded=False,
               command=command, helper_stdout=result.stdout.strip(),
               query_rebuild='aris_repo/tools/research_wiki.py:rebuild_query_pack(research-wiki)',
               research_jobs_rerun=0,
               changed_wiki_paths=['research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md',
                    *[records[key]['wiki_path'] for key in rows], 'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md',
                    'research-wiki/index.md', 'research-wiki/query_pack.md', 'research-wiki/log.md'])
receipt_path = HERE / 'Q8_CYCLIC_D13_KERNEL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=rel(receipt_path), record_count=371,
                      updated_existing_records=3, new_target_graphs=0), ensure_ascii=False))
