# 指定RS精确判据上的统一整数增益

本文的超图均为有限简单超图；Property B 指存在使每条边同时含两色的顶点二染色。对整数 $k\ge2$，以 $m(k)$ 表示不具有 Property B 的 $k$ 元超图的最少边数。以下 $\log$ 均为自然对数，$v_k$、$g_k$ 采用 [定义2](CORE_THEOREM.md#core-definition-2) 的记号。

## 定义B.1：精确接受集合与预算

给定整数 $k\ge12$，令 $d=2^{k-1}$，并对 $p\in[0,1]$ 定义

$$
a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy.
$$

定义整数接受集合

$$
\mathcal A_k=\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
$$

<a id="gain-definition-brs"></a>
此判据由 [引理1](CORE_THEOREM.md#core-lemma-1) 的实际重染失败上界和有向单交对数 $\gamma(H)\le M(M-1)$ 得到。其概率分析来自 [Radhakrishnan–Srinivasan 作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)：第4页第2节给出延迟重染算法，第6页给出 Claim 2.4，第7页其证明中的未编号式给出所用精确积分，第26–27页附录A的 Claim A.1 给出正关联与 Jensen 估计。本文组合这些估计、保留精确积分并采用 $M(M-1)$ 的有向对计数，定义 $\mathcal A_k$ 及下述预算；原文不逐字包含这一预算量。

引理B.4将证明 $\mathcal A_k$ 非空且有限，因此下式良定：

$$
B_{\rm RS}(k)=\max\mathcal A_k
=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.\tag{1}
$$

## 引理B.1：接受参数的控制

<a id="gain-lemma-b1"></a>
设 $k\ge12$ 为整数，$M\in\mathcal A_k$ 且 $M\ge2^k$。设 $p\in[0,1]$ 是接受不等式的见证，记 $a=a_k(p)$、$J=J_k(p)$、$\kappa=M/d$。则

$$
p>\frac1{k^2},\qquad J\ge\frac1{2k^2},\qquad
\kappa<2k,\qquad \kappa\log a>-2\log k.
$$

**证明。** 因为 $M\ge2^k$，所以 $\kappa\ge2$、$M\ge2$。接受不等式给出

$$
\frac{\kappa^2}2J\le\frac{M(M-1)}{d^2}J<a^\kappa.\tag{3}
$$

当 $p=0$ 时，接受不等式两边同为零，因此 $p>0$，从而 $a>0$。若 $p\le1/k^2$，则对 $0\le y\le p$，Bernoulli 不等式给出

$$
(1-y^2)^{k-1}\ge1-(k-1)y^2\ge1-\frac{k-1}{k^4}\ge\frac12.
$$

因此 $J\ge p/2$。又由 Bernoulli 不等式有 $a\le kp$，故 (3) 蕴含

$$
\frac{\kappa^2}{4k}<(kp)^{\kappa-1}\le kp\le\frac1k\le\frac{\kappa^2}{4k},
$$

矛盾。这里使用了 $0<kp\le1/k\le1$ 及 $\kappa\ge2$。所以 $p>1/k^2$。在区间 $[0,1/k^2]$ 上使用同一被积函数下界，得到

$$
J\ge\frac1{2k^2},\qquad
a^\kappa>\frac{\kappa^2}{4k^2}\ge\frac1{k^2}.
$$

由于 $a\le1$，后一严格不等式一方面给出 $\kappa^2/(4k^2)<1$，另一方面可以取对数。因此

$$
\kappa<2k,\qquad \kappa\log a>-2\log k.\tag{4}
$$

∎

## 引理B.2：统一增长比较

<a id="gain-lemma-b2"></a>
对所有实数 $x\ge17$，有

$$
2^{x/2}>8x+4x\log x.\tag{5}
$$

此外，若 $k\ge17$、$M\ge2^k$ 均为整数，$N=M+1$，$v=v_k(N)$，则 $v\ge k$，并且

$$
\frac1v\ge\frac1{2k\sqrt M}>\frac{4+2\log k}{M}.\tag{6}
$$

**证明。** 先验证 (5) 的起点。由

$$
e^3>\sum_{j=0}^5\frac{3^j}{j!}=\frac{92}5>17
$$

得到 $\log17<3$。又 $\sqrt2>7/5$，故在 $x=17$ 时，(5) 左边大于 $256\cdot7/5>340$，右边小于 $340$。由

$$
\log2=\int_1^2\frac{dt}{t}>\frac12
$$

可得比值 $2^{x/2}/[x(2+\log x)]$ 的对数导数满足

$$
\frac{\log2}2-\frac1x-\frac1{x(2+\log x)}
>\frac14-\frac2x\ge\frac14-\frac2{17}>0.
$$

所以 (5) 对全部 $x\ge17$ 成立。

根据 $v_k(N)$ 的定义，$N\ge1$ 蕴含 $v\ge k$，且

$$
v\le1+k\sqrt N\le2k\sqrt M.
$$

最后一个不等式使用 $N\le2M$、$\sqrt2<3/2$ 以及 $1\le(k/2)\sqrt M$。又由 $\sqrt M\ge2^{k/2}$ 和 (5) 得到 $\sqrt M>8k+4k\log k$；将其除以 $2kM$，即得 (6)。∎

## 引理B.3：接受预算的加一转换

<a id="gain-lemma-b3"></a>
设 $k\ge17$ 为整数，$M\in\mathcal A_k$ 且 $M\ge2^k$。则任意边数至多 $M+1$ 的有限简单 $k$ 元超图均具有 Property B。

**证明。** 取 $M$ 的一个接受见证 $p$，沿用引理B.1中的 $a,J,d,\kappa$。令 $N=M+1$、$v=v_k(N)$，并置

$$
R=\frac{N^2(1-1/v)}{M(M-1)}>0.
$$

由 $\log(1+t)\le t$、$\log(1-t)\le-t$ 的适用情形，结合引理B.2的 (6) 及引理B.1的 (4)，得到

$$
\begin{aligned}
\log R
&\le\frac2M-\frac1v+\frac1{M-1}\\
&\le\frac4M-\frac1v\\
&<-\frac{2\log k}{M}\\
&<\frac{\kappa\log a}{M}=\frac{\log a}{d}.
\end{aligned}
$$

第二步使用 $1/(M-1)\le2/M$。所有对数均有定义，因为 $M\ge2$、$v\ge k\ge17$、$a>0$。于是

$$
\frac{g_k(N)}{M(M-1)}\le R<a^{1/d}.
$$

将此式与 $M$ 的接受不等式相乘，得到

$$
\frac{g_k(N)}{d^2}J<a^{(M+1)/d}.
$$

引理B.1给出 $p>0$，所以该不等式满足定理A对参数的要求，并且正是定理A在预算 $N$ 的充分条件。因此任意至多 $M+1$ 边的原始超图均可二染。∎

## 引理B.4：接受集合的有限最大值

<a id="gain-lemma-b4"></a>
对每个整数 $k\ge12$，集合 $\mathcal A_k$ 非空且有限，含有 $2^k$，且其每个元素均小于 $k2^k$。因此 $B_{\rm RS}(k)$ 存在，满足 $2^k\le B_{\rm RS}(k)<k2^k$，并且该最大整数本身有一个接受见证 $p\in(0,1]$。

**证明。** 取 $M_0=2^k$、$p=1/k$。由二项式展开的前三项，

$$
(1-1/k)^{-k}=\left(1+\frac1{k-1}\right)^k
\ge1+\frac{k}{k-1}+\frac{k}{2(k-1)}>\frac52,
$$

故 $(1-1/k)^k<2/5$，即 $a_k(1/k)>3/5$。又 $J_k(1/k)\le1/k$，因此

$$
\frac{M_0(M_0-1)}{d^2}J_k(1/k)
<\frac4k\le\frac13<\frac9{25}<a_k(1/k)^2.
$$

这证明 $M_0\in\mathcal A_k$。若 $M\in\mathcal A_k$ 且 $M\ge2^k$，引理B.1给出 $M/d<2k$，即 $M<k2^k$；若 $M<2^k$，同一上界也成立。因此 $\mathcal A_k$ 是非空有限整数集合，必有最大元。最大元属于 $\mathcal A_k$，故有实际见证；由引理B.1，该见证满足 $p>0$。这里无需假定任何连续参数优化问题的最优值可达。∎

## 定理B：统一加一增益

<a id="gain-theorem-b"></a>
对每个整数 $k\ge17$，式 (1) 定义的预算满足

$$
2^k\le B_{\rm RS}(k)<k2^k,\qquad
\boxed{m(k)\ge B_{\rm RS}(k)+2.}\tag{2}
$$

等价地，任意有限简单 $k$ 元超图，只要边数至多 $B_{\rm RS}(k)+1$，就具有 Property B；此结论不附加顶点数、点对覆盖、度数、共度或线性条件。

**证明。** 引理B.4保证 $B_{\rm RS}(k)\in\mathcal A_k$、$B_{\rm RS}(k)\ge2^k$，并给出 (2) 中预算的上下界。将引理B.3用于 $M=B_{\rm RS}(k)$，即得所有至多 $B_{\rm RS}(k)+1$ 边的原始超图均可二染。因此不可二染超图至少有 $B_{\rm RS}(k)+2$ 条边。∎

## 精确性与比较范围

积分是显式有理系数多项式：

$$
J_k(p)=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}j\frac{p^{2j+1}}{2j+1}.
$$

令 $Q=M(M-1)J_k(p)/d^2\ge0$。接受判据等价于 $Q^d<a_k(p)^M$，因而是 $p\in[0,1]$ 上有理多项式的严格正性问题。引理B.4将候选整数 $M$ 限制在有限区间内；定义及统一证明均不依赖浮点搜索。

对任何 $M\in\mathcal A_k$，CORE引理1配合 $\gamma(H)\le M(M-1)$，直接给出任意至多 $M$ 边的原始超图均可二染。因此式 (1) 的判据给出的整数下界为 $m(k)\ge B_{\rm RS}(k)+1$，定理B将它在整个 $k\ge17$ 范围至少提高一。其他参考函数及指定离散位置／度共度测试方案的比较见 [BASELINE_COMPARISON.md](BASELINE_COMPARISON.md)，其范围由各自定理陈述。
