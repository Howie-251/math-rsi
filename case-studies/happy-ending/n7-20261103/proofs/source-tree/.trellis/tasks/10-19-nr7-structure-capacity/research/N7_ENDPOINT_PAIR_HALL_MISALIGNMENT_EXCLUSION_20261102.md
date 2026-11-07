# N7：实际端点对 Hall 与两类临界机制的统一排除

日期：2026-11-02。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文忠实转写主会话批准的数学内容；主会话及其数学协作者的推导、交叉核对属于同会话生成核对，不构成独立数学 review。指定 native gpt-6.1-sol/high 文档执行者仅转写及检查文档一致性，不自主补证、不认定数学接受状态；未报告的 backend 或实际 effort 不得声称已核实。

本轮先给一般有序实际端点对 Hall 排除定理，再给两类临界机制的统一排除：任一方向 η0 的全部 onefull；双侧正缺额 η∈{1,2} 且双侧新 Ω*=∅、M*=∅ 的全部机制。后者覆盖 (1,1)、(1,2)、(2,1)、(2,2)，包含保留在 §3—4 的双亏二 nonΩ/M0 正错位独立短证明，不重复计覆盖。onefull 统一证明包含此前未覆盖的早且独占 Ω 端点与 η2 单Ω/M* 情形。真正双正缺额 Ω/残余例外尚未全闭；无条件 78/79 工作界暂不变。

唯一新增文件为本文及 `tmp/n7_endpoint_pair_hall_20261102/DOCUMENT_CHECK.json`。旧稿、task.json、入口、metadata、接受/assurance、绑定、runtime、运行与指针保持，不提交、不归档。未调用外部 Claude、未向外传送研究材料，未执行研究代码、枚举、SAT、solver 或证明检查；PowerShell 仅作文档操作和一致性检查。

## 1. 完整模型、实际角色与依赖

完整有序 rank-3 signotope 的四点 packet 按 abc、abd、acd、bcd 至多换色一次。路径按实际顶点计长，由连续三元组同色判定，并对子序列遗传。weak7 比较同一对实际首末点的反色路径，长度和至少 9，内部允许共享。

767 禁 R7、B6、weak7；756 禁 R6、B5、weak7，其换色模型禁 R5、B6、weak7；b 为两者共同有效容量。N_sig 表示最大允许人口容量，不是强迫阈值。

本轮沿既有临界入口取 w=0，使用全部 ambient 实际角色：

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),\quad
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),\quad U\cap V=\varnothing.
\tag{1}
\]

Src、End 均在注明的实际点集内计算，ambient 指母体 X。所有端点图保留其注明域内全部实际路径的端点或相邻 pair；删点按实际点计，不额外要求路径内部不交。

主要依赖保持原保证层级：

- [最新锁端口吸收与完整重分划稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCKED_PORT_ABSORPTION_AND_COMPLETE_REPARTITION_20261101.md>) §1—5 提供完整模型、端口、一般 Ω 归一化及正错位入口；§6 提供完整 F 背景、旧位置引理和所需交错颜色。
- [Hall 增广与零 through 闭合稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_HALL_DEFECT_ROOT_AUGMENTATION_AND_ZERO_THROUGH_CLOSURE_20261101.md>) §5 提供一般 η≤2 归一化，§6 提供双核、完整角色、E+/F+ 与既有错位分支。
- [加权稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>) §8 提供既有入口所用的实际头尾替换；本轮正错位应用不新增该调用，旧依赖保持。
- [78/79 参数工作界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>) 提供既有全模型工作上界及其保证边界。

反向 fullstandard 特指 H'=X∖T 是真实满 2b 的 766 域，完整 mixed 禁形、蓝四延长、全部 ambient 角色均已兑现；不能用任意满 766 子集替代。

## 2. 一般有序实际端点对 Hall 排除定理

### 2.1 全量词接口与参数形式

母体为 767。q、d_-、d_+、m 均为非负整数，且 0≤m≤q。U、V 各有 q 点，完整实际 R5 的 U→V 图含 q−m 条匹配。两个实际基础集合 K_-、K_+ 分别含 U、V，且

\[
|K_-|\ge b-d_-,\qquad |K_+|\ge b-d_+.
\tag{2}
\]

根集 B、A 分别在对应基础集合之外，并与对应端口层不交。存在严格 cut c，使 B<c<A。两个实际扩域 X_-=K_-∪B、X_+=K_+∪A 均无 B5，并满足下列**全部路径**接口：

\[
\begin{aligned}
&X_-\text{ 内每一条 R6 的最后相邻 pair 都是 }(u,r)\in U\times B;\\
&X_+\text{ 内每一条 R6 的最前相邻 pair 都是 }(s,v)\in A\times V.
\end{aligned}
\tag{3}
\]

这不是只选择若干有利路径。若

\[
|B|+|A|>q+d_-+d_++m,
\tag{4}
\]

则整个配置不可能。

### 2.2 从全部相邻 pair 到实际 matching

保留 X_- 内全部实际 R6 的最后相邻 pair，建立 U、B 二部图。任意 vertex cover 删掉对应实际点后，余域无 R6、无 B5，并继承 weak7 禁形，所以余人口至多 b。由 (2) 及 König 定理，左图 matching 大小至少 |B|−d_-。完全对偶，右图 matching 大小至少 |A|−d_+。

沿中间 q−m 条实际 R5 matching 运输：左 matching 至多 m 个 U 点没有中间 mate，再在 q 点 V 上与右 matching 的 target 集合相交。因此得到至少

\[
|B|+|A|-q-(d_-+d_++m)
\tag{5}
\]

条三图交会链。只有该数为正时才调用链；(4) 正好保证至少一条。

### 2.3 相同实际端点的 weak 矛盾

任一条交会链给出真实末 pair (u,r)、真实中间 R5(u→v)、真实首 pair (s,v)。路径次序和严格 cut 给

\[
u<r<c<s<v.
\tag{6}
\]

若 χ(u,r,s)=R，便可在末 pair 为 (u,r) 的实际 R6 后 append s 成 R7，故它为 B。若 χ(r,s,v)=R，便可在首 pair 为 (s,v) 的实际 R6 前 prepend r 成 R7，故它也为 B。因此 B4(u,r,s,v) 与中间 R5(u→v) 具有同一对实际端点 u、v，长度和为 9，违反 weak7。

三份 matching 只要求相应层端点各自不同；实际路径内部可以共享，从未把复制链拼成一条红路径。主机制使用 d_-=d_+=m=0。缺额容忍是结构定理参数，Ω 机制若未兑现全部 pair 定位，不得直接扣预算。

## 3. 既有双亏二 nonΩ/M0 正错位的完整入口

沿 Hall 稿 §6 与最新稿 §5，双侧 η=2、nonΩ、M0 时，

\[
K'=P\sqcup U\sqcup Q_0,\qquad K=P_0\sqcup Q\sqcup V,
\qquad |K'|=|K|=b,\qquad |P_0|=|Q_0|=2,
\qquad |U|=|V|=q\ge1,\quad |I|=q+7.
\tag{7}
\]

K'、K 均为实际满 b 的 756 核。五根为

\[
E=\{x,a,y,e_4,e_5\},\qquad F=\{f_1,f_2,x,\beta,y\},\qquad
f_1<f_2<x<a<\beta<y<e_4<e_5,
\qquad P_0<a<\beta<Q_0.
\tag{8}
\]

集合次序表示其中每一点均严格满足。全部 p∈P0 都有实际 S 内入 R6 的末 pair (p,e_p)，e_p∈{x,a}；全部 q0∈Q0 都有实际 T 内出 R6 的首 pair (f_q,q0)，f_q∈{β,y}。

M0 等完整接口保证 K 每一点均无 ambient B5 源，K' 每一点均无 ambient B5 终点；I 点由 R6 joining 同样获得两方向蓝禁形。另有 E+=E、F+=F：E+ 收集全部 I 内能成为 ambient R6 末 pair (s,e) 且 s∈S 的 e；F+ 对偶收集全部首 pair (f,t) 且 t∈T 的 f。完整 D 内红五图含 q-perfect matching。

这些是 ambient 身份与全路径接口，不能用仅内部满核替代。

## 4. 正错位全部 q≥1 的整类排除

### 4.1 严格 cut 两侧的根总量

取

\[
B_0=(I\cap(-\infty,a))\setminus E,\qquad
A_0=(I\cap(a,\infty))\setminus F.
\tag{9}
\]

两集均不含 cut 点 a。由 (8)，

\[
B_0\sqcup A_0=I\setminus\{x,a,\beta,y\},\qquad
|B_0|+|A_0|=q+3.
\tag{10}
\]

其余 I 点按 a 左右恰计一次，不需要额外的 I 跨度限制、中央 gap 为空或 private chain。

### 4.2 左扩域的全部实际末 pair

X_-=K'∪B0 每一点均无 ambient B5 终点，因而无 B5。任一 R6 终点不可能在 P∪U，因为这些点不属于 T；故终点只可能在 Q0 或 B0。

若终于 q0∈Q0，记实际首点 z。原出 R6 首 pair (f_q,q0) 给任 z<f_q 的 χ(z,f_q,q0)=B，否则可 prepend 成 R7。若 z<f_q，这个 B3 又与新 R6(z→q0) 同端违反 weak7。因此 z≥f_q≥β>a，整条有序新 R6 都在 a 右侧，不含 B0<a，于是全在 K' 内，与 K' 无 R6 矛盾。

故任一 R6 终点 r∈B0。它的末前驱不在 Q0，因为 Q0>β>a>r；若在 P∪B0⊂S，则 r∈E+=E，与 B0 定义矛盾；所以末前驱只能在 U。这穷尽 X_- 中全部 R6，完整兑现 U→B0 的最后相邻 pair 定位。

### 4.3 右扩域的全部实际首 pair

X_+=K∪A0 每一点均无 ambient B5 源，因而无 B5。R6 起点不可能在 Q∪V，因为这些点不属于 S；故起点只可能在 P0 或 A0。

若始于 p∈P0，记实际末点 z。原入 R6 末 pair (p,e_p)，e_p≤a，给任 z>e_p 的 χ(p,e_p,z)=B。与新 R6(p→z) 同端 weak7 迫 z≤e_p≤a。整条新路径位于 a 左侧或 a，不含 A0>a，故全在 K 内，与 K 无 R6 矛盾。

余下起点 s∈A0；第二点不可能在 P0<a<s。若第二点在 Q∪A0⊂T，则 s∈F+=F，矛盾。因此第二点只能在 V。这穷尽 X_+ 中全部 R6，完整兑现 A0→V 的最前相邻 pair 定位。

### 4.4 容量 matching 与统一矛盾

应用 §2，取 d_-=d_+=m=0，根集严格满足 B0<a<A0，而 (10) 给 q+3>q，矛盾。等价地，两个完整 pair 图分别饱和全部新增根，与中间 q-perfect matching 至少交会 3 条实际 u、v；其中任一条都给实际 R5(u→v) 和 B4(u,r,s,v) 的同端 weak7 矛盾。

本证明直接兑现实际端点与次序兼容的禁配红五，无须先构造 P0→Q0 红五，也未拼接复制链。该应用不新增头尾替换调用；既有 E+/F+ 等入口原证明的依赖保持。

此前 β<a 已由 cut 排除，a=β 已由 R7 排除，此处 a<β 整类排除。因此既有双亏二 nonΩ/M0 主机制整个关闭，覆盖所有 q≥1；这不代表全部 η2 或 Ω 混合都已关闭。

若同样人口 q+3 及完整 pair 定位在缺额机制中实际成立，§2 还给 d_-+d_++m≤2 时的排除。此为可复用结构推论，尚未兑现的 Ω 入口不能计为覆盖。

## 5. 全部 onefull、另一侧 η≤2 的统一排除

本节新增完整整类排除，覆盖 η≤2 的全部 onefull，包括旧 δ0 与高端点已关闭类；重叠部分不重复计收益。真正新覆盖包含 δ≥1 的早且独占端点及 η2 单Ω/M*，无需先证明这些新端点可延长。

本节 a=|A_H| 及最早源集合 A0 是局部符号，分别与 §4 的 cut 点 a、根集 A0 区分。

### 5.1 完整归一化、修补核与实际 middle

反向真实 fullstandard 满足 H'=X∖T、|H'|=2b，Z'=Src_R5(H')=P⊔U、|Z'|=b。正向沿 Hall 稿 §5 归一化：|H*|=2b−η，0≤η≤2，Ω⊂T∖H* 收集全部 H*-origin R6 终点，o=|Ω|。令 A_H=H*∩S⊂P、a=|A_H|；各源均有 ambient 入 R5、出 B5，三链将其全部 R6 终点与 B5 第二点锁到唯一 Ω 点。

令 L=Ω∩S、δ=|L|。W=S∖L 是实际 D7，具有完整 port，并有

\[
|W|=b+h,\qquad h=3+\eta-o+a,\qquad
u=|U|,\quad |D|=b+u,\quad i=|I|=u+h+\delta.
\tag{11}
\]

完整 port 指 W∩End_R5(X) 的 ambient B5 第二点在 T∖W；W∪U 内 B4 能保首 pair 向右延长，反 full 的 T∪V 同理能保末 pair 向左延长。不得用任意满 766 子集替代。

对每个 Ω 点，从全部 H*-origin 入供中取最早源，组成 A0，|A0|=o、A0⊂A_H∩P。不同 Ω 对应不同源，因为三链给唯一锁。令 C_H=End_R5(H*)，则 A0∩C_H=∅：若 owner 有 H* 内入 R5，与其第二点为 ω 的出 B5 joining，蓝桥给 B6；红桥则给更早的 H*-origin 源到 ω，两色均矛盾。

对任 C_H 点，假设的 ambient B5 与核内入 R5 joining，迫其第二点属于 Ω；A_H 也由三链锁 Ω。因此 K=C_H⊔A0 内部无 B5，H* 又无 R6，K 是实际 756。删 C_H 后无 R5、继承无 B6 与 weak7，换色 756 容量给 |C_H|≥b−η。因此可写

\[
|K|=b-\kappa,\qquad 0\le\kappa\le\eta-o.
\tag{12}
\]

H*=D⊔Q_H⊔A_H，其中 Q_H=Q∩H*，所以 |Q_H|=b−u−η−a。集合 C_H∪Q_H∪A_H 仍为 H* 内实际 756：C_H、A_H 的蓝五第二点只能在域外 Ω，Q_H⊂T 根本无 ambient B5 源。该集合恰是 (C_H∩D)⊔Q_H⊔A_H。令 t=|C_H∩D|，容量给

\[
t+|Q_H|+a\le b,\qquad t\le u+\eta.
\tag{13}
\]

此处允许 M* 非空，未使用早端点可延长。

取 D_all=D⊔A0⊂H*∩H'。反 full 完整角色给 Src_R5(D_all)⊂U⊔A0；删除全部源后，换色 756 容量 b 又给源数至少 u+o，所以恰为 U⊔A0。端点属于 C_H∩D，因为 A0∩C_H 为空。

这里仅声称 End_R5(D_all)⊂C_H∩D，不取一般等号。源层和端点层在实际点上可能交叠；König cover 删除对应实际点至多 cover 大小，仍击中全部实际 R5，因此不影响容量矛盾。

若完整 R5 端点图的最大 matching 小于 u+o，König 删至多 u+o−1 个对应实际点，便留下至少 b+1 点、无 R5、无 B6、无 weak7，矛盾。因此 middle matching M 覆盖全部 U⊔A0，像为

\[
J\subseteq C_H\cap D,\qquad |J|=u+o.
\tag{14}
\]

### 5.2 完整 adjacent 根及严格分离

定义全部相邻根

\[
\begin{aligned}
\widehat E&=\{e\in W\cap T:\text{某 ambient R6 的末 pair 为 }(s,e),\ s\in W\},\\
\widehat F&=\{f\in I:\text{某 ambient R6 的首 pair 为 }(f,t_0),\ t_0\in T\},
\qquad e=|\widehat E|,\quad f=|\widehat F|.
\end{aligned}
\tag{15}
\]

Ehat 是整个 W∪U 的右红根：若有 B3(e,x,y)，原 R6 末 pair 帽给 B4(s,e,x,y)，完整蓝四延长保首 pair 得 B5；但 s∈W∩End_R5(X)，第二点 e∈W，违完整 port。Fhat 对偶为 T∪V 的左红根。它们包含原 W、T 内部 E、F，均非空。

证明 Fhat<Ehat。任取 f0∈Fhat，取原实际 R6 首 pair (f0,t0)，t0∈T 且有 Src_R5(X) 身份。反 full mixed 给 t0 无 ambient B5 终点。Z'+t0 全部点均无 ambient B5 终点，b+1 容量迫 R6(p,z1,z2,z3,z4,t0)，p∈P，因为 U 不属于 S，前五点在 Z'。

若 p<f0，原首帽 B3(p,f0,t0) 与该 R6 同端 weak7 矛盾；p=f0 因 P∩I=∅ 排除，故 f0<p。任取 e0∈Ehat，若 e0<p，完整右根在 W∪U（包含 Z'）给 χ(e0,p,z1)=R；前接这五点 prefix 成 R6，终于 z4∈Z'⊂X∖T，矛盾。e0=p 同样因 I∩P=∅ 排除，故 p<e0。于是

\[
\widehat F<\widehat E,\qquad e+f\le i.
\tag{16}
\]

### 5.3 两个完整 pair 图、锁边与 middle 交会

取

\[
B=I\setminus(\widehat E\cup L),\qquad
A=I\setminus(\widehat F\cup L),\qquad
\nu=|\widehat F\cap L|.
\tag{17}
\]

Ehat∩L=∅，故

\[
|B|=i-e-\delta=u+h-e,\qquad
|A|=i-f-\delta+\nu=u+h-f+\nu.
\tag{18}
\]

左扩域 Z'∪B 全部点无 ambient B5 终点。任一 R6 终点只能在 B，因为 Z' 避 T；若末前驱在 P∪B⊂W，则终点属于 Ehat，矛盾，所以末前驱只能在 U。§2 的实际 vertex-cover 容量论证给 matching，将全部 B 饱和到 U。

每 ω∈L 再加入其 owner a_ω→ω 锁边，得到 |B|+δ 条左边，源互异、根互异：A_δ⊂A0 与 U 不交，L 与 B 不交，根均避 Ehat。锁边的实际 R6 末 pair 来自 ambient 入 owner 红五与 B5(a_ω,ω,…) joining；蓝桥给 B6，红桥才给末 pair (a_ω,ω) 的另一条 R6。不能把原 owner-origin R6 的末 pair 直接视作该锁边。

右扩域 K∪A 无 B5：K 的潜在第二点只可能在 Ω，而 Ω 不在 K 或 A；A⊂T 没有 ambient B5 源。任一 R6 不能从 K⊂H* 开始，因为其终点必须在缺席的 Ω，所以首点 s∈A。第二点若在 T，则 s∈Fhat，矛盾；由 K⊂H*=D⊔Q_H⊔A_H、A⊂T，第二点必在 (C_H∩D)∪A_H。

保留全部首 pair 的图，König 容量给 matching 大小至少 |A|−κ：若 cover 更小，删后剩余超过 b 点且无 R6、B5，矛盾。舍弃 target 不在 J 的边，至多损失 a+(t−|J|) 条；不要求 C_H∩D 全部端点可延长。

Middle M 覆盖全部左源 U⊔A0。三图 inclusion-exclusion 因而给实际链数

\[
\begin{aligned}
\ell&\ge |A|+|B|+\delta-\kappa-a-t\\
&\ge u+2h-e-f+\delta+\nu-\kappa-a-\eta.
\end{aligned}
\tag{19}
\]

每链保留真实末 pair (u0,r)、真实 middle R5(u0→v0) 和真实首 pair (s,v0)。若 r<s，则两条 R6 的 R7 帽给同端 B4(u0,r,s,v0)，与 middle 红五违反 weak7；故 s≤r。左右根端点各自互异，并且 r∈I∖Ehat、s∈I∖Fhat。

### 5.4 严格根 cut 与正余量矛盾

取 c=max Fhat。对每一条 s≤r 的链，若 r≤c，将它计入 distinct s≤c 且 s∉Fhat；若 r>c，将它计入 distinct r>c 且 r∉Ehat。Fhat 全部≤c，Ehat 全部>c，两侧可计点总数给

\[
\ell\le i-e-f=u+h+\delta-e-f.
\tag{20}
\]

(19) 下界比 (20) 上界至少多

\[
h+\nu-\kappa-a-\eta
=3-o+\nu-\kappa
\ge3-\eta+\nu\ge1.
\tag{21}
\]

由 e+f≤i，链下界本身至少为这个正差，故没有负链数或小 u 遗漏。矛盾。全部 onefull、另一侧 η≤2 的机制统一关闭，反序亦然。

此证明以完整实际首 pair matching 处理早且独占 Ω 端点，不要求先延长该端点。δ0/η0 与旧闭合类重叠，不重复计数值 saving。

## 6. 全部双正缺额 nonΩ/M0 的统一排除

本节覆盖正反缺额均在 {1,2}、双侧新 Ω*=∅、M*=∅ 的全部机制，包括 §3—4 的正错位子类；后者作为独立短证明保留，不重复计覆盖。本节 α、β 是两个缺额，β 与 §3 的根名 β 区分；r、s 是前驱、后继集合的大小，与路径参数或链根点区分。

本节 P0/Q0 按全部低根/高根相邻 pair 重新定义，不沿用 §3 的固定两点人口。

### 6.1 参数、完整扩根与 ambient pair 头尾替换

取 n=3b+3、w=0，正反缺额 α、β∈{1,2}，有

\[
|S|=b+3+\alpha,\quad |T|=b+3+\beta,\quad
H=X\setminus S,\ |H|=2b-\alpha,\quad
H'=X\setminus T,\ |H'|=2b-\beta.
\tag{22}
\]

H 全局无 R6 源，H' 全局无 R6 终点。双侧 nonΩ/M0 给完整 port，尤其 S∩End_R5(X)∩Src_B5(X)=∅，T∩Src_R5(X)∩End_B5(X)=∅。写

\[
i=|I|=q+3+\alpha+\beta,\qquad
|D|=b+q,\qquad |P|=b-q-\beta,\qquad |Q|=b-q-\alpha.
\tag{23}
\]

暂不预设 q 非负。定义 Ehat 为全部 e∈I，使某 ambient R6 末 pair 为 (p,e)、p∈S；Fhat 为全部 f∈I，使某 ambient R6 首 pair 为 (f,t)、t∈T。完整根域 S∪U、T∪V 照 §5 证明。令 e=|Ehat|、f=|Fhat|、x=min Ehat、y=max Fhat。

S、T 无 B5；删去其 R6 横截后容量至多 b，所以 τ_R6(S)≥3+α、τ_R6(T)≥3+β。各扩根族自身为红 clique，禁 R7 又给

\[
3+\alpha\le e\le6,\qquad 3+\beta\le f\le6.
\tag{24}
\]

weighted 稿 §8 的头尾替换原证明对 ambient pair 版仍有效，不要求整条 R6 都在 S 或 T 内。完整尾替换短证如下。取实际 R6(v1,v2,v3,z4,z5,z6)，z4∈End_R5(X)，z5<f0∈Fhat；取入 z4 红五的末前驱 d，及 f0 原红六首 pair (f0,t0)，t0∈T。若 χ(d,z4,z5)=R，原入红五追加 z5、z6 成 R7，所以它为 B。若 χ(z4,z5,f0) 也为 B，首帽 χ(z5,f0,t0)=B 给 B5(d,z4,z5,f0,t0)，违反 t0∈T∩Src_R5(X) 无 B5 终点。因此 χ(z4,z5,f0)=R，可把原红六尾点替成 f0。

头替换为完整反序：实际 R6 第三点有 Src_R5(X) 身份，且 e0∈Ehat 严格早于第二点，即可替首为 e0。此处使用 M0/完整 port；后文每次调用均检查相应第三或第四点的实际身份。

### 6.2 全 ambient 低/高 pair 压缩与 q 非负

令 C=End_R5(H)，则 |C|≥b−α。C 无 ambient B5 源：核内入红五 joining 的红桥会造 H-origin R6，蓝桥会造 B6。

P0 收集全部终于 Ehat 中小于 y 的根的 ambient 红六中，落在 S 的末前驱，r=|P0|。若有 α+1 个不同前驱，则 C 加这些点超过 b 点且无 B5：前驱属于 S∩End_R5(X)，由 M0 无 B5 源。容量迫 R6，其源只能是某个前驱 p。原对应末 pair (p,e_p)、e_p<y 的帽和同端 weak7 迫新终点≤e_p；全部点都有 End_R5(X) 身份，尾替换到 y 后与 B3(p,e_p,y) 同端 weak7 矛盾。所以 r≤α。

若某前驱 p 还在 T，Fhat 根 y 在 T∪V 的左根给 χ(p,e_p,y)=R，而原末帽给 B，矛盾。因此 P0⊂P。完整反序令 Q0 收集全部始于 Fhat 中大于 x 的根的 ambient 红六中，落在 T 的第二点，则

\[
P_0\subseteq P,\quad r\le\alpha,\qquad
Q_0\subseteq Q,\quad s=|Q_0|\le\beta.
\tag{25}
\]

令 k=|Ehat∩(−∞,y)|。P0∪(Ehat∩[y,∞)) 击中全部 S 内部 R6：每条内部红六末端属于 Ehat，低根的末前驱在 P0。所以 k≤e+r−3−α≤e−3≤3；即使 k=r=0，该论证也由 e≥τ 有效，不提前假定前驱存在。

Fhat 与 Ehat 中≥y 的部分至多交于 y，故 k≥e+f−i−1。合并得到

\[
i\ge f+2+\alpha-r,\qquad
q=i-3-\alpha-\beta\ge2-r\ge2-\alpha\ge0.
\tag{26}
\]

先排除负 q 后才使用 middle；q=0 允许空 matching。

### 6.3 初始近满 budget 与全部 gap 的必要条件

令 C'=Src_R5(H')，c_-=|C'∩D|、c_+=|C∩D|。集合 C'∪P=P⊔(C'∩D)、C∪Q=Q⊔(C∩D) 均为实际 756：它们分别在无 R6 的 H'、H 内，全部 ambient 对应蓝禁形保持。缺额为

\[
d_-=q+\beta-c_-\ge0,\qquad d_+=q+\alpha-c_+\ge0.
\tag{27}
\]

D 的全部实际 R5 端点图有至少 q 条 matching；否则 König 删少于 q 个实际点，余超过 b 点且无 R5、无 B6、无 weak7，违反换色容量。固定 q 条，源像 J_U、终像 J_V 各 q 点，分别在 C'∩D、C∩D。

任取不经过 I 的 gap c，令 B_c=(I∩(−∞,c))∖Ehat，A_c=(I∩(c,∞))∖Fhat。左扩域全部 R6 末 pair 只能由 C'∩D 指向 B_c：终点不在 P 或 D，末前驱若在 P∪B_c⊂S，则该终点属于 Ehat，矛盾。对偶右扩域全部首 pair 只能由 A_c 指向 C∩D。全部蓝禁形保持，capacity Hall 两图 matching 至少为 |B_c|−d_-、|A_c|−d_+。

舍弃非 middle 端口最多损失 c_-−q、c_+−q；每侧总损失恰为 d_-+c_-−q=β、d_++c_+−q=α。若 |A_c|+|B_c|>q+α+β，就有实际交会，根点位于 c 两侧，实际蓝四与 middle 红五同端 weak7 矛盾。因此每个 gap 都满足

\[
|\widehat E\cap(-\infty,c)|+|\widehat F\cap(c,\infty)|\ge3.
\tag{28}
\]

y 左侧紧邻 gap 给 k≥2，x 右侧紧邻 gap 给 |Fhat∩(x,∞)|≥2，故 x<y、r,s≥1。特别 y 有 actual second t_y∈Q0 且 t_y>y，所以

\[
s_{<y}:=|Q_0\cap(-\infty,y)|\le s-1.
\tag{29}
\]

### 6.4 修补全部前驱、后继后仍为实际 756

取

\[
L_+=C\cup Q\cup P_0=P_0\sqcup Q\sqcup(C\cap D),\qquad
L_-=C'\cup P\cup Q_0=Q_0\sqcup P\sqcup(C'\cap D).
\tag{30}
\]

全部点分别具有 End_R5(X)/无 B5 源、Src_R5(X)/无 B5 终点：Q 有 End_R6(X)，P 有 Src_R6(X)，前驱、后继用 M0。

若 L_+ 有 R6，源只能在 P0；原帽迫终点≤e_p<y，全部点有 End_R5(X)，尾替换 y 造成同端 weak7。所以 L_+ 是 756。L_- 完整反序，用头替换 x；每个 Q0 点对应的高根 f_t>x，故同样是 756。记非负缺额

\[
\kappa_+=q+\alpha-r-c_+\ge0,\qquad
\kappa_-=q+\beta-s-c_-\ge0.
\tag{31}
\]

这里无需满核，也无需 U、V 人口取等。

### 6.5 最终 strict cut y 与额外 Q0 端口

令 B=(I∩(−∞,y))∖Ehat，A=(I∩(y,∞))∖Fhat。因为 y=max Fhat，不论 y 是否属于 Ehat，均有

\[
|A|+|B|=i-1-k=q+2+\alpha+\beta-k.
\tag{32}
\]

在 L_-∪B 中，若 R6 终于 t∈Q0，原首帽迫其首点≥f_t>x。扩域全部点都有 Src_R5(X) 身份，包括 B⊂I，所以可头替换首点为 x，与 B3(x,f_t,t) 同端 weak7 矛盾。因此终点在 B。

末前驱若在 P∪B⊂S，则终点属于 Ehat，矛盾；余下只可能在 C'∩D 或 Q0 中小于 y 的点。**必须保留后一类：排除 Q0 作为终点，不等于排除它作为末前驱。** Capacity Hall 给 matching 至少 |B|−κ_-。舍弃非 J_U 的 D 源 c_-−q，以及额外 Q0<y 端口至多 s−1，总损失为

\[
\kappa_-+c_--q+s_{<y}=\beta-s+s_{<y}\le\beta-1,
\tag{33}
\]

故保留至少 |B|−(β−1) 条。

右域 L_+∪A 中，若 R6 源 p∈P0，原帽迫其末点≤e_p<y，新 A>y 不参与，于是全在旧 L_+，矛盾。余下源在 A。全部 P0<y 不能作这些路径的第二点；第二点若在 Q∪A⊂T，则该源属于 Fhat，矛盾；所以第二点仅在 C∩D。容量 matching 舍弃非 J_V 后总损失 κ_++c_+−q=α−r，保留至少 |A|−(α−r) 条。

与固定 middle q-matching 复合，实际交会下界为

\[
\begin{aligned}
\ell&\ge |A|+|B|-q-(\beta-1)-(\alpha-r)\\
&=3+r-k\ge3+r-(e+r-3-\alpha)\\
&=6+\alpha-e\ge\alpha>0.
\end{aligned}
\tag{34}
\]

每链根点 r_left<y<s_right，两条实际 R6 的帽给 B4(u,r_left,s_right,v)，与 actual middle R5(u→v) 同实际端点 weak7 矛盾。q=0 时 middle 为空，正的实际交集下界直接矛盾，不声称空 matching 真产生路径，也不使用负规模。

所以全部双正缺额 α、β∈{1,2} 的双侧 nonΩ/M0 整类关闭，包含四个参数组合。不需要根数恰为 5、不需要 Ehat 等于 ordinary E、无需 C=Q∪V 或 |U|=|V|=q。

## 7. 完整 F 的区间占用分划与极端分离排除

### 7.1 全部 bases 背景与区间占用定理

沿最新锁端口稿 §6 的严格完整 F 背景：p≥3，禁 B_(p+1)、R_(p+2) 及同实际端点 R_(p+1)+B3。F 是全部红 R_(p+1) 成员和蓝 Bp 成员；目标 K⊔Y=X，使每红同时遇 K、Y，每蓝遇 K。

红横截数为 p，全部 minimum bases 恰是 p 个各至少 2 点的红块 G_i 的 rank1 product，每个 basis 都是实际 Bp。G 是全部 bases 的并集，每红 H 的 trace H∩G 含某完整块。

固定 p 点块 A、basis S=D⊔{s}，其中 D={d1<⋯<d_(p−1)}<A。全部 s-private 红成员均为 A⊔{v}，V 收集全部 v∉G。旧位置引理给 V<d*=d_(p−1)，且 V∪{d*} 全为 ambient R_(p+1) 源；本轮不冒称重证该旧位置引理。

令 d0=−∞，V_j=V∩(d_(j−1),d_j)，ν_j=|V_j|。若每个 ν_j>0 的 j，或者 d_j 是 ambient R_(p+1) 源，或者满足

\[
i+\sum_{k=i}^{j}\nu_k\le p-1\qquad\text{对全部 }1\le i\le j,
\tag{35}
\]

则 Y=D∪V、K=X∖Y 满足完整 F。

完整红证明：H 若遇 D 就遇 Y；否则 S 横截迫 H 为 s-private，故恰 A+v，仍遇 Y。又 Y∩G=D 不含整块，而每个 H 的 trace 含某整块，故 H 也遇 K。

蓝侧沿旧已证交错颜色：VDD、VDV 红，DVD 蓝。实际 Bp 不能终于 ambient R_(p+1) 源，因为 joining 的两色分别给 B_(p+1) 或 R_(p+2)。若 Y 有 Bp，它必形为 D_L<V_C<d，V_C 非空、d∈D。

设 max V_C∈V_j，把末点 d 降为 d_j 仍是 Bp：若 d_j<d，对 v<w∈V_C 的 packet(v,w,d_j,d)=(?,B,R,R) 迫 χ(v,w,d_j)=B；新 DVD、纯 D 三元组蓝，其余继承原路径。若 d_j=d 直接保留。d_j 若为源即矛盾；否则设 min V_C∈V_i，D_L 最多 i−1 点，V_C 最多 Σ_(k=i)^j ν_k 点，加上最后点总数至多 (35) 的 p−1，不可能承载 Bp。故 Y 无 Bp，全部原蓝遇 K，完整分划得证。

### 7.2 多外供全类推论与两外供剩余位置

若前 p−2 个 gap 各有 ν_j≤1，最后 gap ν_(p−1) 任意，则完整 F 可分划。因为非末 j 满足 i+Σ_(k=i)^jν_k≤j+1≤p−1，而末右继 d* 自动是源。

两个外供时，除两点同时在倒数第二 gap (d_(p−3),d_(p−2)) 外，其余全部交错均由该构造关闭。唯一未自动关闭的位置还须有实际

\[
B_p\bigl((D\setminus\{d^*\})\cup\{v,w\}\bigr).
\tag{36}
\]

证明：Y 共 p+1 点，任何 Bp 若只用一个外供，必用全 D 而终于源 d*，不可能。所以必须用两外供，且唯一省略的 D 点只能是 d*；蓝路径形状 D_L<V_C<d 又迫 v、w 同处倒数第二 gap。这是剩余位置说明，不是新增排除。

结构证明后代 p=5：前三 gap 各至多 1 个外供，最后 (d3,d4) 任意外供均可分划；两个外供只剩同时位于 (d2,d3)，且相应五点全蓝的情形尚未由该构造关闭。

### 7.3 singleton 正确但严格全部 bases 背景为空类

上一轮 singleton 外供分划推论本身正确，但在这里的严格全部 minimum-bases 背景中，该 singleton 结构为空类，不能再计作实质临界覆盖。

若唯一 v∉G 属于每条 s-private 红 H，则 S'=(S∖{s})∪{v} 命中全部红：非 private 成员由 S∖{s} 命中，private 成员由 v 命中。|S'|=p=τ，所以 S' 也是 minimum basis，迫 v∈G，矛盾。

本轮多外供定理避免只处理这个已知空类，但仍不声称任意 critical 必然进入完整 F 背景；旧稿保持原字节，不回写。

### 7.4 极端分离块外供整类排除

若 G∖A<A，即全部其他整块都在 A 左侧，则任意 basis 的 A 位必有 G 内 private。

取 A 最前 pair a1<a2。若每个其他块都有一点 c 使 χ(c,a1,a2)=B，从各块选这样的点便得到 B_(p+1)：distinct-block 三元组由 product basis 为蓝，含 A pair 的三元组由选择为蓝，矛盾。因此某整块 B≠A 的全部 c 都对该 pair 给红。每 c∈B 均在 A 左侧，所以 c+A 是实际 R_(p+1)：首三元组红，其余在 A 内也红。

B 至少两点，选 c 不等于该 basis 的 B 代表，则 A+c 属于完整 F，且与 basis 只交 s，为 G 内 private。故“该 A 位全部 private 均为外供”的极端分离类不可能。反序的最左块同理。

不能把全部其他块在一侧弱化为仅当前 D<A，也不能套用于删减 F 或 MUS。上述竞争路线均未证明任意 critical 进入这些背景，无独立数值 saving。

## 8. 参数后数字、覆盖范围与剩余目录

本轮确实关闭两个整类：

- 全部 onefull：任一方向 η0，另一侧 η≤2 的全部机制，包含 Ω、δ 与 M*；其中旧 δ0、高端点等重叠覆盖不重复计收益。
- 全部双正缺额 nonΩ/M0：双侧 η∈{1,2} 且双侧新 Ω*=∅、M*=∅，覆盖 (1,1)、(1,2)、(2,1)、(2,2)。§3—4 的正错位是其中独立短证明，不重复计覆盖。

若 n=3b+3 的 counterexample 仍存在，两个归一化方向都 η≥1，且至少一方向的新 Ω* 或残余 M* 非空。下列真正双正例外及其他入口仍未关闭；不声称已找到任何含 Ω/M* 子类的实例：

| 参数/机制 | 本轮边界 |
|---|---|
| 两方向 η≥1，至少一方向新 Ω* 或残余 M* 非空 | 真正双正例外仍开放；不能称全部临界机制已闭 |
| 合法 rootcycle 的临界 positive-through | 尚未证明 |
| 完整 F 新构造 | 尚无任意 critical 进入其完整背景的证明 |

本轮 actual 端点图方法解决旧“选定 pure 供应未必接 middle”的接口：从容量迫出全部 pair 图的实际 matching，再与 middle 交会。下一最高优先级是带真实锁点的双正缺额，兑现扩域全部首/末 pair 与完整端口损失；尤其不能把 Q0 终点已排误认为它不能作末前驱。继续保留完整 F 区间重分划竞争，不再把 onefull 早独占延长或无异常正错位作为开放主攻。

既有参数工作式仍为

\[
|X|+w\le3b+3,\qquad
N_{\rm sig}(7,6,7)\le3b+3,\qquad
N_{\rm sig}(7,7,7)\le3b+4.
\tag{37}
\]

最后代入既有用户授权工作输入 b=25：

\[
N_{\rm sig}(7,6,7)\le78,\qquad
N_{\rm sig}(7,7,7)\le79.
\tag{38}
\]

全局 77/78 尚未证明。b=25 证书本轮未重验证，未读取新证书，旧报告与 accepted 层级不升级。本轮额外无条件数值 saving 仍为 0；全部 onefull 与全部双正缺额 nonΩ/M0 的统一排除是新的结构进展，不把其重叠覆盖、正错位短证明或竞争路线重复计入数值收益。

## 9. 保证、文档回执与保护状态

全部新增 unreviewed/unaccepted；同会话生成与交叉核对不构成独立数学 review。指定 native Sol/high 仅忠实文档执行；未报告的 backend 与实际 effort 不声称核实。文档 PASS_DOCUMENT_ONLY 不认证数学，不升级任何旧接受或 assurance。

回执为 `tmp/n7_endpoint_pair_hall_20261102/DOCUMENT_CHECK.json`。检查限严格 UTF-8、公式 tag 唯一连续、本地链接可读、参数代入字符串及手工算术一致、四份数学保护稿与 task.json 的当前 SHA256、status、completedAt，以及指定两新路径。

未调用外部 Claude，未向外传材料，未执行研究代码、枚举、SAT、solver 或 proof 检查。旧五保护文件、入口、metadata、接受/assurance、绑定、runtime、运行与指针保持；任务仍为 in_progress、completedAt=null。不 commit、不 archive；长期任务未完成。本文已由主会话全文通读及落实指定精度修正；这不构成独立数学审阅。
