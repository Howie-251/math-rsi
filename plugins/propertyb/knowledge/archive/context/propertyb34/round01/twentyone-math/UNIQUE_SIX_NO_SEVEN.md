# The 21-vertex unique-six, no-seven branch

2026-10-13. **Complete paper candidate for this branch**, with independent exact local arithmetic checks; not yet formalized in Lean. Original claim: a simple pair-covering five-uniform hypergraph H on 21 vertices, with 34 edges, a unique degree-six vertex x and all other degrees at least eight, has Property B.

The previous complete reduction is frozen at `context/propertyb34-hour1-20261013/low-math/TWENTYONE_SIX_REDUCTION.md`, with its 61 strict local witnesses independently checked in `TWENTYONE_SIX_REDUCTION_VERIFIED.json`. We use its actual-input argument and close the previously open equality case here. The parent proof must retain that entire reduction; this note alone does not replace it.

## 1. The actual equality case

If none of the earlier strict selected profiles gives Property B, the degree sequence is $6^1,8^{16},9^4$. There are disjoint sets U, B, C of sizes 12, 4, 4 respectively, plus x, such that:

- Points in U and B have degree eight, and points in C have degree nine.
- $\lambda(x,u)=1$ for each $u\in U$, $\lambda(x,b)=2$ for each $b\in B$, and $\lambda(x,c)=1$ for each $c\in C$.
- Each pair of distinct U points has codegree two.
- Every edge through x contains exactly two U points.

These are necessary actual incidence identities, not merely a list of hypothetical local counts.

## 2. An additional codegree identity at each U point

Fix $u\in U$. Double-count the pairs $(e,w)$ with $u,w\in e$ and $w\ne u$. Since $d(u)=8$, the sum of all codegrees from u is $4d(u)=32$. Its eleven U neighbors contribute 22, and x contributes one. Consequently

$$\sum_{z\in B\cup C}\lambda(u,z)=32-22-1=9.$$

There are eight terms and all are positive integers by pair coverage. Exactly one is two and the remaining seven are one. In particular

$$1\leq\lambda(u,b)\leq2\quad(u\in U,\ b\in B).$$

## 3. Select four locks from one actual edge

Choose any $b\in B$. Because $\lambda(x,b)=2$, an edge e containing x and b exists. The equality case gives precisely two U points u,v in e. Choose the four distinct locks in the order $(x,u,v,b)$.

Their degree tuple is $(6,8,8,8)$. In the pair order $(xu,xv,xb,uv,ub,vb)$ the codegrees are

$$(1,1,2,2,a,c),\qquad a,c\in\{1,2\}.$$

The common-four-point multiplicity is exactly one: e witnesses positivity, and the unit codegree $\lambda(x,u)=1$ bounds it above by one. In exact-trace notation, every triple containing x has multiplicity zero after excluding the four-point trace. The only potentially nonzero exact triple is uvb. It is at most one since $\lambda(u,v)=2$ and the four-trace has consumed one. It can be one only if a=c=2.

Thus precisely the following five local profiles cover the actual selected input:

| a | c | Exact uvb triple count | Common-four count | Strict failure upper bound |
|---|---|---|---|---|
|1|1|0|1|24231/24310|
|1|2|0|1|12152/12155|
|2|1|0|1|12152/12155|
|2|2|0|1|12013/12155|
|2|2|1|1|23759/24310|

All five bounds are strictly less than one. The existing conditional-permutation coloring lemma therefore supplies a proper two-coloring. This closes the equality case and, combined with the frozen reduction, the whole unique-six/no-seven branch.

## 4. Arithmetic and proof obligations

`equality_quad.py` generates exactly the five profiles and selects strict layouts using the existing avoided-lock quota method. `EQUALITY_QUAD.json` stores exact counts, positions, rational dual coefficients, all A/B/C rows and bounds. `verify_exact.py EQUALITY_QUAD.json` independently recomputes A/B/C using labelled injections; checks actual degrees and 34-edge binding; checks all quota coefficients and the complete unordered-slot capacity domain; and confirms the strict rational bounds. `EQUALITY_QUAD_VERIFIED.json` records five successful checks. The computation took less than a second and is a finite local formula verification, not enumeration of 21-vertex hypergraphs.

The remaining cross-model questions are precise: (i) does the frozen reduction really force the stated equality case; (ii) is the extra codegree identity sufficient to force a,c in {1,2}; (iii) is q=1 with only the listed possible exact triple exhaustive; (iv) are the avoided-lock deductions valid for actual bad edge pairs and the conditional probability event. The first and fourth reuse mathematical interfaces, while the new logical closure is Sections 2–3.

This result leaves other degree-six configurations, as well as minimum degrees seven and eight, open. It does not establish the full 21-point branch or T34.
