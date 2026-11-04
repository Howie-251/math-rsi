# Independent review of the Q4 core and Q5 split class

Verdict: **PASS for the stated scope**, with semantic acceptance **same-family / provisional**, relative to Fink's perfect-matching theorem. The five finite certificate universes are deterministically verified in full. This is not a proof of full Q5 A4, full six-hole P6, or the remaining 8–18-hole obligations.

Reviewer: fresh independent GPT-6.1-sol, high reasoning, as explicitly requested by the user. Review date: 2026-11-01. This reviewer did not treat earlier reviews as mathematical evidence and did not modify the proof or root state. Main input: `Q4_CORE_AND_A4_SPLIT.md`, lines 1–175. Exact reviewed hashes are in `Q4_CORE_REVIEW.json`.

## External input and dependency ledger

I directly inspected the [Fink–Mütze author PDF](https://tmuetze.de/papers/match.pdf), page 1, extension definition and Theorem 2. It states the perfect-matching extension theorem for K(Qd), d ≥ 2; the preceding definition requires all added edges to belong to Qd. Consequently it allows arbitrary prescribed pairs and applies at d=4. It is imported, not reproved here. No d≥5 avoidance theorem is used at d=4.

The dependency graph is acyclic:

* Checked certificate universes + Q4 symmetries → N14_4.
* N14_4 + checked residual universes + Q4 symmetries → A4_4.
* N14_4 + imported Fink theorem → N10_4 → NC_4.
* A4_4 + NC_4 → K4_4.
* N14_4 + NC_4 + path compression → S4D → G4D.

K4_4 is a derived available input, not an assumed premise of S4D. No node depends on unproved full A4 or P6.

## Obligation ledger

All 35 obligations below close. Mathematical arguments use finite graphs; there are no analytic limits, stochastic modes, interchanges, or asymptotic uniformity claims.

| ID | Location | Obligation and resolution |
|---|---|---|
| Q01 | 9–19 | Quantifiers concern every matching on exactly the specified covered set; prescribed edges may be arbitrary. Added edges alone must be short. |
| Q02 | 23–26 | XOR sends the forbidden hole to zero and preserves adjacency and parity equality; coordinate permutations preserve extension witnesses. |
| Q03 | 23–30 | A distinct same-parity hole has even nonzero weight 2 or 4, yielding precisely representatives 3 and 15. Independent permutation enumeration gives orbit sizes 6 and 1. |
| Q04 | 28–31 | Every allowed covered set has 14 vertices; the number of all unrestricted perfect matchings is 13!! = 135135. |
| Q05 | 35–38 | Submitted checker validates every mate involution, hole set, distinct cycle vertex set, original-edge containment, and short added edge. |
| Q06 | 39–47 | Ranking partitions pairings into 2k−1 blocks of size (2k−3)!!; recursion gives a bijection. Its implementation has the correct argument after removal of the pivot. |
| Q07 | 49–51 | Both certificate universes are complete and valid. A second implementation verified all 270270 records without using ranking or the submitted checker. |
| Q08 | 55–58 | Translation of the minority hole makes all majority holes odd, even when translation flips all absolute parities. |
| Q09 | 55–58 | A short edge from a to an available nonforbidden majority hole produces two same-parity holes including v; N14_4 preserves the inserted short edge and the original matching. |
| Q10 | 60–67 | Nonadjacent odd vertices in Q4 have weight 3. Any two distinct such supports have intersection size 2 and normalize to unordered {7,11}. |
| Q11 | 60–69 | The stabilizer acts on the remaining odd vertices in exactly the listed three pairs. Direct enumeration covers all 168 normalized configurations: adjacent132, residual12 per representative. |
| Q12 | 69–74 | Residual matchings cover 12 vertices and number 11!! = 10395 per representative. All 31185 records independently checked. |
| Q13 | 76–78 | Finite proofs rely only on witnesses and full covered-universe checks, not solver search-completeness assertions. Total records = 301455. |
| Q14 | 82–90 | N10_4 has two distinct holes and y≠r with p(y)=p(s). Free y must equal s; adding rs produces a perfect K(Q4) matching, satisfying Fink's d≥2 hypothesis. |
| Q15 | 86–90 | Deleting the compulsory auxiliary rs from its full cycle yields a simple spanning r–s path, with every remaining new edge short. |
| Q16 | 92–94 | For covered y, k is distinct from the two holes and y. Swapping yk to kr gives a matching with exactly same-parity holes y,s. |
| Q17 | 93–97 | N14_4 avoids y, covers 15 vertices, and contains kr. Deleting kr opens one r–k path and appending ky introduces precisely missing y. |
| Q18 | 95–97 | Removed artificial kr disappears and original yk is restored; any long appended ky was already required. All original L edges survive. |
| Q19 | 99–103 | Opposite-hole hypothesis gives p(y)=p(s) for any short neighbor y of r; N10_4 applies also if y=s. |
| Q20 | 99–103 | A simple spanning 16-vertex path cannot contain its endpoint edge. Adding short ry therefore makes a simple spanning cycle. |
| Q21 | 105–109 | Balanced four holes means two of each parity. With free opposite y, adding ry leaves one hole of each parity, so NC_4 applies. |
| Q22 | 109–111 | With covered opposite y, swapping yk to kr changes 2/2 holes to 1/3, with y in the majority, independently of k's parity. |
| Q23 | 110–112 | A4_4 avoids y and contains kr; deleting and appending restore original yk, prescribed endpoints, and all 16 vertices. |
| Q24 | 116–126 | Each coordinate side is a Q4. Global parity restricted to a side differs from intrinsic parity by a fixed bit, preserving equal/opposite relations. |
| Q25 | 122–125 | Exactly two holes in A gives 2|F_A|+|C|=14. Nonempty C thus has positive even cardinality and admits a complete-graph port pairing D. |
| Q26 | 125–127 | X_A is disjoint from F_A endpoints and holes. F_A∪D is a valid Q4 matching with exactly same-parity holes v,b, discharging N14_4. |
| Q27 | 129–130 | Deleting nonempty matching D from a simple cycle breaks it into |D| paths. D edges cannot be consecutive, so paths are nontrivial and endpoints are exactly X_A. |
| Q28 | 131–135 | Original crossing matching maps distinct X_A ports bijectively to X_B. Attaching all crossing edges gives disjoint transferred paths and a genuine matching R. |
| Q29 | 137–138 | R covers exactly X_B; F_B covers every other nonhole vertex in B. Their disjoint union has only opposite-parity holes a,t, meeting NC_4. |
| Q30 | 138–141 | Expanding all R edges in one Hamilton circle preserves connectedness and simplicity: interiors are disjoint, outside B, and cover A\{v}. |
| Q31 | 134–141 | All original internal and crossing edges survive. D and R disappear; only local Q4 short edges are new. Original long crossing edges are allowed. |
| Q32 | 145–155 | A coordinate in v&b&~t differs from any in v&t&~b. Every such pair produces hole patterns 00,10,01,11 and each cut has an S4D split. |
| Q33 | 155–159 | If both cuts have no crossing edge, each matching edge lies inside one of four Q3 cells. Each cell has one hole and seven covered vertices, impossible for internal pairs. Thus an S4D cut exists for every matching in this geometry. |
| Q34 | 161–166 | Nonneighbors of 0 among odd Q5 vertices number 11. There are C(11,2)·14=770 normalized choices; fresh enumeration yields 255 both,350 one,165 none. These count geometries, never all matchings. |
| Q35 | 168–175 | Final scope matches proved statements. Outside G4D, S4D remains conditional on a crossing cut. Full Q5 A4/P6 and all larger-hole claims remain open. |

## Independent finite verification

`q4_core_independent_audit.py` does not import either producer or `verify_q4_extension_certificates.py`. It explicitly generates every mate array using the largest remaining vertex and descending partner order, stores a set of all possibilities, and removes each certificate matching exactly once. Thus coverage and duplication are checked without the rank function used in the submitted verifier. Cycle verification uses vertex positions modulo 15 for matching inclusion and tests each consecutive pair for shortness or membership in the matching. The run completed successfully with 301455 witnesses checked. Its explicit exceptions remain active with optimized Python.

`q4_core_independent_audit.json` records the observed result and SHA256 values. Both Q4 orbit coverage and the Q5 mask partition were recomputed independently. All normalized residual configurations and every qualifying coordinate pair were checked for the four distinct cell patterns.

Counterexample/degeneracy pass: tested the maximal-distance two-hole orbit, each of the three residual four-hole orbits, free-target and covered-target alternatives, arbitrary parity of the covered target's mate, two crossings as the minimum nonzero case, all possible crossing counts up to14, and arbitrary long crossing/auxiliary pairs. None breaks the argument. In particular, no parity or shortness assumption is silently placed on C,D,R. Attempting to infer a crossing from one mask alone fails; the proof correctly confines the unconditional geometry conclusion to the two-mask class.

No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue was found. The finite-check PASS is deterministic; the semantic proof-review guarantee remains same-family/provisional and relative to the identified external theorem, not formal or cross-family acceptance.
