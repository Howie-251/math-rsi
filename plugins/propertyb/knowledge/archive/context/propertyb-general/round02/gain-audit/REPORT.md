# Uniform-gain independent audit

2026-10-21. Independent local mathematical audit, `review_independence: same-family`, `acceptance_status: provisional`. No external reviewer or Lean execution is represented by this report.

## Verdict and exact scope

**PROVABLE AS STATED.** I read the complete `round01/comparison/UNIFORM_GAIN.md` and the complete `round01/root/SINGLE_INTERSECTION_TURAN.md`, independently checked each inequality, and found no mathematical error in the stated conditional analytic lemma for every integer $k\ge32$, every integer $M\ge2^k$, and every $p\in[0,1]$ satisfying its strict old criterion. This is a universal proof, not a sampled numerical check.

The original manuscript remains unchanged. The separate `SIMPLIFIED_GAIN_AND_INTEGER_BOUND.md` gives a shorter complete proof, strengthens the analytic range to $k\ge17$, proves the old budget set is nonempty and finite, and states the exact integer conclusion. Its conclusion is relative to the specified RS–FKG–exact-integral criterion only. It does not establish superiority to the complete literature envelope, nor does this audit certify the separate RS probability/interface obligation.

## Line-by-line checks of the original lemma

Write $r=k-1$, $\kappa=M/2^r$, $a=1-(1-p)^k$, and $I=\int_0^p(1-y^2)^r\,dy$. The hypothesis is exactly

$$\frac{M(M-1)}{4^r}I<a^\kappa.$$

1. At $p=0$ the original objective is exactly $1$, so the strict hypothesis excludes it. Hence $a,I>0$, and all divisions and logarithms used later are defined. The endpoint $p=1$ is permitted; then $a=1$ and the logarithmic inequalities still hold.
2. $M\ge2^k$ implies $\kappa\ge2$ and $M(M-1)/4^r=\kappa^2(1-1/M)\ge\kappa^2/2$. For $p\le1/k$, Bernoulli gives $I\ge p/2$ and $a\le kp$. If $p\le1/k^2$, the manuscript's division by $p$ yields the strict/non-strict contradiction $\kappa^2/(4k)<(kp)^{\kappa-1}\le1/k\le\kappa^2/(4k)$. Thus $p>1/k^2$.
3. Restricting the integral to $[0,1/k^2]$ directly proves $I\ge1/(2k^2)$, without needing the manuscript's two cases. Consequently $a^\kappa>\kappa^2/(4k^2)$, so $\kappa<2k$ and $M<k2^k$. Also $a\ge p>1/k^2$ gives $-\log a<2\log k$; the weaker non-strict version used in the original is valid.
4. For $f(x)=x+x^2\log x$, $3f(x)/x-f'(x)=2+x\log x-x\ge0$ on $x\ge32$. The manuscript's derivative bound and exact anchor $2^{16}=65536>41216$ therefore prove its inequality (7) throughout the entire half-line. It is not an inference from a finite list of $k$.
5. $M+1\le2M$ and $1\le(k/2)\sqrt M$ imply $1+k\sqrt{M+1}\le2k\sqrt M$ using $\sqrt2<3/2$. Thus the stated upper bound on $V'$ implies inequality (9). Combining it with (8) yields (10) in the correct direction: $1/V'\ge1/(2k\sqrt M)>(4+4k\log k)/M$.
6. Since $V'>1$ and $M>1$, both logarithms in $R=(M+1)^2(1-1/V')/[M(M-1)]$ are defined. Expanding the logarithm yields exactly $2\log(1+1/M)+\log(1-1/V')-\log(1-1/M)$. Each of the three estimates in (11) has the correct sign. The $4/M$ bound and strict (10) give (12).
7. The signs in the last chain are correct: $\kappa<2k$ implies $-4k\log k/M\le-2\kappa\log k/M$, while $\log a\ge-2\log k$ implies $-2\kappa\log k/M\le\kappa\log a/M$. Since $\kappa/M=2^{-r}$, this is precisely the exponent needed to pay for $M\mapsto M+1$.
8. Exponentiating gives $G'/[M(M-1)]\le R<a^{2^{-r}}$. If $G'=0$, the final conclusion follows immediately because $a>0$; otherwise multiply the old strict inequality by its positive ratio. Either way the final sufficient criterion is strict. No integrality assumption on $G'$ or $V'$ is needed for this analytic statement.

The candidate $V'=V_k(M+1)$ from the root manuscript does satisfy $1<V'\le1+k\sqrt{M+1}$ on this range. The exact Turan value $2t_{V'}(M+1)$ satisfies the required real cap $G'\le(M+1)^2(1-1/V')$. Establishing that this $G'$ dominates the actual directed single-intersection count is a separate hypergraph/interface argument, explicitly excluded from the analytic lemma.

## Missing integer-budget closure, now supplied

For $k\ge17$, define

$$\mathcal A_{\rm RS}(k)=\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\ 1-a_k(p)^{M/2^{k-1}}+\frac{M(M-1)}{4^{k-1}}I_k(p)<1\right\}.$$

At $M=2^k$, choose $p=1/k$. Integer Bernoulli gives $(1-1/k)^{-k}>2$, hence $a_k(1/k)>1/2$. Also $I_k(1/k)\le1/k$. Therefore

$$\frac{M(M-1)}{4^{k-1}}I_k(1/k)<\frac4k<\frac14<a_k(1/k)^2,$$

so $2^k\in\mathcal A_{\rm RS}(k)$. Every member below $2^k$ is already bounded, and the parameter argument above shows every member at least $2^k$ is less than $k2^k$. Consequently the set is nonempty and finite and

$$B_{\rm RS}(k):=\max\mathcal A_{\rm RS}(k)\quad\text{exists},\qquad 2^k\le B_{\rm RS}(k)\le k2^k-1.$$

The maximum is an actual member with an actual witnessing $p$; no limiting argument or attainment of a real-valued optimizer is required. For fixed $p$, the objective is nondecreasing in integer $M\ge1$, so the set is an initial segment as well, although maximality alone suffices for the improvement proof.

If the new graph-cap probability criterion is valid for all original hypergraphs with at most the input budget, the analytic gain applied to this maximum proves all hypergraphs with at most $B_{\rm RS}(k)+1$ edges are two-colorable. Thus the exact lower bound is

$$\boxed{m(k)\ge B_{\rm RS}(k)+2.}$$

The old integer bound from this criterion is $m(k)\ge B_{\rm RS}(k)+1$. These formulas distinguish an accepted edge budget from a lower bound on the first noncolorable edge count; there is no off-by-one ambiguity.

## Shorter proof and range improvement

The old hypothesis actually gives the stronger coupled estimate $\kappa\log a>-2\log k$ directly from $a^\kappa>\kappa^2/(4k^2)\ge1/k^2$. Using it avoids separately bounding $\kappa$ and $\log a$ in the exponent comparison. It is enough to require

$$2^{k/2}>8k+4k\log k.$$

This holds throughout $k\ge17$: at $17$, $\log17<3$ and $2^{17/2}>256\cdot7/5>340>8\cdot17+4\cdot17\log17$; the ratio $2^{x/2}/[x(2+\log x)]$ has positive logarithmic derivative for every $x\ge17$. A full proof with all constants and endpoints appears in the separate manuscript. No per-$k$ computation was used or needed.

## Outstanding work outside this audit

The final global theorem still needs the actual hypergraph-to-RS probability criterion and the complete applicable literature-envelope comparison. In particular, improving this specified RS criterion by one integer budget does not alone establish a new public best lower bound for any range of $k$.
