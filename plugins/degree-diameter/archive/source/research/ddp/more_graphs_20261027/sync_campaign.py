"""Incremental Wiki update for verified families and completed finite trials."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
template=json.loads((ROOT/'research/ddp/global_coverage_20261027/candidate42343/wiki_rows.json').read_text())['rows'][0]
families=json.loads((HERE/'delivery/families.json').read_text())['families']

def graph_row(delta, n, base_n, check_rel, orders, evidence):
    r=copy.deepcopy(template)
    check=json.loads((HERE/check_rel).read_text())
    assert check['valid'] and check['n']==n and check['max_degree']==delta
    assert check['diameter']==5 and check['roots_checked']==n and check['bad_unordered_pairs']==0
    r.update(id=f'ddp-h9-qline-d{delta}-family-{n}',
        title=f'完整新图族：({delta},5)各阶{orders[0]}–{n}，最强{n}全源验收',
        family='H9 quadric-line extension',record_type='mathematically-verified-new-lower-bound-family',
        target_Delta=delta,target_D=5,savedL=base_n,n=dict(actual=n,hypothetical=None),
        actual_graph_Delta=delta,actual_D=5,
        actual_D_scope=f'Strongest{n}: root all{n}-source ordinary BFS. Every prefix separately has root earlier-graph R4 induction certificate; not inferred by deleting vertices.',
        ordinary_bad_unordered_pairs=0,ordinary_bad_target_D=5,
        scope=f'Fixed literal Q-line/anchor extension sequence from the public{base_n} graph; alloldedges retained; complete examples at every order{orders[0]}..{n}. Strongest expanded edge list independently all-source checked.',
        failure_or_result=f'最强n{n}/m{check["m"]}/max{delta}/D5/全{n}根bad0。各整数阶前缀有独立完整earlier-R4证据；共{len(orders)}例，公开基线{base_n}，最强提升{n-base_n}。Lean完整实例未完成。',
        positive_guarantees=[
            'Every new point has a distinct complete neighbor set; every affected olddegree had a free slot.',
            'Root independently checked each complete current-base radius4 cover before adding future vertices.',
            f'Strongest graph rebuilt from edge list: simple,connected,max{delta},exactD5,all{n}roots,0badpairs.',
            'Literal family generator dry-run exactly matches the strongest verified edge set; no search is needed to reproduce a prefix.'],
        unclosed_gap='数学构造与验收已完成；对应完整Lean仍未完成，批次Gemini复核另存实际回执。未声称精确最优或已公开接收。',
        lesson_and_restart_condition='几何规则自动处理全部旧核心，剩余degree与extras覆盖作有界精确完成。只接受完整新图，不按坏对下降续轮；未试候选和当时base拒绝范围分开保留。',
        outcome_class='MATHEMATICAL_NEW_BOUND_FAMILY_LEAN_PENDING',wiki_verdict='yes')
    r['other_metrics']=dict(new_lower_bound_mathematically_verified=True,
        improved_parameter_pair=[delta,5],example_orders=orders,example_count=len(orders),
        strongest_n=n,strongest_m=check['m'],public_baseline=base_n,improvement=n-base_n,
        roots_checked=n,all_source_check_CPU_seconds=check['CPU_seconds'],
        all_source_check_wall_seconds=check['wall_seconds'],Lean_complete=False,
        complete_Lean_instances=0,Goal_complete=False,public_submission=False,
        source_author='Dharunish Yugeswardeenoo; underlying partial-fold/duality Rishabh Rajiv',
        prefix_validation='Independent complete new-old R4 plus retained old-old routes; strongest has all-source BFS',
        family_generator='research/ddp/more_graphs_20261027/delivery/family_generator.py')
    if delta==12:
        r['other_metrics'].update(global_degree_pool=609,global_10pin_new_scope=592,
            global_10pin_processed=367,accepted_in_last_batch=32,
            rejected_at_recorded_base=280,degree_rejected=55,unattempted_10pin=225,
            unattempted_8pin=13,failed_earlier_items_retried=False,
            original_7_retested=False)
    else:
        r['other_metrics'].update(global_original_lines=5380830,global_degree_feasible_10pin_sets=24,
            first_hit_pool_index=3,subsequent_scope_items=20,subsequent_hits=2,
            old_first3_failed_not_retried=True,
            current_split_fibers=4074,old_witness_split_fibers=3075,
            old_current_split_intersection=305,
            core_WL_classes=33397,core_WL_pairs=4074,core_WL_singletons=29323,
            fixed_d12_core_only_quotient_degree_invariant_extras=672)
    r['variants']=[dict(order=o,degree=delta,D5_by_complete_induction=True,
                        allsource_BFS_here=(o==n),not_independent_method=True) for o in orders]
    r['report_paths']=[str((HERE/p).relative_to(ROOT)) for p in evidence]+[
        'research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md',
        'research/ddp/more_graphs_20261027/BASELINES_REFRESH.json',
        'research/ddp/more_graphs_20261027/delivery/README.md',
        'research/ddp/more_graphs_20261027/delivery/families.json']
    return r

rows=[
 graph_row(12,42377,42342,'h9_d12_global_extensions/graphs/independent_all_source_BFS_42377.json',
    list(range(42343,42378)),['h9_d12_global_extensions/REPORT.md',
    'h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges',
    'h9_d12_global_extensions/graphs/independent_all_source_BFS_42377.json',
    'h9_d12_global_extensions/root_sequential_R4_checks.json',
    'h9_d12_global_extensions/accepted_extensions.json']),
 graph_row(11,37631,37628,'h9_d11_followups/independent_all_source_BFS_37631.json',
    list(range(37629,37632)),['h9_other_degrees/REPORT.md',
    'h9_d11_followups/REPORT.md','h9_d11_followups/graph_d11_D5_n37631.edges',
    'h9_d11_followups/independent_all_source_BFS_37631.json',
    'h9_d11_followups/root_sequential_R4_checks.json',
    'h9_other_degrees/mapping11_result.json','h9_core_quotient_capacity/REPORT.md'])]

q=dict(id='ddp-h9-d10-free-r4-exactcover',title='(10,5)全部364余量点的≤10精确覆盖：UNKNOWN，已核对称性改为5分支',
 family='H9 quadric-line extension',record_type='finite-coverage-model-no-final-graph',
 target_Delta=10,target_D=5,savedL=33397,n=dict(actual=None,hypothetical=33398),
 actual_D=None,actual_graph_Delta=None,ordinary_bad_unordered_pairs=None,
 scope='Fixed unregularF33397: every one-vertex monotone augmentation has pins among the364 H3 sparevertices. Full R4-covering Booleanmodel with cardinality<=10; 26117 deduplicated targetrows.',
 failure_or_result='LP最小9.0367893；整数dual9036606/1e6严格>9，仅证需要至少10pins。一次120CPU窗MIP无incumbent返回UNKNOWN，未排10pins。后核SL3+J仅C2无用；新增真row-symmetry生成5个pin轨道，下一有限无损分支求解单列，不将意图当完成。',
 positive_guarantees=['364个sparepoints的R4并集确实覆盖全部33397，≤10是否足够仍开放。',
   '五轨道[84,84,28,84,84]来自全26117行保持的实际列置换；固定首个被选轨道代表、前面轨道置零的五分支无损。'],
 unclosed_gap='尚无33398完整候选；UNKNOWN不是整个族不可行，新5分支的结果须按实际后续文件更新。',
 lesson_and_restart_condition='不原样延长旧MIP；只因已验证新的对称性约束才开展一次有限分支检验。分支未解决继续保留原可行性，不以小坏对下降续算。',
 outcome_class='UNKNOWN_NO_NEW_GRAPH_STRUCTURE_CHANGED',wiki_verdict='partial',
 other_metrics=dict(new_graphs_generated=0,original_spare_vertices=364,
  original_target_rows=33397,deduplicated_cover_rows=26117,
  LP_objective=9.036789297658839,original_model_MIP_result='UNKNOWN_NO_INCUMBENT',
  original_LP_MIP_CPU_seconds=116.546768,integer_dual_numerator=9036606,
  integer_dual_denominator=1000000,integer_pins_lower_bound=10,
  SL3_plus_J_candidates=5617,old_symmetry_pin_orbits=192,
  verified_new_pin_orbit_sizes=[84,84,28,84,84],new_case_count=5,
  family_excluded=False),
 report_paths=[str((HERE/p).relative_to(ROOT)) for p in [
  'h9_other_degrees/degree10_exact_cover/REPORT.md',
  'h9_other_degrees/degree10_exact_cover/RESULT.json',
  'h9_other_degrees/degree10_exact_cover/symmetry/REPORT.md',
  'h9_other_degrees/degree10_exact_cover/symmetry_g2_root/REPORT.md']])
rows.append(q)
neg=json.loads((HERE/'wiki_rows_negative.json').read_text())['rows']
rows+=neg
source=dict(updated_UTC=NOW,row_count=len(rows),rows=rows,
            note='Two positive families, one live mathematical gap and two completed finite operation records; no independent-method inflation.')
assert not common['capture'].screen(json.dumps(source,ensure_ascii=False))
(HERE/'wiki_rows.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
normalized=[]
for raw in rows:
    r=common['normalize'](raw)
    r['goal']['baseline_date']='2026-10-27'
    assert r['evidence_paths']
    common['write_node'](r)
    normalized.append(r)
ledger_path=ROOT/'research-wiki/DDP_METHOD_LEDGER.json'
ledger=json.loads(ledger_path.read_text())
replace={r['id']:r for r in normalized}
allrows=[replace.pop(r['id'],r) for r in ledger['rows']]+list(replace.values())
hits={(r['goal']['Delta'],r['goal']['D']) for r in allrows
      if r.get('other_metrics',{}).get('new_lower_bound_mathematically_verified')}
examples=set()
for r in allrows:
    if r.get('other_metrics',{}).get('new_lower_bound_mathematically_verified'):
        for n in r['other_metrics'].get('example_orders',[r['actual_order']]):
            examples.add((r['goal']['Delta'],r['goal']['D'],n))
ledger.update(updated_UTC=NOW,rows=allrows,record_count=len(allrows),
 new_lower_bounds=len(hits),mathematical_new_lower_bounds=len(hits),
 mathematically_improved_parameter_pairs=len(hits),valid_new_graph_examples=len(examples),
 formally_completed_new_lower_bounds=0)
ledger['input_counts']['../more_graphs_20261027/wiki_rows.json']=len(rows)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
page=common['render'](allrows).replace('## 家族目录',
 '当前最强数学结果：N(11,5)≥37631，N(12,5)≥42377；共38个完整阶数例子、2个改进参数对，完整Lean实例0。\n\n## 家族目录',1)
assert not common['capture'].screen(page)
(ROOT/'research-wiki/DDP_METHOD_LEDGER.md').write_text(page)
common['helper'].rebuild_index(str(ROOT/'research-wiki'))
common['helper'].rebuild_query_pack(str(ROOT/'research-wiki'))
result=dict(updated_UTC=NOW,nodes_upserted=[r['id'] for r in normalized],
 record_count=len(allrows),mathematically_improved_parameter_pairs=len(hits),
 valid_new_graph_examples=len(examples),complete_Lean_instances=0,
 historical_nodes_rewritten=0,experiments_rerun=0)
(HERE/'WIKI_SYNC_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
