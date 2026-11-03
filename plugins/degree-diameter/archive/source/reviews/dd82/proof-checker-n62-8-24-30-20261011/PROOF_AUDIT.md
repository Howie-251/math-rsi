# Fresh proof audit: the actual 8,24,30 quotient exclusion

**Verdict: PASS — all proof obligations discharged.** There are no open fatal, critical, major, or minor mathematical issues in `proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md` as reviewed. The proof excludes precisely the stated actual quotient. It does not establish quotient-enumeration coverage, exclude arbitrary order-62 graphs, or determine N(8,2).

This is a fresh Codex review under the project-local `proof-checker` skill. `review_independence: same-family`; `acceptance_status: provisional`. The parent reports the explicit invocation `model: gpt-6-astra`, `reasoning_effort: ultra`, `fork_turns: none`. Actual backend identity is not independently attested. Reviewer task identifier: `/root/proof_review_n62_8_24_30`. One review round; no source changes or fixes were required.

The user-directed output is Markdown/JSON only. No hashes, checksums, HTML, TeX, PDF, solver work, or order-63–65 work were generated. The obligation skeleton and audit state are embedded here and in `PROOF_AUDIT.json`.

## Reviewed statement and source map

For every finite simple undirected graph G on 62 vertices, if its maximum degree is at most 8 and its diameter is at most 2, there do not exist its actual positive-repeat-support components C,K,L, of sizes 8,24,30, respectively, whose original adjacency quotient, with source component indexing rows and target component indexing columns, is

```text
        C K L
    C   2 6 0
    K   2 1 5
    L   0 4 4.
```

The component sizes sum to 62, so these are all components. The repeat matrix is the actual B=A²+A−7I−J, not an independently prescribed matrix.

Target line map:

| Lines | Content |
|---|---|
| 5–22 | Claim, quotient orientation, and limited scope |
| 26–59 | Actual identities; triangle-freeness and simplicity of B[C] |
| 63–67 | Matching P, incidence X, parent pair F |
| 84–107 | Cross-block equation and exclusion of G[C]=C8 |
| 111–150 | Two four-cycles, multiplicities, opposite-label symmetry, connectedness |
| 154–207 | Zero-label choice, weighted commutation marginals, contradiction |
| 209–222 | Dependencies and non-claims |

Direct dependencies read and checked at the scope used:

- `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Sections 3–4: component equitability and the D1 incidence bounds. Its other spectral and port conclusions are not required.
- `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`, Sections 1–4, together with `S_TOUCH_SATURATED_ROW_EXCLUSION.md`: every original triangle lies in a closed six-vertex repeat component. The final global simple-repeat exclusion is not required.
- `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`, Sections 1–2: closure of both surviving D0 types. Its global parity/outlet theorem is not required.
- `D2_MATCH_SATURATED_ROW_EXCLUSION.md` and `D0_EDGE_BIN_SATURATED_ROW_EXCLUSION.md`: the two excluded double-root types.
- `RECOVERED_REDUCTION.md`, actual identities and the double-root parent classification in Step 6. Its triple-repeat finite enumeration is not used as audit evidence; the quotient gives a direct exclusion of entries three, recorded below.
- `D1_MATCH_HARD_BRANCH_REDUCTION.md`: normalized D1 parent data and the local rows underlying the cited incidence bounds. The minimum-size, spectral-classification, and harder transport results are not required.

No prior audit output was used as evidence. The old partial `THREE_COMPONENT_8_24_30_REDUCTION.md` was not read as a proof replacement. The read dependency papers are not being given separate blanket verdicts here.

## Assumptions, symbols, and dependency structure

All matrices are finite. A is a symmetric binary 62×62 adjacency matrix with zero diagonal. B is symmetric, nonnegative integral, zero-diagonal, and has row sum 3. It obeys AB=BA and c(x,y)+Axy=1+Bxy for distinct vertices. These follow from the actual graph hypotheses: a vertex of degree at most 7 reaches at most 57 vertices within two steps, hence G is 8-regular. The formula for B then supplies the stated row sum and commutation. On original edges the repeat weight counts triangles, and 2t(x)≤3 gives t(x)≤1.

| Symbol | Type and meaning |
|---|---|
| C,K,L | Disjoint actual connected components of positive support of B |
| rUV | Integer original-neighbor count in V at every vertex of U |
| D | 8×8 matrix A[C,C] |
| X | 8×24 binary incidence matrix A[C,K] |
| P | 24×24 adjacency matrix A[K,K], a perfect matching |
| p | Fixed-point-free matching involution of K |
| F(v) | Two-element subset of C, the original parents of v∈K |
| ai,bj | Vertices of the two original four-cycles, i,j modulo 4 |
| o | Opposite-vertex involution within either four-cycle |
| M | 4×4 matrix with Mij=B(ai,bj), eventually binary |
| mij | Nonnegative integer count of vertices with parent pair {ai,bj} |
| U,V | Subsets of K covering o(ai), respectively o(bj), as parents |

There is no symbol-type drift. The target's component L and the all-ones matrix J are distinct; the temporary generated-triangle component J in the dependency paragraph is identified by context and never used in a conflicting equation.

The dependency DAG is acyclic:

```text
actual graph → actual A,B identities → component equitability
actual identities + S_TOUCH local contradiction → triangle pairing
triangle pairing + component sizes → triangle-free G
double-root parent classification + D2/BIN exclusions → D0 or D1
D0 closure + D1 incidences + target quotient → simple B[C]
target quotient + actual matrix identity → DX+XP+X=J
cross-block identity + triangle-freeness → G[C]=2C4 and opposite parents
simple B[C] + row budget + actual multiplicities + connected C → (6)–(8)
zero entry of M + matching → unique zero-weight intersection
AB=BA + weighted row budget → 4≤3.
```

No limiting, probabilistic, asymptotic, integration, differentiation, or uniformity argument occurs. The only sum regrouping is finite weighted inclusion-exclusion. Constants 8,24,30,2,3,4 are exact.

## Proof-obligation ledger

Every item below is discharged. Locations refer to the target unless another file is specified.

| ID | Obligation and verification |
|---|---|
| MC01 | **Actual identities** (26–37). The degree bound proves regularity; the actual definition of B gives its diagonal, nonnegative off-diagonal entries, symmetry, row sum 3, and commutation. No independent matrix realizability is assumed. |
| MC02 | **Closed triangle component** (44–46). The dependency's S_TOUCH contradiction uses only forced saturated unit rows, not global simplicity. Triangle mates avoid the original triangle neighborhood, are distinct by commutation, and themselves form a triangle by nonnegativity. Both triangles' six rows are exhausted, and the prism is connected. |
| MC03 | **Triangle-free G** (53–55). A triangle would force an actual support component of size 6. The three actual components have sizes 8,24,30 and cover all 62 vertices, excluding that possibility. Thus Buv=0 on every original edge. |
| MC04 | **Actual equitable quotient** (10–11,39–41). Symmetric row-sum-3 B has eigenvalue-3 vectors exactly constant on support components, by its nonnegative energy identity. AB=BA preserves that space, so A applied to every component indicator is constant on each actual component. The stated R therefore supplies genuine per-vertex neighbor counts. |
| MC05 | **No weight-three entry** (47). A weight-three entry exhausts both rows and makes its two endpoints a closed two-vertex support component. None of the stipulated components has size 2. Thus B≤2 follows directly in this quotient case; the global triple-repeat theorem is unnecessary. |
| MC06 | **Coverage of a double root** (47–48). At an endpoint 0 of a double repeat, its row is 2e_w+e_a and it is triangle-free. Every outside vertex has at least one parent; the actual row gives exactly the parent triple P(w), parent pair P(a), and otherwise single parents. Their intersection sizes 0,1,2 yield D0,D1,D2. Original adjacency w~a is possible only in the disjoint case; its remaining repeat label is BIN or BOUT. The read saturated-row proofs exclude D2 and BIN. This applies to an arbitrary chosen double edge, not merely an existential root. |
| MC07 | **D0 support size 4** (48,56). The read D0 proofs force two further distinct vertices and complete rows forming an alternating 2,1,2,1 cycle. All four rows are saturated; this is exactly a closed component, so a double edge in C cannot be D0. |
| MC08 | **D1 quotient orientations** (48–51). In raw D1 notation, B1=e2+e3+e4 places 1,2,3,4 in the generated-triangle component J. Vertex 0 in the heavy component H has these four original neighbors. Vertex 1 has the distinct neighbors 0,w,a in H. Equitability gives rHJ≥4 and rJH≥3 when H≠J, or rHH≥4 when equal. |
| MC09 | **B[C] is simple** (55–59). For a D1 heavy edge in C, J=C contradicts rCC=2<4; J=K contradicts the correctly oriented reverse entry rKC=2<3; J=L contradicts rCL=0<4. D0 and weight 3 have already been excluded. Nonnegative integrality leaves only 0 and 1 in B[C]. |
| MC10 | **Matching and parents** (63–67). rKK=1 makes the simple induced graph on K a perfect matching; rKC=2 gives two distinct parents in C per vertex. The matching map p is a genuine involution. |
| MC11 | **Cross-block equation** (84–87). B[C,K]=0 because C,K are distinct repeat components. A[C,L]=0. Therefore the (C,K) block of A²+A=7I+J+B is exactly DX+XP+X=J; there is no omitted path through L and no identity-matrix term. |
| MC12 | **Disjoint closed parent neighborhoods** (89–91). Column v of (D+I)X is the sum of the two closed-neighborhood indicators. Column v of XP is the indicator of F(p(v)), because P is a symmetric matching matrix. The right side is all ones, proving disjointness and the exact complementary pair, without a transpose error. |
| MC13 | **Eight-cycle contradiction** (93–103). A simple triangle-free 2-regular graph on 8 vertices is C8 or 2C4. In C8 the two closed neighborhoods are disjoint only at cyclic distance 3 or 4. At distance 3 their complement is an adjacent pair and creates a triangle with p(v). Hence all parents would be antipodal, and the six K-neighbors of each c would also neighbor its antipode. The bound c(c,c′)=1+Bcc′≤4 contradicts c(c,c′)≥6. |
| MC14 | **Opposite parent rule in 2C4** (105–115). Two three-element closed neighborhoods within one four-cycle cannot be disjoint. Parents therefore lie in different cycles. Each closed neighborhood omits exactly its opposite within its cycle, proving F(p(v))=o(F(v)). |
| MC15 | **Within-cycle repeat entries** (117–121). Adjacent cycle vertices have no common neighbor; opposite vertices have exactly their two cycle neighbors. No K vertex can have two parents in one cycle, and C has no original neighbor in L. The actual common-neighbor identity gives repeat weights 0 and 1 respectively. |
| MC16 | **Binary cross matrix and multiplicities** (123–132). Each B[C] row has one unit at its opposite and two units across cycles; symmetry gives both row and column sums 2 of binary M. Cross-cycle parent vertices have no common neighbor in C or L, so their common-neighbor count is exactly mij. They are nonadjacent, giving mij=1+Mij. |
| MC17 | **Simultaneous opposite symmetry** (134–136). The bijection p takes the full parent-label class (i,j) onto (i+2,j+2), including multiplicities. Thus mij=mi+2,j+2 and Mij=Mi+2,j+2. No uniqueness is presumed at a label of multiplicity 2. |
| MC18 | **Connectedness forces complementary entries** (138–150). If both row ones occupy j,j+2, opposite-label symmetry gives the same ones in row i+2. With the two opposite repeat edges these four vertices form a unit K4, exhausting all four rows. This would be a closed proper component of C. Hence every row has one one in each opposite column pair; interchanging the two actual cycles gives the column counterpart, proving both identities (8). |
| MC19 | **Unique opposite representative** (154–164). A binary row of sum 2 has a zero. At Mij=0, mij=1. Simultaneous opposite symmetry also gives mi+2,j+2=1. The opposite class's unique representative is p(v) by the matching rule. Triangle-free G then gives B(v,p(v))=0. |
| MC20 | **Weighted parent marginals and orientation** (166–193). Block diagonality of B gives B[C]X=XB[K]. Its (o(ai),v) entry is B(o(ai),ai)+B(o(ai),bj)=1+Mi+2,j=2; the right side is sum over w with o(ai)∈F(w) of Bwv, equal to the displayed Bvw by symmetry. At o(bj), the cross term is Mi,j+2, not Mi+2,j. Both equal 1 at a zero Mij, so both marginals are 2. |
| MC21 | **Exact intersection and its zero weight** (195–197). Every K vertex has exactly two parents, one from each cycle. Therefore membership in U∩V is equivalent to the exact opposite parent pair, not merely containing it. MC19 makes this intersection precisely {p(v)} and its repeat weight from v is zero. |
| MC22 | **Weighted contradiction and scope** (198–207). Finite inclusion-exclusion gives 2+2=B(v,U∪V)+B(v,p(v)). The second term is zero; nonnegativity bounds the first by B(v,K). Because K is the actual support component containing v, this equals the full row sum 3. Thus 4≤3. The argument allows weight-two entries anywhere in B[K]; no global or K-block simplicity was used. |

## Adversarial and counterexample pass

The following concrete break attempts were checked analytically. None yields a counterexample under the stated hypotheses. These tests supplement the derivations above; their failure is not the reason an obligation is accepted.

1. **Reverse the critical D1 incidence.** For heavy component C and generated component K the needed lower bound is rKC≥3, whereas rCK=6 is allowed. The target uses rKC=2, the correct reverse direction. Taking H=J is separately covered by the internal bound, and the remaining L case fails the forward bound rCL≥4.
2. **Collapse a double/triple repeat or its auxiliary points.** A weight-three pair is a closed size-2 component. The D0 proof prevents its auxiliary c-points from coinciding by a row/commutation bound before counting common neighbors, and forces the four heavy/light vertices to be distinct. The resulting size-4 component cannot be embedded as a proper connected subset of the stipulated C with extra positive edges.
3. **Use an alternative original cycle type.** A triangle-free simple 2-regular eight-vertex graph has no component of order below 4; the only cycle decompositions are 8 and 4+4. On C8, parents {0,3} have complementary pair {5,6}, which is adjacent. Parents {0,4} avoid that triangle but force the six-common-neighbor contradiction. Cyclic distances 1 and 2 already violate closed-neighborhood disjointness.
4. **Place both parents in one C4.** Each closed neighborhood has size 3 in a set of size 4, so overlap is unavoidable. Hence no extra K common neighbor can invalidate the claimed within-cycle repeat counts.
5. **Concentrate a row of M on an opposite pair.** For example, ones at (0,0),(0,2) force ones at (2,0),(2,2). Together with a0a2 and b0b2, this creates the closed unit K4. Dropping connectedness would indeed admit this local pattern; connectedness is part of the actual-component hypothesis and is used explicitly.
6. **Choose a label with Mij=1.** Such a label has multiplicity 2, so a uniqueness assertion there would be invalid. The proof deliberately chooses a zero label, whose existence and multiplicity 1 were proved. Matching both copies in multiplicity-2 classes does not affect the zero-label argument.
7. **Use a heavy repeat inside K to cover both marginals.** Arbitrary nonnegative integral repeat weights in K are permitted. A common supplier of the two parent marginals must lie in U∩V={p(v)}, whose weight is exactly zero. Heavy weights at different suppliers are still charged to the same total row budget 3, so cannot supply the required total 4.
8. **Allow a positive matching repeat.** Since vp(v) is an actual original edge, B(v,p(v)) counts its common neighbors. A positive value would create a forbidden original triangle; the proof has already established triangle-freeness from component sizes.
9. **Interpret C,K,L as arbitrary cells rather than support components.** This would break block diagonality, the connectedness argument, and the final row-budget equality. The theorem explicitly concerns actual support components; these properties were checked wherever used. No matrix relaxation is substituted for a graph.

## Optional dependency simplification

No target edit is needed for correctness. Its imported triple-repeat exclusion is stronger than necessary here. Directly, Buv=3 with u≠v and nonnegative row sum 3 forces every other entry in rows u and v to vanish. Thus {u,v} is an entire connected support component. Since 8,24,30 are all component sizes, this is impossible. This removes any need to invoke the recovered global triple-repeat finite enumeration for the present quotient.

Similarly, the exact D1 incidence bounds used here follow from the raw D1 parent sets P(w)={1,2,3}, P(a)={1,4}, and the complete row B1=e2+e3+e4. The deeper reroot and minimum-component-size results can be left outside this theorem's logical dependency chain. These observations simplify dependencies without strengthening any hypothesis or widening the conclusion.

## Final audit state

One new theorem was audited, with 22 discharged obligations and no open issues. No critical/fatal fix or second-round fix review was needed. The source is unchanged. The fresh same-family mathematical verdict is **PASS**, with acceptance **provisional**. Cross-family acceptance, Lean formalization, the separate quotient enumeration, other repeat-component quotients, arbitrary order-62 exclusion, and the full N(8,2) goal are outside this audit.
