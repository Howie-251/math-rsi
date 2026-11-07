# N7：任意次序 product 禁形、全局根障碍与完整外供边界

日期：2026-10-30。状态：**本轮工作稿；全部新增 unreviewed/unaccepted**。本文仅转写主会话批准的数学，文档执行者不自行补证。主会话与生成协作者的交叉核对不是独立审阅，不改变旧稿、接受或 assurance。本文已加入主会话批准的完整参数证明、合法根结构、条件分支排除及两项实际反例校准；现保存为本轮工作稿，不构成数学接受。

本轮主结果按参数表述：任意次序的 p 个大红块不能支持完整蓝 p product；在完整路径拟阵背景中，必存在一个 minimum basis 的某个位置，其每一条 private 红成员都触及 minimum-transversal support G 外；双满临界接口的全部 ambient 红六端点图及去掉共同点后的端点图均有 perfect 匹配，并且每个共同点都被后一图的真实红六严格跨越。下文给出批准证明，并单列未解边界。

无外部 Claude 或其他外部服务，无科学代码、枚举、SAT、solver、proof checker 或证书重放。PowerShell 只用于文档写入、UTF-8、链接、公式编号及固定算术检查；这些检查不认证数学。本轮唯一写入归属是本文及指定的文档检查回执，不修改其他文件。

## 1. 模型与依赖

主要依赖为 [共同根间隙、内部支持及交叠组件前稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_GAP_AND_INTERNAL_SUPPORT_OBSTRUCTIONS_20261030.md>)、[联合 through 与合法根循环前稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>)，以及 [完整重分块二分与拟阵背景](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §6。所有依赖保留原保证边界，不在本文重审或升级接受。

完整有序 rank-3 signotope 的 packet 对 a<b<c<d 按 abc、abd、acd、bcd 排列，至多换色一次。单色路径按实际顶点计长且对子序列遗传；同端禁形比较同一对实际首末点。767 禁 R7、B6、weak7；766 禁 R6、B6、weak7；换色 756 禁 R5、B6、weak7，其共同容量上界为 b。weak7 禁同实际端点反色路径长度和至少 9；p=5 时同时禁 R_(p+1)+B3 与 R_p+B4。

不同参数定理各自保留假设：§2 的任意次序大红块定理使用上述两种同端禁形；§4 的内部 private 选择族定理只需其中 R_(p+1)+B3，不额外要求 R_p+B4。两者均不从数值 p=5 起步。

## 2. 任意次序大红块 product 全排

### 2.1 完整参数定理

**任意次序 product 禁形定理。** 设 p≥3，完整 signotope 禁 B_(p+1)、R_(p+2)，以及同实际端点的 R_(p+1)+B3、R_p+B4。不存在 p 个两两实际不交的红块 Ai，使

\[
|A_i|\ge p\quad(1\le i\le p),\qquad
\{a_1,\ldots,a_p\}\text{ 为实际 }B_p
\quad\text{对每个 }a_i\in A_i. \tag{1}
\]

不要求拟阵、private 成员或块的次序分离。红块可以交错；每块至少 p 点是本定理的独立假设。

### 2.2 整块红见证及已证组件结构

固定某个 Ai 内部 pair x<y，必存在另一整块 Aj 对它全红。否则每个其他块各取一个 zj 使 χ(x,y,zj)=B，合上 x、y 得 p+1 点；含 x、y 的三元组按选择蓝，其他三元组来自三个不同块的完整 product，亦蓝，形成 B_(p+1)，矛盾。因此

\[
\forall i\ \forall x<y\text{ in }A_i\quad
\exists j\ne i\quad\forall z\in A_j:\quad\chi(x,y,z)=R. \tag{2}
\]

三元颜色始终按实际点次序读取。

前稿已证：某块开跨度中不能同时有来自两个不同外块的点 d<e，否则 packet(min Ai,d,e,max Ai) 首尾均由三块 product 为蓝，因而全蓝；其同端 B4 与 Ai 内含极点的红 p 冲突。

由此前稿进一步证明，闭跨度交叠图是 matching：每个连通组件只含一个块或两个交叠块，各组件的 union spans 按实际次序严格分离。若 A 同时交叠 B、C，而 B、C 各有点在 A 内部，则已矛盾；否则某 B 没有点在 A 内却跨度交叠，必严格包住 A。C 若有点在 B 内，B 内同时有 A、C 点；若没有，则 C 严格包住 B，C 内同时有 A、B 点，仍矛盾。实际端点全不同，没有相触例外。

最左组件为单块的情形也已在前稿完整排除：只近推 A 后全局最早两点 z1<z2，而不误推整个交叠组件。对 A 任意 pair，用 (2) 的整块见证及 (?,R,B,B) packet 得对 z1、z2 均红。若两点来自异块，A 内含极点的 p 点加 z2 所成红(p+1)，与 B3(min A,z1,z2) 同端冲突。否则两点同属 B；weak 迫 χ(min A,z1,z2)=R，红(p+2) 帽迫 χ(max A,z1,z2)=B。该 B pair 的整块红见证不能是 A，只能是第三块 C，而其点 c 晚于 z2。packet(min A,z1,z2,c)=RBBR 非法。因此最左组件不可能为单块。

下面补齐最左组件为交叠对的情形，从而不再留下上一轮的交叠对—单块—交叠对。

### 2.3 首交叠对的所有 2A+1B 三元组都红

设 A、B 构成最左交叠组件，重命名使

\[
a_0=\min A<\min B=b_0<\max A,\qquad
\text{所有其余块全部在 }A\cup B\text{ 右侧。} \tag{3}
\]

这里 b₀ 是实际点，不是容量参数 b。任取 A 内 pair x<y，按 (2) 选其整块红见证。

若 y<b₀，见证为 B 时直接得到对整个 B 红；若见证为外部块 C，任取 z∈B、c∈C，实际顺序 x<y<z<c，packet(x,y,z,c)=(?,R,B,B)，迫 χ(x,y,z)=R。z 任意，仍得到对整个 B 红。

若 y>b₀，外部见证 C 不可能。取 c∈C，分两类：

- x<b₀<y 时，packet(x,b₀,y,c)=(?,B,R,B)，无论首项取何色都非法。
- b₀<x<y 时，packet(a₀,x,y,c) 首尾为红，故全红，特别 χ(a₀,y,c)=R；再看 packet(a₀,b₀,y,c)=(?,B,R,B)，仍非法。

因此 y>b₀ 时红见证只能为 B。两块实际不交，所以不存在 y=b₀ 或 x=b₀ 的相等例外。综上

\[
\chi(x,y,z)=R\quad\text{对所有 }x<y\text{ in }A,\ z\in B. \tag{4}
\]

本步骤只对 A pair 向 B 作有根据的整块推导，不把最早两点的近推直接冒充整组件推导。

### 2.4 B 的末 pair 见证与最终矛盾

取 B 的最后两个点 u<v。若有任意外部点 c 使 χ(u,v,c)=R，在 B 中选含 min B、u、v 的 p 点并追加 c，得到以 min B、c 为实际端点的 R_(p+1)。同时

\[
\min B<\max A<c,\qquad B3(\min B,\max A,c), \tag{5}
\]

蓝色由三个不同块的 product，违反同端 R_(p+1)+B3。

所以 B 末 pair 对所有外部块的点均蓝，其 (2) 中的整块红见证只能为 A。取任意 p 个 A 点并合上 u、v：A 内红；2A+1B 由 (4) 红；1A+2B 由该整块见证红。所得 p+2 点全红，违反 R_(p+2)。

最左组件无论是单块还是交叠对都不可能。任意次序 product 禁形定理成立；上一轮 p=5 剩余的交叠对—单块—交叠对现已完整排除，但仍只在 (1) 的大红块完整 product 假设下。

## 3. minimum-transversal 支持界的参数收益

在具有上述完整 product 假设的纯 rank 1 支持表示中，恰有 p 个实际红块，所有 bases 是从各块选一点的蓝 p product，每块大小至多 p+1。§2 迫至少一个块大小至多 p−1。

旧单锚定理还给出至多 p−2 个块可满 p+1，故至少另有一个块不满、大小至多 p。合计

\[
|G|\le(p-1)+p+(p-2)(p+1)=p(p+1)-3. \tag{6}
\]

含 rank 2 的旧支持界保留

\[
|G|\le p^2-1. \tag{7}
\]

先保留参数式，再代 p=5：

\[
\text{纯 rank 1： }|G|\le27,\qquad
\text{含 rank 2： }|G|\le24. \tag{8}
\]

27 与 24 只是全部 minimum-transversal-support 的大小界，不是 UNSAT 核大小，更不是全局 N 收益。不把短块结论外推到没有上述完整 product 假设的任意配置，也不删除 G 外点或原完整约束成员。

## 4. 无分离的内部 private 选择族禁形

### 4.1 完整背景与准确量词

设 p≥3，完整 signotope 禁 B_(p+1)、R_(p+2) 及同实际端点的 R_(p+1)+B3。本节不额外要求 R_p+B4，也不要求组件顺序分离。

设完整路径角色约束族 F 为 UNSAT：每个红成员 H∈F_R 是实际红(p+1)，必须同时遇两侧角色；每个蓝成员是实际蓝 p，必须遇指定一侧；两侧角色分划全部实际点。假设 τ(F_R)=p，全部 minimum 红横截族 ℬ 满足基交换，定义

\[
G=\bigcup_{S\in\mathcal B}S. \tag{9}
\]

继承原已证规范化 rank 1 / connected rank 2 红组件、每块大小至多 p+1、所有 basis 为蓝 p、红 G-trace 含 cocircuit 且 rank 至多 2 等结论。恰含两个 parallel classes 的 rank 2 部分拆为两个 rank 1 组件；不假定拆分后的组件仍分离。

完整 trace 背景保留：rank 2 cocircuit 具有 rank 2，含它的 trace 只能在本块；rank 1 cocircuit 是整块，之外至多再占一个其他块的 rank 1 子集，可能是另一 rank 1 块的一部分，也可能是 rank 2 块单个 parallel class 的一部分。全部 F 成员都保留。

**无分离内部 private 选择族禁形定理。** 在上述完整背景下，

\[
\exists S\in\mathcal B\ \exists s\in S\ \forall H\in F_R:\quad
H\cap S=\{s\}\ \Longrightarrow\ H\setminus G\ne\varnothing. \tag{10}
\]

即必有一个 minimum basis 的某个位置，该位置每一条 private 红成员都遇到 G 外。不把 G 当成 UNSAT 核。

其反证假设 I 是

\[
\forall S\in\mathcal B\ \forall s\in S\ \exists H\in F_R:\quad
H\cap S=\{s\},\quad H\subseteq G. \tag{11}
\]

这只要求每个位置至少选择一条内部 private，不是要求全部 private 都内部。

### 4.2 排除 connected rank 2 与 singleton

反设 (11) 的逐位置内部选择假设 I 成立。

**第一步：排 connected rank 2。** 在一个 connected rank 2 块内取 basis 点 s、t，扩成整个拟阵的 basis S，并按 I 选一条全在 G 的 s-private 红(p+1)成员 H。本块的 fundamental cocircuit 具有 rank 2，红 trace 的 rank 至多 2，故 H 全在本块。它避开 t，而块大小至多 p+1，所以 |H|≤p，矛盾。

于是恰有 p 个 rank 1 红块，所有 bases 为完整 product。任何全在 G 的 Ai-private 红成员都含整个 Ai，且至多再使用一个其他块。

**第二步：排 singleton。** 若 Ai={s}，对每个其他块 Aj，考虑所有内部红成员 {s}∪Q，其中 Q⊂Aj、|Q|=p。每个非空 Q 族都有公共点：若 |Aj|≤p，非空时唯一可能是 Q=Aj；若 |Aj|=p+1 且这些 Q 交集为空，必包含全部 Aj\{v}，v∈Aj。于是 s 与任意两个 Aj 点都包含于某条红 H，故 {s}∪Aj 全红，形成 R_(p+2)，矛盾。

对每个非空 Q 族，在其公共交中选 Aj 的 basis 代表；空族任取代表。连同 s 构成一个 minimum basis S。所有内部 s-private 红成员都被另一个所选 basis 点堵住，与 I 矛盾。因此每块大小至少 2。

### 4.3 不使用 R_p+B4 的跨度组件推导

**第三步：I 迫 span graph 为 matching。** 若一条内部红(p+1)成员 H 同时使用 Ai、Aj，其两个实际端点之间没有任何第三块的点 c。

若 H 的端点分别属于 Ai、Aj，三块 product 给同端 B3，与该 H 构成被禁的 R_(p+1)+B3。若两个端点同属一块，取 H 在另一块的点 z。z 也在两端之间。无论 c、z 的先后如何，按实际顺序读取四包“端点、c/z、z/c、端点”，首尾都因来自三个不同块而蓝，包含两端及 z 的项却因 H 红，直接违反 packet。

若 |Ai|≤p，假设 I 对 Ai 的一个位置提供内部 private H；它含整个 Ai，且必须再用另一个块。上段迫 Ai 开跨度内至多出现这一个其他块的点。

若 |Ai|=p+1，假设有两个来自不同外块的点 d、e 位于其开跨度。packet(min Ai,d,e,max Ai) 首尾由三块 product 蓝，故全蓝，得与 Ai 同端的 B3，违反 R_(p+1)+B3。

所以每块开跨度至多见一个其他块。按前稿严格区间论证，span graph 的连通组件至多两块，各组件 union spans 实际分离。每块至少 2，保证 min/max 不同；不同块的实际端点始终不同。此推导没有使用额外的 R_p+B4 禁形。

**第四步：完整 product 整块红见证。** Ai 的任何内部 pair 若对每个其他块都有一个蓝点，选出这些点便形成 B_(p+1)。所以每个内部 pair 至少有另一整块对它全红。这个步骤不要求块大小达到 p，也不要求分离。

### 4.4 首 single 组件不可能

**第五步。** 设最左组件为单块 A。

若 |A|≤p−1，在每个外块 C 选 max C 作 basis 代表，本块任取代表。由 I 选一条内部 A-private 红成员 H=A∪Q，其中 Q⊂C，且 Q 至少两点、避开 max C。所有外块全在 A 右侧；给 H 追加 max C 只新增一个全在 C 的红连续 triple，得到 R_(p+2)，矛盾。

若 |A|≥p，取 A 后全局最早两点 z1<z2。其他块至少两点，所以任意 A-pair 的整块红见证最大点至少为 z2。若 zj 在见证块中，直接红；否则用 (?,R,B,B) packet 近推，得所有 A-pair 对 z1、z2 均红。

取 A 内含 min A、max A 的 p 点。若 z1、z2 来自不同外块，A 所选 p 点加 z2 形成 R_(p+1)，与 B3(min A,z1,z2) 同端冲突。因此两点同属 B。weak 迫 χ(min A,z1,z2)=R，而无 R_(p+2) 迫 χ(max A,z1,z2)=B。

B-pair(z1,z2) 的整块红见证不可能是 A，只能是第三块，其点 c>z2，给 packet(min A,z1,z2,c)=RBBR，矛盾。首 single 的全部大小情形已排除。

### 4.5 首 pair 组件：所有 2A+1B 红

**第六步。** 设最左组件为交叠对 A、B，重命名使 a₀=min A<min B=b₀<max A，所有外块全在其右侧。

沿 §2.3 逐 pair 的证明：A-pair x<y 若 y<b₀，红见证 B 直接成立，外部见证则以 (?,R,B,B) packet 迫对整个 B 红；若 y>b₀，外部见证分别在 x<b₀<y 或 b₀<x<y 两种情形给非法 (?,B,R,B) packet，所以见证只能为 B。因此所有 2A+1B 三元组都红。该逐 pair 证明不需要块大小至少 p。

### 4.6 首 pair 组件：|B|≤p

令 k=p+1−|B|≥1，并定义 T 为所有使 B+a 全红的 a∈A。全部 2A+1B 红、B 内部红以及 T 的定义共同给 B∪T 全红，所以 |T|≤k。

一条内部 B-private 红成员若使用 A，必为 B∪Q，其中 Q⊂T、|Q|=k。因此只有 |T|=k 时才存在，且 Q=T。

若 |T|=k，在 T 中选 A 的 basis 代表；若 |T|<k，A 代表任取。每个外块 C 的 basis 代表都选 max C。本块 B 任取代表。

内部 B-private 若使用 A，前述选择已将它堵住。若使用外块 C，当 |B|≤p−1 时，其 Q 至少两点且避开 max C，可追加 max C 得 R_(p+2)；当 |B|=p 时，H=B+c，与 B3(min B,max A,c) 同端违反 R_(p+1)+B3。

因此这个 B 位置不存在任何内部 private，违反 I。

### 4.7 首 pair 组件：|B|=p+1

B 的末 pair 对所有外块点均蓝；否则向 B 追加该外点就得 R_(p+2)。该 pair 的整块红见证只能为 A。因此这对 B 点与整个 A 全红，迫 |A|≤p−1。

再取任意 B-pair x<y。如果 χ(a₀,x,y)=R，其整块红见证若是外块，取其点 c，packet(a₀,x,y,c)=RBBR，矛盾。所以这种 pair 的整块红见证只能是 A，即该 pair 对整个 A 红。

现取内部 A-private H=A∪Q⊂A∪B，|Q|≥2。若 v=max B 不在 Q，对任意 q∈Q，取另一个 q′∈Q。packet(a₀,min(q,q′),max(q,q′),v) 的首项由 H 红，末项由 B 内部红，故全红，特别 χ(a₀,q,v)=R。上一段于是给 pair(q,v) 对全 A 红。

结合全部 2A+1B 红、B 内部红和这些 1A+2B 红，H+v 全红，形成 R_(p+2)，矛盾。因此所有使用 mate B 的内部 A-private 都含 max B。

现在选 B 的 basis 代表为 max B，每个外块 C 的代表为 max C，A 内任取代表。使用 mate B 的内部 A-private 全被 max B 堵住；使用外块 C 的内部 A-private 至少取两个 C 点且避开 max C，可追加 max C 得 R_(p+2)，也不可能。因此这个 A 位置不存在内部 private，仍违反 I。

### 4.8 完整结论与机制边界

最左组件只可能是 single 或 pair；pair 的 |B|≤p 与 |B|=p+1 又穷尽原块大小上界。全部可能已排除，反证假设 I 为假，得到 (10)。

这是整个内部 private 选择机制的排除：必有一个 (S,s)，其每条 private 红成员都触及 G 外。它不是 F 本身 UNSAT 的排除，不删除任何 F 成员，允许任意 multi-private，也不需要 R_p+B4。

## 5. 两个完整 perfect 与共同点的严格跨越

### 5.1 双满临界接口

本节回到双满 critical 767 配置 X，使用全部 ambient 红六源和终点：

\[
|X|=3b+4,\quad
S=\operatorname{Src}_{R6}(X),\quad
T=\operatorname{End}_{R6}(X),\quad
|S|=|T|=b+4. \tag{12}
\]

令

\[
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T),\quad Y=X\setminus I,
\quad |P|=|Q|=b-q,\quad |Y|=3b-q. \tag{13}
\]

这里 q 是人口参数。本节不要求两侧五根或 τ5，因而覆盖全部具有该双满身份的 q、四根、τ4 及已真实 promotion 的亏一接口。未 promotion 的亏一分支不能直接套 (12)—(13)。

### 5.2 全部 ambient 红六端点图 S→T 有 perfect

以全部 ambient R6 构造端点图 S→T。若没有 perfect，König 定理给大小至多 b+3 的端点副本 cover。删去对应的实际点，所有 R6 都被命中；实际删除至多 b+3 点，余集至少 2b+1 点，且无 R6、B6、weak7，违反 766 容量 2b。

I 中同一个点可在左右副本重复出现，但实际只删除一次，所以副本 cover 的大小仍给实际删点数的正确上界。因此

\[
\text{全部 ambient R6 的完整端点图 }S\longrightarrow T
\text{ 有 perfect 匹配。} \tag{14}
\]

使用全部实际路径，不挑一组样本；匹配边的路径内部可以共享点。

### 5.3 Y 内部全部红六端点图 P→Q 亦有 perfect

Y 内部任何 R6 的首点在 S∩Y=P，终点在 T∩Y=Q。若完整端点图没有 perfect，König 给至多 b−q−1 个端点副本的 cover。实际删除至多这么多点，命中全部 Y 内 R6；由 |Y|=3b−q，余集至少 2b+1 点，成为超过容量的 766，矛盾。因此

\[
\text{Y 内部全部 R6 的完整端点图 }P\longrightarrow Q
\text{ 有 perfect 匹配。} \tag{15}
\]

此为前稿完整 Y 端点图结论的参数重述，不要求路径内部顶点不交。

### 5.4 每个共同点都被真实 Y 内红六严格夹住

任取 i∈I。取全 S→T 的任意 perfect 匹配，它覆盖 T_<i 及终点 i。红六边严格向前，所以这 |T_<i|+1 个终点的不同前驱均属于 S_<i。因此

\[
\delta(i):=|P_{<i}|-|Q_{<i}|
=|S_{<i}|-|T_{<i}|\ge1. \tag{16}
\]

再取 Y 内 P→Q 的任意 perfect。全部边严格向前，且 i 不在 P 或 Q，所以严格跨过 i 的匹配边数恰是 δ(i)：Q_<i 的全部前驱都在 P_<i，而 P_<i 剩余的 δ(i) 条出边恰通向 Q_>i。

因此对每个 i∈I、每个这样的 Y 内 perfect，都有一条真实 Y 内 R6 的两端 p₀、q₀ 满足

\[
p_0<i<q_0. \tag{17}
\]

这是严格夹在实际端点之间，不要求 i 本身在该路径上，也不要求不同跨边的路径内部不交。于是任何全 ambient 禁止 R6 跨过的 separator 都不在 I。

本定理给出真实跨越的必要结构，不会自动把一条跨越红六与前稿的具体 ports 配成同端 weak 禁形；端口交会仍是独立缺口。

## 6. 全 ambient 合法根结构与五根接口的条件排除

### 6.1 全部合法根是蓝 separator

沿前稿已证：固定同一交替符号 ω，全部合法 blue-root 集合 𝓡 的周期 3≤m≤6，每个 root 的 chart 唯一，合法 reroot 与 weak/cofactor 刻画可用；实际少数点身份在合法 charts 间不变。

固定 r 的 blue-root chart，取另一合法 root g。对所有 a<g<b，都有 χ(a,g,b)=B。否则 χ(a,g,b)=R，packet(r,a,g,b)=BBBR，唯一少数点为第三位 g；改到 g 的合法 blue-root chart，含根包只能 BBBB 或 BBBR，少数点从不在第一位 g，违反实际少数点身份不变。

所以每个合法 root 都是全 ambient 蓝 separator。若一条实际 Rk 的两端 a<b 之间有 t 个合法 roots，则 a、这些 roots、b 组成蓝(t+2)：任意三元组的中点都是合法 root。由同实际端点的 weak7，必有

\[
k+t+2\le8,\qquad t\le6-k.
\]

特别是，所有实际 R6 不能跨过任何内部合法 root，R5 至多跨一个合法 root。

### 6.2 相邻合法根的全点 edgefan 与唯一闭 gap

循环相邻合法 roots g→h 具有全点有向 edgefan：对所有其他实际点 z，ω(g,h,z)=B。证明从 h-chart 最右根 g 的已证归一化获得：原次序 h<z<g，root 三元组蓝，且循环换序给 ω(g,h,z)=ω(h,z,g)=B。

因此 h 是 g-chart 删根后全体点的实际 first，不只是根集中 first。最右实际点也是合法 root 已由前稿证明。故在任一删根配置 Yr 中，其余合法 roots 按次序 h1<⋯<h_(m−1) 排列，h1、h_(m−1) 恰是 Yr 的首尾点。

由蓝 separator，任何 R6 唯一落在某个相邻 roots 的闭 gap [hi,h_(i+1)]。一个开 gap 内部点的全 ambient 红六源/终身份，恰等于在该闭 gap 内重算的身份。边界 root 若启动 R6，只能进入右 gap；若结束 R6，只能来自左 gap。

### 6.3 连续三根之间的真实共享对象

若 g<h 是 r-chart 中相邻 roots，定义

\[
K(r;g,h)=\{x:\text{实际四点 }\{r,g,h,x\}\text{ 中，}x\text{ 是唯一少数点}\}.
\]

则 K(r;g,h)=Yr∩(g,h)。若 x 在该 gap 内，全点 edgefan 给 ω(g,h,x)=B，换序后 χ(g,x,h)=R，所以根包 BBBR 的唯一少数点恰是 x。反之，x 在 gap 外时，g 或 h 是中间 separator，根包第四项蓝，整个包 BBBB 平衡，x 不是唯一少数点。

少数点身份不随合法 chart 改变。因此当 r、g、h 是循环连续三根，同一实际集合 K 在 r-chart 中是 (g,h) gap，在 h-chart 中是 (r,g) gap。m=3 时，全体非根集是三个 charts 共享的唯一 gap。

这里只给出批准的共享对象，不声称一般换 root 后所有 gap 的分配都不变。

### 6.4 五根满接口中的中区间没有合法 root

设 X=Yr 是 critical 双满配置，w=0，两侧 E/F 各五根且 τS=τT=5。沿前稿已有共同根 x=e2=f3<y=e3=f4，以及实际 private 红六 R6(a*,E)、R6(F,b*)。

先有 e5=max(S∪U)。若存在 z>e5 且 z∈S∪U，由 E 右根 e4 得 χ(e4,e5,z)=R，追加到 private 根链成 R7。反向同理 f1=min(T∪V)。

两条 private 根链的开跨度 (a*,e5)、(f1,b*) 都含 (x,y)，它们的并集覆盖 (f1,e5)。合法 root 不能被真实 R6 严格跨越，所以这个开区间没有合法 root。端点 f1、e5 均在 I，又由 §5 的共同点严格跨越定理排除。因此

\[
\mathcal R\cap X\cap[f_1,e_5]=\varnothing.
\]

### 6.5 内部合法 roots 至多两个，故本子类 m≤5

任取 X 内部的合法 root g，即其左右均有 X 点。它不能启动或结束 ambient B5：全 ambient 蓝 separator 提供前接或后接的蓝桥，会形成 B6。

若 g∈D，满身份 Src_B5(H)=D\V 与 End_B5(H′)=D\U 迫 g 同时属于 U、V，违反 w=0。若 g∈I，§5 的真实红六严格跨越又排除它。因此 g∈P∪Q。

若 g∈P，则 P⊂S≤e5，而中区间 [f1,e5] 无合法 root，故 g<f1。若有 p₀∈P 位于 g 左侧，Y 内 P→Q 的 perfect 将 p₀ 匹配到 Q⊂T≥f1>g，得到严格跨 g 的真实红六，不可能。因此 g=min P，这类至多一个。

Q-root 反向同理，只能为 max Q，也至多一个。所以 X 内部合法 roots 至多两个；X 的非内部实际端点最多两个，再加被删除的 root r，得到本子类 m≤5。

未假设 X 首尾属于 P/Q，保留它们可能位于 D 的 U/V 中。由此完整排除“存在上述双满五根 τ5 chart，且 m=6”的子类。四根、τ4、未 promotion 的亏一不能套此结论。

### 6.6 根结构仍不提供无条件第二单位

§5 的共同点严格跨越定理覆盖全部双满 q、四根/τ4 与已真实 promotion 的亏一接口；§6.4—6.5 的 m≤5 则额外要求双满五根 τ5，范围更窄。

对完整合法 root 循环，仍继承

\[
3\le m=|\mathcal R|\le6,\qquad
|Z|+\max_{r\in\mathcal R}w(Y_r)\le3b+5. \tag{18}
\]

critical |Z|=3b+5 下完整循环必有 positive through 仍未证明。不把本子类 m≤5 写成全部 777 均 m≤5，不相加不同 chart 的容量，也不把 R6 当作换 chart 时只换端点的同色路径。主线端口交会仍未闭合。

### 6.7 m=5 剩余情形的准确停止点

本段只保存下一步上下文，归于开放接口，不计为新的整类排除。

在 §6.5 的全部假设下进一步令 m=5。X 中恰有四个合法 roots；两个内部合法 roots 必为 gP=min P<f1 与 gQ=max Q>e5，另两个为实际首 root u₀ 与末 root v₀。

首点不可能属于 Q，因为它不能结束 R6；不可能属于 I，因为共同点必须被红六严格跨越；也不能属于 P，否则会与内部点 min P=gP 重复。因此 u₀∈D，末点对偶得 v₀∈D。满角色 End_B5(H′)=D\U 与 Src_B5(H)=D\V 又分别迫 u₀∈U、v₀∈V，故 X 的合法根次序是 u₀、gP、gQ、v₀。

最早的 S 点若在 I，它的入 R6 必从更早的 S 点启动，矛盾。因此 min S=min P=gP；反向同理 max T=max Q=gQ。所有 R6 的源终端点于是都在中央闭 gap [gP,gQ]，全部红六也都位于这个闭 gap。

两外侧 gap 除中央边界根 gP、gQ 外的点全在 D。左侧点早于 f1，不能属于 V；右侧点晚于 e5，不能属于 U。因此各外侧 D 区均无内部 R5，继承无 B6、无 weak7，均为换色 756，分别具有容量上界 b。

但中央区容量尚不能与这两区组成产生正缺额的统一分解，五个 charts 的人口也不能相加。因此“所有五个 charts 均处 m=5 五根情形”仍开放；不能把进入四根或亏一分支当作矛盾。本段不升级为全局上界下降。

## 7. 两项完整实际构造的反例校准

本节两例均由主会话逐表手工复核批准，未运行颜色枚举、solver 或其他科学检查。它们远非临界，也不带满核；其作用是阻止把尚未证明的全局势函数或通用 uncrossing 当作现成工具，不反驳临界饱和目标。

### 7.1 十二点 777：完整合法根循环全 w0，源关系却有二环

**完整颜色。** 实际次序为 g<C5<r<P5，其中 C5={c1<⋯<c5}、P5={p1<⋯<p5}。凡含 g 的三元组全蓝；其余颜色按组成完整规定如下：

| 三元组组成 | 颜色 |
| --- | --- |
| CCC | B |
| PPP | R |
| CCr、CCP、rPP | R |
| CrP、CPP | B |

表内字母表示从对应块选互异点，并按实际次序读取；它覆盖所有不含 g 的三元组。

**全部 packet 与 777 帽。** 不含 g 的四点包只可能为 BBBB、RRRR、BRRR、RRBB 或 BBBR；含 g 的包为 BBBχ。因此全部 packet 合法。

删 g 得 Yg，其唯一红六为 r+P5；涉及 C 的红路径长至多 3，全部蓝路径长至多 5。同实际端点的全部路径长度界为：

| 端点类型 | 红长上界 | 蓝长上界 |
| --- | --- | --- |
| C—C | 2 | 5 |
| C—r | 3 | 2 |
| C—P | 3 | 3 |
| r—P | 6 | 2 |
| P—P | 5 | 2 |

各行长度和至多 8。加回蓝 root g 后，以 g 为端点的红长至多 2、蓝长至多 6，仍无 weak7；整体无红七、蓝七。因此得到完整实际 777 配置。

**r-chart 与源二环。** 合法 r-chart 的完整次序为

\[
r,p_5,p_4,p_3,p_2,p_1,g,c_5,c_4,c_3,c_2,c_1.
\]

它与原模板同型，C 对应倒序 P，P 对应倒序 C。删 r 得 Yr，其唯一红六为 g+C5。所以 r∈S(Yg)、g∈S(Yr)，根之间“在对方删根 chart 中为红六源”的关系具有二环。

Yg、Yr 各自删去唯一红六源、终后，D 无 R5，所以 w=0。

**p5-chart 的完整校准。** 另一个合法 chart 次序为

\[
p_5,g,c_5,c_4,c_3,c_2,c_1,p_4,p_3,p_2,p_1,r.
\]

记 A 为倒序 C5，B 为倒序 P4。删 root p5 后次序 g<A<B<r，完整颜色为：

| 三元组组成 | 颜色 |
| --- | --- |
| AAA | R |
| BBB | B |
| gAA、gBB | R |
| gAr | B |
| gBr | R |
| AAB | B |
| ABB | R |
| AAr | B |
| ABr | R |
| BBr | B |
| gAB | B |

该表覆盖全部三元组，块内颜色已包含于 AAA、BBB。唯一红六为 g+A；除此红块外，红路径长至多 4。删去其唯一源终后，D 无 R5，故该 chart 同样 w=0。其 chart 合法与 weak 禁形由已证合法最右 reroot 运输；c1-chart 则由前述 g/r 同构对称同样成立。

**恰好四个合法 roots，完整循环全 w0。** 合法 roots 恰为 {g,c1,r,p5}。四者由上述 charts 及已证最右操作给出。其余 ci、i≥2 被实际包 (g,c1,ci,r)=BBBR 排除，因为它的唯一少数点是 ci；其余 pi、i≤4 被 (g,r,pi,p5)=BBBR 的少数点 pi 排除。合法 root 不能在自身 blue-root chart 的第一位仍为这个少数点。

因此这是完整四 root 循环、全部 w=0 的实际 777 例。它没有 critical/full 接口，某些 chart 的极端 roots 位于 D。它只反驳“root 源关系天然无环或自带严格排序”的通用断言，不反驳临界完整 rootcycle 必有 positive through 的目标。

### 7.2 十二点 767：严格交错红六不能通用外端 uncross

**实际次序与完整颜色。** 取

\[
a<X_4<c<b_0<Y_4<d,\qquad J=\{c,b_0\}.
\]

下列点集的全部三元组为红：对每个 j∈J，{a}∪X4∪{j} 与 {j}∪Y4∪{d}，以及 {a}∪J∪{d}。另外对所有 x∈X4、y∈Y4，将 (a,x,y)、(a,x,d)、(a,y,d) 染红。其余三元组全部蓝。这是完整颜色定义，不只指定两条显示红六。

**无 a、d 的全部 packet。**

| 四点组成 | packet |
| --- | --- |
| XXXX、XXXJ、JYYY、YYYY | RRRR |
| XXXY、XXJY | RBBB |
| XXJJ | RRBB |
| XXYY、XJJY | BBBB |
| XJYY、XYYY | BBBR |
| JJYY | BBRR |

**恰含一个外点的全部 packet。** 下表以中间三点组成 T 为行，分别列 aT、Td：

| T | aT | Td |
| --- | --- | --- |
| XXX | RRRR | RBBB |
| XXJ | RRRR | RBBB |
| XXY | RRRB | BBBB |
| XJJ | RRRB | BBBR |
| XJY | RRBB | BBBR |
| XYY | RRBB | BBBR |
| JJY | RBBB | BRRR |
| JYY | BBBR | RRRR |
| YYY | BBBR | RRRR |

**同时含 a、d 的全部 packet。**

| 中间 pair | packet |
| --- | --- |
| XX、XJ、XY | RRRB |
| JJ | RRRR |
| JY、YY | BRRR |

所有显示 packet 都至多换色一次，所以完整 signotope 合法。

**全部路径帽与同端 weak。** 长度至少 5 的红路径只能落在某个红六块 a+X4+j 或 j+Y4+d 内，故红长至多 6。

蓝长至多 4：中间三块 X、J、Y 各至多取两点；使用 J 时，XXJ、JYY 为红，迫至多 1X+2J+1Y；不使用 J 时至多 2X+2Y。含 a 的蓝路径长至多 3，含 d 的蓝路径长至多 4。

红六端点只可能为 (a,j) 或 (j,d)。任何中间点与这对端点都成红 triple，所以相同实际端点的蓝长至多 2。由 a 启动或到 d 结束的红五同样给同端蓝长至多 2；另两类红五 X4+j、j+Y4 的同端蓝长至多 3，因为相同端点的蓝四必含 XXX、XXJ、JYY 或 YYY 中的一种红三元组。其余红长至多 4，与蓝长至多 4 之和也至多 8。

因此无 weak7、无 B6、无 R7，是完整实际 767 配置。

**严格交错与外端失败。** 该配置包含实际红六 R6(a,X4,b₀)、R6(c,Y4,d)，且实际端点严格交错 a<c<b₀<d。然而 a→d 的红路径最长仅 4，实际红四为 (a,c,b₀,d)，不存在所期待的外端红六。

这只否定没有饱和假设的通用外端 uncrossing；需要满容量接口的版本仍须另证。此例不带满核，不能将它登记为饱和目标的反例或全局 N 收益。

## 8. 未解边界与数值分账

| 当前工作结果 | 范围 | 不推出 |
| --- | --- | --- |
| 任意次序大红块 product 全排 | p≥3、每块≥p、完整蓝 product 及两类同端禁形；不需拟阵或分离 | 任意短块或一般拟阵分支全部不可能 |
| 支持界 p(p+1)−3 / p²−1 | 具完整 product 的纯 rank 1 / 含 rank 2 minimum-transversal support | UNSAT 核大小或新 N 上界 |
| 无分离内部 private 选择族禁形 | 完整 F、τ=p、基交换；至少有一个位置的全部 private 出 G | F 本身 UNSAT 不可能、删除 G 外约束后仍 UNSAT |
| 两个完整端点 perfect 及共同点严格跨越 | 所有双满临界 q、四根/τ4及真实 promotion 亏一接口 | 未 promotion 亏一可套双满身份，或全部四根/τ4/亏一 w0 关闭 |
| 全 ambient 合法根结构 | 蓝 separator、红六闭 gap 定位、连续三根的少数点共享 gap | 所有 gap 换 root 后均不变，或必有 positive through |
| 五根满接口的 m6 子类排除 | 存在 critical 双满五根 τ5 chart 时 m≤5 | 全部 777 均 m≤5，四根/τ4/未 promotion 亏一关闭 |
| 完整四 root 全 w0 校准 | 12点777中 root 源关系有二环 | 临界 full 目标反例，或源关系天然无环 |
| 严格交错红六校准 | 12点767中两条红六严格交错、外端红长仅4 | 通用 uncrossing，或满容量版本已被否定 |

主线端口交会、critical 完整 rootcycle 必有 positive through，以及全部四根、τ4、亏一 w0 分支关闭均未证明。§6.7 的 m=5 剩余结构没有得到统一正缺额；所有五个 charts 都处 m=5 五根情形仍开放。本轮任意次序大红块 product 全排完整关闭旧 2—1—2 大块 product 类，但不等于闭合临界母体。

无条件工作证明链仍为

\[
N757\le a+b-1,\qquad C766\le2b,\qquad
N767\le3b+4,\qquad N777\le3b+5. \tag{19}
\]

固定代 a=16、b=25，仍为

\[
a+b-1=40,\qquad2b=50,\qquad3b+4=79,\qquad3b+5=80. \tag{20}
\]

支持界 27 不计入 N；本轮无条件全局数值下降为 0。

## 9. 文档与保证边界

本轮只新增本文及 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_arbitrary_product_root_barriers_20261030/DOCUMENT_CHECK.json>)。回执按最终保存内容记录 SHA256、UTF-8 字节数、公式界定符配平、编号唯一连续、本地链接存在性、固定算术 40/50/79/80 及支持界 27/24。结果为 PASS_DOCUMENT_ONLY，只认证文档层检查通过，不认证数学。

全部新增 unreviewed/unaccepted；生成交叉核对非独审。外部调用与科学执行均为 0。旧稿、任务 metadata、接受、assurance、runtime、proof、sealed 证据及运行不改；没有打开页面，也没有宣布长期研究完成。
