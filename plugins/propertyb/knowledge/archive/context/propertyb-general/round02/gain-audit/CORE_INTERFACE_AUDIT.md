# Independent audit of the complete core interface

2026-10-21. Auditor: fresh task continuation, local same-family mathematical audit. `review_independence: same-family`; `acceptance_status: provisional`. Read-only review of `proofs/propertyb-general/CORE_THEOREM.md`; only this report was written. No claim registry, Lean project, old Goal, or v2 project was changed.

## Conclusion

**PASS / PROVABLE AS STATED.** I read the entire core manuscript and checked its proof against the local RS author text, printed pages 4–7 and Appendix A.1, printed pages 26–27. I found no substantive error or missing mathematical interface in Theorem A, including the same-algorithm combination of the FKG/Jensen endpoint bound and exact directed single-intersection integral, the minimal-vertex quotient, the self-contained graph bound, and the passage from actual $m$ to budget $M$.

Consequently, composing Theorem A with the independently proved analytic gain and finite-budget definition in `SIMPLIFIED_GAIN_AND_INTEGER_BOUND.md` yields the unconditional mathematical conclusion

$$m(k)\ge B_{\rm RS}(k)+2\qquad\text{for every integer }k\ge17,$$

where $B_{\rm RS}(k)$ is exactly the maximum accepted integer budget of the specified RS–FKG–exact-integral criterion. No extra vertex, degree, intersection, or algorithmic certificate hypothesis remains in this composed conclusion. This result is a uniform improvement relative to that specified criterion; superiority to the full applicable literature envelope remains unestablished by this audit.

## Source alignment: one random algorithm throughout

The source's printed p.4 algorithm independently samples the initial coloring, Bernoulli eligibility bits, and continuous independent delays, then processes each vertex once. The manuscript's lines 50–52 describe this same algorithm. RS says that a relevant initially monochromatic edge “continues to be monochromatic.” The manuscript says it is still monochromatic in its initial color. These descriptions agree at the step of processing a vertex $x$: the edge contains the not-yet-processed $x$, whose color is still its initial color. No second algorithm or Boppana variant is being substituted.

RS printed p.5 Lemma 2.1 divides final monochromatic edges into (i) edges monochromatic initially and finally in the same color, and (ii) edges not initially of their final monochromatic color, which blame an initially monochromatic triggering edge. The manuscript uses precisely this split at lines 54–96. Appendix A.1 sharpens the union bound for class (i) of this same algorithm. The integral on printed pp.6–7 bounds class (ii) of that same algorithm. Adding the two estimates is therefore valid directly; independence between the two classes is neither used nor required.

## Initial-monochromatic event and conditional positive association

For any edge initially all red, each vertex has only one possible flip, from its initial red to blue. Hence final all-red is equivalent to no flip on the edge. If all eligibility bits on the edge are zero, no flip on that edge can occur, regardless of other edges. Conversely, if the edge has an eligible vertex but no flips have occurred on the edge by the earliest eligible vertex, the edge itself triggers that vertex's flip. Thus an initially monochromatic edge remains in its initial monochromatic color if and only if all its eligibility bits are zero. This is RS Claim 2.1 and Appendix A.1's event identity.

Condition on the complete initial coloring, not on any subsequent trajectory. Let $X$ be the number of initially monochromatic edges. The remaining eligibility bits retain their independent Bernoulli distribution. For each of these $X$ edges, the event “at least one eligibility bit equals one” is increasing in these bits and has probability $a_k(p)=1-(1-p)^k$. The positive-association induction in the manuscript is valid: the conditional covariance on the first coordinates is nonnegative by induction; conditional means remain increasing in the last bit; their covariance is $p(1-p)(u_1-u_0)(v_1-v_0)\ge0$. Iterating on finite event intersections gives probability at least $a_k(p)^X$ that all initially monochromatic edges have an eligible vertex.

Each edge is initially monochromatic with probability $2^{1-k}$, so linearity of expectation gives $\mathbb EX=m/2^{k-1}$ without an edge-independence assumption. Since $a_k(p)>0$ for $p>0$ and $x\mapsto a_k(p)^x$ is convex, Jensen yields the manuscript's first term

$$\Pr(\text{a surviving initial-color monochromatic edge})\le1-a_k(p)^{m/2^{k-1}}.$$

Empty $X=0$ uses the empty product $1$; $p=1$ gives $a=1$ and a constant function in Jensen. Neither case invalidates the argument. The theorem excludes $p=0$, so no $0^0$ convention is required.

## New-monochromatic events, actual directed pairs, and coefficient

Suppose $f$ is finally all blue and is not initially all blue. Its initially red vertex set is nonempty. Let $x$ be the last such vertex processed and flipped. An initially all-red edge $g$ containing $x$ is still all red immediately before this flip, by the algorithm. Because every vertex flips at most once, $g$ being all its initial color at that time means none of its vertices has previously flipped.

If another vertex $z$ were in $f\cap g$, then $z$ would be initially red and finally blue and hence would have flipped before $x$, contradicting the preceding fact. Thus $f\cap g=\{x\}$. In particular $f\ne g$ since $k\ge2$. This argument also covers an edge initially all red and finally all blue; it does not omit full color reversals. It is RS Claim 2.2 specialized to the actual blame witness.

For a fixed directed pair $(f,g)$ with unique intersection $x$, fix $t_x=t$ and initial red subset $S\subseteq f\setminus\{x\}$. The necessary event imposes:

- all $k$ vertices of $g$ initially red and exactly $S$ initially red in $f\setminus\{x\}$;
- $b_x=1$;
- each $z\in S$ eligible and earlier than $t$;
- no $z\in g\setminus\{x\}$ both eligible and earlier than $t$.

There are exactly $2k-1$ distinct vertices in $f\cup g$, so the prescribed initial configuration has probability $2^{-(2k-1)}$. The constrained eligibility/delay coordinates are disjoint after isolating $x$, giving exactly

$$2^{1-2k}p(pt)^{|S|}(1-pt)^{k-1}.$$

Vertices initially blue in $f\setminus\{x\}$ have no imposed later-trajectory condition in this upper bound. This omission enlarges the event and is therefore allowed. No sufficiency assertion about these local conditions is made.

The different $S$ prescribe mutually exclusive initial colors. Summing them gives the binomial factor $(1+pt)^{k-1}$. Integrating $t$ from $0$ to $1$ gives

$$2^{1-2k}p\int_0^1(1-p^2t^2)^{k-1}\,dt=2^{1-2k}J_k(p).$$

This matches the exact intermediate expression on RS printed p.7, before the source bounds the integral by $p$. There is no missing factor of $p$ in the manuscript's $J_k$: the substitution is $y=pt$, with $p>0$.

One red/blue-reversed bound doubles the expression to $2^{2-2k}J_k(p)=4^{1-k}J_k(p)$ per directed pair. The manuscript's $\gamma(H)$ already counts both orientations of each undirected single-intersection adjacency; no further orientation factor is needed. A union bound over the two colors and all these directed pairs is exactly the stated second term. Multiple possible blaming edges merely overcount the union and cause no issue.

Every failed final coloring contains a monochromatic edge, and every such edge falls in one of the two cases already bounded. Lemma 1 is consequently valid for each actual finite input hypergraph, before any structural reduction.

## Minimal-vertex quotient and the original object class

If any finite simple $k$-uniform non-B hypergraph with at most $M$ edges exists, its possible vertex counts form a nonempty set of nonnegative integers and have a least element. The selected counterexample has $m\ge1$ and $v\ge k\ge2$.

For two vertices that never occur together in an edge, the quotient identifying just these vertices is injective on every original edge. Each image edge therefore still has exactly $k$ elements. Taking the set of image edges removes any duplicates, leaves a finite simple $k$-uniform hypergraph, and cannot increase the number of edges. Any proper coloring of this quotient pulls back to a proper coloring of every original edge because each original edge maps bijectively onto its image edge. Thus the quotient must also be non-B and has $v-1$ vertices, contradicting minimality.

The selected counterexample is therefore pair-covering, and counting unordered vertex pairs yields

$$v(v-1)\le k(k-1)m\le k(k-1)M.$$

The nonnegative quadratic root gives $v\le v_k(M)$ after the floor. This is an internal reduction on the counterexample class; it adds no pair-covering hypothesis to the original theorem. No edge padding, fixed vertex count, or distinctness preservation of image edges is assumed. Deduplication is legitimate precisely because the budget is “at most $M$.”

## Self-contained graph cap

A clique of size $q$ in the actual single-intersection graph consists of $q$ actual $k$-edges with every distinct pair meeting in exactly one point. Their incidence Gram matrix is $(k-1)I_q+J_q$, positive definite since $k\ge2$. Thus $q\le v$.

In the complement graph $T$ on the $m$ original edges, choose the vertices that precede all their neighbors in a uniformly random permutation. The selected set is independent: two adjacent vertices could not each precede the other. Its expected size is $\sum_i(d_i+1)^{-1}$. Every such independent set is a clique in the single-intersection graph and has size at most $v$. Cauchy–Schwarz then gives

$$v\ge\sum_i\frac1{d_i+1}\ge\frac{m^2}{m+2|E(T)|}.$$

Since $m+2|E(T)|=m^2-\gamma(H)$, rearranging gives

$$\gamma(H)\le(1-1/v)m^2.$$

All denominators are positive: $m\ge1$ and $v\ge2$. Together with the simple-graph cap $\gamma(H)\le m(m-1)$, this proves the two actual caps, with no use of the exact Turan theorem or a finite table.

Both remain upper bounds after replacing the actual parameters by the budget: $m(m-1)\le M(M-1)$ and $(1-1/v)m^2\le(1-1/v_k(M))M^2$, because $m\le M$ and $2\le v\le v_k(M)$. Therefore $\gamma(H)\le g_k(M)$ exactly as stated. Note also $v_k(M)\ge k\ge2$ for every allowed $M\ge1$, so the theorem's defining denominator never vanishes.

## Closing the original quantified theorem

For the same selected counterexample, $0<a_k(p)\le1$ and $m\le M$ imply

$$1-a_k(p)^{m/2^{k-1}}\le1-a_k(p)^{M/2^{k-1}}.$$

Its integral is nonnegative, so $\gamma(H)\le g_k(M)$ also moves the second term in the correct direction. The actual failure probability is at most the budget expression, which is strictly below $1$. Thus success has positive probability and at least one final proper coloring exists. This contradicts non-B and eliminates every original finite simple input with at most $M$ edges. Empty-edge inputs are automatically properly colored and do not enter the counterexample argument.

## Composition with the $k\ge17$ gain

Take $M=B_{\rm RS}(k)$ and $N=M+1$. The gain manuscript has proved that $M$ is an actual accepted budget with an actual witnessing $p>0$ and $M\ge2^k$. Use

$$V=v_k(N),\qquad G=g_k(N).$$

One has $V>1$, $V\le1+k\sqrt N$, and $0\le G\le N^2(1-1/V)$ by their definitions and the bound for the quadratic root. Thus the analytic gain lemma makes Theorem A's criterion strict at budget $N$. Theorem A now proves all original inputs with at most $N$ edges colorable, yielding $m(k)\ge B_{\rm RS}(k)+2$ without the conditional interface assumption that appeared in the earlier gain manuscript.

The graph-cap function here is the real-valued coarse cap, rather than the exact integer Turan function used as an example in the earlier manuscript. This change does not weaken the analytic comparison's applicability: the gain lemma was stated for every nonnegative $G$ under the real-valued coarse cap, and Theorem A directly certifies this choice.

## Issues and remaining scope

No mathematical correction to the core theorem is requested. The source pairing is valid, every actual-to-budget step is connected, and the proof uses no unmentioned hypergraph condition. No finite computation or Lean execution was necessary for this interface audit.

This is a same-family review of the displayed derivation and cited local source, not cross-family acceptance, independent-machine reproduction, or a claim of literature novelty. The complete literature-envelope comparison and the project's specified external final reviews remain outside this report.
