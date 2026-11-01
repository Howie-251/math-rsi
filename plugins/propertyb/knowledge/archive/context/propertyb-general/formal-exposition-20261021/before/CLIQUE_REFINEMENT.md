# 单交团的公共点二分与增长的整数增益

2026-10-21，完整增长整数增益证明；正式规格为 `FORMAL_SPEC_PROPERTYB_GENERAL.md`，审计与有效跨家族审阅在 `context/propertyb-general/round02/`。文献归属和参考界比较见 `BASELINE_COMPARISON.md`。

## 团大小的加强

设 $q$ 条互异 $k$ 元边两两恰交一点，支撑包含在 $v$ 个顶点内。

若全部边有公共点，它们去掉公共点后的尾互不相交，故 $q(k-1)+1\le v$。

若无公共点，固定其中一条边 $e$。对每个 $x\in e$，取团中一条不含 $x$ 的边 $f$。所有含 $x$ 的团内边都恰交 $f$ 一点，且这些交点互不相同：否则两条团内边会同时含 $x$ 及另一个交点。因此团内含 $x$ 的边数 $d_x\le k$。每条非 $e$ 的边恰交 $e$ 一点，故

$$q-1=\sum_{x\in e}(d_x-1)\le k(k-1).$$

所以原超图的单交图满足

$$\omega(S(H))\le\max\left\{k^2-k+1,\left\lfloor\frac{v-1}{k-1}\right\rfloor\right\}.$$

结合此前Gram界 $\omega\le v$ 及最小顶点反例上界，定义

$$r_k(N)=\min\left\{v_k(N),\max\left\{k^2-k+1,\left\lfloor\frac{v_k(N)-1}{k-1}\right\rfloor\right\}\right\}.$$

则可将定理A的 $g_k(N)$ 改成

$$g_k^*(N)=\min\left\{N(N-1),N^2(1-1/r_k(N))\right\}.$$

证明仍为原补图独立集期望加Cauchy，使用团界 $r_k(N)$；不要求上面两类团拼成任何全局分类。

## 相对指定RS判据的增长整数增益

设 $k\ge17$，整数 $M\ge2^k$ 满足旧精确判据，取同一个见证 $p$，并沿用 $a,J,d,\kappa$。前稿已得 $\kappa\log a>-2\log k$。取

$$s=\left\lfloor\frac{\sqrt M}{8(1+\log k)}\right\rfloor,\qquad N=M+s.$$

此时 $s\ge1$：在 $k=17$ 由 $\sqrt M\ge2^{17/2}>340$、$8(1+\log17)<32$；比值 $2^{x/2}/[8(1+\log x)]$ 的对数导数为 $(\log2)/2-1/[x(1+\log x)]>0$，故全范围成立。又 $s\le M$，所以 $N\le2M$。

对 $x\ge16$，$2^{x/2}/x^2$ 的对数导数 $(\log2)/2-2/x>0$，而 $x=16$ 时比值为1。因此 $\sqrt M\ge2^{k/2}\ge k^2$。由 $v_k(N)(v_k(N)-1)\le k(k-1)N$ 得

$$\frac{v_k(N)-1}{k-1}\le\sqrt{\frac{kN}{k-1}}\le2\sqrt M,$$

从而 $1<r_k(N)\le2\sqrt M$。

写 $r=r_k(N)$。有

$$
\log\frac{N^2(1-1/r)}{M(M-1)}
\le\frac{2s+2}{M}-\frac1r.
$$

又

$$
(2+2\log k)s+2\le\frac{\sqrt M}{4}+2<\frac{\sqrt M}{2}\le\frac M r.
$$

故上面的对数严格小于 $-2s\log k/M$，而由旧参数控制，这又小于 $s\log a/d$。因此

$$
\frac{g_k^*(N)}{M(M-1)}<a^{s/d},
\qquad
\frac{g_k^*(N)J}{d^2}<a^{N/d}.
$$

新充分判据在预算 $N$ 成立。取 $M=B_{\rm RS}(k)$，由最大预算的存在性及加强后的定理A，得到

$$
m(k)\ge B_{\rm RS}(k)+1+
\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor
\quad(k\ge17).
$$

这里保持同一个旧判据见证 $p$，由结构削减吸收新增的 $s$ 条边。公共点二分属于经典线性交族／Deza型团界，正文给出自含证明；参考界的比较在 `BASELINE_COMPARISON.md` 中完成。
