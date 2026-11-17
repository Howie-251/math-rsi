# N7：完整实际 pair 扇的边界预算与紧核二分

日期：2026-10-29。本文为主会话 Astra 与三名授权生成协作者确定数学后的完整转写，全部新增 **unreviewed/unaccepted**；执行者仅作文档与文件一致性检查，不构成独立数学审查。没有新全局上界，没有实际 X50 反例，也没有排除任何完整 m 分支。科学运行、solver、proof checker 与 Closure 获取均为零；指定深审有一次平台工具尝试，被自动审批拒绝；没有 jobId、没有 Claude 数学响应，完成独审数为零。新增数学仍未独立审阅、未接受。

## 1. 结论与来源归属

本轮主结果是对完整临界母体中的**每条实际路径**施加支持限制：两色诱导端点图都严格 Hall 时，任一实际 c 路径的每个内部点对 x<y 必须满足

\[
|L_{\ge x}|+|D_{\le y}|\ge2.
\]

这个限制来自同一实际三元颜色在相同 owners 上的完整互补扇，而不是只选一份匹配的见证。若实际载体的内部 pair 完全居中，则两图同时产生非平凡紧集，载体端点边不属于任何完美匹配，并得到两个实际满核分割；这条逃逸仍开放。边界数为一时，无需可延拓假设，两个 slack 分支均迫至少一图的明确非平凡紧集；可延拓子类进一步得到相反色无长路径的实际满紧核及其插点端点化。

生成来源为 [A：Hall 紧核](N7_BRANCH_A_HALL_TIGHT_CORES_20261029.md)、[B：严格 Hall 支持](N7_BRANCH_B_STRICT_HALL_SUPPORTS_20261029.md)、[C：临界阻挡修复](N7_BRANCH_C_CRITICAL_BLOCKER_PROPAGATION_20261029.md)。其中 A/B 的最终跨线段落已纳入完整扇结果，不能把其前段探索性定位重计为独立突破。此前主入口是 [2026-10-28 饱和接口稿](N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md)。本次所读主来源中，分支稿以前的主承重稿仍为该 Oct28 稿；这不是整个工作区或外部文献的穷尽检索。

旧归属精确保留：[R23 §5](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md) 给全族四核饱和与纯互补供应；[R3 §6.3](RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md) 给同实际端点支持矩形及同中间边可靠拼接；[R22 §5.1](RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md) 给全路径横截到单色端点匹配；Oct28 稿给两个诱导图的边不交完美匹配。Hall、packet gluing、单匹配和双匹配本身均非本轮新结果。本轮新推导使用**同一 owners 上全部实际三元扇的颜色互补性**，旧 pure-through pair-shadow 不表达这一完整恒等式。本文不作相对于全部文献的正式新颖性声明。

## 2. 一般参数与完整饱和入口

先取整数 p≥4、n=p+2，令 b 为完整模型 N_sig(n,p,p+1) 的有效上界。设 X 是同一个完整有序 rank-3 signotope，|X|=2b，无红(p+1)、蓝(p+1)及 weak n。路径长度计顶点数；packet 次序为 abc,abd,acd,bcd，至多换色一次。同色路径对子序列遗传。weak 始终使用同一实际首末点，反色长度和达到 n+2 可保端点缩短得到禁形。

令 S_c、E_c 为 X 内全部实际 c-p 路径的首点、末点集合。若一个点同时是蓝 p 的末点和红 p 的首点，取前者最后一条边及后者第一条边的相邻三元，任一颜色都会延长对应路径，违反单色(p+1)禁形。故 S_R∩E_B=S_B∩E_R=∅。E_B 内无红 p，否则其红首点带有蓝 p 前供，出现同样连接禁配；X\E_B 内无蓝 p。两部分各落在容量 b 的颜色对偶域中，总人口为 2b，故都恰 b。再由 X\S_R 无红 p 及 S_R⊆X\E_B，得到 S_R=X\E_B；换色同理。

因此

\[
S_R\sqcup E_B=X=S_B\sqcup E_R,\qquad
|S_R|=|S_B|=|E_R|=|E_B|=b.
\]

每个 v∈E_B 的实际 S_R+v 有 b+1 点，容量迫蓝 p；其末点只能是 v，得到全部实际 B_p(S_R^{p-1},v) 供应。每个 u∈S_R 同理有全部 R_p(u,E_B^{p-1}) 供应，另两族换色。这一说法保存所有替代见证，不固定方便的一条。

定义

\[
L=S_R\cap S_B,\quad D=E_R\cap E_B,\quad
T_R=S_R\cap E_R,\quad T_B=S_B\cap E_B,
\]

则四原子互斥覆盖 X，且

\[
|T_R|=|T_B|=m,\qquad |L|=|D|=k=b-m.
\]

设 Y_c=X\T_c，H_c 为在 Y_c 内重新按实际三元颜色定义的全部 c-p 路径的 L×D 端点图。路径内部可同时使用多个 L、D 及相反 through 点；不是 ambient 图删端点后继承路径，更不是只保纯供应。

任意横截 Y_c 中全部 c-p 的集合 Z 删后进入容量 b 域，故 |Z|≥|Y_c|−b=k；删除 L 达到 k。对 U⊆L，(L\U)∪N_Hc(U) 横截全部这些路径，因此 k−|U|+|N_Hc(U)|≥k，得到 Hall。若最大匹配未覆盖 L，从未匹配左点沿交替路到达左集 U 及全部邻集，不能到达未匹配右点，否则可增广，故 |N(U)|<|U|，矛盾。所以两图各有完美匹配。两色不能共享实际端点边，否则红 p+蓝 p 长度和 2p≥p+4=n+2，违反 weak。这里只保证端点互异，不保证内部不交。

## 3. 完整三元扇与精确边界恒等式

对**任意实际点对** x<y 及颜色 c，定义

\[
A_c=\{l\in L:l<x,\ \chi(l,x,y)=c\},\qquad
D_c=\{d\in D:y<d,\ \chi(x,y,d)=c\},
\]

\[
s_c=k-|A_c|-|D_c|,\qquad
e=e(xy)=|L_{\ge x}|+|D_{\le y}|.
\]

若 x 或 y 本身属于端点原子，e 中非严格不等号仍必须保留。每个实际三元恰有一色，故在同一 owners 上

\[
A_R\sqcup A_B=L_{<x},\quad D_R\sqcup D_B=D_{>y},\quad
\boxed{s_R+s_B=e}. \tag{1}
\]

对 l∈A_c、d∈D_c，packet(l,x,y,d) 首尾同 c，四项全 c，得到实际 c4(l,x,y,d)。它与同实际端点的相反色 p 长度和为 4+p=n+2，故

\[
H_{\bar c}\cap(A_c\times D_c)=\varnothing. \tag{2}
\]

H_bar_c 的任意完美匹配中，从 A_c 出发的 |A_c| 条边与进入 D_c 的 |D_c| 条边由 (2) 互不重复。因此 s_c≥0，并且**恰好 s_c 条**匹配边位于

\[
(L\setminus A_c)\times(D\setminus D_c). \tag{3}
\]

这不是内部资源计费，是任意完美匹配中的精确端点计数。

称实际边可延拓，是指它属于某个本色完美匹配。若 Y_c 中一条指定实际 c-p 路径 P 内部包含 x,y，且其端点边可延拓，将该边扩成完美匹配并保留指定 P 作为见证，其余匹配边见证任意选择。P 的首点不在 A_bar_c、末点不在 D_bar_c，因为相应三元颜色均为 c。因此该匹配在 (3) 的相反色指标矩形中至少有一条边，即

\[
\boxed{s_{\bar c}\ge1}. \tag{4}
\]

指定见证不能被换掉，其余全部替代见证均未受限制。

## 4. 严格 Hall 的所有实际路径限制

严格 Hall 指对每个非空真子集 U⊊L，有 |N(U)|≥|U|+1。先设指定 P 的边可延拓，且相反图 H_bar_c 严格 Hall。P 的首末点保证 A_c、D_c 均非空；由 s_c≥0，两者均为真子集。由 (2)

\[
|A_c|+1\le |N_{H_{\bar c}}(A_c)|\le k-|D_c|,
\]

所以 s_c≥1。结合 (1)、(4)，得到 e≥2。

再证明严格 Hall 图的每条实际边均可延拓。删除边 (l,d) 的两个端点后，任意非空 U⊆L\{l} 在原图有至少 |U|+1 个邻点，删去 d 后仍有至少 |U| 个邻点；空集条件自动成立。余图 Hall 成立，有完美匹配，补回 (l,d) 即得原图完美匹配。该论证不需要 Ferrers 结构或实际路径 uncrossing。

**主定理。** 在第2节完整一般参数入口下，如果 H_R、H_B 都严格 Hall，则每个 Y_c 中的每条实际 c-p 路径，以及该路径内部的每一实际点对 x<y，均满足

\[
\boxed{e(xy)=|L_{\ge x}|+|D_{\le y}|\ge2}. \tag{5}
\]

证明的全称范围由逐条实际边可延拓保证，故不局限于预选匹配、预选纯供应或预选支持。它排除的是完整临界母体中的实际路径模式；没有证明每个该母体都被迫产生 e≤1 的内部 pair。这个支持密度进入问题是严格 Hall 路线的首次缺口，不能省略后宣布整个严格分支不存在。

## 5. 零边界与一边界的精确紧核逃逸

**零边界，不预设可延拓。** 若某条 Y_c 内实际载体路径的内部 pair 满足 e=0，则全部 L<x<y<全部 D。由 (1) 及 s_R,s_B≥0，二者均为零。载体使 A_c,D_c 非空，而其大小和为 k，故均非空真集；此时完整互补性使另两扇也非空真集。由 Hall 与 (2) 同时得到

\[
N_{H_R}(A_B)=D_R,\qquad N_{H_B}(A_R)=D_B. \tag{6}
\]

因此两图都具有非平凡紧集。每个 H_c 完美匹配必须把 A_bar_c 全部匹配至 D_c，不能使用载体从 A_c 到 D_c 的边。故载体边不可延拓；同样推理适用于携带此 pair 的每条实际载体。

还有两个实际满核

\[
W_R=A_B\cup T_B\cup D_B,\quad
W_B=A_R\cup T_R\cup D_R. \tag{7}
\]

每核人口为 k+m=b，互不交且并为 X；W_R 无红 p，W_B 无蓝 p。以 W_R 为例，它位于 Y_R，任何内部红 p 必首于 A_B、末于 D_B，但其端对被蓝4矩形禁止。另一色同理。载体内部 pair 不在 L 或 D，又避本色 T_c，故 pair⊂T_bar_c。载体穿越两个满核的支持与这些内部禁形相容，没有矛盾。特别地，零边界载体不可能与任意一图严格 Hall 共存，但双紧逃逸仍在。

**一边界，无可延拓假设的完整二分。** 任意实际 c 载体若 e=1，两个非负整数 slack 只有两种可能。若 s_c=0、s_bar_c=1，载体保证 A_c,D_c 非空，由其大小和 k 及矩形禁边、Hall 直接得到 (8)，不需要载体可延拓。若 s_c=1、s_bar_c=0，则 |A_c|+|D_c|=k−1，载体使两项均≥1，故各≤k−2。令 ell=|L_<x|、t=|D_>y|，因 (k−ell)+(k−t)=1，二者各≥k−1。完整颜色互补性因此给

\[
|A_{\bar c}|=\ell-|A_c|\ge1,\quad
|D_{\bar c}|=t-|D_c|\ge1.
\]

又 s_bar_c=0 使其大小和为 k，故两者是非空真集，并且

\[
N_{H_c}(A_{\bar c})=D\setminus D_{\bar c}. \tag{8a}
\]

于是本色图有明确非平凡紧集。精确补矩形计数在此为零，而载体端点边位于 (L\A_bar_c)×(D\D_bar_c)，故该边不可延拓。两种情况穷尽：**任意一边界实际载体均迫至少一图非平凡紧，零边界载体则迫两图均非平凡紧。** 因而主定理 (5) 也可不经过逐边可延拓引理，直接由本二分与零边界结论证明。第一种 slack 情形不反过来保证载体可延拓；混合情形整体仍未解决。
**一边界，可延拓载体。** 若 e=1 且 c 载体边可延拓，则由 (4) 得 s_bar_c=1、s_c=0。A_c,D_c 非空真集，且

\[
N_{H_{\bar c}}(A_c)=D\setminus D_c,\quad |A_c|+|D_c|=k. \tag{8}
\]

所以 A_c 是相反图的非平凡紧集。实际核

\[
W=A_c\cup T_c\cup D_c \tag{9}
\]

人口 b，无相反色 p：W⊂Y_bar_c，任何相反 p 的首末点只能落在 A_c,D_c，与 (2) 矛盾。x,y 均在 W 外，故容量 b 迫 W+v 中存在相反色 p（v=x 或 y）。所有这种路径都用 v，并且 v 必为实际端点，否则其首末点仍落在被禁矩形。这也覆盖 v 属于 through 原子的情况；不能据此声称两个方向都存在。

因此，可延拓的一边界 c 载体与相反图严格 Hall 不可能共存。任意一边界载体均与双严格不相容。一边界不可延拓边现由上述完整二分覆盖其紧集入口；它不自动满足本段 s_c=0 的特定 W 插点结论。混合紧/严格与双紧整体仍未排除。

## 6. 紧核缺角与插点尝试的首个缺口

普通匹配事实给：有完美匹配的二部图中，边 (l,d) 不属于任何完美匹配，当且仅当存在紧 U⊆L，满足 l∉U、d∈N(U)。正向由删除 l,d 后 Hall 失败：某 U 的 |N(U)\{d}|<|U|，原图 Hall 迫 |N(U)|=|U| 且 d∈N(U)。反向则每份完美匹配必须把 U 配满 N(U)，不给 l 使用 d。

对实际 H_B 的此类边，令 W_U=U∪T_R∪(D\N(U))。其人口 b 且无 B_p。容量对两次实际插点分别迫

\[
Q:l\longrightarrow d',\ d'\in D\setminus N(U),\quad Q\subseteq W_U+l,
\]

\[
R:l'\longrightarrow d,\ l'\in U,\quad R\subseteq W_U+d. \tag{10}
\]

源终定位由 ambient 身份与紧集禁边得到；保存所有 Q、R 替代见证。缺角 (l',d') 不能是实际 H_B 边。p=5 时，若 Q、R 在 (l',d') 内共有三个实际内部点，旧 packet gluing 会给 W_U 内的 B5(l',d')，矛盾；只有共同 pair 时只给 B4，尚不违反 B5-free。原载体 P 的支持可能完全不同，不能自动提供第三点或合法的额外延长。因此 (10) 的真实三条路径仍可能共存，尚未证明所有实际边都可延拓。

紧集在交、并下闭合是旧 Hall 子模结论，不是 laminarity。A 分支的支持松弛 J_F 仍只是旧全路径横截下界 τ≥r−|F| 加 H_F⊆J_F 的过近似，不能作主新增收益。首次缺口是没有迫足够实际反色供应关闭全部剩余三槽支持。

另外，偶数 k 时若 k/2 条同色匹配见证共享内部 pair，矩形达到半匹配等号，确实得到另一色满核以及插点端点定位，尚无矛盾。以蓝载体、反色红插入为例，红5终于 x、红5始于 y 的模式，利用禁红6可迫连接边蓝；即使原载体在 x,y 之间另有 z，packet 也仅给替代 B5(a,x,z,y,b)，不是 B6 或 weak7。另一朝向的共享 pair 只给 R4；除非其端对恰为原蓝5匹配边，否则 R4+B4 总长八，也不是 weak7。没有迫共同第三点、匹配端点一致或额外延长；所有方向与替代见证均保留。

## 7. 次要推论：同 pair 的两色匹配出现次数

任取两色完美匹配并为每条边任选实际路径见证，令 q_R、q_B 分别为内部含 x,y 的红、蓝见证数。第3节精确计数立即给

\[
q_R\le s_B,\quad q_B\le s_R,\quad q_R+q_B\le e. \tag{11}
\]

q_R 条红见证的 q_R 个首点 I、q_R 个末点 J 由共享 pair 给完整红4矩形；蓝匹配避开 I×J，从 I 出发与进入 J 的各 q_R 条边不重复，剩余 k−2q_R 条才可能携带蓝 pair，故 q_B≤k−2q_R。换色得

\[
2q_R+q_B\le k,\quad q_R+2q_B\le k. \tag{12}
\]

在并图任意长 2h 的交替圈上，对其 h 个首点、h 个末点重复同一证明，得 q_{R,C}+q_{B,C}≤⌊2h/3⌋，覆盖所有圈长。交替圈是二部图圈，不是有向实际路径圈。两色都携带同 pair 时 pair 必属于 Y_R∩Y_B=L∪D，但内部可共享多个 owners，(11)—(12) 始终不提供独占资源收费。本节为次要必要式，不替代主定理。

## 8. 独立竞争线：同一临界赋值的完整阻挡修复

本节使用 767 母体：无 B6、R7、weak7。将角色划分为 K⊔Y，每条实际红6要求同时遇 K、Y，每条蓝5要求遇 K；F 为按完整路径要求计的包含极小不可满足族，红的两个要求仍捆绑。

若 Q=(q1<⋯<q5) 为 F 中蓝5，固定满足 F\{Q} 的同一赋值 σ，则 Q⊂Y。单翻 qi 到 K 只能新造某条红6全 K，故存在 Ri∩Y=Ri∩Q={qi}。五条 Ri 不同。其区间共同支持由旧 packet+同端 weak 给

\[
|(R_i\cap R_j)\cap(q_i,q_j)|\le5-(j-i). \tag{13}
\]

确实若共享 h≥2 点，首尾红 packet 补齐 qi,H,qj 的红(h+2)，与 Q 的蓝(j−i+1) 总长 h+j−i+3≤8；h≤1 自动符合。

对固定 q∈Q，必须修复**所有**红6阻挡

\[
\mathcal A_q=\{A\in F:A\text{ 红6},\ A\cap Y=\{q\}\}.
\]

令 S⊆K，同时翻 q 到 K、S 到 Y。新赋值满足 F，当且仅当 S 横截每个 A\{q}，并且不存在避 q 的路径 T∈F，其原 K-trace 非空且包含于 S。第一条件恰修掉可能全 K 的红6；第二条件恰排新全 Y 的红6或蓝5，穷尽全部失败类型。

取包含极小横截 S。F 不可满足迫某 T 避 q 且 ∅≠T∩K⊆S。每个 x∈S 有 private 红6 A_x∈A_q，A_x∩S={x}；因此

\[
A_x\cap T=\{x\}\ (x\in T\cap K),\qquad
A_x\cap T=\varnothing\ (x\in S\setminus T). \tag{14}
\]

若 T 为红，t=|T∩K|，与蓝 Q 最多共享两点（否则同一三元同时两色），所以

\[
|T\cap(Y\setminus Q)|\ge\max(0,4-t).
\]

若 qa,qb∈T、a<b，则同端两色子链的 weak 限制给

\[
\operatorname{rank}_T(q_b)-\operatorname{rank}_T(q_a)\le6-(b-a). \tag{15}
\]

这些都是同一 σ 下的支持数，不逐次收费。若 F 纯红6，删除任一红 Q 后可全局交换角色令 Q⊂Y，同一完整阻挡/极小横截框架仍成立，但没有蓝 seed，既无 |T∩Q|≤2，也没有 (15) 的反色同端预算，分支仍开放。

关键停止处是：修复后的赋值可能同时违反**多条**路径，不能视为满足 F\{T} 的新临界赋值，因此不能无条件迭代五阻挡引理。private 交为 singleton，也不给紧核路线需要的共享 pair。C 分支没有证明更小 z；其“未采用普遍 z≤5 证明”仅表示本分支未重证，绝不挑战旧 R7 链已保留的 z≤5 基线。本轮 z 不变。

## 9. 三轮实质推进与停止理由

| 推进轮次 | 确实留下的数学 | 失败后的改向理由 |
|---|---|---|
| 第一轮：紧核、严格图、临界阻挡并行生成 | A 保留实际紧核插点定位与全支持删点；B 分析两色匹配支持；C 给完整 A_q 修复判据 | J_F 是旧 τ 加松弛；裸图严格 Hall 不构成实际染色矛盾；修一个选中阻挡不能修全族 |
| 第二轮：保同 owners 的完整扇 | 任意 pair 的 s_R+s_B=e、精确补矩形匹配计数以及所有实际路径的两严格边界限制 | pure-through shadows 缺完整互补；选中匹配计数不能擅自覆盖全部实际路径，须逐边可延拓证明 |
| 第三轮：检验逃逸与闭合 | e0 强迫双紧、不可延拓边和双满核；e1 任意载体按两种 slack 迫至少一图紧，可延拓子类给相反紧核及插点端点化；C 留同赋值 private 关系 | 缺角仅共享 pair 不给 B5；插入替代 B5 不给 B6；MUS 新赋值可多重违反，无法迭代临界下降 |

这三轮不是新增全局界的三次下降。精确排除类为：双严格下实际路径内部 e≤1；任一图严格时的零边界实际载体；相反图严格时的一边界可延拓载体。混合与双紧整体未解，所有剩余 m 分支未解，没有实际 X50 反例。停止裸图严格 Hall 矛盾、共享 pair 自动 B5 和新 MUS 赋值自动临界化三种推法。

## 10. 基线证据与数值结算

限定模型 a=16、b=25 的地位与新结构草稿分开。b25 的 [C8 人工正式验收记录](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) 明载 C1—C10 全部 accepted、pending 空；assurance 仍 same-family/provisional，exact backend/model/actual effort 不可验证。它不是无条件几何 Erdős–Szekeres 极值结论。旧结构链 40/50/80/81 仍属其原草稿层级，本轮不升级。

[Through14 历史重放元数据](../../../../tmp/balanced49_abstract_port_20261026/through14_replay_result.json) 为固定字节 strict-RUP PASS；[Joint17 公式绑定](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json) 与 [完整 strict-RUP 结果](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json) 各保其范围。两者的全类语义迁移仍未独审、未接受。因此在 p5、n7、b25 时，9≤m≤13、12≤k≤16 仅作既有研究范围；主定理不需要这些数字。本轮只读元数据，没有证明重放。

[Closure schema 结果](../../../../tmp/n7_global_proof_completion_20261027/closure/result.json) 虽 PASS，actual_cnf_equality_checked=false、UNSAT_checked=false；[获取停止回执](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json) 为 ABORTED_BUDGET_FEASIBILITY，source_acquisition_complete=false、CNF_binding=false。C≤49 没有闭合。

最后才代入旧结构关系

\[
N_{757}\le a+b-1,\quad C\le2b,\quad Q\le C+b+5,\quad F=Q+1.
\]

代 a16、b25 仍为 40/50/80/81。新结构直接全局下降、递推传播下降及新外部界收益均为零；旧链收益不重计。

## 11. 文件边界与唯一下一问题

[来源清单](../../../../tmp/n7_full_pair_fan_20261029/SOURCE_MANIFEST.json) 在写本稿前固定有限明确读取源的当前字节与 SHA256，把三份新生成分支稿与历史源分列；不是全工作区审计，不按旧 hash 恢复。写后 [文档检查](../../../../tmp/n7_full_pair_fan_20261029/DOCUMENT_CHECK.json) 只核对这些源未变、链接、UTF-8 与基本公式分隔，非独立数学审计。未改历史/配置/接受/任务指针，没有提交、归档或 Trellis 本地脚本执行。

[ARIS README](../../../../.aris/README.md) 原文仍称两路线 disabled、review-runtime activated=false；当前 review-runtime.json 为 activated=true，当前 .codex/config.toml 两路线 enabled=true、deep effort=max，而旧 validation/alt-g-config.json 仍记禁用。这是不同时间配置证据的差异；不能据旧 README 声称当前路线不可用。主会话指定的一次 deep review_start 尝试被平台自动审批拒绝：平台认为具体未发表内部研究材料向外部 Claude 服务的导出缺少明确授权。未取得 jobId 或任何 Claude 数学响应，服务端执行未获确认；没有重试、间接调用或改配置。完整拒绝原文与指定材料见 [审阅阻止回执](../../../../tmp/n7_full_pair_fan_20261029/REVIEW_BLOCKED.json)。因此本轮 completed_reviews=0、independent_math_review=false，正文仍 unreviewed/unaccepted；本地机械检查不替代独审。requested native Sol/high 为执行角色记录，backend/actual effort 不能从角色名自动验证。
唯一下一问题是：**在同一完整饱和临界 X 中，实际端点边是否可能被排除于所有完美匹配之外？等价地，紧核缺角所产生的三条实际路径，能否与全部四核纯供应同时共存？** 需要在实际 packet 合法支持上证明额外延长或矛盾。零边界双紧逃逸与第6节缺角推导使这个问题具体化；解决它也不自动降低全局界，严格支持密度的首次缺口仍须保留。本文在这个问题处停止，不另列一般路线图。



