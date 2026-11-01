# 条件排列、共享坏对和有限弱对偶

## 一条证书的语义

先从实际贪心过程证明失败覆盖，再在固定实际锁集和位置的非空排列空间中计数。临界边对必须是同一H里的有序异边对。锁迹只负责概率权重与容量；真实是否额外相交由坏对向量z记录，不能让每个位置或每个布局重选不同z。

对位置h，终点事件给A_h、起点事件给B_h、临界对并界扣真实坏对给C_h−D_h。它们是同一位置事件的三个上界，故总失败界为 $\sum_h\min\{A_h,B_h,C_h-D_h\}$。双向权重与无序坏对容量必须相配：异迹容量μTμU，同迹容量 $\binom{\mu_T}2$；若改为有序，就用μT(μT−1)并同步改两个方向，不能再扣第二遍。

建议计算器返回精确分数、每位置活跃项、名义扣除和有效下降。L12给有效下降的精确恒等式；不先确认活跃项，就增加配额常常只增成本而不改善界。

## 基础失败覆盖和联合计数
## L3．贪心失败由临界单交边对覆盖；左右条件要联合计数

**失败覆盖。** 对任意有限 r 元超图（r≥2）及顶点顺序，起初全红，按顺序扫描：当当前点是某条仍全红边的最后一点时，将它翻蓝。最终若失败，则存在不同边 A,B 及 x，使

\[
A\cap B=\{x\},\qquad x=\max A=\min B.
\]

证明分两步。最终若有全红边，它的最后一点扫描时该边也全红，算法必把该点翻蓝，矛盾。因此失败只能来自全蓝边。取一条全蓝边 \(B\) 的最早点 \(x\)，再取 \(x\) 当时翻蓝的全红见证边 \(A\)；\(A\) 的其余点在 \(x\) 前，\(B\) 的其余点在 \(x\) 后，得到所示单交关系。因 \(r\ge2\)，两边不能相等。该条件是失败的必要覆盖事件，不是失败的充要条件。

[Greedy.lean](../../../../knowledge/archive/formal/Aris4Math/Greedy.lean) 的 `uniform_failure_covered`、`failureAt_covered`、`failure_event_cover` 已量化任意 r≥2；最终 `Simple5Hypergraph` 包装仍是五元。

**联合计数。** 固定锁点到指定位置后，余下 \(N\) 个自由点与 \(N\) 个自由槽均匀双射。设自由点集 \(A,B\) 互不相交，\(|A|=a\)、\(|B|=b\)；自由槽集 \(L,R\) 互不相交，\(|L|=\ell\)、\(|R|=h\)。则

\[
\Pr(\sigma A\subseteq L,\ \sigma B\subseteq R)
=\frac{\binom\ell a\binom h b}
 {\binom N a\binom{N-a}b}.
\]

证明：像集是均匀的有序不交集合对，共有 \(\binom Na\binom{N-a}b\) 个；合格对有 \(\binom\ell a\binom h b\) 个。每对像集都对应 \(a!b!(N-a-b)!\) 个双射，故计数比就是所示概率。\(a+b\le N\) 来自真实不交自由点集，锁定双射空间还须非空。左右事件不是独立事件。

[JointCounting.lean](../../../../knowledge/archive/formal/Aris4Math/JointCounting.lean) 的 `locked_joint_subset_ratio`、`card_locked_joint_subset` 支持一般有限类型和锁点类型；[Counting.lean](../../../../knowledge/archive/formal/Aris4Math/Counting.lean) 处理实际排列计数。[ConditionalUnion.lean](../../../../knowledge/archive/formal/Aris4Math/ConditionalUnion.lean) 的 `propertyB_of_position_bounds` 将严格总界接回原染色。



## L6．避锁子族必有多少相交边对

**集合族定理。** 设 \(F\) 是 \(N\) 点上不同的 \(t\) 元集合构成的有限族，\(t\ge2\)。\(q\) 为不同成员之间有非空交集的无序对数，则

\[
q\ge\max\left\{0,\left\lceil\frac{t|F|-N}{t-1}\right\rceil\right\}.
\]

证明：令 \(a_x=|\{A\in F:x\in A\}|\) 为点 \(x\) 在该集合族中的度，则

\[
t|F|=\sum_x a_x
\le N+\sum_x\binom{a_x}{2}
=N+\sum_{\{A,B\}\subseteq F}|A\cap B|
\le N+(t-1)q.
\]

首个不等式用每个非负整数 \(a\) 都满足 \(a\le1+\binom a2\)；中间等式从点和无序集合对两个方向数公共点；最后一步用不同 \(t\) 元集合的交至多 \(t-1\)。再用 \(q\) 为非负整数取整。允许重复成员时最后一步可能失效。

**避锁 link 推论。** 在简单 \(r\) 元超图中固定中心 \(x\)，\(r\ge3\)，取 \(R\subseteq V\setminus\{x\}\)，令 \(f\) 为含 \(x\) 且避开 \(R\) 的边数。删去 \(x\) 后得到 \(N=v-1-|R|\) 点上的不同 \((r-1)\) 元集合，所以这些边中在 \(x\) 外仍相交的无序对数 \(b_R\) 满足

\[
b_R\ge\max\left\{0,\left\lceil
\frac{(r-1)f-(v-1-|R|)}{r-2}\right\rceil\right\}.
\]

这里无需点对覆盖。\(r=2\) 不能代入分母 \(r-2\)。

若新结构还提供整个 link 度数序列 \((a_x)_x\)，可以保留证明中的中间量，得到

\[
q\ge\left\lceil\frac{\sum_x\binom{a_x}{2}}{t-1}\right\rceil.
\]

它至少不弱于只用 \(t|F|-N\) 的界，有时更强；是否值得取得这些额外数据，应看它能否改善活跃槽。当前通用配额只需要 \(|F|\) 和 \(N\)，并未实现这份更细输入的完整调用。

五元实现：[AvoidedLink.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyThree/AvoidedLink.lean) 的 `avoided_bad_pair_budget`、`avoided_bad_pair_lower`，以及 [RefinedDeletion.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyThree/RefinedDeletion.lean) 的 `avoided_dual_lower`。下一次应挑选能约束低权槽的 R，而不是默认所有避锁配额都值得加入。



## L7．配额可相加，但重叠必须由容量修复

**有限弱对偶定理。** 索引集合 \(S,Q\) 有限。对每个槽 \(s\in S\)，\(z_s\) 是真实数量、\(c_s\) 是容量、\(w_s\) 是目标权重；对每个配额索引 \(q\in Q\)，\(q_q\) 是配额下界，\(a_{qs}\) 是该配额对槽的系数。所有量取实数，并满足

\[
0\le z_s\le c_s\quad(s\in S),\qquad
\sum_{s\in S}a_{qs}z_s\ge q_q\quad(q\in Q).
\]

任取非负乘子 \(\delta_q\ge0\)，有

\[
\sum_s w_sz_s\ge
\sum_q\delta_q q_q-
\sum_s c_s\max\left\{0,\sum_q\delta_q a_{qs}-w_s\right\}.
\]

**证明。** 把每个配额不等式乘以对应的 \(\delta_q\ge0\)，相加并交换有限求和次序，得到

\[
\sum_{q\in Q}\delta_q q_q
\le\sum_{q\in Q}\sum_{s\in S}\delta_q a_{qs}z_s
=\sum_{s\in S}\left(\sum_{q\in Q}\delta_q a_{qs}\right)z_s.
\]

对每个槽，把超过目标权重 \(w_s\) 的那部分系数用容量 \(c_s\) 控制：

\[
\left(\sum_q\delta_q a_{qs}-w_s\right)z_s
\le\max\left\{0,\sum_q\delta_q a_{qs}-w_s\right\}c_s.
\]

若括号内系数为负，由 \(z_s\ge0\)，左边不大于0，而右边恰为0；若系数非负，则由 \(z_s\le c_s\) 得到该式。对槽求和，再从前一式中减去这些容量项，恰得到定理。这是该有限代数命题的完整证明。

[MixedLayoutDual.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/MixedLayoutDual.lean) 的 `quota_repair` 已在任意有限索引、\(\mathbb{Q}\) 上证明；系数 \(a_{qs}\) 和权重 \(w_s\) 不要求非负。纸面证明适用于 \(\mathbb{R}\)，当前 Lean 声明采用 \(\mathbb{Q}\)。这里不需要 LP 强对偶、最优解或浮点容差：求解器只负责提出 \(\delta\)，精确不等式负责验收。

对无序坏边对槽，异类型容量是 \(\mu_T\mu_U\)，同类型容量是 \(\binom{\mu_T}{2}\)；对有序槽，同类型为 \(\mu_T(\mu_T-1)\)，相应双向权重及除2必须一致。不能混用两种约定后重复扣除。

**应用时还须证明什么？** 本引理的前提把真实数量、容量和配额都交给调用者。要用于 Property B，须从实际超图构造 \(z_s\)，证明这些配额与容量确实成立，核对 \(w_s\) 正是概率事件的权重，再证明扣除后的总界严格小于1。本引理只完成其中的加权下界步骤。

**2026-10-19算术实现补充。** 合作者在k10/11中以整数向外舍入验证非负计数上界和容量扣除；方向证明、溢出边界及实际重放见[小k迁移笔记](../../../../knowledge/archive/research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)。本组允许带符号系数，不能直接将全部系数上取整，需另证整体上界方向。



## L8．共享同一真实坏对向量的多布局定理

设某个实际超图 \(H\) 已给出固定锁点及真实坏对向量 \(z\)。有限多个布局 \(\ell\) 都使用这些数据；它们可以对应不同的锁定排列样本空间。假设已证明每个布局的贪心失败概率由下式控制：

\[
U_\ell(z)=F_\ell+
\sum_j\min\{a_{\ell j},\ c_{\ell j}-D_{\ell j}(z)\},
\]

其中 \(D_{\ell j}(z)\) 是对同一批实际坏对的线性加权扣除。取 \(\gamma_\ell\ge0\)、\(\sum_\ell\gamma_\ell=1\)，再取 \(0\le\beta_{\ell j}\le\gamma_\ell\)。因为 \(\min(a,c-D)\) 同时不超过 \(a\) 和 \(c-D\)，分别乘以非负数 \(\gamma_\ell-\beta_{\ell j}\) 和 \(\beta_{\ell j}\) 再相加，逐项得到

\[
\gamma_\ell\min(a,c-D)
\le(\gamma_\ell-\beta_{\ell j})a+\beta_{\ell j}c-\beta_{\ell j}D.
\]

如果通过 L7 或直接计数证明，对每个 \(j\) 都有 \(\sum_\ell\beta_{\ell j}D_{\ell j}(z)\ge L_j\)，将上式对 \(\ell,j\) 求和，就得到

\[
\sum_\ell\gamma_\ell U_\ell(z)
\le\sum_\ell\gamma_\ell F_\ell+
\sum_{\ell,j}[(\gamma_\ell-\beta_{\ell j})a_{\ell j}
+\beta_{\ell j}c_{\ell j}]-\sum_jL_j=:B.
\]

若 \(B<1\)，至少一个布局满足 \(U_\ell(z)<1\)：否则所有 \(U_\ell(z)\ge1\)，由非负权重和总质量1，其凸平均也至少为1，矛盾。由开头假设，这个布局的实际失败概率小于1，故其有限非空排列空间中至少有一个成功输出，从而 \(H\) 有合法染色。

这是依赖“各布局上界确实控制实际失败事件”的条件论证。该概率前提由 L3 的实际算法、条件计数和相应扣除接口提供，不能由上面的代数自行推出。

**价值。** 分别优化每个布局时，对手可以在不同布局中把同一批坏对放到互相矛盾的最坏槽；共享 z 消除了这份额外自由。因此有时不用增加锁点，就能得到过去单布局没有给出的严格结论。

这个论证平均的是各布局的有效数值界，不要求不同布局的概率空间相同，也不假设独立。量词是“对每个 H，取它的实际数据，再选择布局，再抽余下排列”；不能看过随机排列后再随意选择条件空间。各布局若使用不同锁集，必须先证明都来自同一更大实际数据的投影，不能直接套共享 z。

Lean 核心为 [MixedLayoutDual.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/MixedLayoutDual.lean) 的 `min_split`、`average_le`、`exists_strict_of_average`；[MixedLayoutCounts.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/MixedLayoutCounts.lean) 将扣除接到真实坏对；[MixedLayoutApplication.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/MixedLayoutApplication.lean) 的 `propertyB_of_mixed_layouts` 返回实际 Property B。宿主五元，锁数、点数、边数可变；当前 profile 接口还显式要求 `emptyPairCap=none` 等真实实现条件。不存在成功的当前证书，不等于没有好布局。



## L12．只有跨过活跃界的扣除才改善总概率

令 \(A,B,C\) 为实数，\(d\ge0\)，\(L=\min(A,B)\)，则

\[
\min(L,C)-\min(L,C-d)
=\max\{0,d-\max(0,C-L)\}.
\]

若 \(C\le L\)，则 \(C-d\le C\le L\)，左边为 \(C-(C-d)=d\)，右边也为 \(d\)。若 \(C>L\)，令 \(h=C-L>0\)：当 \(d\le h\) 时，两个最小值都是 \(L\)，左右均为0；当 \(d>h\) 时，左边为 \(L-(C-d)=d-h\)，右边也为 \(d-h\)。这穷尽所有情形，本次未新增 Lean 声明。

这把一个常见误判变成可直接记录的量：改进名义坏对扣除 \(d\)，却仍有 \(C-d\ge\min(A,B)\) 时，总上界下降恰为0。下一次诊断应输出每个位置的活跃项及这份有效下降，再决定增加配额、改变布局还是加强结构。


## 可执行算术方案及方向证明

浮点LP只寻找有理乘子；保存的精确不等式才承担证明。下面向外舍入只适用于已证明非负的正项乘数；带符号dual不能整体上取整。整数实现还须检查中间正项M²，而非只看减对角后的最后值。

## 二、整数向外舍入：把有理算术放在正确方向

固定每个位置h，令A_h、B_h为边终止／起始概率和，C_h为全部互异有向类型对的记账上界。
单交临界对覆盖失败；已知实际坏对不能临界，对其最少可扣权D_h有

`P(Fail)≤Σ_h min(A_h,B_h,C_h−D_h)`。

取统一尺度S（作者实现为`2^52`）。对非负概率p，整数 `ceil(Sp)` 给上界，`floor(Sp)` 给下界。
用上取整系数形成 `Â_h,B̂_h,Ĉ_h`；其乘数必须是非负整数重数，特别同型有向对数为 `ℓ_T(ℓ_T−1)`。
对k≥3，真实link给坏对下界 `q=ceil(((k−1)d−(v−1))/(k−2))`；每无序类型格容量为 `C(ℓ_T,2)` 或 `ℓ_Tℓ_U`。
每格扣除权取两个方向的下取整之和，按容量从最轻格装满q，得整数 `D̂_h`。
任一真实q坏对集合可放入这些容量格；对其逐项下取整，再对所有合法装填取min，所以 `D̂_h≤S D_h`。
故 `Ĉ_h−D̂_h≥S(C_h−D_h)`；A、B同向上界，min的单调性保证

`Ucert=Σ_h min(Â_h,B̂_h,Ĉ_h−D̂_h)≥S Σ_h min(A_h,B_h,C_h−D_h)`。

因此纯整数比较 **`Ucert<S`** 即足够；没有把浮点近似当证明。
必须保留零权格及其容量：q>0未必有正扣除，扣了C也未必改变该位置活跃的min项。
作者缓存每(v,锁数)权表并向量化类型重数；NumPy int64仅在实际中间积和界小于`2^63−1`后使用，最终和用Python整数。
安全界应覆盖减对角前的`M²`正项和；不只检查最终`M(M−1)`，更不能只看最终结果未溢出。
这项实现策略可先迁移到已有k5算术，不解决锁点存在或分类覆盖。
带负系数的多布局dual不能直接套“所有系数上取整”：须按符号定方向并保留同一实际坏对与配额，另证整体支配。
上述数学机制分别已有 [L3失败计数、L6 link坏对、L7容量弱对偶](../../../../knowledge/archive/research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md)；新增价值主要在算术实现组织。
