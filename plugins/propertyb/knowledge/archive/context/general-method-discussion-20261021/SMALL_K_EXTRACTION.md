# Existing small-k material: exact scope and general mechanisms

Read-only extraction, 2026-10-21. No research computation, certificate rerun, Lean, new Goal, or public-record search was performed. The m(5)≥36 Goal remains paused. Sources are the supplied local manuscripts and the existing transfer note; attribution remains with their authors.

## 1. Exact numerical statements and evidence level

All statements concern arbitrary **finite simple k-uniform hypergraphs**. Pair coverage is a reduction of a minimum-vertex counterexample, not an assumption of the original problem.

| k | Supplied lower bound | Maximum colorable edge budget M | Candidate vertex interval | Original profile count |
|---|---:|---:|---:|---:|
|6|m(6)≥65|64|27–42|200|
|7|m(7)≥130|129|37–73|115|
|8|m(8)≥266|265|47–120|1,290|
|9|m(9)≥542|541|57–194|2,568|
|10|m(10)≥1112|1111|67–316|28,545|
|11|m(11)≥2275|2274|79–500|70,472|

Sources: `propertyB_small_k/propertyB_m6_proof.md`, `propertyB_m7_proof.md`, `propertyB_k8_k9_proof.md`, `propertyB_k10_k11_research.md`. The last two explicitly call the results computer-assisted proof candidates, without independent peer review or Lean verification. The existing `research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md` records earlier local replay of all 103,190 original profiles; that replay is **not** a new independent implementation, and this extraction did not repeat it. That reading/replay was same-family/provisional. No claim about current published records follows here.

m(5)≥34 is the project's completed formal result; m(5)≥36 is not established. The k≥6 material must not be presented as completing it.

## 2. General lemmas already proved in the supplied text

**Reduction (all k).** Identifying two vertices in no common edge preserves uniformity and noncolorability. A minimum-vertex counterexample therefore has λxy≥1 and

\[
(k-1)d(x)\ge v-1,\qquad vd_0(v)\le kM,
\quad d_0(v)=\lceil(v-1)/(k-1)\rceil.
\]

Balanced coloring excludes v whenever

\[
M\,[\binom{\lfloor v/2\rfloor}k+\binom{\lceil v/2\rceil}k]/\binom vk<1.
\]

Padding to exactly M distinct edges requires **C(v,k)≥M**, checked in the supplied numerical intervals. A fully general formulation must retain that condition or process actual m≤M; theorem A's proof expressly acknowledges this.

**Conditioned-permutation certificate (any k≥3, any lock set).** The greedy algorithm's failure implies ordered edges A,B with A∩B={x} and max A=min B=x. Exact lock traces T have multiplicities ℓT. For each position h, A_h/B_h sum exact edge-end/start probabilities; C_h uses all distinct ordered pairs with type multiplicities ℓT(ℓU−1[T=U]) and the exact critical-pair weight w_h(T,U). Noncritical bookkeeping terms are nonnegative.

At a locked center j, at least

\[
q_j=\left\lceil\frac{(k-1)d(x_j)-(v-1)}{k-2}\right\rceil
\]

unordered incident-edge pairs meet again. Type-cell capacities are C(ℓT,2) or ℓTℓU. Taking the q_j cheapest removable weights w_h(T,U)+w_h(U,T), **including zero weights**, gives D_h; set D_h=0 at free positions. Thus

\[
\Pr(\mathrm{Fail})\le U=\sum_h\min(A_h,B_h,C_h-D_h).
\]

U<1 implies a proper coloring. For no locks, subtract at least 2Q ordered candidates, where

\[
Q=\max\{0,\lceil[M\binom k2-\binom v2]/\binom{k-1}2\rceil\}.
\]

Sources: k8/9 §§1–2; k10/11 theorem A and its mathematical foundation.

**Two-lock existence.** For a minimum-degree vertex of degree d, at least s_d=2(v−1)−(k−1)d other vertices have codegree 1 with it. When s_d>0, let B≥d be the least integer satisfying vd+s_d(B+1−d)>kM. Then some such neighbor has degree in [d,B]. Source: k8/9 §3; k10/11 theorem A.

**Arbitrary-number lock existence (already general).** For pair-covering simple k-uniform H with exactly M edges, choose integer D≥d0 and define

\[
Z=(D+1)v-kM,\qquad T=(k-1)(D+1)-v+2.
\]

For every integer s≥2,

\[
Z>0,\qquad4(k-1)Z>(s-1)T^2
\]

guarantee s vertices of degree ≤D with **all pairwise codegrees exactly 1**. Proof: the conflict graph on low-degree vertices has 2e≤(T−1)r−(k−1)Z; Caro–Wei and Cauchy give α≥r²/[Tr−(k−1)Z], and completing the square gives α>s−1. This is k10/11 **theorem B**, not a new conclusion of this discussion. The k8/9 §4 version is s=3.

For unit-codegree locks, traces of size ≥2 form a clique decomposition of K_s, each occurring exactly once. Singletons and the empty trace are reconstructed from degrees. Three locks have only two forms: one triple block or three pair blocks. For s≥4 the complete clique-decomposition domain must be handled; unit codegrees alone do not provide the subsequent coloring certificate.

## 3. What remains parameter-specific; what is not yet asymptotic

The general finite-certificate theorem is **already stated** in k10/11 theorem A: every surviving v must be covered by a 0/1/2/3-lock branch, and every admissible degree/trace profile in that branch must satisfy U<1. Specific budgets M, vertex cutoffs, degree thresholds D(v), chosen central lock positions, and strict rational inequalities are finite instantiations. k6–11 use at most three locks; s≥4 is only a general structural input in these supplied computations.

The material proves no all-k numerical lower-bound function beyond this conditional certificate criterion, and no asymptotic improvement. Such an improvement would need a **uniform-in-k analytic bound on U plus selection/coverage for every surviving v**, with explicit margins; finitely many successful k do not supply those estimates. Directed integer rounding and cached weights improve certificate execution, not the asymptotic mathematical bound by themselves.

The existing transfer note also records a real limit: k=5,M=35,v=25,D=7 guarantees five unit locks by this sufficient criterion; its six-lock inequality fails for every D. This does not prove six locks impossible. Three central degree-7 locks give U>1 in both trace forms, so the unchanged three-lock certificate does not settle the paused k=5 problem.
