# D2_MATCH saturated-row exclusion: fresh mathematical review

Date: 2026-10-11 UTC. Reviewer task: `/root/proof_review_n62_d2`.

**Verdict: PASS, same-family and provisional.** The complete proof establishes that no simple undirected graph of order 62, maximum degree at most 8, and diameter at most 2 realizes the displayed D2_MATCH root structure. No fatal, critical, major, or minor mathematical issue was found. No source change is needed. This judgment concerns this branch; it is not an exclusion of all order-62 graphs.

The requested review configuration was `gpt-6-astra`, reasoning `ultra`. The actual backend model and effort are not independently attested in this review context. This fresh Codex review has `review_independence: same-family` and `acceptance_status: provisional`; it does not supply a cross-family acceptance overlay.

## Inputs and boundary

The complete 181-line `proofs/dd82/n62/D2_MATCH_SATURATED_ROW_EXCLUSION.md` was read and checked. Its local premises were compared directly with `proofs/dd82/n62/RECOVERED_REDUCTION.md`, especially lines 42–52 and 205–235, and with the complete original `D2_MATCH` entry of `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_root_templates.json` (lines 1916–2379), including its parent map and singleton classes.

The audit does not certify the recovered global triple-edge elimination, its finite checker, seven-template coverage, or any other branch. These are unnecessary for the local contradiction. It does not use previous audit verdicts, archived solver statuses, SAT, graph enumeration, a matrix lifting assertion, spectral classification, or the order-59 N15 condition. Only Markdown and JSON review artifacts are produced; proof sources, formal files, and the wiki are unchanged.

## Exact theorem and premise alignment

For every finite simple undirected graph G with |V(G)| = 62, maximum degree at most 8, and diameter at most 2, there cannot exist distinct labels 0,1,…,8,w,a such that:

- N(0) = X = {1,…,8}, and X is independent.
- The vertices outside {0} ∪ X partition as {w,a} and singleton-parent classes C1,…,C8, where P(v) means N(v) ∩ X.
- P(w) = {1,2,3}, P(a) = {1,2}, w is nonadjacent to a, and P(v) = {i} for v ∈ Ci.

Regularity then gives |C1| = |C2| = 5 and |C3| = 6. The source assumes exactly this structure. In the original JSON, w = 9, a = 10, C1 = {11,…,15}, C2 = {16,…,20}, and C3 = {21,…,26}; `H_edges` is empty and `[9,10]` is a fixed nonedge. All other vertices occur in exactly one of C4,…,C8.

The JSON also contains `global_B_mode: 0/1/2`, specified triangle information, and local neighbor restrictions on w. None of these stronger template facts is imported into the argument. In particular, no global upper bound Buv ≤ 2 is required. The proof therefore excludes a class containing the original D2_MATCH template, which is the correct direction for this use of fewer premises.

## Direct derivation of the graph identities

A degree-at-most-7 vertex could see at most 1 + 7 + 7·7 = 57 vertices at distance at most 2. Hence every vertex has degree 8. For the actual adjacency matrix A, define B = A² + A − 7I − J. Its diagonal is 8 − 7 − 1 = 0. For distinct u,v, Buv = c(u,v) + Auv − 1 is a nonnegative integer: a nonedge has a common neighbor by the diameter condition, and an edge contributes Auv = 1. Symmetry follows from undirectedness.

Its row sum is 64 + 8 − 7 − 62 = 3. Since AJ = JA = 8J, A commutes with B. Finally, on an edge uv one has Buv = c(u,v), so summing over neighbors v of u counts each triangle at u twice:

Σ(v adjacent to u) Buv = 2t(u).

Thus every positivity, integer-budget, symmetry, row-sum, parity, and commutation condition used later follows from the same original graph. There is no independent choice of B to realize or lift.

## Line-by-line substantive checks

### Step 1, lines 54–74: four saturated rows

For a vertex outside the closed root neighborhood, its common neighbors with 0 are exactly its parents. Thus B0w = 2 and B0a = 1, exhausting row 0.

The common neighbors of 1 and 2 are exactly 0,w,a. No point of X can contribute because X is independent, and no singleton-parent vertex can be adjacent to both. Likewise, 1 and 3, and 2 and 3, have exactly 0,w in common. All three pairs are nonedges. Hence B12 = 2 and B13 = B23 = 1 exactly, giving the entire rows B1 = 2e2 + e3 and B2 = 2e1 + e3. Their positive supports are nonneighbors, so t(1) = t(2) = 0.

The assumed nonedge wa has at least common neighbors 1,2, so Bwa ≥ 1. Row w already has weight 2 at 0. Nonnegativity and its row sum force Bwa = 1 and Bw = 2e0 + ea. Both endpoints are nonneighbors, yielding t(w) = 0. Additional common neighbors of w,a would increase Bwa and exceed the row budget, rather than constitute a missing case.

### Step 2, lines 76–106: the residual endpoint of a

Symmetry fixes Ba0 = Baw = 1 exactly. The zero diagonal and integrality imply that the remaining weight is one unit at a single distinct vertex c. Commutation at (0,a) gives Σ(i ∈ X) Bia = 0 because wa is a nonedge; consequently c is not in X. It is not 0,w,a by the already fixed entries and the diagonal, so it belongs to one singleton class.

At (1,a), (BA)1a = 2A2a + A3a = 2, whereas (AB)1a = B0a + Bwa + Baa + Σ(x ∈ C1) Bxa = 2 + Σ(x ∈ C1) Bxa. Thus c is not in C1. The explicit exchange of labels 1 and 2 gives c not in C2. This exchange reuses identical hypotheses; it does not assume an automorphism of G.

At (1,c), (AB)1c ≥ Bac = 1 because 1 is adjacent to a. The other product is 2A2c + A3c = A3c, since c is an ordinary vertex outside C2. Therefore A3c = 1 and c ∈ C3. In the complete row Ba = e0 + ew + ec, the first two endpoints are nonneighbors. The incident repeat weight can only be 0 or 1, but it equals the even integer 2t(a); it is 0. Hence a is nonadjacent to c. This parity argument uses no global simplicity of B.

### Step 3, lines 108–116: independence and zero entries

Row 3 has weights one at each of the nonneighbors 1,2, leaving at most one unit on neighbors. The same even triangle-budget argument gives t(3) = 0. Its entire neighborhood is independent, in particular C3.

At (1,3), (BA)13 = 2A23 + A33 = 0. Every summand in (AB)13 is nonnegative, including each Bx3 for x ∈ C1, so all such entries vanish. The analogous computation at (2,3) yields the corresponding statement on C2. Symmetry gives equation (5) in the stated orientation.

### Step 4, lines 118–141: complete support, including the 5-versus-6 count

Fix x ∈ C1. Then (BA)2x = 2A1x + A3x = 2. In the expansion over N(2), the entries of rows 0,w,a at x vanish: row a only has the extra endpoint c ∈ C3. Thus Σ(y ∈ C2) Bxy = 2. This proves that each C1 row has only one unit left outside C2, without imposing anything on its location yet.

For q ∈ C3, (BA)1q = 2A2q + A3q = 1. Expansion over N(1) gives (AB)1q = 1(q=c) + Σ(x ∈ C1) Bxq. Hence the column totals into C3 are exactly 0 at c and 1 at each of the other five points.

To make the capacity argument explicit, put rx = Σ(q ∈ C3) Bxq. The disjointness of C2 and C3, row sum 3, and the preceding C2 total give 0 ≤ rx ≤ 1 for each of five x ∈ C1. The column equation gives Σ(x ∈ C1) rx = 6 − 1 = 5. Therefore every rx = 1. Together with the C2 weight 2, this exhausts each entire row and forces zero at every vertex outside C2 ∪ C3. No unexplored class can retain positive repeat weight.

Repeating the same equations with labels 1 and 2 exchanged gives the complete support bound for each C2 row. Integrality and nonnegativity also show that, for every q ≠ c in C3, its total weight one toward either five-point class is one unit at exactly one endpoint. The proof needs this consequence only for q = d at the end.

### Step 5, lines 143–147: actual cross-matching

For x ∈ C1, the pair 2,x is a nonedge because x has sole parent 1. The complete row 2 has B2x = 0, so c(2,x) = 1. The full neighborhood of 2 is {0,w,a} ∪ C2. The point x is not adjacent to 0 because it lies outside the closed root neighborhood. An edge xw or xa would form a triangle at 1, already shown triangle-free. Thus the one common neighbor lies in C2, which means exactly one actual A-edge from x into C2.

The same argument for y ∈ C2 yields exactly one actual neighbor in C1. These assertions give a perfect matching between the two classes. No repeat edge is mistaken for an original edge, and no separate matching assumption from the archived template is used.

### Step 6, lines 149–165: the exceptional original neighbor d

For x ∈ C1, the nonedge 3,x has B3x = 0, so it has exactly one common neighbor. In N(3) = {0,w} ∪ C3, neither 0 nor w can be adjacent to x by the arguments above. Thus x has exactly one actual neighbor in C3, and e(C1,C3) = 5.

For q ∈ C3, the nonedge 1,q has B1q = 0, so it has exactly one common neighbor. In N(1), q is not adjacent to 0. It cannot be adjacent to w, because 3 is adjacent to both w and q and an edge qw would form a triangle at w (also at 3). Therefore Aaq + |N(q) ∩ C1| = 1.

Summing over the six q gives Σ(q ∈ C3) Aaq + 5 = 6. Because A is a simple adjacency matrix, exactly one q, named d, is adjacent to a. As a is nonadjacent to c, d ≠ c. The pointwise equation yields no neighbors of d in C1. Its counterpart using parent label 2 yields no neighbors in C2 using the same already known Aad = 1. Finally, d has no neighbor in C3 because C3 is independent. This is an exact count of A-edges, separate from the earlier exact count of B-weight.

### Step 7, lines 167–175: product orientation and contradiction

Since d ≠ c, equation (7) supplies x ∈ C1 with Bxd = 1. Step 5 supplies its actual matching mate y ∈ C2, so Ayx = 1. The v=x summand of (AB)yd = Σv Ayv Bvd is therefore 1; every other summand is nonnegative. Hence (AB)yd ≥ 1.

The entire row By is supported in C1 ∪ C3 by Step 4. For every v in this support, Avd = 0 by Step 6 and the independence of C3. Thus every summand in (BA)yd = Σv Byv Avd vanishes, giving (BA)yd = 0. If v=d occurs in the support, the same assertion follows from Add = 0. Neighbors of d in a or in other classes do not contribute, because the corresponding entries of By are zero. This contradicts actual matrix commutation and completes exactly the stated branch exclusion.

## Counterexample and hidden-assumption attacks

These were direct symbolic attempts to break the inferences; no numerical search or exhaustive enumeration was used.

| Attempt | Decisive obstruction |
|---|---|
| Add an unlisted common neighbor of 1,2 or 1,3 | The vertex partition, exact parent sets, and independence of X exclude every available vertex type. |
| Give wa repeat weight greater than one | Bw0 = 2 and row sum 3 make this impossible. |
| Put the residual endpoint c at 0,w,a or in X | Fixed exact entries, the zero diagonal, and commutation at (0,a) exclude these locations. |
| Put c in C1, C2, or an unexamined class C4,…,C8 | Commutation at (1,a),(2,a) excludes the first two; at (1,c) it forces parent 3. |
| Make ac an edge, or place an edge inside C3 | Each would make a positive odd incident repeat budget at a or a triangle at 3 despite the even budget bound. |
| Concentrate the five C3 repeat units on fewer than five C1 rows, leaving other repeat support elsewhere | Each row has residual capacity at most one and there are exactly five units in total. |
| Use a double repeat entry between C1 and C2, or allow triple repeats elsewhere | Such weights need not be forbidden; the proof uses only their total weight two. No step requires global B ≤ 2. |
| Give a vertex in C1 two actual matching mates or none | Its exact common-neighbor count with 2 is one, and the only possible common-neighbor locations are C2. |
| Let the sole a-neighbor d equal c | The established nonedge ac rules this out. |
| Add a hidden positive contribution to (BA)yd outside C1 ∪ C3 | The complete row-support deduction makes its B coefficient zero; inside the support its A coefficient is zero. |
| Swap AB and BA or use a repeat edge as the matching mate | The expanded products above place A and B on the correct legs and derive the matching from A. |

No counterexample was found. The reason for the verdict is the discharged deductions, not merely the failure of these attempts.

## Review checklist and validation

Definitions are stable: A is always actual adjacency, B is always its defined defect matrix, and the words “repeat” refer to B-weight. The symbol c is overloaded as the two-argument common-neighbor function c(u,v) and the named vertex c, but the arity and context distinguish them unambiguously. All inequalities follow from nonnegative matrix entries or exact row budgets. All sets counted in the two 5-versus-6 arguments are explicitly disjoint or form stated partitions. All sums are finite, so there are no limit or measure-theoretic interchanges, probability modes, asymptotic estimates, uniformity conditions, or hidden constants to discharge. The dependency order is acyclic; the matching and the support statement are both proved before use in the final contradiction.

A separate read-only Python input-consistency check parsed the original JSON and verified the D2 parent sets, fixed nonedge, empty root-neighborhood edge set, distinct and exhaustive singleton partition, sizes (5,5,6,7,7,7,7,7), and degree 8 at all root neighbors. It passed. This checks transcription and premise alignment only and is not a finite nonexistence enumeration.

No mathematical fix was required, and no proof-source, formal, or wiki mutation was made. The local theorem has no remaining proof obligation identified in this review. Global coverage, the other branches, formalization, and independent-family acceptance remain separate matters.
