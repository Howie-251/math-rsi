# 独立核对：两／三独立方向完整线族的局部精确接口

2026-11-01。两个iff均成立，未找到反例。这里讨论同一个F_q³目标fiber中的完整仿射线，方向已指定且两两/三者线性独立。它给出局部可实现计数的必要且充分条件及直接生成法，不保证同一批源中心在其他目标fiber同时相容。0solver、0新图/BFS/Lean、0field或旧全部rank重验。

## 1. 两独立方向：包括zero的精确slab条件

设A、B为非负整数。将两独立方向补成坐标基，分别记为x、y方向。每条x线由(y,z)标记，每条y线由(x,z)标记。

**必要性。** x线和y线相交当且仅当其z坐标相同。因此两族非空线使用的z支持Z_A、Z_B必须不交。每个z只容纳q条某一方向的不同线，故

|Z_A|≥ceil(A/q)，|Z_B|≥ceil(B/q)，

合起来必有ceil(A/q)+ceil(B/q)≤q。

**充分性。** 若上述不等式成立，取两个不交z支持，大小分别ceil(A/q)、ceil(B/q)。在Y×Z_A内任取A个不同anchors，在X×Z_B内任取B个不同anchors；容量各至少所需条数，且两族因z支持不交而不交。A或B为0时取对应支持为空即可，无须额外正性假设。

所以两族存在 **iff ceil(A/q)+ceil(B/q)≤q**。方向平行时不套此式；在此声明的独立方向条件下，任意完整线族都被覆盖，未假设线族本身是矩形。

q9的指定检验：

- 50/31：ceil50/9+ceil31/9=6+4=10>9，不可能，虽然总数正好81。
- 27/54：3+6=9，取Z_A={0,1,2}、Z_B={3,…,8}及全部相应anchors，给27/54条，恰分区729点。
- zero处理也实际检查：0/81、0/0可行，0/82不可行。

这补上旧832 count模型对含零三族的缺口：若只有两个正族，应降成这里的两族精确接口，不能完全跳过可实现性检验。例如旧target32的50/31/0已被第一项排除。本轮没有据此重跑MIP。

## 2. 三独立方向、三族均正：完整projection profiles是iff

记三个轴向族的anchor集合为R⊆Y×Z、G⊆X×Z、Bset⊆X×Y，条数A、B、C都正。

**必要性。** 完整x/y线相交当且仅当z标签相等；x/z线相交当且仅当y标签相等；y/z线相交当且仅当x标签相等。所以必须

Z_R∩Z_G=∅，Y_R∩Y_Bset=∅，X_G∩X_Bset=∅。

令a=|X_G|、b=|Y_R|、c=|Z_R|。由于三族都正，这些支持及其对应不交支持都非空，故a,b,c∈{1,…,q−1}。按anchor集合的投影包络，必有

A≤bc，B≤a(q−c)，C≤(q−a)(q−b)。

这一必要性继承此前THREE_DIRECTION/f9分析，本次没有把旧上界重记为新认识。

**充分性。** 给定满足三式的a,b,c，选择X_G⊆F_q大小a、Y_R大小b、Z_R大小c；令X_Bset、Y_Bset、Z_G分别为其全补集。在Y_R×Z_R内任取A个anchors，在X_G×Z_G内任取B个anchors，在X_Bset×Y_Bset内任取C个anchors。三式确保数量足够，投影支持分离确保三族两两不交；同族不同anchors给不同平行线。

因此三正族存在 **iff至少一个a,b,c∈1..q−1满足上述三式**。充分性允许在矩形包络内任选所需条数，不要求把整个矩形都填满。若有一族为0，应改用第1节两族接口，不强套这个只声明三正族的profile。

## 3. target19的真实方向与实际小witness

目标19在旧832向量的三条入射来自source17、45、71；12/50/11是它们的计数，不是source编号。按已接受PARAMETERS中的实际port/chart：

|source|source port|target port|chart|noise direction|
|---|---|---|---|---|
|17|a_plus=0|a_minus=1|cross_0_1_forward=0|(1,0,0)|
|45|b_minus=3|b_plus=2|cross_2_3_reverse=3|(1,1,1)|
|71|b_plus=2|b_minus=3|cross_2_3_forward=2|(1,2,1)|

只核这三个实际方向，按已有真实GF9乘法表算列行列式为2≠0。并未重验field或旧all-rank。

- 12/50/11：实际512个profiles全部失败。旧推导已有C≤3：A≥12迫c≥2，B≥50迫c≤2，故c=2；继而a=8、b≥6，C≤(9−a)(9−b)≤3。
- 12/50/3：实际唯一profile为(a,b,c)=(8,6,2)，矩形容量12/56/3。取X_G={0,…,7}、Y_R={0,…,5}、Z_R={0,1}；R取全部12anchors，G在56anchors中按字典序取50，Bset取全部3anchors。于是65条线、585pins两两不交。

本次补全的是“3确实可达”，而非再次声称发现旧必要上界3。WITNESSES保存所有实际anchors。27/54的两族分区和12/50/3的三族witness均已用上述三个实际方向作为基底映回target19，逐线9点、族内无重复、族间交集0；未把抽象counts当实际局部线族。

该witness只针对单target，不是完整source中心packing，也不声称全图D3。

## 4. 应执行的生成决策和剩余耦合

以后先选允许的两族z slabs，或三族(a,b,c)及互补投影支持，再在其矩形包络内选真实anchors，随后按每条实际dart的字面M和noise direction运输/拉回源中心；不再只优化837/832这些counts再期待自然互补。它既能提前拒绝50/31、12/50/11，也给27/54和12/50/3明确生成规则。

局部iff没有消除耦合：同一source fiber选定的中心集合S_i必须经它的全部6个dart同时使用，不能为不同target独立换一份S_i。一个target的漂亮slab/矩形拉回，与另外5个target指定的投影支持可能不一致；还须保证各dart内不同中心产生不同线，以及不同source的像互不交。固定W若有已接受的逐dart transversal接口可继承，但也不能解决跨target一致性。

因此剩下的问题是全dart运输兼容，不是单target计数界不够强。本次不求解这一耦合、不再开count MIP或大点池，不把局部不可行counts扩大成整个B线无望。

实际小计算0.017331505 CPU秒，预算3CPU；RESULT/TERMINAL、可运行check.py及WITNESSES齐，全进程终态。只检查本任务指定局部例子及zero处理，0旧all-rank/field/source图/BFS/Lean、0solver、0图计数。Wiki留待root另一次合并，不为本primitive另开节点。
