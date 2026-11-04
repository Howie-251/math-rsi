# Near-perfect extension: adversarial proof review

Date: 2026-11-01. Reviewer: fresh Codex subagent `/root/near_perfect_audit`.

- `review_independence: same-family`
- `acceptance_status: provisional`
- Scope: full `NEAR_PERFECT_EXTENSION.md`, source Theorems 1, 6, 8 and C1–C3 in `paper.txt`, and dependencies D1–D3 in `CORE_DERIVATION.md`.
- Result: no substantive error found in N1–N3, conditional on the cited source theorems. This is a semantic review, not formal verification or a cross-family acceptance. No literature-newness claim is assessed.
- Audited proof SHA256: `8A7F875EE232FBB1553F46180543320A53C92131E12091AD20F3590DFB37C8BE`.
- Core SHA256: `89647AD6635911BB77F5B112EE82C27EF737CCEAC5F42B17D7AB0B9EF49555A6`.
- Source SHA256: `E7036BADBCA184E006A075E569772520AADFB6514F1A42B68840838EBA8F887F`.

## A. Definitions and quantified statement

The short edges are exactly edges of `Q_n`; `B(Q_n)` joins opposite-parity vertices, and `K(Q_n)` joins every distinct pair. `P(z)` is the unique partner under the perfect matching. An i-half-layer has endpoint set `S={z: sum_{k != i} z_k = epsilon mod 2}`. Both induced cube graphs on S and its complement T have only i-edges.

The N3 statement is: for every integer n >= 5, every cube matching M and vertex u avoided by M, if there exist w and a cube matching L containing M and avoiding exactly u,w, then for every v of parity opposite to u there exists a cube Hamilton u–v path containing M. L and w may be fixed before v is chosen; x and the resulting path may depend on v. The proof has this quantifier order.

## B. Applications and discharged hypotheses

| Application | Hypotheses checked |
|---|---|
| Theorem 1 in D3 / N3 step 1 | n >= 5 implies n >= 2; L covers all vertices except the distinct opposite-parity u,w; adding uw gives a perfect matching of K(Q_n). The theorem adds only cube edges. Deleting uw leaves all L edges and produces endpoints u,w. |
| D2 / N3 step 2 | If d(u,w)=1, L plus uw is a cube perfect matching containing M; n >= 5, u is uncovered by M, and v has opposite parity. |
| Theorem 1 in D2 | P is perfect, n >= 2, and the removed edge uv cannot belong to M because u is uncovered by M. |
| D1 and Theorem 6 in D2 | P consists entirely of cube edges. In the nonpartner case uv is not in P and endpoints have opposite parity. A half-layer in compressed R forces at most two directions by D1; otherwise Theorem 6 applies. |
| Theorem 8 in D2 / N3 step 3 | n >= 5; M is a cube matching using at most two / three directions, hence at most five; endpoints have opposite parity. C1 covers u, C2 contains an edge incident to u, and C3 contains uv, so all are excluded by u being uncovered. |
| N1 / N3 step 5 | P=L plus uw is a perfect matching of B(Q_n), and uw is its unique long edge. Chosen x and v have opposite parity; x != P(v) is exactly the nonpartner condition. Thus any compressed half-layer would force L to use at most three directions, contrary to the current branch. |
| Theorem 6 / N3 step 5 | All preceding hypotheses hold, n >= 5, and the compressed matching contains no half-layer. Its conclusion permits the one long edge already in P but adds only cube edges. |
| N2 / N3 step 6 | K contains all 2^n vertices, P is perfect, and every edge of K is bipartite. Starting at x, parity agrees with u at even positions; every P edge occupies an even-to-odd position. Consequently uw appears as u then w. |

N1 is exhaustive: either the inserted edge ab is in H or it is not. In the latter case H already saturates S and a unique long edge inside T cannot coexist with all remaining T vertices matched along i. In the former case a,b are matched across to x,y; if the unique long edge is one of these two crossing edges, i-pairing forces y=x^e_i and equal crossing distances, a contradiction. Otherwise the four distinct vertices x,y,c,d form a union of i-pairs. Excluding x^e_i=y leaves c=x^e_i and d=y^e_i after exchanging names. This exchange is valid because f is an undirected edge. The two crossing directions differ, so f has length three and every short edge uses one of i,j,k.

N2 uses only uniqueness of the perfect matching on an even-order path. The splice then removes an internal edge uw and yields the components K[x,u] and K[w,v]. Reversing the first and adding xw gives one spanning path from u to v. xw is a cube edge between the components, so is new; no L edge was removed. This discharges the long-edge removal and orientation obligations.

## C–F. Counts, interchanges, probability, uniformity

- Equal bipartition sizes imply the two holes have opposite parity. Their nonadjacent distance is odd and at least three.
- A cube vertex has n distinct neighbors. Excluding at most P(v) leaves at least n-1 choices. For the selected x, x != u follows from d(u,w) >= 3; x != v follows from parity. Also v != w in this branch, so uw is internal in K.
- The direction estimates are at most three versus at least four. No hidden dependence on n occurs.
- A Q6 matching avoiding u has at most 31 edges. Every 31-edge such matching is itself a valid L. The extension criterion does not assert that every smaller matching is extendable to such L.
- D: no limit, derivative, integral, sum-interchange issue.
- E: no probabilistic premise. The reported experiments are not used in the proof.
- F: the result is uniform for every integer n >= 5. No asymptotic constants or omitted large-n restriction occur. N1 is combinatorial and needs no Theorem 6 dimension restriction; N3 does not apply that theorem below n=5.

## G. Counterexample attempts

An independent in-memory exhaustive enumeration generated every perfect matching of B(Q3) and B(Q4), every even-odd endpoint pair excluding partners, and the compressed matching. Half-layers were checked directly as edge subsets. The stronger test below, not merely the unique-long special case, passed:

| n | All bipartite perfect matchings | Tested endpoint pairs | Pairs with compressed half-layer | Violations of short-direction count <= 3 |
|---|---:|---:|---:|---:|
| 3 | 24 | 288 | 72 | 0 |
| 4 | 40,320 | 2,257,920 | 5,376 | 0 |

A separate exhaustive enumeration specifically of the unique-long case tested:

| n | Unique-long perfect matchings | Tested endpoint pairs | Pairs with compressed half-layer | N1 violations |
|---|---:|---:|---:|---:|
| 2 | 0 | 0 | 0 | 0 |
| 3 | 8 | 96 | 24 | 0 |
| 4 | 1,536 | 86,016 | 192 | 0 |

Every obstruction in the unique-long case had long-edge length exactly three and exactly three short directions. These are finite checks of the rigidity lemmas, not exhaustive tests of N3 at n >= 5.

A sharp example in Q3 is P={(3,2),(5,1),(6,4),(0,7)}, x=3, y=4, with half-layer H={(1,5),(2,6)} after compression. The unique long edge is (0,7), and all three short directions occur. Thus replacing the three-direction bound by two is false.

Degenerate branches checked: v=w, adjacent holes, M empty, L itself near-perfect, x=P(v) excluded, x=u impossible in the long-edge branch, and v covered by L whenever v != w. No counterexample was found.

## H. Dependencies and optional simplification

The dependency graph is acyclic: source Theorems 1,6,8 plus D1 yield D2/D3; independent N1/N2 and these results yield N3. No six-direction conjecture, experimental success, or N3 corollary is used to prove an upstream claim. The source Theorem 8 itself relies on the paper's computer-assisted five-dimensional result; that source proof/certificate has not been independently revalidated in this review.

The parent supplied a proposed simplification during review, and it also checks out analytically: for ANY perfect P of B(Q_n), if compression at nonpartner x,y contains an i-half-layer, every short edge outside {xP(x),yP(y)} has direction i. If ab is not in H then H saturates S and no P edge crosses S,T. If ab is in H, H minus ab saturates S minus {a,b}, and exactly xa,yb can cross S,T. Every remaining short edge lies within S or T, so has direction i. Therefore the short edges of P use at most three directions, irrespective of how many long edges P has. This can replace the only use of N1 in N3; the length-three conclusion is unnecessary for N3.

## Nonblocking editorial notes

- `NP-R1`: status `UNCLEAR`; impact `COSMETIC`; category `DIMENSION_TRACKING`; location CORE_DERIVATION D3. D3 does not restate n >= 2 although its proof invokes Theorem 1, whose stated range is n >= 2. Every use in N3 has n >= 5, so no downstream obligation is affected. Counterexample: NO; the n=1 statement also holds by the single cube edge. Minimal fix: state n >= 2 in D3, or mention the trivial n=1 case.
- For an implementation of the near-perfect completion test, one must explicitly require u to remain unmatched: on residual U=V(Q6) minus V(M), test maximum matching in Q6[U minus {u}] for size |U|/2 minus 1. An arbitrary maximum matching on Q6[U] alone need not expose the desired u. The proof's existence hypothesis already has this restriction; this is an implementation clarification, not a counterexample to N3.
- The remainder statements in older CORE_DERIVATION describe the state before N3. If presented as current status, update them to cite N3.

The result covers all matchings admitting the stated completion, including every 31-edge Q6 instance with an uncovered starting vertex. It does not close P6 for matchings lacking both perfect and u-preserving near-perfect completion, and it establishes no novelty claim.

## Addendum: N0 and N4, and reproducibility

The later version now labels the general short-direction lemma N0 and invokes it in N3 step 5. The proof is exactly the valid simplification checked above; there is no new dependency cycle.

N4 was read in full. Its Hall characterization is correct under the existing assumptions that M is a cube matching and u is uncovered. Put k=|E|=|O|. A preserving completion must add a matching in the induced residual graph, avoid u, and saturate E minus {u}; this has k-1 edges and covers k-1 of the k vertices of O. Hall's theorem applies to the finite bipartite graph (E minus {u},O), with neighborhoods exactly N_F(S). Necessity and sufficiency follow, and the uncovered opposite-parity vertex w is existential. The statement should explicitly say "for some w in O" to avoid suggesting a prescribed second hole. If k=1, the left side is empty and the criterion is vacuous, correctly accepting M itself. Failure has a nonempty witness S because the empty set never violates Hall.

For a 30-edge matching in Q6, exactly four vertices remain, with two on each side. Writing them as {u,z,w,t}, with u,z on the same side, the only nonempty left subset is {z}; Hall reduces to z having a neighbor among w,t. Adding that single edge leaves u and the other opposite-parity vertex. Thus the four-hole reduction is exact. It is a criterion for this completion route only, not for Hamilton path nonexistence. No new substantive issue was found.

The implementation clarification above was advisory; the parent confirms that `verify_near_perfect.py` already excludes the specified u when testing near-perfect completion. No bug in that implementation is alleged by this review.

The original all-P enumeration source is preserved verbatim inside `near_perfect_audit_enumeration.py` as JavaScript, with a Python launcher that uses Node.js; the original code ran in the functions.exec V8 runtime. `near_perfect_audit_enumeration.json` records the existing observed output, including counts grouped by number of long edges. No exhaustive enumeration was rerun merely to preserve these artifacts.
