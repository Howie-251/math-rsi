#!/usr/bin/env python3
"""Read saved artifacts, compare final edges under the known relabel, write report; no BFS."""
from pathlib import Path
import json
import time

base=Path(__file__).resolve().parent
start=time.process_time()
def edges(path,relabel=False):
    data=list(map(int,path.read_text().split()));assert data[:2]==[820,4920]
    def f(a):return (a//41%2)*410+a%41+41*(a//82) if relabel else a
    out=[tuple(sorted((f(a),f(b)))) for a,b in zip(data[2::2],data[3::2])]
    assert len(out)==4920 and len(set(out))==4920
    return set(out)
assert edges(base/'profile.best.edges')==edges(base.parent/'affine_cayley820_capacity/profile.best.edges',True)
assert (base.parent/'affine_cayley820_capacity/profile.best.independent_check.json').is_file()
verification={'saved_final_edges_equal_relabelled_independently_checked_source':True,'edge_count':4920,'source':'../affine_cayley820_capacity/profile.best.edges','source_all_root_verification':'../affine_cayley820_capacity/profile.best.independent_check.json','relabel':'old(x,j) -> (j%2,x,j//2)','no_additional_BFS':True,'inherited_n':820,'inherited_degree':12,'inherited_diameter':4,'inherited_bad_unordered_pairs':13940,'comparison_CPU_seconds':time.process_time()-start}
(base/'best.relabel_verify.json').write_text(json.dumps(verification,indent=2)+'\n')
terminal=json.loads((base/'profile.terminal.json').read_text())
terminal['final_verification']={'status':'EXACT_RELABEL_OF_ALREADY_INDEPENDENTLY_VERIFIED_GRAPH','file':'best.relabel_verify.json','new_BFS_runs':0}
terminal['pending']=[]
(base/'profile.terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
rows=[json.loads(line) for line in (base/'profile.seed_results.jsonl').read_text().splitlines()]
run=json.loads((base/'profile.run.json').read_text())
report='''# 820点双轨道固定profile终态

**原seed加32个随机起点的授权范围已完整结束，无直径3命中。** 解除两侧内部集合及跨电压的原Cayley约束后，本次固定尝试的最好两根总缺失仍为68，没有改善原图。此结论只针对实际执行的有限profile，不排除整个固定相位族。

完整构造、合法性、两根评分证明和源图拆分见 [STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md)。固定随机种子为2026102624，14坐标不再额外规范化。

## 实际完成范围

- 33个起点全部完成：源seed一个、随机合法seed32个；随机seed共43次抽取。
- 297个下降段全部完成，每个起点的初始下降加8次双坐标扰动后下降；全部到达规定单坐标邻域的局部最小，没有触及30步上限。
- 双坐标扰动共275次抽取，得到264次合法扰动；接受869次严格下降。
- 实际评分634,601个候选，包含一个源seed校准、32个随机起点评分、264个扰动起点评分及634,304个合法单坐标邻点评分。
- 每个候选完整遍历两代表根，共1,269,202次完整根BFS；另18,656个非法单坐标邻点跳过。没有三步早退或截断评分。

同一候选可能沿不同轨迹再次被检查，因此634,601是实际评估次数，不声称是互不同构图或不同参数的数量。所有297段都扫描了完整合法单坐标邻域后停止，未耗尽预算、未中断或重启。

## 唯一保存图与校准

最终最好参数恰为原seed，没有变化：

```
A fields = [0,36,28,22]         # phases 1,3,5,5
B fields = [0,25,24,13]         # phases 1,3,5,5
T fields = [34,6,16,17,3,8]     # phases 1,1,1,8,8,8
```

两根谱均为 `[1,12,132,641,34]`，总缺失68。全图820点、4,920边、简单连通12正则、直径4，距大于3的坏无序点对为 `205*68=13940`。32个随机seed各自最佳段末分数中的最小值为73；这不改变全profile最佳68。

保存图见 [profile.best.edges](profile.best.edges) 和 [profile.best.json](profile.best.json)。源图全部4,920边到双轨道坐标的精确重标号在准备阶段核对通过，完整两根评分校准也通过，分别见 [calibration.edges.json](calibration.edges.json)、[calibration.roots.json](calibration.roots.json)。

最终文件又直接与**已独立完整820根验收过的源图**作精确边集合重标号比较，全部相等，见 [best.relabel_verify.json](best.relabel_verify.json)。因此保存图的全源验收结果由这一次精确同构直接继承；没有重复跑全820根BFS，也没有新的图等待验收。原唯一全源验收记录见 [源图检查](../affine_cayley820_capacity/profile.best.independent_check.json)。

## 各起点结果

| seed | 初始两根总缺失 | 本seed最终最好缺失 |
|---:|---:|---:|
'''
for row in rows:
    report+=f"| {row['seed_index']} | {row['initial_score']} | {row['best_candidate']['score']} |\n"
report+='''
每个seed均完整完成9段。全部初始坐标见 [profile.seeds.json](profile.seeds.json)，297段的初末坐标、实际邻点次数与停止原因见 [profile.segments.jsonl](profile.segments.jsonl)，每seed的最终参数见 [profile.seed_results.jsonl](profile.seed_results.jsonl)。

## CPU与终态

'''
report+=f"准备/编译/边校准记录CPU {run['preparation_CPU_seconds']:.6f}秒，生产记录CPU {terminal['CPU_seconds']:.4f}秒，驱动记录总CPU **{run['total_recorded_CPU_seconds']:.6f}秒**，低于共用120秒预算。驱动预留的1秒是保守收尾额度，并非额外实测CPU。最终只读边集合比较另记录 {verification['comparison_CPU_seconds']:.6f}秒；没有增加图搜索。\n\n"
report+='''终态 `COMPLETE_FIXED_PROFILE_NO_SOLUTION`，33/33起点、297/297段完成，无运行任务和验收待办。源码及驱动为 [profile.cpp](profile.cpp)、[run_profile.py](run_profile.py)，完整计数与终态见 [profile.terminal.json](profile.terminal.json)、[profile.run.json](profile.run.json)。不追加seed、相位或其他群；没有新下界声明。
'''
(base/'REPORT.md').write_text(report)
print(json.dumps(verification,indent=2))
