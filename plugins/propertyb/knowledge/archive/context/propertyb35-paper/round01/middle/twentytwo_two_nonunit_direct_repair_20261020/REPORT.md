# Twenty-two vertices: two non-singleton intersections at one edge

**Current strengthening (§6).** The analytic seven-four-set forest lemma closes types A and B below without any degree or covering hypothesis. Consequently every22-vertex/35-edge simple five-uniform H with qΓ(F)=2 and maximum degree at most10 is two-colorable. Only the general types C,D,E remain in this report. Sections1–5 retain the complete original single-sample calculation and its first-stage consequences.

Let H be a simple five-uniform hypergraph on 22 vertices with 35 edges. Define Γ on its original edges by joining distinct edges whose intersection size is not one. Suppose an original edge F has Γ-degree exactly two. This note proves that H is two-colorable in either of these ranges:

1. maximum vertex degree at most 8, with no covering or minimum-degree hypothesis;
2. pair covering, minimum vertex degree at least 7, and maximum degree at most 9.

The proof uses only the Γ-degree of F. It makes no assumption about the Γ-degrees of its two exceptional neighbors. The unrestricted local residuals of this method are listed below; they are not hypergraph counterexamples. This is a same-family, provisional mathematical check, not cross-family acceptance or a proof of the global bound.

## 1. The actual edge partition and one common sample

Write the exceptional edges as G,H, and put T1=G∩F and T2=H∩F. Their sizes belong to {0,2,3,4}: size five is excluded by simplicity. The other 32 original edges each meet F in exactly one point. Let a_i count those attached at i∈F, so Σa_i=32. If m_i is the number of T1,T2 containing i, then

\[
d_H(i)=1+a_i+m_i,\qquad \sum_{i\in F}d_H(i)=37+|T_1|+|T_2|.
\]

Fix v∈F red, color F\{v} blue, and choose uniformly an r-element red subset of the other 17 vertices. All original edges, including F,G,H, are handled in this same sample. Let c=a_v, and interpret binomial coefficients outside their range as zero. The sample size and singleton-edge numerators are

\[
D=\binom{17}{r},\quad R=\binom{13}{r-4},\quad B=\binom{13}{r}.
\]

A red-attached edge is bad precisely when its external four-set is all red. A blue-attached edge is bad precisely when its external four-set is all blue. For two red-attached edges, their external union has size at most eight. Thus their simultaneous bad-event probability is at least

\[
J/D,\qquad J=\binom9{r-8}.
\]

For c≥1, take any tree on those c indexed red-attached edges. Pointwise, the number of occurring vertices of a tree minus the number of occurring tree edges is the number of components of its induced forest, and is at least the indicator that some vertex occurs. Hence the union of the c bad events is at most their sum minus the tree joints. This gives the valid bound

\[
U(v,r)=cR+(32-c)B-\max(c-1,0)J+E(T_1,v,r)+E(T_2,v,r).
\tag{1}
\]

Here the exceptional-edge numerator is exactly

\[
E(T,v,r)=
\begin{cases}
\binom{12}{r-5}+\binom{12}{r},&T=\varnothing,\\
0,&v\in T,\\
\binom{12+|T|}{r},&v\notin T,\ |T|\ge2.
\end{cases}
\]

The middle line holds because that original edge already contains both colors on F. Therefore U(v,r)<D implies a proper coloring of every original edge. No independence of edges or joints is used.

## 2. Fifteen elementary risk pairs

Call an exceptional edge P when already proper, D when disjoint from F, and Bj when its j fixed points are all blue. The following table gives the smallest c=k for which all the tested samples r=9,…,17 fail to be strictly below one. For each risk pair every c<k succeeds; this is verified exactly. The same thresholds are attained already among r=10,11,12.

| Pair | k | Pair | k | Pair | k |
|---|---:|---|---:|---|---:|
| P,P | 8 | P,D | 7 | P,B2 | 7 |
| P,B3 | 6 | P,B4 | 4 | D,D | 7 |
| D,B2 | 7 | D,B3 | 5 | D,B4 | 3 |
| B2,B2 | 6 | B2,B3 | 6 | B2,B4 | 4 |
| B3,B3 | 5 | B3,B4 | 3 | B4,B4 | 2 |

These are only integer substitutions in (1), not a search over original hypergraphs. PROFILE.json records all r-specific numerators and thresholds. VERIFY.py recomputes them independently as hypergeometric fractions, using C(r,4)/C(17,4), C(17−r,4)/C(17,4), and C(r,8)/C(17,8), with analogous formulas for the exceptional events.

## 3. Complete trace-pair coverage and exact residuals

There are 1+10+10+5=26 possible traces on the fixed five labels, and 351 unordered pairs with repetition. Two unordered trace pairs are equivalent under relabeling F precisely when their two sizes and their intersection size agree. These invariants give 19 types. PROFILE.py also constructs the full S5 orbit of each representative and saves every image; their sizes sum to 351. VERIFY.py separately generates all 351 pairs and checks the size/intersection classification and orbit cardinalities.

For a type, apply the table separately at each possible red point v, obtaining lower bounds a_v≥k_v if none of these choices proves repair. Fourteen types have Σk_v>32 and are immediately impossible. The remaining five types are below. Entries are in the order of the displayed traces on labels 0,…,4. The extra column is the only possible surplus Σ(a−k)=32−Σk.

| Type | T1,T2 | k-vector | Surplus | Resulting degrees on F, up to trace-preserving relabeling |
|---|---|---|---:|---|
| A | ∅,012 | 7,7,7,5,5 | 1 | (10,9,9,6,6) or (9,9,9,7,6) |
| B | ∅,0123 | 7,7,7,7,3 | 1 | (10,9,9,9,4) or (9,9,9,9,5) |
| C | 012,034 | 8,6,6,6,6 | 0 | (11,8,8,8,8) |
| D | 012,0134 | 8,8,4,6,6 | 0 | (11,11,6,8,8) |
| E | 0123,0124 | 8,8,8,4,4 | 0 | (11,11,11,6,6) |

The A/B degree variants distinguish whether the one surplus attachment lies inside or outside their nonempty trace. In C the degree-11 point is the common trace point; in D the two common trace points have degree 11; in E the three common trace points have degree 11. All degree formulas come from the actual original edges in §1. The complete 19 rows and all labeled residual degree vectors are retained in the JSON files.

## 4. The two complete structural consequences

If Δ≤8, the degree identity gives |T1|+|T2|≤3. Thus only trace-size pairs (0,0),(0,2),(0,3) are possible. The first two have threshold sum 35>32. In (0,3), failure forces each of the three trace points to have a_i≥7, hence original degree at least 9, again impossible. This proves the first stated range without a minimum-degree or pair-covering assumption.

For the second range, the full residual list suffices. Δ≤9 excludes C,D,E, all of which require degree 11. Pair covering on 22 vertices gives d_H(v)≥ceil(21/4)=6 and excludes B. Minimum degree at least 7 excludes A, which always has a degree-6 point. Hence no residual type remains.

Before the strengthening in §6, under Δ≤9 and pair covering alone the only unclosed type of the scalar bound (1) is A with F-degree pattern (9,9,9,7,6), with all three degree-9 points in the exceptional triple. Under pair covering and δ≥7 but no maximum degree, only C remains. These are method boundaries, not claims that the local data extend to a non-colorable H.

One can also check pair covering locally before claiming these consequences: for each i∈F,

\[
4a_i+\sum_{T\in\{T_1,T_2\}:i\in T}(5-|T|)\ge17.
\]

This counts the slots that actual edges through i provide toward the 17 vertices outside F. The local filter in PROFILE.py uses exactly this necessary condition; the two proofs above need only its simpler minimum-degree consequence.

## 5. Evidence and stopping boundary

- PROFILE.py/json: all 351 trace pairs, 19 full S5 orbits, exact common-sample integer bounds, local scope filters. Measured CPU 0.004772 seconds.
- VERIFY.py/json: independent hypergeometric probability formulas, all 15 risk-pair rows, independent 351-pair invariant classification, every saved orbit size, and every residual degree vector. PASS; CPU 0.018832 seconds.

The classification transports only the five labels of the actual edge F; it does not assume an automorphism of H. A strict entry yields an original 22-vertex coloring directly by the finite union bound in §1. No whole-H enumeration, exceptional-neighbor leaf assumption, or free-set search is involved. This note does not settle arbitrary 22-point qΓ(F)=2 systems beyond the stated ranges, nor any complete vertex-count branch of the global problem.

## 6. Analytic closure of the A/B residuals; maximum degree10

The independent [seven-four-set forest lemma](../seven_red_foursets_seventeen_20261020/PROOF.md) proves that seven distinct external four-sets on at most17 points have, in the10-red/7-blue sample, a single event-tree joint deduction of at least636 outcomes out of19448. Its proof partitions the overlap graph by its number of connected components; the deductions in the three cases are636,762,2484. All subtractions belong to one common tree. The finite scalar/support verification is [CHECK.json](../seven_red_foursets_seventeen_20261020/CHECK.json), PASS.

In type A or B the nonempty exceptional trace has at least three points, each with baseline attachment7. There is only one surplus attachment in the entire F, so choose a point v of this trace with exactly7 singleton-edge attachments. The other exceptional trace is empty. Color v red and the other four F-points blue, and take10 red points uniformly outside F. The nonempty-trace exceptional edge is proper. Simplicity makes the seven red-attached external four-sets distinct. The25 blue-attached edges and the disjoint exceptional edge are counted in that same sample, giving

\[
\Pr(\text{some original edge is bad})\le
\frac{7\cdot1716+25\cdot286+858-636}{19448}
=\frac{2423}{2431}<1.
\]

This repairs A and B for every placement of their single surplus, including the variants with a degree10 point. No δ, Δ, covering, or exceptional-neighbor Γ-degree condition is used in this step. The only remaining general candidate types are C,D,E, with the exact degree patterns in §3; each has a degree11 point. Therefore Δ≤10 excludes all of them and proves the strengthened complete structural consequence stated at the top. This is a coloring of the original H, and does not assert that unrestricted C,D,E have been settled.
