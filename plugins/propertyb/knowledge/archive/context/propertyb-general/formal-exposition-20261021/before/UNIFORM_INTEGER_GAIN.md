# 指定RS精确判据上的统一整数增益

2026-10-21。与 `CORE_THEOREM.md` 合成一条无额外结构前提的完整自然语言证明。正式审计及跨家族审阅见 `context/propertyb-general/round02/`；完整比较源为 `BASELINE_COMPARISON.md`。

## 定理B

对整数 $k\ge17$，令 $d=2^{k-1}$，

$$
a_k(p)=1-(1-p)^k,\quad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

并定义一个完全确定的整数

$$
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.\tag{1}
$$

则此最大值存在，且

$$
2^k\le B_{\rm RS}(k)<k2^k,\qquad
\boxed{m(k)\ge B_{\rm RS}(k)+2.}\tag{2}
$$

换言之，任意有限简单 $k$ 元超图若边数不超过 $B_{\rm RS}(k)+1$，必可二染。指定的旧RS精确判据仅直接给出 $m(k)\ge B_{\rm RS}(k)+1$；本定理在整个 $k\ge17$ 范围将这个整数结论至少提高一。

## 证明一：旧判据强迫的参数控制

设整数 $M\ge2^k$ 被 (1) 接受，取其实际见证 $p$，缩写 $a=a_k(p)$、$J=J_k(p)$、$\kappa=M/d\ge2$。有

$$
\frac{\kappa^2}2J\le\frac{M(M-1)}{d^2}J<a^\kappa.\tag{3}
$$

因 $p=0$ 时两边同为零，严格性强迫 $p>0$。若 $p\le1/k^2$，则Bernoulli不等式给 $J\ge p/2$、$a\le kp$，从而

$$
\frac{\kappa^2}{4k}<(kp)^{\kappa-1}\le kp\le\frac1k\le\frac{\kappa^2}{4k},
$$

矛盾。因此 $p>1/k^2$。在 $[0,1/k^2]$ 上，被积函数至少 $1/2$，积分先给出下式的 $J$ 下界；再代入 (3)，得到 $a^\kappa$ 下界：

$$
J\ge\frac1{2k^2},\qquad
a^\kappa>\frac{\kappa^2}{4k^2}\ge\frac1{k^2}.
$$

由于 $a\le1$，得到

$$
\kappa<2k,\qquad \kappa\log a>-2\log k.\tag{4}
$$

## 证明二：整个参数范围内的严格余量

对所有实数 $x\ge17$，

$$2^{x/2}>8x+4x\log x.\tag{5}$$

在 $x=17$，由 $e^3>\sum_{j=0}^5 3^j/j!=92/5>17$ 得 $\log17<3$；又 $\sqrt2>7/5$，所以左边大于 $256\cdot7/5>340$，右边小于 $340$。而比值 $2^{x/2}/[x(2+\log x)]$ 的对数导数为

$$
\frac{\log2}2-\frac1x-\frac1{x(2+\log x)}
>\frac14-\frac2x\ge\frac14-\frac2{17}>0.
$$

此处 $\log2>1/2$ 来自积分 $\int_1^2dt/t>1/2$。于是 (5) 在整个半轴成立。

令 $N=M+1$、$v=v_k(N)$、$g=g_k(N)$，其中 $v_k,g_k$ 取定理A的定义。这里 $v\ge k\ge17$，且

$$
v\le1+k\sqrt N\le2k\sqrt M.
$$

最后一个不等式由 $N\le2M$、$\sqrt2<3/2$ 及 $1\le(k/2)\sqrt M$ 得出。由 $M\ge2^k$ 与 (5)，

$$
\frac1v\ge\frac1{2k\sqrt M}>\frac{4+2\log k}{M}.\tag{6}
$$

## 证明三：坏边对削减吸收新增的一条边

令 $R=N^2(1-1/v)/[M(M-1)]>0$。初等对数不等式给

$$
\begin{aligned}
\log R
&\le\frac2M-\frac1v+\frac1{M-1}\\
&\le\frac4M-\frac1v\\
&<-\frac{2\log k}{M}\\
&<\frac{\kappa\log a}{M}=\frac{\log a}{d}.
\end{aligned}
$$

依次使用 $1/(M-1)\le2/M$、(6)及(4)。因此

$$
\frac{g_k(N)}{M(M-1)}\le R<a^{1/d}.
$$

结合旧判据，得到

$$
\frac{g_k(N)}{d^2}J<a^{(M+1)/d}.
$$

这正是定理A在预算 $N=M+1$ 的严格充分条件。故每个被旧判据接受且至少 $2^k$ 的整数预算，都可增加一条边。

## 证明四：最大预算存在，结论无优化器假设

取 $M_0=2^k$、$p=1/k$。由

$$
(1-1/k)^{-k}=\left(1+\frac1{k-1}\right)^k\ge1+\frac{k}{k-1}>2
$$

得 $a_k(1/k)>1/2$。而 $J_k(1/k)\le1/k$，故

$$
\frac{M_0(M_0-1)}{d^2}J_k(1/k)<\frac4k<\frac14<a_k(1/k)^2.
$$

所以 (1) 的集合非空并含 $2^k$。其所有至少 $2^k$ 的元素由 (4) 满足 $M<k2^k$；更小的元素本已在有限区间内。最大整数 $B_{\rm RS}(k)$ 因而存在，并有一个实际的 $p$ 见证，不需要连续最优值可达的额外论证。

将证明三用于 $M=B_{\rm RS}(k)$，定理A即给任意至多 $B_{\rm RS}(k)+1$ 边原始超图的合法染色，推出 (2)。∎

## 精确性和比较范围

函数定义不依赖浮点搜索。积分是显式有理系数多项式

$$
J_k(p)=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}j\frac{p^{2j+1}}{2j+1}.
$$

令 $Q=M(M-1)J_k(p)/d^2\ge0$。判据等价于 $Q^d<a_k(p)^M$，是 $p\in[0,1]$ 上有理多项式的严格正性问题；候选 $M$ 仅在已证有限区间内。统一证明无需逐个求解这些问题。

本定理精确比较的是 (1) 指定的RS–FKG–精确积分整数界。其他参考函数与指定离散位置／度共度测试方案的比较由 `BASELINE_COMPARISON.md` 完整给出，范围按其各定理陈述。
