# Three-intersection middle saturation with four units of high-degree excess

## Conditional theorem

Let H be a simple five-uniform hypergraph on 21 vertices with 35 edges. Let G,J be two original edges with |G∩J|=3, and write

\[
A=G\setminus J=\{a,b\},\qquad B=J\setminus G=\{c,d\}.
\]

Assume every point-pair within A∪B has codegree at most four, and

\[
\sum_{v\in A\cup B}\max(d_H(v)-9,0)\le4.                 \tag{1}
\]

If at least 15 original edges F satisfy

\[
F\cap G=\{g\},\qquad F\cap J=\{j\},\qquad g\ne j,
\]

then H has Property B. No minimum or maximum vertex degree, point-pair coverage, A1 degree-role assumption, or bound on the number of degree-seven points is an additional hypothesis. In fact, saturation itself forces the four selected points to have degree at least eight.

In particular, if all original point-pairs have codegree at most four and the global sum Σ_v max(d_H(v)−9,0) is at most four, a non-B H satisfies

\[
c(G,J)\le14\quad\hbox{for every pair }|G\cap J|=3,
\qquad C_3\le14n_3.                                      \tag{2}
\]

The global degree/codegree assumptions in this last consequence must be established separately for any intended A2/A3 application. This note proves the conditional gate, not those imports or a complete vertex-count branch.

## Actual H to the complete small domain

Give A the bit labels 0,1 and B the bit labels 2,3. Let μ_T count the original edges with exact intersection T with A∪B. The original distinguished edges give

\[
\mu_3\ge1,\qquad\mu_{12}\ge1.
\]

Every valid middle F has exact trace one of the four cross pairs 5,6,9,10. Indeed its two attachment points must lie respectively in G\J and J\G. A point of G∩J would be in both singleton intersections and violate their distinctness. Conversely, a cross-trace edge may also meet G∩J and fail the middle condition; no converse is assumed. Thus, with

\[
a_T=\mu_T\ (T=5,6,9,10),\qquad t=\sum_T a_T,
\]

we have t≥c(G,J)≥15. Each a_T is at most four, so t=15 or 16. Consequently the four a_T are either all four, or three fours and one three. The inclusive cross-pair spare capacity is 16−t≤1. Any triple trace consumes two of these spare slots, and a quadruple trace consumes four. Hence there are no triple or quadruple traces at all.

Only the empty trace, four singletons, two same-side pairs and four cross pairs remain. The same-side inclusive pair caps now give μ_3,μ_12∈{1,2,3,4}. Every cross row/column has sum at least seven. Adding the distinguished same-side edge gives d_H(v)≥8 for all four selected points. Hypothesis (1) therefore places the selected degrees in {8,…,13} and bounds their total incidence by 40.

A complete necessary inventory is specified by:

1. the five choices for the four cross counts (all fours, or one specified three);
2. the two same-side counts in {1,…,4};
3. nonnegative singleton counts such that each selected degree is at most 13 and the sum in (1) is at most four;
4. the forced empty count μ_0=35−Σ_{T≠0}μ_T, required nonnegative.

These conditions are a relaxation, not a claim that every inventory has an actual completion. In particular, no unproved degree restriction or free-vertex realization is used to exclude an actual H.

There are 1303 labeled inventories, grouped into 183 representatives under the order-eight group that swaps within A, within B, and interchanges A,B. The full counts are:

| Cross total t | Labeled inventories |
|---|---:|
| 15 | 1200 |
| 16 | 103 |

The action transports every point degree and every exact trace multiplicity. It preserves the unordered marked pair {A,B}. An actual H may be relabeled into the corresponding inventory representative; an automorphism of H is not required.

## Strict zero-deduction certificates and original coloring

Use the conditional permutation theorem from [PROBABILITY_LEMMAS.md](../../../../../proofs/PROBABILITY_LEMMAS.md). For each representative the saved layout puts the four selected points at four distinct positions of a 21-vertex permutation, and uniformly permutes the other 17 vertices. The exact bound is

\[
\sum_{k=1}^{21}\min(A_k,B_k,C_k),                       \tag{3}
\]

with **every link-overlap quota and deduction set to zero**. Thus no point-pair coverage, low center, or A1 quota formula is imported. The A/B endpoint events and C critical ordered pairs are computed from the same 35 original edge indices, retaining the exclusion of equal edge indices. Even when two indices have identical selected traces, they remain two distinct original edges in this computation.

All 183 saved certificates are strict. Grouping representatives by their maximum selected degree gives:

| Maximum selected degree | Representatives | Maximum bound (3) |
|---|---:|---:|
| 9 | 4 | 1349/2145 |
| 10 | 42 | 2381/3060 |
| 11 | 90 | 242713/291720 |
| 12 | 38 | 67553/87516 |
| 13 | 9 | 40787/58344 |

The overall maximum is 242713/291720<1. One inventory attaining it has degree tuple (9,10,10,11), layout (9,10,20,21), and exact nonzero counts

\[
\mu_0=15,\ \mu_3=2,\ \mu_5=3,\ \mu_6=4,\ \mu_9=4,\ \mu_{10}=4,\ \mu_{12}=3.
\]

The strict probability bound supplies an actual permutation outside the failure event of the greedy recoloring algorithm: start all vertices red, and process the permutation, turning a vertex blue when it is the last vertex of an edge still wholly red. Outside the theorem's critical events every original edge retains both colors. Applying the representative's layout after relabeling the same actual H therefore produces an original-H proper coloring. This proves the conditional theorem and (2).

## Independent completeness and arithmetic evidence

[PILOT.py](PILOT.py) generates inventories cross-first and singleton-first. It solves the complete four-lock position problem with zero deductions, and independently replays each selected layout using injection probabilities. Its result is [RESULT.json](RESULT.json); measured CPU was 1.830233 seconds, including complete domain generation and all 183 cases. [PROFILE.json](PROFILE.json) records the domain counts.

[VERIFY.py](VERIFY.py) does not import the discovery generator or the position solver. It starts with each degree tuple in {8,…,13}^4 satisfying (1), chooses the five cross possibilities and the two same-side counts, and recovers singleton counts by subtraction. The forced empty count completes the inventory. It checks equality of all 1303 full labeled keys with the discovery result. It independently builds the marked-pair group from three binary choices and checks all 183 full transported representative keys.

For each representative it expands all 35 original edge indices, checks the selected degrees and all 21 injection-probability rows, and recomputes (3) with zero deductions. The implementation is independent of the subset-position optimization and processes 1190 ordered distinct original-index pairs per case. [VERIFY.json](VERIFY.json) is PASS, maximum 242713/291720, CPU 1.342588 seconds.

This is a finite exact local-inventory proof, not an enumeration of H. The mathematical interface is strictly wider than the old degree-at-most-nine near-saturation domain. Only t≥15 is covered here: no t=14 high-degree extension, x-star expansion, or unrestricted high-trace inventory was generated. Deterministic and mathematical checks here are same-family/provisional; designated cross-family review remains separate.
