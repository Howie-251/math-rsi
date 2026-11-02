"""Incrementally record the completed symmetry and exact-route batch."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def load(folder, name='RESULT.json'):
    return json.loads((HERE / folder / name).read_text())


def evidence(folder):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / folder).rglob('*'))
            if p.is_file() and p.suffix in {'.md', '.json', '.py', '.cpp'}
            and '__pycache__' not in p.parts]


def append_variant(row, variant):
    variants = row.setdefault('variants', [])
    variants[:] = [v for v in variants if v.get('label') != variant['label']]
    variants.append(variant)


translation = load('d15_translation_symmetry_gate')
certificate = load('k5_q16_NB4_quotient_gate')
provider = load('k5_actual_route_provider_gate')
actual = load('k5_q16_actual_R4', 'TERMINAL.json')
calibration = load('k5_q16_actual_R4', 'CALIBRATION.json')
prefix = ROOT / 'reviews/ddp/controller33_no_external_triangle_20261030'
review = json.loads(prefix.with_suffix('.response.json').read_text())['structuredContent']
assert (review['status'], review['model'], review['effort']) == (
    'SUCCESS', 'gemini-3.8-flash-high', 'high')
assert (translation['rank'], translation['unknowns'], translation['kernel_dimension']) == (768, 768, 0)
assert translation['running'] is False and translation['pending'] == []
assert (certificate['complete_projection_assignments'], certificate['passed_assignments']) == (4096, 0)
assert (provider['tested'], provider['passed'], provider['remaining_Q16_full_assignments']) == (4096, 30, 122880)
assert actual['status'] == 'COMPLETE_NO_FULL_GRAPH'
assert actual['fully_decided_lifts'] == actual['actual_lift_scope'] == 122880
assert actual['root0_pass_candidates'] == 0
assert actual['root0_failed_base_counts'] == [122880, 0, 0, 0, 0]
assert actual['running'] is False and actual['pending'] == []
assert actual['old_full_NB4_gate_used'] is False
assert calibration['pointwise_matches'] == 6480
assert calibration['cache_R4_size'] == calibration['literal_R4_size'] == 4563

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
existing = {r['id']: r for r in before['rows']}
assert before['record_count'] == len(existing) and before['record_count'] in {377, 378}
id15 = 'ddp-d15-d4-literal15552-all648-k2-cooperative-cover-20261030'
id33 = 'ddp-wave2-triangle-factor33-controller'
id12 = 'ddp-k5-q16-f3four-actual-r4-voltage-route-gates-12d4-20261030'
new_records = int(id12 not in existing)
rows = []

d15 = copy.deepcopy(existing[id15]['source_record'])
append_variant(d15, dict(
    label='full_synchronous_fiber_translation_kernel_gate_20261030',
    status=translation['status'],
    scope='Only source-preserving simultaneous fiber translations x_c -> x_c+t_c for the literal 192-controller linear recipe; not all automorphisms.',
    equations=2880, unknowns=768, rank=768, kernel_dimension=0,
    translation_group_order=1, all_960_arcs_checked=True,
    deleted_virtual_loops_preserved=True, literal_free_ports=648,
    free_port_orbits=648, freeport_transitive=False,
    K2_single_anchor_reduction_justified=False,
    CPU_seconds=translation['CPU_seconds'], source_graph_reads=0,
    BFS_runs=0, solver_calls=0, graph_exports=0, running=False,
    all_Aut_excluded=False, K2_family_excluded=False,
    result='research/ddp/refresh_20261029/d15_translation_symmetry_gate/RESULT.json'))
d15['other_metrics']['synchronous_fiber_translation_kernel_dimension'] = 0
d15['other_metrics']['translation_based_K2_anchor_reduction_supported'] = False
d15['other_metrics']['all_source_automorphisms_excluded'] = False
d15['failure_or_result'] += '；完整同步fiber平移方程2880×768满秩768，核0、群仅identity，648个freeport各自成轨道，0.671092911CPU。该候选自同构不能提供固定单anchor的无损K2归约；未检验/排除全部Aut，原完整K2仍UNKNOWN。'
d15['lesson_and_restart_condition'] += '；同步平移入口经完整线性方程门已停止，不据此假设独立fiber平移或强加A0；其它实际自同构若要归约仍须给出作用和保全依据。'
d15['report_paths'] = list(dict.fromkeys(d15['report_paths'] + evidence('d15_translation_symmetry_gate')))
rows.append(d15)

c33 = copy.deepcopy(existing[id33]['source_record'])
review_meta = dict(status='SUCCESS_SOUND_AS_STATED', actual_model=review['model'],
    effort=review['effort'], thread_id=review['threadId'],
    scope='Simple C33 = designated 11K3 I plus edge-disjoint cross-block simple 2factor F; diameter<=3 implies F has no triangle component. Hence also necessary for common exact NB3.',
    code_or_solver_or_BFS_or_Lean_run_by_review=False,
    general_triangle_free_C33_excluded=False,
    response=str(prefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition=str(prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
append_variant(c33, dict(
    label='external_2factor_triangle_component_paper_obstruction_20261030',
    status='PAPER_NECESSARY_F_TRIANGLE_FREE_ACTUAL_STATIC_REVIEW_SUPPORTED',
    scope=review_meta['scope'],
    proof='An F-triangle root needs the 33-point B3 capacity bound to be tight. Each of its three I-blocks must send four F edges to distinct outside I-blocks; the three four-block sets must be disjoint, requiring 12 outside blocks but only 8 exist.',
    intermediate_triangle_component_limit=3,
    final_F_triangle_components_allowed=0,
    double_triangle_linegraph_bound_is_published_not_new=True,
    designated_double_triangle_controller_order_at_most=21,
    actual_external_review=review_meta,
    saved_best_F_cycle_lengths=[24, 5, 4],
    saved_best_still_missing_ordered_NB3_pairs=28,
    saved_best_repaired=False, performance_improvement_proven=False,
    numerical_enumerations=0, solver_calls=0, BFS_runs=0,
    new_controllers=0, new_large_graphs=0, Lean_instances=0,
    automatic_old_solver_continuation=False))
c33['other_metrics'].update(F_triangle_components_allowed_by_necessary_lemma=0,
    F_triangle_free_proof_review=review_meta,
    general33_family_excluded=False,
    saved_best_repaired_by_new_lemma=False)
c33['scope'] += '；同一指定11K3+跨块简单2factor模型中，普通D3即迫F不含三角分量；因此共同NB3模型可以无损禁止F三角，仍保留所有F圈长≥4。'
c33['failure_or_result'] += '；新纸面路线容量取等与三个根的外部I块集合计数给12>8矛盾，排任何F三角分量；实际Gemini SUCCESS/SOUND AS STATED。双三角线图界另属已发表成果。保存best的F=24+5+4本来无三角，28个NB3有序缺项未修复；0新枚举/solver/BFS/控制器/提升/Lean。'
c33['lesson_and_restart_condition'] += '；今后生成可无损只保留F圈长≥4；该新禁形没有修复旧best或证明加速，本轮不追加旧solver时间。'
c33['unclosed_gap'] += '；一般无三角F的C33仍开放。新定理已获真实静态外审，未Lean，也不说明4125点图存在。'
c33['report_paths'] = list(dict.fromkeys(c33['report_paths'] + evidence('controller33_second_triangle_factor') +
    [str(prefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md', '.response.json', '.DISPOSITION.md']]))
rows.append(c33)

k5 = dict(
    id=id12, title='K5/Q16/F3^4真实短路线：NB4证书失败后保全商门30项，完整电压域全部排除',
    family='four-label affine route-chart lifts', idea_family='idea:ddp-breadth-20261027',
    date='2026-10-30', record_type='fixed-new-controller-group-chart-complete-voltage-route-gates',
    target_Delta=12, target_D=4, savedL=6156, baseline_date='2026-10-26',
    savedL_source='context/DD_PORTFOLIO_START_20261026/registry/cases.json',
    n=dict(actual=6480, hypothetical=6480), actual_graph_Delta=12,
    actual_D=None, actual_D_scope='One calibration graph is simple12regular; root0 R4=4563/6480, so D>4. Global diameter not computed. The complete voltage domain is excluded using exact route caches, not full graph enumeration.',
    ordinary_bad_unordered_pairs=None,
    outcome_class='COMPLETE_FIXED_K5_Q16_CHART_ACTUAL_D4_VOLTAGE_FAMILY_EXCLUDED',
    scope='Fixed K5 porting from two oriented complementary C5s, inverse ports [1,0,3,2], stored F3^4 four-chart/noise input. Ordinary right Q16 voltages on all ten K5 edges; star-tree gauge fixes four edges to identity and leaves six independent chords. Whole 16^6=16777216 voltage domain covered by 4066 rejected V4 projections plus 30*4096 full-Q16 assignments. Not other groups, chart sets, bases, nonordinary lifts, or general N(12,4).',
    failure_or_result='The sufficient exact-NB4 V4 gate tested4096/failed4096 in0.043517287CPU, which alone did not exclude actual D4. A distinct necessary actual-route provider gate includes all341 words of length0..4 and their true field images, merges only equal signed deck-word keys, and retains30/4096 in0.647435435CPU. The one full actual-Q16 call then decides all122880 lifts: every assignment fails the zero-root own-base field/deck slot,0root0-pass candidates,0main-enumeration graphs/BFS. Native0.058621CPU, child0.059756CPU, total charged2.157211698CPU including preparation and both gates. One separately recorded calibration graph6480/38880 is simple12regular; literal BFS root0 and exact cache agree pointwise6480entries, R4=4563, first missing162. Fixed actual-D4 family stopped.',
    positive_guarantees=[
        'All 108 reduced four-port words of the stored F3^4 chart are rank4; this is a binding for a sufficient certificate, not the actual D4 gate.',
        'Tree gauge is a deck relabeling and preserves the field graph; all six chord values remain independent.',
        'Actual-route filtering uses all length0..4 raw words, including backtracking field noise; only signed deck words are freely reduced.',
        'A field coordinate needs four distinct deck targets in each V4 coset, so fewer than four provider keys is necessary failure, not a sufficient success test.',
        'The actual full search does not reuse the failed full-NB4 gate as an actual-graph filter.'],
    other_metrics=dict(
        complete_tree_gauge_assignments=16777216, inverse_ports=[1,0,3,2],
        group='Q16', quotient='V4', star_identity_edges=4, free_chords=6,
        exact_NB4_projection_count=4096, exact_NB4_projection_passes=0,
        exact_NB4_gate_CPU_seconds=certificate['CPU_seconds'],
        exact_NB4_gate_excludes_actual_D4_alone=False,
        actual_provider_projection_count=4096, actual_provider_passes=30,
        actual_provider_failures=4066, actual_words_per_base_root=341,
        actual_merged_keys_per_root=161, actual_provider_CPU_seconds=provider['CPU_seconds'],
        actual_full_lifts=122880, fully_decided_lifts=122880,
        root0_pass_candidates=0, root0_failed_base_counts=[122880,0,0,0,0],
        main_numeric_calls=1, main_driver_pid=actual['driver_pid'], main_child_pid=actual['child_pid'],
        child_CPU_seconds=actual['child_CPU_seconds'], whole_CPU_seconds=actual['whole_CPU_seconds'],
        native_CPU_seconds=actual['native_CPU_seconds'], whole_CPU_budget=90,
        main_enumeration_graphs_generated=0, main_enumeration_BFS_runs=0,
        calibration_graphs_generated=1, calibration_BFS_roots=1,
        calibration_n=6480, calibration_m=38880, calibration_simple=True,
        calibration_degree=12, calibration_R4=4563, calibration_first_missing=162,
        calibration_cache_literal_pointwise_matches=6480,
        actual_D4_lift_family_excluded=True, current_running=False, pending=[],
        accepted_graphs=0, new_record=False, new_independent_method_claimed=False),
    variants=[
        dict(label='D16_inverse_orbit_capacity_paper_cancel_before_numeric_20261030',
             status='EXACT_NB4_CERTIFICATE_PAPER_EXCLUDED_NO_NUMERIC',
             reason='K5 has24 closed NB4 words,12 reversal pairs; D16 requires13 inverse orbits.',
             actual_D4_lift_excluded=False, numerical_calls=0),
        dict(label='Q16_all4096_V4_exact_NB4_sufficient_certificate_gate_20261030',
             status=certificate['status'], prediction='At least one projection passes',
             prediction_result='REFUTED', tested=4096, passed=0,
             diagonal_identity_coset_threshold=6, other_threshold=4,
             CPU_seconds=certificate['CPU_seconds'], actual_D4_family_excluded=False,
             graphs_generated=0, BFS_runs=0, solver_calls=0),
        dict(label='Q16_all4096_V4_actual_short_route_provider_necessary_gate_20261030',
             status=provider['status'], prediction='Short/backtracking route union can survive even though the stronger NB4 certificate fails',
             prediction_result='SUPPORTED', tested=4096, passed=30, failed=4066,
             words0through4=341, keys_per_root=161, remaining_full_assignments=122880,
             CPU_seconds=provider['CPU_seconds'], graphs_generated=0, BFS_runs=0,
             actual_D4_family_excluded_by_this_gate_alone=False),
        dict(label='Q16_literal6480_graph_one_root_cache_calibration_20261030',
             status='PASS_EXACT_CACHE_BINDING_ACTUAL_GRAPH_R4_FAIL',
             n=6480, m=38880, simple=True, degree=12, root=0,
             literal_R4=4563, cache_R4=4563, pointwise_matches=6480,
             first_missing=162, actual_graphs_generated=1, BFS_roots=1,
             global_diameter_computed=False, ordinary_bad_unordered_pairs=None),
        dict(label='Q16_all122880_surviving_voltage_assignments_actual_R4_complete_20261030',
             status=actual['status'], tested=122880, untested=0,
             root0_pass_candidates=0, root0_own_base_failures=122880,
             actual_numeric_calls=1, native_CPU_seconds=actual['native_CPU_seconds'],
             child_CPU_seconds=actual['child_CPU_seconds'],
             whole_CPU_seconds=actual['whole_CPU_seconds'],
             old_full_NB4_gate_used=False, graph_generations=0, BFS_roots=0,
             solver_calls=0, running=False, pending=[], actual_fixed_D4_family_excluded=True)],
    lesson_and_restart_condition='The stronger full-NB4 certificate was too restrictive to infer actual impossibility: true short-route provider filtering left30 projections. The complete retained domain still fails specifically at the zero-root own-base target coverage; this precise common-voltage rule is now closed. Stop this fixed K5/Q16/chart family without group,seed,chart or timer ladder. Any future rule needs a real structural change and explicit new coverage justification.',
    unclosed_gap='No accepted6480(12,4) graph. General N(12,4), other groups/base/chart/voltage constructions remain open; this result is a finite exact fixed-rule exclusion, not a general bound or Lean theorem.',
    report_paths=evidence('k5_q16_NB4_quotient_gate') + evidence('k5_actual_route_provider_gate') + evidence('k5_q16_actual_R4'),
    hardware_raw='Single worker; one finite native common-voltage search; no solver.',
    duration_raw='ExactNB4 .043517287CPU; actualprovider .647435435CPU; all preparation+gates+actual call charged whole2.157211698CPU.')
rows.append(k5)

spec = importlib.util.spec_from_file_location('capture_filter', ROOT / 'aris_repo/tools/capture_filter.py')
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)
for row in rows:
    assert all((ROOT / p).exists() for p in row['report_paths'])
    assert not capture.screen(json.dumps(row, ensure_ascii=False))

raw_path = HERE / 'SYMMETRY_REAL_ROUTE_WIKI_ROWS.json'
raw_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
run = subprocess.run([sys.executable, str(ROOT / 'research/ddp/more_graphs_20261027/sync_additional_probes.py'),
                      str(raw_path)], cwd=ROOT, text=True, capture_output=True, check=True)
after = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == before['record_count'] + new_records == 378
for key in ['validated_graph_examples_including_novelty_pending', 'validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples', 'confirmed_publictable_improved_parameter_pairs', 'complete_Lean_graph_instances']:
    assert before[key] == after[key]
gap_path = WIKI / 'gap_map.md'
gap = gap_path.read_text()
gap = gap.replace('账本现377条实验／来源记录', '账本现378条实验／来源记录', 1)
gap_path.write_text(gap)
receipt = dict(status='PASS_SYMMETRY_AND_REAL_ROUTE_TERMINALS_SYNCED_PENDING_ROOT_FINAL_QUERY',
    updated_UTC=NOW, record_count=378, records_updated=[id15, id33, id12],
    new_experiment_records=new_records, new_independent_methods_claimed=0,
    D15_translation_kernel_dimension=0, D15_all_Aut_excluded=False,
    C33_no_external_triangle_review=review_meta,
    K5_exact_NB4_projection_passes=0, K5_actual_provider_projection_passes=30,
    K5_actual_full_assignments_decided=122880, K5_actual_full_status=actual['status'],
    K5_actual_fixed_D4_family_excluded=True, K5_calibration_failed_graphs=1,
    new_accepted_graphs=0, valid_examples=104, valid_pairs=4,
    confirmed_examples=103, confirmed_pairs=3, Lean_instances=1,
    D2_paused=True, expert_snapshot_UTC='2026-10-30 02:02 UTC',
    root_documents_changed=False, expert_package_changed=False,
    final_query_after_root_update_pending=True, helper_stdout=run.stdout.strip())
out = HERE / 'SYMMETRY_REAL_ROUTE_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=receipt['status'], record_count=378,
    new_experiment_records=new_records, receipt=str(out.relative_to(ROOT))), ensure_ascii=False))
