# χ17=6的规范四生成元族：216项全部未达D10

本轮只处理另一耦合χ17(alpha)=6，没有复用χ5的任何数值控制。216个规范设置全部实际生成新的Cayley邻接关系并作完整identity根BFS；全部simple四正则且连通，没有D≤10项，没有导出完整边表，预测REFUTED。

## 新群与等价范围

群阶20400，G=(F5²×C17)⋊H48，H=beta^u alpha^v，H乘法为(u+(-1)^v u',v+v')。模作用保留实际source矩阵

~~~
rho(alpha)=[[4,2],[1,1]], rho(beta)=[[0,4],[1,4]] overF5,
~~~

但C17作用换成chi17(alpha)=6、chi17(beta)=1。6是primitive16root，新的左群作用不要求是旧χ5图的自同构；本程序直接使用新半直积法则，没有把旧source的图验收当作新图验收。

[VALID耦合证明](../normalized_group_family/normalization_proof/FAITHFUL_C17_COUPLINGS.md) 确认：保持rho(alpha)²=3I时，alpha重标指数须为1 mod4，因此primitive16 characters分两类，以5和6=5³代表。本任务只算6，χ5的并行规范族由另一任务负责。

[PREDICTION.json](PREDICTION.json) 在新设置前冻结。采用同一已确认的归一化：

~~~
g=(V0,c0,alpha^a), a∈{1,3,5,7};
h=(v,c1,beta alpha^b), b∈{0,...,8};
v∈{(1,0),(1,1),(1,2),(1,3),(1,4),(0,1)}.
~~~

总4×9×6=216项，按a、b、v顺序全算，skip为空。覆盖范围及归一化依据见 [源归一化证明](../normalized_group_family/normalization_proof/PROOF.md)。没有添加其它χ、field或H phase。

## 真逆元与完整验收

新群乘法为

~~~
(V,c,h)*(W,d,k)=(V+rho(h)W,c+chi(h)d,h*k).
~~~

两个负生成元从每项新正生成元重新计算为(-rho(h^-1)V,-chi(h^-1)c,h^-1)，使用chi6而非旧chi5坐标。实际四个group IDs均不同且非identity；逆闭给无向simple四正则Cayley图。

每项完整identity BFS均访问全部20400点，所以全216项连通。Cayley左平移保持全部边并传递于根，identity偏心率即全图精确直径；没有重复全20400根，也没有重跑旧sourceBFS。

| 项目 | 实际值 |
| --- | ---: |
| 完整新设置 | 216 |
| 四逆闭生成元合法 | 216 |
| 连通及完整新根BFS | 216 |
| D11 / D12 / D13设置 | 122 / 92 / 2 |
| D≤10命中 | 0 |
| 完整edgefile导出 | 0 |
| χ5控制继承 | 0 |
| 未试 / UNKNOWN | 0 / 0 |
| native CPU秒 | 0.092164 |
| 编译CPU秒 | 0.807618 |
| 整批CPU秒 | 0.901910 |

最后cursor为a7、b8、line5。逐项参数及精确D记录在 [cases.tsv](cases.tsv)，没有选最小坏对、保存best失败图或据分数修边。family顶层actual_n/D及普通无序坏对为null；上表是216个参数的D分布，不是新图数或坏对数。

证据为 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)、[probe.cpp](probe.cpp)、[run.py](run.py)。已闭为这个χ6群的指定完整规范族，不外推任意20400点图或degree4/D10全局上界。按约停止，不追加χ、field、H phase或局部repair。
