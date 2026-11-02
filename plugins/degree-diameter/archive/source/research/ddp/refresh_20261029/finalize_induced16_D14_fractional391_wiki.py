"""Finalize the fixed-source16 exclusion and actual fractional/391 K2 outcomes."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib
import copy
import importlib.util
import json
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ROOT_UPDATED='2026-10-30 00:50:11 UTC'


def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'aris_repo/tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


helper,capture=module('research_wiki'),module('capture_filter')


def screen(text):
    assert not capture.screen(text),capture.screen(text)
    return text


folder=HERE/'d14_K2_fractional_support391'
integer=json.loads((folder/'SOLVER_TERMINAL.json').read_text())
fractional=json.loads((HERE/'d14_K2_fractional_capacity/RESCALING_RESULT.json').read_text())
turn=json.loads((HERE/'INDUCED_GEOMETRIC_TURN_RESULT.json').read_text())
assert integer['status']=='UNKNOWN' and integer['returncode']==0 and integer['actual_solver_calls']==1
assert integer['running'] is False and integer['pending']==[]
assert integer['observation_timeouts']==24 and integer['same_PID_waited_to_exit'] is True
assert integer['graphs_generated']==integer['source_graph_reads']==integer['BFS_runs']==0
assert fractional['status']=='EXACT_GLOBAL_FRACTIONAL_WITNESS_VERIFIED'
assert fractional['sum_numerator']==24136823828 and fractional['positive_groups']==391
assert turn['all_started_numeric_batches_terminal'] is True
owned=[ROOT/'AGENTS.md',ROOT/'RESEARCH_BRIEF.md',
    ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md',ROOT/'research/progress.html',
    ROOT/'expert_review_current/EXPERT_HANDOFF_20261029.md',
    ROOT/'expert_review_current/build_handoff_20261029.py']
owned_before={p:p.read_bytes() for p in owned}
brief=(ROOT/'RESEARCH_BRIEF.md').read_text()
current_brief=brief.split('<!-- REFRESH_20261029_CURRENT_END -->',1)[0]
root_update=re.search(r'更新(2026-10-30 \d{2}:\d{2}:\d{2} UTC)',current_brief)
assert root_update and root_update.group(1)>='2026-10-30 00:50:11 UTC'
ROOT_UPDATED=root_update.group(1)
assert 'INDUCED_GEOMETRIC_TURN_RESULT.json' in current_brief and '120.016794' in current_brief
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows'])==374
ids=['ddp-f5-literal3750-induced-retention-max16-d3-20261029',
     'ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029']
old={r['id']:r for r in before['rows']}
rows={key:copy.deepcopy(old[key]['source_record']) for key in ids}
experiment_names=sorted(p.name for p in (WIKI/'experiments').glob('*.md'))
claim_names=sorted(p.name for p in (WIKI/'claims').glob('*.md'))
f5=rows[ids[0]]
assert f5['other_metrics']['fixed_source_induced_n_at_least1921_computationally_excluded'] is True
assert f5['other_metrics']['exact_CNF_LRAT_verified'] is True
assert f5['other_metrics']['negative_16_Lean'] is False
f5['other_metrics']['latest_research_root_update_UTC']=ROOT_UPDATED
f5['other_metrics']['all_started_numeric_batches_terminal']=True
f5['unclosed_gap']='本固定3750源的全部任意诱导n≥1921/max16/D3范围已计算排除并停止；不是一般N(16,3)上界，负结论未Lean。uniform75保平面chart局部障碍未外审。14度分数完整松弛精确可行而整数仍未知，实际391受限pool已UNKNOWN终态，见同K2聚合行。'
k2=rows[ids[1]]
variants={v['label']:v for v in k2['variants']}
label='exact_fractional_positive391_pool_full_target_integer_single_call_20261030'
v=variants[label]
v.update(
    status='UNKNOWN_TERMINAL',running=False,terminal_result_recorded=True,
    solver_returncode=0,actual_solver_calls=1,
    solver_CPU_seconds=integer['solver_CPU_seconds'],
    whole_CPU_seconds=integer['whole_CPU_seconds'],
    observation_timeouts=24,same_PID_waited_to_exit=True,
    observation_timeouts_were_not_solver_restarts=True,
    SAT_candidates=0,graphs_generated=0,source_graph_reads=0,BFS_runs=0,
    automatic_continuation=False,pending=[],
    restricted391_pool_excluded=False,allK2_excluded=False,
    final_result='research/ddp/refresh_20261029/d14_K2_fractional_support391/SOLVER_TERMINAL.json',
    final_decision='research/ddp/refresh_20261029/d14_K2_fractional_support391/FINAL_DECISION.md',
    independent_literal_validator_source_only=True,
    independent_literal_validator_compiled=False,
    independent_literal_validator_read_graph_or_run=False)
k2['variants']=list(variants.values())
k2['outcome_class']='INTEGER_K2_UNRESOLVED_RESTRICTED391_UNKNOWN_FRACTIONAL_FEASIBLE'
k2['failure_or_result']='全94186target的标准分数覆盖有精确有理可行向量，总24.136823828<26、391正组、每侧12.068411914，最终读RESCALING_RESULT；不是LP最优或整数存在声明。以其391支撑生成的额外受限整数模型10948vars/209323clauses完整覆盖188372两侧行（精确去重187858），唯一-t120返回UNKNOWN/code0，120.016794solver/124.059995631wholeCPU，24次观察超时均等待同一PID，0SAT/候选/图。该池与allK2均未排，本批停止，最终读SOLVER_TERMINAL而非preparedMODEL或旧LPRESULT。'
k2['other_metrics'].update(
    current_numerical_status='INTEGER_K2_UNRESOLVED_RESTRICTED391_UNKNOWN_FRACTIONAL_FEASIBLE',
    current_running=False,restricted391_terminal_recorded=True,
    restricted391_status='UNKNOWN',restricted391_actual_solver_calls=1,
    restricted391_solver_CPU_seconds=integer['solver_CPU_seconds'],
    restricted391_whole_CPU_seconds=integer['whole_CPU_seconds'],
    restricted391_observation_timeouts=24,restricted391_same_PID_waited_to_exit=True,
    restricted391_SAT_candidates=0,restricted391_graphs=0,
    restricted391_pool_excluded=False,fixed_K2_family_excluded=False,
    restricted391_automatic_continuation=False,
    restricted391_independent_literal_validator_source_only=True,
    restricted391_independent_literal_validator_compiled_or_run=False,
    current_fractional_result='RESCALING_RESULT.json',
    current_integer_result='SOLVER_TERMINAL.json',
    all_started_numeric_batches_terminal=True,
    latest_research_root_update_UTC=ROOT_UPDATED)
k2['lesson_and_restart_condition']='完整有理分数可行证据排除了标准分数容量dual>26作为阻断；其391支撑给出了数据驱动的不同整数生成池，并实际建成完整target模型，而非续旧1188行CEGIS。唯一调用UNKNOWN无候选，说明本批未决定整数兼容性，不能称该池或allK2无解。停止该池批次，不自动续timer/seed/换池；后续需具体新的整数连接/兼容问题，而不能仅凭分数可行或未成功授权无限搜索。'
k2['restart_condition']='This391restrictedpoolbatchisterminalUNKNOWN;noautomaticcontinuation. A new run requires a concrete new integer connection/compatibility question. It is not a lossless allK2 reduction.'
k2['unclosed_gap']='全部3589等价组的整数K2存在性仍UNKNOWN；391额外受限pool亦只UNKNOWN，均未排。分数全94186目标已精确可行，不证明LP最优或整数可行。没有候选，所以独立literal验收器仅源码，未编译/读图/执行。全部已启动数值均终态，无后台待收项。'
paths=[str(p.relative_to(ROOT)) for p in sorted(folder.iterdir())
    if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'}]
k2['report_paths']=list(dict.fromkeys(k2['report_paths']+paths))
turnpaths=['research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json',
           'research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN.md']
for row in rows.values():
    row['report_paths']=list(dict.fromkeys(row['report_paths']+turnpaths))
    assert all((ROOT/p).exists() for p in row['report_paths'])
    screen(json.dumps(row,ensure_ascii=False))
pending=HERE/'INDUCED16_D14_FRACTIONAL391_FINAL_WIKI_ROWS.json'
pending.write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- INDUCED16_D14_FRACTIONAL391_FINAL_20261030 -->'
note=f'''
## {NOW} 固定16源排除与14度分数／整数诊断全部终态

root00:50:11原状态及[当前总终态](../research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json)已更新。16度固定3750源全部任意诱导n≥1921/max16/D3计算排除、LRAT及图→CNF链完整；不是一般N(16,3)上界，负结论未Lean，停止该源删点范围。

14度[RESCALING_RESULT](../research/ddp/refresh_20261029/d14_K2_fractional_capacity/RESCALING_RESULT.json)才是完整分数结论：24.136823828<26、391正组、每侧12.068411914，全94186行精确通过；旧三轮LP RESULT/TERMINAL是历史阶段。391支撑额外受限整数pool的[SOLVER_TERMINAL](../research/ddp/refresh_20261029/d14_K2_fractional_support391/SOLVER_TERMINAL.json)为唯一调用UNKNOWN/code0，120.016794solver/124.059995631wholeCPU；24次观察超时均等待同一PID，不是重启。0SAT/候选/图，不能排该pool或allK2；prepared MODEL不覆盖真实终态，未运行独立literal验收器。

本批依[FINAL_DECISION](../research/ddp/refresh_20261029/d14_K2_fractional_support391/FINAL_DECISION.md)停止，不自动加时/seed/换池。全部已启动数值终态，无待收项。ledger374、104/4、confirmed103/3、Lean1保持；专家23:55冻结不重包。最后canonical index/query在root00:50:11后重建，Goal仍ACTIVE，旧D2继续暂停。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:out.write('\n\n'+marker+'\n'+screen(note))
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
assert '账本现374条实验／来源记录' in gap[:1800]
start=gap.index('<!-- INDUCED16_CERTIFIED_CURRENT_20261030 -->')
end=gap.index('<!-- EXPERT_HANDOFF_2355_CURRENT_DELIVERY_20261029 -->',start)
current='''<!-- INDUCED16_CERTIFIED_CURRENT_20261030 -->
当前两线均已收束（root00:50:11 UTC）：[总终态](../research/ddp/refresh_20261029/INDUCED_GEOMETRIC_TURN_RESULT.json)。固定已验3750源的任意诱导n≥1921/max16/D3全域已由[图→CNF链](../research/ddp/refresh_20261029/f5_induced_same_fiber_model/EXCLUSION_SCOPE.md)、75000邻接绑定及LRAT VERIFIED计算排除，不限wholefiber/均匀/恰1921；仅排固定源，不是一般N(16,3)上界，负结论未Lean。14K2分数最终读RESCALING_RESULT：全94186target精确可行24.136823828<26，每侧12.068411914，非最优/整数存在声明。391正组是额外受限整数pool，其完整target单call最终SOLVER_TERMINAL为UNKNOWN，120.016794solver/124.059995631wholeCPU、0候选/图；既不排该pool也不排allK2，不从preparedMODEL恢复假RUN。两批均停，无后台待收项；专家23:55冻结不重包，374与104/4、confirmed103/3、Lean1保持。


'''
gap=gap[:start]+screen(current)+gap[end:]
gap_path.write_text(gap)
with (HERE/'INDUCED16_D14_FRACTIONAL391_FINAL_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Finalroot00:50:11sync:fixedsource16LRAT-backedexclusionretained;D14exactfractionalRESCALINGfeasibleandrestricted391integerSOLVER_TERMINALUNKNOWNonecall120.016794/124.059995631CPU,24samePIDobservationtimeouts,0candidates/graphs;literalvalidator sourceonly. Allstartednumericterminal. Ledger374/1044/confirmed1033/Lean1 unchanged;expert23:55frozen;finalcanonicalindex/queryrebuilt.')
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
assert len(query)<=8000 and 'INDUCED_GEOMETRIC_TURN_RESULT.json' in query
assert '24.136823828' in query and 'SOLVER_TERMINAL' in query
receipt=dict(status='PASS_INDUCED16_D14_FRACTIONAL391_ALL_TERMINAL_FINAL_QUERY_REBUILT',
    updated_UTC=NOW,root_state_update_UTC=ROOT_UPDATED,record_count=374,
    existing_ids=ids,fixed_source16_computationally_excluded=True,
    generalN16_upper_bound_claimed=False,negative16_Lean=False,
    D14_exact_fractional_final='RESCALING_RESULT.json',
    D14_restricted391_integer_final='SOLVER_TERMINAL.json',
    D14_restricted391_status='UNKNOWN',D14_restricted391_actual_solver_calls=1,
    D14_restricted391_solver_CPU_seconds=integer['solver_CPU_seconds'],
    D14_restricted391_whole_CPU_seconds=integer['whole_CPU_seconds'],
    D14_observation_timeouts=24,same_PID_waited_to_exit=True,
    D14_pool_or_allK2_excluded=False,independent_literal_validator_compiled_or_run=False,
    all_started_numeric_batches_terminal=True,pending=[],
    new_experiments=0,new_methods=0,new_graphs=0,new_Lean_instances=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    expert_snapshot_preserved='2026-10-29 23:55 UTC',root_and_expert_files_unchanged=True,
    canonical_helper='aris_repo/tools/research_wiki.py',query_chars=len(query),
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    final_query_rebuild_after_root_update_pending=False,helper_stdout=run.stdout.strip())
out=HERE/'INDUCED16_D14_FRACTIONAL391_FINAL_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=374,query_chars=len(query),final_query='COMPLETE_AFTER_ROOT_STATE'),ensure_ascii=False))
