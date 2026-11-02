# AGL(1,19) 八度直径3：唯一剩余相位模式完整检查

**结合前序完整相位分类和符号容量排除，固定群 $\mathbb F_{19}\rtimes_2 C_{18}$ 上不存在八元逆闭非单位 Cayley 集合使直径至多3。** 本批完整检查最后一个模式的381个规范代表，均失败。381项本身只覆盖该模式；完整群结论依赖下述保存的715模式排除链，不外推一般342点八度图。

## 完整范围的来源

前序参数与保全证明见 [axis_parameter_capacity/REPORT.md](../axis_parameter_capacity/REPORT.md)。实际使用的根为 $r=2$，已核其在 $\mathbb F_{19}^*$ 中阶为18，且 $2^9=-1$。乘法与逆元为

\[
(x,j)(y,k)=(x+2^j y,j+k),\qquad
(x,j)^{-1}=(-2^{-j}x,-j).
\]

19个非单位对合均为相位9；非对合逆对相位类为0至8，其中相位0有9个平移逆对，其余各19对。完整八元逆闭组成的相位多重集数为

\[
\sum_{p=0}^4\binom{p+8}{p}=\binom{13}{4}=715.
\]

前序实际排除链为：

| 阶段 | 检查范围 | 通过数 | 保存依据 |
|---|---:|---:|---|
| 逐商相位形式词容量至少19 | 全部715模式 | 100 | [agl19_d8.patterns.json](../axis_parameter_capacity/agl19_d8.patterns.json) |
| 逐商相位不同field线性形式至少19 | 前序100模式 | 1 | [agl19_d8.symbolic_patterns.json](../axis_parameter_capacity/agl19_d8.symbolic_patterns.json) |
| 实际原图完整单根 BFS | 唯一模式的381规范代表 | 0 | 本批 [production.terminal.json](production.terminal.json) |

汇总见 [CAPACITY_RESULTS.json](../axis_parameter_capacity/CAPACITY_RESULTS.json) 与 [SYMBOLIC_CAPACITY_RESULTS.json](../axis_parameter_capacity/SYMBOLIC_CAPACITY_RESULTS.json)。前两阶段没有实际field赋值或图搜索，本批没有重新运行它们。

符号排除的必要性是：固定相位及每个组件的field变量后，每个短词的field坐标是模19线性形式；同相位同系数向量对所有赋值都相等。因此不同形式数小于19时，不可能覆盖该19点纤维。形式数足够仍不保证具体赋值覆盖，故最后阶段必须检查实际图。

## 唯一模式及381项规范

保存的唯一模式为 [agl19_d8.symbolic_survivors.json](../axis_parameter_capacity/agl19_d8.symbolic_survivors.json) 中原ID543：四个非对合逆对，相位代表 `[2,3,4,8]`，没有对合。

普通 Cayley 图允许共同仿射自同构

\[
(x,j)\longmapsto(\lambda x+(1-2^j)t,j),\qquad\lambda\ne0.
\]

以相位2槽为锚，因 $1-2^2=-3\ne0$，先平移使其field坐标为0，再共同缩放使其余三个坐标按槽顺序的首个非零值为1。全零向量只生成18点补群内的子群，不能连通342点图。故完整保全代表为

\[
\mathbb P^2(\mathbb F_{19}),\qquad19^2+19+1=381.
\]

四个逆对相位类互异且均非零，所有381项自动给出八个互异非单位生成元；实现仍实际检查该条件。没有增加相位置换、逆对方向或field半区约束。

## 实际执行与保存图

[search_projective.py](search_projective.py) 读取上述唯一存活文件，核实际根阶18、全部342个元素的两侧逆元，随后依次枚举381个规范向量。每项构建完整342点八邻接表，并将根0 BFS 跑到结束，无评分截断。Cayley 图的左正则作用传递，故单根完整距离谱精确给出全图直径。

381项全部合法，全部检查，无直径3命中。终态 `COMPLETE_NO_SOLUTION`，下一游标381；逐项field坐标与分数在 [production.cases.tsv](production.cases.tsv)，无在途进程。

实际381项中唯一最小根三步缺失为46，保存代表索引52：

```
phases = [2,3,4,8]
fields = [0,1,14,2]
S      = [38,304,58,292,90,277,154,194]  # x+19*j
```

图有342点、1368边、8正则、连通、直径4，根距离谱 `[1,8,56,231,46]`，相对目标D3坏无序点对 $342\cdot46/2=7866$。边表和参数见 [production.best.edges](production.best.edges)、[production.best.json](production.best.json)。**46仅是本批实际381项的最小值；前序已排除但未展开的模式没有参与最优分数比较。**

父代理已完成该一张保存图的唯一独立最终验收：从真实坐标重建的1368条边与文件完全相等；一次全部342根的通用 BFS 确认简单、连通、8正则、直径4、相对D3坏无序点对7866。全图有序距离谱 `[342,2736,19152,79002,15732]` 恰为保存根谱的342倍。独立 CPU 为 **0.007248110秒**（重建0.003364110秒、通用检查0.003884秒），没有搜索或检查其他图。结果见 [best.independent_verify.json](best.independent_verify.json) 和 [production.best.independent_check.json](production.best.independent_check.json)，无验证待办。

## 成本与结论边界

本批完整算法记录 CPU **0.276537242秒**，包含进程准备的记录 CPU **0.311653秒**，低于授权单worker 30秒。未编译C++，未扩大参数，也未重跑715模式筛选或272/312/330群。进程与预算记录见 [production.run.json](production.run.json)。

完整固定群结论由“715模式保全 → 两个必要容量筛 → 唯一相位模式的381项完整实际检查”共同支持，没有直径3命中或新下界声明。
