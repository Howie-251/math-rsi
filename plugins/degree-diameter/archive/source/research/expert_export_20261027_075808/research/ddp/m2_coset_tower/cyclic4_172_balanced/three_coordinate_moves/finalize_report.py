#!/usr/bin/env python3
"""Summarize terminal artifacts and compare final edges; no BFS or search."""
from pathlib import Path
import json
import time

base=Path(__file__).resolve().parent
terminal=json.loads((base/'terminal.json').read_text());run=json.loads((base/'run.json').read_text())
assert not terminal['running'] and not run['running'] and run['exit_code']==0
best=json.loads((base/'best.json').read_text());rows=[json.loads(line)for line in (base/'rounds.jsonl').read_text().splitlines()]
start=time.process_time()
def edges(path):
    data=list(map(int,path.read_text().split()));assert data[:2]==[172,602]
    values=[tuple(sorted(pair))for pair in zip(data[2::2],data[3::2])]
    assert len(values)==len(set(values))==602
    return set(values)
equal=edges(base/'best.edges')==edges(base.parent/'best.edges')
verification={'saved_final_edges_equal_original_in_same_labels':equal,'n':172,'m':602,'new_BFS_runs':0,'comparison_CPU_seconds':time.process_time()-start}
if equal:
    assert (base.parent/'best.independent_check.json').is_file()
    verification.update(status='EXACT_REUSE_OF_PREVIOUS_INDEPENDENT_FULL_GRAPH_CHECK',source_edges='../best.edges',source_independent_check='../best.independent_check.json',diameter=4,bad_unordered_pairs=258)
    terminal['pending']=[]
else:
    verification['status']='NEW_SAVED_GRAPH_PARENT_INDEPENDENT_FINAL_PENDING'
    terminal['pending']=['parent-owned unique independent final check of best.edges']
(base/'best.edge_comparison.json').write_text(json.dumps(verification,indent=2)+'\n')
terminal['final_verification']={'status':verification['status'],'file':'best.edge_comparison.json','new_BFS_runs':0}
(base/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
score=terminal['best_score']
if terminal['status']=='COMPLETE_THREE_COORDINATE_LOCAL_MINIMUM':
    opening='完整三坐标邻域扫描结束于无严格改善，已按规则停止。'
elif terminal['status']=='CPU_LIMIT_PREFIX_SAVED':
    opening='在累计预算内完成已保存前缀，最后一轮未完整，不能声称达到三坐标局部最小。'
elif terminal['status']=='FOUND_D3':
    opening='实际四根完整BFS发现目标D3候选，已立即停止并保存；等待父代理唯一独立全源验收。'
else:
    opening='达到五个完整轮的固定上限，已保存实际最好候选；没有继续追加轮次。'
report=f'''# 平衡3/2/2底图：三坐标邻域终态

**{opening}** 实际最佳四根缺失和为{score['score_sum']}，坏无序点对{score['bad_unordered_pairs']}，直径{score['diameter']}。此次只有一个固定起点，没有随机扰动、新起点、其他底图或原双坐标范围重跑。

本次是完整三坐标邻域上的有限下降轨迹，不是十一维电压族穷举。任何局部停止结论都不能外推固定底图全族或一般172点图。

## 范围与评分

完整定义、规范、合法邻点解析计数及预算规则见 [SCOPE.md](SCOPE.md)。唯一起点为父目录已独立全172根验收的best，电压

```
[0,14,34,20,10,7,0,17,31,35,0,42,14,30]
```

树边 `[0,6,10]` 固定为0，自由边 `[1,2,3,4,5,7,8,9,11,12,13]`。源602边重建相等，起点四根缺失 `[2,5,3,2]`、总和12的完整校准直接复用为正式初始评分，见 [seed_edges_check.json](seed_edges_check.json)、[seed_calibration.json](seed_calibration.json)。

每轮选三条自由边，每个新值都不同于当前值；**同时赋三值后**统一检查平行边互异。每个合法候选完整执行四根BFS，无容量剪枝、深度截断或提前评分。共同C43平移保证坏点对计数等于43乘四根缺失和再除2。本次每完整轮为 `C(11,3)*42^3=12,224,520` 原始槽。

解析合法计数为11,088,102、非法1,136,418；其中三坐标分属三类合法7,559,252，2+1分组合法3,459,848，三坐标同类合法69,002。所有实际完整轮都核对此常数，见 [neighborhood_counts.json](neighborhood_counts.json)。参数换位可能表示相同图，所以评估次数不声称是不同图或同构类数。

## 实际轨迹和计数

| 轮 | 邻域完整 | 原始槽 | 非法槽 | 合法四根评分 | 轮初总缺失 | 本轮最好总缺失 | 停止/动作 |
|---:|---|---:|---:|---:|---:|---:|---|
'''
for row in rows:
    report+=f"| {row['round']} | {'是' if row['complete_neighborhood'] else '否'} | {row['raw_slots']:,} | {row['illegal_parallel_collisions']:,} | {row['legal_candidates_scored']:,} | {row['initial_score']} | {row['best_neighbor_score']} | {row['stop']} |\n"
report+=f'''
合计处理 **{terminal['raw_neighbor_slots']:,}** 个原始槽，其中非法 **{terminal['illegal_parallel_collisions']:,}**、合法邻点完整评分 **{terminal['actual_legal_neighbor_BFS_candidates']:,}**。加起点校准共 **{terminal['total_legal_candidates_scored_including_seed']:,}** 个候选、**{terminal['complete_root_BFS_runs']:,}** 次完整根BFS。完成{terminal['complete_rounds']}轮，接受{terminal['accepted_strict_moves']}次严格改善。

整轮的选择是严格最佳改善，等分不接受。若预算中断某轮，暂存最好邻点只是该轮已评分前缀中的最好值，不能当作已完成全邻域最佳选择。逐轮实际参数、完整标志及成本保存在 [rounds.jsonl](rounds.jsonl)，最后位置与当前/暂存状态在 [terminal.json](terminal.json)。

## 唯一保存图

完整边表及参数为 [best.edges](best.edges)、[best.json](best.json)。最终电压是

```
{best['voltages']}
```

四根缺失 `{score['root_misses']}`，总和{score['score_sum']}，坏无序点对{score['bad_unordered_pairs']}；图172点、602边、7正则，实际四根完整评分直径{score['diameter']}。

'''
if equal:
    report+='保存文件的602条边与父目录已验源图在相同标签下完全相等，见 [best.edge_comparison.json](best.edge_comparison.json)。因此复用 [原独立全172根验收](../best.independent_check.json)，没有重复全源BFS，没有新的最终验收待办。\n\n'
else:
    report+='保存边集合不同于源图。该实际新best交父代理安排唯一独立全源验收，本代理不重复或提前自行全源检查；当前待办仅这一张保存图。边集合比较记录见 [best.edge_comparison.json](best.edge_comparison.json)。\n\n'
report+=f'''## 成本与停止

准备、编译及源边比较记录CPU {run['preparation_CPU_seconds']:.6f}秒；生产记录CPU {terminal['CPU_seconds']:.6f}秒；驱动累计 **{run['total_recorded_CPU_seconds']:.6f} CPU秒**，单worker预算300秒。1秒保守收尾储备不计作实测CPU；最后只读边集合比较另记录 {verification['comparison_CPU_seconds']:.6f}秒、0 BFS。

终态 `{terminal['status']}`，正常退出，无自动重启或在途搜索。源码为 [search.cpp](search.cpp)、[run.py](run.py)，实际运行记录 [run.json](run.json)、[search.log](search.log)。全部产物仅在本子目录，不修改父目录或旧双坐标结果。不因局部失败而追加种子、底图或轮次。
'''
(base/'REPORT.md').write_text(report)
print(json.dumps({'status':terminal['status'],'best_score':score,'verification':verification,'pending':terminal['pending']},indent=2))
