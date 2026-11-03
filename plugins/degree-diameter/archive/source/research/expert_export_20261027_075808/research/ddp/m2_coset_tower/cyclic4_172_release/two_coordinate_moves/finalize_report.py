#!/usr/bin/env python3
"""Summarize the saved run and compare final edges, without further BFS."""
from pathlib import Path
import json
import time

base=Path(__file__).resolve().parent
start=time.process_time()
def read_edges(path):
    data=list(map(int,path.read_text().split()));assert data[:2]==[172,602]
    rows=[tuple(sorted((u,v))) for u,v in zip(data[2::2],data[3::2])]
    assert len(rows)==len(set(rows))==602
    return set(rows)
assert read_edges(base/'best.edges')==read_edges(base.parent/'best.edges')
assert (base.parent/'best.independent_check.json').is_file()
verification={'status':'EXACT_REUSE_OF_PREVIOUS_INDEPENDENT_FULL_GRAPH_CHECK','all_602_edges_identical_in_same_labels':True,'source_edges':'../best.edges','source_independent_check':'../best.independent_check.json','n':172,'degree':7,'diameter':4,'bad_unordered_pairs':387,'new_BFS_runs':0,'comparison_CPU_seconds':time.process_time()-start}
(base/'best.exact_reuse.json').write_text(json.dumps(verification,indent=2)+'\n')
terminal=json.loads((base/'terminal.json').read_text());run=json.loads((base/'run.json').read_text())
assert terminal['status']=='COMPLETE_TWO_COORDINATE_LOCAL_MINIMUM'
assert terminal['complete_rounds']==1 and terminal['accepted_strict_moves']==0
terminal['final_verification']={'status':verification['status'],'file':'best.exact_reuse.json','new_BFS_runs':0};terminal['pending']=[]
(base/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
report='''# 172点C43四轨道塔：完整两坐标邻域终态

**唯一已验最佳起点的完整两坐标邻域没有严格改善。** 第0轮完整扫描97,020个原始槽，其中87,597个合法候选全部完成四个轨道代表根BFS、9,423个因平行边电压重复被拒绝。最小总缺失仍为18，故按既定规则停止，没有开启第二轮、添加随机起点或扰动。

这表明当前参数在所指定的完整两坐标邻域内无更小分数，不排除固定底图上的其他参数，也不排除一般172点图。本次没有新下界图。

## 固定对象和起点

沿用 [原构造推导](../DERIVATION.md) 的四点底图、C43电压和14条无向基边。基边0至13的端点分别为四条01、四条23、两条02、两条13、一条03和一条12。顶点编码为 `43*orbit+x`；电压v使 `(a,x)` 与 `(b,x+v)` 相邻，反向电压为−v。

三条树边0、8、12保持电压0；自由边为

```
[1,2,3,4,5,6,7,9,10,11,13]
```

唯一固定起点就是前一批已经独立全172根验收的最佳图：

```
voltages = [0,12,33,30,11,37,16,31,0,7,15,39,0,11]
root misses = [4,1,10,3]
score sum = 18
```

准备阶段按该电压重建全部602条边，与原保存文件精确一致，见 [seed_edges_check.json](seed_edges_check.json)。新评分器只做一次起点四根完整BFS，所得四根缺失和直径与保存值一致，该结果直接作为生产初始评分，见 [seed_calibration.json](seed_calibration.json)。

同时平移所有轨道的field坐标保持边，并在每个43点轨道上传递。因此四个根0、43、86、129的完整BFS足以精确评分全图；坏无序点对数为 `43*score_sum/2`。每个合法电压表都产生简单172点、602边、7正则图。

## 完整两坐标邻域

从11条自由边中选无序不同两条，各改成与当前值不同的42个field值，共

\[
\binom{11}{2}42^2=97,020
\]

个原始槽。**先同时写入两条新电压，再检查全部同端点基边电压互异**。因此同一平行类里互换两旧电压的合法槽也保留，不能因第一条中间赋值暂时相撞而误删。

若两坐标分属不同大小为n、m的平行类，合法数为 `(43−n)(43−m)`。若属于同一个大小为n的平行类，每条新值允许 `44−n` 种，二者共有 `43−n` 个可碰撞相同值，所以合法数为 `(44−n)^2−(43−n)`。

参与的五个平行类“总边数/自由边数”为 `4/3,4/4,2/1,2/2,1/1`。同类两坐标合法槽15,772，跨类合法槽71,825，合计 **87,597**；非法槽为 **9,423**。完整轮的三个实际计数在程序中与这些解析值核对一致。

遍历顺序为自由边索引对递增、第一新值递增、第二新值递增。每个合法候选均完整完成四根BFS，无容量剪枝、距离截断或提前评分返回。整轮选分数严格最小的改善者，等分不接受，并列优先首次遇到者；若无严格改善则停止。授权上限为20轮或90 CPU秒，本次第一轮已满足停止条件。

同一底图电压表可能因同类边交换而对应同一完整图，因此评估次数不声称是非同构图数量。

## 实际终态与保存图

| 项目 | 实际数 |
|---|---:|
| 固定起点 | 1 |
| 完整轮数 | 1 |
| 原始两坐标槽 | 97,020 |
| 非法平行边重复槽 | 9,423 |
| 合法邻点完整评分 | 87,597 |
| 含起点的完整评分次数 | 87,598 |
| 完整根BFS次数 | 350,392 |
| 接受的严格改善 | 0 |

唯一最终保存图见 [best.edges](best.edges)、[best.json](best.json)，电压与起点完全相同。图简单连通、7正则、直径4，四根谱分别为

```
[1,7,42,118,4]
[1,7,42,121,1]
[1,7,42,112,10]
[1,7,42,119,3]
```

总缺失18，对应387个坏无序点对。最终保存文件再次与已验起点作同标签下的精确602边集合比较，全部相等，见 [best.exact_reuse.json](best.exact_reuse.json)。因此复用 [原独立全根验收](../best.independent_check.json)，没有另跑全根BFS或新增最终验收待办。

## CPU、游标及代码

'''
report+=f"准备/编译/边比较记录CPU {run['preparation_CPU_seconds']:.6f}秒，生产记录CPU {terminal['CPU_seconds']:.6f}秒，驱动记录总CPU **{run['total_recorded_CPU_seconds']:.6f}秒**，低于共用90秒预算。1秒收尾储备不是实测CPU；最终只读边集合比较另记录 {verification['comparison_CPU_seconds']:.6f}秒、0 BFS。\n\n"
report+='''终态 `COMPLETE_TWO_COORDINATE_LOCAL_MINIMUM`，正常退出，无超时重启、运行任务或待验事项。完整一轮轨迹及计数在 [rounds.jsonl](rounds.jsonl)，末位置和终态在 [terminal.json](terminal.json)、[run.json](run.json)。源码 [search.cpp](search.cpp) 复用原版的完整建图/四根BFS逻辑，并独立实现本批两坐标邻域；驱动为 [run.py](run.py)。所有新产物仅在本子目录，原release报告与共享源文件未修改。
'''
(base/'REPORT.md').write_text(report)
print(json.dumps(verification,indent=2))
