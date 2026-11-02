#!/usr/bin/env python3
"""Read-only final edge comparison and report; no extra BFS or search."""
from pathlib import Path
import json
import time

base=Path(__file__).resolve().parent
start=time.process_time()
def edges(path):
    data=list(map(int,path.read_text().split()));assert data[:2]==[172,602]
    rows=[tuple(sorted((u,v))) for u,v in zip(data[2::2],data[3::2])]
    assert len(rows)==len(set(rows))==602
    return set(rows)
assert edges(base/'best.edges')==edges(base.parent/'best.edges')
assert (base.parent/'best.independent_check.json').is_file()
verification={'status':'EXACT_REUSE_OF_PREVIOUS_INDEPENDENT_FULL_GRAPH_CHECK','source':'../best.edges','source_independent_check':'../best.independent_check.json','all_602_edges_identical_in_same_labels':True,'n':172,'degree':7,'diameter':4,'bad_unordered_pairs':258,'new_BFS_runs':0,'comparison_CPU_seconds':time.process_time()-start}
(base/'best.exact_reuse.json').write_text(json.dumps(verification,indent=2)+'\n')
terminal=json.loads((base/'terminal.json').read_text());run=json.loads((base/'run.json').read_text())
assert terminal['status']=='COMPLETE_TWO_COORDINATE_LOCAL_MINIMUM'
assert terminal['complete_rounds']==1 and terminal['accepted_strict_moves']==0
terminal['pending']=[];terminal['final_verification']={'status':verification['status'],'file':'best.exact_reuse.json','new_BFS_runs':0}
(base/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
report='''# 平衡3/2/2底图：完整双坐标邻域终态

**唯一已验最佳起点的完整两坐标邻域无严格改善。** 一轮全部97,020个原始槽完成，其中90,663个合法邻点均完整执行四根BFS，6,357个因平行边电压重复跳过。最小总缺失仍为12，因此立即停止，没有开启第二轮或新增扰动、起点、底图。

本次只说明该参数在规定的完整双坐标邻域内无更小分数，不排除其他电压参数或一般172点图。没有新下界图。

## 实际底图与唯一输入

使用当前平衡底图实际端点数组：

```
edge_u = [0,0,0,2,2,2,0,0,1,1,0,0,1,1]
edge_v = [1,1,1,3,3,3,2,2,3,3,3,3,2,2]
tree   = [0,6,10]
free   = [1,2,3,4,5,7,8,9,11,12,13]
seed   = [0,14,34,20,10,7,0,17,31,35,0,42,14,30]
```

这里树索引、自由边索引与旧4/2/1底图不同。准备时由seed展开的全部602条边与父目录保存文件精确相等；新评分器一次完整四根BFS得到预期缺失 `[2,5,3,2]`、总和12、直径4，该评分直接作为生产初值复用。见 [seed_edges_check.json](seed_edges_check.json)、[seed_calibration.json](seed_calibration.json)。

合法性、精确四轨道评分及邻域保全说明见 [SCOPE.md](SCOPE.md)。两条新电压**同时写入后**再检查同端点边互异，未误删交换同类两旧电压的合法槽。每轮55×42²=97,020槽；本底图六平行类的“总边数/自由数”为3/2、3/3、2/1、2/2、2/1、2/2，推出同类合法10,010、跨类合法80,653，合计90,663，非法6,357，实际完整轮计数全部吻合。

每个合法候选完整执行根0、43、86、129的BFS，不使用容量剪枝、深度截断或早退评分。整轮选择严格最佳改善，并列保留先遇到者；无改善即停。完整对象具有C43共同平移作用，故坏无序点对数精确为 `43*四根缺失和/2`。

## 实际结果

| 项目 | 数量 |
|---|---:|
| 固定起点 | 1 |
| 完整轮数 | 1 |
| 原始双坐标槽 | 97,020 |
| 非法平行边重复槽 | 6,357 |
| 合法邻点完整四根评分 | 90,663 |
| 含起点的实际评分次数 | 90,664 |
| 完整根BFS次数 | 362,656 |
| 接受的严格改善 | 0 |

这些是实际槽/评分次数，不声称参数互不同构；同平行类电压交换可表示同一图。完整一轮及末游标保存在 [rounds.jsonl](rounds.jsonl)、[terminal.json](terminal.json)。

唯一保存图 [best.edges](best.edges)、[best.json](best.json) 的电压未改变。其四根距离谱为

```
[1,7,42,120,2]
[1,7,42,117,5]
[1,7,42,119,3]
[1,7,42,120,2]
```

图简单连通、172点、602边、7正则、直径4，坏无序点对258。最终602边已与父目录已验图在同标签下直接比较，完全相同，见 [best.exact_reuse.json](best.exact_reuse.json)。因此复用 [原独立全172根验收](../best.independent_check.json)，没有额外全源BFS，也无新图等待验收。

## 成本与终态

'''
report+=f"准备/编译/源边比较记录CPU {run['preparation_CPU_seconds']:.6f}秒，生产记录CPU {terminal['CPU_seconds']:.6f}秒，驱动累计 **{run['total_recorded_CPU_seconds']:.6f} CPU秒**，低于单worker90秒上限。1秒收尾储备并非实测CPU；最终只读边集合比较另记录 {verification['comparison_CPU_seconds']:.6f}秒、0 BFS。\n\n"
report+='''终态 `COMPLETE_TWO_COORDINATE_LOCAL_MINIMUM`，正常退出，没有超时重启、在途任务或验收待办。代码为 [search.cpp](search.cpp)、[run.py](run.py)，实际成本见 [run.json](run.json)。所有新文件均在本子目录，未修改父目录报告或共享代码。

按本轮范围到此停止，不追加三坐标、其他种子或底图；现有结果保留供下一阶段整体决策。
'''
(base/'REPORT.md').write_text(report)
print(json.dumps(verification,indent=2))
