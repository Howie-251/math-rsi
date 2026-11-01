# A uniform one-edge gain and its exact integer consequence

2026-10-21. Separate proposed revision; the original round01 manuscript is unchanged. Mathematical status: **PROVABLE AS STATED** as an analytic comparison lemma. Review status: same-family/provisional. The Property B consequence is conditional on the separately audited graph-cap probability criterion.

## Claim, notation, and dependency map

For integer $k\ge17$, write $d=2^{k-1}$ and define, for $p\in[0,1]$,

$$a=a_k(p)=1-(1-p)^k,\qquad I=I_k(p)=\int_0^p(1-y^2)^{k-1}\,dy.$$

For integer $M\ge1$ let

$$F_k(M,p)=1-a_k(p)^{M/d}+\frac{M(M-1)}{d^2}I_k(p).$$

**Analytic gain lemma.** Let $M\ge2^k$ be an integer and suppose $F_k(M,p)<1$. Put $N=M+1$. For every pair of real numbers satisfying

$$1<V\le1+k\sqrt N,\qquad 0\le G\le N^2(1-1/V),$$

one has

$$1-a_k(p)^{N/d}+\frac{G}{d^2}I_k(p)<1.$$

**Integer-budget consequence.** The set $\mathcal A_{\rm RS}(k)=\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\ F_k(M,p)<1\}$ is nonempty and finite. Its maximum $B_{\rm RS}(k)$ exists and satisfies $2^k\le B_{\rm RS}(k)\le k2^k-1$. If the graph-cap criterion is valid for all finite simple $k$-uniform hypergraphs at the stated input budget, then

$$\boxed{m(k)\ge B_{\rm RS}(k)+2\quad(k\ge17).}$$

The analytic lemma uses only Bernoulli's inequality, elementary logarithm bounds, and the displayed definitions. The integer consequence uses that lemma and the stated separate validity of the graph-cap probability criterion. No assertion about the complete known lower-bound envelope is included.

## 1. Parameters forced by the old strict criterion

Set $\kappa=M/d\ge2$. The hypothesis is equivalent to

$$C I<a^\kappa,\qquad C=\frac{M(M-1)}{d^2}=\kappa^2(1-1/M)\ge\frac{\kappa^2}{2}.$$

At $p=0$ the criterion equals $1$, so $p>0$ and $a,I>0$. If $p\le1/k^2$, then $p\le1/k$ and Bernoulli gives

$$I\ge p/2,\qquad a\le kp.$$

It would follow that

$$\frac{\kappa^2}{4k}<(kp)^{\kappa-1}\le kp\le\frac1k\le\frac{\kappa^2}{4k},$$

a contradiction. Therefore $p>1/k^2$. On $0\le y\le1/k^2$, Bernoulli also gives $(1-y^2)^{k-1}\ge1-(k-1)y^2\ge1/2$, whence

$$I\ge\frac1{2k^2},\qquad a^\kappa>\frac{\kappa^2}{4k^2}\ge\frac1{k^2}.$$

Since $a\le1$, this implies both

$$\kappa<2k,\qquad \kappa\log a>-2\log k.\tag{1}$$

The second estimate keeps the two factors together and is the simplification that permits a lower uniform threshold.

## 2. One inequality throughout the entire half-line

For every real $x\ge17$,

$$2^{x/2}>8x+4x\log x.\tag{2}$$

To check the initial point, $e^3>\sum_{j=0}^{5}3^j/j!=92/5>17$, so $\log17<3$. Also $\sqrt2>7/5$. Thus

$$2^{17/2}=256\sqrt2>256\cdot7/5>340>8\cdot17+4\cdot17\log17.$$

For the rest of the interval, the logarithmic derivative of $2^{x/2}/[x(2+\log x)]$ is

$$\frac{\log2}{2}-\frac1x-\frac1{x(2+\log x)}>\frac14-\frac2x\ge\frac14-\frac2{17}>0.$$

Here $\log2>1/2$ follows by integrating $1/t>1/2$ on $1\le t<2$. Hence the ratio increases throughout the half-line, proving (2) without sampling integer values.

Since $M\ge2^k$, (2) implies $\sqrt M>8k+4k\log k$. Moreover $N\le2M$, $\sqrt2<3/2$, and $1\le(k/2)\sqrt M$ give

$$V\le1+k\sqrt N\le2k\sqrt M.$$

Consequently

$$\frac1V\ge\frac1{2k\sqrt M}>\frac{4+2\log k}{M}.\tag{3}$$

## 3. Paying for the extra edge

Define the positive real ratio

$$R=\frac{N^2(1-1/V)}{M(M-1)}.$$

Because $M>1$ and $V>1$, all logarithms below are defined. Using $\log(1+u)\le u$, $\log(1-u)\le-u$, and $-\log(1-u)\le u/(1-u)$ gives

$$\begin{aligned}
\log R
&=2\log(1+1/M)+\log(1-1/V)-\log(1-1/M)\\
&\le\frac2M-\frac1V+\frac1{M-1}\\
&\le\frac4M-\frac1V\\
&<-\frac{2\log k}{M}\\
&<\frac{\kappa\log a}{M}=\frac{\log a}{d}.
\end{aligned}$$

The penultimate step is (3), and the final step is (1). It follows that

$$\frac{G}{M(M-1)}\le R<a^{1/d}.$$

If $G=0$, the desired inequality follows immediately from $a>0$. Otherwise multiply the old strict inequality by $G/[M(M-1)]$ to obtain

$$\frac{G I}{d^2}<a^{\kappa+1/d}=a^{N/d}.$$

This proves the analytic gain lemma, with the same $p$ and a strict conclusion. The argument also allows $p=1$; it only excludes $p=0$ by the old hypothesis.

## 4. Nonempty finite integer budget set

Let $M_0=2^k$ and choose $p=1/k$. Integer Bernoulli gives

$$(1-1/k)^{-k}=(1+1/(k-1))^k\ge1+\frac{k}{k-1}>2,$$

so $a_k(1/k)>1/2$. Since $I_k(1/k)\le1/k$,

$$\frac{M_0(M_0-1)}{d^2}I_k(1/k)<\frac4k<\frac14<a_k(1/k)^2.$$

The strict middle inequality uses $k\ge17$. Thus $M_0\in\mathcal A_{\rm RS}(k)$.

Any member below $M_0$ belongs to a finite interval. Any member at least $M_0$ satisfies $\kappa<2k$ by Section 1, hence $M<k2^k$. Therefore

$$\varnothing\ne\mathcal A_{\rm RS}(k)\subseteq\{1,\ldots,k2^k-1\}.$$

The largest member $B_{\rm RS}(k)$ exists, is at least $2^k$, and has an actual witnessing $p$. This definition needs no claim about a continuous optimizer attaining its supremum. In addition, for fixed $p$ the expression $F_k(M,p)$ is nondecreasing in $M\ge1$, so all smaller positive integer budgets are also accepted.

The definition can also be expressed using a finite collection of exact polynomial positivity questions. Indeed

$$I_k(p)=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}{j}\frac{p^{2j+1}}{2j+1},\qquad Q_{k,M}(p)=\frac{M(M-1)}{d^2}I_k(p).$$

Since $Q_{k,M}(p),a_k(p)\ge0$ on $[0,1]$, the strict criterion is equivalent to

$$Q_{k,M}(p)^d<a_k(p)^M.$$

Both sides are polynomials with rational coefficients and integer exponents. Thus $B_{\rm RS}(k)$ is an exactly specified finite maximum, not a rounded floating-point root; exact real-algebraic positivity would decide it. No such large computation is needed by the uniform gain proof.

## 5. Exact conditional Property B consequence

For integer budget $N$, put

$$V_k(N)=\left\lfloor\frac{1+\sqrt{1+4k(k-1)N}}2\right\rfloor,\qquad G_k(N)=2t_{V_k(N)}(N),$$

where $t_v(N)$ is the number of edges in the balanced complete $v$-partite graph on $N$ vertices. For the budgets used here, $V_k(N)>1$. Its definition gives

$$V_k(N)\le1+k\sqrt N,\qquad 0\le G_k(N)\le N^2(1-1/V_k(N)).$$

Assume the separate probability/interface theorem: for every budget $N$, the strict inequality

$$1-a_k(p)^{N/d}+G_k(N)I_k(p)/d^2<1$$

implies that every finite simple $k$-uniform hypergraph with at most $N$ edges has Property B. Apply the analytic gain lemma to $M=B_{\rm RS}(k)$ and its witnessing $p$, with $N=M+1$. The displayed sufficient inequality holds. Hence every original hypergraph with at most $B_{\rm RS}(k)+1$ edges is two-colorable, which means

$$m(k)\ge B_{\rm RS}(k)+2.$$

The specified old criterion alone yields $m(k)\ge B_{\rm RS}(k)+1$. Thus this conditional conclusion improves its exact integer lower bound by at least one, uniformly on $k\ge17$.

## What this proof does not settle

The actual RS event decomposition and graph-cap interface, as well as superiority to all applicable published lower bounds, remain separate obligations. This proof neither assumes that other criteria are weaker nor labels its conditional integer improvement a new best-known bound.
