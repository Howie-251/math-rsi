"""Record the explicit remaining-budget decision, without claiming a new run."""
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
spec = importlib.util.spec_from_file_location('capture_filter', ROOT/'aris_repo/tools/capture_filter.py')
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)
terminal_path = HERE/'d14_D5_K2_route_gate/K2_model/SOLVER_TERMINAL.json'
terminal = json.loads(terminal_path.read_text())
assert terminal['status'] == 'UNKNOWN_SOLVER_RETURN' and terminal['solver_calls'] == 2
assert terminal['rounds'][0]['root_missing_counts'] == [6292,6096]
assert len(terminal['rounds'][0]['exact_violated_rows_added']) == 512
assert terminal['rounds'][1]['code'] == -9
assert terminal['rounds'][1]['observation_expired'] is False
ledger = json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert ledger['record_count'] == len(ledger['rows']) == 374
identifier = 'ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029'
row = copy.deepcopy(next(r for r in ledger['rows'] if r['id']==identifier)['source_record'])
variant = dict(
    label='parent_explicit_remaining_original_budget_reassessment_after_stage2_UNKNOWN_20261029',
    status='PREPARING_NOT_RUNNING_PARENT_REVIEW_REQUIRED',
    justification='Round1 returned SAT and actual complete-target counterexamples, followed by512 exact violated rows; this is actionable model feedback, not merely a smaller missing count.',
    inherited_stage2_terminal='UNKNOWN_SOLVER_RETURN',
    inherited_stage2_solver_exit=-9, inherited_stage2_observation_expired=False,
    old_solver_process_terminal=True, same_model_active_coverage_rows=1188,
    solver_CPU_spent=19.21988, solver_CPU_cumulative_cap=60,
    maximum_solver_CPU_remaining=40.78012,
    whole_batch_CPU_spent=28.25784697, whole_batch_CPU_cumulative_cap=90,
    maximum_whole_batch_CPU_remaining=61.74215303,
    solver_calls_already_used=2, next_call_number=3, maximum_total_calls=6,
    budget_reset=False, new_family_or_goal=False, new_actual_handle_recorded=False,
    parent_audits_carryover_before_launch=True, running=False,
    scope='Only the same all3685 K2 model with the existing1188 exact rows and original remaining cumulative budgets; no new source, seed or parameter ladder.',
    inherited_F5_induced_or_C11_C31_C33_stops_revoked=False)
variants = {v.get('label',v.get('name')):v for v in row['variants']}
variants[variant['label']] = variant
row['variants'] = list(variants.values())
row['other_metrics'].update(
    current_numerical_status='UNKNOWN_SOLVER_RETURN',
    current_running=False, latest_completed_calls=2,
    parent_remaining_budget_reassessment='PREPARING_NOT_RUNNING',
    same_model_active_exact_rows=1188,
    cumulative_solver_CPU_spent=19.21988, cumulative_solver_CPU_cap=60,
    cumulative_whole_batch_CPU_spent=28.25784697, cumulative_whole_batch_CPU_cap=90,
    cumulative_budget_reset=False, next_authorized_call_number=3)
row['unclosed_gap'] = 'K2第二轮真实UNKNOWN保留，旧solver已终止。父级因首轮SAT+真实反例+512exactcuts明确重评：同1188row模型可在原60solver/90wholeCPU的剩余额内继续，累计call从3、总≤6；carryover模式尚待root审计，未据此记新RUN。数学可行性未决，无候选图。'
row['lesson_and_restart_condition'] += '；本次父级显式修订首UNKNOWN即停的初始批策略：首轮SAT反馈产生真实模型精化，原预算尚余，因此允许同1188row模型在原剩余额内一次重评继续；保留stage2终态历史，不重置预算、不把它称observationtimeout重启。新handle前仍非运行，F5 induced及旧C11/31/33停止边界不变。'
row['restart_condition'] = 'Explicit parent-authorized remaining-budget continuation only after carryover audit; original cumulative60solver/90wholeCPU caps and totalcalls<=6 retained. No automatic restart of terminated stage2 process.'
assert not capture.screen(json.dumps(row,ensure_ascii=False))
pending = HERE/'K2_REMAINING_BUDGET_REVIEW_WIKI_ROWS.json'
pending.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
command = [sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run = subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after = json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == 374
for k in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
          'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert ledger[k] == after[k]
receipt = dict(status='PASS_K2_PARENT_REMAINING_BUDGET_REASSESSMENT_PREPARATION_RECORDED',
    updated_UTC=NOW,record_count=374,existing_id=identifier,
    stage2_actual_status='UNKNOWN_SOLVER_RETURN',stage2_process_terminal=True,
    parent_reassessment_status='PREPARING_NOT_RUNNING',new_RUN_claimed=False,
    active_exact_rows=1188,solver_calls_spent=2,next_call_number=3,total_call_cap=6,
    solver_CPU_spent=19.21988,solver_CPU_cap=60,
    whole_batch_CPU_spent=28.25784697,whole_batch_CPU_cap=90,budget_reset=False,
    new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out = HERE/'K2_REMAINING_BUDGET_REVIEW_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),record_count=374),ensure_ascii=False))
