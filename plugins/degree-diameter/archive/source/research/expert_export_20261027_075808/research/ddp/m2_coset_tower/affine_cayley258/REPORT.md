# 258阶仿射群八度直径3完整检查终态

**固定群 $\mathbb F_{43}\rtimes_{37}C_6$ 上不存在八元逆闭非单位 Cayley 集合使直径至多3。** 完整支持链为35种相位模式 → 18种普通词容量通过 → 3种符号容量通过 → 74种四反射仿射轨道 → 全部404,114个合法代表的实际单根 BFS。保全证明见 [STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md)，不外推任意258点八度图。

## 实际完成范围

只剩两个逆对加四反射的三种模式。对每个反射轨道代表，两个逆对field各完整遍历43值，没有残余稳定子去重：

| 逆对相位 | 原始输入 | 实际非法 | 合法代表 / 完整 BFS |
|---|---:|---:|---:|
| `[0,1]` | 136,826 | 3,182 | 133,644 |
| `[0,2]` | 136,826 | 3,182 | 133,644 |
| `[1,2]` | 136,826 | 0 | 136,826 |
| 合计 | 410,478 | 6,364 | 404,114 |

每个合法代表使用真实群乘法表产生右 Cayley 邻居，并对根0 BFS 遍历到结束；没有在三步失败后截断评分。全部404,114个合法图都连通，没有直径3命中。左正则作用传递，因此单根完整距离谱精确决定全图直径。

终态为 `COMPLETE_NO_SOLUTION`，下一游标410,478，三模式各74轨道全部完成。逐项结果在 [production.cases.tsv](production.cases.tsv)；222个“模式/轨道”块的完成数、合法数、缺失直方图见 [production.terminal.json](production.terminal.json)。无在途作业，没有续种或追加群。

原先估算的10,500,603个项目代表没有运行；父代理明确授权四反射轨道规范后，实际运行的是上述410,478项范围，不能把二者都计作已完成搜索。

## 保存图

实际展开的404,114个合法代表中最小根三步缺失为15，有三项达到。**该最小值仅限实际展开范围；前序被容量排除的模式没有展开作最优分数比较。** 保存首个达到者：

```
cursor = 333029
source_pattern_id = 8
reflection_orbit_index = 32
pair_phases = [1,2]
pair_fields = [4,37]
reflection_fields = [0,1,3,19]
S = [47,230,123,208,129,130,132,148]  # x+43*j
```

保存图有258点、1032边、8正则、连通、直径4；根距离谱为 `[1,8,52,182,15]`，相对目标D3的坏无序点对为 $258\cdot15/2=1935$。完整边表和参数分别在 [production.best.edges](production.best.edges)、[production.best.json](production.best.json)。

父代理已完成该唯一保存图的独立最终验收：从真实群坐标重建的1032条边与文件完全相等；一次全部258根的通用 BFS 确认简单、连通、8正则、直径4、坏无序点对1935。全图有序距离谱 `[258,2064,13416,46956,3870]` 恰为保存根谱的258倍。独立 CPU 为 **0.004713864秒**（重建0.002123864秒、通用检查0.002590秒），没有检查其他图或重跑搜索。结果见 [best.independent_verify.json](best.independent_verify.json) 与 [production.best.independent_check.json](production.best.independent_check.json)，无验证待办。

## 成本和复现

两层容量计算 CPU 为0.026942657秒；反射轨道计算0.018388228秒。二者完整进程记录 CPU 合计0.130155秒，准备编译0.868833秒，实际图生产3.09381秒。包含以上任务和驱动的总记录 CPU 为 **4.095573秒**，低于原授权单worker 120秒上限。

复现入口是 [capacity.py](capacity.py)、[reflection_orbits.py](reflection_orbits.py)、[search_reflections.cpp](search_reflections.cpp) 和 [run_reflections.py](run_reflections.py)。前两步输出 [CAPACITY_RESULTS.json](CAPACITY_RESULTS.json)、[REFLECTION_ORBITS.json](REFLECTION_ORBITS.json)；[production.run.json](production.run.json) 保留PID、正常exit0、预算和完成游标。纯符号乘法复用已保存函数，没有重跑其他参数的筛选。

本批没有命中，没有新下界声明，也未查询或改写公开基线。
