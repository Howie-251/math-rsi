# q11/D8单控制：实际98736点Cayley图直径九

唯一控制已完成，未得到目标D8。实际图98736点、296208边、simple、无向、全六正则且连通；完整identity根BFS偏心率九。它是一个Cayley轨道，左平移保持全部边，所以全图实际直径恰九，不需要重跑98736个根。

## 固定来源与参数

继承实际source的H48及C17部分，使用debruijn已确认VALID的F11表示：

~~~
H=<alpha,beta | alpha16=beta3=1, alpha beta alpha^-1=beta^-1>;
rho(alpha)=[[7,5],[1,4]], rho(beta)=[[0,10],[1,10]];
chi17(alpha)=5, chi17(beta)=1.
~~~

alpha矩阵平方为−I，beta立方为I，且alpha将beta共轭成其逆。source H配方在 ../../h48_complement/SOURCE_SEMIDIRECT_RECIPE.json；本轮不重恢复H或旧source。

G=(F11²×C17)⋊H，共121×17×48=98736元素。三个正生成元固定为

~~~
A=(V(0,0),c0,beta0 alpha1);
B=(V(0,1),c1,beta1 alpha12);
C=(V(0,2),c5,beta2 alpha11).
~~~

保留source归一关系C_V=2B_V，区别于跨characteristic逐坐标centered表示。三个负生成元从新群inverse公式重新计算，未沿用旧F5逆向量。编码、field tables和完整规则见 [RECIPE.json](RECIPE.json)；六个正逆生成元实际ID为6171、92565、76241、29292、72622、36896。

[PREDICTION.json](PREDICTION.json) 在构图前冻结唯一控制D≤8的预测。实际邻接已逐点核simple、六邻及无向反边。

## 实际全根结论与计数类型

完整root0 BFS访问全部98736点，距离直方图为

~~~
[1,6,30,150,736,3568,15429,44655,33175,986].
~~~

R8尚漏986点，预测REFUTED。986仅为固定根的有向target数，没有填入全图普通无序坏对字段。actual_global_D=9来自Cayley左平移与完整根偏心率，不是把一般多轨道图的单根结果当全局。

native0.007772CPU秒，编译0.708841CPU秒，整批0.718620CPU秒。仅一个新根BFS，旧sourceBFS零；结果为 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)，实现为 [probe.cpp](probe.cpp)、[run.py](run.py)。失败图没有导出完整边表；recipe完整保留可复现。

按约停止此唯一q11控制，不扩q11参数或其它q。本case与原D7四表示/2625设置严格分开，不混入其计数。
