# 单交边对的结构上界与一般二染色判据

<a id="core-definition-1"></a>

## 定义1：超图、二染色与单交边对

设 $k\ge2$ 为整数。有限简单 $k$ 元超图是二元组 $H=(V,E)$，其中 $V$ 为有限集合，$E\subseteq\binom Vk$ 为集合；因而每条边有恰好 $k$ 个顶点，且没有重复边。记 $v=|V|$、$m=|E|$。

若存在染色 $c:V\to\{0,1\}$，使每条边 $f\in E$ 都满足

$$
\exists x,y\in f,\qquad c(x)=0,\quad c(y)=1,
$$

则称 $H$ 具有 **Property B**。记 $m(k)$ 为不具有 Property B 的有限简单 $k$ 元超图的最小边数。此最小值存在：顶点数为 $2k-1$ 的完全 $k$ 元超图在任意二染色中都有至少 $k$ 个同色顶点，故不具有 Property B。

定义实际有向单交边对集合及其大小为

$$
\mathcal P(H)=\{(f,g)\in E\times E:f\ne g,\ |f\cap g|=1\},
\qquad \gamma(H)=|\mathcal P(H)|.
$$

其中 $(f,g)$ 与 $(g,f)$ 分别计数。定义单交图 $S(H)$ 为以 $E$ 为顶点集的简单图，两条不同原边在 $S(H)$ 中相邻，当且仅当它们恰交一点。

<a id="core-definition-2"></a>

## 定义2：解析量与结构上界

对整数 $k\ge2$、实数 $0<p\le1$ 及整数 $M\ge1$，定义

$$
d_k=2^{k-1},\qquad
 a_k(p)=1-(1-p)^k,\qquad
 J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

以及

$$
v_k(M)=\left\lfloor\frac{1+\sqrt{1+4k(k-1)M}}2\right\rfloor,
\qquad
g_k(M)=\min\left\{M(M-1),\left(1-\frac1{v_k(M)}\right)M^2\right\}.
$$

这里 $0<a_k(p)\le1$、$J_k(p)\ge0$，且 $v_k(M)\ge k$。

<a id="core-definition-3"></a>

## 定义3：随机重染过程及必要事件

给定有限简单 $k$ 元超图 $H=(V,E)$ 和 $0<p\le1$。各顶点 $x\in V$ 独立选初始颜色 $c_x\in\{0,1\}$，两色各以概率 $1/2$ 出现；独立选资格位 $b_x\sim\operatorname{Bernoulli}(p)$ 及时刻 $t_x\sim\operatorname{Unif}[0,1]$。以上全部随机量相互独立。

按时刻递增处理每个顶点一次。处理 $x$ 时，若 $b_x=1$，且存在含 $x$ 的边 $g$ 在初态为单色、截至处理 $x$ 前仍全部保持该初始颜色，则翻转 $x$；否则保持颜色。记最终染色为 $c^{\mathrm{fin}}$，失败事件为

$$
\mathcal F=\{\exists f\in E,\ \exists q\in\{0,1\},\ \forall z\in f,\ c_z^{\mathrm{fin}}=q\}.
$$

时刻互异以概率 $1$ 成立；碰撞时按预先固定的顶点次序处理，不影响下列概率。该过程为 Radhakrishnan–Srinivasan 的延迟重染算法，见 [RS2000, §2 “Slow recoloring”, 作者稿第4页 “The Algorithm”](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=4)。

定义初态残留事件

$$
\mathcal R=\{\exists f\in E:\ f\text{ 初始单色，且 }b_z=0\text{ 对所有 }z\in f\text{ 成立}\}.
$$

对 $(f,g)\in\mathcal P(H)$、$f\cap g=\{x\}$ 和目标颜色 $q\in\{0,1\}$，定义必要事件 $\mathcal N_{f,g}^{q}$ 为以下条件同时成立：

- $g$ 初始全为颜色 $1-q$，且 $b_x=1$；
- 对所有 $z\in f\setminus\{x\}$，若 $c_z=1-q$，则 $b_z=1$ 且 $t_z<t_x$；
- 对所有 $z\in g\setminus\{x\}$，若 $b_z=1$，则 $t_z>t_x$。

此事件仅规定初态、资格位和次序条件；其定义不要求 $f$ 最终单色，也不要求算法实际以 $g$ 触发 $x$ 的翻转。

<a id="core-lemma-1-1"></a>
## 引理1.1：独立 Bernoulli 变量的正关联

设 $b_1,\ldots,b_n$ 为相互独立的 Bernoulli 变量，其参数可分别取 $[0,1]$ 中的任意值。若实函数 $u,w:\{0,1\}^n\to\mathbb R$ 均关于各坐标单调不减，则

$$
\mathbb E[uw]\ge\mathbb E[u]\mathbb E[w].
$$

因此，对任意有限个关于这些坐标递增的事件 $A_1,\ldots,A_r$，有

$$
\Pr\left(\bigcap_{i=1}^r A_i\right)\ge\prod_{i=1}^r\Pr(A_i).
$$

**证明。** 对坐标数 $n$ 归纳。$n=0$ 时两函数均为常数，结论为等式。设结论对 $n-1$ 个坐标成立，并以 $\theta$ 表示最后一位取 $1$ 的概率。全协方差公式给出

$$
\operatorname{Cov}(u,w)
=\mathbb E[\operatorname{Cov}(u,w\mid b_n)]
 +\operatorname{Cov}(\mathbb E[u\mid b_n],\mathbb E[w\mid b_n]).
$$

第一项由归纳假设非负。令 $u_i$、$w_i$ 分别为将最后一位固定为 $i$ 后对其余坐标取期望的值；单调性给出 $u_1\ge u_0$、$w_1\ge w_0$，故第二项等于

$$
\theta(1-\theta)(u_1-u_0)(w_1-w_0)\ge0.
$$

这证明两函数的结论。取事件指示函数即得两个递增事件的正关联；由于递增事件的交仍递增，再对事件个数归纳得到有限交结论。∎

这是独立乘积测度下正关联的自含证明；[RS2000, Appendix A, Claim A.1 的证明，作者稿第26页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)以 FKG 不等式调用这一事实。

<a id="core-lemma-1-2"></a>
## 引理1.2：初态残留概率

设 $k\ge2$、$0<p\le1$，且 $H$ 为实际边数 $m\ge1$ 的有限简单 $k$ 元超图。对定义3的随机过程，至少一条边初始单色且最终保持其初始单色颜色，当且仅当 $\mathcal R$ 发生。并且

$$
\Pr(\mathcal R)\le1-a_k(p)^{m/d_k}.
$$

**证明。** 每个顶点至多翻转一次。因此，初始为颜色 $q$ 的边最终仍全为 $q$，当且仅当它没有顶点翻转。若它的全部资格位为零，便没有顶点翻转。反之，若它存在有资格顶点而最终没有顶点翻转，则其中最早的有资格顶点被处理时，这条边仍全为原色，因而触发翻转，矛盾。这证明所述事件等价。

条件于初始染色，记初始单色边数为 $X$。对每条初始单色边 $f$，事件 $A_f=\{\exists z\in f:b_z=1\}$ 是资格位的递增事件，且其条件概率为 $a_k(p)$。由引理1.1，

$$
\Pr(\mathcal R^{\mathrm c}\mid c)\ge a_k(p)^X.
$$

每条 $k$ 元边初始单色的概率为 $2^{1-k}=1/d_k$，故 $\mathbb E X=m/d_k$。因 $a=a_k(p)>0$，函数 $x\mapsto a^x$ 为凸函数；$a=1$ 时它为常函数。Jensen 不等式于是给出

$$
\Pr(\mathcal R^{\mathrm c})\ge\mathbb E[a_k(p)^X]
\ge a_k(p)^{\mathbb E X}=a_k(p)^{m/d_k}.
$$

取补事件即得结论。∎

此估计及其正关联、Jensen 证明见 [RS2000, Appendix A, Claim A.1，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)。其中原文式(31)是条件平均等式，Claim A.1 的最终概率上界使用正关联与 Jensen；这里保留该上界未作线性放宽的形式。

<a id="core-lemma-1-3"></a>
## 引理1.3：新单色边的必要单交事件

设 $k\ge2$、$0<p\le1$，且 $H$ 为有限简单 $k$ 元超图。对定义3的过程，以概率 $1$ 有

$$
\mathcal F\subseteq\mathcal R\ \cup\!
 \bigcup_{(f,g)\in\mathcal P(H)}\ \bigcup_{q\in\{0,1\}}\mathcal N_{f,g}^{q}.
$$

此外，每个 $(f,g)\in\mathcal P(H)$ 和 $q\in\{0,1\}$ 均满足

$$
\Pr(\mathcal N_{f,g}^{q})=2^{1-2k}J_k(p).
$$

**证明。** 先限制到所有时刻互异的概率 $1$ 事件。若 $f$ 最终全为 $q$，且初态也全为 $q$，则由引理1.2得到 $\mathcal R$。否则，在 $f$ 中初始为 $1-q$ 的非空顶点集中，选取处理最晚者 $x$。这些顶点最终均为 $q$，故均已翻转。$x$ 翻转时，有一条含 $x$ 的触发边 $g$，它初始全为 $1-q$，且直到当时仍全为 $1-q$。

若还存在 $z\in(f\cap g)\setminus\{x\}$，则 $z$ 初始为 $1-q$、最终为 $q$，所以必须在 $x$ 之前翻转；这与 $g$ 在处理 $x$ 时仍保持初始单色矛盾。因此 $f\cap g=\{x\}$。因为 $|f|=k\ge2$，这又蕴含 $f\ne g$。

$x$ 翻转需要 $b_x=1$。$f\setminus\{x\}$ 中所有初始为 $1-q$ 的顶点都在 $x$ 之前翻转，故均有资格且时刻小于 $t_x$。对 $g\setminus\{x\}$ 中任一有资格顶点 $z$，若 $t_z<t_x$，则由于 $g$ 在处理 $x$ 前未有顶点翻转，$z$ 被处理时便会由 $g$ 触发翻转，矛盾。因此 $t_z>t_x$。这些正是 $\mathcal N_{f,g}^{q}$ 的全部条件，覆盖关系得证。这一论证也覆盖 $f$ 初态全为 $1-q$、最终全为 $q$ 的情形。

再固定单交对 $(f,g)$ 及交点 $x$，条件于 $t_x=t$。对每个 $S\subseteq f\setminus\{x\}$，规定 $S$ 恰为该集合中初始颜色为 $1-q$ 的顶点集，同时规定 $g$ 初始全为 $1-q$。因 $|f\cup g|=2k-1$，此初态配置的概率为 $2^{-(2k-1)}$。其余资格及次序条件分别发生于互不相交的顶点集：$x$ 有资格的概率为 $p$；每个 $z\in S$ 有资格且早于 $x$ 的概率为 $pt$；每个 $z\in g\setminus\{x\}$ 不同时满足有资格和早于 $x$ 的概率为 $1-pt$。故相应联合概率为

$$
2^{1-2k}p(pt)^{|S|}(1-pt)^{k-1}.
$$

不同 $S$ 的初始配置互斥。对 $S$ 求和、再对 $t$ 积分，得到

$$
\begin{aligned}
\Pr(\mathcal N_{f,g}^{q})
&=2^{1-2k}p\int_0^1(1-pt)^{k-1}(1+pt)^{k-1}\,dt\\
&=2^{1-2k}\int_0^p(1-y^2)^{k-1}\,dy
=2^{1-2k}J_k(p).
\end{aligned}
$$

最后一步使用换元 $y=pt$。∎

必要事件的单交归约见 [RS2000, §2.1, Lemma 2.1 与 Claims 2.1–2.3，作者稿第5–6页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=5)；精确积分见 [RS2000, Claim 2.4 的证明，作者稿第7页未编号积分式](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)。原文在该积分之后才进一步放宽概率；这里直接保留积分。

<a id="core-lemma-1"></a>
## 引理1：完整RS上界

设 $k\ge2$ 为整数、$0<p\le1$，$H$ 为实际边数 $m\ge1$ 的有限简单 $k$ 元超图。则定义3的实际重染失败概率满足

$$
\Pr(\mathcal F)\le
1-a_k(p)^{m/2^{k-1}}+
\frac{\gamma(H)}{4^{k-1}}J_k(p).\tag{1}
$$

**证明。** 对引理1.3的覆盖关系使用并界，再代入引理1.2及引理1.3的概率式，得

$$
\begin{aligned}
\Pr(\mathcal F)
&\le\Pr(\mathcal R)+\sum_{(f,g)\in\mathcal P(H)}\sum_{q\in\{0,1\}}
\Pr(\mathcal N_{f,g}^{q})\\
&\le1-a_k(p)^{m/2^{k-1}}+2\gamma(H)2^{1-2k}J_k(p),
\end{aligned}
$$

而 $2\cdot2^{1-2k}=4^{1-k}$，故得式(1)。∎

引理1将 [RS2000, Appendix A, Claim A.1](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26) 的残留估计与 [RS2000, Claim 2.4 的证明](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)中的精确积分作用于同一实际算法，并保留实际有向单交对数。式(1)是这些估计的组合，不是对原文某一条定理的逐字转述。

<a id="core-lemma-2"></a>
## 引理2：最小顶点反例覆盖

设整数 $k\ge2$、$M\ge1$。若存在边数至多 $M$ 的非 Property B 有限简单 $k$ 元超图，则其中存在顶点数最少的反例 $H=(V,E)$。对任一这样的 $H$，记 $v=|V|$、$m=|E|$，则 $m\ge1$、$v\ge k$，任意两个不同顶点都同处于至少一条边，且

$$
\binom v2\le m\binom k2\le M\binom k2,
\qquad v\le v_k(M).\tag{2}
$$

此约化见 [Grill–Linzmayer，§1，式(3)前的Goldberg–Russell论证](https://arxiv.org/html/2403.05674v3#S1)。

**证明。** 有限顶点数的非空集合有最小值，故可选取所述 $H$。没有边的超图具有 Property B，因此 $m\ge1$，继而 $v\ge k$。

若两个不同顶点 $x,y$ 从未同处一条边，将它们合并，其他顶点不变。每条原边的像仍有恰好 $k$ 个顶点；以这些像边组成集合得到简单 $k$ 元超图，其边数不超过 $m$。若像超图具有 Property B，将其染色沿合并映射拉回，便使每条原边同时含两色，违背 $H$ 为反例。因此像超图仍为边数至多 $M$ 的反例，却比 $H$ 少一个顶点，矛盾。

于是每对不同顶点至少同处一条边。计数所有“顶点对包含于边”的关联，得 $\binom v2\le m\binom k2\le M\binom k2$。解关于 $v$ 的二次不等式并利用 $v$ 为整数，即得 $v\le v_k(M)$。∎

<a id="core-lemma-3-1"></a>
## 引理3.1：由团数控制图的边数

设 $G$ 为有 $m\ge1$ 个顶点的有限简单图。若其每个团的大小都不超过实数 $r\ge1$，则

$$
2|E(G)|\le\left(1-\frac1r\right)m^2.
$$

**证明。** 令 $T$ 为 $G$ 的补图，记 $T$ 的顶点度数为 $\delta_1,\ldots,\delta_m$。均匀随机排列全部顶点，并选取早于自身全部 $T$ 邻居的顶点。若两个所选顶点在 $T$ 中相邻，则它们各自都须早于对方，矛盾；故所选集合在 $T$ 中独立，在 $G$ 中为团，其大小至多 $r$。

顶点 $i$ 被选中的概率为 $1/(\delta_i+1)$。取期望，再用 Cauchy–Schwarz 不等式，得到

$$
r\ge\sum_{i=1}^m\frac1{\delta_i+1}
\ge\frac{m^2}{\sum_{i=1}^m(\delta_i+1)}
=\frac{m^2}{m+2|E(T)|}.
$$

因为 $m+2|E(T)|=m^2-2|E(G)|>0$，整理即得结论。∎

此为 Turán 团数上界所对应的边数不等式；上面的随机排列证明不需要精确 Turán 数或等号情形的分类。

<a id="core-lemma-3"></a>
## 引理3：Gram矩阵与单交图界

设 $k\ge2$，且 $H=(V,E)$ 为实际边数 $m\ge1$、顶点数 $v$ 的有限简单 $k$ 元超图。则 $S(H)$ 的每个团大小至多 $v$，且

$$
\gamma(H)\le\left(1-\frac1v\right)m^2.\tag{3}
$$

若此外 $m\le M$ 且 $H$ 是引理2中的最小顶点反例，则

$$
\gamma(H)\le g_k(M).\tag{4}
$$

**证明。** 取 $S(H)$ 中任一 $q$ 点团，即取 $q$ 条两两恰交一点的不同原边。令 $A$ 为这些边的 $0/1$ 关联矩阵，行对应所选边，列对应 $V$。每行恰有 $k$ 个 $1$，不同两行的内积为 $1$，故

$$
AA^{\mathsf T}=(k-1)I_q+J_q,
$$

其中 $I_q$ 为单位矩阵，$J_q$ 为全一矩阵。对非零实向量 $z\in\mathbb R^q$，由于 $k\ge2$，有

$$
z^{\mathsf T}AA^{\mathsf T}z
=(k-1)\sum_{i=1}^qz_i^2+\left(\sum_{i=1}^qz_i\right)^2>0.
$$

因此 $AA^{\mathsf T}$ 为正定矩阵，$q=\operatorname{rank}(AA^{\mathsf T})\le\operatorname{rank}(A)\le v$。将引理3.1用于 $G=S(H)$、$r=v$，并注意 $2|E(S(H))|=\gamma(H)$，便得式(3)。

若 $H$ 是引理2的反例，则 $v\le v_k(M)$。因 $m\le M$，式(3)给出

$$
\gamma(H)\le\left(1-\frac1{v_k(M)}\right)M^2.
$$

另一方面，按有向不同边对计数，总有 $\gamma(H)\le m(m-1)\le M(M-1)$。对这两个上界取最小值即为式(4)。∎

<a id="core-theorem-a"></a>
## 定理A：无附加结构假设的充分判据

设整数 $k\ge2$、$M\ge1$。若存在实数 $p\in(0,1]$ 满足

$$
1-a_k(p)^{M/2^{k-1}}+
\frac{g_k(M)}{4^{k-1}}J_k(p)<1,\tag{A}
$$

则任意边数至多 $M$ 的有限简单 $k$ 元超图均具有 Property B。因此 $m(k)\ge M+1$。

**证明。** 没有边的超图具有 Property B。若结论不成立，由引理2可取顶点数最少的反例 $H$，其实际边数满足 $1\le m\le M$。将引理1用于这个 $H$。因为 $0<a_k(p)\le1$ 且 $m\le M$，有

$$
1-a_k(p)^{m/2^{k-1}}\le1-a_k(p)^{M/2^{k-1}}.
$$

再由引理3的式(4)、$J_k(p)\ge0$ 以及假设(A)，实际失败概率满足

$$
\Pr(\mathcal F)
\le1-a_k(p)^{M/2^{k-1}}+
\frac{g_k(M)}{4^{k-1}}J_k(p)<1.
$$

所以补事件 $\mathcal F^{\mathrm c}$ 有正概率，存在一个随机结果使最终染色中没有单色边。其最终染色为 $H$ 的合法二染色，与 $H$ 为反例矛盾。因此所有边数至多 $M$ 的原始超图均具有 Property B。根据 $m(k)$ 的定义，$m(k)\ge M+1$。∎

## 参考文献

[RS2000] Jaikumar Radhakrishnan and Aravind Srinivasan. *Improved bounds and algorithms for hypergraph 2-coloring*. Random Structures & Algorithms **16**(1) (2000), 4–32. [DOI](https://doi.org/10.1002/%28SICI%291098-2418%28200001%2916%3A1%3C4%3A%3AAID-RSA2%3E3.0.CO%3B2-2)；[作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)；本地副本：`ref/radhakrishnan_srinivasan_2000_two_coloring.pdf`。本文的章节、命题编号及具体页码均按该作者稿标注。
