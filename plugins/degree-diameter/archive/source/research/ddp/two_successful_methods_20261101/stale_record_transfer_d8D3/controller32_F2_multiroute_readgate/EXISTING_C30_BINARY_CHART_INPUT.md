# 已存最佳binary chart与实际C30：字面输入绑定

实际见证已定位，无需重枚197568：`breadth_20261027_wave5/binary_route_chart3/best_candidate.json` 是旧遍历按编码顺序遇到的首个28/36候选；`best.independent_check.json` 已对该单见证核36词和全部inverse关系。本轮只复制它们的既有常数，不重算矩阵、rank、word、chart或图。

## 四port的字面F2输入

向量code是x0+2*x1+4*x2；矩阵以三**列**的binary codes保存，不能当三行。一步T_p作用为按输入bit异或对应列。

|port p|符号|matrix column codes|实际forward offset v_p|bar(p)|
|---|---|---|---|---|
|0|A|[4,2,1]|1|1|
|1|A inverse|[4,2,1]|4|0|
|2|B|[5,1,2]|6|3|
|3|B inverse|[2,4,3]|7|2|

旧best fields为A_index0、B_index25、v_A1、v_B6；`b_codes=[1,4,6,7]` 是**实际正向偏移**，不是原F5 directions字段的同名位置。

原成功F5 `refresh_20261029/f5_full_d20_D3/generate.py` 第27–31行使用

`(u,x) -> (C[u][p], T_p*x + lambda*directions[bar(p)])`。

若复用这种接口，必须令 `directions[bar(p)]=v_p`，因此这份binary chart的direction codes应为 `[4,1,7,6]`。这是四个已存v的逆port索引重命名，没有做新矩阵计算。也可直接把上表v_p当forward offset，避免间接directions命名。原F5的e1/e2/e3/(1,1,1)不能原样误套本binary chart，更不能逐系数mod2原F5矩阵来猜inverse。

## 实际controller字段与可冻结pair

原 `refresh_20261029/f5_full_d20_D3/PARAMETERS.json` 的字段名确为 `controller`（30×4）、`inverse_ports=[1,0,3,2]`、`directions`、`matrices`；`source_controller` 指向原Mizuno construction。附属JSON完整复制了30×4controller，不生成新图或controller，也未改变行内port顺序。

只冻结一个最简单的已有相邻pair：**0→18**，理由是原controller0的第一port，非按覆盖评分选。

- `C[0]=[18,20,2,9]`，所以port0直达18；
- `C[18]=[2,0,29,4]`，反向port1直回0。

这只是字面adjacency绑定，未枚其余≤3路线。**是否存在多个路线、是否没有单条满rank路线、各source x的union是否全八点，全部待root实际计算；此处不预设。** C30本身及这个pair也没有被当作所有controller的对称代表。

使用binary数据的typed步应明确为

`(u,xcode)->(C[u][p], T_p(xcode) XOR(lambda*v_p)), lambda=0/1`。

条件label可写 `8*u+x0+2*x1+4*x2`。这只是C30/q2的240点局部校准输入，不是新纪录，不是实际240图已验证；目标256仍需另有C32，当前没有选择或生成它。

旧28/36最优并不保证AAA满rank（旧报告明确该首best未过AAA），更不提供某controllerpair的多route证书。后续若root授权一个packet，应收该pair所有真实≤3词、含shorter routes；未经fiber层面的消去证明，不可只用旧36约化3词丢弃controller立即反向路线。若不同word的线性部分不同，x=0的plane并覆盖也不能代替全部8个source x的coset覆盖。

本轮cap1CPU，读取/静态整理保守计0.3。0新矩阵/inverse/rank计算、word/chart/controller搜索、field/graph/BFS/solver/Lean；只写本md/json，停止等root的具体局部检验决定。

## root最新首选：四arc与共线对照，仅纸面展开

上面的旧best字面已找到并保留，但root现在选择更直接的手选packet对照，不以28词评分选局部route。实际C30数组和0→18/p0的绑定不变；下面矩阵用**row-major**，与旧best的column-codes格式区分。

令A交换e1/e2、固定e3。四arc的实际forward offsets为V=(e1,e2,e3,111)，T0=T1=A，

`T2=T3=B=[[1,0,1],[0,1,1],[0,0,1]]=I+110*e3^T`。

因e3^T110=0，N²=0，故B²=I；它交换e3与111。A²=I且交换e1/e2，因此四port inverse/offset条件逐对成立。这是纸面等式，不运行F2程序。

共线对照改V3为110，保T0=T1=A，令

`T2=T3=B'=[[0,0,1],[1,1,1],[1,0,0]]=I+111*(1,0,1)`。

(1,0,1)·111=0使B'²=I；直接看两列有B'e3=110、B'110=e3，故也满足相同bar约定。A仍保持这组V（交换前两向量、固定后两向量）。不是只改offset却保一个不相容的逆matrix。

若走source port0再q、bar(q)，controller返回同一18端点；由trueinverse条件展开，其fiber终点为

`A*x + lambda*v0 + (mu+nu)*v_bar(q)`。

因此每个word的image是共同平移A*x加span(v0,v_bar(q))，秩至多2。q的逆port offset遍历V；直接forward的一维image也包含其中。在四arc情形，除v0以外三个向量投影到F2³/<v0>，正好是商空间三个非零方向，三张rank2平面并为全八点。共线V3=e1+e2的投影重复e2方向，只剩span(e1,e2)与span(e1,e3)，并为六点。共同A*x平移说明该纸面结论对全部source x，而非只x=0。

数值预言于是为四arc8/8、共线6/8；这只是root下一sole packet程序的已说明预言，没有在本门计算实际route包或field表。新默认输入见JSON的preferred_local_calibration_input。若仍复用F5式offset=directions[bar(p)]，四arc direction codes应为[2,1,7,4]，共线为[2,1,3,4]；更直接是使用给定forward v_p，别误取directions[p]。

此处的controller立即回退不是fiber强制回退：两个独立控制系数mu、nu可以相异。它解释为什么旧36个controller约化词的singlefullrankNO不能排这个局部union；不证明整C30图D3，更不生成C32或宣称240/256新纪录。静态read/prep仍在cap1内保守0.3收束，未增加任何程序矩阵/rank/word/图/BFS/solver计算。停止。
