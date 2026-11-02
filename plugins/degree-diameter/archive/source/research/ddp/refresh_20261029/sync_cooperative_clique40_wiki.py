"""Record the exact provider-chain exclusion on the existing successful D13 family."""
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


directory = HERE / 'd13_D5_cooperative_clique40'
result = json.loads((directory / 'RESULT.json').read_text())
chain = json.loads((directory / 'PROVIDER_ELIMINATION.json').read_text())
assert result['status'] == 'EXACT_FIXED_POOL_EXCLUDED_BY_PROVIDER_CHAIN'
assert result['provider_removed'] == 40 and result['provider_rounds'] == 2
assert result['provider_survivors'] == [] and len(chain['deletion_chain']) == 40
assert result['solver_calls'] == result['new_graphs'] == 0
assert len(chain['rounds']) == 2 and chain['surviving_indices'] == []

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == len(before['rows']) == 372
ident = 'ddp-d13-singlefault-star-family-51457-20261027'
current = next(r for r in before['rows'] if r['id'] == ident)
row = copy.deepcopy(current['source_record'])
variant = dict(label='current40_free_part_clique_cooperation_provider_fixpoint_20261029',
    status=result['status'], source_n=51457, source_m=324863,
    saved_original_neighborhoods=40, fixed_free_parts=40, empty_free_parts=2,
    all_nonempty_helper_clique_subsets_excluded=True, includes_K1=True,
    helpers_attach_to='P_i = current-free members of exact savedS_i; no guards or changedP_i',
    direct_or_cooperative_distance='d(y_i,t)=min(1+d_G(P_i,t),2+min_(j!=i)d_G(P_j,t))',
    condition='EveryR4-gap target of each selectedi needs some selectedR3providerj.',
    provider_rounds=2, round0_removed_count=39, round0_only_survivor=28,
    round0_witness=dict(index=0, original_added_vertex=51417, missing_target=207, original_R3_providers=[]),
    round1_removed_indices=[28],
    round1_witness=dict(index=28, original_added_vertex=51445, missing_target=265,
                        original_R3_providers=[14, 30, 34, 35, 38], all_providers_removed_in_round0=True),
    fixedpoint_survivors=0,
    proof='Inductively any feasible subset must stay in the active pool; deletei with anR4gap target having no activeR3provider. Empty fixedpoint forbids every nonempty subset.',
    degree_and_port_constraints_needed_for_exclusion=False,
    actually_enumerated_subsets=0, source_reads=1, multisource_radius4_runs=40,
    source_diameter_allroot_BFS=0, solver_calls=0, new_graphs=0,
    worker_CPU_seconds=0.088320, aggregate_prepare_compile_CPU_seconds=result['aggregate_cpu_seconds'],
    same_fixed_pool_stopped=True,
    other_neighborhoods_guards_or_general_cooperation_excluded=False)
variants = {v.get('label', v.get('name')): v for v in row.get('variants', [])}
variants[variant['label']] = variant
row['variants'] = list(variants.values())
row['scope'] += '；current40 free-part P_i保持不变、选任意非空subset并令新helpers成clique的完整固定池，由两轮R3provider删除定点为空排除，包括K1，不依赖degree/port约束。'
row['failure_or_result'] += '；新合作P40池实际1source读/40多源R4保存R3/R4，round0删39仅留index28，round1删index28；其target265的原providers14/30/34/35/38已全删。定点空排全部非空subset，0solver/图，0.739728CPU。'
row['lesson_and_restart_condition'] = row['lesson_and_restart_condition'].replace(
    '新free-part clique池尚未在本记录登记数值运行或结果。',
    '后续fixed free-part clique40池已有实际完整provider-chain阴性，停止该池，不按k梯子或选另一subset续算。')
row['lesson_and_restart_condition'] += '；这一失败来自具体缺项没有共同R3provider，不是单纯总缺项评分。若要再改合作规则须引入不同P_i、新邻域/guard或改变连接，不能将固定池排除外推全部合作扩张。'
row['unclosed_gap'] = '完整source构造最大性未证。固定40静态邻域multiplicity max40与current40-free-part全clique-subset池现均严格闭合；不同邻域、额外guard或其它合作连接仍开放。'
row['other_metrics'].update(current40_free_part_clique_numerical_result_recorded=True,
    current40_free_part_clique_status=result['status'],
    current40_free_part_clique_provider_removed=40,
    current40_free_part_clique_provider_rounds=2,
    current40_free_part_clique_all_nonempty_subsets_excluded=True,
    current40_free_part_clique_solver_calls=0)
paths = [str(p.relative_to(ROOT)) for p in sorted(directory.iterdir())
         if p.is_file() and p.suffix in {'.md', '.json', '.jsonl', '.py', '.cpp', '.txt', '.bin'}]
row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))
assert all((ROOT / p).exists() for p in row['report_paths'])
screen(json.dumps(row, ensure_ascii=False))
pending = HERE / 'COOPERATIVE_CLIQUE40_WIKI_ROWS.json'
pending.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)

comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
s = comments.read_text()
s = s.replace('current40 free-part clique合作池待实际RESULT才登记数值，不将准备冒运行。',
    '后续current40 free-part clique合作池已实际provider定点为空排除所有非空subset，见下一节；不再记准备。', 1)
marker = '<!-- COOPERATIVE_CLIQUE40_PROVIDER_CHAIN_COMPLETE_20261029 -->'
note = '''
## current40 free-part clique池实际全域排除

这是执行记录。固定P_i为现有40成功邻域在current51457中的free部分，保持两空集，允许任意非空subset、helper彼此全连并接各自P_i。新旧距离的精确式给出R4缺项须有其它选中P_j的R3provider。round0排39项，仅留index28；round1由其target265的五个原providers已全排再删28，定点为空，故包括K1的全部非空subset严格失败，无subset枚举。

这不依赖degree/port额外限制，不能用加上那些限制恢复解。1source读、40多源R4，0.739728CPU、0solver/新图，当前固定池停止。不排改变P_i、加guard、新邻域或一般合作规则。ledger372及104/4、confirmed103/3、Lean1不变，原v4580真四guard仍UNKNOWN。

用户本次先要专家交付。当前专家快照第五节末关于“未保证40组在原B0独立覆盖”的信息已由新静态40/40、780pair、容量证书补足，需由root在交付修订时更新；本writer只做Wiki与只读附件建议，不改主稿/专家包或root入口。[合作池完整报告](../research/ddp/refresh_20261029/d13_D5_cooperative_clique40/REPORT.md)。最终query等root状态完成。
'''
if marker not in s:
    s += '\n\n' + marker + '\n' + screen(note)
comments.write_text(screen(s))
with (HERE / 'COOPERATIVE_CLIQUE40_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Recorded exact two-round provider-chain exclusion of fixedP40 clique cooperation on existing D13 source family; all nonempty subsets includingK1, zero solver/newgraph; expert artifact reviewed read-only; final query waits for root.')

after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 372
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_COOPERATIVE40_EXISTING_VARIANT_QUERY_PENDING_ROOT',
    updated_UTC=NOW, updated_existing_experiment=ident, record_count=372,
    cooperative_status=result['status'], provider_rounds=2, round0_removed=39,
    round1_removed_index=28, fixedpoint_survivors=0,
    all_nonempty_fixed_pool_clique_subsets_excluded=True,
    actually_enumerated_subsets=0, solver_calls=0, new_graphs=0,
    aggregate_CPU_seconds=result['aggregate_cpu_seconds'],
    different_P_or_guards_or_general_cooperation_excluded=False,
    new_experiments=0, new_methods=0, new_claims=0,
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    expert_handoff_and_builder_modified=False, root_state_modified=False,
    final_query_rebuild_after_root_update_pending=True, command=command, helper_stdout=run.stdout.strip())
receipt_path = HERE / 'COOPERATIVE_CLIQUE40_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=372, solver_calls=0, final_query='WAITING_FOR_ROOT'), ensure_ascii=False))
