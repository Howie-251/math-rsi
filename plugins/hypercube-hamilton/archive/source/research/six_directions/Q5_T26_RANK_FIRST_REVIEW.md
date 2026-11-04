# Independent audit: first marked T26 orbit

Verdict: **PASS**, same-family / provisional. Reviewer `/root/t26_first_rank_review`, GPT-6.1-sol high, explicitly selected by the user through the parent. This route overrides the ARIS skill's default reviewer model. This fresh reviewer read the full frozen proof and wrote new checkers; no producer checker or search was imported or executed.

The exact accepted local statement is: for every perfect matching F of the complete graph on K={0,...,31}\{0,1,3,4,14,22,28,31}, there exists a simple 30-cycle with vertex set Q5\{1,4}, containing F, and having only short edges outside F. Its common cube-automorphism images are included, with the minority/majority/omitted sets transformed together. No restriction to bipartite or short F is imposed.

## Obligation ledger and proof

1. **Exact short forest interface — discharged computationally and analytically.** Independently parsed 2048 forests of 18 distinct short edges. Each has degree zero at omissions, degree one at precisely K, degree two at the other six holes. DSU rejects every cycle. Its twelve components have exactly two K endpoints; deriving component endpoints reproduces every saved P(S). All 2048 columns independently have each K vertex exactly once. Repeated vertices, omitted endpoints, long added edges, cycles, incorrect degrees and incorrect saved pairings were explicit rejection conditions.
2. **Generic rank upper bound — discharged by primary-source inspection.** Cygan, Kratsch and Nederlof's accepted manuscript defines H_t using all complete-graph perfect matchings (abstract, PDF page 1). Theorem 3.4 and Corollary 3.5 (PDF page 9) apply to every even t>=2 over GF(2). Consequently rank(H_24)=2048, and the upper bound alone suffices. This is independent of the previous t=22 application. Primary source: [author accepted manuscript](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf). The inherited source note's appendix start-page description is immaterial to this import: the inspected corollary and factorization on page 9 suffice.
3. **Finite full rank — discharged independently.** A new Python implementation contracts P(S)'s twelve edges and applies DSU to each column matching. Exactly 4,194,304 computed connectivity bits agree byte for byte with the saved 524,288-byte matrix, SHA256 fb590ff0b36db8ac94d1c9de3643aeeb211e041c710a1f1b3244034a3298504c. Lowest-set-bit Gaussian elimination, unlike the supplied highest-set-bit pivots, gives rank 2048. Additionally each of the 2048 saved pivot combinations was independently XOR-checked and its stated highest pivot verified. All manifest hashes and sizes match.
4. **Universal F quantifier — discharged analytically.** These restricted independent rows remain independent as complete rows of H_24. The upper bound makes them a row-space basis. For every F={(a_i,b_i)}, the matching R={(b_i,a_(i+1))} gives a connected alternating 24-cycle, so column F is nonzero. If all selected rows vanished at F, their span and hence R's row would vanish there, contradiction. Thus an admissible selected forest connects to every F. This argument does not assume that F is one of the 2048 test columns.
5. **Simple cycle expansion — discharged analytically.** Forest interiors are disjoint and exactly the six included holes; expanding its twelve endpoint pairs preserves connectedness. Every resulting vertex has degree two. A common F/P pair would be a separate two-vertex component, incompatible with connectedness on 24 endpoints. In particular a single-edge forest path cannot duplicate F. Expansion is therefore a simple cycle on all 30 specified vertices, preserving every arbitrary required edge.

The dependency DAG is primary rank upper bound + explicit forests/columns/matrix -> local universal theorem -> optional uniform Q6 transfer. There is no reverse dependence on a ten-hole or P6 conclusion.

## Q6 application and exact latest residual

The imported uniform transfer is independently replayed for both actual rows, with k=5. The c=0 boundary remains its previously accepted five-direction input. For c>0:

- Row (a,b)=(2,1): s=a+1-b=2 and S=Z intersect A. Its mirrors Y are odd, nonholes by Z-W independence, internally covered because a free source cannot have a crossing mate, and distinct from root 0 by parity. If root is in A take r=u and pair X_A union S; otherwise choose r in S and pair X_A union (S\{r}). Both completions leave balanced (1,1) A holes. The resulting B holes are minority Z intersect B and majority (W intersect B) union Y, with exactly Y omitted.
- Row (a,b)=(0,3): t=b-a-1=2 and S is any two W intersect A excluding the possible mirror of root. The target is covered, so it is not in W; three sources minus at most one exclusion leave a pair. Its mirrors Y are even, internally covered, and different from root. If root is in A take r=u; otherwise choose an even crossing port, which exists since even-minus-odd port count is b-a=3. The completions leave balanced (1,1) A holes. B minority is W intersect B and majority (Z intersect B) union Y, omitting exactly Y.

In both cases delete the artificial completion matching, attach original crossings and the two short bridges. The accepted tag joins terminal components of a path forest. Conflict vertices Y have distinct original pendant mates outside transfer endpoints (opposite parity and internally covered). Thus simultaneous suppression creates an arbitrary complete-graph matching L on B, with exactly the displayed holes and omissions. The local theorem explicitly allows every such L, even when compressed edges are long or same-parity. Expanding the cycle and deleting the tag preserves the prescribed root and covered target and all original matching edges. All remaining introduced edges are short. This holds for **every realizing original short matching**, independently of its crossing pattern, artificial completion, and resulting compressed L.

The independent application checker constructs all 3840 translations/permutations of the *whole* marked geometry; they produce 1920 distinct marked images. It enumerates every actual outer cut and legal source pair, compares the actual projection against this lookup, and saves an explicit common automorphism for each newly accepted input. It also independently validates the full older 11340-record coverage and each producer witness, but computes the new decrement directly on the latest 41236 inputs bound by TEN_COVERED_Q5_ENDPOINT_REVIEW.json.

| Target | Latest input | Net new | Remaining |
|---:|---:|---:|---:|
|1|12910|1920|10990|
|7|12696|1890|10806|
|31|15630|1980|13650|
|Total|41236|5790|35446|

Independent residuals preserve input byte order and equal exactly the input set minus independently covered records. They are `Q5_T26_RANK_FIRST_REVIEW_remaining_v{1,7,31}.bin`; hashes are recorded in the checker JSON. This coincidentally equals the producer's older T63-only net number; it was not obtained by subtracting that number blindly.

Evidence: Q5_T26_RANK_FIRST_REVIEW_check.py/.json and Q5_T26_RANK_FIRST_REVIEW_witnesses.json. No producer file, accepted ledger or main state was modified. No fatal, critical or major mathematical gap remains in this scope. Full T26, full ten-hole covered/free layers and full P6 remain **OPEN**. Other marked batch certificates are outside this first-orbit report.
