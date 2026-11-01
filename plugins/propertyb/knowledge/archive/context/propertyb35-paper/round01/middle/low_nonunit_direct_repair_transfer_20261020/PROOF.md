# Direct low-nonunit-degree repair on21–25 points

## Theorem and exact scope

Let H be a simple five-uniform hypergraph on n vertices, with exactly35 original edges. Let Gamma have these35 original edge indices as vertices, joining two indices exactly when their intersection size differs from one.

The following sufficient conditions give a proper two-coloring of H.

1. **21<=n<=25, no degree hypothesis:** Gamma has an isolated vertex.
2. **21<=n<=23, no degree hypothesis:** Gamma has a degree-one vertex F whose unique Gamma neighbor G is disjoint from F.
3. Gamma has a degree-one vertex F with exceptional G satisfying |F intersect G|>=2, and some v in F intersect G has original H-degree at most9 when n=21 or22, or at most8 when n=23,24 or25.

In particular the complete Gamma-degree-at-most-one repair holds for n=21,22 with Delta(H)<=9, and for n=23 with Delta(H)<=8. On24/25 points with Delta<=8 it repairs every isolated Gamma vertex and every degree-one vertex whose exceptional pair overlaps, but the disjoint exceptional pair is not covered by the stated bounds.

No point-pair coverage, A1 role, edge-critical assumption, existing coloring, low-lock inventory or restriction on the external points is required. All probabilities below refer to the same original H and a single explicitly defined sample. This is a direct Property-B proof, not merely a necessary graph condition.

## 1. The common finite sample and general criterion

Fix an original edge F and a point v in F. Color v red and the other four points of F blue. Write N=n−5, and color a uniformly chosen r-element subset of the remaining N vertices red, all b=N−r others blue. The sample is nonempty, of size binom(N,r), and F is already proper.

Suppose s other original edges intersect F exactly once, and c of them meet F at v. Set

    alpha=binom(r,4)/binom(N,4),
    beta =binom(b,4)/binom(N,4),
    gamma=[binom(r,5)+binom(b,5)]/binom(N,5),
    delta=binom(N−8,r−8)/binom(N,r).

Invalid binomial coefficients are zero. An edge attached at v can only become all red, with probability alpha; one attached at a blue F-point can only become all blue, with probability beta. A five-edge disjoint from F has monochromatic probability gamma.

There is a useful uniform common-event deduction inside the c red-attached edges. Their outside four-sets are distinct because the original H is simple. For any two, the union has at most eight vertices. The probability that both are all red is therefore at least delta: for a fixed u-element union it is binom(N−u,r−u)/binom(N,r), decreasing in u. If r<8, the stated lower bound is merely zero and remains safe.

Choose any tree on these c event indices when c>=1. The elementary Hunter forest inequality gives

    Pr(at least one singleton-attached bad edge)
      <= c*alpha+(s−c)*beta−max(c−1,0)*delta.              (1)

All other singleton bad events are isolated vertices of this forest. To verify the inequality pointwise, if k event vertices are active, their induced forest has at most k−1 edges unless k=0; hence the sum of the active vertex indicators minus the active forest-edge indicators is at least the union indicator. Taking expectations proves (1). No bad-event independence or random choice of the tree is assumed.

For a Gamma-isolated F, s=34 and there is no other risk. The five attachment groups sum34, so choose v in a smallest group, with0<=c<=6. A sufficient criterion is

    max_{0<=c<=6}[c*alpha+(34−c)*beta−(c−1)_+*delta]<1.    (2)

For degree-one F with disjoint exceptional G, s=33 and again the smallest group has c<=6. Union-bound the single remaining event of G after (1): a sufficient criterion is

    max_{0<=c<=6}[c*alpha+(33−c)*beta−(c−1)_+*delta]
       +gamma <1.                                      (3)

For degree-one F with |F intersect G|>=2, choose v in the intersection. G then contains red v and at least one blue F-point, so it is automatically proper. All33 other edges are singleton-attached, and the group at v has **exactly** c=d_H(v)−2 edges: F and G are the other two original edges through v. A sufficient criterion is therefore

    c*alpha+(33−c)*beta−(c−1)_+*delta<1.                 (4)

For a degree bound d_H(v)<=D one may safely maximize the expression over0<=c<=D−2. These criteria establish a positive chance that every original edge is proper; the sample coloring itself is the desired H-coloring.

## 2. Every isolated Gamma vertex is repairable through25 points

The following table uses (2), with the maximum over all integers c=0,...,6. Each entry is an exact common-sample upper bound, strictly below one.

| n | N | outside red r | outside blue b | failure upper bound |
|---:|---:|---:|---:|---:|
|21|16|10|6|259/286|
|22|17|10|7|4531/4862|
|23|18|11|7|3773/3978|
|24|19|12|7|12425/12597|
|25|20|12|8|25141/25194|

The last two rows are a real gain from the **same** red-event tree. Their bare union bounds are not strict for the displayed sample, so dropping the tree deduction would not prove them. The25-point margin is53/25194>0; no rounding of that margin is used.

This proves part1 of the theorem without any original maximum-degree assumption.

## 3. A disjoint exceptional neighbor through23 points

For condition(3), the exact strict rows are:

| n | outside red r | outside blue b | complete failure upper bound |
|---:|---:|---:|---:|
|21|10|6|7659/8008|
|22|10|7|2337/2431|
|23|11|7|5269/5304|

The added gamma includes **both** colors of G; it was not made proper by the one-red/four-blue coloring on F. This proves part2. No assumption on vertices of G or disjointness between G and any other edge is used.

For the same safe general bound, minimizing over the integer outside sample parameter r>=ceil(N/2) on24 and25 points gives respectively78007/75582 and26155/25194, both greater than one. These are failures of this bound, not signed or original-H counterexamples, and do not exclude a stronger treatment of the same original G event. No further domain or configuration was searched.

## 4. Overlapping exceptional neighbor and the22-point equality

For n21 and22 with d_H(v)<=9, maximize(4) over c=0,...,7:

| n | outside red r | outside blue b | failure upper bound |
|---:|---:|---:|---:|
|21|9|7|701/715|
|22|10|7|2404/2431|

The22-point row is especially simple. Here alpha=210/2380, beta=35/2380. If c<=6 the bare union bound is strict. If c=7, its bare sum is exactly

    7*210/2380+26*35/2380=1.

There are seven actual red-attached edge events. Every pair of their outside four-sets has union at most eight, while r=10, so every such pair has positive joint probability. A single pair deduction would suffice to make the union strict. The uniform tree on the seven events gives six deductions, each at least

    binom(9,2)/binom(17,10)=36/19448.

The original union count is19448, and the tree deduction is216; thus failure<=19232/19448=2404/2431<1. All seven events and all deductions refer to the same H and the same balanced outside sample. Even if some outside four-sets intersect in additional points, this only increases the joint deduction.

For23–25 points, the condition d_H(v)<=8 gives c<=6 and the following strict bounds from(4):

| n | outside red r | outside blue b | failure upper bound |
|---:|---:|---:|---:|
|23|11|7|2485/2652|
|24|11|8|12440/12597|
|25|12|8|8259/8398|

In fact the24-point bare union at c6 already equals645/646<1, while the25-point bare value324/323>1 requires the tree. This proves part3 and the combined corollaries in the theorem statement.

For d_H(v)<=9 on23–25 points, this uniform alpha/beta/delta bound does not become strict for any tested integer sample parameter r>=ceil(N/2); its minimum1 includes the degenerate all-red outside sample. This is only a boundary of the stated common-event lower bound. Neither degree9 impossibility nor a non-B H is inferred. The criterion(4) remains available with the actual attachment count c or with stronger actual joint intersections.

## 5. Exact checks, commands and review boundary

CHECK.py uses only binomial coefficients and Fraction. It checks the selected table values, scans the finite outside-red parameter r and finite attachment counts c, and independently verifies the22-point integer counts. The entire computation takes about0.006 CPU seconds. No hypergraph, outside-set arrangement, locking table, graph optimizer, solver, Lean or MCP was used.

The complete scalar output is CHECK.json. Its finite parameter scan is merely a check of the displayed explicit bounds; the proof of actual H coverage is §§1–4. The two strict transfer corollaries are **21/22 with Delta<=9** and **23 with Delta<=8** for any Gamma-degree<=1 node. The no-degree isolated-node theorem holds on all21–25 points. The exceptional disjoint neighbor on24/25 remains outside the proved general repair scope.

Reproduction:

```sh
python3 -B context/propertyb35-paper/round01/middle/low_nonunit_direct_repair_transfer_20261020/CHECK.py
```

This new transfer proof awaits root's independent read and any designated cross-family review. It does not declare A1, an entire vertex-count branch or the36 target proved. The previously completed21-point theorem is an exact special case with an optional sharper red-tree count; the derivation here supplies the original-H interface rather than importing a generic probability score as a premise.
