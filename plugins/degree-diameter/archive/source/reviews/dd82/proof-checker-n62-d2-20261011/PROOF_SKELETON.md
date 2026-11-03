# D2_MATCH proof-obligation ledger

Status: all obligations below discharged in the reviewed source; semantic judgment is same-family/provisional. Source line numbers refer to `proofs/dd82/n62/D2_MATCH_SATURATED_ROW_EXCLUSION.md`.

## Symbols and assumptions

| Symbol or hypothesis | Type or exact meaning | Verification |
|---|---|---|
| G | finite simple undirected graph, 62 vertices, maximum degree ≤ 8, diameter ≤ 2 | Theorem hypothesis, lines 5 and 15 |
| A | actual 62×62 symmetric zero-diagonal {0,1} adjacency matrix | Definition, line 15 |
| B | A² + A − 7I − J, an actual 62×62 defect matrix | Lines 17–25; direct derivation in audit |
| X | N(0) = {1,…,8}, independent | Local template premise, line 29 |
| P(v) | N(v) ∩ X for v outside the closed root neighborhood | Parent-set premise; recovered reduction line 205 |
| w,a | distinct vertices outside the closed root neighborhood, parents 123 and 12, with wa a nonedge | Lines 29–31; original JSON labels 9,10 |
| Ci | disjoint singleton-parent class with sole parent i | Line 33; original JSON exact partition |
| c(u,v) | nonnegative integer count of common neighbors | Line 23 |
| t(u) | nonnegative integer count of triangles containing u | Line 27 |
| c | unique remaining unit endpoint of row a, later proved in C3 | Lines 76–102 |
| d | unique actual a-neighbor in C3, distinct from c | Line 161 |
| ex | coordinate unit row at vertex x | Row notation in lines 58–72 |
| e(C1,C3) | number of original A-edges between disjoint classes | Lines 149–155 |

The common-neighbor function and vertex both use the letter c; their arity distinguishes them. No premise asserts a globally specified B-support pattern or a realizability lift. Global B ≤ 2 and the archived local restrictions at w are not used. The class sizes 5,5,6 follow from regularity and the exact parent sets, rather than being additional graph assumptions.

## Dependency DAG

Graph hypotheses → regularity → actual defect identities and triangle-budget identity.

Parent partition + regularity → class sizes and exact parent neighborhoods.

Defect identities + parent partition → saturated rows 0,1,2,w → triangle-freeness at 1,2,w.

Saturated rows + commutation → c ∈ C3 and complete row a → ac nonedge.

Saturated rows + triangle budget → triangle-freeness at 3 → independence of C3.

Saturated rows + commutation → B3,C1∪C2 = 0.

Complete row a + saturated rows + class sizes + commutation → complete B-support of C1,C2 and unit endpoints from C3\{c}.

Saturated rows + exact common-neighbor identities + triangle-freeness at 1,2 → actual C1–C2 matching.

B3,C1 = 0 + exact common-neighbor identities → five A-edges C1–C3 → unique d adjacent to a, d ≠ c, with no neighbors in C1 or C2.

Unit B-endpoint from d + actual matching → (AB)yd ≥ 1.

Complete row By + d avoiding C1 + independence of C3 → (BA)yd = 0.

Commutation → contradiction. There is no dependency cycle.

## Micro-claims in sequent form

| ID | Context ⇒ conclusion; rule and discharge | Source |
|---|---|---|
| MC01 | Degree bound and diameter ⇒ regularity 8; root count ≤57 for any degree ≤7 | 15; recovered 44 |
| MC02 | Actual adjacency and regularity ⇒ B symmetric, nonnegative integral, zero diagonal, row sum 3, AB=BA; direct matrix algebra | 17–25 |
| MC03 | Exact parent partition and degree 8 ⇒ |C1|=|C2|=5, |C3|=6 | 29–41 |
| MC04 | Parent sets ⇒ B0w=2, B0a=1 ⇒ complete row 0; row saturation | 54–58 |
| MC05 | Independent X and singleton parents ⇒ exact common-neighbor counts 3,2,2 for 12,13,23 | 60–62 |
| MC06 | MC05 and row sums ⇒ complete rows 1,2 ⇒ t(1)=t(2)=0 | 64–68 |
| MC07 | Nonedge wa with two common parents and Bw0=2 ⇒ Bwa=1 and complete row w ⇒ t(w)=0 | 70–74 |
| MC08 | Exact Ba0=Baw=1, diagonal zero, integrality ⇒ one distinct remaining endpoint c with weight one | 76 |
| MC09 | Commutation (0,a), wa nonedge ⇒ all BX,a=0 ⇒ c is a singleton-parent vertex | 78–86 |
| MC10 | Commutation (1,a) and (2,a), complete rows ⇒ c∉C1∪C2 | 88–94 |
| MC11 | Commutation (1,c), Bac=1 and c∉C2 ⇒ A3c=1 ⇒ c∈C3 | 96–102 |
| MC12 | Complete row a, 0,w nonneighbors, even triangle budget ⇒ ac nonedge and t(a)=0 | 104–106 |
| MC13 | B31=B32=1 at nonneighbors, even triangle budget ⇒ t(3)=0 ⇒ C3 independent | 108 |
| MC14 | Commutation (1,3),(2,3), nonnegative entries ⇒ B3x=0 for x∈C1∪C2 | 110–116 |
| MC15 | x∈C1, commutation (2,x), complete rows 0,w,a ⇒ sum of B-weight into C2 equals 2 | 118–120 |
| MC16 | q∈C3, commutation (1,q), complete rows 0,w,a ⇒ sum from C1 is 1−1(q=c) | 122–131 |
| MC17 | MC15, MC16 and class sizes 5,6 ⇒ every C1 row has weight 1 into C3 and no support elsewhere | 133–137 |
| MC18 | Identical premises with labels 1,2 exchanged ⇒ C2 row support in C1∪C3; unit endpoints for q≠c | 135–141 |
| MC19 | Pair 2,x for x∈C1 is nonadjacent with B2x=0; t(1)=0 excludes w,a ⇒ exactly one actual C2 neighbor | 143–147 |
| MC20 | Symmetric MC19 ⇒ actual perfect matching between C1,C2 | 147 |
| MC21 | Nonedge 3,x with B3x=0 and excluded common-neighbor locations 0,w ⇒ each x∈C1 has one C3 neighbor ⇒ five A-edges | 149–155 |
| MC22 | Nonedge 1,q with B1q=0 and excluded locations 0,w ⇒ Aaq+|N(q)∩C1|=1 | 157–159 |
| MC23 | MC21,MC22, six points of C3 ⇒ unique a-neighbor d in C3; MC12 ⇒ d≠c | 161 |
| MC24 | Pointwise MC22 and its parent-2 counterpart with Aad=1 ⇒ d avoids C1∪C2; MC13 ⇒ d avoids C3 | 161–165 |
| MC25 | MC16 at d≠c, integrality ⇒ x∈C1 with Bxd=1; MC20 ⇒ mate y∈C2 with Ayx=1 ⇒ (AB)yd≥1 | 167–169 |
| MC26 | MC18 support of By and MC24 absence of A-neighbors ⇒ (BA)yd=0 ⇒ contradiction to MC02 | 171–175 |

Every application uses only hypotheses established earlier or the explicitly stated template premises. There are no asymptotic, probabilistic, limiting, or analytic interchange obligations. Counterexample attacks on the key deductions are recorded in `PROOF_AUDIT.md`.
