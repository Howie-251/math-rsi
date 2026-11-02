"""Record the actual one-call restricted391 integer solver handle."""
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
folder=HERE/'d14_K2_fractional_support391'
model=json.loads((folder/'MODEL.json').read_text())
handle=json.loads((folder/'SOLVER_HANDLE.json').read_text())
assert handle['status']=='RUNNING_SINGLE_INTEGER_CALL' and handle['running'] is True
assert (handle['driver_pid'],handle['pid'])==(2092379,2092382)
assert (model['selected_groups'],model['selector_variables'],model['all_variables'],model['total_clauses'])==(391,782,10948,209323)
assert model['source_sided_coverage_rows']==188372 and model['unique_coverage_rows']==187858
assert model['full_target_system'] is True
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows'])==374
identifier='ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029'
row=copy.deepcopy(next(r for r in before['rows'] if r['id']==identifier)['source_record'])
variant=dict(
    label='exact_fractional_positive391_pool_full_target_integer_single_call_20261030',
    status='RUNNING_SINGLE_INTEGER_CALL',running=True,
    pool_groups=391,all_groups=3589,pool_selection='Positiveexactnumeratorinthesavedglobalrationalwitness.',
    additional_restricted_pool=True,lossless_for_all_K2=False,
    selector_variables=782,all_variables=10948,clauses=209323,
    original_two_side_target_rows=188372,exact_unique_coverage_rows=187858,
    exact_duplicate_rows_merged=514,full_target_system=True,
    capacity1_mutex_groups=379,capacity2_groups=12,side_pin_limit=13,
    prepare_CPU_seconds=4.008762751,
    actual_driver_pid=2092379,actual_solver_pid=2092382,
    actual_handle='research/ddp/refresh_20261029/d14_K2_fractional_support391/SOLVER_HANDLE.json',
    solver_option='-t120',solver_CPU_hard_limit=121,whole_CPU_budget=150,
    whole_budget_includes_preparation=True,max_solver_calls=1,UNKNOWN_stops=True,
    root_code_review_saved=True,
    source_graph_reads=0,BFS_runs=0,graphs_generated=0,
    terminal_result_recorded=False)
variants={v['label']:v for v in row['variants']}
variants[variant['label']]=variant
row['variants']=list(variants.values())
row['outcome_class']='RUNNING_RESTRICTED391_FULL_TARGET_INTEGER_SINGLE_CALL'
row['other_metrics'].update(
    current_numerical_status='RUNNING_RESTRICTED391_FULL_TARGET_INTEGER_SINGLE_CALL',
    current_running=True,allfree_original_integer_status='UNKNOWN',
    proposed_integer_support_pool_size=391,
    proposed_integer_support_pool_is_extra_restriction=True,
    proposed_integer_support_pool_lossless_for_allK2=False,
    proposed_integer_support_solver_run_recorded=True,
    restricted391_actual_driver_pid=2092379,restricted391_actual_solver_pid=2092382,
    restricted391_selector_variables=782,restricted391_all_variables=10948,
    restricted391_clauses=209323,restricted391_full_targets=True,
    restricted391_unique_two_side_rows=187858,restricted391_max_calls=1,
    restricted391_solver_window=120,restricted391_whole_CPU_budget=150,
    restricted391_terminal_recorded=False)
row['failure_or_result']+='；由精确分数391正组生成的额外受限整数域已真实启动唯一调用：782selectors/10948vars/209323clauses、全部188372两侧targetrows精确去重187858、379cap1mutex/12cap2。driver2092379/solver2092382，-t120硬121，whole150含prepare4.008762751，UNKNOWN即停；目前不登记终态或新图，不视为allK2等价。'
row['unclosed_gap']='391正组额外受限pool的完整目标整数单call已实际RUNNING，等待root终态；不是all3589组K2无损归约。全K2原整数问题仍UNKNOWN；分数全目标可行不等于整数可行。未生成94187/94188图，不自动续预算。'
paths=[str(p.relative_to(ROOT)) for p in sorted(folder.iterdir())
    if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'}]
row['report_paths']=list(dict.fromkeys(row['report_paths']+paths))
assert all((ROOT/p).exists() for p in row['report_paths'])
spec=importlib.util.spec_from_file_location('capture_filter',ROOT/'aris_repo/tools/capture_filter.py')
capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
assert not capture.screen(json.dumps(row,ensure_ascii=False))
pending=HERE/'D14_SUPPORT391_RUNNING_WIKI_ROWS.json'
pending.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==374
for k in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
          'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[k]==after[k]
receipt=dict(status='PASS_D14_RESTRICTED391_ACTUAL_SINGLE_RUN_RECORDED',
    updated_UTC=NOW,existing_id=identifier,record_count=374,
    actual_status='RUNNING_SINGLE_INTEGER_CALL',driver_pid=2092379,solver_pid=2092382,
    groups=391,selectors=782,all_variables=10948,clauses=209323,
    complete_target_rows_original=188372,exact_unique_rows=187858,
    additional_restricted_pool=True,allK2_equivalence_claimed=False,
    max_calls=1,solver_window=120,solver_hard_CPU_limit=121,whole_CPU_budget=150,
    terminal_result_recorded=False,new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out=HERE/'D14_SUPPORT391_RUNNING_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),record_count=374),ensure_ascii=False))
