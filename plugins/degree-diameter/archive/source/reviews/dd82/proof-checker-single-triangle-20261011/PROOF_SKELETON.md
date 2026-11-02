# Proof skeleton and obligation ledger

All obligations below are discharged analytically under the explicit original-graph and N15 hypotheses. This is the skeleton of the conditional theorem, not a proof that N15 holds in every graph.

## Assumption ledger and typed symbols

- G: finite simple undirected graph, |V|=59; maximum degree ≤8; every distinct vertex pair has a path of length one or two. These are main-theorem hypotheses. They imply 8-regularity by 59≤1+8d(x).
- A: actual 59×59 integer adjacency matrix of G; B=A²+A−7I−J: actual symmetric, nonnegative integer defect matrix with diagonal zero and row sums six. AB=BA follows from regularity.
- A zero vertex belongs to no triangle. For each such vertex, the complete positive B row is 2,2,1,1 and its support induces exactly the two same-weight edges in G. This is the explicit N15 hypothesis, not an inherited conclusion.
- T: nonnegative integer number of undirected triangles; C₄,C₅: numbers of simple undirected cycles of the indicated lengths, allowing chords. T=1 is used only inside the contradiction argument.
- s=tr(B²), w_tr=tr(AB²): scalar integer traces. The source reuses the glyph w for a triangle vertex later; in each formula the context distinguishes them. No identity mixes the types.
- q_r,a_r,c_r,e_r: scalar integer row statistics for a triangle vertex r, as defined in H5 lines 11–19. Q₂(r) is half the quadratic form of the actual row-support vector. All are evaluated in the same graph.
- u,v,w: the three distinct vertices of the unique triangle, relabeled so c_w=2 and c_u=c_v=1.
- P_u,P_v,P_w: disjoint six-element private neighborhoods. R: their complement after deleting u,v,w, of cardinality 38. All these vertices are zero.
- R_u,R_v,R_w⊆R: actual sets of weight-one repeats of the corresponding triangle vertex, with cardinalities 2,2,4. Overlap is unrestricted.
- h_uv,h_uw: nonnegative integer intersection sizes. k_uv,k_uw: numbers of unordered heavy pairs in disjoint private-neighborhood blocks. ℓ_uv: number of light cross pairs, at most two.

## Dependency DAG

Original graph hypotheses → regularity/B foundations → global trace identities and positive-zero-endpoint product identity.

Global trace identities + N15 → fifth-walk congruence.

T=1 + foundations + endpoint identity → triangle-row types and q=a+2c → local c ranges.

Local ranges + heavy-graph parity + fourth-walk integrality + fifth-walk congruence → four row candidates.

Four candidates + actual private-neighborhood common-neighbor count → unique row candidate + two cross matching edges.

Unique candidate + endpoint identity → support normal forms + remainder repeat sizes/edges.

Remainder repeat structure + common-neighbor identities → internal light pairs → light cross restrictions.

Remainder incidence counts + light restrictions → at least 3+4 heavy cross pairs.

Actual independence of P_v∪P_w + heavy partner adjacency → at most 6 heavy cross pairs → contradiction.

No edge in this DAG points back to the desired exclusion. The optional R₂ short-cycle corollary is outside the DAG.

## Micro-claim inventory

| ID | Context and goal | Rule and side-condition discharge | Source |
|---|---|---|---|
| MC01 | Graph hypotheses ⊢ 8-regularity | Root-ball upper bound 1+8d; 59>57 | Main 15 |
| MC02 | MC01 ⊢ B diagonal 0, B≥0, row sums 6, AB=BA | Actual adjacency, path premise, regular AJ=JA | Main 17–23 |
| MC03 | Zero endpoint on actual edge ⊢ B=0 | Any common neighbor would make a triangle | Main 23 |
| MC04 | Positive B pair at zero endpoint ⊢ (AB)_xy=B_xy | N15 full induced support, MC02 symmetry/commutation | H5 65–69 |
| MC05 | MC04 ⊢ trace-difference localization | Finite trace sums; zero B terms vanish | H5 71–75 |
| MC06 | MC01–02 ⊢ trace formulas through degree five | Exact matrix identities and finite traces | Global 53–79 |
| MC07 | Simple 8-regular graph ⊢ tr(A⁵)=10C₅+210T | Simple walks; unique used triangle for nonsimple words | Global 81–89 |
| MC08 | MC06–07 + N15 ⊢ remainder congruence | s_zero=10, 2Q₂_zero=10; integral C₅ | Global 91–109 |
| MC09 | MC08 + T=0 ⊢ contradiction | 10 does not divide 24662 | Global 103 |
| MC10 | T=1 + MC02–03 ⊢ residual row types 22,211,1111 | Residual mass 4; every nonedge repeat is zero and has entry ≤2 | H5 77 |
| MC11 | MC04 + MC10 ⊢ q=a+2c and e=4−c | Same actual row quadratic form counted twice | H5 79–92 |
| MC12 | T=1 + MC11 ⊢ necessary local c ranges | Zero repeat cannot meet both other triangle vertices | H5 94–96 |
| MC13 | MC10 ⊢ even number of 211 rows | Degree-sum parity in actual nonedge B=2 graph | H5 98 |
| MC14 | MC08 + T=1 ⊢ Σc≡4 mod5 | e=4−c for each of three triangle rows | H5 100 |
| MC15 | MC06 + row squares ⊢ n₂₁₁+2n₁₁₁₁≡2 mod4 | Four-walk identity, integral C₄ | H5 102–116 |
| MC16 | MC12–15 ⊢ exactly four necessary row candidates | Exhaustive small integer partitions, including all labels | H5 118–125 |
| MC17 | T=1 ⊢ disjoint independent private six-sets | Regularity; each violation creates another triangle | H5 129–133; Main 33 |
| MC18 | MC17 ⊢ a_u=m_uv+m_uw cyclically | Actual common-neighbor identity B_ux=d_Pu(x) | H5 133–139 |
| MC19 | MC16 + MC18 ⊢ unique all1111 candidate, m=(2,0,0) | Nonnegative cross-edge counts impose triangle inequalities | H5 141–145 |
| MC20 | MC19 ⊢ two cross edges form matching | Cross degrees equal entries in all1111 triangle rows, hence ≤1 | H5 145 |
| MC21 | MC04 + MC19 ⊢ complete support forms | Unit weights make each zero repeat's support degree exactly 1 | H5 147–151 |
| MC22 | MC17 + MC19–21 ⊢ R sizes and edges, cardinality(R_w)=4 | Exhaust all private/triangle locations of repeats; no disjointness premise | H5 153; Main 35–41 |
| MC23 | MC22 ⊢ d_Pu(x)=1+1_Ru(x), and cyclic formulas | All common neighbors with u are in P_u for x∈R | Main 47–51 |
| MC24 | MC20 ⊢ B_pv=1 exactly for active p | Common neighbors are u and P_v neighbors | Main 53–57 |
| MC25 | MC17,20,22,23 ⊢ two disjoint internal light pairs | Common neighbors only u,R; adjacent R_u points have disjoint parent pairs | Main 59–63 |
| MC26 | MC24–25 + N15 ⊢ internal pairs use all inactive points | Active internal endpoint would force forbidden qv edge | Main 65 |
| MC27 | MC24,26 + N15 ⊢ no P_u–P_w light pairs | Other known light endpoint has no neighbor in P_w | Main 67–71 |
| MC28 | MC20,26 + N15 ⊢ at most two P_u–P_v light pairs | Inactive endpoints excluded; two actual active edges have B=0 | Main 73 |
| MC29 | MC17,20,23 ⊢ B block totals 8+h_uv,8+h_uw | All common neighbors in R; count 36 pairs and actual cross edges | Main 79–103 |
| MC30 | MC27–29 ⊢ k_uv≥3, k_uw≥4 | Entries 0,1,2; h≥0; ≤2 and 0 light entries | Main 93–109 |
| MC31 | MC17,19 + N15 ⊢ k_uv+k_uw≤6 | P_v∪P_w independent; each of six P_u points contributes ≤1 | Main 113–115 |
| MC32 | MC30–31 ⊢ T≠1 | 7≤k_uv+k_uw≤6 | Main 117 |

All finite sums and inequalities use fixed exact integer data. There is no limit-order map or probability-mode obligation. The only unapplied external premise remains N15 itself, explicitly included in the main theorem.
