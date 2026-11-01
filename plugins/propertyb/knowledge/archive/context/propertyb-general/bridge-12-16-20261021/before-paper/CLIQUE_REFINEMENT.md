# 单交团的公共点二分与增长的整数增益

以下采用 [CORE_THEOREM.md](CORE_THEOREM.md) 及 [UNIFORM_INTEGER_GAIN.md](UNIFORM_INTEGER_GAIN.md) 的记号。超图均为有限简单超图，$\log$ 为自然对数；$S(H)$ 的顶点为 $H$ 的边，两顶点相邻当且仅当相应两条原边恰交一点。

## 引理C.1：单交团的公共点二分

<a id="clique-lemma-c1"></a>
设整数 $k\ge2$、$q\ge1$、$v\ge k$，$V$ 为大小 $v$ 的有限集合，$e_1,\ldots,e_q\subseteq V$ 为互异的 $k$ 元集合，且对所有 $i\ne j$ 有 $|e_i\cap e_j|=1$。则：

- 若 $\bigcap_{i=1}^q e_i\ne\varnothing$，则 $q(k-1)+1\le v$；
- 若 $\bigcap_{i=1}^q e_i=\varnothing$，则 $q\le k^2-k+1$。

因此，对任意 $v$ 点简单 $k$ 元超图 $H$，有

$$
\omega(S(H))\le\max\left\{k^2-k+1,\left\lfloor\frac{v-1}{k-1}\right\rfloor\right\}.
$$

**证明。** 若存在公共点 $x$，两两单交保证 $e_i\setminus\{x\}$ 互不相交。因此所有边的并集恰有 $q(k-1)+1$ 个顶点，得到第一个结论；这也包括 $q=1$ 的情形。

若没有公共点，固定一条边 $e$。对每个 $x\in e$，存在族中一条不含 $x$ 的边 $f_x$。设 $d_x$ 是族中含 $x$ 的边数。这些边与 $f_x$ 的交点两两不同：若两条含 $x$ 的边在 $f_x$ 上有同一交点 $y$，则因 $x\notin f_x$ 而 $y\ne x$，这两条边便至少交于 $x,y$ 两点，违背假设。故 $d_x\le|f_x|=k$。每条不同于 $e$ 的边恰交 $e$ 一点，因而

$$
q-1=\sum_{x\in e}(d_x-1)\le k(k-1).
$$

这给出第二个结论。最后，将二分应用于 $S(H)$ 的任意非空团，即得所述团数上界；若 $H$ 无边，其单交图的团数为零，上界仍成立。∎

## 推论C.2：加强的无结构二染色判据

<a id="clique-corollary-c2"></a>
设整数 $k\ge2$、$N\ge1$。定义

$$
r_k(N)=\min\left\{v_k(N),\max\left\{k^2-k+1,\left\lfloor\frac{v_k(N)-1}{k-1}\right\rfloor\right\}\right\},
$$

以及

$$
g_k^*(N)=\min\left\{N(N-1),N^2\left(1-\frac1{r_k(N)}\right)\right\}.
$$

若存在 $p\in(0,1]$ 满足

$$
\frac{g_k^*(N)}{4^{k-1}}J_k(p)<a_k(p)^{N/2^{k-1}},
$$

则任意边数至多 $N$ 的有限简单 $k$ 元超图均具有 Property B。因此 $m(k)\ge N+1$。结论不附加顶点数、点对覆盖、度数、共度或线性假设。

**证明。** 因 $N\ge1$，有 $v_k(N)\ge k$；又 $k^2-k+1\ge k$，故 $r_k(N)\ge k\ge2$，定义中的分母均非零。

若结论不成立，按CORE引理2选取边数至多 $N$ 的最小顶点反例 $H$，记实际顶点数为 $v$、边数为 $m$。该引理给出 $v\le v_k(N)$。CORE引理3的关联矩阵论证给出 $\omega(S(H))\le v$，引理C.1则给出另一团数上界。结合这两个界及右端对 $v$ 的单调性，得到

$$
\omega(S(H))\le r_k(N).
$$

为将此界转为有向单交对数的上界，令 $T$ 为 $S(H)$ 的补图，顶点度数记为 $d_1,\ldots,d_m$。引理3.1中随机排列选独立集的论证及 Cauchy–Schwarz 不等式给出

$$
r_k(N)\ge\alpha(T)\ge\sum_{i=1}^m\frac1{d_i+1}
\ge\frac{m^2}{m+2|E(T)|}.
$$

由 $\gamma(H)=m(m-1)-2|E(T)|$，可得

$$
\gamma(H)\le\left(1-\frac1{r_k(N)}\right)m^2.
$$

再结合 $\gamma(H)\le m(m-1)$ 及 $m\le N$，得到 $\gamma(H)\le g_k^*(N)$。将这一上界代入CORE引理1，并使用 $0<a_k(p)\le1$、$m\le N$，实际失败概率至多为

$$
1-a_k(p)^{N/2^{k-1}}+\frac{g_k^*(N)}{4^{k-1}}J_k(p)<1.
$$

于是存在合法二染色，与 $H$ 是反例矛盾。∎

## 定理C：增长的整数增益

<a id="clique-theorem-c"></a>
设整数 $k\ge17$，并以定义B.1定义 $B_{\rm RS}(k)$。置

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

则 $\Delta(k)\ge1$，且任意边数至多 $B_{\rm RS}(k)+\Delta(k)$ 的有限简单 $k$ 元超图均具有 Property B。因此

$$
\boxed{m(k)\ge B_{\rm RS}(k)+1+
\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor}
\qquad(k\ge17).
$$

**证明。** 先证明对任意整数 $M\in\mathcal A_k$、$M\ge2^k$，都可在同一个接受参数下增加

$$
s=\left\lfloor\frac{\sqrt M}{8(1+\log k)}\right\rfloor
$$

条边。取接受见证 $p$，记 $a=a_k(p)$、$J=J_k(p)$、$d=2^{k-1}$、$\kappa=M/d$，并令 $N=M+s$。引理B.1保证 $p>0$、$a>0$，且

$$
\kappa\log a>-2\log k.
$$

先控制 $s$ 的范围。在 $k=17$ 时，引理B.2的 (5) 及其起点估计给出 $2^{17/2}>340$、$8(1+\log17)<32$。对于实数 $x\ge17$，比值 $2^{x/2}/[8(1+\log x)]$ 的对数导数为

$$
\frac{\log2}2-\frac1{x(1+\log x)}
>\frac14-\frac1x>0,
$$

其中使用引理B.2证明中的 $\log2>1/2$。结合 $\sqrt M\ge2^{k/2}$，得到 $s\ge1$。又因 $8(1+\log k)>1$ 且 $M\ge1$，有 $s\le\sqrt M\le M$，从而 $N\le2M$。

接着控制 $r=r_k(N)$。对于实数 $x\ge16$，比值 $2^{x/2}/x^2$ 的对数导数满足

$$
\frac{\log2}2-\frac2x>\frac14-\frac2x>0,
$$

而在 $x=16$ 时该比值等于一。因此 $\sqrt M\ge2^{k/2}\ge k^2$。根据 $v=v_k(N)$ 的定义，有 $v(v-1)\le k(k-1)N$，故

$$
\frac{v-1}{k-1}\le\sqrt{\frac{kN}{k-1}}\le2\sqrt M.
$$

最后一步使用 $N\le2M$ 及 $k/(k-1)\le2$。同时 $k^2-k+1\le k^2\le\sqrt M$。因此，推论C.2中定义的 $r$ 满足

$$
1<k\le r\le2\sqrt M.
$$

由初等对数不等式，

$$
\begin{aligned}
\log\frac{N^2(1-1/r)}{M(M-1)}
&=2\log\left(1+\frac sM\right)+\log\left(1-\frac1r\right)
+\log\left(1+\frac1{M-1}\right)\\
&\le\frac{2s+2}{M}-\frac1r.
\end{aligned}
$$

这里 $1/(M-1)\le2/M$，且所有对数均有定义。由 $s$ 的定义、$\sqrt M\ge2^{17/2}>340$ 以及 $r\le2\sqrt M$，有

$$
(2+2\log k)s+2\le\frac{\sqrt M}{4}+2
<\frac{\sqrt M}{2}\le\frac M r.
$$

故

$$
\log\frac{N^2(1-1/r)}{M(M-1)}
<-\frac{2s\log k}{M}
<\frac{s\kappa\log a}{M}=\frac{s\log a}{d}.
$$

第二个严格不等式使用引理B.1及 $s>0$。因此

$$
\frac{g_k^*(N)}{M(M-1)}<a^{s/d}.
$$

与 $M$ 的接受不等式相乘，得到

$$
\frac{g_k^*(N)J}{d^2}<a^{N/d}.
$$

推论C.2遂保证任意至多 $N=M+s$ 边的原始超图均可二染。最后，引理B.4给出 $B_{\rm RS}(k)\in\mathcal A_k$ 及 $B_{\rm RS}(k)\ge2^k$；取 $M=B_{\rm RS}(k)$，便得到 $s=\Delta(k)\ge1$ 以及所述染色结论和整数下界。∎

引理C.1是线性交族的自含团界。其公共点二分只用于约束同一实际超图的单交团，不要求将全部团划为两种全局结构。定理C始终保留同一个接受见证 $p$，用有向单交对数的削减吸收新增的 $\Delta(k)$ 条边。与其他明确参考界的比较见 [BASELINE_COMPARISON.md](BASELINE_COMPARISON.md)。
