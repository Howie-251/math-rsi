# Independent audit: A4 reduces to one remaining hole orbit

**Verdict: PASS for the stated reduction**, with semantic acceptance **same-family / provisional** relative to the declared external theorem inputs. All 540540 matching records and 2448249 circle witnesses pass a separate deterministic verifier. Full Q5 A4 and P6 remain unproved: arbitrary matchings with holes {0,1,14,22}, forbidden vertex1, are still an open family.

Reviewer: independent GPT-6.1-sol with high reasoning, as requested by the user. Date: 2026-11-01. Main input: `A4_SINGLE_GEOMETRY_REDUCTION.md`. Exact input hashes are bound in `A4_SINGLE_GEOMETRY_REVIEW.json`. No previous proof, audit, or root-state file was modified.

## Dependency and import audit

The graph of proof obligations is acyclic. Positive spectrum certificates and Q4 symmetry prove L15/L18; those prove Z0. Z0 plus the previously directly reviewed S4D prove S2D. Q4 N14_4 and the two-mirror bridge argument prove S3D. Q5 N14 handles the adjacent-hole branch. These inputs plus support geometry prove R1A. Neither T44 nor S1D is needed; neither A4 nor P6 is assumed anywhere.

The earlier core N14_4/NC_4/S4D arguments were reviewed directly in this independent agent, and their hash-bound inputs remain unchanged. This audit also read the N14 statement and proof in `TWO_ODD_HOLES_TRANSFER.md`, restricting that imported file's reviewed scope to N14 rather than its later Z14 result.

For Q5 N14, the external input is [Fink–Mütze, Theorem8, author PDF pages3–4](https://tmuetze.de/papers/match.pdf). I directly checked the statement and extension definition: d≥5, arbitrary K(Qd) matchings, an avoided normalized vertex, and condition(H). With exactly two same-parity holes, any contained half-layer leaves the two holes in the same complementary coordinate face, so the other hole discharges(H). The matching's even-minus-odd covered-vertex count is twice its same-even-minus-same-odd edge count. A cycle has equal such vertex/edge differences; adding only short edges preserves the edge difference. Consequently an avoiding cycle must include the other hole. This proves the imported N14 application without importing full A4. The perfect-matching theorem used to derive the earlier NC_4 is Theorem2 of that PDF, d≥2, with arbitrary prescribed pairs and short added edges. These external theorems are not reproved here.

## Proof-obligation ledger

All38 obligations close. The analysis is finite and deterministic; there are no analytic limits, stochastic modes, interchanges, or asymptotic uniformity assertions to audit.

| ID | Location | Obligation and check |
|---|---|---|
| R01 | R1A | The residual family quantifies over every K(Q5) matching on the other28 vertices. Reducing hole geometry does not solve or enumerate these matchings. |
| R02 | L15 symmetry | XOR by the forbidden hole and coordinate permutations preserve all original edges, new-edge shortness, and optional-edge cardinalities. Same-parity hole distances in Q4 are2 or4, represented by3 or15. |
| R03 | L18 symmetry | Translate either opposite-parity hole to0; the other has weight1 or3, represented by1 or7. There are no missing distance orbits. |
| R04 | Finite universes | Every representative has14 covered vertices and13!!=135135 arbitrary perfect matchings. Four universes total540540 records. |
| R05 | Binary decoding | Both verifier implementations enforce complete variable-length headers and lists, positive circle counts, and exact end-of-file consumption. |
| R06 | Matching validity | Submitted checker validates precisely holes{0,s}, a fixed-point-free covered involution, and no pairing outside the covered set. Separate checker requires membership in its independently generated exact universe. |
| R07 | Matching coverage | Submitted rank is a bijection; separate checker instead removes explicit mate arrays once from a full set. No omitted or repeated matching can pass either method. |
| R08 | Circle support | Every witness is simple with exactly15 required vertices for A, or all16 vertices for B. Required matching edges are actually consecutive. |
| R09 | Optional-edge definition | Only short edges outside the fixed matching are accumulated. Separate checker represents the32 actual Q4 short edges as bits and rejects any long nonmatching edge. |
| R10 | Bounds | Every record's certified optional union has at least15 edges for A or18 for B. No simultaneous occurrence or completeness of the witness list is assumed. |
| R11 | Independent verification | Independent set-subtraction and positional-edge checks pass all540540 records and2448249 circle witnesses. This does not trust a producer's search result or optional-union total. |
| R12 | Z0 local inputs | A zero-crossing cut leaves precisely same-parity holes v,b in A and opposite-parity holes a,t in B. Each side is Q4; local/global parity differ only by a fixed bit. |
| R13 | Z0 intersection | A Q4 has32 short edges. Natural face identification maps both optional sets into this same universe;15+18>32 forces a common edge. |
| R14 | Z0 witnesses | Select one witness circle in each face for that edge. The circles need not witness other optional edges simultaneously. Both chosen edges are outside their original local matching. |
| R15 | Z0 splice | Removing these two edges opens two vertex-disjoint spanning paths on15 and16 vertices. Two distinct short mirror bridges join them into one simple31-cycle, preserving F. |
| R16 | S2D | If crossing count is positive, the S4D hypotheses are exactly this2/2 hole split. If zero, Z0 applies. The alternatives exhaust all crossing counts. |
| R17 | Adjacent branch | If ab or at is short, add that edge at free endpoints. Exactly two same-parity holes remain, one v. Q5 N14 at dimension5 yields the required31-cycle; the auxiliary edge is short relative to original F. |
| R18 | S3D crossing parity | Three holes in A give2|F_A|+c=13; hence c is odd, positive, and at most13. |
| R19 | Mirror availability | The B mirrors of b,t are distinct. Neither equals a because neither ab nor at is short; B has no other global hole. Each mirror is therefore internally covered or a crossing port. |
| R20 | Mirror selection | With c=1, at most one of these two distinct mirrors belongs to X_B, so choose an internal one. With c≥3, either mirror is allowed. The forbidden majority hole v is never used for the bridge. |
| R21 | A port pairing | X_A∪{t} has positive even size and is disjoint from F_A's covered set. A pairing D is valid and leaves exactly the same-parity holes v,b. |
| R22 | A extension | N14_4 is applied only in dimension4, with the correct same-parity holes and forbidden v. Its15-circle contains every D edge. |
| R23 | Transferred segments | Deleting the nonempty matching D from a simple cycle yields nontrivial disjoint paths. Attach original crossing edges at X_A and short tw at t. All A vertices except v are included, with no unwanted auxiliary edge retained. |
| R24 | Internal-w overlap | With w internal to F_B, w∉X_B. Transfer endpoints are distinct X_B∪{w}; compressed R overlaps F_B at precisely w. |
| R25 | Internal-w repair | k=F_B(w) is internal, d=R(w) is a crossing port, and k,d,w are distinct. Removing wk,wd and inserting kd leaves a valid matching with exactly holes a,w. |
| R26 | Internal-w B input | w is the mirror of majority t, so p(w)=p(a). Thus N14_4 applies to B with forbidden w and supplies a cycle on B\{w}. |
| R27 | Internal-w expansion | Expanding kd as kw followed by the transferred w–d path restores w and the original wk. Other R paths have disjoint interiors, so expansion gives one31-cycle containing all original edges. This works even at c=1. |
| R28 | Port-w pairing | The selection rule forces c≥3 if w∈X_B. Its original partner x∈X_A differs from free t. Choose tx∈D and pair all remaining ports; |D|≥2. |
| R29 | Component separation | Removing tx alone opens the A circle into a spanning t–x path. Every other D edge lies in that path; deleting one separates t from x, and later deletions cannot reconnect them. |
| R30 | Port-w join | Attaching tw and original xw joins two different components at w, so produces a path rather than a detached cycle. Remaining path endpoints are exactly X_B\{w}. |
| R31 | Port-w B input | These compressed R edges are disjoint from F_B. Their union covers every B vertex except a,w, which have the same parity. N14_4 avoiding w is therefore legal. |
| R32 | Port-w expansion/accounting | Expand all R edges into their disjoint paths with interiors(A\{v})∪{w}. All original A,B,crossing edges survive; new edges are only local short edges and tw. The resulting circle covers exactly Q5\{v}. |
| R33 | S2D geometry trigger | Any coordinate with v_i=1,b_i≠t_i has the required2/2 split after exchanging names b,t if needed. All matching crossing patterns are already covered by S2D. |
| R34 | S3D geometry trigger | Any coordinate with b_i=t_i=v_i=1 isolates minority0 and is solved by S3D, including both original-edge parity possibilities and every crossing count. |
| R35 | Residual support | Avoiding both triggers forces b_i=t_i=0 wherever v_i=1, exactly supp(v)∩(supp(b)∪supp(t))=∅. |
| R36 | Residual orbit | Distinct odd b,t of weight≥3 have union size≥4. Nonzero disjoint v in five coordinates forces union size4 and v unit. Both b,t are3-subsets of the other4 coordinates with distinct missing coordinates, mapping to unordered{14,22} while v maps to1. |
| R37 | Counts | Fresh enumeration of all770 normalized residual geometries gives S2D605,S3D510,intersection375,union740 and remaining30. Every remaining configuration explicitly maps to the claimed representative under one of120 coordinate permutations. Also30=5·C(4,2). |
| R38 | Scope/dependencies | The proof establishes a reduction to one orbit, not connectivity of the residual factor or a full A4/P6 theorem. The cited factor result is not used to infer a circle. No circular import or higher-dimension theorem is used at d=4. |

## Deterministic evidence and adversarial checks

The separate script `a4_single_geometry_independent_audit.py` imports only the explicit pairing-universe generator and exception helper from this reviewer's earlier independent implementation. It imports neither submitted spectrum verifier nor producer. It uses explicit exception checks, so checks remain active under optimized Python.

For each file, it constructs all135135 complete mate arrays using a largest-vertex pairing recursion and subtracts every observed array exactly once. Every circle's matching-edge inclusion is checked by positions modulo15 or16. Each nonmatching edge must be in the independently constructed32-edge universe and contributes one bit to the certified optional union. Results and input hashes are saved in `a4_single_geometry_independent_audit.json`.

Counterexample attempts covered distance4 and distance3 normalization extremes, multiple witness circles where an optional edge need not occur in the same circle as another edge, a common edge whose mirror might otherwise have been required, c=1 internal mirrors, c=3 port mirrors, arbitrary same-parity original long edges, and maximum possible c=13. In particular, intersection of the two optional sets certifies optionality in both faces, so the splice never deletes an original F edge. With port w, the required choice tx∈D plus another D edge prevents the detached-circle failure. These checks found no gap or counterexample.

The sole unresolved mathematical task asserted by R1A is still genuinely universal over the representative family's28 covered vertices. The reduction supplies no finite coverage or witness for all those matchings. No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue was found within the stated reduction.
