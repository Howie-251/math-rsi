# k=12：锁点证书的更强局部下界

**完整整数证书给出 $m(12)\ge4661$ 的计算机辅助证明候选。** 它将同一 RS 最大预算基线 $4633$ 提高 $28$；较直接优化结构 RS 判据所得 $4647$ 再提高 $14$。原方法是合作者的一至三锁有限证书准则；本次贡献是它在 $k=12,M=4660$ 的完整新实例及迁移核查。新实例尚未 Lean 形式化；独立参数域与算术检查已在明确范围内通过，指定跨模型讨论的状态在末节分别列出。

| 路线 | $m(12)$ 下界 | 相对同一基线 $4633$ | 结论与证据范围 |
|---|---:|---:|---|
| 同一最大 RS 预算基线 | 4633 | 0 | $B_{\rm RS}(12)=4632$；本文定义的最大接受整数预算 |
| 一般增长定理 | 4635 | +2 | 全部 $k\ge12$ 的统一定理；已端到端 Lean |
| 直接优化结构 RS 判据 C.2 | 4647 | +14 | $k=12$ 的严格局部数值；不是本次锁点法 |
| 合作者锁点法的新实例 | **4661** | **+28** | 纸面归约＋691429 个完整局部型的整数证书；尚未 Lean |

统一方法提供无限参数范围和已完成的形式证明；锁点法在这一固定参数上给出更强数值。本表的 +2、+14、+28 使用同一个 k=12 基线；总览图现已统一采用已核参考下界的最大值：$k=11$ 的共同基线为 $2245$，故其红线增益是 $2275-2245=30$，与本页 $k=12$ 的 $28$ 使用同一比较规则。此前相对 GL 公式 $2213$ 的 $62$ 保留在历史附表。这里没有据单次成功断言 $k=6,\dots,11$ 都容易，也没有把有限实例外推成任意大的 $k$ 都能同样推进。比较基线及 C.2 的原始数值见 [k=12…16 数值报告](context/propertyb-general/bridge-12-16-20261021/NUMERIC_REPORT.md)，一般定理的证明见 [完整 Lean 阅读页](PROPERTY_B_GENERAL_LEAN.html)。

## 1. 对象、来源与结论

**定义 1.1（Property B 与 $m(k)$）。** 有限简单 $k$ 元超图是有限集合 $V$ 及由不同 $k$ 元子集组成的边集 $E$。若存在 $c:V\to\{\mathrm{red},\mathrm{blue}\}$，使每条边同时含两色，则称其具有 Property B。$m(k)$ 是不具有 Property B 的此类超图的最少边数。

**来源说明。** 下文的随机排列、条件概率公式、最轻坏对扣除、统一证书准则和一般选锁定理，来自合作者 [《一般 k-uniform Property B 的锁点证书定理：k=10,11 的严格整数验证》](propertyB_small_k/propertyB_k10_k11_research.md) 的**定理 A、其“数学基础”全节以及定理 B**。它们本来就对一般 $k\ge3$ 成立；不能将这套方法归为本次新发明。下文把完整公式和证明连接重述在同一阅读页。原作者 $k=10,11$ 的实例不作为 $k=12$ 的计算证据。

**定理 1.2（本次实例，计算机辅助证明候选）。** 任意有限简单 12 元超图，若边数至多 $4660$，则具有 Property B。因此

$$m(12)\ge4661.$$

**证明结构。** 引理 2.1 将任意假定反例归到同一实际的点对覆盖、恰有 $4660$ 条边、$93\le v\le782$ 的超图。引理 3.1–3.4 给出真实失败概率的证书上界；引理 4.1–4.3 保证所用锁点及全部迹型。命题 5.2 的整数计算覆盖每个候选点数及每个必要参数型，并逐型严格小于统一分母。于是每个反例都具有成功概率为正的染色，矛盾。具体公式、覆盖和证书结果如下；本页的“候选”状态指新实例尚待指定验收，不将尚未完成的审阅写成通过。$\square$

## 2. 从原始超图到完整有限点数域

**引理 2.1（最小反例与补边；合作者定理 A 的实例化）。** 若存在至多 $M=4660$ 边的有限简单 12 元不可染超图，则存在同一类型的反例 $H$，恰有 $M$ 条边，每点对共边，且顶点数恰落在 $93\le v\le782$。

**证明。** 在全部至多 $M$ 边的反例中取顶点数最小者。若两个不同点不共边，将它们合并；每条边仍含 12 个不同点，去重后边数不增。商图任何染色都可拉回原图，故商仍不可染，矛盾。因此任意点对共边。记 $d(x)$ 为度数、$\lambda_{xy}$ 为共度，则

$$11d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1,\qquad d_0(v)=\left\lceil\frac{v-1}{11}\right\rceil,\qquad vd_0(v)\le12M.$$

当 $v\le22$ 时，将两色类都取成至多 11 点即可。其余点数使用均衡随机染色；每条边单色的概率为

$$p_{v,12}=\frac{\binom{\lfloor v/2\rfloor}{12}+\binom{\lceil v/2\rceil}{12}}{\binom v{12}}.$$

若 $Mp_{v,12}<1$，并集界直接给可染。完整整数筛查 $23\le v\le12M$，同时保留 $vd_0(v)\le12M$ 与 $Mp_{v,12}\ge1$，所得域恰为 $93,\dots,782$；不是取样。尾部还有显式界

$$783\left\lceil\frac{782}{11}\right\rceil=56376>55920=12M,$$

且左侧随 $v$ 单调不减。又

$$\binom{93}{12}=416579843773639>M.$$

可在原顶点集补入不同的 12 边直至恰有 $M$ 条；不可染性和点对覆盖保留。以下所有度数、迹重数及坏对均取自**这一补后同一个实际 $H$**。$\square$

## 3. 条件排列与真实失败概率

**定义 3.1（锁点和精确迹）。** 取 $s\in\{0,1,2,3\}$ 个不同实际顶点 $x_1,\dots,x_s$，固定在排列位置 $t_1<\cdots<t_s$，其余 $N=v-s$ 点在空位上均匀随机排列。对一条实际边 $e$，令其迹 $T(e)=\{j:x_j\in e\}\subseteq[s]$，其重数为 $\ell_T$，自由顶点数为 $r_T=k-|T|$。对位置 $h$，令 $a_h,b_h$ 为其严格左／右侧自由空位数，$I_h^-,I_h^+$ 为其严格左／右侧锁点标签集合。约定不满足组合条件的二项式为零。

**引理 3.1（失败的实际单交见证；合作者定理 A）。** 初始全红，按排列依次处理各点；仅当当前点是某条仍全红边的最后点时将它改蓝。最终没有全红边；若有全蓝边，则存在实际有序边对 $(A,B)$，满足

$$A\cap B=\{x\},\qquad \max_\sigma A=\min_\sigma B=x.$$

**证明。** 红边在其最后点处必被破坏。若最终有蓝边 $B$，取它排列中第一个顶点 $x$。$x$ 改蓝时有一条仍全红的见证边 $A$，且 $x$ 是 $A$ 的最后点。若 $A,B$ 另共享 $y$，由 $A$ 得 $y$ 早于 $x$，由 $B$ 得 $y$ 晚于 $x$，矛盾。$\square$

**定义 3.2（精确有序单交权重）。** 对固定的实际单交对、迹为 $T,U$，其见证点恰处于 $h$ 的概率如下。若 $h$ 自由，$T\subseteq I_h^-$、$U\subseteq I_h^+$，$r_T,r_U\ge1$ 且 $r_T+r_U-1\le N$，则

$$w_h(T,U)=\frac{\binom{a_h}{r_T-1}\binom{b_h}{r_U-1}}{N\binom{N-1}{r_T-1}\binom{N-r_T}{r_U-1}}.$$

若 $h=t_j$，$T\cap U=\{j\}$，$T\setminus\{j\}\subseteq I_h^-$、$U\setminus\{j\}\subseteq I_h^+$ 且 $r_T+r_U\le N$，则

$$w_h(T,U)=\frac{\binom{a_h}{r_T}\binom{b_h}{r_U}}{\binom N{r_T}\binom{N-r_T}{r_U}}.$$

其余情形为零。这些是依次无放回选择左右顶点集的联合计数，没有假设左右事件独立。

**定义 3.3（单边端点概率）。** 单边终点概率为

$$\operatorname{last}_h(T)=\begin{cases}\displaystyle\frac{r_T}{N}\frac{\binom{a_h}{r_T-1}}{\binom{N-1}{r_T-1}},&h\text{ 自由},\ T\subseteq I_h^-,\ r_T\ge1,\\\displaystyle\frac{\binom{a_h}{r_T}}{\binom N{r_T}},&h=t_j,\ j\in T,\ T\setminus\{j\}\subseteq I_h^-,\\0,&\text{其他情形}.\end{cases}$$

$\operatorname{first}_h(T)$ 将左右对调。置

$$A_h=\sum_T\ell_T\operatorname{last}_h(T),\quad B_h=\sum_T\ell_T\operatorname{first}_h(T),\quad C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf1_{T=U})w_h(T,U).$$

**引理 3.2（加权 link 扣除；合作者定理 A）。** 在锁点 $x_j$ 的位置 $h=t_j$，至少有

$$q_j=\left\lceil\frac{(k-1)d(x_j)-(v-1)}{k-2}\right\rceil$$

个无序 incident 边对还共享中心以外的点。对都含 $j$ 的类型 $T,U$，令容量和双向权重分别为

$$\operatorname{cap}(T,U)=\begin{cases}\binom{\ell_T}{2},&T=U,\\\ell_T\ell_U,&T\ne U,\end{cases}\qquad \delta_h(T,U)=w_h(T,U)+w_h(U,T).$$

从全部类型对槽位按 $\delta_h$ 升序取最轻的 $q_j$ 个，按容量计重，和为 $D_h$；自由位置令 $D_h=0$。则真实失败概率满足

$$\Pr(\mathrm{Fail})\le U:=\sum_{h=1}^v\min\{A_h,B_h,C_h-D_h\}.$$

**证明。** 去掉中心后的 $d=d(x_j)$ 条 link 边是不同的 $(k-1)$ 元集合，覆盖全部 $v-1$ 点。令外点出现次数为 $r_y\ge1$。重复超额

$$E_j=(k-1)d-(v-1)=\sum_y(r_y-1)\le\sum_y\binom{r_y}{2}$$

等于或小于所有 link 边对交集大小之和；每一非空交集至多 $k-2$ 点。因此至少有 $q_j$ 个额外相交的无序对。这些对不能是真实单交见证。真实坏对在类型槽位中占据至少 $q_j$ 个位置，其权重和至少为最轻槽位和 $D_h$；零权槽位同样计入，不能跳过。$C_h-D_h$ 因而仍是见证事件的并集上界。该事件也分别被“某边终止于 $h$”和“某边始于 $h$”覆盖，概率分别至多 $A_h,B_h$；可逐位置取三者最小值，再对 $h$ 求和。扣除仅用于该锁点位置，没有跨位置重复收费。$\square$

**引理 3.3（零锁的全局修正；合作者定理 A）。** 点对覆盖时，至少有

$$Q_v=\max\left\{0,\left\lceil\frac{M\binom k2-\binom v2}{\binom{k-1}2}\right\rceil\right\}$$

个无序多交边对，故有序单交对数至多 $M(M-1)-2Q_v$。零锁计算将这一数量代入 $C_h$。

**证明。** 按顶点对或边对双计数，且 $\binom\lambda2\ge\lambda-1$，得

$$\sum_{\{A,B\}}\binom{|A\cap B|}{2}=\sum_{\{x,y\}}\binom{\lambda_{xy}}2\ge M\binom k2-\binom v2.$$

不同简单边交集至多 $k-1$，每个多交对贡献至多 $\binom{k-1}2$，从而得到 $Q_v$。$\square$

## 4. 实际锁点存在与两型覆盖

**引理 4.1（一锁及二锁；合作者定理 A）。** 一锁可取全图最低度点，其度数满足

$$d_0(v)\le d\le\left\lfloor\frac{kM}{v}\right\rfloor.$$

若 $s_d=2(v-1)-(k-1)d>0$，则存在与该点共度恰为 1、度数 $e$ 满足 $d\le e\le B_d$ 的第二点，其中

$$B_d=d+\left\lfloor\frac{kM-vd}{s_d}\right\rfloor.$$

一锁重数为 $\ell_\varnothing=M-d,\ell_{\{1\}}=d$；二锁重数为

$$\ell_\varnothing=M-d-e+1,\quad \ell_{\{1\}}=d-1,\quad\ell_{\{2\}}=e-1,\quad\ell_{\{1,2\}}=1.$$

**证明。** 最低度不超过平均度。若与最低度点共度 1 的点有 $n_1$ 个，其余共度至少 2，故 $(k-1)d\ge2(v-1)-n_1$，即 $n_1\ge s_d$。若这些点全度至少 $B_d+1$，总度至少 $vd+s_d(B_d+1-d)>kM$，矛盾。重数由共度恰 1 和实际度数恢复。$\square$

**引理 4.2（一般选锁定理；合作者定理 B）。** 对任意点对覆盖的简单 $k$ 元超图，令

$$D\ge d_0(v),\quad Z=(D+1)v-kM,\quad T=(k-1)(D+1)-v+2.$$

若整数 $s\ge2$ 满足

$$Z>0,\qquad4(k-1)Z>(s-1)T^2,$$

则存在 $s$ 个度数至多 $D$、两两共度恰为 1 的点。

**证明。** 令 $L=\{x:d(x)\le D\}$，$r=|L|$。由 $Z>0$ 得 $r>0$，总度预算给 $\sum_{x\in L}d(x)\le r(D+1)-Z$。在 $L$ 上按 $\lambda_{xy}\ge2$ 连辅助图 $G$；每点的这类邻点数至多 $(k-1)d(x)-(v-1)$，故

$$2e(G)\le(T-1)r-(k-1)Z.$$

Caro–Wei 和 Cauchy–Schwarz 给

$$\alpha(G)\ge\frac{r^2}{r+2e(G)}\ge\frac{r^2}{Tr-(k-1)Z}.$$

这里分母由前式至少为 $r>0$。又

$$r^2-(s-1)\bigl(Tr-(k-1)Z\bigr)=\left(r-\frac{(s-1)T}{2}\right)^2+(s-1)(k-1)Z-\frac{(s-1)^2T^2}{4}>0.$$

所以 $\alpha(G)>s-1$，有至少 $s$ 个两两无辅助边的点；原点对覆盖保证其共度恰为 1。$\square$

**引理 4.3（三锁迹型完备；合作者定理 A）。** 对两两共度恰为 1 的三锁，恰有以下两种多点迹；度数排序为 $d_1\le d_2\le d_3$ 后，全部重数为

$$\begin{array}{ll}\mathrm{triple}:&\ell_{123}=1,\quad\ell_i=d_i-1,\quad\ell_\varnothing=M-d_1-d_2-d_3+2;\\\mathrm{separate}:&\ell_{12}=\ell_{13}=\ell_{23}=1,\quad\ell_i=d_i-2,\quad\ell_\varnothing=M-d_1-d_2-d_3+3.\end{array}$$

未列的迹重数均为零。

**证明。** 若有一条边含三锁，则它已经使用全部三对的唯一共边，不再有二点迹。否则三个点对各由不同边承载，得到三个二点迹。其余单点迹与空迹由各点实际度数和总边数唯一确定；没有第三型。排序只是给实际点重新命名，并将其放到相应固定位置；不需要概率公式对三个位置对称。$\square$

**定义 4.4（本次布局和完整枚举域）。** 一锁位置为 $\lfloor v/2\rfloor$；二锁为 $\lfloor v/2\rfloor,\lfloor v/2\rfloor+1$；三锁为 $\lfloor v/2\rfloor-1,\lfloor v/2\rfloor,\lfloor v/2\rfloor+1$。一锁枚举引理 4.1 的全部 $d$；二锁对每个这样的 $d$ 验证 $s_d>0$ 并枚举全部 $d\le e\le B_d$。三锁取 $d_0\le D\le M$ 中使

$$Z=(D+1)v-12M>0,\qquad22Z>[11(D+1)-v+2]^2$$

成立的最小整数 $D$，枚举全部 $d_0\le d_1\le d_2\le d_3\le D$ 及两种迹型。此处没有原 helper 的 $D\le d_0+49$ 截断，也没有用“最小度配置最坏”的未经证明单调性代替枚举。必要域允许包含无实际超图实现的类型；关键是包含每个实际输入且全部类型都满足严格证书界。

## 5. 向外舍入、逐位置最小值与完整整数证书

**引理 5.1（整数证书的方向）。** 取 $S=2^{52}=4503599627370496$。对所有概率上界系数用 $\lceil Sp\rceil$；对每一方向的坏对删除权重用 $\lfloor Sw\rfloor$。具体置

$$\widehat A_h=\sum_T\ell_T\lceil S\operatorname{last}_h(T)\rceil,\qquad\widehat B_h=\sum_T\ell_T\lceil S\operatorname{first}_h(T)\rceil,$$

$$\widehat C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf1_{T=U})\lceil Sw_h(T,U)\rceil.$$

把每个无序槽位赋权 $\lfloor Sw_h(T,U)\rfloor+\lfloor Sw_h(U,T)\rfloor$，按这些**已向下舍入的权重**排序取最轻 $q_j$ 个，得到 $\widehat D_h$。自由位置为零。则

$$\Pr(\mathrm{Fail})\le U_{\rm cert}/S,\qquad U_{\rm cert}=\sum_{h=1}^v\min\{\widehat A_h,\widehat B_h,\widehat C_h-\widehat D_h\}.$$

**证明。** 每个上界项向上舍入。任何真实坏对集合的原权重不小于它自己的向下舍入权重，后者又不小于全部槽位中最轻的 $q_j$ 个的和。因此减去 $\widehat D_h$ 仍保留上界，重新排序不会破坏方向。三个数各自都是同一实际位置失败事件的上界，故其最小值也是上界；最后求和。严格的 $U_{\rm cert}<S$ 就足以给出正的成功概率，不使用浮点近似。零锁按引理 3.3 修正后的对数向上舍入计算。$\square$

**命题 5.2（$k=12,M=4660$ 的完整计算）。** 下表覆盖全部 690 个候选点数，全部 691429 个必要局部参数型。每个最终分子严格小于 $S$。

| 锁数 | 点数 $v$ | 完整型数 | 最大 $U_{\rm cert}$ | 最大处 | $S-\max U_{\rm cert}$ |
|---:|---|---:|---:|---|---:|
| 0 | 93–511 | 419 | 4503308793007378 | $v=511$ | 290834363118 |
| 1 | 512–564 | 2929 | 4503474369079970 | $v=564,d=52$ | 125258290526 |
| 2 | 565–648 | 87807 | 4503473506514732 | $v=648,(d,e)=(59,59)$ | 126120855764 |
| 3 | 649–782 | 600274 | 4498353804903973 | $v=782,(71,71,71)$，separate | 5245822466523 |

**计算证据。** 完整逐点数记录在 [M4660.json](context/propertyb-general/k12-lock-pilot-20261021/pilot/M4660.json)，分段及计数在 [SUMMARY.json](context/propertyb-general/k12-lock-pilot-20261021/pilot/SUMMARY.json)，实际执行日志在 [M4660.log](context/propertyb-general/k12-lock-pilot-20261021/pilot/M4660.log)。全部计算墙钟 86.712 秒、CPU 84.620 秒、峰值 RSS 42.8 MB。这是完整局部度数／迹型证书，不是整图枚举，也不是由几张抽样超图归纳。

NumPy 只做确切 signed int64 的非负乘加。所有最终使用的 271 张锁表均检查了安全界：$M^2W_{\max}$ 的全局最大值为 $95038134995454400$，$M P_{\max}$ 的全局最大值为 $492840100122427600$，均小于 $2^{63}-1=9223372036854775807$。坏对扣除受同一对数容量界约束，最终逐位置最小值的和由 Python 无界整数计算。两个完整运行 $M=4647,4660$ 共七个分段最紧型，另经原 `FixedCertificate` 的纯 Python 大整数路径逐位复核；这七型复核本身不被描述为第二实现重跑全部 691429 型。$\square$

**定理 1.2 的完成。** 任意假定反例先由引理 2.1 进入实际候选域。每个点数落入命题 5.2 的某段；引理 4.1 或 4.2 给出真实锁点，引理 4.3 和定义 4.4 保证其真实型被枚举。引理 3.1–3.3 与 5.1 将对应分子接回该超图的失败概率。命题 5.2 给严格小于 1，因此某个条件排列的贪心结果是正确二染色，矛盾。原命题不增加点数、点对覆盖、度数、锁点或证书作为外部前提。$\square$

## 6. 证据状态与未通过试验的准确含义

本次已经取得纸面迁移归约和完整整数证书。新实例尚未 Lean 形式化。独立实现已重建全部 690 个候选点数、全部 691429 个必要参数型，无漏项或重复；其中二锁的 $B_d$ 直接由严格整数不等式搜索，三锁的最小 $D$ 在完整区间中重新搜索。另以独立 Python `Fraction` 公式复算 31 个型，覆盖各段最紧型、锁数交界两侧、度数上下端点及两种三锁迹型，精确值均不超过原证书上界且严格小于 1。零／一锁的全部 3348 型还由独立 $10^{20}$ 分母、Python 大整数实现完整重放，1.690 秒，全部严格小于 1。二／三锁尚未由第二实现全量重算概率；不能称 691429 型都完成双算术复核。该检查是 same-family / provisional，范围详见 [independent/REPORT.md](context/propertyb-general/k12-lock-pilot-20261021/independent/REPORT.md)，不负责以计算证明选锁结构引理。Grok 初次数学讨论已有效返回（`grok-4.7-build`、`xhigh`、`end_turn`）：一般选锁准则与概率计数可迁移至 $k=12$，并要求完整覆盖实际输入域。该次讨论的提示使用早期 $M=4647$ 试算，未审阅最终 $M=4660$ 全表，不能记为最终新实例已获跨家族终审。[原始回应](context/propertyb-general/k12-lock-pilot-20261021/GROK_REVIEW.json)保留原文；其中关于补边的压缩说法以本页引理 2.1 的正确方向为准：原图不可染蕴含加边后不可染，加边后的染色限制为原图染色。原始迁移核查见 [STRUCTURAL_TRANSFER.md](context/propertyb-general/k12-lock-pilot-20261021/STRUCTURAL_TRANSFER.md)，计算说明见 [pilot/REPORT.md](context/propertyb-general/k12-lock-pilot-20261021/pilot/REPORT.md)。迁移报告末尾在途描述是早于完整 M4660 结果的历史快照。

$M=4670$ 的当前 driver 在 $v=507$ 失败：零锁分子 $4518736808473300>S$，一锁 $d=46$ 分子 $4504066958865140>S$；二锁必要度域含 $d=92$、此时 $s_d=0$；全部 $46\le D\le4670$ 中三锁的严格差最大仍为 $-507442$。这是“每个 $v$ 统一选一个零／一／二／三锁模式”的当前策略未取得完整证书。按度数混合不同锁数的分流尚未测试；失败不是不可染反例，不是锁点法上限，本次不展开新的研究。

## 7. 源码与复现

原合作者方法与公式：[原稿定理 A/B](propertyB_small_k/propertyB_k10_k11_research.md)；原算术实现：[FixedCertificate](context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_certified.py)、[FastExact](context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_verified.py)。本次新增：[完整 driver](context/propertyb-general/k12-lock-pilot-20261021/pilot/scan.py)、[标量重放与安全汇总](context/propertyb-general/k12-lock-pilot-20261021/pilot/replay.py)、[分段汇总](context/propertyb-general/k12-lock-pilot-20261021/pilot/summarize.py)。原作者文件保持原样。

在项目根目录执行：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .tools/math-python/bin/python context/propertyb-general/k12-lock-pilot-20261021/pilot/scan.py 4660 --seconds 350
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .tools/math-python/bin/python context/propertyb-general/k12-lock-pilot-20261021/pilot/replay.py
.tools/math-python/bin/python context/propertyb-general/k12-lock-pilot-20261021/pilot/summarize.py
```

本页独立于一般增长主阅读页与已发布图；它展示一个新固定参数实例，不改写旧小参数实例的验收状态。
