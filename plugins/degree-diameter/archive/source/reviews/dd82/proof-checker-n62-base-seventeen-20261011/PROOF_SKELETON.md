# Proof skeleton: order-62 heavy base, seventeen edges

Review: `/root/proof_review_n62_base_seventeen`; 2026-10-11.
Assurance: **same-family; provisional**. Scope is the new paper argument and its immediate heavy-lift predecessor, modulo the imports below.

## Inputs and assumptions

Read in full:

- `proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_BASE_NEAR_EXTREMAL_EXCLUSION.md` (282 lines).
- `proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md` (307 lines).

Read source statements to resolve imports: `CONNECTED_REPEAT_REDUCTION.md`, `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, and `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`. Their upstream classifications and proofs are not reaudited here; prior review verdicts are not evidence for this review.

Explicit imports: the actual simple order-62 graph is 8-regular and triangle-free; its symmetric repeat matrix satisfies the displayed identity, row sums, and commutation; heavy pairs are D1 and exhaust double repeats; generated repeat triangles are pairwise disjoint and outside the heavy endpoints; every normalized heavy root has the complete unit row at label 4; D1 unit mates lie outside the heavy set and all generated triangles; the normalized generated-triangle ports are distinct and have the stated original adjacencies. The restriction to odd d in {1,3,5,7,9} is imported for the predecessor's table, and d=9 is assumed for the new result.

## Typed symbols and canonical conclusion

- A: 62-by-62 original adjacency matrix; B: 62-by-62 repeat matrix.
- D: heavy endpoints; h: their mate involution; a(x): a heavy endpoint's unit mate.
- S_i: three generated repeat-triangle vertices; S: their disjoint union; W: V(G) minus D union S.
- Q: adjacency matrix of G[D]; H: permutation matrix of h; Z: integer symmetric signed adjacency matrix on the antisymmetric lift space.
- F: simple signed graph on d heavy pairs; r_i: its degree; m: its unordered edge count.
- t,t_i: base triangle counts, globally and at i; a,a_i: edges in no base triangle, globally and at i. The scalar a is distinct from the predecessor's function a(x).
- b,b_i: nonedge pairs of base codegree one, globally and at i; c,c_i: nonedge pairs of codegree zero, globally and at i.

For every actual graph satisfying the imported setting, if d=9 then m≤16 and |E(G[D])|=2m≤32. Consequently |E_G(D,V minus D)|≥80 and at least 26 original edges go to W or another pair's generated triangle. If, additionally, every two base vertices have distance at most two, then |E_G(D,W)|≥26 and the previously derived repeat-edge inequality e_B(W)≤7 applies.

## Dependency DAG and obligations

The DAG is acyclic: imports → heavy involution/lift/degree bound → signed short cycles and m≤17 → local slack and triangle restrictions → t in {4,5} → t=4 → exclusion of degree patterns A and B → m≤16 → original-incidence consequence. The distance lemma separately feeds only the conditional W statements.

| ID | Obligation and justification | Location | Result |
|---|---|---|---|
| P1 | Heavy-heavy commutation splits even and binary differences, forcing mate automorphism. | Predecessor §1 | Checked |
| P2 | Symmetric 2-by-2 blocks are zero or perfect matchings; generated-neighbor separation excludes the full block. | Predecessor §2 | Checked |
| P3 | Actual repeat identity excludes four-cycles in G[D]; original triangle-freeness excludes triangles. | Predecessor §2 | Checked |
| P4 | Three generated neighbors plus label 4 are nonheavy, so r_i≤4. | Predecessor §2 | Checked modulo normalized-row import |
| P5 | Positive sign product would lift each base 3/4-cycle to an original cycle of the same length. | Predecessor §2 | Checked |
| P6 | Count common-heavy-neighbor endpoint pairs to obtain Σr_i²≤2d(d−1), with the exact equality matrix. | Predecessor §3 | Checked |
| P7 | Restrict equality matrix to antisymmetric vectors to get Z²+Z=diag(r); commuting forces equal degrees across edges. | Predecessor §4 | Checked |
| P8 | Integer balancing excludes equality for d=5,7; the irreducible polynomial x²+x−4 cannot act on a rational space of dimension 9. | Predecessor §5 | Checked |
| P9 | Distance one or two excludes E_G(D_i,S_j); additional diameter assumption gives D-to-W and repeat-port counts. | Predecessor §6 | Checked modulo port imports |
| N1 | Three common neighbors force a positive four-cycle by equal path signs. | New §1.1 | Checked |
| N2 | Two triangles sharing an edge force a positive four-cycle; a=m−3t and a_i=r_i−2t_i. | New §1.2 | Checked |
| N3 | Multiply three prism rectangles: product is −1 but also the product of two negative triangles, +1. | New §1.3 | Checked |
| N4 | Exhaustive endpoint codegree count yields ε_i=2d−2−Σ_{j~i}r_j=a_i+b_i+2c_i and its summed identity. | New §2 | Checked |
| N5 | Distance at least three gives disjoint closed neighborhoods and r_i+r_j≤d−2, with no stronger use. | New §2 | Checked |
| N6 | Degree deficiency from 4 sums to two, giving exactly A=(4^7,3^2) and B=(4^8,2); squares and triangle bounds give t=4 or 5. | New §3 | Checked |
| N7 | Triangle intersection graph is simple and triangle-free; t=5 forces K_2,3 and hence a prism. | New §4 | Checked |
| N8 | Pattern B has ε_z=8 but a_z+b_z≤3 after t=4. | New §5 | Checked |
| N9 | Pattern A local slack and b+2c=2 exhaust two cases; incidence counting or triangle union size contradicts each. | New §6 | Checked |
| N10 | Heavy degree sum 144 consumes 4m internally and 54 on own generated triples; conditional diameter use is preserved. | New consequences | Checked |

All arguments are finite exact graph/matrix arguments. There are no asymptotic parameters, limit orders, analytic interchanges, probability-mode changes, or unresolved side conditions within this scope.
