# Loz 3243 的实际三轨道配方与唯一 F139 控制

恢复了原 3243 点源的完整电压配方；唯一冻结的 9591 点迁移控制未达到 D9。新图实际简单、连通、4 正则，首轨道根偏心率 10、R9 漏 245 点后即停止；没有检查另外两个轨道根，不能把偏心率 10 写作全局直径。

## 实际来源与配方

[Comellas 官方 D8 说明](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g8.html) 列出 Eyal Loz 于 2006 年 7 月提供的 3243 点图。取其 [官方 raw 邻接](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD8/Loz_3243.txt) 一次，文件 86376 字节；3243 行显式 1-based 标签，每行 4 个邻点。实际统计为 3243/6486，全 4 正则，简单且无向。没有重跑源图 BFS。官方 [Sage 结果](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD8/3243_loz_SageMath.txt) 给出 D8、girth10、Aut=C47:C23，阶 1081，非 Cayley、非点传递；这些距离/自同构事实继承原公开结果。

从 literal 的编号恢复群坐标：

~~~text
G = F47 semidirect C23, |G|=1081
(x,y)*(a,c) = (x+a mod23, y+6^x*c mod47)
vertex = base*1081 + x + 23*y, base=0,1,2.
~~~

6 在模 47 下精确 23 阶。三个底点形成 K3，0→1、0→2 电压为单位元，1→2 为 (4,45)；三个底点各有一条双向 loop，其正向电压依次为 (3,8)、(11,2)、(6,35)。全部反向电压由此群法取真实群逆。该恢复配方与原 literal 的全部 12972 条有向边逐项吻合，见 [SOURCE_FACTS](SOURCE_FACTS.json)；并非从 3243 的因数猜群。源检查 CPU 0.019697199 秒，不包含网络等待。

每个底点纤维有群的左乘 deck 作用。这个作用保留上述右乘邻接，故形成三个 1081 点轨道；与公开自同构结果一致，无需重新恢复大型 Aut。

## 两个相近操作已有严格障碍

保留全部旧边添加新点的固定度数操作被实际全 4 正则直接阻断，没有旧 free port。另继承官方 girth10 后，源的任何非平凡 ordinary graph cover 都不能有直径至多 9：长度至多 9 的投影闭路全部自由约化为空，因此其 lift 回到原 sheet，不能到达同一源顶点之上的另一个点。这个论证关闭的是原 3243 图的 ordinary covers。

本次改变 F47→F139 的电压族不是原 3243 图的 ordinary cover，阶数比 139/47 也不是整数；不能套用上述 cover 障碍。此前旧 1344 源的固定投影路线阻碍亦不能代替此源的分析。

## 唯一受控迁移：实际失败与边界

保留 quotient C23、全部 phase、三个底点与边类型，取 p139、r6；6 在模 139 也精确 23 阶。固定原场内电压的 centered 整数代表：loop translations 为 8、2、−12，cross1→2 为 −2；这是一条明确选择的 controlled rule，不是原作者已证明的通用公式。n=3×23×139=9591，目标 (4,9) 超过本轮给定基线 7884。

源 phase quotient 的长度至多 9 非回退词精确计数为每根 39365；三个根的最薄槽分别有 533/510/528 条，均大于 139。容量通过仅为必要条件。事前预测是这个唯一控制的全部三个轨道根 R9 均覆盖。新群中两条 loop 的 commutator normal translation 为 7，故能生成 F139；phase3 生成 C23，两个单位元 cross 连接底点，由此有连通依据。

实际完整生成新邻接，检查简单、无向、全 4 正则，首根 0 完整 BFS 到达全部 9591 点，偏心率 10，R9 漏 245 点，预测被推翻。首个未覆盖点为 69=(base0,phase0,field3)，完整最短路：

~~~text
0—187—1570—2332—8726—5157—5836—4836—1639—256—69
~~~

CPU 0.026808571 秒，编译为 0。仅这一个新图、一次完整新图根 BFS；另外两个轨道根未查，global D 为空、只知至少 10。245 是指定根的缺点数，不是普通无序坏对数。失败图边表没有导出；没有旧源 BFS，也没有其它 r、offset、prime 或自由参数试验。固定控制到此结束，不能由此排除其它电压选择或一般 (4,9) 图。

证据：[冻结预测](PREDICTION.json)、[新图配方](CONTROL_RECIPE.json)、[新图结果](CONTROL_RESULT.json)、[phase 容量](PHASE_RAW_COUNTS.json)、[源恢复程序](source_analysis.py)、[唯一控制程序](run_control139.py)。
