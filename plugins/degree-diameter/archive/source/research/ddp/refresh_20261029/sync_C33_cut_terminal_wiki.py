"""Synchronize the single completed capacity-cut model without expanding scope."""
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


def load(name):
    return json.loads((HERE / 'controller33_capacity_cuts' / name).read_text())


result = load('RESULT.json')
model = load('MODEL.json')
assert result['status'] == 'UNKNOWN' and result['solver_calls'] == 1
assert result['running'] is False and result['valid_controllers'] == result['complete4125_graphs'] == 0
assert (model['all_variables'], model['clauses']) == (65890, 194694)
assert result['aggregate_CPU_seconds'] < result['total_CPU_budget'] == 90
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 372
identifier = 'ddp-wave2-triangle-factor33-controller'
old = next(r for r in before['rows'] if r['id'] == identifier)
row = copy.deepcopy(old['source_record'])
variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
variant_label = 'complete_common_NB3_model_with_local_capacity_cuts_20261029'
variants[variant_label] = dict(
    label=variant_label, status='UNKNOWN_TERMINAL',
    controller_order=33, fixed_triangle_blocks=11,
    scope='Full simple external2factor domain with the inherited canonical labeling and prescribed exact NB3 migration condition; necessary local capacity cuts retain every valid solution.',
    extra_edge_variables=495, all_variables=65890, clauses=194694,
    inherited_canonical_variables=31845, inherited_canonical_clauses=109466,
    forbidden_nonmatching_triples=model['forbidden_nonmatching_triples'],
    exact_m3_flags=model['exact_m3_flags'],
    pair_conjunction_terms=model['pair_conjunction_terms'],
    weighted_occurrences_per_vertex=model['weighted_occurrences_per_vertex'],
    weighted_bound_per_vertex=3,
    cuts=['Atmost3 extra edges per triangle-block pair; if3, they are a perfect matching.',
          'Blockpairs with3 extra edges form a matching.',
          'Exact pair conjunctions and repeated literals encode weighted lower bound L(v)<=3.'],
    encoding='Bidirectional definitions for pair conjunctions and m3 flags; repeated input literals retain their weight.',
    static_code_review='PASS reported by the assigned degree5 reviewer; not an external review or formalization.',
    solver_calls=1, solver_option='-t60', solver_exit_code=result['solver_exit_code'],
    solver_CPU_seconds=result['child_CPU_seconds'],
    preparation_CPU_seconds=result['preparation_CPU_seconds'],
    aggregate_CPU_seconds=result['aggregate_CPU_seconds'],
    aggregate_CPU_budget=90, valid_controllers=0, complete4125_graphs=0,
    running=False, continued_timer=False, restart_authorized=False,
    general33_family_excluded=False, performance_improvement_proven=False,
    combined_external_review_status='PENDING')
local = variants['local_triangle_fourcycle_and_weighted_pair_NB3_capacity_20261029']
local['later_full_cut_model_dispatch_recorded'] = True
local['later_full_cut_model_terminal_status'] = 'UNKNOWN'
local['later_full_cut_model_variant'] = variant_label
c11 = variants['C11_simultaneous_triangle_block_translation_complete_NB3_gate_20261029']
c11['paper_derivation_excludes_entire_defined_C11_domain'] = True
c11['same_family_static_attack'] = 'PASS; phase multisets, both moments and loop capacity checked in the mathematical static attack.'
row['variants'] = list(variants.values())
row['scope'] = row['scope'].replace(
    '尚不把后续完整cut模型派发冒已运行。',
    '完整cut模型现已单次终态UNKNOWN，保留一般非对称外边自由域。')
if '；局部容量cut完整模型65890/194694' not in row['failure_or_result']:
    row['failure_or_result'] += '；局部容量cut完整模型65890/194694，唯一-t60为UNKNOWN，child60.007625CPU、prep0.288120746、aggregate60.31161875CPU，0控制器/0提升，已停。'
row['unclosed_gap'] = '一般非对称33固定三角因子控制器仍开放；原始90秒、规范90秒及新增容量cut60秒完整模型均UNKNOWN，均无控制器或4125图，不续timer。C11整域有枚举与纸面矩排除，但只针对规定NB3迁移规则，不是普通D3或所有F5图不可能。联合Gemini外审仍pending；新必要cut不构成性能证据。'
row['other_metrics'].update(
    current_complete_model_status='UNKNOWN_CAPACITY_CUTS_TERMINAL',
    current_complete_model_running=False, later_full_cut_model_run_recorded=True,
    local_capacity_cut_all_variables=65890, local_capacity_cut_clauses=194694,
    local_capacity_cut_solver_calls=1,
    local_capacity_cut_solver_CPU_seconds=result['child_CPU_seconds'],
    local_capacity_cut_total_CPU_seconds=result['aggregate_CPU_seconds'],
    local_capacity_cut_valid_controllers=0, actual_lift4125_generated=False,
    local_capacity_cut_static_code_review='PASS_PARENT_REPORTED',
    performance_improvement_proven=False,
    combined_C11_capacity_external_review_status='PENDING')

report = '''# C33局部容量cut完整模型单次终态

保留完整495条跨三角边变量域及原规范标号，加入块对至多3边、三边必须matching、三重块对成matching和每点加权L≤3。CNF为65890变量/194694子句。配对AND、m3标志采用双向定义，加权输入保留重复literal；本地静态代码复核通过。此复核不等同外审或形式化。

唯一一次cadical -t60实际返回UNKNOWN，child60.007625CPU、准备0.288120746CPU、总60.31161875CPU，0控制器、0个4125图，已停止。不是原90秒模型续时；原始、规范、cut三个有界模型各自UNKNOWN，不排一般33控制器，不声称cut已加速。

C11的1800合法设置全拒另有共同相位一、二次矩纸面排除，独立静态相位攻击通过。排除范围仍仅C11同时块平移下规定恰三步非回退迁移条件，不是普通D3控制器。联合Gemini仍等待原一次调用，不记通过、不重试。

本次只更新原33family的一行变体，ledger372、104/4、confirmed103/3、Lean1不变。D13全图Aut入口的历史外围绑定缺口仍保留；新外围必要门和改邻域问题未在这里冒充已运行或排除。root最终同步后再做最后query。
'''
report_path = HERE / 'C33_CAPACITY_CUT_TERMINAL_WIKI_REPORT.md'
report_path.write_text(screen(report))
evidence = [
    str(p.relative_to(ROOT))
    for p in sorted((HERE / 'controller33_capacity_cuts').iterdir())
    if p.is_file() and p.suffix in {'.md', '.json', '.py'}
]
row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + evidence
                                       + [str(report_path.relative_to(ROOT))]))
assert all((ROOT / p).exists() for p in row['report_paths'])
screen(json.dumps(row, ensure_ascii=False))
pending = HERE / 'C33_CAPACITY_CUT_TERMINAL_WIKI_ROWS.json'
pending.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- C33_CAPACITY_CUT_TERMINAL_20261029 -->'
note = '''
## 同一C33容量cut完整模型已停止

完整模型65890变量/194694子句唯一-t60终态UNKNOWN，child60.007625CPU、准备0.288120746、总60.31161875CPU，0controller/0提升，不续。新cut双向定义/重复literal加权/三重块matching本地静态核对通过，但不宣称性能获证。此前‘后续cut待回执’现以这个真实终态为准。

C11同时平移域1800设置还具有完整纸面矩排除，范围仅规定NB3迁移规则；联合Gemini原调用仍pending。ledger372及主104/4、confirmed103/3、Lean1均不变。[单次终态与证据](../research/ddp/refresh_20261029/C33_CAPACITY_CUT_TERMINAL_WIKI_REPORT.md)。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:
        out.write('\n\n' + marker + '\n' + screen(note))
with (HERE / 'C33_CAPACITY_CUT_TERMINAL_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Updated existing C33 family with one completed capacity-cut model:65890vars/194694clauses, single60sec UNKNOWN,0controller/lift; C11 paper scope retained, combined review pending; no method or graph count increase.')
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for key in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[key] == after[key]
receipt = dict(
    status='PASS_C33_CAPACITY_CUT_SINGLE_UNKNOWN_RECORDED_PENDING_FINAL',
    updated_UTC=NOW, existing_id=identifier, record_count=372,
    solver_status='UNKNOWN', all_variables=65890, clauses=194694,
    solver_calls=1, child_CPU_seconds=result['child_CPU_seconds'],
    preparation_CPU_seconds=result['preparation_CPU_seconds'],
    aggregate_CPU_seconds=result['aggregate_CPU_seconds'], running=False,
    controllers=0, complete4125_graphs=0, continued_timer=False,
    combined_external_review_status='PENDING',
    new_experiments=0, new_methods=0, new_claims=0, new_graphs=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3,
    complete_Lean_instances=1, final_query_rebuild_after_root_update_pending=True,
    command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'C33_CAPACITY_CUT_TERMINAL_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
                     record_count=372, final_query='WAITING_FOR_ROOT_FINAL'), ensure_ascii=False))
