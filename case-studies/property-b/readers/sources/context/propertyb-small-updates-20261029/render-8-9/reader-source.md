<div class="result-strip"><div><span>八元 · 相对基线 263</span><strong>m(8) ≥ 267 · 增加 4</strong><small>任意 266 条八元边均可二染色</small></div><div><span>九元 · 相对基线 538</span><strong>m(9) ≥ 543 · 增加 5</strong><small>任意 542 条九元边均可二染色</small></div></div>

<p class="proof-status">完整计算机辅助证明 · 独立全域重建与全概率复算 · 尚未 Lean</p>

本卷给出两项针对任意有限简单超图的完整证明：$m(8)\ge267$ 与 $m(9)\ge543$。点对覆盖、点数和度数条件均由同一实际最小反例内部推出；原始输入只要求有限、简单且每条边具有指定大小。

## 两项原始命题与验证范围

**八元定理。** 任意有限简单八元超图，若边数至多266，则存在使每条原边同时含红、蓝两色的染色。因此 $m(8)\ge267$。

**九元定理。** 任意有限简单九元超图，若边数至多542，则存在使每条原边同时含红、蓝两色的染色。因此 $m(9)\ge543$。

|结果|本卷固定参考基线|下界增益|全部独立概率复算|内部完整点数域|
|---|---:|---:|---:|---|
|$m(8)\ge267$|263|4|2094型，另299项组件配额|47–120|
|$m(9)\ge543$|538|5|3450型|57–195|

以下先收入通用条件排列的完整概率公式，再完整收入两份证明。两项均已完成独立全域重建和全概率复算，Grok与Gemini的整篇静态审阅均未发现实质缺口；准确范围见文末审阅记录，尚无 Lean 形式证明。


<a id="generic-probability"></a>

## 通用条件排列概率：完整公式

### 通用 · 2. Generic conditioned greedy bound

Take a uniformly random permutation conditioned on fixed distinct vertices $s_i$ occupying fixed distinct positions $t_i$, and greedily recolor each vertex blue if it is the final vertex of a presently all-red edge; otherwise leave it red. The final coloring has no red monochromatic edge. If there is a blue monochromatic edge $B$, its first vertex $x$ is the last vertex of another edge $A$, and $A\cap B=\{x\}$. Thus failure is covered by ordered **critical pairs**.

Write $T\subseteq [s]$ for the exact set of locked vertices in an edge, $\ell_T$ for the count of its type and $r_T=k-|T|$, $N=v-s$. At a position $h$, write $a_h,b_h$ for the numbers of free positions before and after $h$. The allowed preceding/succeeding lock masks are $I_h^-,I_h^+$. For a genuinely single-intersection ordered pair of types $T,U$, its critical probability is

$$w_h(T,U)=
\begin{cases}
\displaystyle\frac{\binom{a_h}{r_T-1}\binom{b_h}{r_U-1}}{N\binom{N-1}{r_T-1}\binom{N-r_T}{r_U-1}},&h\text{ free, }T\subseteq I_h^-,\ U\subseteq I_h^+,\ r_T+r_U-1\le N,\\[3mm]
\displaystyle\frac{\binom{a_h}{r_T}\binom{b_h}{r_U}}{\binom N{r_T}\binom{N-r_T}{r_U}},&h=t_j,\ T\cap U=\{j\},\ T\setminus\{j\}\subseteq I_h^-,\ U\setminus\{j\}\subseteq I_h^+,\ r_T+r_U\le N,\\[3mm]
0,&\text{otherwise.}
\end{cases}$$

A locked center cannot have its incident locked vertices in the wrong order. For a free center, both incident edge types must respect the earlier/later locked vertices. Binomial coefficients are zero when their lower argument exceeds the upper argument.

Let $A_h$ and $B_h$ be the sums of exact one-edge endpoint probabilities of ending/starting at $h$, respectively, and let

$$C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf 1_{T=U})w_h(T,U).$$

The latter bounds true critical-pair probability because it replaces the number of genuinely single-intersection pairs by the number of all distinct ordered pairs in each type cell.

For a locked center $s_j$, link counting yields at least

$$q_j=\left\lceil\frac{(k-1)d(s_j)-(v-1)}{k-2}\right\rceil$$

distinct unordered incident-edge pairs that share another vertex. None can be critical. For each unordered type cell $\{T,U\}$ of edges incident to $s_j$, there are at most $\binom{\ell_T}{2}$ available unordered pairs when $T=U$, or $\ell_T\ell_U$ when $T\ne U$; each has nonnegative removable accounting weight $w_{t_j}(T,U)+w_{t_j}(U,T)$. Sum the $q_j$ cheapest available such weights, counting cells with multiplicity: call this $D_{t_j}$. Then every possible placement of at least $q_j$ actual bad pairs has total removable weight at least $D_{t_j}$. At free positions set $D_h=0$.

Therefore the conditional failure probability is at most

$$\boxed{U(v,t,\ell)=\sum_{h=1}^v\min\{A_h,B_h,C_h-D_h\}}.$$

If this is below 1, the hypergraph is 2-colorable.

For no locks, the global pair surplus yields at least

$$Q_v=\max\left\{0,\left\lceil\frac{M\binom k2-\binom v2}{\binom{k-1}2}\right\rceil\right\}$$

unordered multi-intersection pairs. So in the no-lock stage, replace the total number of ordered critical-pair candidates $M(M-1)$ by $M(M-1)-2Q_v$.


<a id="eight-proof"></a>

## 八元：完整证明

### 八元 · 八元超图的 Property B 下界：$m(8)\ge267$

**主定理（完整计算机辅助证明）。** 对任意有限顶点集 $V$ 及由互不相同八元子集组成的边集 $E$，若 $|E|\le266$，则存在映射 $\chi:V\to\{\text{红},\text{蓝}\}$，使每条边同时含两种颜色。因此 $m(8)\ge267$。

本稿覆盖原始完整对象域。所有选点条件均在同一实际最小反例内推出，有限计算只核验完整必要局部类型的精确有理不等式。最终2094型全部严格，最大 $433608879718/433637886825<1$。全部2094型及299项组件配额现已由独立实现完整复算；Grok与Gemini均已完成整篇静态审阅，未发现实质缺口。验收状态为sound-modulo-imports，明确保留有限精确计算及通常软件信任；本参数尚无Lean。详见[独核报告](context/propertyb-m8-267-20261029/independent/REVIEW.md)与[联合审阅](context/propertyb-small-updates-20261029/reviews-8-9/DISPOSITION.md)。

### 八元 · 1. 定义与无损归约

**定义1.1。** 有限简单八元超图 $H=(V,E)$ 具有 Property B，指存在上述合法二染色；$m(8)$ 是不具有 Property B 的此类超图的最少边数。记 $v=|V|$、$d(x)=|\{A\in E:x\in A\}|$、$\lambda_{xy}=|\{A\in E:x,y\in A\}|$。

**引理1.2。** 若主定理为假，则存在同一实际反例，满足
$$47\le v\le120,\qquad |E|=266,\qquad
\sum_xd(x)=8\cdot266=2128,$$
$$\lambda_{xy}\ge1\ (x\ne y),\qquad
 d(x)\ge\left\lceil\frac{v-1}{7}\right\rceil. \tag{1}$$

**证明。** 在原始反例中选顶点数最少者。若某不同点对从不共边，将这两点识别，任一原边的像仍有八个不同点；重复像边仅保留一次。所得边数不增加，合法像染色可拉回为原染色，所以仍是反例，违背最小性。因此每个点对被覆盖。

对每点求共度和，得 $7d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1$，于是
$$v\left\lceil\frac{v-1}{7}\right\rceil\le2128.$$
该整数函数非减，而 $121\lceil120/7\rceil=121\cdot18=2178>2128$，故 $v\le120$。

若 $v\le14$，将顶点分成两个大小均至多七的颜色类即可。若 $15\le v\le46$，均匀选择 $\lfloor v/2\rfloor$ 点染红。固定八元边单色的概率为
$$p(v)=\frac{\binom{\lfloor v/2\rfloor}{8}+\binom{\lceil v/2\rceil}{8}}{\binom v8}.$$
全部32个整数的确切检验给
$$\max_{15\le v\le46}266p(v)=\frac{343672}{343785}<1,$$
最大在45、46点达到。因此并集界排除这些点数。47点的同一充分界为 $85918/82861>1$，故本证明保留47点起的完整必要域，而没有沿用未经重新核对的旧起点。

此时 $\binom v8\ge\binom{47}{8}\ge266$。若边数不足266，补入不同八元边直到恰266条；补边保留点对覆盖和不可二染。以后度数、共度、迹重数均指这个完成后的同一实际超图，得到(1)。$\square$

### 八元 · 2. 原染色算法与条件排列充分界

本节复述既有八／九元通用机制，来源为 [propertyB_small_k/propertyB_k8_k9_proof.md](#generic-probability) 第2节及 `propertyB_m8_certificate_v2.py` 的 `Calculator`。机制不固定总边数265；本次全部重数之和为266。

固定不同实际锁点 $(x_0,\ldots,x_{s-1})$ 及不同位置 $p_j\in\{1,\ldots,v\}$，将其余 $N=v-s$ 个实际顶点均匀排列。令 $\ell_T$ 为恰含锁指标集 $T$ 的实际边数，$r_T=8-|T|$，故 $\ell_T\ge0$、$\sum_T\ell_T=266$。

**引理2.1（实际失败见证）。** 初始全红，按排列依次处理顶点：若当前点是一条当前全红边的最后点，将其改蓝。最终没有全红边。若有全蓝边 $B$，取其最早点 $z$；$z$ 改蓝时有仍全红且在此结束的边 $A$。$A\setminus\{z\}$ 全在前，$B\setminus\{z\}$ 全在后，故 $A\cap B=\{z\}$，且两边不同。$\square$

记 $e_h(T),f_h(T)$ 为某实际 $T$ 型边在位置 $h$ 结束／开始的条件概率，$w_h(T,U)$ 为固定实际有序单交边对在 $h$ 形成该见证的条件概率。它们由给定锁点布局下对自由顶点的均匀抽样得到，完整容量／锁点顺序条件及二项式公式见所引第2节和 `Calculator.endpoint/weight`；这些公式只将每条边的大小设为本次的八。

定义
$$A_h=\sum_T\ell_Te_h(T),\quad B_h=\sum_T\ell_Tf_h(T),\quad
C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf1_{T=U})w_h(T,U).$$
$C_h$ 对全部不同有序原边对记非负权，非单交对不是实际失败见证，可以扣除其合法下界权。若 $D_h$ 不超过该位置实际非单交对总记账权，则三次并集界及引理2.1给
$$\Pr(\text{失败})\le U=\sum_{h=1}^v\min(A_h,B_h,C_h-D_h). \tag{2}$$
自由位置取 $D_h=0$。合法非空有限条件排列空间中，$U<1$ 给至少一次成功排列，其输出就是当前全部266边的实际二染色。

### 八元 · 3. 七元链接的坏对配额

**引理3.1（基础链接配额）。** 固定锁点 $j$，只取含它并避开锁指标集 $R$ 的实际边，边数为 $f$。删去该锁，得到至多 $N=v-1-|R|$ 点上的 $f$ 个不同七元集合。若有 $q$ 个相交无序集合对，则
$$7f\le N+6q,\qquad
q\ge\max\left(0,\left\lceil\frac{7f-N}{6}\right\rceil\right). \tag{3}$$

**证明。** 不同七集的交至多六点。对各支撑点的出现重数 $a$ 用 $a\le1+\binom a2$，再对不同集合对求交点数即得。原超图简单性保证链接不同。$\square$

**引理3.2（component 支撑加强）。** 对 $f$ 个不同七集，建立相交图。一个含 $t$ 个集合、$e$ 条图边的连通分量满足 $t-1\le e\le\binom t2$。令
$$a(t,e)=\max\left(\left\lceil\frac{t^2}{t+2e}\right\rceil,
\left\lceil\frac{2t-e-1}{2}\right\rceil\right).$$
其支撑至少 $7a(t,e)$；若 $t\ge2$ 还至少八；若 $e<\binom t2-\lfloor t/2\rfloor$ 还至少十五。

**证明。** 随机次序中早于全部邻点的图点形成独立集，期望为 $\sum1/(1+d_G)$。Cauchy–Schwarz 给独立数至少第一个上整项。固定生成树，为每条非树边删去一名端点，共至多 $e-t+1$ 名；余图是森林，大二分部给第二个上整项。独立图点对应不交七集，所以支撑至少其数的七倍。两不同七集的并至少八。

若支撑至多十四，每个七集至多有一个不同的不交伙伴：支撑不足十四时没有，恰十四时只有其补集。因此补图至多 $\lfloor t/2\rfloor$ 条边，给最后结论。$\square$

不同相交分量的支撑不交。取上述所有适用支撑界的最大值 $u(t,e)$，另取 $u(1,0)=7$，定义
$$S(0,q)=0,\quad
S(f,q)=\min_{1\le t\le f,\ t-1\le e\le\min(q,\binom t2)}
\{u(t,e)+S(f-t,q-e)\}.$$
对实际分量逐个归纳，支撑至少 $S(f,q)$。递推允许无实现图的参数或不用完预算，只会削弱下界。因此
$$q_*(f,N)=\min\{q\ge0:S(f,q)\le N\} \tag{4}$$
是合法相交对下界。本次底层 DP 先按精确图边数求支撑下界，再取预算前缀最小，正好实现允许至多 $q$ 的松弛。全部实际299个调用输入满足 $f\le28$、$82\le N\le119$，接受配额至多23；表构建到 $f=30,q=80$，因此没有以截断忽略较小可接受预算。

**引理3.3（同一坏对向量的最大避点扣除）。** 在含锁 $j$ 的无序迹型格 $\{T,U\}$ 中，实际坏对容量为 $\binom{\ell_T}{2}$ 或 $\ell_T\ell_U$，权重为 $w_{p_j}(T,U)+w_{p_j}(U,T)\ge0$。对每个 $R\subseteq S\setminus\{j\}$，在 $(T\cup U)\cap R=\varnothing$ 的格内按递增权填足配额 $q_*(f_{j,R},v-1-|R|)$，得到单项最小成本 $D_{j,R}$。则
$$D_j=\max_R D_{j,R}$$
不超过同一个实际坏对总权，可以用于(2)。

**证明。** 实际坏对计数向量满足每个单项配额和全部容量，故实际目标至少每个单项最小值，也至少其最大值。没有将不同避点成本相加；每个固定位置的实际坏对只记一次。$\square$

### 八元 · 4. 零锁：47–82点

**引理4.1。** 对 $47\le v\le82$，存在合法染色。

**证明。** 令 $Q$ 为交至少二的不同无序原边对数。简单八元性给 $|A\cap B|\le7$，从而
$$21Q\ge\sum_{\{A,B\}}\binom{|A\cap B|}{2}
=\sum_{\{x,y\}}\binom{\lambda_{xy}}2
\ge266\binom82-\binom v2=7448-\binom v2.$$
取 $q(v)=\max(0,\lceil(7448-\binom v2)/21\rceil)$，实际有序单交对至多 $266\cdot265-2q(v)$。零锁时每对的条件权相同，将此数用于 $C_h$ 的全位置界。完整36个确切值都严格，最大为82点的 $433608879718/433637886825<1$。由(2)得到实际染色。$\square$

### 八元 · 5. 最低度一锁：83–89点

对实际最小度 $d$，由(1)和总度
$$\left\lceil\frac{v-1}{7}\right\rceil\le d\le\left\lfloor\frac{2128}{v}\right\rfloor.$$
选实际最小度点，固定位置 $\lfloor v/2\rfloor$；其实际迹为 $\ell_1=d$、$\ell_0=266-d$。完整七个点数的全部89个必要度数型用 component 完整池配额（只有空避点集）全部严格，最大 $68318532492247/68457295662756<1$，故这些点数可染。

### 八元 · 6. 最低单位伙伴及自适应三锁：90–107点

**引理6.1（实际 successive-min 选点）。** 取实际最低度点 $x$，$d=d(x)$，记
$$n=2(v-1)-7d>0.$$
在 $x$ 的实际单位共度伙伴中选最低度点 $y$，$e=d(y)$。则
$$d\le e\le d+\left\lfloor\frac{2128-vd}{n}\right\rfloor. \tag{5}$$
若
$$t=n-1-(7e-(v-1))>0,$$
则可选实际共同单位伙伴 $z$，其最低度 $f$ 满足
$$e\le f\le e+\left\lfloor\frac{2128-vd-n(e-d)}t\right\rfloor. \tag{6}$$

**证明。** $x$ 的非单位伙伴至多 $7d-(v-1)$ 名，故其单位池至少 $n$ 名，全体度至少 $e$，得到 $2128\ge vd+n(e-d)$。该池除去 $y$ 后，至多 $7e-(v-1)$ 名与 $y$ 非单位，因此共同池至少 $t$，并且它是第一池的子集。选其中最低度点 $z$，余者仍按 $e$ 收费，得到 $2128\ge vd+n(e-d)+t(f-e)$。三点实际不同、两两共度一。$\square$

对全部 $v=90,\ldots,107$、全部允许的最低度 $d$，(5)中 $n$ 均正。完整双锁域包含867种 $(v,d,e)$。实际双锁迹为
$$\ell_3=1,\quad\ell_1=d-1,\quad\ell_2=e-1,\quad\ell_0=267-d-e.$$
795型用引理3.3直接严格。剩余72型分布于103–107点，计数依次7、9、21、21、14；每型的共同池 $t$ 都正，最小为31。因此对每一剩余实际型应用(6)。

单位三锁的完整迹恰为两种：若有三点同边，则 $\ell_7=1$、$\ell_i=d_i-1$、$\ell_0=268-\sum d_i$；否则三个点对由三条不同边承载，$\ell_3=\ell_5=\ell_6=1$、$\ell_i=d_i-2$、$\ell_0=269-\sum d_i$。两种都不能删除。

全部72个父型的完整第三度数区间及两种迹合计508型，全部严格；最大 $788865098801232514/796148628468304293<1$。这些型来自引理6.1的真实最低伙伴及共同池，而不是把某份可实现性未知的整数解作为实际超图。由(2)，90–107点全部可染。

### 八元 · 7. 统一低度单位三锁：108–119点

**引理7.1。** 对该范围，存在三名度数至多二十、两两共度一的实际点。

**证明。** 令 $L=\{x:d(x)\le20\}$、$r=|L|$、$Z=21v-2128>0$。在 $L$ 上以共度至少二连冲突边。每点冲突度至多 $7d(x)-(v-1)$；外点度至少21给
$$r+2e(G)\le Tr-7Z,\qquad T=149-v.$$
随机排序独立集加 Cauchy–Schwarz 给
$$\alpha(G)\ge\frac{r^2}{r+2e(G)}\ge\frac{r^2}{Tr-7Z}.$$
分母至少 $r>0$；并且
$$r^2-2(Tr-7Z)=(r-T)^2+14Z-T^2>0,$$
因为 $14(21v-2128)-(149-v)^2$ 在108–119递增且在108点为279。因此独立数大于二，整数性给三名点。点对覆盖使其两两共度恰一。$\square$

将这三个实际点按度数排序，在 $\lceil(v-1)/7\rceil\le d_1\le d_2\le d_3\le20$ 的完整域内保留第6节的两种实际迹，固定其位置为 $(\lfloor v/2\rfloor-1,\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)$。全部660型只用基础完整池配额(3)便严格，最大 $160893083202769161823/161038233221975713656<1$。故这些点数可染。

### 八元 · 8. 120点的全局单位十七度点

**引理8.1。** 120点时，可以选四名不同的实际十七度点，且它们两两共度一。

**证明。** (1)给每点度至少17。若十七度点有 $r$ 名，其余点至少十八度，则
$$2128\ge17r+18(120-r)=2160-r,$$
所以 $r\ge32$。对每名十七度点，$\sum_{y\ne x}\lambda_{xy}=7\cdot17=119=v-1$，而每项至少一，故它与全图所有其他点的共度都恰一。因此任选四名即可。$\square$

四个单位共度锁的全部至少二点迹恰为 $K_4$ 点对的团划分，共六种带标签型：六条二点迹；四种三点迹加其余三条二点迹；或一条四点迹。完整分类也由独立的十一候选团子集小枚举在本程序内重建；该小枚举属于作者分类实现；独核另用首次未覆盖点对递归重建六型，结果一致。

全部单点迹由度17减去已有多点迹确定，空迹由266减去非空数。固定位置 $(58,59,60,61)$，用 component 最大避点扣除后，六型全部严格，最大为
$$42737314248516385339/43417170721611099270<1.$$
故120点也可染。这个入口用实际大量十七度全局单位点，绕过了原最低三锁 separate 型的不严格充分界。

### 八元 · 9. 原命题装配

反设存在至多266边的原始反例。引理1.2将其归到同一实际简单、点对覆盖、恰266边、47–120点的反例。第4–8节覆盖此完整区间；每支的实际选锁保证输入属于完整必要局部域，每个域的全部型均有严格概率上界，故由(2)得到实际合法染色，矛盾。

该染色染好完成后的全部266条边，因而也染好补边前的原边。最初的识别操作只用于推出最小反例的点对覆盖，并未给原输入增加点数、度数、共度、平衡染色或证书假设。主定理成立，得到 $m(8)\ge267$。$\square$

### 八元 · 10. 证书、复现与准确状态

| 完整实际分支 | 必要型数 | 最大精确上界 |
|---|---:|---:|
|47–82零锁|36|433608879718/433637886825|
|83–89一锁|89|68318532492247/68457295662756|
|90–107直接双锁|795|47610603055191656213/47614325741405382960|
|72个未直接结束父型的完整三锁延展|508|788865098801232514/796148628468304293|
|108–119低度单位三锁|660|160893083202769161823/161038233221975713656|
|120四名十七度点|6|42737314248516385339/43417170721611099270|
|总计|2094|433608879718/433637886825|

[CERTIFICATE.json](context/propertyb-m8-267-20261029/CERTIFICATE.json) 保存全部实际迹、实际标签与布局、完整父域/第三度数范围、299个实际 component 配额和每行精确值。[SUMMARY.json](context/propertyb-m8-267-20261029/SUMMARY.json) 为摘要。[certificate.py](context/propertyb-m8-267-20261029/certificate.py) 不再搜索布局，而按保存的成功布局重建完整域并全部重算；单次约8.437 CPU秒。

复现：

```sh
python3 context/propertyb-m8-267-20261029/certificate.py
```

该程序依赖本目录 [component_trial.py](context/propertyb-m8-267-20261029/component_trial.py) 及既有 [propertyB_small_k/propertyB_m8_certificate_v2.py](propertyB_small_k/propertyB_m8_certificate_v2.py)，均是标准库 Python。初次布局与分流诊断保存在 [INITIAL.json](context/propertyb-m8-267-20261029/INITIAL.json)、[COMPONENT_TRIAL.json](context/propertyb-m8-267-20261029/COMPONENT_TRIAL.json)、[ADAPTIVE_TRIAL.json](context/propertyb-m8-267-20261029/ADAPTIVE_TRIAL.json)，它们的失败型仅是历史充分界失败，不是超图反例或最终缺口。最终证书覆盖域不依赖删除这些历史记录。

本轮记录的三次有界试算约5.187、2.761、2.861 CPU秒，最后完整固定布局重放8.437 CPU秒，合计约19.25 CPU秒；另有很小的导入／表初始化开销，未触及60 CPU秒预算。作者程序复用既有二项式核。独立检查另写下降阶乘注入核及递归组件DP，不导入作者概率或域生成模块：全部2094个分数与299项配额精确相等且严格，约9.401 CPU秒。Grok与Gemini均静态核查完整数学链和计算依据，均未执行程序；原始回应完整保留。最终数学结论是上述完整计算机辅助证明，本参数无Lean，也未宣称第二台机器复现。


<a id="nine-proof"></a>

## 九元：完整证明

### 九元 · 九元超图的Property B下界：m(9)≥543

### 九元 · 1. 命题与证明范围

**主命题。** 任意有限简单九元超图H=(V,E)，若|E|≤542，则存在红／蓝染色，使每条原边同时含两种颜色。因此m(9)≥543；相对本任务固定参考538，增益为五。

**证明状态。** 完整计算机辅助证明。原始输入归约、实际选点、完整必要迹域及3450个严格有理数证书均已完成；独立实现重新生成完整决策树并复算全部分数，逐项精确相等且严格。Grok与Gemini整篇静态审阅均未发现实质缺口。验收状态为sound-modulo-imports，明确保留有限精确计算及通常软件信任；本参数尚无Lean。详见[独核报告](context/propertyb-m9-543-20261029/independent/REVIEW.md)与[联合审阅](context/propertyb-small-updates-20261029/reviews-8-9/DISPOSITION.md)。

概率机制及二项式条件概率沿用合作者[`propertyB_k8_k9_proof.md`](#generic-probability)第2节，原始实现为[`propertyB_m9_certificate_v2.py`](propertyB_small_k/propertyB_m9_certificate_v2.py)。本次显式使用k=9、M=542、总度4878；链接为八元集合，不沿用六元研究中的五元链接常数。

完整成功记录在[[CANDIDATE.json](context/propertyb-m9-543-20261029/CANDIDATE.json)](context/propertyb-m9-543-20261029/CANDIDATE.json)，每行包括顶点数、实际度数、实际迹重数、锁位置、扣除方法及精确失败概率界。独立于阶段选择逻辑的实际域核查在[[coverage.py](context/propertyb-m9-543-20261029/coverage.py)](context/propertyb-m9-543-20261029/coverage.py)和[[SUMMARY.json](context/propertyb-m9-543-20261029/SUMMARY.json)](context/propertyb-m9-543-20261029/SUMMARY.json)。

**定义1.1。** d(x)为实际度数，$\lambda_{xy}$为不同点的实际共度，v=|V|。简单性指原边互不相同，每边恰九个不同顶点。Property B指每条边都不是单色。下文点对覆盖、度数及锁点都是同一实际反例内部的归约条件，不增加主命题的假设。

### 九元 · 2. 原题反例的完整必要域

**引理2.1。** 若主命题为假，则有同一实际不可二染的简单九元超图满足

$$|E|=542,\qquad57\le v\le195,\qquad\sum_xd(x)=4878,$$

$$\lambda_{xy}\ge1\ (x\ne y),\qquad
\left\lceil\frac{v-1}{8}\right\rceil\le d(x),\qquad
\delta:=\min_xd(x)\le\left\lfloor\frac{4878}{v}\right\rfloor.\tag{2.1}$$

**证明。** 在至多542边的反例中取顶点数最少者。如果两个点从不共边，将二者识别；每条像边仍有九个不同点，重复像边只保留一条。所得超图边数不增加，而且其合法染色可拉回原边，因此仍不可二染，违背最小性。故每个点对被覆盖。

对每个点有$8d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1$，求和得$v\lceil(v-1)/8\rceil\le4878$。左边非减，$195\lceil194/8\rceil=4875\le4878$，而$196\lceil195/8\rceil=4900>4878$，所以v≤195。新端点195包含于本证书。

v≤16时把点分成两个大小均至多八的颜色类。17≤v≤56时，均匀选⌊v/2⌋名点染红，固定九元边单色概率为

$$p(v)=\frac{\binom{\lfloor v/2\rfloor}{9}+\binom{\lceil v/2\rceil}{9}}{\binom v9}.$$

完整40项精确计算给$\max542p(v)=6233/6307<1$，排除这些点数。所有值保存在[PROFILE.json](context/propertyb-m9-543-20261029/PROFILE.json)的`balanced`字段。

于是57≤v≤195；在此域有C(v,9)≥542，故可补入不同九元边至恰542边。补边保持不可二染和点对覆盖；以下全部度数、共度和迹针对补边后的同一实际超图。∎

### 九元 · 3. 条件贪心和八元链接避锁配额

**引理3.1（实际失败见证）。** 固定一个顶点排列，初始全部红色，按序处理当前点：若它是一条当前仍全红边的最后点则改蓝。最终无红色单色边；若有蓝色单色边B，则存在原边A，使A∩B={z}，且z是A的最后点和B的最早点。

**证明。** 最终全红边的最后点在处理时会被改蓝，矛盾。若B全蓝，取其最早点z。它改蓝时有一条仍全红、在z结束的边A，故A除z外全在前，B除z外全在后，交点唯一。∎

固定不同实际锁点$x_j$及不同位置$p_j$，其余顶点在其余位置均匀随机排列。以$\ell_{T}$表示实际原边在锁集上的迹恰为T的条数。原稿第2节给单条T型边在h结束／开始的精确条件概率$e_{h}(T)$,$f_{h}(T)$，以及固定实际有序单交边对在h形成上述见证的权$w_{h}(T,U)$。它们仅依赖实际迹、k=9、自由点数和排列位置，不依赖原边标签。令

$$A_h=\sum_T\ell_Te_h(T),\quad B_h=\sum_T\ell_Tf_h(T),$$

$$C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf1_{T=U})w_h(T,U).$$

全部不同原边对赋非负单交记账权，实际非单交对不会成为失败见证。锁位置若有不超过该位置实际非单交对总记账权的扣除$D_j$，自由位置扣零，则

$$U=\sum_h\min(A_h,B_h,C_h-D_h)\tag{3.1}$$

是实际失败概率上界。三个局部上界分别来自结束边、开始边、实际单交见证的并集界，再对位置取并集界。严格U<1意味着有限条件排列空间中存在一次成功排列，其输出是当前实际全部边的合法染色。

**引理3.2（九元避锁配额）。** 固定锁j及其余锁子集R。含j且避开R的f条实际边，删去j后是支撑至多N=v−1−|R|的不同八元集合。它们相交无序对数Q满足

$$8f\le N+7Q,\qquad Q\ge q_R:=\max\left(0,\left\lceil\frac{8f-N}{7}\right\rceil\right).\tag{3.2}$$

在含j的无序迹型胞{T,U}中，容量为C($\ell_{T}$,2)或$\ell_{T}$ $\ell_{U}$，每个实际坏对的记账权为$w_{h}(T,U)$+wh(U,T)。在避开R的胞中按权从低到高填足$q_R$单位，所得$D_R$不超过同一实际坏对总权。因此$D_j$=maxRDR是合法扣除；只用R空集也是合法的完整池扣除。

**证明。** 每点链接重数a满足a≤1+C(a,2)。按点求和再换序得8f≤N+Σ链接对|L∩L′|。原边简单，所以链接互不相同，两个不同八元集合交至多七，得到(3.2)。实际坏对同时属于其真实迹型胞并满足容量；其总权不小于每个单项配额的最小成本，也不小于这些成本的最大值。各R成本没有相加，不会重复扣除。∎

[repair.py](context/propertyb-m9-543-20261029/repair.py)中的`AvoidCalculator`实现此最大扣除，完整池原语来自原`Calculator`。最终证书只有零、一、二及三锁，不需要新的原超图分类。

### 九元 · 4. 选锁与完整迹域

**引理4.1（最低度单位伙伴）。** 取实际最低度点x，d=d(x)。若

$$n=2(v-1)-8d>0,$$

则其单位共度伙伴至少n人。选择其中最低度点y，e=d(y)，则

$$d\le e\le B:=d+\left\lfloor\frac{4878-vd}{n}\right\rfloor.\tag{4.1}$$

若

$$t=n-1-(8e-(v-1))>0,$$

则x,y的实际共同单位伙伴中可选最低度点z，f=d(z)，满足

$$e\le f\le F:=e+\left\lfloor\frac{4878-vd-n(e-d)}t\right\rfloor.\tag{4.2}$$

**证明。** x的共度超额为8d−(v−1)，故非单位伙伴至多该数，单位池A大小r≥n。全体点最低度为d，而A全体度至少e，故4878≥vd+r(e−d)≥vd+n(e−d)。共同池在A\{y}中，去掉y至多8e−(v−1)名非单位伙伴后仍至少t人；它们度均至少f≥e。实际度数预算给4878≥vd+n(e−d)+t(f−e)，从而两式成立。三个点均是实际不同顶点，两两共度一。∎

**引理4.2（高点数低度单位三锁）。** 对183≤v≤195，存在三名实际度数介于$\delta_0$=⌈(v−1)/8⌉与28之间、两两共度一的点。

**证明。** 令L={d≤28}，r=|L|，Z=29v−4878>0，T=234−v。在L上以共度至少二连冲突边，点x的冲突度至多8d(x)−(v−1)。外部顶点度至少29，所以$r+2e(G)\le Tr-8Z$。随机排列独立集期望及Cauchy–Schwarz给$\alpha(G)\ge r^2/(Tr-8Z)$，分母正。并且

$$r^2-2(Tr-8Z)=(r-T)^2+16Z-T^2>0,$$

因为完整13个整数的最小差为4263（v=183）。故α(G)>2，存在三个独立点，点对覆盖使它们共度恰一。∎

**引理4.3（完整实际迹）。** 一锁度d时，$\ell_{1}$=d、$\ell_{0}$=542−d。二单位锁度d,e时

$$\ell_{12}=1,\quad\ell_1=d-1,\quad\ell_2=e-1,\quad\ell_0=543-d-e.$$

三单位锁的实际迹恰有两种：

$$\begin{array}{c|c|c|c}
\text{模式}&\text{多锁迹}&\text{单锁迹}&\text{空迹}\\\hline
\text{一条三重边}&\ell_{123}=1&\ell_i=d_i-1&544-\sum_i d_i\\
\text{三个点对边}&\ell_{12}=\ell_{13}=\ell_{23}=1&\ell_i=d_i-2&545-\sum_i d_i.
\end{array}$$

**证明。** 单、二锁公式由实际度数与边数直接恢复。三锁每个点对仅有一条共边：若三点共边，它用尽全部三对容量；否则三对各属于一条不同边。这两种耗尽全部实际可能，剩余重数由度数与总边数确定。∎

### 九元 · 5. 完整决策树与精确证书

**引理5.1。** 对引理2.1的每个实际输入，下述有限决策树都到达一个严格U<1的实际迹型。

**证明。** 所有最低度域均按(2.1)从头计算；所有伙伴和第三点度数域均使用(4.1)–(4.2)。证书是以下完整分流，不能把各阶段的顶点区间误读为每个点数仅适用一种方法。

**57–134点。** 不取锁。点对覆盖给多交无序原边对数至少

$$q(v)=\max\left(0,\left\lceil\frac{542\binom92-\binom v2}{\binom82}\right\rceil\right).$$

因此实际有序单交原边对数至多542·541−2q(v)。在原稿第2节的零锁公式中代入这些新常数，78个点数全严格。

**135–154点。** 对每个完整实际最低度d，先取一锁、位置⌊v/2⌋。证书中287个一锁型严格（135–149的全部最低度型，以及150–153的部分型）。其余最低度型使用引理4.1选择实际最低度单位伙伴，并遍历其完整e区间。该区间每个型都有成功二锁界。154点没有一锁成功叶，全部最低度域由二锁覆盖。

**155–182点。** 对每个完整实际最低度d，直接使用引理4.1的全部二锁伙伴域。严格二锁型即结束；未严格的73个实际(d,e)父型位于175–182点。对每个父型，(4.2)的共同池t均正，最小115；完整第三度区间最大上端28。逐项保留f=e,…,F及引理4.3的两种完整实际三锁迹，共480型，全部严格。

**183–195点。** 用引理4.2选三名度至多28的单位锁，将度数非减排序，遍历$\delta_0$≤d1≤d2≤d3≤28及两种实际迹，共976型，全部严格。新195点也在此完整域内。

成功二锁叶总计1629型；其实际位置与扣除方法逐行记录。全体叶及精确最大值为

|成功叶|完整型数|点数跨度|最大有理上界|
|---|---:|---:|---:|
|零锁|78|57–134|106487496857099087577/106600839931609480600|
|一锁|287|135–153|1972282554392680909022596/1972426008426513683838795|
|二锁|1629|150–180|394476918471453327981799/394489458501784689243720|
|实际条件三锁|480|175–182|896688388734878356588012/904701259945736563545105|
|低度三单位锁|976|183–195|41317885902922681304309/41563621287040215236328|
|合计|3450||全部严格|

这里一、二锁的点数跨度只是成功叶出现的范围；181、182的实际二锁域全部继续到条件三锁，并未遗漏。[coverage.py](context/propertyb-m9-543-20261029/coverage.py)独立于原阶段循环重建整棵决策树：先按v,d列出全部输入，再按每个实际最低度单位伙伴的e域列出子节点，若无二锁叶则按实际共同池重建所有f和两个迹。它核对叶键集合与3450行恰相等，无重复、无缺口；同时检查每行总边数542、实际度数、全部单位共度、非负迹及真实位置。完整73个父型和f上限保存在[SUMMARY.json](context/propertyb-m9-543-20261029/SUMMARY.json)的`conditional_parents`字段。

每行精确概率已由`Calculator(9,542)`或八元链接`AvoidCalculator(9,542)`实际计算，所有分数均严格小于一。具体布局属于同一实际锁点的合法条件排列，选择一个成功布局不改变实际超图或迹。因此每个实际输入都到达引理3.1–3.2的合法严格充分界。∎

### 九元 · 6. 原命题装配

**主命题的证明。** 假设原命题存在反例。引理2.1给同一实际恰542边、点对覆盖的反例，顶点数在57–195。引理4.1或4.2为它选择实际锁点，真实迹属于引理4.3的完整分类。引理5.1把全部顶点数、最低度、单位伙伴和三锁迹域覆盖完毕，给一个严格失败概率上界。有限实际排列空间中必有成功排列，贪心输出是补边后超图的合法二染色，故也染好原来至多542条边，矛盾。因而主命题成立，m(9)≥543。∎

### 九元 · 7. 复算入口与验证状态

从项目根运行：

```sh
python3 context/propertyb-m9-543-20261029/profile.py
python3 context/propertyb-m9-543-20261029/candidate.py
python3 context/propertyb-m9-543-20261029/coverage.py
```

[profile.py](context/propertyb-m9-543-20261029/profile.py)重建新参数的完整必要域和基础条件概率；[candidate.py](context/propertyb-m9-543-20261029/candidate.py)构造本证明使用的完整成功叶；[coverage.py](context/propertyb-m9-543-20261029/coverage.py)重建实际决策树与每行输入绑定。前两次实际计算分别约16.73和6.56CPU秒；全部有界数值工作连同辅助试算和最终覆盖核查约25.71CPU秒，未耗尽60秒初始预算。

作者算术复用原二项式概率原语。独立检查另写下降阶乘注入概率、避锁扣除及决策树生成，不导入作者数值或域生成模块；完整3450型全部精确相等且严格，含域重算约30.09 CPU秒。Grok与Gemini均静态核查完整数学链和计算依据，均未执行程序。此处记录本参数自身的验收，不借用六元或七元审阅状态；本参数无Lean或第二台机器复现。


## 独立核验、证书与复现

八元证明的47–120点完整实际参数域、全部2094型概率及299项七元链接组件配额已由另一套实现重建并精确复算；所有有理值与提交证书逐项相等，且均严格小于一。详见[八元独立审阅](context/propertyb-m8-267-20261029/independent/REVIEW.md)、[完整核验记录](context/propertyb-m8-267-20261029/independent/CHECK.json)和[原始精确证书](context/propertyb-m8-267-20261029/CERTIFICATE.json)。

九元证明的57–195点完整决策树已由不导入作者数值或域生成模块的实现独立重建，包括319次一锁分流测试、1702次二锁分流测试及73个实际条件三锁父型。全部3450个成功叶以具名自由顶点的下降阶乘注入计数复算，逐项精确相等且严格。详见[九元独立审阅](context/propertyb-m9-543-20261029/independent/REVIEW.md)、[完整核验记录](context/propertyb-m9-543-20261029/independent/CHECK.json)和[原始成功叶](context/propertyb-m9-543-20261029/CANDIDATE.json)。

这里的“独立”指不同概率实现与完整输入域重建，不表示第二台机器复现或形式化内核认证。两项仍使用所列条件贪心数学机制及普通精确整数／有理数软件信任；完整证明已在使用处写明实际选点、迹分类和合法扣除。联合静态终审的实际范围见[审阅处置](context/propertyb-small-updates-20261029/reviews-8-9/DISPOSITION.md)，原[审阅范围](context/propertyb-small-updates-20261029/reviews-8-9/REQUEST.md)一并保留。

复算命令：

```sh
python3 context/propertyb-m8-267-20261029/independent/check.py
python3 context/propertyb-m9-543-20261029/independent/check.py
```
