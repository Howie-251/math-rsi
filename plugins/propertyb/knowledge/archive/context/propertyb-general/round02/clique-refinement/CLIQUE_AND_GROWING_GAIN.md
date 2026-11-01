# Refined single-intersection cliques and a growing uniform integer gain

2026-10-21. Independent mathematical verification and full derivation. `review_independence: same-family`; `acceptance_status: provisional`. The clique estimate is a standard-type fact about pairwise singly intersecting set families; no originality claim is attached to it. The new formula below is compared only with the specified RS–FKG–exact-integral criterion, not with the full literature envelope.

## 1. A complete clique bound

Let $\mathcal F$ be a nonempty family of $q$ distinct $k$-subsets of a $v$-element set, where $k\ge2$ and every two distinct members meet in exactly one point. Put $K=k^2-k+1$.

If all members contain a point $x$, their sets outside $x$ are pairwise disjoint and each has size $k-1$. Hence

$$q(k-1)\le v-1,\qquad q\le\left\lfloor\frac{v-1}{k-1}\right\rfloor.\tag{1}$$

Otherwise the common intersection of the whole family is empty. Fix one member $e$. For each $x\in e$, choose a member $f_x$ not containing $x$, which exists by the empty-common-intersection assumption. Every member $g$ containing $x$ meets $f_x$ in a unique point. These meeting points are distinct as $g$ varies: two different members through $x$ sharing a point of $f_x$ would meet in that point and in $x$, while $x\notin f_x$. There are only $k$ points in $f_x$, so the number $d(x)$ of family members through $x$ is at most $k$.

Each member other than $e$ meets $e$ in exactly one point. Counting these members at their unique intersection with $e$ gives the exact identity

$$q-1=\sum_{x\in e}(d(x)-1)\le k(k-1),\qquad q\le K.\tag{2}$$

These two cases exhaust all families. Therefore

$$q\le\max\left\{K,\left\lfloor\frac{v-1}{k-1}\right\rfloor\right\}.\tag{3}$$

The incidence-Gram argument in the audited core manuscript also gives $q\le v$. Combining these bounds is valid and sometimes useful when $v$ is small.

## 2. A sufficient criterion with no structural premise

For an integer edge budget $N\ge1$, define

$$w=v_k(N)=\left\lfloor\frac{1+\sqrt{1+4k(k-1)N}}2\right\rfloor,$$

$$r_k(N)=\min\left\{w,\max\left\{K,\left\lfloor\frac{w-1}{k-1}\right\rfloor\right\}\right\},$$

and

$$g_k^*(N)=\min\left\{N(N-1),\left(1-\frac1{r_k(N)}\right)N^2\right\}.$$

For every allowed $k,N$, $w\ge k\ge2$ and $K\ge3$, so $r_k(N)\ge2$ and all denominators are defined.

The minimal-vertex counterexample reduction of the audited core theorem gives an actual counterexample $H$ with $m\le N$ edges and $v\le w$ vertices. Any clique in its actual single-intersection graph is a family of the kind considered in Section 1. Thus its clique number is at most $r_k(N)$. Apply the core manuscript's self-contained complement-graph/Caro–Wei/Cauchy argument with this integer $r_k(N)$ in place of $v$. It gives

$$\gamma(H)\le\left(1-\frac1{r_k(N)}\right)m^2\le\left(1-\frac1{r_k(N)}\right)N^2.$$

Also $\gamma(H)\le m(m-1)\le N(N-1)$, so $\gamma(H)\le g_k^*(N)$. The actual RS failure lemma from the audited core therefore proves the following unconditional sufficient criterion:

$$1-a_k(p)^{N/2^{k-1}}+\frac{g_k^*(N)}{4^{k-1}}I_k(p)<1\quad\Longrightarrow\quad m(k)\ge N+1,\tag{4}$$

where $a_k(p)=1-(1-p)^k$, $I_k(p)=\int_0^p(1-y^2)^{k-1}\,dy$, and $0<p\le1$. This introduces no pair-covering, fixed-vertex, degree, or intersection hypothesis on the original input hypergraph.

## 3. Parameters forced by the old RS criterion

Fix an integer $k\ge17$ and an accepted old integer budget $M\ge2^k$. Write $d=2^{k-1}$, $\kappa=M/d$, $a=a_k(p)$, and $I=I_k(p)$ for a witnessing $p\in[0,1]$. The old strict criterion is

$$\frac{M(M-1)}{d^2}I<a^\kappa.\tag{5}$$

It excludes $p=0$ and implies $p>1/k^2$, $I\ge1/(2k^2)$, and

$$a^\kappa>\frac{\kappa^2}{4k^2}\ge\frac1{k^2},\qquad \kappa\log a>-2\log k.\tag{6}$$

For completeness, $M(M-1)/d^2\ge\kappa^2/2$ because $M\ge2$. If $p\le1/k^2$, Bernoulli gives $I\ge p/2$ and $a\le kp$, forcing

$$\frac{\kappa^2}{4k}<(kp)^{\kappa-1}\le kp\le1/k\le\frac{\kappa^2}{4k},$$

a contradiction since $\kappa\ge2$. Integrating only on $[0,1/k^2]$ then proves the lower bound on $I$ and hence (6). No numerical optimization is used.

## 4. Quantified gain

Define the positive integer increment

$$\boxed{s=s_k(M)=\left\lfloor\frac{\sqrt M}{8(1+\log k)}\right\rfloor,\qquad N=M+s.}\tag{7}$$

The following estimates hold throughout the entire range $k\ge17$, $M\ge2^k$.

First, $2^{x/2}/x^2$ is increasing for all real $x\ge16$: its logarithmic derivative is $(\log2)/2-2/x>1/4-2/16>0$. Since $2^{16/2}=16^2$, this proves

$$\sqrt M\ge2^{k/2}\ge k^2.\tag{8}$$

The elementary bound $\log k\le k-1$ shows

$$\frac{\sqrt M}{8(1+\log k)}\ge\frac{k^2}{8k}=\frac k8\ge\frac{17}{8}>2,$$

so $s\ge2$, in particular $s\ge1$. Also $s\le\sqrt M/[8(1+\log k)]<M$, whence $N<2M$.

Next, the integer $w=v_k(N)$ satisfies $w(w-1)\le k(k-1)N$. Therefore

$$\frac{w-1}{k-1}\le\sqrt{\frac{kN}{k-1}}.$$

Combining this with (8), $K<k^2\le\sqrt M$, $N<2M$, and $k/(k-1)\le2$, gives

$$2\le r_k(N)\le\max\left\{K,\sqrt{\frac{kN}{k-1}}\right\}\le2\sqrt M.\tag{9}$$

This is the quantitative difference from the old Gram-only estimate, whose corresponding scale was $k\sqrt M$.

Let $r=r_k(N)$ and define

$$R=\frac{N^2(1-1/r)}{M(M-1)}>0.$$

Elementary logarithm inequalities yield

$$\begin{aligned}
\log R
&=2\log(1+s/M)+\log(1-1/r)-\log(1-1/M)\\
&\le\frac{2s}{M}-\frac1r+\frac1{M-1}\\
&\le\frac{2s+2}{M}-\frac1r.
\end{aligned}\tag{10}$$

Definition (7) gives

$$2(1+\log k)s+2\le\frac{\sqrt M}{4}+2<\frac{\sqrt M}{2},\tag{11}$$

where the strict final inequality uses $\sqrt M\ge k^2>8$. Using (9) in (10), then (11) and (6), gives the strict chain

$$\begin{aligned}
\log R
&\le\frac{2s+2}{M}-\frac1{2\sqrt M}\\
&<-\frac{2s\log k}{M}\\
&<\frac{s\kappa\log a}{M}=\frac{s\log a}{d}.
\end{aligned}\tag{12}$$

Thus

$$\frac{g_k^*(N)}{M(M-1)}\le R<a^{s/d}.$$

Multiplying (5) by the nonnegative ratio gives

$$\frac{g_k^*(N)I}{d^2}<a^{\kappa+s/d}=a^{N/d}.$$

If $g_k^*(N)=0$ the conclusion follows directly from $a>0$; otherwise the preceding multiplication preserves strictness. This proves criterion (4) at the larger budget $N=M+s$, using the very same $p$ as the old criterion.

## 5. Exact integer lower bound and growth scale

The independently audited budget definition is

$$B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\ 1-a_k(p)^{M/2^{k-1}}+\frac{M(M-1)}{4^{k-1}}I_k(p)<1\right\}.$$

For every $k\ge17$, the set is nonempty and finite and $2^k\le B_{\rm RS}(k)<k2^k$. Take $M=B_{\rm RS}(k)$ in (7) and apply the sufficient criterion just proved. The unconditional lower bound is

$$\boxed{m(k)\ge B_{\rm RS}(k)+\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor+1\qquad(k\ge17).}\tag{13}$$

The old bound from the specified criterion is $m(k)\ge B_{\rm RS}(k)+1$, so the exact accepted-budget gain is the displayed floor. Since $\log k\ge1$ on this range,

$$s_k(M)\ge\left\lfloor\frac{\sqrt M}{16\log k}\right\rfloor.$$

Thus one may state the simpler, slightly weaker uniform improvement

$$\boxed{m(k)\ge B_{\rm RS}(k)+\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{16\log k}\right\rfloor+1\qquad(k\ge17).}\tag{14}$$

This establishes a growing absolute improvement of order $\sqrt{B_{\rm RS}(k)}/\log k$ over that exact old integer criterion. It does not change its leading asymptotic constant and does not by itself establish superiority over every applicable published lower bound. No per-$k$ scan, finite graph table, Lean execution, or unverified real-root rounding is part of this proof.
