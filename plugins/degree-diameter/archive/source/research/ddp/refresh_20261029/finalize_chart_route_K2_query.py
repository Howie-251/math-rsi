"""Finish the previous mathematical turn's recovery/query sync, without research."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib
import importlib.util
import json

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
ROOT_UPDATED='2026-10-30 01:52:40 UTC'


def module(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'aris_repo/tools'/(name+'.py'))
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


helper,capture=module('research_wiki'),module('capture_filter')


def screen(text):
    assert not capture.screen(text),capture.screen(text)
    return text


ledger_path=WIKI/'DDP_METHOD_LEDGER.json'
ledger_before=ledger_path.read_bytes()
ledger=json.loads(ledger_before)
assert ledger['record_count']==len(ledger['rows'])==377
assert ledger['validated_graph_examples_including_novelty_pending']==104
assert ledger['validated_parameter_pairs_including_novelty_pending']==4
assert ledger['confirmed_publictable_graph_examples']==103
assert ledger['confirmed_publictable_improved_parameter_pairs']==3
assert ledger['complete_Lean_graph_instances']==1
turn=json.loads((HERE/'CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json').read_text())
assert turn['status']=='CHART_ROUTE_AND_D14_D15_BATCHES_COMPLETE_NO_NEW_GRAPH'
assert turn['all_started_numeric_batches_terminal'] is True and turn['Goal_status']=='ACTIVE'
brief=(ROOT/'RESEARCH_BRIEF.md').read_text()
assert '2026-10-30 01:52:40 UTC' in brief and 'CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json' in brief
goalpath=ROOT/'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md'
goal=goalpath.read_text()
assert '同一 Goal 为 ACTIVE' in goal[:800]
assert 'D=2' in goal
for path in [ROOT/'AGENTS.md',ROOT/'context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md']:
    s=path.read_text()[:7500]
    assert '2026-10-30 01:52:40 UTC' in s and 'CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json' in s
current={
    'ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029':'FULL_ALLGROUP_FULLTARGET_INTEGER_UNKNOWN_FRACTIONAL_FEASIBLE',
    'ddp-c21-fano-flag-uniform100-affine-plane-deletion-route-obstruction-16d3-20261030':'PAPER_EXCLUDED_SPECIFIED_C21_UNIFORM100_RULE_STATIC_REVIEW_SUPPORTED',
    'ddp-f5-fiber80-two-type-normal-scaling-chart-rigidity-16d3-20261030':'PAPER_FRAMEWORK_N_AT_MOST24_STATIC_REVIEW_SUPPORTED_C25_SOLVER_STOPPED',
    'ddp-d15-d4-literal15552-all648-k2-cooperative-cover-20261030':'FULL_ALL648_LITERALPORT_FULL15552_TARGET_K2_UNKNOWN'}
rows={r['id']:r for r in ledger['rows']}
assert all(rows[identifier]['status']==status for identifier,status in current.items())
comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- CHART_ROUTE_K2_TRANSFER_FINAL_QUERY_20261030 -->'
note=f'''
## {NOW} 上轮chart／14、15度K2最终恢复同步

root01:52:40的[当前总终态](../research/ddp/refresh_20261029/CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json)与[解释](../research/ddp/refresh_20261029/CHART_ROUTE_K2_TRANSFER_TURN.md)已进入唯一恢复入口和最终query。14度全部3589组/94186双侧target模型UNKNOWN，charged390.163813与measuredlower303.579242分列，不能把缺失prepare selfCPU填成精确总计。15度全部648literalports/15552双侧targets模型UNKNOWN，120.009668solver/121.957097678wholeCPU，0候选/图，两者均停但未排。

C21指定uniform100规则及S80两type normal-scaling框架N≤24的paper障碍均已实际外审SUCCESS/SOUND，C25必要模型0solver、停止启动；不外推一般16度。旧3750源任意诱导max16/n≥1921/D3的LRAT计算排除继续继承。全部已启数值终态，无假RUN或新研究派发。

有效Goal文件声明同一Goal ACTIVE，旧D2暂停；本子代理未持独立Goal，也未create/reset。ledger377是实验／来源记录而非方法数；合法104/4、confirmed103/3、具体公式Lean1及3750最新全球纪录pending口径一致。原root/专家文件未改，无数值重跑；当前用户请求的新专家稿由root另行撰写，就绪后再同步真实交付入口。
'''
if marker not in comments.read_text():
    with comments.open('a') as out:out.write('\n\n'+marker+'\n'+screen(note))
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
assert '账本现377条实验／来源记录' in gap[:1800]
latest_marker='<!-- CHART_ROUTE_K2_TRANSFER_CURRENT_20261030 -->'
latest='''<!-- CHART_ROUTE_K2_TRANSFER_CURRENT_20261030 -->
当前研究批次已终态（root01:52:40 UTC）：[总索引](../research/ddp/refresh_20261029/CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json)／[推导与判断](../research/ddp/refresh_20261029/CHART_ROUTE_K2_TRANSFER_TURN.md)。14度K2已恢复全部3589组/94186双侧targets，唯一完整模型UNKNOWN，不排K2，charged390.163813与measuredlower303.579242不混同。新C21指定uniform100机制及S80两type normal-scaling框架N≤24/order≤1920均paper排除且实际GeminiSOUND，C25必要CNF仅prepare、0solver，不是UNSAT。15度15552源all648literalports完整K2也UNKNOWN，0候选/图。全部已启数值终态，不自动续timer/seed；旧3750诱导LRAT排除继承，一般N(16,3)与整数K2未排。Goal ACTIVE、D2暂停；377记录、104/4、confirmed103/3、Lean1保持。新专家稿由root独立撰写，未就绪前不冒交付完成。

'''
if latest_marker not in gap:
    anchor='<!-- INDUCED16_CERTIFIED_CURRENT_20261030 -->'
    assert anchor in gap
    gap=gap.replace(anchor,screen(latest)+anchor,1)
gap=gap.replace('当前两线均已收束（root00:50:11 UTC）',
    '历史阶段两线收束（root00:50:11 UTC；当前读上方01:52总索引）',1)
gap_path.write_text(screen(gap))
with (HERE/'CHART_ROUTE_K2_TRANSFER_FINAL_WIKI_HELPER.log').open('w') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Completed previousmathturnfinalquery afterroot01:52:40. Fourcurrentrowsreadback:14allgroupUNKNOWN,C21uniform100paperexcluded,S80frame<=1920paperexcluded/C25unrun,15all648K2UNKNOWN. Ledger377,1044,confirmed1033,Lean1;effectiveGoalACTIVE/D2paused. No newGoal/research/root/expertedit. Newexpertdeliveryentryawaitsactualreadyfiles.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))
assert ledger_path.read_bytes()==ledger_before
query=(WIKI/'query_pack.md').read_text()
assert len(query)<=8000 and 'CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json' in query
assert '账本现377' in query
receipt=dict(status='PASS_CHART_ROUTE_K2_TRANSFER_FINAL_INDEX_QUERY_REBUILT',
    updated_UTC=NOW,root_state_update_UTC=ROOT_UPDATED,record_count=377,
    latest_batch='research/ddp/refresh_20261029/CHART_ROUTE_K2_TRANSFER_TURN_RESULT.json',
    actual_current_experiment_statuses=current,
    all_started_numeric_batches_terminal=True,effective_Goal_file=str(goalpath.relative_to(ROOT)),
    project_Goal_status_from_effective_file='ACTIVE',old_D2='PAUSED',
    child_independent_Goal_created=False,new_research_started=False,
    ledger_unchanged=True,new_experiments=0,new_methods=0,new_graphs=0,
    valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    latest_20D3_global_novelty='PENDING',root_or_expert_files_modified=False,
    new_expert_document_root_owned_not_yet_recorded_ready=True,
    canonical_helper='aris_repo/tools/research_wiki.py',query_chars=len(query),
    final_query_rebuilt_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    final_query_rebuild_after_root_update_pending=False)
out=HERE/'CHART_ROUTE_K2_TRANSFER_FINAL_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=377,query_chars=len(query)),ensure_ascii=False))
