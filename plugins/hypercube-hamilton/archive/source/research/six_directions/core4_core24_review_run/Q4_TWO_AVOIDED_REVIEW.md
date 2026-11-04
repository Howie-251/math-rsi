# Independent review: T44, S1D, and G2D

**PASS for the stated scope**, with semantic assurance **same-family / provisional** relative to Fink's perfect-matching extension theorem. The independent finite verification is deterministic: all 311850 certificates in all 30 configurations pass. Full Q5 A4 and unconditional P6 remain unproved.

Reviewer: fresh independent GPT-6.1-sol, high reasoning, as requested by the user. Date: 2026-11-01. This is an additive audit of `Q4_TWO_AVOIDED_TRANSFER.md`. The earlier core proof/audit and root state were not edited. Input hashes, including imported core proof inputs, are bound in `Q4_TWO_AVOIDED_REVIEW.json`.

## Dependency and hypothesis ledger

The dependency graph is acyclic: finite T44 certificates plus symmetry prove T44; T44 plus Fink's perfect-matching theorem prove both cases of S1D; S1D plus the cell-parity contradiction prove G2D. G4D is the separately checked core result; the union count uses only the two explicit geometry predicates.

The sole external theorem needed for S1D is [Fink's perfect-matching extension theorem, restated as Theorem 2 on page 1 of the Fink–Mütze author PDF](https://tmuetze.de/papers/match.pdf). I directly checked its d≥2 hypothesis and the preceding extension definition: arbitrary K(Qd) perfect matchings are allowed and all added edges belong to Qd. It therefore applies in the four-dimensional B side, even when the port pairing contains long edges. This theorem is imported, not reproved. No dimension-five avoided-vertex theorem is used in Q4.

All 29 obligations below close. All objects are finite graphs; no analytic, probabilistic, limit-interchange, or asymptotic-uniformity obligations occur.

| ID | Claim | Check |
|---|---|---|
| T01 | T44 quantified domain | Four distinct holes all have one parity; any two distinct designated holes must be omitted, and the other two must be visited. Arbitrary original matching pairs are permitted. |
| T02 | Translation | XOR by the first designated hole preserves short edges and equality of parity, and makes all four holes even. |
| T03 | Representative distances | The other designated hole has nonzero even weight 2 or4, mapped to3 or15 by a coordinate permutation. |
| T04 | Remaining-hole coverage | After that permutation the other two holes may be any pair of six remaining even vertices: exactly15 cases per representative. Retaining all15 does not require further stabilizer reductions. |
| T05 | Global symmetry coverage | Independent enumeration of all840 same-parity four-hole/unordered-avoided-pair configurations verifies that every one maps to one of the30 submitted universes. |
| T06 | Matching universe | Twelve covered vertices have11!!=10395 arbitrary perfect matchings. The mate-array universe has exactly this size in every case. |
| T07 | Submitted verifier | Hole-set checks, covered involution checks, rank uniqueness/completeness, exact14-vertex support, edge inclusion, and new-edge shortness are all present and correct. |
| T08 | Rank validity | Successive partner choices partition pairings into equal-size blocks; its multiplier counts the matchings of the remaining vertices. No rank-dependent producer order is assumed. |
| T09 | Independent complete coverage | A separate set-subtraction verifier checks all311850 mate arrays exactly once and validates every cycle through positions modulo14, without using ranking. |
| T10 | S1D cut types | The majority side A has three holes and B has only a; each side is Q4. Intrinsic parity differs from global parity by a constant and preserves all required parity relations. |
| T11 | Crossing count | On B, 2|F_B|+c=15 makes c positive odd. No assumption that original crossing edges are short is made. |
| T12 | Perfect B matching | X_B∪{a} has c+1 even cardinality, disjoint from F_B. Any pairing D of it gives a perfect K(B) matching, satisfying Fink at d=4. |
| T13 | B path decomposition | D is nonempty and is a matching in a simple full circle; deleting it yields nontrivial disjoint paths with endpoints exactly X_B∪{a}, covering B. |
| T14 | Attachments | Every X_B endpoint has a unique original crossing mate in X_A; a receives new short aw. All original B and crossing edges are retained, and only aw is new across the cut. |
| T15 | Internal-w endpoint set | If w has internal mate k, w∉X_A. Transferred paths have distinct endpoints X_A∪{w}; their compression R overlaps F_A at exactly w. |
| T16 | Internal-w repair | d=R(w) lies in X_A; k is internal, so k,d,w are distinct. Removing wk,wd and adding kd produces a valid matching with precisely holes b,t,v,w. |
| T17 | Internal-w parity | All b,t,v have majority parity and w has parity opposite a. Hence all four holes have equal parity and T44 may avoid v,w. |
| T18 | Internal-w expansion | The T44 circle contains kd; replacing it by kw followed by the transferred w–d path inserts w and that B interior exactly once. Other R edges expand disjointly. |
| T19 | Internal-w preservation | kw restores the removed original edge. All B, crossing, and other A edges survive. Artificial kd,R edges disappear; new edges are only local short edges and aw. The argument allows c=1. |
| T20 | Port-w pairing choice | In case2, w's mate x lies in X_B. Choose ax∈D; c≥3 leaves c−1 even ports and at least one other D edge. |
| T21 | Different B components | Deleting ax alone opens the full circle into an a–x path containing every other D edge. Removing another such edge separates a from x; further deletions cannot reconnect them. |
| T22 | Port-w join | The distinct a-component and x-component join at w via aw,xw without a cycle or repeated vertex. Remaining paths stay disjoint. Their interiors cover B∪{w}; their endpoints are exactly X_A\{w}. |
| T23 | Port-w T44 input | Compressed R is disjoint from F_A. Their union has exactly holes b,t,v,w of one parity. T44 avoiding v,w then permits expansion of every R edge. |
| T24 | Port-w conclusion and boundary | Expansion gives one simple31-vertex circle, containing every original edge and adding only short edges. With c=1 the attachments instead close a separate circle; that case is correctly excluded. |
| T25 | G2D bridge availability | Two common1-coordinates place all majority holes in cell11; the distinct bridge vertices w_i,w_j lie in10 and01 and cannot be holes. Each cut has positive odd crossing count. |
| T26 | Exceptional-form exhaustion | For each cut, a covered bridge is internal or a port. S1D solves every internal case and every port case with c≥3, leaving only c=1 with its unique crossing edge incident to that bridge. |
| T27 | Same exceptional edge | If e_i=e_j it must join w_i,w_j, hence runs10–01. It is the only edge crossing either coordinate, so cell00 has no outgoing matching edge. Its one hole leaves7 covered vertices, impossible internally. |
| T28 | Distinct exceptional edges | If e_i≠e_j, e_i cannot cross j and e_j cannot cross i. They therefore run10–00 and01–00. Cell11 has no outgoing matching edge and has3 holes, leaving5 covered vertices, impossible internally. |
| T29 | Geometry count and scope | Fresh exhaustive evaluation on all770 residual geometries gives G4D255, G2D120, intersection30, union345, outside425. These count labeled normalized geometries, not matchings or minimal symmetry orbits; the complete Q5 A4/P6 statements remain open. |

## Deterministic evidence and counterexample pass

`q4_two_avoided_independent_audit.py` imports only the explicit pairing-universe generator and exception helper from the earlier independent checker. It imports neither search program nor either rank-based verifier. For each of the30 files it builds the full set of10395 mate arrays, removes each certified array exactly once, and demands the set be empty. Exact cycle support, matching edges, and short added edges are independently checked. Observed result: **PASS,311850 certificates**, recorded in `q4_two_avoided_independent_audit.json` with all binary hashes.

The same run enumerated all840 Q4 geometric configurations before normalization and found an explicit XOR/permutation image in the certificate configuration set. It recomputed all five Q5 coverage counts and checked every qualifying pair of common coordinates for bridge availability and majority-cell placement.

Analytical attempts to break the transfer covered internal w with the minimum c=1, port w with minimum c=3, arbitrary parity/length of k,d and crossing edges, and both ways two exceptional cuts can share or not share their unique edge. The internal repair never pairs a vertex with itself; the port repair has no closed transferred component because ax is deliberately in D and at least one further D edge is removed. The explicitly excluded port c=1 branch indeed yields a detached circle and is not used as evidence for a full extension.

No mathematical issue of FATAL, CRITICAL, MAJOR, or MINOR severity was found. This scoped PASS does not replace the remaining425 geometric cases with an existence claim: additional S1D/S4D conditions may resolve specific matchings there, but universal closure is not proved.
