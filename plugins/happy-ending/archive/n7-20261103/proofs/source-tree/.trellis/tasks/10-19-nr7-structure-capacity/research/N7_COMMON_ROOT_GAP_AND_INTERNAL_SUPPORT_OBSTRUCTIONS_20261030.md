# N7：共同根间隙、内部切点校准与内支持分离拟阵障碍

日期：2026-10-30。状态：**本轮工作稿；全部新增 unreviewed/unaccepted**。本文忠实转写主会话批准的数学，文档执行者不自行补证。主会话与生成协作者的交叉核对不属于独立审阅。本稿及其文档检查回执均不提升旧稿的接受或 assurance 状态。

用户授权继续 N7 结构研究，明确不调用外部 Claude 或其他外部服务，不运行科学代码、枚举、SAT、solver、proof checker 或证书重放。本地 PowerShell 仅用于文档写入、UTF-8、链接、公式编号及固定算术检查；这些检查不认证数学。主会话已批准现有数学正文保存为本轮工作稿；文档检查已完成，结果为 PASS_DOCUMENT_ONLY，仍不属于数学接受。

本轮在五根、双满、w=0 标准接口中证明两个共同根之间没有 I 点，因而前稿两个实际紧割满核相同；给出任意内部切点处添红一至四点的合法校准构造；并在竞争路线排除逐位置存在内部 private 见证且规范化组件实际顺序分离的拟阵分支。它还给出不依赖分离的 connected rank 2 外供推论、完整 weak 下的大红块交叠组件分类，并记录完整 P/Q 外供与共同根供应尚未闭合的交会。它们不构成新的无条件数值下降，也不证明完整合法 root 循环必有 positive through。

## 1. 模型、来源及本轮范围

主要来源为 [联合 through 与顺序紧割前稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>)，特别是其 §4—6；拟阵背景继承 [联合 neutral 与重分块二分稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §6。实际路径与 private 根链工具亦见 [三匹配主稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_SATURATION_THREE_MATCHING_OBSTRUCTION_20261029.md>)。这些依赖保留各自历史保证边界，不在本文重新独审或接受。

完整有序 rank-3 signotope 的四点 packet 对 a<b<c<d 按 abc、abd、acd、bcd 排列，至多换色一次。单色路径长度按实际顶点计，且对子序列遗传；weak7 比较同一对实际首末点的反色路径，长度和至少 9。767 模型禁 R7、B6、weak7；换色 756 模型禁 R5、B6、weak7，b 是其有效容量上界。有效上界不意味着规模 b 必可达。

§2—3 限定在前稿 §4 的双满标准接口：

\[
|X|=3b+4,\quad S=\operatorname{Src}_{R6}(X),\quad
T=\operatorname{End}_{R6}(X),\quad |X\setminus S|=|X\setminus T|=2b. \tag{1}
\]

两向 canonical 或真实 promotion 所提供的 unrestricted 蓝 fan 及混合角色禁形均继承，不能替换成任意两块满 766。定义

\[
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D). \tag{2}
\]

前稿带 through 主式在本规模给 w=|U∩V|=0；所以 U、V 实际不交。沿用 |D|=b+q、|U|=|V|=q，以及本分支两侧各五根、最小红六横截数各为 5：

\[
E=\{e_1<\cdots<e_5\},\quad
F=\{f_1<\cdots<f_5\},\quad
x=e_2=f_3<y=e_3=f_4,\quad A=I\setminus E,\quad B=I\setminus F. \tag{3}
\]

E 是 W=S∪U 内的右红根，F 是 W′=T∪V 内的左红根。根 fan 只在相应规定集合内可用，不能无条件用于全部 D 或全部 X。已有实际 private 根链为

\[
R6(a^*,e_1,e_2,e_3,e_4,e_5),\quad a^*<e_1,
\qquad R6(f_1,f_2,f_3,f_4,f_5,b^*),\quad f_5<b^*. \tag{4}
\]

本稿 §4 的内部添点构造与 §5—6 的参数 p 竞争路线分别陈述自己的假设，不把它们自动嵌入该双满母体。

## 2. 两个共同根之间没有 I 点

**共同根间隙定理。** 在 §1 的五根分支中，

\[
I\cap(x,y)=\varnothing. \tag{5}
\]

反设存在 i∈I 且 x<i<y。由 (3)—(4)，七个实际点严格有序且两两不同：

\[
a^*<e_1<x<i<y<f_5<b^*. \tag{6}
\]

这些点形成实际 R7(a*,e1,x,i,y,f5,b*)。五个连续三元组逐项为：

| 连续三元组 | 红色来源及适用集合 |
| --- | --- |
| (a*,e1,x) | (4) 的实际 R6(a*,E) |
| (e1,x,i) | e1∈E 的右根性质，三点均在 S⊆W |
| (x,i,y) | x∈E 的右根性质，三点均在 I⊆W |
| (i,y,f5) | f5∈F 的左根性质，三点均在 T⊆W′ |
| (y,f5,b*) | (4) 的实际 R6(F,b*) |

路径实际长度为 7，违反 767 的 R7 帽，证明 (5)。因此 x、y 在 I 的诱导实际次序中相邻；这只排除 I 中间点，不排除 D 中间点。

## 3. 两个紧割满核实际相同

沿用前稿完整第二点支持图及其反向图，而非只固定一组匹配。对 c∈{x,y} 定义

\[
L_c=N_\alpha(A_{\le c})\subseteq U,\qquad
R_c=N_\beta(B_{>c})\subseteq V. \tag{7}
\]

这里 Nα、Nβ 是前稿保留全部替代路径的完整邻集。前稿已证明它们在相应 cut 取 Hall 等号，并且由全部 ambient 红五端点边定义的 N_R 满足

\[
|L_c|+|R_c|=q,\qquad N_R(L_c)=V\setminus R_c. \tag{8}
\]

因 x、y 同属 E 和 F，且 (5) 排除两者之间的 I 点，有实际集合恒等式

\[
A_{\le x}=A_{\le y},\qquad B_{>x}=B_{>y}.
\quad\text{因此 }L_x=L_y=:L,\quad R_x=R_y=:R. \tag{9}
\]

这说明完整邻集相同，不只是两组所选匹配或其人口相同。前稿实际删除定义的两个满核因此为同一个实际集合：

\[
K_x=K_y=:K=N_0\sqcup L\sqcup R,\qquad
N_0=D\setminus(U\cup V),\qquad |K|=b. \tag{10}
\]

前稿对每个 cut 的支持顺序给 L<x 及 R>y，故

\[
L<x<y<R,\qquad K\cap(x,y)\subseteq N_0. \tag{11}
\]

式 (11) 的集合顺序意为每个 L 点均早于 x，每个 R 点均晚于 y；L、R 均非空。没有证明 N0 在该间隙中为空，也没有把 E/F 根 fan 延长到 N0。

前稿的 ambient 双端封闭仍适用于这个共同满核：没有任何 ambient R5 以 K 的两个点为实际首末点，即使内部允许经过任意 X 点。任意 i∈I 的 K+i 由容量迫出 R5，并且该 R5 中 i 必须是端点。这些结论与 (5)—(11) 一起，完整排除“两个 cut 产生不同满核”或“共同根间有 I 点”的子类；它们尚未排除剩余单一 K 与全部外根共同实现的分支。

## 4. 任意内部切点插入红块的实际校准定理

### 4.1 完整构造与 packet 检查

**内部切点插入定理。** 任取换色 756 核 K，即 K 禁 R5、B6、weak7。任取实际 cut K=K−⊔K+，其中 K−<K+，允许某侧为空。在该 cut 插入有序红块 J，1≤|J|≤4：

\[
K_-<J<K_+. \tag{12}
\]

保持 K 的旧三元颜色；J 内部三元组全红。其余三元组按以下完整规则着色：

\[
\begin{aligned}
&2J+1K:\quad B;\\
&1J+2K:\quad
R\text{，若两个 K 点位于 cut 同侧；}\quad
B\text{，若两个 K 点跨 cut。}
\end{aligned} \tag{13}
\]

这些规则给出完整 signotope。旧四点包继承；含 J 的包按实际顺序穷尽如下，χ 表示相应旧 K 三元组颜色：

| 包内组成及 J 的位置 | packet |
| --- | --- |
| 1J+3K，J 在第一位 | RRRχ |
| 1J+3K，J 在第二位 | BBχR |
| 1J+3K，J 在第三位 | RχBB |
| 1J+3K，J 在第四位 | χRRR |
| 2J+2K | BBRR、RRBB 或 BBBB |
| 3J+1K | RBBB 或 BBBR |
| 4J | RRRR |

每个显示字都至多换色一次，故全部 packet 合法。这里是对批准构造的手工理论检查，没有运行颜色枚举或数学检查程序。

### 4.2 全部混合路径帽

任何长度至少 3 的混合红路径只能含一个 J 点，其余 K 点全在 cut 同一侧：两个 J 点配一个 K 点会蓝；一个 J 点配跨侧两个 K 点也会蓝。K 无 R5，故混合红路径长至多 5。

混合蓝路径在左侧至多用一个 K 点，在 J 中至多用两个点，在右侧至多用一个 K 点，故长至多 4。旧 K 无 B6；J 至多四点。因此整个 K⊔J 无 R6、无 B6。

### 4.3 weak7 必须按同一对实际端点核对

不能因新的跨 cut 蓝路径最多四点，就声称所有跨 cut 蓝路径都最多四点：旧 K 内的蓝五路径可能仍存在。正确检查按同一对实际端点分型。

| 实际端点类型 | 同端红蓝路径检查 |
| --- | --- |
| 两端均在 K−，或均在 K+ | 有序路径不经过 J，完全继承 K 的 weak7 禁形 |
| 两端在 K 且跨 cut | 使用 J 的新蓝路径长≤4；红路径不能使用 J，且 K 内红长≤4，故其和≤8。两条路径都不使用 J 时继承 K；旧蓝五路径不与一条新红路径配对，因为这种新红路径不存在 |
| 一端在 J、另一端在 K | 红长≤5，蓝长≤3，和≤8 |
| 两端在 J | 红长≤4，蓝长≤2，和≤6 |

因此 K⊔J 无 weak7，是实际合法的 766 配置，也属于 767。这个检查比较同一对实际首末点，不把不同端点的全局路径上界任意相加。

### 4.4 满核、内部根、红四根与端点化可以共存

构造中没有 ambient R5 双端落在 K。若两个端点位于 K 的同侧，有序路径不经过 J，K 自身无 R5；若两端跨 cut，红路径不能使用 J，也仍由 K 的 R5 帽排除。

若 K 确实是规模 b 的满换色 756 核，则对每个 j∈J，K+j 有 b+1 点、无 B6、无 weak7。容量迫其含 R5。该路径必须使用 j；由上段双端封闭，j 必须为实际端点，即使 j 在整个 K 的内部 cut 处也是如此。

取 |J|=4 得红四点块。对每个单独的 K+j，该 j 是其右侧 K 点的右红根，也是其左侧 K 点的左红根：同一侧两个 K 点与 j 的三元组均红。这里不把该性质延长为整个 K⊔J 中的全部根 fan。这个实际合法构造同时保留满核、内部根、红四根和插入端点化。它条件于满 K 存在，不预设 b 可达。

因此这些局部条件不足以排除共同实现。该构造缺少原双满母体的 P/Q 外部供应及其完整接口，不是临界母体反例，也不把前稿单向全出根校准误当作全部外供相容性的答案。

## 5. 分离大红块的 product 禁形定理

### 5.1 定理及每个内部 pair 的全红见证

**分离大红块 product 定理。** 设 p≥3，实际 signotope 配置禁 B_(p+1)、R_(p+2)。不存在 p 个两两不交且按实际顺序分离的红块

\[
A_1<\cdots<A_p,\qquad |A_i|\ge p, \tag{14}
\]

使从每块任取一点所得的全部 product 选择均为实际蓝 p。

固定某块 Ai 的内部 pair x<y。必有另一整块 Aj 对该 pair 全红：

\[
\exists j\ne i\quad\forall z\in A_j:\quad \chi(x,y,z)=R,
\tag{15}
\]

其中 χ(x,y,z) 总按这三个点的实际次序取色。否则每个其他块均可选 zj 使 χ(x,y,zj)=B。把这些 p−1 个点与 x、y 合在一起，共 p+1 点。含 x、y 的三元组按选择为蓝；来自三个不同块的全部三元组由蓝 product 遗传为蓝。因此该实际点集为 B_(p+1)，矛盾。

### 5.2 见证压到相邻块

若 (15) 有右侧红见证块 Aj，则其见证可压到 Ai+1。j=i+1 时已经成立；j>i+1 时，任取 z_near∈Ai+1、z_far∈Aj。实际顺序为 x<y<z_near<z_far，其 packet 为

\[
(\chi(x,y,z_{\rm near}),R,B,B). \tag{16}
\]

后两项由三个不同块的蓝 product，第二项由全红见证。packet 至多换色一次，强迫首项红。z_near 任意，故整个 Ai+1 是红见证。左侧情形由反序得到 Ai−1 为整块红见证。

### 5.3 沿实际分离块归纳至矛盾

第一块的每个内部 pair 只能有右侧见证；由 §5.2，它们全部向 A2 红。

假设 Ai−1 的所有内部 pair 向 Ai 全红。若 Ai 的某内部 pair 对任何左侧整块全红，将该见证压到 Ai−1 后，取 Ai−1 的任意 p 点及这个 pair。两块内部红；两个 Ai−1 点配一个 pair 点由归纳假设红；一个 Ai−1 点配这两个 pair 点由左见证红。所得 p+2 个实际点全部红，违反 R_(p+2)。

因此 Ai 的任何内部 pair 都不能有左侧见证，只能有右侧见证，且可压到 Ai+1。归纳到最后一块 Ap，其 pair 必有另一整块红见证，却既不能向左，也没有右邻，矛盾。定理成立。

该定理只使用实际分离、块大小至少 p、全部蓝 product 及两条单色帽，不需要额外同端 weak 假设。它不要求这些块构成整个红路径族。

## 6. 逐位置内部 private 见证与分离拟阵分支排除

### 6.1 继承的完整路径背景与新增假设

沿用前稿路径重分块竞争路线。设 p≥3，实际配置禁 B_(p+1)、R_(p+2) 及同实际端点的 R_(p+1)+B3。所研究完整路径角色约束族 F 为 UNSAT：每个红成员是实际 R_(p+1)，必须同时遇角色两侧 K_role、Y_role；每个蓝成员是实际 Bp，必须遇 K_role；两侧分划全体实际点。此处用 K_role 区别于 §3—4 的容量核 K。

假设 F 的完整红族横截数 τ_R=p。令 ℬ 为全部 minimum 红横截，并假设其满足基交换。前稿已证明 G=∪ℬ 上形成 rank p 拟阵，分成 rank 1、rank 2 的实际红块：

\[
G=\bigsqcup_i A_i,\qquad r(A_i)\in\{1,2\},\qquad
|A_i|\le p+1,\qquad\sum_i r(A_i)=p. \tag{17}
\]

所有 bases 都是实际蓝 p，且为各块 bases 的 product。全部原红成员及 G 外点均保留。任意 basis S 的某 s∈S 所对应 private 红成员 H 满足 H∩S={s}。为保持 trace 结构的准确条件，把恰有两个 parallel classes 的 rank 2 部分拆成两个 rank 1 组件；其余 rank 2 块取不可分 connected 组件。在这种规范化表示中，rank 2 块的 cocircuit 具有 rank 2。

前稿的完整 trace 限制是：每个红成员的 G-trace 含某个块的 cocircuit，且其拟阵秩至多 2。若所选 cocircuit 位于 rank 2 块，trace 全在该块；若位于 rank 1 块，trace 含整个该块，之外至多再占一个其他块的 rank 1 子集，即另一 rank 1 块的任意子集，或一个 rank 2 块的单一 parallel class 子集。不能把后一种可能性从背景中删去。

对于 rank 2 块中 basis 点 s 的 singleton-private 成员，含其他块的 cocircuit 会遇到其他 basis 点，所以相应 cocircuit 只能来自本块；它必须含本块内完整 fundamental cocircuit C(S,s)，并避开同块另一 basis 点 t。这里保留原稿的 cocircuit 定义，不把它误写成固定集合 Ai\{t}，rank 2 块内仍允许 parallel classes。

新增反证假设为以下两项：

- **规范化后的** rank 1 与 connected rank 2 组件按实际点次序两两分离。若拆开 parallel classes 后两个 rank 1 组件交错，则不满足本项假设；不能由拆分前分离悄悄推定拆分后仍分离。
- 对每个 minimum basis S、每个 s∈S，**至少存在一条**全在 G 的 s-private 红(p+1)成员。

第二项只要求逐位置存在内部见证，不要求该位置的全部 private 成员都在 G。允许其他 private 成员及非private 红成员含 G 外点。没有删除任何完整约束，也没有把 G 本身当成 UNSAT 核。

### 6.2 排除 connected rank 2 块

若有 connected rank 2 块 Ai，在其中取 basis 点 s、t，并扩成整个拟阵的 basis S。按逐位置存在性假设，选择一条全在 G 的 s-private 实际红成员 H，|H|=p+1。

由 private trace 限制，H∩G 只能留在本块；又 H⊆G，所以 H⊆Ai。它避开 t，因此

\[
|H|\le|A_i|-1\le p, \tag{18}
\]

与 |H|=p+1 矛盾。故没有 connected rank 2 块；由总秩 p，恰有 p 个 rank 1 组件。按规范化后分离假设可写 A1<⋯<Ap。


**不依赖顺序分离的 rank 2 外供推论。** 上述 §6.2 完全没有使用组件的实际顺序分离。只要规范化后存在 connected rank 2 组件，就存在一个 basis S 及其中某个 rank 2 点 s，使其所有 s-private 红成员都触及 G 外，无论组件彼此交错与否。否则每个这种位置都有内部见证，按同一 cocircuit、trace 及避开 t 的长度论证立即矛盾。后续全 rank 1 的极端 basis 证明才需要实际分离假设。

### 6.3 极端 basis 迫每块至少 p 点

反设某 Ai 满足 |Ai|≤p−1。取任意 s∈Ai，构造 minimum basis S：本块选 s；每个左侧块 Aj、j<i，选 min Aj；每个右侧块 Aj、j>i，选 max Aj。

按逐位置存在性假设，选择一条全在 G 的 s-private 红成员 H，|H|=p+1。rank 1 块 Ai 的 fundamental cocircuit 就是整个 Ai，故 H 必须包含 Ai。由 trace 限制，H 只能再用某一个其他块 Aj。因为 |Ai|≤p−1，H 至少从该 Aj 取两个点。

若 Aj 位于左侧，H 的首两点落在 Aj。若 H 不含 min Aj，可把 min Aj 前接到 H：新连续首三元组全在红块 Aj，原连续三元组保持红，得到实际 R_(p+2)，矛盾。因此 H 必含 min Aj。但 min Aj 是 S 在 Aj 中选出的 basis 点，违反 H∩S={s}。

若 Aj 位于右侧，反向使用 max Aj：H 的末两点在 Aj；若不含 max Aj，就可后接得到 R_(p+2)，故必须含它，仍撞上另一个 basis 点。两种位置均矛盾，因此

\[
|A_i|\ge p\quad\text{对全部 }i=1,\ldots,p. \tag{19}
\]

### 6.4 分离 product 矛盾与正面外部供应结论

全部 bases 是从这 p 个 rank 1 块各取一点的完整蓝 product；规范化组件实际分离且 (19) 给每块至少 p 点。§5 定理立即给矛盾。

因此在路径重分块 UNSAT、τ_R=p、minimum transversals 满足基交换且规范化组件实际分离的背景下，必存在一个 minimum basis S 及 s∈S，使这个位置的**每一条** s-private 红成员都遇到 G 外。等价地，不可能每个位置都拥有一条内部 private 见证。

该结论允许全部 multi-private，不要求每点恰有一条 private 成员，也允许非private 红成员在 G 外。证明只在每个使用位置选取一条假设存在的内部见证，没有使用“所有 private 都内部”的更强条件。主会话与生成协作者已交叉核对这一量词减弱，仍不属于独立审阅。

本轮没有去掉规范化组件实际分离假设，没有排除一般拟阵分支的 G 外 private 供应，也没有完成非拟阵完整交换失败分支。τ_R=p 仍指所研究完整路径约束族的红横截数，不是整个临界母体全部 R6 的横截数。

## 7. 完整 weak 下的交叠组件分类

### 7.1 独立参数模型与每块跨度的限制

本节是独立的完整 product 分类，不要求块的次序分离。设 p≥3，实际配置禁 B_(p+1)、R_(p+2)，并禁同实际端点的 R_(p+1)+B3 及 R_p+B4；实际 p=5 的 weak7 同时禁止这两种长度和为 9 的形态。

假设有 p 个两两实际不交的红块 Ai，每块至少 p 点，且从每块任取一点所得的全部 product 选择均为实际蓝 p。本节的 |Ai|≥p 是独立假设，不能由前节只在分离及内部见证背景中得到的大小下界外推到所有纯 rank 1 拟阵。

任一 Ai 的开跨度 (min Ai,max Ai) 内，不能同时有两个分别属于不同外块的实际点 d<e。否则 packet(min Ai,d,e,max Ai) 的首项与末项均来自三个不同块的蓝 product，所以 packet 全蓝，形成同实际端点的 B4(min Ai,d,e,max Ai)。Ai 内可选含极点的红 p，与之构成被禁的同端 R_p+B4。

### 7.2 跨度交叠图每个连通组件至多两块

在这些红块上建闭跨度交叠图：两块的闭跨度相交时连边。每个连通组件至多两块。

反设某块 A 同时交叠 B、C。如果 B、C 各有点位于 A 的开跨度，立即违反 §7.1。否则其中一块，记 B，没有点在 A 的开跨度，却与 A 的闭跨度交叠。因块实际不交且端点全不同，B 的跨度必严格包住 A。

C 的跨度与 A 交叠。若 C 有点位于 B 的开跨度，B 的开跨度中便同时有 A、C 两个不同外块的点，违反 §7.1；若 C 没有点位于 B 的开跨度，则 C 的跨度必严格包住 B，而 C 的开跨度同时含 A、B 的点，仍违反 §7.1。

因此每个顶点度数至多 1，所有连通组件都是单块或交叠对。实际端点全不同，不存在仅相触的边界例外。各组件的 union spans 彼此严格分离，故有明确的从左到右组件次序。

### 7.3 最左与最右组件都不能是单块

反设最左组件为单块 A，因此其余所有块的全部点都晚于 max A。记 A 之后全体点中最早的两点为 z1<z2。

§5.1 的全红整块见证证明不使用次序分离，在这里仍成立：对 A 内任意 pair x<y，有另一整块 C 对该 pair 全红。因为 |C|≥p≥3，有 max C≥z2。对于 j∈{1,2}，若 zj∈C，直接有 χ(x,y,zj)=R；否则 zj<max C，且 packet(x,y,zj,max C) 为 (?,R,B,B)，后三项分别由红见证及三个不同块的蓝 product 给出，故首项红。因此 A 的每个内部 pair 对 z1、z2 都全红。

在 A 中选含 min A、max A 的 p 点。若 z1、z2 属于不同外块，前述红性给出以 min A、z2 为实际端点的 R_(p+1)，蓝 product 又给 B3(min A,z1,z2)，违反同端禁形。因此 z1、z2 同属某一块 B。

同一条 R_(p+1) 及同端 weak 禁形迫 χ(min A,z1,z2)=R。若 χ(max A,z1,z2)=R，则所选 A 中 p 点加 z1、z2 形成 R_(p+2)，矛盾。因此 χ(max A,z1,z2)=B。

再对 B 的内部 pair(z1,z2) 应用全红整块见证。其见证不可能是 A，因为 χ(max A,z1,z2)=B，所以必为第三块 C。该 C 的任一点 c 都晚于 z2：z1、z2 是 A 后最早两点且都在 B。于是 packet(min A,z1,z2,c) 依次为 RBBR，其中两项蓝来自三个不同块的 product，首项由刚才 weak 迫红，末项由 C 的整块见证红。该包换色两次，矛盾。

最左组件因此不能是单块；最右组件由反序同理也不能是单块。

### 7.4 参数分类与 p=3、p=5 的精确范围

综上，每个组件是单块或交叠对，组件 union spans 严格分离，并且最左、最右组件均为交叠对。

这完整排除 p=3 的大红块蓝 product：三个块不可能同时提供两个不同的端部交叠对，而单个组件又至多两块。

p=5 时只剩“交叠对—单块—交叠对”的组件次序。本节尚未排除这一型；它没有外推为所有纯 rank 1 拟阵都具有 |Ai|≥p，也没有排除一般短块或 G 外 private 供应。该分类为主会话批准的工作证明，尚未独审，不登记新的全局 N 下降。

## 8. 完整外供接口与尚未闭合的交会

本节回到 §1—3 的双满、五根、τ5、w=0 与共同满核 K 接口，不将竞争路线的拟阵地集 G 当作该 K。

### 8.1 全部 Y 内部红六的端点图具有 perfect 匹配

令

\[
Y=X\setminus I=P\sqcup D\sqcup Q,\qquad
|P|=|Q|=b-q,\qquad |Y|=3b-q. \tag{20}
\]

任何 Y 内部 R6 的首点属于全部 ambient 源 S，且不在 I，故在 P；终点同理在 Q。以全部实际 Y 内部 R6 建立端点图 P→Q，每条边保留其实际路径含义，不挑样本。

若没有 perfect 匹配，König 定理给出大小至多 b−q−1 的端点副本 cover。将对应的实际端点删去，便命中全部 Y 内部 R6。实际删点至多 b−q−1 个，余集至少 2b+1 点；它继承无 B6、无 weak7，且删除后无 R6，所以是超过容量 2b 的 766，矛盾。因此

\[
\text{全部 Y 内部 R6 的完整端点图 }P\longrightarrow Q
\text{ 有 perfect 匹配。} \tag{21}
\]

此处的完整图不要求匹配路径内部顶点互不相交，也不把不同见证的共享点当成独占资源。

### 8.2 两个共同根处的完整末对与首对供应

定义全部实际 pair 供应集合

\[
\begin{aligned}
\mathcal A_x&=\{p_0:\text{存在 S 内部 R6，其最后 pair 为 }(p_0,x)\},\\
\mathcal B_y&=\{q_0:\text{存在 T 内部 R6，其最初 pair 为 }(y,q_0)\}.
\end{aligned} \tag{22}
\]

这里 p₀、q₀ 是实际点变量，与前文人口参数 q 区别；下文写 p₀∈𝒜x、q₀∈ℬy 时均依此实际点含义。两集合非空，且

\[
\varnothing\ne\mathcal A_x\subseteq P,\qquad
\varnothing\ne\mathcal B_y\subseteq Q. \tag{23}
\]

证明 𝒜x⊆P：任何末前驱 p₀ 在 S=P⊔I。如果 p₀∈I，则 p₀<x<y 三点均在 T⊆W′，由 y∈F 的左根性质，χ(p₀,x,y)=R。把 y 追加到终于 (p₀,x) 的该 S 内部 R6，得到 R7，矛盾。ℬy⊆Q 反向同理：若 q₀∈I，则由 x∈E 的右根性质得到 χ(x,y,q₀)=R，前接 x 形成 R7。

对每个 p₀∈𝒜x，终于 (p₀,x) 的实际 R6 给全 ambient fan χ(p₀,x,z)=B，对所有 z>x；否则追加 z 成 R7。因此任何 ambient R6(p₀→t) 都有 t≤x：若 t>x，同实际端点的 B3(p₀,x,t) 与该 R6 长度和为 9，形成 weak7。反向同理得到

\[
R6(p_0\to t)\Rightarrow t\le x\quad(p_0\in\mathcal A_x),\qquad
R6(s\to q_0)\Rightarrow s\ge y\quad(q_0\in\mathcal B_y). \tag{24}
\]

两个全 ambient fan 还给每个 p₀∈𝒜x、q₀∈ℬy 的实际 B4(p₀,x,y,q₀)。因此

\[
\text{不存在 ambient R5 从 }\mathcal A_x\text{ 到 }\mathcal B_y. \tag{25}
\]

这里 (25) 只禁止同一对实际端点的红五供应；不能把它写成所有 P→Q 红六供应都被排除。

### 8.3 共同满核内红四的完整矩形外供

设 K 内实际 R4(d1,d2,d3,d4) 满足 d1∉U、d4∉V。满角色身份给出 H′=P⊔D 内终于 d1 的蓝五，以及 H=Q⊔D 内从 d4 启动的蓝五。

任取前类蓝五的末前驱 p₀，任取后类蓝五的第二点 q₀。若桥 χ(p₀,d1,d2)=B，前一条蓝五可追加 d2 得 B6；若桥 χ(d3,d4,q₀)=B，后一条蓝五可前接 d3 得 B6。两桥因此都红，连同该实际 R4，得到

\[
R6(p_0,d_1,d_2,d_3,d_4,q_0),\qquad p_0\in P,\quad q_0\in Q. \tag{26}
\]

最后两个身份来自 p₀∈P⊔D、q₀∈Q⊔D，以及 D 没有 ambient R6 源或终点。此结论对任意上述左供、任意上述右供同时成立，是完整矩形供应，不是只选一条见证。

但尚未证明这些供应必与 𝒜x×ℬy 相交。因此该外供接口还不是矛盾，也不产生新上界下降。若该 R4 跨越整个 [x,y]，即 d1<x<y<d4，则其所有左供 p₀ 都不在 𝒜x、所有右供 q₀ 都不在 ℬy：否则 (26) 的终点 q₀>y>x 或首点 p₀<x<y 分别违反 (24)。这一位置排斥只标清尚未闭合的交会缺口，不计新增全局收益。

## 9. 完整合法根循环的现状

前稿已证明同一交替符号下全部实际合法 blue-root charts 构成单一完整循环，根数 m 满足 3≤m≤6；删去合法根 r 得 767 配置 Yr，并有

\[
|Z|+\max_{r\in\mathcal R}w(Y_r)\le3b+5,\qquad
3\le m=|\mathcal R|\le6. \tag{27}
\]

critical |Z|=3b+5 下，完整循环中全 w(Yr)=0 不可能这一命题仍未证明。换 chart 会改变共同实际点的次序与三元颜色，所以 R6 不能当作一条颜色不变、仅更换端点的路径来运输；不同 charts 的容量不能相加。

完整循环虽有限，尚没有可逐步累计的严格损耗，也没有从有限性本身推出某个 chart 必有 positive through。§7 只登记已批准的完整 weak 下交叠组件分类，保留其每块大小与 weak 假设。

## 10. 收益分账与仍开接口

| 本轮新增工作结论 | 完整关闭的范围或迫出的接口 | 尚未推出 |
| --- | --- | --- |
| 共同根间隙与共同满核 | 双满、五根、τ5、w=0 中两个 cut 不同核或根间有 I 点的子类 | 剩余单一 K 与全部外根共同实现不可能 |
| 内部 cut 插入红一至四点 | 满核、内部根、红四根及端点化本身不足的实际校准 | 原 P/Q 外供齐备的临界母体反例 |
| 分离大红块 product 禁形 | p 个实际分离、每块至少 p 点且全部 product 蓝的类 | 任意相交或交错次序块的同一结论 |
| connected rank 2 外供推论 | 无需顺序分离，若有该组件，必有一个 rank 2 位置的每条 private 都遇 G 外 | 含外部供应的 rank 2 分支不可能 |
| 逐位置内部见证的分离拟阵排除 | 规范化组件分离时，必有一个 (S,s) 的每条 private 成员都遇 G 外 | 一般 G 外 private 供应不可能、非分离拟阵、全局重分块完成 |
| 完整 weak 下的大红块 product 分类 | 每组件≤2块，端部均交叠对；p3全排，p5只剩交叠对—单块—交叠对 | p5剩余型不可能、任意纯 rank 1 块大小≥p |
| 完整 P→Q 外供及共同根 pair 方向界 | Y 内全部 R6 端点 perfect；核内合格红四给完整矩形供应 | 外供必遇共同根供应集合，或临界母体矛盾 |

完整合法 blue-root 循环中必有 positive through 仍未证明。四根、τ4、canonical 亏一的单 Ω、单 M 与全空机制之 w=0 共同实现仍未排除。前稿带 through 式已经覆盖这些机制的 positive-through 部分，但不能写成亏一分支全部关闭。

无条件工作证明链保持

\[
N757\le a+b-1,\qquad C766\le2b,\qquad
N767\le3b+4,\qquad N777\le3b+5. \tag{28}
\]

代 a=16、b=25，固定算术为

\[
a+b-1=40,\qquad2b=50,\qquad3b+4=79,\qquad3b+5=80. \tag{29}
\]

本轮无条件全局数值上界新增收益为 0；没有得到 78/79，也没有把条件 positive-through 收益或支持排除登记为新的全局下降。

## 11. 文档检查与保证边界

本轮唯一新增归属是本文及 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_root_gap_internal_support_20261030/DOCUMENT_CHECK.json>)。回执按最终保存内容记录相对与绝对文档路径、SHA256、UTF-8 字节数、公式界定符配平、公式编号唯一连续、本地链接存在性及固定算术 40/50/79/80；结果为 PASS_DOCUMENT_ONLY，只表示文档层检查通过，不认证数学。

全部新增保持 unreviewed/unaccepted。主会话与生成协作者交叉核对不是独审；外部审阅、外部服务、科学代码、枚举、SAT、solver、proof checker 及证书重放均为 0。未修改旧稿、task.json、接受或 assurance、配置、sealed 证据及运行；没有打开页面，也没有宣布长期研究任务完成。
