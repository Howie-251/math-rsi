"""Attach one completed literal-controller gate to the existing F5 route-chart record."""
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
gate_dir = HERE / 'controller41_transfer_gate'
gate = json.loads((gate_dir / 'RESULT.json').read_text())
assert gate['status'] == 'REJECTED_AT_FIRST_TRIANGLE_FREE_VERTEX'
assert gate['first_failure'] == 1 and gate['checked_prefix'][-1]['neighbor_edges'] == []
assert gate['checked_prefix'][-1]['neighbors'] == [0, 3, 4, 5]
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count'] == 371
ident = 'ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029'
current = next(r for r in before['rows'] if r['id'] == ident)
row = copy.deepcopy(current['source_record'])
variant = dict(label='allwright41_fixed_affine_line_controller_triangle_obstruction_20261029',
    status=gate['status'], object_level='literal_known_controller_gate',
    source='research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges',
    source_order=41, source_edges=82, source_degree=4, inherited_source_diameter=3,
    source_credit='Allwright Graph1(a), Comellas-maintained literal adjacency.',
    vertices_checked=2, first_triangle_free_vertex=1, neighbors=[0, 3, 4, 5],
    edges_inside_neighbor_set=[],
    reasoning='At a triangle-free controller vertex there is no3-step return; the four2-step edge/reverse returns in this affine-line rule cover at most1+4(q-1) fiber points.',
    self_fiber_capacity_F5=dict(upper_bound=17, required=125),
    self_fiber_capacity_F4=dict(upper_bound=13, required=64),
    proposed_lifts=[dict(field='F5', order=5125, degree_bound=20, D_target=3),
                    dict(field='F4', order=2624, degree_bound=16, D_target=3)],
    nb3_ordered_pairs_checked=0, bfs_runs=0, lift_graphs_generated=0,
    other_controllers_checked=0, CPU_seconds=gate['cpu_seconds'],
    excluded_scope='This literal41 controller with the proposed q-point affine-line relation onFq^3 fibers.',
    not_excluded=['Other41-vertex controllers', 'Other fiber relations'],
    old_C9_ordinary_cover_scope_is_different=True,
    stopped_after_first_obstruction=True)
variants = {v['label']: v for v in row.get('variants', [])}
variants[variant['label']] = variant
row['variants'] = list(variants.values())
row['lesson_and_restart_condition'] += '；Allwright literal41作为同类仿射线controller的迁移在顶点1无triangle处被self-fiber短路容量17<125(F5)/13<64(F4)阻断；停止这个实际source，不续NB3、改邻接或其它controller。此域不同于旧C9普通覆盖，不混作旧排除。'
paths = [str(p.relative_to(ROOT)) for p in sorted(gate_dir.iterdir())
         if p.is_file() and p.suffix in {'.md', '.json', '.py'}]
paths.append('research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges')
row['report_paths'] = list(dict.fromkeys(row.get('report_paths', []) + paths))
assert all((ROOT / p).exists() for p in row['report_paths'])
assert not capture.screen(json.dumps(row, ensure_ascii=False))
pending = HERE / 'CONTROLLER41_GATE_WIKI_ROWS.json'
pending.write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'), str(pending)]
result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
marker = '<!-- ALLWRIGHT41_AFFINE_LINE_GATE_TERMINAL_20261029 -->'
comment = '''
## 一个41点控制器迁移的必要路线门

这是执行记录。复用Allwright Graph1(a)的literal41/82源及其既存四正则/D3证据，不重复BFS。按序只检查顶点0、1；顶点1的四邻点{0,3,4,5}内无边，故该控制器顶点无triangle。同fiber至多3步仅有四条edge/reverse回退线，最多1+4(q−1)，F5为17<125、F4为13<64，排除此实际source的仿射线提升规则。CPU0.000321952，0NB3/新图/BFS/solver/其它controller。

这不同于旧C9普通覆盖排除，不混成同一旧结论，不据此排其它41点图或其它纤维关系。仅在现有F5/routechart实验加变体，账本仍371；q8已有审阅与独立mod4核对的最终PASS保持，104/4、confirmed103/3、Lean1及一般非循环辅助图开放不变。[来源与见证](../research/ddp/refresh_20261029/controller41_transfer_gate/REPORT.md)。
'''
comments = WIKI / 'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if marker not in comments.read_text():
    assert not capture.screen(comment)
    with comments.open('a') as output:
        output.write('\n\n' + marker + '\n' + comment)
with (HERE / 'CONTROLLER41_GATE_WIKI_HELPER.log').open('w') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Appended literal Allwright41 affine-line controller triangle obstruction to existing F5 route-chart experiment; no new method, graph or claim; final query rebuild remains pending root state update.')
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 371
q8 = next(r for r in after['rows'] if r['id'] == 'ddp-q8-k64-cube-external2factor-13d3-20261029')
assert q8['other_metrics']['new_cross_model_review_status'] == 'SUCCESS_SUPPORT'
assert q8['other_metrics']['independent_mod4_verification_status'] == 'PASS_COMPLETE_COUNTS_MATCH'
for field in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
              'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[field] == after[field]
receipt = dict(status='PASS_CONTROLLER41_EXISTING_VARIANT_QUERY_PENDING_ROOT', updated_UTC=NOW,
    updated_existing_id=ident, record_count=371, first_failure_vertex=1,
    source_gate_status=gate['status'], new_methods=0, new_claims=0, new_graphs=0,
    source_BFS_rerun=0, NB3_checks=0, other_controllers=0,
    q8_final_review_preserved='SUCCESS_SUPPORT', q8_final_independent_mod4_preserved='PASS_COMPLETE_COUNTS_MATCH',
    valid_examples=104, valid_pairs=4, confirmed_examples=103, confirmed_pairs=3, complete_Lean_instances=1,
    command=command, helper_stdout=result.stdout.strip(), final_query_rebuild_after_root_update_pending=True)
receipt_path = HERE / 'CONTROLLER41_GATE_WIKI_RECEIPT.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
final_receipt_path = HERE / 'Q8_REGULAR_CYCLIC_FINAL_WIKI_RECEIPT.json'
final = json.loads(final_receipt_path.read_text())
final.update(controller41_gate_status=gate['status'], controller41_wiki_receipt=str(receipt_path.relative_to(ROOT)),
    updated_existing_ids=['ddp-q8-k64-cube-external2factor-13d3-20261029',
                          'ddp-d13-v4580-current51457-fourguard-unknown-20261029', ident])
final_receipt_path.write_text(json.dumps(final, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], receipt=str(receipt_path.relative_to(ROOT)),
    record_count=371, q8_review='SUCCESS_SUPPORT', final_query='WAITING_FOR_ROOT_UPDATED'), ensure_ascii=False))
