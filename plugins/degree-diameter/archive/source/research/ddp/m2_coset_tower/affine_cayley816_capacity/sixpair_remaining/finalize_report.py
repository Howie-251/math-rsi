#!/usr/bin/env python3
from pathlib import Path
import json
import time

start=time.process_time();here=Path(__file__).resolve().parent
run=json.loads((here/'run.json').read_text())
assert not run['running'] and run['exit_code']==0
t=json.loads((here/'terminal.json').read_text());meta=json.loads((here/'metadata.json').read_text())
c=t['counts'];calibrations=[json.loads(s)for s in (here/'prefix_calibration.jsonl').read_text().splitlines()]
assert c['processed_marked_inputs']==c['legal_marked_inputs']+c['illegal_marked_inputs']
assert sum(c['fiber_rejections_in_test_order'])+c['full_root_BFS']==c['legal_marked_inputs']
assert all(r['all48_equal'] and r['actual_masks']==r['symbolic_masks']for r in calibrations)
assert sum(r['counts']['processed_marked_inputs']for r in t['per_pattern'])==t['processed_inputs']
if not t['saved_best_graph']:assert not list(here.glob('production.best.*'))
partial=[r for r in t['per_pattern']if 0<r['counts']['processed_marked_inputs']<r['scope']]
next_position=t['next_position']
next_input=None
if next_position is not None:
    with (here/'inputs.jsonl').open()as handle:
        for index,line in enumerate(handle):
            if index==next_position['pattern_index']:
                next_input=json.loads(line);break
    z=[0]*5;lead=next_position['lead'];z[lead]=1;code=next_position['prefix_code']
    for k in range(3,lead,-1):z[k]=code%17;code//=17
    z[4]=next_position['last_coordinate']
    next_input['next_z']=z
summary={'status':t['status'],'running':False,'scope_patterns':50680,'scope_marked_inputs':4497393880,'patterns_complete':t['patterns_completed'],'partial_patterns':partial,'processed_marked_inputs':t['processed_inputs'],'remaining_marked_inputs':4497393880-t['processed_inputs'],'legal_marked_inputs':c['legal_marked_inputs'],'illegal_marked_inputs':c['illegal_marked_inputs'],'actual_full_root_BFS':t['actual_full_root_BFS'],'saved_graph':t['saved_best_graph'],'first_failed_fiber_position_histogram':c['fiber_rejections_in_test_order'],'next_position':next_position,'next_input':next_input,'symbolic_modes_prepared':t['symbolic_modes_prepared'],'symbolic_preparation_CPU_seconds':t['symbolic_preparation_CPU_seconds'],'production_CPU_seconds':t['CPU_seconds'],'recorded_run_CPU_seconds':run['total_recorded_CPU_seconds'],'prefix_mask_calibrations':len(calibrations),'all_prefix_masks_equal':True,'old48_modes_repeated':0,'five_or_four_pair_modes_processed':0}
if t['status']=='COMPLETE_REMAINING_SIXPAIR_SCOPE_NO_SOLUTION':
    summary['combined_complete_sixpair_symbolic_patterns']=50728
    summary['combined_complete_sixpair_marked_inputs']=4497393880+4259568
    summary['combined_complete_sixpair_legal_inputs']=c['legal_marked_inputs']+4259568
first_fail='、'.join(f'第{i+1}个：{x:,}'for i,x in enumerate(c['fiber_rejections_in_test_order'])if x)
remaining=summary['remaining_marked_inputs']
if next_position is None:
    continuation='没有未处理cursor，本批完整结束。'
else:
    continuation=f"下一未处理位置为模式index {next_position['pattern_index']}、source cursor {next_input['source_cursor']}、lead {next_position['lead']}、prefix {next_position['prefix_code']}、末坐标 {next_position['last_coordinate']}，模式内索引 {next_position['local_projective_index']}、全局索引 {next_position['global_index']}；对应z={next_input['next_z']}。该输入尚未执行。"
closure=''
if t['status']=='COMPLETE_REMAINING_SIXPAIR_SCOPE_NO_SOLUTION':
    closure='加上此前已完整执行、此次严格排除的48个maximin模式，全部50,728个符号存活六逆对模式、4,501,653,448个标记参数现均已完成而无D3。此为选定群F17 ⋊_3 C48的六逆对范围，不能外推五逆对/四逆对分支或一般816点图。'
report=f'''# 816点剩余六逆对：实际终态

终态`{t['status']}`，进程exit0、已停止、无重启。授权50,680模式共4,497,393,880项，实际完成{t['patterns_completed']:,}个完整模式，执行{t['processed_inputs']:,}个标记参数，余{remaining:,}项。

真实合法生成元{c['legal_marked_inputs']:,}项，非法{c['illegal_marked_inputs']:,}项；全部48纤维通过后触发完整根BFS {t['actual_full_root_BFS']}次，保存图={t['saved_best_graph']}。没有通过者时没有另外生成诊断图。

{continuation}

{closure}

每模式由C++即时生成全部约化三步形式，原48个去重数与保存capacity逐项相等；删除真正的非单位action锚后再次去重，未改变各纤维形式数。只在五维剩余field中作一次射影规范。生成元实际12元素的identity/重复检查在所有fiber测试之前，保留phase0、phase16和同phase多组件。

正式前缀共{len(calibrations)}次实际群短词集合与符号取值集合校准，全部48mask逐点相等；均在生产cursor内，无额外候选或BFS。各输入首次失败位置的拒绝数为：{first_fail}。这些计数是首次失败位置分类；不是第一纤维单独拒绝全部，也不代表所有模式共享同一phase。

准备/编译CPU {run['preparation_CPU_seconds']:.9f}秒；C++累计CPU {t['CPU_seconds']:.9f}秒，其中逐模式符号准备{t['symbolic_preparation_CPU_seconds']:.9f}秒已包含；driver记录总CPU（含source准备）{run['total_recorded_CPU_seconds']:.9f}秒，wall {run['wall_seconds']:.9f}秒。单worker、600秒上限、无进程重启。

完整输入次序/原48容量在`inputs.jsonl`，排除的旧48 cursor在`metadata.json`。真实进程终态在`run.json`，各模式的执行量、各首次失败位置以及精确下一位置在`terminal.json`；简表与下一field坐标在`summary.json`。代码为`run.py`、`search.cpp`。本次未触碰五逆对或四逆对分支。
'''
(here/'REPORT.md').write_text(report)
summary['report_generation_CPU_seconds']=time.process_time()-start
summary['total_CPU_including_report_seconds']=run['total_recorded_CPU_seconds']+summary['report_generation_CPU_seconds']
(here/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:summary[k]for k in ('status','patterns_complete','processed_marked_inputs','remaining_marked_inputs','legal_marked_inputs','illegal_marked_inputs','actual_full_root_BFS','saved_graph','recorded_run_CPU_seconds','report_generation_CPU_seconds','total_CPU_including_report_seconds')},indent=2))
