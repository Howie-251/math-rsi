# 一般下界的参考包络与有限测试方案比较

## 1. 参考界的组成与主要结论

本节比较明确给定的普遍数值函数及一个有限必要数据测试方案。全部超图结论仍指任意有限简单 $k$ 元超图；固定顶点数结论保持其原量词，不单独转写成同值的 $m(k)$ 下界。

令 $d=2^{k-1}$、$r=k-1$，并记

$$
\kappa=\frac Md,\qquad
a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^r\,dy,\qquad
\gamma_0(M)=M(M-1).
$$

沿用前文的整数预算

$$
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
1-a_k(p)^{M/d}+\frac{\gamma_0(M)}{d^2}J_k(p)<1\right\}.
\tag{B1}
$$

这是RS原始FKG端项与精确积分、再以有向单交对上界 $M(M-1)$ 代入的指定判据。已证对 $k\ge17$，

$$2^k\le B_{\rm RS}(k)<k2^k.$$

为固定比较对象，再定义：

* $B_{\rm lin}(k)$：存在 $p\in[0,1]$ 使 $\kappa(1-p)^k+\kappa^2p<1$ 的最大整数预算。这是RS及CK保留的线性端项判据。
* $B_{\rm cont}(k)$：以 $\gamma=\gamma_0(M)$ 代入下面Grill连续式后，使其严格小于1的最大整数预算。
* $B_{\rm pair}(k)$：满足 $\gamma_0(M)\beta_k<1$ 的最大整数预算，其中
  $$\beta_k=\int_0^1[x(1-x)]^{k-1}dx=\frac{((k-1)!)^2}{(2k-1)!}.$$
  它保留纯有向单交对的准确排列概率。
* $L_{\rm GR}(k)$：Goldberg–Russell型的Schönheim覆盖与平衡染色min–max下界，准确公式在下一节给出。

本节的**参考包络**明确取为

$$
\boxed{L_{\rm ref}(k)=\max\bigl\{
B_{\rm RS}(k)+1,\ B_{\rm lin}(k)+1,\ B_{\rm cont}(k)+1,
B_{\rm pair}(k)+1,\ L_{\rm GR}(k)\bigr\}.}
\tag{B2}
$$

这里每个 $B$ 是可染边数预算，下界要再加一；$L_{\rm GR}$ 本身已经是 $m(k)$ 的下界。所有最大值的存在性将在比较中一并得到。

**比较定理。** 对每个整数 $k\ge32$，

$$L_{\rm GR}(k)\le2^k,
\qquad L_{\rm ref}(k)=B_{\rm RS}(k)+1.\tag{B3}$$

因此，前文增长增益定理在此范围给出

$$
m(k)\ge L_{\rm ref}(k)+
\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
\tag{B4}
$$

Grill已发表的锁点数值定理适用于 $k=5,\ldots,9$，不提供本节 $k\ge32$ 的另一条完整数值函数。其固定 $v=2k+1$ 的Catalan结论也不能单独加入全超图包络作为同值下界。RS/CK的渐近常数结论，对每个固定 $c<1/\sqrt2$ 在充分大 $k$ 成立；本节用准确有限判据比较，不把未知起点或端点常数冒用为逐 $k$ 数值。

第5–9节另证明：对 $k\ge256$，一个明确列出测试项目的Grill零锁必要数据松弛方案，不能接受任何 $M>B_{\rm RS}(k)$。这是对该有限测试方案的补充比较，不将全部可能的真实结构推理或多锁扩展混入(B2)。

## 2. Goldberg–Russell型一般公式及其全域量词

对整数 $v\ge2k-1$，置

$$
S_k(v)=\left\lceil\frac vk\left\lceil\frac{v-1}{k-1}\right\rceil\right\rceil,
\qquad
R_k(v)=\frac{\binom vk}
{\binom{\lfloor v/2\rfloor}k+\binom{\lceil v/2\rceil}k}.
$$

则

$$
L_{\rm GR}(k)=\min_{v\in\mathbb Z,\ v\ge2k-1}
\max\{S_k(v),\lceil R_k(v)\rceil\},
\qquad m(k)\ge L_{\rm GR}(k).\tag{B5}
$$

证明其量词如下。若存在非B超图，在边数不增加的反例中取顶点数最少者。前文的合并点归约保证它覆盖每个点对。因此每点度至少 $\lceil(v-1)/(k-1)\rceil$；按关联总数计数，边数 $m$ 至少为 $S_k(v)$。

在同一 $v$ 点超图上，均匀抽取大小为 $\lfloor v/2\rfloor$ 的红色类。每条指定边单色的概率是 $1/R_k(v)$。非B意味着每份这样的染色都有单色边，所以期望单色边数 $m/R_k(v)\ge1$，即 $m\ge\lceil R_k(v)\rceil$。此处不能在 $R_k(v)$ 为整数时多加一。两种必要条件作用于同一个实际反例，随后取 $v$ 的最小值即得(B5)。$v\le2k-2$ 时可将两色类均取少于 $k$ 点，直接可染，故无遗漏。∎

## 3. 对全部 $k\ge32$ 的解析比较

取

$$q=2^{\lfloor k/2\rfloor},\qquad v=(k-1)q.$$

有 $\lceil(v-1)/(k-1)\rceil=q$，从而

$$S_k(v)=\left\lceil\frac{(k-1)q^2}k\right\rceil\le q^2\le2^k.\tag{B6}$$

还要上界同一个 $v$ 的 $R_k(v)$。对所有实数 $x\ge32$，函数 $2^{x/2}/x$ 严格递增，因为其对数导数为 $\log2/2-1/x>0$，且在32有 $2^{16}>16\cdot32$。所以

$$q\ge2^{k/2-1}>8k,\qquad v>8k(k-1)\ge4k^2.$$

令 $a=\lfloor v/2\rfloor$、$b=\lceil v/2\rceil$。对 $t\in\{a,b\}$ 和 $j=0,\ldots,k-1$，

$$\frac{t-j}{v-j}\ge\frac12\left(1-\frac{2k}v\right).$$

因此单色概率 $P=1/R_k(v)$ 满足

$$
P=\frac{\binom ak+\binom bk}{\binom vk}
\ge2^{1-k}\left(1-\frac{2k}v\right)^k
\ge2^{1-k}\left(1-\frac{2k^2}v\right)>2^{-k}.
$$

所以 $R_k(v)<2^k$，且 $\lceil R_k(v)\rceil\le2^k$。与(B6)合用得到(B3)的第一式。这是选择一个 $v$ 上界外层最小值，不是断言所有 $v$ 的max项都不超过 $2^k$。∎

## 4. 其余参考函数被指定RS精确判据覆盖

记Grill连续式为

$$
C_k(M,\gamma)=\int_0^1\min\{Mkx^r,Mk(1-x)^r,\gamma[x(1-x)]^r\}\,dx.
\tag{B7}
$$

对 $x\in[0,1/2]$，第二端点项不小于第一项；坏对项与第一项的比值 $\gamma(1-x)^r/(Mk)$ 随 $x$ 非增。因此两项至多交换一次，允许交换点在端点。令交换位置为 $x=(1-p)/2$ 并积分，得到准确恒等式

$$
C_k(M,\gamma)=\min_{0\le p\le1}
\left\{\kappa(1-p)^k+\frac\gamma{d^2}J_k(p)\right\}.\tag{B8}
$$

对 $\kappa\ge1$、$0\le z\le1$，Bernoulli凸性不等式给

$$1-(1-z)^\kappa\le\kappa z.$$

代入 $z=(1-p)^k$，可见(B1)的失败上界不大于同一 $p$ 的(B8)表达式（取 $\gamma=\gamma_0$）；又 $J_k(p)\le p$ 且 $\gamma_0/d^2\le\kappa^2$，故(B1)也不大于线性判据。于是任何 $M\ge d$ 被连续或线性判据接受，都会被(B1)接受。较小的 $M<d$ 已低于 $B_{\rm RS}\ge2^k$。这证明

$$B_{\rm cont}(k),\ B_{\rm lin}(k)\le B_{\rm RS}(k)\qquad(k\ge32).$$

连续min逐点不大于坏对项，故 $C_k(M,\gamma_0)\le\gamma_0\beta_k$，进而 $B_{\rm pair}\le B_{\rm cont}$。这些集合非空，例如 $M=1$ 时坏对项为零且可取 $p=1$；又均受有限的 $B_{\rm RS}$ 控制，最大值存在。结合第3节及 $B_{\rm RS}\ge2^k$，得到(B3)第二式，继而由增长增益定理得到(B4)。∎

## 5. 补充定理：明确的零锁有限测试方案

以下只讨论一个完全指定的必要数据松弛。对固定 $k,M$，它遍历整数 $v\ge2k-1$ 及下列有限数据；$S_k(v)\le M$ 已使 $v$ 的范围有限。

选一个标号中心0，给出整数度 $d_0,\ldots,d_{v-1}$、中心共度 $c_i$（$i>0$）和最大共度参数 $r_i$。只保留下述测试均通过的数据：

1. $1\le d_i\le M-1$，$\sum_i d_i=kM$；所有度至少为 $\ell=\lceil(v-1)/(k-1)\rceil$，并有 $S_k(v)\le M$。
2. $1\le c_i\le\min(d_0,d_i)$，$\sum_{i>0}c_i=(k-1)d_0$；$r_0=\max_{i>0}c_i\le d_0$，对 $i>0$ 有 $c_i\le r_i\le d_i$，并有 $r_i\le\max_{j\ne i}d_j$。
3. 对每个 $i>0$，令 $\theta_i=(k-1)d_i-c_i$，要求
   $$v-2\le\theta_i\le\sum_{j>0,\,j\ne i}\min(r_i,r_j),\qquad \sum_{i>0}\theta_i\text{为偶数}.$$
4. 覆盖点对的标量条件 $v(v-1)\le k(k-1)M$。

这些是标量与逐行容量测试，**没有**要求存在一张同时满足全部行和的对称共度矩阵，也没有要求存在实际边族。实际非B输入不能有度为 $M$ 的点，否则将该点染红、其余点染蓝即proper；所以第1项未丢掉非B对象。下文仅在 $r_i=c_i$（$i>0$）的子域构造不通过数据，不把这项等式作为一般原H的必要条件。

对这样的数据，记 $R=\max_i r_i$，使用Grill列出的两条上界

$$
\Gamma_1=M(M-1)-R(R-1),\qquad
\Gamma_2=\sum_i\bigl[d_i(d_i-1)-r_i(r_i-1)\bigr],\qquad
\Gamma=\min(\Gamma_1,\Gamma_2).
$$

测试方案只有当每份保留数据都满足以下至少一项时，才接受固定 $M$：平衡染色联合上界严格小于1，或下列零锁离散式严格小于1：

$$
\begin{aligned}
D_k(v,M,\gamma)=\frac1v\sum_{h=1}^v\min\biggl\{
&Mk\frac{\binom{h-1}r}{\binom{v-1}r},\quad
Mk\frac{\binom{v-h}r}{\binom{v-1}r},\\
&\gamma\frac{\binom{h-1}r\binom{v-h}r}
{\binom{v-1}r\binom{v-k}r}\biggr\}.
\end{aligned}\tag{B9}
$$

不可能的二项式取零。该方案只比较(B9)、两条指定 $\gamma$ 公式及上述数据测试；不包含实际边族可实现性、edge-critical结构、完整真实共度或任意多锁推理。

**补充定理。** 对每个整数 $k\ge256$、每个整数 $M>B_{\rm RS}(k)$，存在通过全部上述测试的数据，其平衡联合上界大于1，且 $D_k(v,M,\Gamma)>1$。因此该明确的“全部松弛数据均须通过”方案不能接受任何这样的固定 $M$。

## 6. 通过全部数据测试的非全含中心构造

设 $t=\sqrt M$，并取

$$
v=\lfloor(k-2)t\rfloor,\qquad n=v-1,\qquad
T=\left\lfloor\frac M{k^{16}}\right\rfloor,\qquad D=M-T.
$$

先记一个全范围余量：对所有实数 $x\ge256$，

$$2^{x/2}>300x^{10}.\tag{B10}$$

因为 $\log(2^{x/2}/x^{10})$ 的导数大于 $1/4-10/256>0$，而在256有 $2^{128}>300\cdot2^{80}$。由 $M>B_{\rm RS}\ge2^k$ 得 $t>300k^{10}$；特别 $T\ge1$ 且 $D<M$。

将 $(k-1)D$ 均分为 $n$ 个尽量相等的整数 $c_i$，将 $kT$ 独立均分为 $n$ 个尽量相等的整数 $b_i$。取

$$d_0=D,\qquad d_i=c_i+b_i\ (i>0),\qquad r_i=c_i\ (i>0),\qquad r_0=R=\max_i c_i.$$

两个均分的向上取整重数分别选择以保持各自精确总和，不要求二者的余数位置相同。总度为

$$D+\sum_{i>0}(c_i+b_i)=D+(k-1)D+kT=kM.$$

以下取整范围用于核全部测试：

$$v\ge\frac k2t,\qquad t\le c_i\le2t,\qquad 0\le b_i\le t/2.\tag{B11}$$

第一式由 $v\ge(k-2)t-1$ 得到。令 $\varepsilon=k^{-16}$。$c_i$的均值大于 $[(k-1)/(k-2)](1-\varepsilon)t$，至少超过 $t$ 达 $t/[2(k-2)]>1$，所以向下取整仍不小于 $t$。另一方面 $n\ge(k-3)t$，故 $c_i\le[(k-1)/(k-3)]t+1\le2t$；同理

$$b_i\le\frac{k}{k-3}\varepsilon t+1\le t/2.$$

这些不等式在 $k\ge256$、$t>300k^{10}$ 下均有严格余量。于是所有非中心度不超过 $5t/2<M$；中心度 $D\ge M/2\ge t$，且 $D<M$。又 $c_i\le2t\le D$，所以中心共度的范围测试通过。

由于 $(v-1)/(k-1)<t-t/(k-1)<t-1$，所有度均不小于 $\ell$；总度等式给 $v\ell\le kM$，故 $S_k(v)\le M$。粗点对覆盖式也由 $v\le(k-2)t$ 直接得到。

普通点的目标共度行和为

$$\theta_i=(k-2)c_i+(k-1)b_i.$$

其下界 $\theta_i\ge(k-2)t\ge v>v-2$。其上界 $\theta_i<3kt$，而

$$\sum_{j>0,\,j\ne i}\min(c_i,c_j)\ge(v-2)t\ge3kt.$$

所以逐行上限也通过。总行和

$$\sum_i\theta_i=(k-1)(k-2)D+k(k-1)T$$

为偶数，因两个系数都是相邻整数之积。普通点的 $r_i$ 在已指定的中心共度 $c_i$ 中达到；中心参数为 $r_0=\max_i c_i$。

令 $P$ 是一条指定边在均匀平衡染色下单色的概率。第3节的乘积下界同样给

$$MP\ge\kappa\left(1-\frac{2k}v\right)^k
\ge\kappa\left(1-\frac{2k^2}v\right)>1,\tag{B12}$$

因为 $\kappa=M/d\ge2$、$v>4k^2$。因此平衡染色联合界不排除这份数据。这是充分判据的数值不通过，不是实际染色失败概率的下界。

记

$$\Lambda=D(D-1)-R(R-1).$$

两条旧公式满足 $\Gamma_1\ge\Lambda$，而

$$\Gamma_2=\Lambda+\sum_{i>0}\bigl[d_i(d_i-1)-c_i(c_i-1)\bigr]\ge\Lambda.$$

因此 $\Gamma\ge\Lambda$。还由 $R\le2t$ 得

$$
\gamma_0-\Lambda\le2MT+4M,\qquad
\Lambda\ge M^2(1-2k^{-16})-5M\ge M^2/2.
\tag{B13}
$$

由于(B9)关于 $\gamma$ 非减，下文只需证明使用更小 $\Lambda$ 时仍大于1。

## 7. 实际离散式向连续min的统一下比较

对任意 $\gamma\ge0$，令

$$
f(x)=\min\{Mkx^r,Mk(1-x)^r,\gamma[x(1-x)]^r\},\qquad
C=\int_0^1f(x)dx,\qquad L=f(1/2).
$$

$f$关于 $1/2$ 对称，在 $[0,1/2]$ 非减，所以总变差至多 $2L$。置

$$N=v-2k+3,\qquad s=N/v.$$

在(B9)中只保留 $h=k-1,\ldots,v-k+2$，令 $j=h-k+1$，便有 $j=0,\ldots,N$。两个分子降阶乘的最小因子分别为 $j$、$N-j$；分母降阶乘均至多 $v^r$。端项因此有 $s^r$ 因子、坏对项有 $s^{2r}$ 因子；再用 $s^r\ge s^{2r}$，每个保留位置的最小项至少为 $s^{2r}f(j/N)/v$。

总变差的黎曼和估计给

$$\sum_{j=0}^N f(j/N)\ge NC-2L.$$

于是得到关于实际离散式的代数下界

$$\boxed{D_k(v,M,\gamma)\ge s^{2k-1}C-\frac{2s^{2k-2}}vL.}\tag{B14}$$

它没有将离散式换成渐近连续近似，且完整保留外部 $1/v$ 与位置偏移。

## 8. 有限 $\kappa$ 区间：FKG间隙覆盖位置损失

先设 $2\le\kappa\le3k$，取 $\gamma=\Lambda$，$q=\Lambda/d^2$。由(B8)，

$$C=\min_{0\le p\le1}\{\kappa(1-p)^k+qJ_k(p)\}.$$

括号内的导数为 $(1-p)^r[q(1+p)^r-\kappa k]$。若 $q\ge\kappa k$，最小点是 $p_*=0$，$C=\kappa$。否则，由 $q\ge\kappa^2/2$ 得 $\kappa k/q\le k<2^r$，所以唯一最小点在内部且

$$p_*=(\kappa k/q)^{1/r}-1\le k^{1/(k-1)}-1\le\frac{2\log k}k<\frac12.$$

最后一个非严格比较可由 $e^u-1\le u/(1-u)$ 及 $k/2\ge1+\log k$ 得到。令 $z=(1-p_*)^k$；由 $\log(1-p)\ge-2p$，

$$z\ge k^{-4}.$$

对 $\kappa\ge2$、$0\le z\le1$，

$$h_\kappa(z)=\kappa z-1+(1-z)^\kappa\ge z^2.\tag{B15}$$

$\kappa=2$时等号成立；固定 $z$，令 $u=1-z$，则关于 $\kappa$ 的导数 $z+u^\kappa\log u\ge z+u\log u\ge0$。端点由连续性处理。

由 $M>B_{\rm RS}$ 的定义，对同一个 $p_*$，旧RS失败上界 $F_0(M,p_*)\ge1$。因此

$$
\begin{aligned}
C&=F_0(M,p_*)+h_\kappa(z)
-\frac{\gamma_0-\Lambda}{d^2}J_k(p_*)\\
&\ge1+k^{-8}-18k^{-14}-\frac{36k^2}M.
\end{aligned}\tag{B16}
$$

这里用(B13)、$T/M\le k^{-16}$、$J_k\le1$和 $\kappa\le3k$。若 $p_*=0$，$F_0(M,0)=1$、$h_\kappa(1)=\kappa-1\ge1$，故同一较弱估计仍成立。

又 $C\le\kappa\le3k$、$L\le q\le\kappa^2\le9k^2$。由 $1-s^{2k-1}\le(2k-1)(2k-3)/v$，(B14)给

$$D_k(v,M,\Lambda)\ge C-\frac{30k^3}v\ge C-\frac{60k^2}t.$$

结合(B16)及 $M>t$，

$$
D_k(v,M,\Lambda)>1+k^{-8}-18k^{-14}-\frac{96k^2}t>1.
\tag{B17}
$$

最后由(B10)，$96k^2/t<(96/300)k^{-8}$；而 $18k^{-14}=(18/k^6)k^{-8}<(1/3)k^{-8}$，两个损失的和严格小于 $k^{-8}$。

## 9. 全部更大 $M$：不假设可接受预算下闭

现在设 $\kappa\ge3k$。由(B13)，$q\ge\kappa^2/2\ge\kappa k$，所以 $C=\kappa$、$L=\kappa k$。直接由(B14)，

$$
\begin{aligned}
D_k(v,M,\Lambda)
&\ge\kappa\left[1-\frac{(2k-1)(2k-3)+2k}v\right]\\
&\ge\kappa\left[1-\frac{4k^2+2k}v\right]
\ge\kappa/2>1.
\end{aligned}
$$

倒数第二步使用 $v\ge(k/2)t$ 与 $t>300k^{10}$。两种 $\kappa$ 区间覆盖每个整数 $M>B_{\rm RS}$；小区间内 $F_0(M,p)\ge1$ 直接来自(B1)的最大值定义，而不是仅在 $B_{\rm RS}+1$ 失败后假设所有更大预算也失败。

第6节数据通过全部明确测试，平衡界由(B12)不通过，且 $\Gamma\ge\Lambda$ 使真正使用两条旧公式的(B9)也大于1，补充定理得证。∎

## 10. 原始来源与自含证明的边界

RS–FKG及有向坏对积分来自 [Radhakrishnan–Srinivasan作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)第4–7页和附录A.1。线性判据及渐近归一化见 [Cherkashin–Kozik](https://doi.org/10.1002/rsa.20556)。准确排列概率也见 [Pluhár, Greedy colorings of uniform hypergraphs](https://doi.org/10.1002/rsa.20267)。

(B5)的可读原始陈述见 [Grill–Linzmayer2024式(3)–(5)](https://arxiv.org/html/2403.05674v3)，以及[Aglave等2020](https://arxiv.org/abs/1602.00218)刊页83的Lemma4.3；两者将该方法归于Goldberg–Russell。(B7)、(B9)及两条度/最大共度公式使用同一Grill原文。Goldberg–Russell作者稿的实际正文以四元情形为主，并附局部错误警示，故本节一般公式不以其未核的局部分类为进口；所需全域归约与计算已在正文自含证明。

前文公共点二分属于经典线性交族／Deza型团界。Deza1974的出版元数据及Erdős1975的历史记录可定位其归属；本节不把未读的Deza完整定理作为可信进口。这里所需的恰单点交特例已在增长增益章节完整证明。

原始资料的实际核对及本轮有界检索范围见[最终文献核对记录](../../context/propertyb-general/round02/final-literature/REPORT.md)。参考包络采用(B2)的明确组成；固定小 $k$ 数表与固定 $v$ 特例仍按其原量词使用。
