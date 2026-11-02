#!/usr/bin/env python3
"""Summarize saved trajectories and reuse the exact same previously verified graph; no BFS."""
from pathlib import Path
import collections
import json
import time

base=Path(__file__).resolve().parent
start=time.process_time()
source=base.parent/'affine_cayley820_capacity'
def edges(path):
    data=list(map(int,path.read_text().split()));assert data[:2]==[820,4920]
    values=[tuple(sorted((u,v))) for u,v in zip(data[2::2],data[3::2])]
    assert len(values)==len(set(values))==4920
    return set(values)
assert edges(base/'production.best.edges')==edges(source/'profile.best.edges')
assert (source/'profile.best.independent_check.json').is_file()
verification={'saved_final_edges_exactly_equal_already_verified_source':True,'n':820,'m':4920,'source':'../affine_cayley820_capacity/profile.best.edges','source_independent_all_root_check':'../affine_cayley820_capacity/profile.best.independent_check.json','new_BFS_runs':0,'inherited_simple':True,'inherited_connected':True,'inherited_degree':12,'inherited_diameter':4,'inherited_bad_unordered_pairs':13940,'comparison_CPU_seconds':time.process_time()-start}
(base/'best.exact_reuse.json').write_text(json.dumps(verification,indent=2)+'\n')
terminal=json.loads((base/'terminal.json').read_text());run=json.loads((base/'run.json').read_text())
terminal['final_verification']={'status':'EXACT_SAME_SAVED_GRAPH_AS_PREVIOUS_INDEPENDENT_FINAL','file':'best.exact_reuse.json','new_BFS_runs':0};terminal['pending']=[]
(base/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
seeds=json.loads((base/'seeds.json').read_text())
results=[json.loads(line) for line in (base/'seed_results.jsonl').read_text().splitlines()]
rounds=[json.loads(line) for line in (base/'rounds.jsonl').read_text().splitlines()]
accepted=collections.Counter(row['accepted']['move_type'] for row in rounds if 'accepted' in row)
labels=['替换一个逆对','替换一个反射','一个逆对换两个反射','两个反射换一个逆对']
report='''# 820阶仿射Cayley：相位与组成移动的固定轨迹终态

**17个保存起点的授权轨迹全部完成，未命中直径3；最好根缺失仍为34。** 本次允许替换整个真实逆对、替换反射，以及逆对与两个反射相互转换，实际改变了相位和组成。它不是固定相位field坐标下降的重复执行，但仍只是固定起点的有限局部构造尝试，不排除整个820阶群。

群、真实元素池、必要相位过滤及每轮邻域计数证明见 [STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md)。实际池为389个非自逆逆对加41个反射；旧best与保存top16按实际S去重后得到17个不同起点，没有随机起点、扰动或重启。

## 完成范围与分类计数

17条轨迹全部在规定的**容量存活合法邻域**内无严格改善后停止，没有触及每轨迹30步上限。共完整扫描43个邻域，接受26次严格下降；每个已保存起点的初始分数均由本实现完整根BFS与旧值精确对齐。

| 邻域方向 | 合法邻点次数 | 必要容量剪枝 | 实际完整BFS | 接受的下降 |
|---|---:|---:|---:|---:|
'''
counts=terminal['neighbor_counts']
for index,label in enumerate(labels):
    report+=f"| {label} | {counts['legal_neighbors'][index]} | {counts['capacity_pruned'][index]} | {counts['actual_BFS_candidates'][index]} | {accepted[index]} |\n"
report+='''
合计278,782次合法邻点评估入口，其中130,118次由前序完整符号容量表排除，未执行BFS；其余148,664次执行完整单根BFS，加上17个起点校准，共 **148,681次实际完整根BFS**。这些是实际评估次数，不声称参数互异或图非同构。完整一轮的四类合法邻点计数均在程序中按当前逆对/反射数量核对。

必要容量剪枝保留所有可能D3图，却不保留所有较小的非零缺失。因此“无严格改善”只指过滤后的邻域，不能说每个轨迹已到整个合法邻域的局部最小；同样不能把容量被筛的邻点当作已经BFS验证过的图。

## 各保存起点的实际终态

| 本次seed | 输入来源 | 初始根缺失 | 最终根缺失 | 接受步数 | 终态逆对/反射数 |
|---:|---|---:|---:|---:|---|
'''
for row in results:
    k=row['seed_index'];c=row['current']
    report+=f"| {k} | {seeds[k]['source']} | {row['initial_missing']} | {c['root_missing']} | {row['accepted_moves']} | {c['pairs']}/{c['involutions']} |\n"
report+='''
原best（seed0）在第一次完整过滤后邻域扫描中没有严格改善。原top13（本次seed14）经两步也到达同一个实际生成集合。其余轨迹的具体接受参数、逐类计数与完整扫描状态见 [rounds.jsonl](rounds.jsonl)，各终态完整生成集合见 [seed_results.jsonl](seed_results.jsonl)。

## 唯一保存图与验收复用

只展开最终最好一张图，见 [production.best.edges](production.best.edges)、[production.best.json](production.best.json)。其真实S与旧best相同，仅生成元列表顺序不同：

```
S = [82,738,129,700,139,705,157,714,282,606,432,438]
encoding = x + 41*j
```

图为820点、4,920边、简单连通12正则、直径4；根谱 `[1,12,132,641,34]`，相对目标D3的坏无序点对为 `410*34=13940`。

最终保存文件的全部4,920条边直接与先前已独立全820根验收的源文件比较，**在相同标签下完全相等**，见 [best.exact_reuse.json](best.exact_reuse.json)。因此直接复用 [原唯一全源验收](../affine_cayley820_capacity/profile.best.independent_check.json)，不另跑全根BFS，没有新的保存图等待验收。

## CPU、源码与停止范围

'''
report+=f"准备/编译记录CPU {run['preparation_CPU_seconds']:.6f}秒，生产记录CPU {terminal['CPU_seconds']:.6f}秒，驱动记录总CPU **{run['total_recorded_CPU_seconds']:.6f}秒**，低于单worker累计180秒上限。驱动预留1秒是保守收尾储备，不冒充实测CPU；最终边集合只读比较另记录 {verification['comparison_CPU_seconds']:.6f}秒、0 BFS。\n\n"
report+='''终态 `COMPLETE_FIXED_TRAJECTORIES_NO_SOLUTION`，17/17起点、43次完整邻域扫描结束，无超时、运行任务或验收待办。代码为 [search.cpp](search.cpp)、[run.py](run.py)，全部原始起点与真实池见 [seeds.json](seeds.json)、[group_pools.json](group_pools.json)；计数及最后游标见 [terminal.json](terminal.json)、[run.json](run.json)。不追加起点、其他群或轨迹，没有新下界声明。
'''
(base/'REPORT.md').write_text(report)
print(json.dumps({'verification':verification,'accepted_moves_by_type':dict(accepted)},indent=2))
