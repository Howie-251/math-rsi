"""Upsert this study only; preserve all historical experiment nodes."""
from pathlib import Path
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
common = runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
paths = ['REPORT.md', 'h9_relation/REPORT.md', 'h9_relation/star_containment.json',
         'h9_bare_core_clones/REPORT.md', 'h9_bare_core_clones/integer_upper_bound.json',
         'h9_bare_core_clones/STAR_CONTAINMENT_EXTENSION.json',
         'h9_clone_capacity/REPORT.md', 'h9_global_rule/REPORT.md',
         'tail165_mechanism/PREDICTIONS.md', 'tail165_mechanism/RESULT.json',
         'tail165_mechanism/P4_COUNTERFACTUAL.md', 'tail165_mechanism/P4_RESULT.json',
         'tail165_mechanism/P5_PAIR_PREDICTION.md', 'tail165_mechanism/P5_RESULT.json',
         'h9_global_rule/P6_PREDICTION.md', 'tail165_mechanism/P6_RESULT.json']
paths += ['h9_line_signature/REPORT.md', 'h9_line_pair_rule/REPORT.md',
          'h9_quadric_line_signature/REPORT.md', 'h9_quadric_line_rule/REPORT.md',
          'h9_quadric_center/REPORT.md', 'quadric_batch/RESULT.json',
          'h9_quadric_line_extension_pool/REPORT.md', 'quadric_extension/RESULT.json',
          'quadric_anchor_completion/REPORT.md']
row = dict(
    id='ddp-h9-global-coverage-20261027',
    title='H9整体覆盖对照：675条Q-line恢复、统一旧覆盖及343完整星上限',
    family='H9 partial fold global coverage',
    record_type='known-source-mechanism-prediction-study',
    target_Delta=12, target_D=5, savedL=42342,
    n=dict(actual=42342, hypothetical=None), actual_D=5,
    actual_D_scope='Existing public42342 source: inherited geometric core plus all986 sequential earlier-R4 induction checks; not a new graph or repeated full-source BFS.',
    actual_graph_Delta=12, ordinary_bad_unordered_pairs=None,
    scope='Same explicit source pair41699/42342 and common K41356. Exact fixedK ordinary/full-star-containing augmentation ceiling; source-only static/ordered R4 comparisons and two frozen shortcut counterfactuals. No new optimizer, graph, old S/c rerun or local pin repair.',
    failure_or_result='已有42342图从共同K起986步有序R4全通过；新纪录0。固定K完整星扩展整类≤343，n≤41699；当前extras176含完整星、810不含。P1静态独立批推翻，P4单helper因果支持，P5部分推翻，P6固定两helper通用层推翻并停止。',
    positive_guarantees=[
        '共同K的全部234318边精确相同，其D≤5由旧partial-fold定理继承。',
        '287个分割预算行给出343整类上界且旧343独立克隆可行；extra anchors/new-new edges不会绕过核心完整星负载约束。',
        '实测宽包含分类为176完整星且均exact、810 non-star；不将它们直接命名为pencils。',
        '已有986步更早邻集R4覆盖完整更早诱导图，完整证明已有source D≤5，涵盖所有点对类型。',
        'P4/P5保存的helper路线确实提供旧核心shortcut，区别于普通独立克隆。'],
    unclosed_gap='没有超过42342的完整图；810 non-star的统一几何生成公式和可扩展的所有新类间覆盖尚未恢复。有序证书解释既有图，不自动生成第987点；两helper层仅固定选择失败。',
    lesson_and_restart_condition='停止固定K完整星数量搜索和1152局部补洞。下一步仅检验非star几何line-image/锚点及全新类路由；P6失败后不按遗漏加第三helper。不得从结构理解、P1条件失败数或既有source复现宣称新下界。',
    outcome_class='positive-local-known-source-no-new-bound', wiki_verdict='partial',
    other_metrics=dict(
        snapshot_UTC=common['NOW'], known_source_order=42342, known_source_max_degree=12,
        new_graphs_generated=0, new_lower_bounds=0,
        old_full_all_source_BFS_repeated=False,
        common_core_order=41356, common_core_edges=234318, current_extras=986,
        star_containing_actual=176, strict_superset_actual=0, non_star_actual=810,
        fixed41636_ordinary_clone_optimum=63,
        fixed41356_ordinary_clone_optimum=343,
        fixed41356_full_star_containing_count_upper_bound=343,
        fixed41356_all_star_total_order_upper_bound=41699,
        star_upper_bound_cover_rows=287,
        minimum_nonstar_for_current986=643, minimum_nonstar_for_target987=644,
        static_R4_condition_failed_vertices=7, static_pinset_pair_condition_failures=1,
        static_conditions_are_not_finalgraph_badpair_counts=True,
        ordered986_failed_steps=0, ordered_tail165_failed_steps=0,
        P1='REFUTED', P2='SUPPORTED_165_STEPS', P3='SUPPORTED_986_STEPS',
        P4='SUPPORTED_FIXED_HELPER_COUNTERFACTUAL',
        P5='PARTIALLY_REFUTED_one_of_two_not_independently_safe',
        P6='REFUTED_FIXED_TWO_HELPER_UNIVERSAL_LAYER',
        P6_remaining_vertices=163, P6_failed_R4_vertices=6,
        P6_all_pinset_pair_conditions_pass=True,
        P6_new_multisource_tests=7, P6_reused_static_R4_rows=156,
        LP_calls=0, MIP_calls=0, pin_optimization=False,
        active_question='Recover a geometric non-star neighborhood rule and whole-class routes; no third-helper repair.'),
    variants=[
        dict(label='Fixed41636 ordinary twins', optimum=63, order_ceiling=41699, new_graph=False),
        dict(label='BareK full-star-containing family', optimum_ordinary_clones=343,
             all_star_count_ceiling=343, order_ceiling=41699, new_graph=False),
        dict(label='Existing42342 ordered certificate', earlier_R4_checks=986, failed_steps=0,
             known_source=True, new_graph=False),
        dict(label='Fixedtwohelpers P6', status='REFUTED', optimization=False,
             new_multisource_tests=7, new_graph=False)],
    report_paths=[str((HERE/p).relative_to(ROOT)) for p in paths])
row.update(
    failure_or_result='已有42342图986步有序保径通过。675个分散附件全部识别为Q(6,9)奇异线像+anchors，坐标API可生成；统一旧核心→新点≤5证明完成。静态独立批充分证书及中心anchor预测失败。此结构研究另导出42343完整新图，独立新纪录节点分账。',
    unclosed_gap='675的mandatory几何规则已恢复；源anchors仍无统一几何公式，剩余135 non-star未识别。P8只反驳静态核心充分证书，不否定新增独立点之间的互助。新42343图的全图验收与Lean在独立节点记录。',
    lesson_and_restart_condition='实际改用Q-line全旧核心覆盖规则，649已识别中心的81线有限degree筛得到7项；固定至多2anchors精确完整覆盖得到首次新图。不再按坏对下降调参，不扩中心或加第三anchor；已转该数学成果的交付与形式化。')
row['positive_guarantees'] += [
    '675/675匹配非H9的ambientQ singularlines，657像10、18像7；完整两点坐标→line→fold-pins API可重现。',
    'flatness与7381点壳/切超平面计数证明B(p,x)=0 iff H点距≤4；每Q-line遇p-perp，故mandatorypins保证全部旧核心五步覆盖。',
    '675条selectedline均有唯一平面中心；632个非空image10 anchor集反驳直接中心phi-fiber规则，不换witness拟合。']
row['other_metrics'].update(
    Q_line_matched_source_objects=675, Q_line_image10=657, Q_line_image7=18,
    Q_line_witness_uniqueness_checked=False,
    line_api_independent_of_source_adjacency=True,
    uniform_oldcore_to_new_bound=5, arbitrary_new_new_bound_only=6,
    selected_centers=675, distinct_centers=649,
    P8_core_set_pairs_per_condition=227475,
    P8_mandatory_failed_sufficient_conditions=15639,
    P8_full_core_attachment_failed_sufficient_conditions=1752,
    P8_failure_not_necessity_and_not_finalgraph_badpairs=True,
    finite_geometric_lines_generated=52569, degree_feasible_mandatory_sets=7,
    P9_all_seven_mandatory_only_full_extensions_failed=True,
    P10='FIRST_COMPLETE_INSTANCE_FOUND_SEPARATE_RECORD',
    resulting_new_graph_node='exp:ddp-h9-qline-42343',
    active_question='Mathematical hit obtained; preserve mechanism evidence and complete new graph delivery/formalization in its own node.')
source = dict(updated_UTC=common['NOW'], row_count=1, rows=[row],
              note='One existing-source mechanism study; subordinate proofs/tests are not independent methods.')
assert not common['capture'].screen(json.dumps(source, ensure_ascii=False))
(HERE/'wiki_rows.json').write_text(json.dumps(source, ensure_ascii=False, indent=2)+'\n')
normalized = common['normalize'](row)
assert normalized['object_level'] == 'known_source_or_recovery'
assert normalized['order_margin'] is None
assert all((ROOT/p).exists() for p in normalized['evidence_paths'])
common['write_node'](normalized)
ledger_path = ROOT/'research-wiki/DDP_METHOD_LEDGER.json'
ledger = json.loads(ledger_path.read_text())
old = ledger['rows']
rows = [r for r in old if r['id'] != normalized['id']] + [normalized]
ledger.update(updated_UTC=common['NOW'], record_count=len(rows), rows=rows)
ledger['input_counts']['../global_coverage_20261027/wiki_rows.json'] = 1
ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n')
page = common['render'](rows)
addition = ('\nH9当前机制已恢复675条Q-line附件及统一旧核心五步覆盖；'
            '649中心有限线池与至多2anchor精确补全已产生42343图，数学验收与Lean分列。'
            '固定K完整星扩展≤343，总阶≤41699；静态核心充分证书失败不等于实际图失败。'
            '见[当前实验](experiments/ddp-h9-global-coverage-20261027.md)。\n')
page = page.replace('## 家族目录', addition+'\n## 家族目录', 1)
assert not common['capture'].screen(page)
(ROOT/'research-wiki/DDP_METHOD_LEDGER.md').write_text(page)
common['helper'].rebuild_index(str(ROOT/'research-wiki'))
common['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))
result = dict(updated_UTC=common['NOW'], record_count=len(rows),
              nodes_upserted=[normalized['id']], historical_nodes_rewritten=0,
              historical_import=False, experiments_rerun=0, new_lower_bounds=0)
(HERE/'WIKI_SYNC_RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False))
