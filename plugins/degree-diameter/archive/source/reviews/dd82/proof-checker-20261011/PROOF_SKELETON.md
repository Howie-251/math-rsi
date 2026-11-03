# Proof skeleton — bounded fresh review

Reviewer: `/root/proof_review`; native Codex review, same-family, provisional. Caller requested `gpt-6-astra`, effort `ultra`, `fork_turns:none`; the spawn accepted those parameters. This is routing metadata, not independent backend attestation. Full source files were read; prior audit outputs were not read. Review date: 2026-10-11.

## Sources

- `C4`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/h5_zero_r2_c4_interface_20261011.md`
- `Brown57`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/BROWN57_PROOF.md`
- `Edit`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/BROWN_EXTENSION_OBSTRUCTION.md`
- `Foundations`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/FOUNDATIONS.md`

Line references below use these aliases.

## Typed symbols

- `G`: finite simple undirected graph; `n=|V(G)|`; maximum degree at most 8; every distinct pair is adjacent or has a common neighbor.
- `A ∈ {0,1}^{n×n}`: symmetric zero-diagonal adjacency matrix. `B=A²+A−7I−J ∈ Z^{n×n}`: graph-derived defect matrix, used after 8-regularity. In Brown57 and Edit, the letter `B` instead denotes the fixed Brown graph; the contexts are separate and unambiguous.
- `δ=65−n ∈ Z≥0`; `t(v) ∈ Z≥0`: number of triangles containing `v`.
- In C4: `z_i`, `i∈Z/4Z`: four distinct vertices with `t(z_i)=0`; `X_i`: external vertices adjacent exactly to `z_i,z_(i+1)` among the four; `s_i`: the unique external vertex adjacent only to `z_i`; `P={s_i}`; `X=⋃X_i`; `W`: external vertices with no `z` adjacency.
- In C4: `T,C ∈ {0,1}^{4×4}` are the diagonal matching and cyclic adjacency matrices; `U ∈ {0,1}^{4×55}`, `D ∈ {0,1}^{55×55}` are actual graph adjacency blocks. `L ∈ Z^{4×55}` is the corresponding B block. `δ_i=A(s_i,s_(i+2)) ∈ {0,1}` is distinct from scalar graph defect `δ`.
- In Edit: `C,I,E ⊆ V(B)` partition the 57 old vertices; `E` is a vertex class, while `E(B)` is an edge set. `R=E(B)\E(G)`; `r=|R|`; `S=N_G(x)`; equality-case `D=C∪{deleted-edge endpoints}` is a vertex set, not C4's matrix.
- In Foundations §3: `T` is a rational-linear endomorphism; `k` is the rational parameter of an irreducible quadratic; `K=Q[X]/(X²+X−k)` is a quadratic field. No graph `T` is used in this section.

## Canonical statements and assumption discharge

| ID | Quantified statement | Hypotheses and applications |
|---|---|---|
| F1 | Every original graph has `n≤65`; if `n>57`, every vertex has degree 8. | Finite/simple/undirected/degree≤8/path property: Foundations L11, L19–23. Covers the empty graph separately. Applied to C4 at L22 (`n=59`), Edit at L29 (`n=58`), and F2–F6 (`n>57`). |
| F2 | For every original graph with `n>57`, `B≥0`, `diag B=0`, `B1=δ1`, `AB=BA`, and `2t(v)+Σ_(u outside N[v])B_vu=δ` for every `v`. | 8-regularity from F1; actual adjacency and nontruncated integer subtraction: Foundations L27–43. C4 uses `δ=6`; Edit uses the equivalent radius-two count with `δ=7`. |
| F3 | Every finite-dimensional rational operator satisfying an irreducible `T²+T−kI=0` has dimension `2a` and trace `−a` for an integer `a≥0`. | Irreducibility makes the quotient a field. A K-basis decomposes into Q-bases `(v,Tv)`: Foundations L47. For applications, 29 and 33 are nonsquares: L49. Includes dimension zero. |
| F4 | No original graph has 65 vertices. | F1/F2 give `B=0`; the rational sum-zero invariant space has dimension64 and satisfies k=7; constants form a complementary eigenline with eigenvalue8: L53. F3 gives incompatible trace `−24`. |
| F5 | No original graph has 64 vertices. | F2 gives a perfect-matching defect matrix commuting with A; its rational +1 space has dimension32. Intersecting with sum-zero gives invariant dimension31 and k=8: L57. F3 forces even dimension. |
| F6 | Every original graph has order at most63. | F1, F4, F5; no inference about exclusion of any order58–63. Foundations L59. |
| B1 | The displayed 57 projective representatives over F7, with distinct orthogonal points adjacent, form an original graph. | Normalization, nonzero linear functional, and independence of distinct normalized representatives: Brown57 L26–29. A common solution for nonadjacent vertices cannot be an endpoint. |
| E1 | Every original graph on the fixed old Brown vertex set plus one new vertex deletes at least8 Brown edges and adds the same number of old edges. | F1; the Brown finite premises at Edit L14–18 (independently checked); surviving old triangles cannot be removed by additions. Equality arguments use final degree exactly8, not merely an upper bound. |
| C1 | In every original graph of order59, no four distinct zero-triangle vertices satisfy the displayed cyclic B=2 and matching-row support conditions. | F1/F2; all four local row conditions; zero triangles only at the four designated vertices. No N4, global N15, global t≤2, solver, or external structural classification used. |
| C2 | Conditional on the accepted H5⇒N15 implication applying to its zero vertices, H5 admits no all-zero R2 four-cycle component. | C1; H5⇒N15 is explicitly imported/assumed at C4 L12 and L80, not established or independently reviewed here. |
| C3 | Every hypothetical C1 configuration satisfies interfaces (1)–(5). | Actual 0/1 adjacency blocks as defined at C4 L28, plus C1's Steps1–5. The reverse construction statement is read with the same adjacency-matrix domain for D. The full B and degree checks are required; equations (1)–(5) alone are not sufficient. |

The same-weight adjacency condition for the two light supports is not needed for C1's exclusion; it is correctly recorded in C3 at C4 L101. This unused assumption does not invalidate the result.

## Dependency DAG

`original graph assumptions → F1 → F2`; `rational quadratic field argument → F3`; `F1,F2,F3 → F4,F5 → F6`.

`F7 linear algebra → B1 → finite Brown premises`; `F1 + finite Brown premises → E1`.

`F1,F2 + four local matching rows + four zero-triangle vertices → C1`; `C1 + assumed H5⇒N15 → C2`; `C1 Steps1–5 → C3`.

No cyclic dependency was found. C1's contradiction does not use C3.

## Micro-claims

| ID | Context ⊢ conclusion | Rule and checked side conditions |
|---|---|---|
| MC01 | Root degree d ⊢ `n≤1+8d` | Every neighbor has at most7 other neighbors; overlaps reduce the union; genuine path property supplies coverage. |
| MC02 | 8-regular original graph ⊢ F2 | Diagonal/row-sum multiplication; off-diagonal path count; symmetry and `AJ=JA=8J`; triangles counted twice on incident edges. |
| MC03 | Irreducible quadratic annihilates T ⊢ F3 | Polynomial inverse modulo q makes a K-action; basis block `[[0,k],[1,−1]]` has trace−1. |
| MC04 | `n=65` ⊢ contradiction | Nonnegative zero-sum B rows vanish; rational constants plus sum-zero are a direct invariant decomposition. |
| MC05 | `n=64` ⊢ contradiction | Integral B rows of sum1 and zero diagonal form disjoint pairs; the sum functional is nonzero on the +1 space, so its kernel has dimension31. |
| MC06 | Distinct normalized F7 representatives ⊢ rank-two orthogonality system | Nonproportional rows are independent; rank2 on dimension3 leaves a nonzero common solution. For a nonadjacent pair, either endpoint solution would contradict nonadjacency. |
| MC07 | C1 hypotheses ⊢ internal diagonal matching | A B=2 pair involving a zero vertex cannot be adjacent: an adjacent pair has B equal to its triangle count. Heavy-support pairing forces both diagonals. |
| MC08 | Internal matching and zero triangles ⊢ `|X_i|=3`, four private vertices, `|W|=39` | An external vertex cannot meet a diagonal twice. A cyclic pair has exactly3 common neighbors and none internal. Degree8 then leaves exactly one private neighbor per z. |
| MC09 | Matching rows ⊢ `B[z,X]=0` | Actual z–X edges have no triangle. Any other positive entry is light and its X endpoint is adjacent to a heavy support of that row, contradicting mixed-weight nonadjacency. |
| MC10 | MC09 and exact codegrees ⊢ X independent, no X–P edges, each X has6 W neighbors | Shared z adjacency forbids a triangle; the two nonincident z's already have a unique common neighbor in the internal matching, forbidding an additional one. |
| MC11 | z–private nonadjacent consecutive pair ⊢ private cyclic edge | No X–P or z–W edge; the only possible common neighbor is the corresponding private vertex. Diameter2 forces that edge. Private diagonals remain allowed. |
| MC12 | All four z covered from w ⊢ `d_X(w)+h(w)≥2` | d_X≥2: immediate. d_X=1: uncovered labels are consecutive, forcing their private edge inside N(w). d_X=0: all four private vertices required, h≥4. |
| MC13 | `|W|=39`, 72 X–W edges, MC12 ⊢ `Σ_P t≥12+3T_P` | Sum charge: H≥78−72=6. Each P-P-W triangle contributes exactly2 P incidences; internal P triangles contribute3; classes are disjoint. |
| MC14 | MC13 and F2 ⊢ contradiction | Initially t≤3, hence T_P=0 and no private diagonal. Opposite private vertices are then nonadjacent with ≥2 common neighbors, so each has ≥1 nonedge repeat. `6−2t≥1` plus integrality gives t≤2; total≤8 contradicts≥12. |
| MC15 | Actual block adjacency ⊢ C3 | Multiplication gives `UUᵀ=7I+3C`, internal B=2C, `L=TU+UD+U−J`; private L is only the optional opposite entry δ_i. Remaining row mass is 2−δ_i. Private W degree is5−δ_i. |
| MC16 | Edit premises, n=58 ⊢ `r≥7` and edge balance | F1 forces232 total edges and8 new-vertex edges, leaving224 old edges. Each of21 I vertices needs an old triangle destroyed; each removed edge destroys at most1 triangle, each triangle covers at most3 I vertices. |
| MC17 | `r=7` ⊢ disjoint III triangles and a deletion matching | All inequalities `21≤destroyed I incidences≤3·destroyed triangles≤3r` are equalities. Each I is covered exactly once; each deleted edge lies in its own destroyed triangle. |
| MC18 | MC17 + final degree8 ⊢ S lies in22 unit deficits, no added old edge touches S | Degree8 vertices cannot gain an edge; deficit vertices require exactly one added incidence. Membership in S already spends it on x. |
| MC19 | MC18 + no Brown C–(C∪I) edge ⊢ contradiction | Every c outside S has no possible x–S–c path, so S contains C and size8 gives S=C. Every I vertex then remains unreachable from x in ≤2 steps. |

There are no probability claims, limits, integral/expectation interchanges, asymptotic constants, or uniformity obligations in these proofs. All counts are finite exact integers.
