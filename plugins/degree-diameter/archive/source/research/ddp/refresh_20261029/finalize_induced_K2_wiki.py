"""Close the actual induced/K2 research turn after the root-state update."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ROOT_UPDATED='2026-10-29 23:22:14 UTC'


def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'aris_repo/tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


helper,capture=module('research_wiki'),module('capture_filter')


def screen(text):
    assert not capture.screen(text),capture.screen(text)
    return text


owned=[ROOT/'AGENTS.md',ROOT/'RESEARCH_BRIEF.md',
    ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',
    ROOT/'research/progress.html',
    ROOT/'expert_review_current/EXPERT_HANDOFF_20261029.md',
    ROOT/'expert_review_current/build_handoff_20261029.py']
owned_before={p:p.read_bytes() for p in owned}
brief=(ROOT/'RESEARCH_BRIEF.md').read_text()
assert '23:22:14' in brief and 'INDUCED16_K2_14_TURN_RESULT.json' in brief
turn=json.loads((HERE/'INDUCED16_K2_14_TURN_RESULT.json').read_text())
assert turn['status']=='INDUCED16_K2_14_BATCH_COMPLETE_NO_NEW_RECORD'
assert turn['all_numerical_work_terminal'] is True and turn['pending']==[]
k2root=HERE/'d14_D5_K2_route_gate/K2_model'
final=json.loads((k2root/'RESUME_SOLVER_RESULT.json').read_text())
assert final['status']=='UNKNOWN_SOLVER_RETURN' and final['running'] is False
assert final['solver_calls']==3 and final['new_solver_calls']==1
assert final['solver_CPU_seconds']==58.2235 and final['whole_batch_CPU_seconds']==67.547291753
assert final['same_original_batch'] is final['old_stage2_records_preserved'] is True
assert final['error'] is None and final['pending']==[] and final['cached_full_cover_hit'] is False
assert final['rounds'][2]['window_seconds']==39 and final['rounds'][2]['code']==-9
assert final['rounds'][2]['observation_expired'] is False
assert (k2root/'stage2_history/SOLVER_TERMINAL.json').is_file()
stage2=json.loads((k2root/'stage2_history/SOLVER_TERMINAL.json').read_text())
assert stage2['solver_calls']==2 and stage2['solver_CPU_seconds']==19.21988
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows'])==374
ids=['ddp-f5-literal3750-induced-retention-max16-d3-20261029',
     'ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029']
source={r['id']:r for r in before['rows']}
rows={key:copy.deepcopy(source[key]['source_record']) for key in ids}
experiment_names=sorted(p.name for p in (WIKI/'experiments').glob('*.md'))
claim_names=sorted(p.name for p in (WIKI/'claims').glob('*.md'))

f5=rows[ids[0]]
assert f5['other_metrics']['cross_model_transversal_review_status']=='SUCCESS_STATIC_MATH_PASS'
assert f5['other_metrics']['transversal_3600_external_reviewed'] is False
f5['baseline_date']='2026-10-29'
f5['savedL_source']=turn['baseline16']['source']
f5['other_metrics']['latest_batch_all_terminal']=True
f5['other_metrics']['latest_batch_index']='research/ddp/refresh_20261029/INDUCED16_K2_14_TURN_RESULT.json'
f5['unclosed_gap']='一般>=1921点max16/D3诱导子图仍开放；本批必要closure单次15CPU UNKNOWN、0候选并已停止，不续。transversal整域排除和压缩closure规范已实际外审PASS到原2000下界；后续恰3600跨fiber坏对仅本地独立推导及已存单根fiber5缺36一致，不冒全3600外审/CNF/Lean/全对测量。'

k2=rows[ids[1]]
variants={v['label']:v for v in k2['variants']}
initial=variants['all3685_joint_capacity_exact_two_root_K2_CEGIS_model_20261029']
initial['stage']='COMPLETED_INITIAL_STAGE2_HISTORY_PRESERVED'
initial['actual_state_file']='research/ddp/refresh_20261029/d14_D5_K2_route_gate/K2_model/stage2_history/SOLVER_TERMINAL.json'
initial['superseded_as_current_state_by']='same_original_batch_remaining_budget_call3_final_UNKNOWN_20261029'
reassessment=variants['parent_explicit_remaining_original_budget_reassessment_after_stage2_UNKNOWN_20261029']
reassessment['stage_at_creation']='PREPARING_NOT_RUNNING_PARENT_REVIEW_REQUIRED'
reassessment['status']='COMPLETED_WITHIN_ORIGINAL_CUMULATIVE_BUDGETS'
reassessment['new_actual_handle_recorded']=True
reassessment['carryover_review_completed_before_launch']=True
reassessment['running']=False
reassessment['final_solver_CPU_cumulative']=58.2235
reassessment['final_whole_batch_CPU_cumulative']=67.547291753
resume=dict(
    label='same_original_batch_remaining_budget_call3_final_UNKNOWN_20261029',
    status='UNKNOWN_SOLVER_RETURN',running=False,
    final_result='research/ddp/refresh_20261029/d14_D5_K2_route_gate/K2_model/RESUME_SOLVER_RESULT.json',
    stage2_history='research/ddp/refresh_20261029/d14_D5_K2_route_gate/K2_model/stage2_history/',
    same_original_batch=True,budget_reset=False,
    reason_for_reassessment='Actualround1SAT gave fulltargetcounterexamples and512 exactviolatedrows; originalbudgetstillhadremainingcapacity.',
    initial_round1_full_source_missing=[6292,6096],
    initial_rows=676,exact_rows_added=512,refined_exact_rows=1188,
    prior_solver_calls=2,new_solver_calls=1,total_solver_calls=3,
    resumed_call_number=3,resumed_window_seconds=39,
    resumed_solver_exit=-9,resumed_observation_expired=False,
    prior_solver_CPU_seconds=19.21988,new_solver_CPU_seconds=39.00362,
    cumulative_solver_CPU_seconds=58.2235,original_solver_CPU_cap=60,
    prior_whole_batch_CPU_seconds=28.25784697,
    cumulative_whole_batch_CPU_seconds=67.547291753,original_whole_batch_CPU_cap=90,
    new_driver_CPU_seconds=final['new_driver_CPU_seconds'],
    old_stage2_records_preserved=True,
    actual_full_source_two_root_checks=1,
    cached_full_cover_hit=False,source_reads=0,new_R3_runs=0,new_R4_runs=0,
    source_D5_BFS=0,graphs_exported=0,error=None,pending=[],
    fixed_K2_family_excluded=False,automatic_further_resume_allowed=False)
variants[resume['label']]=resume
k2['variants']=list(variants.values())
k2['outcome_class']='UNKNOWN_SAME_ORIGINAL_BATCH_TERMINAL'
k2['failure_or_result']=(
    'All3685newR3balls completed once,oldR4reused; eachtarget25..119providers,T0empty. '
    'One13+13greedy misses3881/3559oldtargets. Jointselector initial676rows returnedSAT but fulltwo-rootcache check missed6292/6096; '
    '512exactrows yielded1188rows. Round2 -t15 UNKNOWN; explicitfeedback-based originalremainingbudgetreassessment allowedcall3 -t39 onthatidenticalCNF. '
    'FinalUNKNOWN,3totalcalls/1resumedcall,58.2235solverCPU/67.547291753wholeCPU underoriginal60/90caps,0graph/nohit/errornull/pending[].')
k2['other_metrics'].update(
    current_numerical_status='UNKNOWN_SAME_ORIGINAL_BATCH_TERMINAL',current_running=False,
    solver_calls_at_snapshot=3,latest_completed_calls=3,
    parent_remaining_budget_reassessment='COMPLETED_WITHIN_ORIGINAL_CAPS',
    same_model_active_exact_rows=1188,exact_real_rows_added=512,
    cumulative_solver_CPU_spent=58.2235,cumulative_solver_CPU_cap=60,
    cumulative_whole_batch_CPU_spent=67.547291753,cumulative_whole_batch_CPU_cap=90,
    cumulative_budget_reset=False,resumed_calls=1,
    resumed_window_seconds=39,actual_full_source_two_root_checks=1,
    actual_round1_SAT_root_missing=[6292,6096],
    old_stage2_records_preserved=True,all_numerical_work_terminal=True,
    latest_batch_index='research/ddp/refresh_20261029/INDUCED16_K2_14_TURN_RESULT.json',
    new_complete_94187_or94188_graphs=0,fixed_K2_family_excluded=False)
k2['other_metrics'].pop('next_authorized_call_number',None)
k2['unclosed_gap']='此literal94186的allfree K2联合覆盖仍未决。原同batch已在累计58.2235solver/67.547291753wholeCPU后终态UNKNOWN，3calls、无hit/图/error/pending；原60/90预算未重置，stage2历史保留。本批停止，不因剩少量预算自动再续。UNKNOWN不是整族排除。'
k2['lesson_and_restart_condition']='跨两root的真实覆盖必须共同满足大多数cap1端口。首SAT通过初始必要子系统却漏6292/6096，产生512实际精确反例row；这项有用反馈支撑一次父级明确的原剩余预算重评。第三call同1188row模型39秒后仍UNKNOWN，累计预算未重置，说明本批未解决共同覆盖。停止本批；下一次必须有具体新生成规则、更强结构表示或有用真实反馈，不机械增长timer/seed/helper数。'
k2['restart_condition']='No automatic continuation of this completed batch. Any future run needs a specific new rule, stronger representation or useful actual feedback; old budgets and histories remain cumulative evidence.'

turn_paths=['research/ddp/refresh_20261029/INDUCED16_K2_14_TURN_RESULT.json',
            'research/ddp/refresh_20261029/INDUCED16_K2_14_TURN.md']
resume_paths=[str(p.relative_to(ROOT)) for p in sorted(k2root.iterdir())
              if p.is_file() and p.name.startswith('RESUME_') and p.suffix in {'.md','.json'}]
k2['report_paths']=list(dict.fromkeys(k2['report_paths']+resume_paths+[
    'research/ddp/refresh_20261029/d14_D5_K2_route_gate/K2_model/stage2_history/SOLVER_TERMINAL.json']))
for row in rows.values():
    row['report_paths']=list(dict.fromkeys(row['report_paths']+turn_paths))
    assert not capture.screen(json.dumps(row,ensure_ascii=False))
    assert all((ROOT/p).exists() for p in row['report_paths'])
pending=HERE/'INDUCED_K2_FINAL_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)

comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- INDUCED_K2_FINAL_COMPLETED_20261029 -->'
note=f'''
## {NOW} induced16／K2-14本轮全部终态

root于23:22:14 UTC更新原状态，当前恢复入口为[总终态](../research/ddp/refresh_20261029/INDUCED16_K2_14_TURN_RESULT.json)和[推导与决策](../research/ddp/refresh_20261029/INDUCED16_K2_14_TURN.md)。

16度仅固定3000点诱导图和四方向transversal域失败；任意keep模型15CPU UNKNOWN，0候选、不续本批。外审PASS原2000下界及压缩closure逻辑；3600加强仅本地独立推导，不能混成全图测量或外审CNF认证。

14度K2首SAT完整检查漏6292/6096，加入512exactrows至1188。第二call15CPU UNKNOWN后，因真实模型反馈明确重评原剩余预算，第三call同CNF39秒，最后仍UNKNOWN；累计58.2235solver/67.547291753wholeCPU，原caps60/90未重置，3totalcalls、0图/nohit/errornull/pending[]。stage2_history保留，不将这次审后续算称observationtimeout重启。

全部工具数值与外审已终态。一般induced和K2均未排，本批停止。ledger374是2条新增实验记录、非方法数；104/4、confirmed103/3、Lean1保持。21:55专家快照不改、不重打包；最终canonical query在root当前状态之后重建。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:out.write('\n\n'+marker+'\n'+screen(note))
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
assert '账本现374条实验／来源记录' in gap[:1800]
old_marker='<!-- CAPACITY_CORE_SWAP_LATEST_BATCH_20261029 -->'
new_marker='<!-- INDUCED_K2_CURRENT_BATCH_20261029 -->'
gap_note=f'''{new_marker}
当前最高研究阶段已收束（root23:22:14 UTC）：[INDUCED16_K2_14总终态](../research/ddp/refresh_20261029/INDUCED16_K2_14_TURN_RESULT.json)／[实际推导与下一步依据](../research/ddp/refresh_20261029/INDUCED16_K2_14_TURN.md)。固定3000/16regular诱导图实际失败；四方向transversal整域排除，原2000下界及压缩closure外审PASS、3600加强仅本地；一般任意keep必要模型15CPU UNKNOWN。14D5 K2真实SAT反例产生512cuts后，明确用原剩余预算续同1188row模型；最终3calls UNKNOWN，累计58.2235solver/67.547291753wholeCPU，caps60/90未重置，stage2历史保留，0新图。一般induced/K2均未排，本批全部终态，不机械续预算或扩seed/order/helper数。专家包仍21:55快照，恢复以本批、当前brief/progress及Wiki为准。
'''
if new_marker not in gap:
    assert old_marker in gap
    gap=gap.replace(old_marker,screen(gap_note)+'\n\n'+old_marker,1)
gap=gap.replace('最新研究批次已收束（root22:34:04 UTC）','上一研究批次已收束（root22:34:04 UTC）',1)
gap_path.write_text(gap)
with (HERE/'INDUCED_K2_FINAL_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Final induced16/K2-14 synchronization after root23:22:14. SameK2batch call3 used originalremainingbudget: finalUNKNOWN3calls,58.2235solver/67.547291753wholeCPU,stage2preserved,0graphs. Generalinduced remainsUNKNOWN; staticreview2000 vs local3600 kept separate. Ledger374,104/4,confirmed103/3,Lean1 unchanged; expert21:55 snapshot retained.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==374
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key]==after[key]
assert sorted(p.name for p in (WIKI/'experiments').glob('*.md'))==experiment_names
assert sorted(p.name for p in (WIKI/'claims').glob('*.md'))==claim_names
assert all(p.read_bytes()==data for p,data in owned_before.items())
query=(WIKI/'query_pack.md').read_text()
assert len(query)<=8000 and 'INDUCED16_K2_14_TURN_RESULT.json' in query
receipt=dict(status='PASS_INDUCED_K2_ALL_TERMINAL_FINAL_QUERY_REBUILT',
    updated_UTC=NOW,root_state_update_UTC=ROOT_UPDATED,
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    final_query_rebuild_after_root_update_pending=False,query_chars=len(query),
    canonical_helper='aris_repo/tools/research_wiki.py',
    latest_batch='research/ddp/refresh_20261029/INDUCED16_K2_14_TURN_RESULT.json',
    updated_existing_ids=ids,record_count=374,
    K2_final_status='UNKNOWN_SOLVER_RETURN',K2_same_original_batch=True,
    K2_total_solver_calls=3,K2_resumed_solver_calls=1,
    K2_solver_CPU_seconds=58.2235,K2_whole_batch_CPU_seconds=67.547291753,
    K2_original_CPU_caps=[60,90],K2_budget_reset=False,
    K2_stage2_history_preserved=True,K2_hit=False,K2_error=None,
    F5_retention_status='UNKNOWN',F5_candidates=0,
    F5_review_scope='Original2000 bound and compressedclosure specification; later3600 onlylocal.',
    all_numerical_and_external_review_terminal=True,pending=[],
    new_experiments=0,new_methods=0,new_graphs=0,new_lower_bounds=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    root_and_expert_files_unchanged=True,expert_snapshot_preserved='21:55 UTC',
    helper_stdout=run.stdout.strip())
out=HERE/'INDUCED_K2_FINAL_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=374,query_chars=len(query),final_query='COMPLETE_AFTER_ROOT_STATE'),ensure_ascii=False))
