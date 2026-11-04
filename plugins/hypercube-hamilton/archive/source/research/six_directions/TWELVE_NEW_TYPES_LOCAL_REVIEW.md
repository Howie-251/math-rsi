# Independent ARIS proof review: 111 new marked Q5 local inputs

2026-11-01. Fresh reviewer: `/root/higher_forced_cherry_review`, explicitly user-directed GPT-6.1-sol/high under ARIS proof-checker. The reviewer did not produce this package. **Verdict: PASS modulo the explicit primary matching-connectivity rank theorem.** Review independence: **same-family**. Acceptance: **provisional**. No mathematical gap remains in these 111 explicit positive local theorems. No producer or production-state artifact was changed.

## Exact accepted domain

The accepted list is exactly the 111 ordered indices in `TWELVE_NEW_TYPES_greedy_registry.json`, as frozen in `TWELVE_NEW_TYPES_LOCAL_MANIFEST.json`. For every listed index, its minority, majority and marked omissions agree exactly between registry, source summary and config. The review JSON records all 111 actual marked geometries directly.

For each such pair (H,U), and every arbitrary perfect matching F of the complete graph on K=V(Q5) minus H, there is a simple cycle on precisely V(Q5) minus U containing F, with every edge outside F a Q5 edge. Required edges may be long or same-parity. The same conclusion holds for any common cube-automorphic image of the marked pair (H,U).

| Type | Audited inputs | Minority/majority | Omissions | Covered terminals N | Rank R | Short edges/forest | Cycle vertices |
|---|---:|---:|---:|---:|---:|---:|---:|
| T28 | 51 | 2/8 | 3 | 22 | 1024 | 18 | 29 |
| T19 | 31 | 1/9 | 4 | 22 | 1024 | 17 | 28 |
| T84 | 17 | 0/8 | 4 | 24 | 2048 | 16 | 28 |
| T105 | 12 | 0/10 | 5 | 22 | 1024 | 16 | 27 |

Only these explicit local inputs are accepted. The greedy registry's coverage counts, optimality, application to a Q6 residual, exhaustive geometry/orbit claims, other producer full-rank records, and all deficient/negative classifications are outside this audit. The names of the four types do not imply unrestricted theorems for those types. No complete twelve-hole Q6, higher Q6 layer or full P6 is accepted here.

## Frozen inputs and review independence

The proof SHA256 is `a05a78d01f589be918d9006ef04c145c0a1343b263aaf44424ba062d91dc9829`; manifest SHA256 is `d7a843b54c6e534e0d94ec2813ca71c7e2ed3bf53f034dc3c10c66c704a7c98e`. All **901** declared file hashes were independently checked and remain unchanged after review. The registry contains 111 distinct indices and exactly 111 matching geometry rows, in the frozen order. The summary's index mapping is unique; the chosen source row/prefix and config were checked directly for every selected index. Producer `rank` and `full_rank` fields are consistency data only; acceptance comes from the independent reconstruction below.

The independent checker mechanism is the reviewer-authored DSU / ascending-pivot verifier previously used for the T37 audit, generalized explicitly to dynamic N=22/24 and R=1024/2048. It neither includes nor runs any producer forest search or alternating-connectivity traversal. In particular, it does not substitute the prior audit's rank results for the new data: every selected forest, bit and rank was recomputed in this package.

Reproduction in this directory:

```
g++ -std=c++17 -O3 TWELVE_NEW_TYPES_LOCAL_REVIEW_check.cpp -o TWELVE_NEW_TYPES_LOCAL_REVIEW_check.exe
./TWELVE_NEW_TYPES_LOCAL_REVIEW_check.exe
```

The explicit input geometry table is `TWELVE_NEW_TYPES_LOCAL_REVIEW_geometries.txt`; it was independently generated and checked against the frozen source registry/summary/config. The checker validates config equality again. Exact dimensions and accepted marked sets are stored in the precheck and final JSON, so reproduction does not rely on a mutable interpretation of type names. The C++ source, executable, geometry table and results are hashed in the final review.

## Complete independent finite checks

For each selected input, the checker enforces exact byte lengths: R forest records of 2E bytes, R row-pairing and column records of N bytes, and R matrix/pivot/combination records of R/8 bytes. Vertices are unsigned bytes and matrix bits are little-bit-first. Runtime checks are explicit and are not compiler-removable assertions.

All **131072** supplied forests were independently checked. Every one consists of the stated number E of distinct cube edges, with labels in 0..31 and one-bit endpoint XOR. A DSU rejects cycles independently of degree checking. Every covered vertex has degree one, every included hole degree two, and each omission degree zero. Every retained vertex is therefore present. The DSU components pair exactly two covered endpoints each, giving N/2 paths. Derived endpoint pairs equal their stored records after orientation/order normalization, and only the independently derived pairs are used in connectivity reconstruction.

Every one of the **131072** matching columns was validated as a perfect matching on exactly K: no self-pair, repeated endpoint, missing endpoint or extra vertex is permitted. Required columns need not be short or bipartite. There is no need to assume the producer generated a particular canonical basis; any legal columns with independently checked full rank suffice.

For every selected forest row and matching column, the independent checker joins the independently derived row pairs and the validated column pairs in DSU. Their labeled union is 2-regular, so connectivity is equivalent to a single alternating cycle. All **169869312** reconstructed bits agree with the frozen matrices. This method does not follow the producer's alternating traversal. Common matching pairs remain labeled two-edge components and fail full connectivity on these N>=22 terminal domains.

Fresh ascending-pivot GF(2) Gaussian elimination on the **reconstructed matrices** gives exact rank 1024 for every selected T28/T19/T105 input and exact rank 2048 for every selected T84 input. The checker does not use producer pivots or combination vectors for that independent rank computation.

As a further check, all **131072** supplied pivots have exactly the indicated highest set bit, and every one equals the XOR of reconstructed matrix rows named by its supplied combination vector. These additional equations pass; they are not the source of the independent rank verdict.

| Type | Forests/columns checked | Connectivity bits rebuilt | Exact rank of every selected matrix |
|---|---:|---:|---:|
| T28 | 52224 | 53477376 | 1024 |
| T19 | 31744 | 32505856 | 1024 |
| T84 | 34816 | 71303168 | 2048 |
| T105 | 12288 | 12582912 | 1024 |
| Total | 131072 | 169869312 | — |

The complete per-index results are in `TWELVE_NEW_TYPES_LOCAL_REVIEW_check.json`. This is exhaustive verification of all claimed finite positive certificates, not a sample, a producer-metadata check, or an exhaustive search over all possible original matchings.

## Primary import and mathematical obligation ledger

The sole external mathematical import is the general matching-connectivity GF(2) rank bound from [Cygan–Kratsch–Nederlof, Corollary 3.5](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf). The primary manuscript was checked in this reviewer's preceding local audit: its matrix is indexed by **all** perfect matchings of a complete graph and its rank is 2^(N/2-1) for every even N>=2. Consequently the required upper bounds are 1024 at N=22 and 2048 at N=24. No bipartite restriction or real-field rank assertion is imported. The frozen primary-source note is also hash-bound by this manifest.

**MC1 — marked-set legality and dimensions.** For every selected row, minority and majority vertices are disjoint, distinct and lie in 0..31; each nonempty parity class has the stated common parity, and the two nonempty classes have opposite parity. U consists of the stated number of distinct majority holes. Empty minority sets in T84/T105 are handled explicitly, not normalized using a nonexistent minority vertex. N=32-|H|, R=2^(N/2-1), and 2E=N+2(|H|-|U|) agree with the statement. Configs contain the exact sorted H followed by the marked omissions.

**MC2 — short-complement forest decomposition.** The verified forest has no cycles, maximum degree two, degree-one set exactly K and no degree-zero retained vertex. Every nontrivial connected component is therefore a path with exactly two covered endpoints; there cannot be a hole-only cycle component. The paths are vertex-disjoint and cover all 32-|U| retained vertices. The resulting P(S) is a perfect matching on K. This discharges the graph hypotheses used to compress S.

**MC3 — matching-connectivity interpretation.** The union of two perfect matchings on K, retaining edge labels, is a 2-regular multigraph. It is a single alternating cycle iff connected. DSU computes that property correctly, including the failure caused by a shared pair making a proper two-edge component. Thus the independently reconstructed matrix is a genuine restriction of the imported complete matching-connectivity matrix, not a matrix of a different predicate.

**MC4 — lower bound for complete rows.** A dependence among the selected complete matching-connectivity rows would persist after restricting to the supplied columns. Exact rank R of the reconstructed R-by-R submatrix excludes such a dependence, so the corresponding full rows are independent over GF(2).

**MC5 — full row-space span.** The generic imported full-matrix rank upper bound is R over the same field. R independent selected full rows therefore span the entire row space. This step, not merely square-submatrix nonsingularity, is what extends the conclusion from the supplied columns to every arbitrary perfect matching F.

**MC6 — nonzero arbitrary columns.** Write any F as edges (a_i,b_i) for i=1..N/2. Pair b_i with a_(i+1) cyclically. This is another perfect matching on exactly K, and its union with F is a single alternating cycle. Hence every F column of the full matrix is nonzero, regardless of shortness or parity of its edges.

**MC7 — universal selected-forest witness.** If all selected full rows vanished at this F column, all rows in their span would also vanish, contradicting MC6. Some selected P(S_i) therefore connects with F. The finite forest family is fixed per marked geometry; the choice of connecting forest may depend on F. This is exactly the required quantifier order.

**MC8 — simple-cycle expansion and shortness.** Expand the selected pairing edges to their actual disjoint forest paths. Their interiors lie in H minus U and are disjoint from F and one another, so connectedness and degree two are preserved on exactly the retained vertex set. A physical edge shared by F and S would be a one-edge forest component whose K endpoint pair is also in F, giving a proper labeled two-edge component. Since N>=22 this contradicts connectivity. Thus expansion does not reuse a physical edge and gives a simple cycle on the stated 29/28/28/27 vertices. Every edge outside F belongs to the checked short forest.

**MC9 — common automorphic images.** Given a matching on the image of K, pull it back through the inverse cube automorphism, apply MC7–MC8, then push the cycle forward. The image contains all required edges, every new edge remains short, and the omitted set is exactly the image of U. H and U move together; no theorem about an unmarked hole set is substituted. This argument does not require an exhaustive orbit classification or independent coverage calculation.

Dependency DAG: explicit selected marked geometry -> independent legal forests and endpoint matchings -> complete connectivity submatrix reconstruction -> independent GF(2) rank lower bound + generic primary rank upper bound -> full row span -> nonzero arbitrary-column coverage -> simple-cycle expansion -> automorphic images. The DAG is acyclic and contains no Q6 coverage or desired twelve-hole theorem.

## Adversarial boundary audit and scope limits

The checks explicitly reject nonshort edges, self-pairs, repeated forest edges, cycle components hidden by correct degrees, nonzero omitted degrees, wrong stored endpoint pairings, malformed arbitrary columns, wrong bit order and incorrect pivot combinations. The mathematical proof separately rejects a shared physical matching/forest edge and guards the transition from restricted columns to arbitrary F with the global rank upper bound. Empty minority sets, N=24/R=2048 dimensions and odd retained-cycle lengths are handled correctly; arbitrary required matching edges are essential and are never restricted to short or bipartite ones.

No asymptotic estimate, probability-mode transition, interchange or unstated limiting regime occurs. No geometry census, unproved normalization, greedy optimality, deficient-rank negative inference or Q6 predecessor argument is required. There are no open FATAL, CRITICAL, MAJOR or MINOR mathematical issues in these 111 explicit positive local claims. Application to actual Q6 geometries, coverage/union counts, other producer positive cases, and all complete-layer/P6 claims remain separate gates.
