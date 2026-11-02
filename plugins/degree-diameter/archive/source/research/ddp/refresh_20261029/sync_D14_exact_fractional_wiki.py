"""Record the exact full-target fractional witness on the existing K2 row."""
from pathlib import Path
from datetime import datetime,timezone
import copy
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
spec=importlib.util.spec_from_file_location('capture_filter',ROOT/'aris_repo/tools/capture_filter.py')
capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
folder=HERE/'d14_K2_fractional_capacity'
result=json.loads((folder/'RESCALING_RESULT.json').read_text())
assert result['status']=='EXACT_GLOBAL_FRACTIONAL_WITNESS_VERIFIED'
assert result['denominator']==1000000000 and result['sum_numerator']==24136823828
assert result['complete_target_count']==94186 and result['positive_groups']==391
assert result['minimum_integer_coverage']==2000000030
assert result['required_integer_coverage']==2000000000
assert result['all_group_caps_exactly_pass'] is True
assert result['additional_LP_calls']==result['BFS_runs']==result['SAT_calls']==0
assert result['running'] is False and result['pending']==[]
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows'])==374
identifier='ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029'
row=copy.deepcopy(next(r for r in before['rows'] if r['id']==identifier)['source_record'])
variant=dict(
    label='exact_all94186_target_symmetric_fractional_capacity_feasible_witness_20261030',
    status='EXACT_GLOBAL_FRACTIONAL_WITNESS_VERIFIED',
    variables='x_g=alpha_g+beta_g on3589exactcoveragegroups',
    fractional_condition='0<=x_g<=c_g;sum(R3support+R4support)*x_g>=2 onalltargets;sumx<=26.',
    denominator=1000000000,sum_numerator=24136823828,
    total_fractional_weight='24.136823828',upper_total_limit=26,
    positive_groups=391,full_targets_checked_exactly=94186,
    minimum_integer_coverage=2000000030,required_integer_coverage=2000000000,
    minimum_target=39334,all_group_caps_exactly_pass=True,
    symmetric_two_side_assignment='alpha=beta=x/2',
    fractional_weight_per_side='12.068411914',per_side_pin_limit=13,
    integer_A_B_feasible_claimed=False,LP_optimal_value_claimed=False,
    prior_three_sparse_row_LPs_preserved=True,actual_LP_calls=3,
    rescaling_after_round3=True,additional_LP_calls=0,
    prior_three_rounds_whole_CPU_seconds=5.425692188,
    rescaling_exact_check_CPU_seconds=result['CPU_seconds'],
    whole_CPU_seconds=5.636402926,
    source_graph_reads=0,BFS_runs=0,SAT_calls=0,new_graphs=0,
    no_fractional_capacity_lower_bound_above26_possible_for_this_exact_relaxation=True,
    latest_result='research/ddp/refresh_20261029/d14_K2_fractional_capacity/RESCALING_RESULT.json',
    exact_vector='research/ddp/refresh_20261029/d14_K2_fractional_capacity/EXACT_GLOBAL_WITNESS.json',
    old_RESULT_and_TERMINAL_are_historical_sparse_round_stage=True)
variants={v['label']:v for v in row['variants']}
variants[variant['label']]=variant
row['variants']=list(variants.values())
row['outcome_class']='INTEGER_K2_UNRESOLVED_EXACT_FRACTIONAL_RELAXATION_FEASIBLE'
row['failure_or_result']+='；新对称分数松弛全94186target有精确有理解：D=1e9、总分子24136823828即24.136823828<26，391正组；最小整数覆盖2000000030≥2e9且逐groupcap通过，alpha=beta=x/2后各侧12.068411914<13。三轮稀行LP+一次root缩放合5.636402926CPU，0追加LP/SAT/BFS/图。不是LP全局最优或整数K2可行声明，最终读RESCALING_RESULT。'
row['other_metrics'].update(
    current_numerical_status='INTEGER_K2_UNRESOLVED_EXACT_FRACTIONAL_RELAXATION_FEASIBLE',
    current_running=False,fractional_actual_LP_calls=3,
    fractional_full_target_count=94186,fractional_exact_denominator=1000000000,
    fractional_exact_sum_numerator=24136823828,
    fractional_exact_sum='24.136823828',fractional_positive_groups=391,
    fractional_min_integer_coverage=2000000030,fractional_required_integer_coverage=2000000000,
    fractional_all_caps_exactly_pass=True,
    fractional_per_helper_sum='12.068411914',
    fractional_optimality_claimed=False,integer_K2_feasible_claimed=False,
    fractional_total_CPU_seconds=5.636402926,fractional_extra_LP_calls=0,
    fractional_latest_result='RESCALING_RESULT.json',
    proposed_integer_support_pool_size=391,
    proposed_integer_support_pool_is_extra_restriction=True,
    proposed_integer_support_pool_lossless_for_allK2=False,
    proposed_integer_support_solver_run_recorded=False,
    fixed_K2_family_excluded=False)
row['lesson_and_restart_condition']+='；标准分数容量松弛现在有全目标精确可行证据，不能再用同一松弛的dual>26作为障碍证书；整数协调仍未解。391个正组可提供一个有实际数据依据的受限生成池，但忽略其它组是额外限制，不是整个K2的无损归约。下一整数准备不能记成新solver已运行，也不把分数可行向量当端口集合或新图。'
row['unclosed_gap']='Allfree整数K2存在性仍UNKNOWN。标准对称及双侧分数覆盖松弛已精确全94186目标可行，总量24.136823828<26；不证明最优或整数可行。391正组受限的完整目标整数构造模型尚准备，范围额外受限、不等价全部K2，尚无新solver回执；原3call整数UNKNOWN与三轮LP历史分别保留。'
paths=[str(p.relative_to(ROOT)) for p in sorted(folder.iterdir())
    if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'}]
row['report_paths']=list(dict.fromkeys(row['report_paths']+paths))
assert all((ROOT/p).exists() for p in row['report_paths'])
assert not capture.screen(json.dumps(row,ensure_ascii=False))
pending=HERE/'D14_EXACT_FRACTIONAL_WIKI_ROWS.json'
pending.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==374
for k in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
          'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[k]==after[k]
receipt=dict(status='PASS_D14_EXACT_GLOBAL_FRACTIONAL_WITNESS_RECORDED_PENDING_INTEGER',
    updated_UTC=NOW,existing_id=identifier,record_count=374,
    exact_full_target_witness=True,target_count=94186,sum_numerator=24136823828,
    denominator=1000000000,total='24.136823828',positive_groups=391,
    minimum_integer_coverage=2000000030,required_integer_coverage=2000000000,
    each_helper_fractional_total='12.068411914',
    LP_optimality_claimed=False,integer_K2_feasible_claimed=False,
    total_CPU_seconds=5.636402926,additional_LP_calls=0,
    restricted391_pool_prepare_only=True,restricted_pool_lossless=False,new_solver_run_recorded=False,
    new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out=HERE/'D14_EXACT_FRACTIONAL_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),record_count=374),ensure_ascii=False))
