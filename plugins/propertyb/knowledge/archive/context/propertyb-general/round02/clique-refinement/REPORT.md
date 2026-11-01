# Independent clique-refinement audit and quantified consequence

2026-10-21. Same-family/provisional mathematical audit. Files outside this directory were not changed. No new claim, Lean execution, goal update, literature-novelty certification, or finite search was performed.

## Verdict

**PASS.** The proposed clique proof is complete. Its common-point case counts disjoint $(k-1)$-petals; its empty-common-intersection case permits an edge avoiding every fixed $x$, and the injective intersection map really gives $d(x)\le k$. The identity $q-1=\sum_{x\in e}(d(x)-1)$ is exact. Thus every pairwise singly intersecting family obeys

$$q\le\max\left\{k^2-k+1,\left\lfloor\frac{v-1}{k-1}\right\rfloor\right\}.$$

The standard Gram bound $q\le v$ may simultaneously be retained by taking a minimum. No assumption of an actual common point was imposed on the family, and the no-common-point branch exhausts its complement.

## Complete proof delivered

`CLIQUE_AND_GROWING_GAIN.md` contains the full clique proof, a refined budget-cap sufficient criterion with no extra hypergraph premise, and the complete analytic integer-gain proof. It uses the already independently audited actual RS failure lemma and minimal-vertex reduction from `CORE_THEOREM.md`, replacing only that manuscript's graph clique bound.

For all integers $k\ge17$ and all old accepted integer budgets $M\ge2^k$, put

$$s=\left\lfloor\frac{\sqrt M}{8(1+\log k)}\right\rfloor.$$

Then the new criterion at budget $M+s$ holds with exactly the old witnessing $p$. The main quantitative facts, each proved over the entire range, are:

1. $\sqrt M\ge2^{k/2}\ge k^2$; the real ratio $2^{x/2}/x^2$ increases for $x\ge16$, with equality at $16$.
2. $s\ge2$ follows from $\log k\le k-1$; also $s<M$, so $N=M+s<2M$.
3. The refined clique cap $r_k(N)$ is at most $\max\{k^2-k+1,\sqrt{kN/(k-1)}\}\le2\sqrt M$.
4. The strict old criterion implies the coupled estimate $\kappa\log a>-2\log k$, where $\kappa=M/2^{k-1}$.
5. For the coefficient ratio $R=N^2(1-1/r_k(N))/[M(M-1)]$, elementary logarithm bounds and $2(1+\log k)s+2\le\sqrt M/4+2<\sqrt M/2$ give $\log R<s\log a/2^{k-1}$.
6. The ratio inequality absorbs the new exponent $s/2^{k-1}$, and hence all $s$ extra edges, at the same $p$.

Taking the actual finite maximum $B_{\rm RS}(k)$ gives the unconditional mathematical conclusion

$$m(k)\ge B_{\rm RS}(k)+\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor+1\qquad(k\ge17).$$

In the exact requested form, the increment is at least

$$\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{16\log k}\right\rfloor.$$

The root's proposed constant $1/8$ and threshold $17$ are valid as stated. I did not tune them further or launch a scan.

## Scope

This is a genuine strengthened structural cap and a growing absolute improvement relative to the specified old RS–FKG–exact-integral integer budget. The pairwise-singly-intersecting-family fact may already be standard; no originality inference is made from this independent proof. Comparison against the full applicable literature envelope and designated cross-family final acceptance remain separate obligations.
