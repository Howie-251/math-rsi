# AGL(1,17) 八度直径3有限检查终态

**固定群 $\mathbb F_{17}\rtimes_3 C_{16}$ 上不存在八元逆闭非单位 Cayley 集合使直径至多3。** 完整商容量筛选及共同仿射规范的保全证明见 [STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md)。这只关闭该272阶群的八度 Cayley 构造，不排除任意272点八度图，不构成新下界。

## 完整实际范围

495种逆对/对合相位模式中，42种“3逆对+2对合”和116种“4逆对”通过必要商容量。其余模式因至少一个17点原纤维的三步词容量不足而排除。通过模式共254,852个规范非零field代表，全部已处理：

| 组成 | 规范输入 | 实际非法 | 合法图 / 完整单根 BFS |
|---|---:|---:|---:|
| 3逆对 + 2对合 | 219,240 | 16,362 | 202,878 |
| 4逆对 | 35,612 | 1,476 | 34,136 |
| 合计 | 254,852 | 17,838 | 237,014 |

非法项仅因真实生成集合包含单位元或不足八个不同元素而拒绝。重复相位未被提前合并；相位0的两种逆对方向均完整保留。规范中的全零类另由16点补群断连排除，不混入表中计数。

每个合法集合实际构建272点的八个右乘邻居，根0 BFS 遍历到结束，无评分截断。左正则作用传递且保持右 Cayley 边，因此完整单根距离谱精确决定全图直径。全部237,014图均未达到直径3。

终态 `COMPLETE_NO_SOLUTION`，下一游标254,852，所有158种模式的完成数都等于各自5220或307项。逐项合法性和评分保存在 [production.cases.tsv](production.cases.tsv)；逐模式游标、合法数量和缺失直方图见 [production.terminal.json](production.terminal.json)。没有运行中作业，没有续种或重启。

## 保存的最小缺失图

实际展开的237,014个合法图中，最小根三步缺失为9，共两项达到。**这个最小值仅针对实际展开范围；商容量失败模式没有展开作最优分数比较。** 保存首个达到者：

```
cursor           = 169531
pattern_index    = 32
source_pattern_id= 138
projective_index = 2491
component_phases = [3,4,7,8,8]   # 前3槽为逆对，后2槽为对合
fields           = [0,1,9,10,8]
S                = [51,221,69,217,128,163,146,144]  # x + 17*j
```

保存图有272点、1088边、8正则、连通、直径4。根距离谱为 `[1,8,55,199,9]`，相对目标D3的坏无序点对为 $272\cdot9/2=1224$。完整边表与参数分别在 [production.best.edges](production.best.edges)、[production.best.json](production.best.json)。

父代理安排的该一张图的独立最终验收已完成：从真实群作用重建的1088条边与保存文件完全相等；一次全部272根的通用 BFS 确认简单、连通、8正则、直径4、坏无序点对1224。全图有序距离谱 `[272,2176,14960,54128,2448]` 恰为根谱的272倍。独立检查总 CPU **0.005613899秒**（重建0.002639899秒、通用检查0.002974秒），没有重跑枚举或检查其他图。结果见 [best.independent_verify.json](best.independent_verify.json) 和 [production.best.independent_check.json](production.best.independent_check.json)，无验证待办。

## 成本与文件

商词表枚举 CPU 为0.076162496秒，包含启动与写表的该进程记录 CPU 为0.115683秒。准备及编译记录 CPU 为1.105765秒；实际图生产 CPU 为2.54702秒。包含前序容量进程、准备编译、生产及驱动的总记录 CPU 为 **3.771149秒**，低于授权单worker 60秒上限。

代码 [quotient_capacity.py](quotient_capacity.py)、[search_projective.cpp](search_projective.cpp) 和 [run_projective.py](run_projective.py) 保留完整输入生成与执行方式。输入 [survivor_patterns.txt](survivor_patterns.txt) 保留原容量表ID；[production.run.json](production.run.json) 记录PID、正常exit0、总时间与结束状态。本批无命中，未查询或改写公开基线，未追加参数或搜索。
