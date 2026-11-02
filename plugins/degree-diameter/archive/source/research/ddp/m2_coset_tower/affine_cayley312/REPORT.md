# 312阶仿射直积群八度直径3完整检查

**固定群 $(\mathbb F_{13}\rtimes_2 C_{12})\times C_2$ 上不存在八元逆闭非单位 Cayley 集合使直径至多3。** 完整相位覆盖、真实对合/逆对分类和共同仿射规范证明见 [STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md)。这只排除此固定群的构造，不排除一般312点八度图，也不构成新下界。

## 完整实际范围

4,060个相位模式中370个通过逐商纤维的三步形式词容量条件。其余模式因某个13点纤维词数不足而排除。通过模式的252,258个规范非零field代表已全部处理：

| 逆对数 $p$ | 中心对合数 $c$ | 模式数 | 规范输入 | 实际非法 | 合法图 / 完整单根 BFS |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 20 | 47,600 | 3,660 | 43,940 |
| 3 | 0 | 64 | 152,320 | 9,150 | 143,170 |
| 3 | 1 | 102 | 18,666 | 336 | 18,330 |
| 4 | 0 | 184 | 33,672 | 672 | 33,000 |
| 合计 | | 370 | 252,258 | 13,818 | 238,440 |

非法项仅由实际生成集合中的单位元或重复元素产生。重复投影、相位为 $(0,1)$ 的非对合逆对、反射field零值都保留到真实元素检查。固定中心对合不占自由field坐标；规范中的全零类另由补群断连排除，不混入表中输入计数。

每个合法集合实际构建312点的八个右乘邻居，并运行到结束的根0 BFS，没有评分截断。左正则作用传递，所以单根完整距离谱精确决定全图直径。全部238,440个合法图都未达到直径3。

终态为 `COMPLETE_NO_SOLUTION`，下一游标252,258，所有370种模式完成其全部2380或183项。逐项结果在 [production.cases.tsv](production.cases.tsv)，逐模式完成数、合法数及根缺失直方图见 [production.terminal.json](production.terminal.json)。无运行中作业，无重启或续种。

## 保存图

实际展开的238,440个合法图中，最小根三步缺失为25，有四项达到。**这是实际展开范围的最小值；商容量已拒绝的模式没有展开作分数比较，不能将25称作整个群所有集合的最小缺失。**

保存首个达到者：

```
cursor           = 55702
pattern_index    = 38
source_pattern_id= 1655
projective_index = 414
pair_count       = 3
reflection_6_0   = 0
reflection_6_1   = 2
central_involution = 0
variable_phases  = [1,13,14,18,18]  # 相位编码 j+12*w
fields           = [0,1,11,5,2]
S                = [13,143,170,305,193,293,239,236]  # x+13*(j+12*w)
```

图有312点、1248边、8正则、连通、直径4；根距离谱为 `[1,8,56,222,25]`，相对目标D3的坏无序点对为 $312\cdot25/2=3900$。完整边表和参数在 [production.best.edges](production.best.edges)、[production.best.json](production.best.json)。

该唯一保存图的独立最终验收已完成：从真实群作用重建的1248条边与文件完全相等；一次全部312根的通用 BFS 确认简单、连通、8正则、直径4、坏无序点对3900。全图有序距离谱 `[312,2496,17472,69264,7800]` 恰为保存根谱的312倍。独立 CPU 共 **0.006707408秒**（重建0.003412408秒、通用检查0.003295秒），没有检查其他图。结果见 [best.independent_verify.json](best.independent_verify.json) 和 [production.best.independent_check.json](production.best.independent_check.json)，无验证待办。

另有独立的纯符号解释 [SYMBOLIC_WORD_BOUND.md](SYMBOLIC_WORD_BOUND.md)：对370个商容量通过模式按真实field线性形式去重，可提前排除其中358种，留下12种、28,560个规范输入。该解释没有被追溯计作本批前置筛选；上述252,258个原始代表与238,440次实际图 BFS 都是本批真实完成量，没有因此重跑或改写范围。

## 成本与范围边界

商词表计算 CPU 为0.251876549秒，其完整进程记录 CPU 为0.326557秒；准备编译记录 CPU 为1.102021秒；实际图生产 CPU 为3.78947秒。包含商容量进程、准备编译、生产及驱动的总记录 CPU 为 **5.220701秒**，低于授权单worker 120秒上限。

复现源码为 [quotient_capacity.py](quotient_capacity.py)、[search_projective.cpp](search_projective.cpp)、[run_projective.py](run_projective.py)。输入 [survivor_patterns.txt](survivor_patterns.txt) 保留原容量表ID与中心/反射组成；[production.run.json](production.run.json) 记录PID、正常exit0、结束游标及时间。

本批仅检查此群，未重跑272或330群，未追加参数、查询或改写公开基线。本批没有直径3命中。
