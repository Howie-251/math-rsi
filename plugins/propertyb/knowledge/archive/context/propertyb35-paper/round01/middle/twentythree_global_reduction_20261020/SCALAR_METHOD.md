# The bounded23-point scalar diagnostic

This document records the arithmetic used by `SCALAR_PILOT.py` and `MIN7_GAMMA3_PILOT.py`. It is a necessary moment relaxation, not a classification of hypergraphs. A non-strict key is not a counterexample or an existence assertion.

Assume23 points,35 distinct five-edges, point-pair coverage, and a specified complete point-degree multiset. Let $n_j$ count unordered original edge pairs meeting in $j$ points, $W=\sum_v\binom{d_v}{2}$, and

\[
 \tau=\sum_{u<v}\binom{\lambda_{uv}-1}{2}.
\]

Pair-cover and total degree give

\[
 \sum_{u<v}(\lambda_{uv}-1)=350-\binom{23}{2}=97.
\]

Thus, writing $m=n_3,t=n_4$,

\[
 n_2=97+\tau-3m-6t,
 \quad n_1=W-194-2\tau+3m+8t,
 \quad n_0=692-W+\tau-m-3t. \tag{1}
\]

All counts are nonnegative integers. No PSD test or H realizability is assumed. The first one-flip necessary inequality gives $n_1\ge366$: with the balanced11-red sample on all 23 points, $D=\binom{23}{11}=1352078$, the single-edge monochromatic numerator is $p_*=50388$, and the ordered singleton-pair numerator is $q_*=6435$. A first-flip failure requires $35p_*+2n_1q_*/5\ge2D$.

## Point capacities

For each point of degree $d$, let $t_v$ count unordered edge pairs whose intersection is exactly that point. Its other through-point pairs satisfy

\[
 \sum_{F,G\ni v}(|F\cap G|-1)=4d-22+\tau_v.
\]

Each summand of a non-singleton pair is at most three. Therefore

\[
 0\le t_v\le p_v:=\binom d2-\max(0,\lceil(4d-22)/3\rceil),
 \qquad \sum_vt_v=n_1. \tag{2}
\]

This is the 23-point instance of the general [vertex flag capacity proof](../../root/vertex_flag_capacity_20261020/PROOF.md); it needs no bound on $\tau$ or codegrees.

For point-degree multiset $7^9,8^{14}$, $W=581$, the capacities are19 for a degree-seven point and24 for a degree-eight point. Hence $n_1\le507$. The old $\Gamma$-minimum-two box is32; the new $\Gamma$-minimum-three theorem changes it to31. Both are above the aggregate point bound here.

Every codegree is at most the second-highest degree $D_2$. The total row excess at a point is $4d-22$. Its maximum row $	au_v$ is bounded by filling integer excesses $e_{uv}=\lambda_{uv}-1$ to their cap $\min(d,D_2)-1$, because $\binom{e}{2}$ is convex. Summing and dividing by two gives the integer upper bound on global $	au$. In the balanced spectrum this is $\lfloor(9\cdot15+14\cdot24)/2\rfloor=235$.

## Shared middle-edge budgets

Use $C_j$ from the [global two-flip path repair](../../../../../proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md). Its23-point weighted sufficient condition is

\[
 4q_*n_1+165C_0+495C_1+1287C_2+3003C_3+6435C_4
 <18811520. \tag{3}
\]

The individual upper caps are:

- $C_0\le33n_0$.
- $C_1\le35n_1-\min\sum_vd_vt_v$, with (2); the minimum is filled by increasing point degree.
- $C_2\le c_2n_2$, $c_2=\min(33,\lfloor(\text{sum of six largest point degrees}-6)/2\rfloor)$.
- $C_3\le\min(c_3,g(\tau))n_3$, where $c_3=\min(33,\lfloor(\text{sum of four largest degrees}-4)/2\rfloor)$, and $g(\tau)$ is the maximum sum of four codegrees in $1,\ldots,D_2$ with total cost $\sum\binom{\lambda-1}{2}\le\tau$. The four actual cross pairs are distinct, so their costs may be charged to global $	au$.
- $C_4\le\min(D_2n_4,\ell(\tau)n_4,2n_4+(D_2-3)\tau)$, where $ell(\tau)=\max\{\lambda\le D_2:\binom{\lambda-1}{2}\le\tau\}$.

For the last cap, outer edge pairs with symmetric difference ${u,v}$ form a matching between edges through $u$ only and edges through $v$ only. Their number is at most $D_2-\lambda_{uv}$. The excess above two per such pair is at most

\[
 (\lambda-2)(D_2-\lambda)
 \le(D_2-3)\binom{\lambda-1}{2}\quad(\lambda\ge3).
\]

Summing proves the third cap. This argument does not assume codegrees at most four.

Let $b=34-\delta(\Gamma)$. For an original edge let $s_F$ be its number of unit-intersection neighbors and $x_{Fv}$ its unit flags attached at $v$, so $s_F=\sum_{v\in F}x_{Fv}$, $s_F\le b$, and $\sum_Fs_F=2n_1$. The total budget $P=\sum_jC_j$ has both upper bounds

\[
 P\le q f(b)+f(r),\quad 2n_1=qb+r,
 \quad f(s)=\frac{s^2-\min_{x_1+\cdots+x_5=s}\sum_i x_i^2}{2},
\]

and

\[
 P\le\left\lfloor\frac{qb^2+r^2-B_*(n_1)}2\right\rfloor,
\quad B_*(n_1)=\min_{\substack{\sum_vt_v=n_1\\0\le t_v\le p_v}}
 \sum_v B_{d_v}(t_v),
\]

where $B_d(t)$ is the minimum squared sum of $d$ nonnegative integers summing to $2t$. Balanced integer bins give each $B_d$; their increasing marginal costs give the exact separable minimum by merging marginal lists. Take the smaller of the two $P$ bounds.

Given individual caps $A_j$ and common cap $P$, a safe weighted maximum is obtained by layer integration:

\[
 \sum_{j=0}^4w_jC_j\le
 w_0\min(P,\sum_jA_j)
 +\sum_{i=1}^4(w_i-w_{i-1})\min(P,\sum_{j\ge i}A_j).
\]

This is exact for these box-plus-sum constraints; in particular it does not independently spend the same $P$ on five different terms.

## Exact output and stopping boundary

The balanced $7^9,8^{14}$ spectrum gives exactly 64220 keys under (1), nonnegativity, $366\le n_1\le507$, and $0\le\tau\le235$. This count is the same with $\Gamma$-minimum two or three. Using the old box32 leaves 6633 non-strict keys; the proved box31 leaves 4902. Exactly 1731 previously non-strict keys become strict. The new point-square $P$ never improves the old five-bin $P$ in this spectrum. All 4902 remaining keys are saved in `MIN7_GAMMA3_PILOT.json`.

The maximum remains non-strict at

\[
 (n_0,n_1,n_2,n_3,n_4)=(74,501,0,0,20),
 \quad\tau=23,\quad P\le12328,
 \quad L=19918800>18811520.
\]

The original bounded pilot also tested the two rare minimum-six spectra imported from the existing23-point analysis; neither closed, and neither gained from the new point-square bound. They are retained only as diagnostic failures and are handed to the separate L6 line. No remaining degree spectra were scanned, no full23-point closure is asserted, and no local layout was added.
