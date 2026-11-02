# Fresh proof review: connected repeat unit triangles

Date: 2026-10-11. Verdict: **PASS within the explicit premises and established imports; same-family, provisional**. No FATAL, CRITICAL, MAJOR, or MINOR issue was found. The 25 obligations in `PROOF_SKELETON.md` are discharged at the paper level. This is not a cross-family acceptance or a Lean verification.

The entire 310-line source `proofs/dd82/n62/CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md` was read afresh. The review assumes an actual simple order-62 graph of maximum degree eight and diameter at most two, its actual matrix `B=A²+A−7I−J`, and **explicitly connected positive B support**. It does not import or prove that connectedness is automatic. The separately stated exclusion of triple repeats is an established import; its finite enumeration was not rerun. The original order-62 existence question and exact N(8,2) remain open.

Reviewer task: `/root/proof_review_n62_unit_triangles`, fresh-context review requested with `gpt-6-astra`, reasoning `ultra`. The actual serving model/backend is not independently attested by the available tool metadata. No claim of cross-family independence is made. Prior audit verdicts were not used as proof evidence.

## Source dependencies actually examined

All paths below are relative to the ar4math project root.

| Source | Scope read and role |
| --- | --- |
| `proofs/dd82/n62/CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md` | Entire file, lines 1–310; declared audit target. |
| `proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md` | Entire file, lines 1–209; actual root rows, distinct external ports, no-heavy light mates, persistent D1 reroot. |
| `proofs/dd82/n62/D1_MATCH_C4_TRANSPORT_REFINEMENT.md` | Entire file, lines 1–116; exact C3–C4 zero block and no-unit-triangle light-mate theorem. |
| `proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md` | Entire file, lines 1–285; generated motifs and original port bound. The component spectral classification is not required for this target. |
| `proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md` | Entire file, lines 1–144; closed six-point repeat component at every original triangle. |
| `proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md` | Entire file, lines 1–133; closed D0 four-point component, odd-double count, arbitrary-double template coverage. |
| `proofs/dd82/n62/S_TOUCH_SATURATED_ROW_EXCLUSION.md` | Entire file, lines 1–88; checked that its actual argument needs no global simple-B premise when imported by triangle pairing. |
| `proofs/dd82/n62/D2_MATCH_SATURATED_ROW_EXCLUSION.md` | Entire file, lines 1–181; D2 exclusion supporting generated unit weights and D1 classification. |
| `proofs/dd82/n62/D0_EDGE_BIN_SATURATED_ROW_EXCLUSION.md` | Entire file, lines 1–79; BIN exclusion supporting remaining-double classification. |
| `proofs/dd82/n62/RECOVERED_REDUCTION.md` | Lines 24–59 and 197–239; graph identities, parity, and lossless root-template relabeling. Triple-repeat enumeration in the intervening section remains an imported result. |

## Main derivations checked

For a unit triangle S, triangle-freeness makes S independent and fixes each pairwise common-neighbor count to two. Thus `0 ≤ t(S) ≤ 2`. With two common centers u,v, their at least three common neighbors and `B_uv ≤ 2` imply precisely `B_uv=2` and `N(u)∩N(v)=S`. Conversely, a generated triangle has its two heavy endpoints as common centers, and the exact pairwise counts forbid a third. Witness collisions in the t=1 and t=0 descriptions give exactly the forbidden additional common centers; the enumerated cases are exhaustive.

For generated-triangle separation, one shared vertex would require four positive B neighbors. Two shared vertices force their external ports relative to the generated triangle to coincide. The normalized hard D1 rows have ports `4,b,c`: 4 is a root-neighborhood label, b and c are ordinary vertices, and b lies in W whereas c lies in the disjoint ordinary neighborhood U of a. These three ports are therefore distinct. This proves separation from **every** other unit triangle, not only another generated one.

For type one, every pair of u,a,b,c shares an S neighbor and hence is a G nonedge. The three lower bounds `B_ua,B_ub,B_uc ≥ 1` exhaust row u, giving exactly `(7)`. Consequently `N(u)∩N(a)={x,y}`, and similarly for b,c. The entry `(AB)_xu=2` while `(BA)_xu=2+A_(p_x,u)` proves the port restriction even when ports repeat. Any B triangle through u uses two of a,b,c, whose intersections with N(u) meet in exactly one of x,y,z. Such a triangle is type one, excluding u from generated triangles. The three unit entries already exclude u from D.

The center-injection argument also checks exactly. If distinct v,w in N(u) have positive repeat, their second common G neighbor r exists because v,w are nonadjacent. Since u,r share v,w, triangle-freeness and the common-neighbor identity imply `B_ur≥1`, so r belongs to {a,b,c}. Its exact neighbors in N(u) are one of the three specified pairs in S. Thus every positive repeat in N(u) is an edge of S; those three entries already equal one. The other five neighbors of u are isolated in this induced B subgraph. A second unit triangle with center u would have to equal S.

For type zero, every two witnesses share an S vertex because their respective S-neighborhoods are two-subsets of a three-set. Triangle-freeness makes the full six-set independent. A double repeat between any two witnesses would have a generated triangle containing a shared S neighbor, contradicting the separation result since S itself is not generated. The three designated witness pairs already have two common neighbors, so their repeat entries are exactly one and their common-neighbor sets are exactly those displayed in `(11)`. Cross-pair unit entries are correctly left undetermined.

For every type, the three counts `n3=t`, `n2+3n3=6`, and `n1+2n2+3n3=24`, together with the order 62, give `(44−t,12+3t,6−3t,t)`. The variable called `q` in the source is the neighborhood-count vector also describable as `d_S=A1_S`. With external-port multiplicities retained, `B1_S=2·1_S+h`; commutation yields `(B−2I)d_S=Ah` without any distinct-port hypothesis. Nonnegativity refers to the resulting right side, not to the matrix `B−2I`.

For the strengthened bound, the D1 hard proof gives complete three-unit rows at both light mates, so neither is heavy. The C4 refinement proves `B(C3,C4)=0`, hence `B_pq=0`; the other two pairs among a's repeat neighbors {0,p,q} vanish by the complete root row. Thus a lies on no unit B triangle. The hard proof establishes the same D1 hypothesis after rerooting at w, so the same argument applies to r. This verifies the no-unit-triangle theorem at **both** endpoints of **every** heavy edge.

Let W now denote `V\(D∪U)` only for this paragraph. Every heavy endpoint's unit mate belongs to W. Summing repeat incidences into W, allowing repeated mates, gives `2d ≤ Σ_(v∈W) B(v,D) ≤ 3|W|`. Since `|D|=2d`, `|U|=3d+v_extra`, and `D∩U=∅`, this is `17d+3v_extra≤186`. Oddness is checked from `2C4=93+d−3T` and triangle pairing; here T=0. Thus `d∈{1,3,5,7,9}`, and d=9 gives `v_extra≤11`.

Finally, the graph consisting of unit B edges has maximum degree three. Two distinct triangles cannot meet at only one vertex. If two share edge xy, x and y already have all three neighbors. A further triangle meeting their four-vertex union can only use the other two vertices z,w together with x or y, forcing zw and therefore a K4. A unit K4 exhausts all four repeat rows and is a proper closed component, forbidden by connectedness on 62 vertices. Thus every cluster under vertex overlap is a single triangle or a diamond. Distinct clusters have disjoint vertex sets. Generated triangles are isolated clusters, and the other clusters yield `v_extra=3s+4k` and `17d+9s+12k≤186`. The source uses k for the number of diamonds; this is the same formula as `3s+4q` when q denotes that count.

## Counterexample attempts on all new load-bearing claims

These are algebraic attempts and failure reasons, not a search for an actual order-62 graph. None is an algebraically verified counterexample to a stated claim.

| Attempt | Result and obstruction |
| --- | --- |
| Add a third common center of S. | Every pair of S would have at least three common neighbors instead of two. |
| Make the two centers adjacent, or give them a fourth common neighbor. | Adjacency creates an original triangle; a fourth neighbor forces B_uv≥3, contrary to the imported bound. |
| Identify two of a,b,c in type one, or identify witnesses for different pairs in type zero. | The identified vertex becomes an additional common center, changing t. |
| Let two generated/other triangles meet in one vertex. | The shared repeat row needs four distinct positive entries. |
| Let a generated triangle share an edge with a nongenerated one. | The edge endpoints acquire the same external port, contradicting the checked distinct D1 ports. |
| Put the type-one center in D or in a generated triangle. | Its exact three-unit row excludes D; every unit triangle through it has t=1. |
| Give one center two different type-one triangles, including disjoint ones. | The exact repeat graph in its eight-neighbor set contains only the one triangle S. |
| Identify two external ports of a nongenerated triangle. | No contradiction is claimed; the multiplicity vector preserves both incidences. The transport proof still holds. Identifying all three would make a forbidden closed unit K4. |
| Add a G edge between two type-zero witnesses. | They already share an S neighbor, producing a G triangle. |
| Add a double B edge anywhere in the six witnesses. | Its generated triangle meets the t=0 triangle, violating proved separation. |
| Add cross-pair unit witness edges. | They are intentionally not excluded. No false induced-matching or global-realizability claim is made. |
| Check all t boundary values in the strata. | t=0,1,2 give `(44,12,6,0)`, `(43,15,3,1)`, `(42,18,0,2)`; every tuple sums to 62, has degree total 24 and pair-intersection total 6. |
| Neglect a repeated port in transport. | An omitted multiplicity would change B1_S; the actual definition of h avoids that failure. |
| Concentrate many heavy endpoints on one light mate. | Counting uses incidences rather than distinct mates; capacity three still bounds the total. A fourth incidence is impossible. |
| Place a heavy endpoint's light mate on any nongenerated unit triangle. | The checked C4 proof excludes all unit triangles, rather than just generated ones, at each light mate. |
| Try d=11, d=10, or d=9 with v_extra≥12. | Respectively violates 17d≤186, oddness, or 17d+3v_extra≤186. |
| Extend a diamond to a chain of three overlapping triangles. | Saturated shared-edge endpoints force a unit K4, which is a closed four-vertex component. |
| Count repeat-edge-connected but vertex-disjoint triangles as one overlap cluster. | This changes the definition. The source explicitly defines cluster adjacency by vertex overlap, so arbitrary external repeat edges do not merge clusters. |

## Scope, hypotheses, and review mechanics

All applications of D1-specific lemmas occur after every double has been put into D1 by the established template reductions and connectedness excluding closed D0 components. No assumption that all unit triangles are generated enters any proof. Neither t=0 nor t=1 is excluded. Center injection does not assert that centers avoid all unit triangles; a center may itself lie on another type-one triangle. The witness result is a matching contained in a simple induced repeat graph, not necessarily the entire induced graph. The packing bounds are necessary conditions, not realization results.

There are no limiting, analytic, probabilistic, asymptotic, or parameter-uniformity assertions. All identities and inequalities are finite, exact, and checked with integer multiplicities. The only relabeling used in the imported hard D1 source interchanges the symmetric labels 2 and 3 after locating r in C2∪C3; it is a lossless relabeling, not an assumed graph automorphism. The dependency graph is acyclic. In particular C4's light-mate proof relies on the prior hard D1 rows, never on this new unit-triangle separation or packing lemma.

No solver, finite search, external web service, or new formal verification was needed. No proof source was edited. Only Markdown and JSON review artifacts were created in this review directory. The usual rendering, compilation, and digest steps in the generic skill were overridden by the user's explicit output restrictions. No wiki claim was silently promoted to verified.

No repair round is required. The remaining mathematical work is exactly the source's stated obstacle: constrain or exclude the t=0 and t=1 possibilities, or find another obstruction to the actual remaining graph. This review does not solve that problem.
