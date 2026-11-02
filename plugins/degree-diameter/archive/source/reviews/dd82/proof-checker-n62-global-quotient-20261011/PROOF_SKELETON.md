# Global double-triangle quotient: proof skeleton

Input: `proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, all 284 lines and all six sections. This review uses the actual finite simple undirected graph and actual B=A²+A−7I−J. No author source was edited.

## Quantified scope and import ledger

For every actual 62-vertex graph of maximum degree at most eight and diameter at most two, assume the established neighboring-paper reductions cited in the source: triple-repeat exclusion, triangle pairing, the root-template classification and D2/BIN exclusions, D0 component structure, and the hard-D1 reduction including the C4 light-mate lemma. Then conclusions (1)–(11) and the stated motif/component restrictions follow. These are necessary consequences; they neither exclude an order-62 graph nor establish evenness of D1 double-edge counts.

The actual identities imply degree eight, symmetric nonnegative integral B with zero diagonal and row sum three, AB=BA, and the triangle budget. The imported coverage and exclusions leave every double edge either in a closed D0 component or in the proved D1 structure. D0 has two double edges per component. D1 light mates have three distinct unit repeats, hence cannot themselves be double-edge endpoints. Universal triangle pairing supplies closed unit-repeat prisms and preserves original triangle status along positive repeats.

Imports inspected/reused:

- `RECOVERED_REDUCTION.md`: exact original-graph identities and root-template coverage; global triple exclusion is a declared prior import, not rerun here.
- `D2_MATCH_SATURATED_ROW_EXCLUSION.md` and `D0_EDGE_BIN_SATURATED_ROW_EXCLUSION.md`: their actual-parent scope and saturated-row arguments were inspected. These exclude the missing double templates; they do not depend on the present quotient.
- `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`: the local four-row components, their c_i construction, and the original induced matching/independence conclusions.
- `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`: paired original triangles lie outside each other's original neighborhoods; all six repeat rows close.
- `D1_MATCH_HARD_BRANCH_REDUCTION.md` and `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`: the actual rows, endpoint locations, rerooting, and absence of unit B triangles at both light mates. These were previously directly audited in this reviewer thread (PASS36 and PASS25).

The use of a finite-check-dependent triple exclusion is explicit in this global note. No finite checker or solver is newly run by this audit.

## Typed symbols and dependency DAG

A and B are actual 62×62 matrices. D is the set of double-edge endpoints; d is their unordered edge count. S_e is a three-vertex common-neighbor set, and S is its disjoint union over double edges. T counts original G-triangles. Components are positive-support B-components, not G-components. R is a k×k integer neighbor-count quotient; n_i are positive component sizes. The letter b denotes a D0 original vertex locally in section 2, a D1 endpoint locally in section 4, and a scalar count of D0_BOUT components in equation (6); these uses have separate declared scopes. H,K in section 4 denote B-components, not the local C1 ordinary class from the imported D1 paper. W in section 5 denotes the global complement, not the earlier local W_i neighborhood set. The signed-eigenspace matrix below is denoted M in the audit to distinguish it from R.

Dependency graph:

1. Actual identities + triple/template/D2/BIN imports → double-edge classification and exact generated triples.
2. Exact generated triples → disjointness, count (1), and partial-matching incidences.
3. Actual identities alone → component equitability → quotient (4) and spectral count (5).
4. D0 local rows + generated triples + equitability → independent companion prisms and (3).
5. Equations (3),(5) + original triangle pairing → bookkeeping (6).
6. D1 complete rows + equitability → incidence bounds (7),(8).
7. D1 unit-row/light-mate conclusions + motif disjointness + triangle pairing → port count (9).
8. Actual identities alone → signed B=-3 eigenspace, integer A restriction, parity/trace (10),(11); D0 induced original edges then force another bipartite component.

The forward reference from section 2 to equitability in section 3 is acyclic: equitability uses neither D0 nor prism conclusions.

## Micro-claim ledger

All obligations are discharged. Locations refer to lines of the audited source.

| ID | Lines | Context → conclusion, with decisive side conditions |
|---|---:|---|
| G01 | 16–21 | Actual graph → regularity and exact matrix identities. Degree ≤7 reaches at most 57 vertices; degree eight yields B row sum three and commutation with J. |
| G02 | 23–27 | Declared triple/template/D2/BIN imports → every double edge lies in a D0 alternating four-cycle or has D1 structure. This is not inferred from quotient data. |
| G03 | 51–55 | B_uv=2 → uv nonedge, CN(u,v)=3 and both endpoints triangle-free; their common-neighbor set is independent in G. Adjacent repeat entries have weight at most one by the triangle budget. |
| G04 | 57–64 | Root u has independent first layer, one triple-parent point v and one double-parent point. D2 exclusion bounds the latter's intersection with the triple by one. Thus each S_e pair has exactly common neighbors u,v and exact B weight one. |
| G05 | 66–67 | Each S_e vertex has two exact nonadjacent unit repeats, so its remaining budget one permits neither a double entry nor an original triangle. Hence S is disjoint from D and from original triangle vertices. |
| G06 | 69–75 | Distinct double edges have four distinct endpoints. One shared generated vertex needs four unit neighbors; two shared vertices would have four common neighbors instead of two. Thus generated triples are disjoint. |
| G07 | 77–79 | Original triangles are vertex-disjoint and avoid D,S; therefore 2d+3d+3T≤62. |
| G08 | 81–87 | For e≠f, an endpoint of e cannot neighbor two S_f vertices because their common-neighbor set is exhausted; a vertex of S_f cannot neighbor both endpoints of e without entering disjoint S_e. Hence the 2×3 incidence is a partial matching. |
| G09 | 94–101 | D0 local theorem gives the closed weighted four-cycle and distinct c_i common to a,b. Since ab is a double nonedge, these three points are precisely S_ab. |
| G10 | 102–109 | The two disjoint generated triples and the matching B_i,ci=1 exhaust all six rows, giving a separate closed unit prism with the displayed block matrix. |
| G11 | 111–113 | In BOUT every c_i has sole root parent b outside {1,2,3}; thus the two independent triples also have no original cross edges. |
| G12 | 115–119 | In MATCH every c_i has at most one original neighbor in {1,2,3}. Equitability (G16) makes G[K] regular, so its internal degree is zero or one. Degree one would give a 3×3 cross permutation matrix P. |
| G13 | 119–125 | P has zero diagonal because each positive matched repeat joins triangle-free vertices. B-closure alone reduces the K,K commutator to [A[K],B[K]]=0; its upper-left block is P−P^T. A symmetric zero-diagonal permutation of odd order is impossible. Therefore internal degree is zero. |
| G14 | 127–136 | The four-vertex D0 induced graph is independent in MATCH and a matching in BOUT, by its local theorem. Companion prisms are independent and distinct, since their generated triples are disjoint. This gives (3). |
| G15 | 140–144 | Weighted Laplacian quadratic form and B row sum three show ker(B−3I) consists exactly of component-constant vectors. |
| G16 | 146–149 | AB=BA sends every component indicator into that full eigenspace; hence A1_Cj is constant on each C_i. This proves equitability and regularity of G[C_i] without individual-component A-invariance. |
| G17 | 151–156 | Restrict A²+A=7I+J+B to component indicators: B acts as 3I and J as 1 n^T. Thus (4) holds; detailed balance counts actual original edges between components. |
| G18 | 158–161 | D=diag(n_i) makes D^(1/2)RD^(−1/2) symmetric. Detailed balance gives n^TR=8n^T, so ker(n^T) is invariant and complementary to span(1); the quadratic there is x²+x−10. |
| G19 | 163–169 | The integer characteristic polynomial and irreducible x²+x−10 give equal conjugate multiplicities m. Eigenvalue eight occurs only on span(1). Thus k=2m+1 and trace R=8−m, proving (5). |
| G20 | 171–172 | Each component's total directed repeat weight 3n_i is twice an integer unordered weight, hence n_i is even. |
| G21 | 174–182 | D0 components, their companions and original-triangle prisms are mutually distinct. Their contributions to k+2trace R are respectively z+2b, z and 5T/2. Original paired triangles have no cross G edges. Removing them gives (6). |
| G22 | 186–193 | D1 unit rows place 1,2,3,4,b,c in one component K, with six distinct vertices. The heavy pair and unit mates a,r lie in H. The stated original neighbors of 0,w,1 are actual distinct vertices. |
| G23 | 195–200 | Equitability propagates the observed four H→K and three K→H neighbors to quotient lower bounds when H≠K. When H=K it yields diagonal degree at least four, as explicitly retained. |
| G24 | 202–208 | For the D1 incidence relation, each distinct target consumes ≥4 of row sum eight and each distinct source contributes ≥3 to the reverse row. Therefore both numbers of distinct other components are ≤2. This is not an edge-pairing or parity conclusion. D0 components separately have only their one closed companion. |
| G25 | 212–220 | D0 light mates lie in D. D1 light mates have complete unit rows, so avoid D, and the C4 lemma excludes membership in any generated unit triangle, so they avoid S. Thus no repeat joins D to S. |
| G26 | 215–221 | Triangle pairing separates triangle-free D from original triangle vertices. Hence each of the 2d1 D1 endpoints has its remaining unit repeat in W, the complement of the three disjoint sets. |
| G27 | 218–230 | D0 has d0=2z double edges; |W|=62−5d−3T. Summing B from D1 endpoints into W gives 2d1≤3|W|, allowing shared mates and proving (9). |
| G28 | 234–242 | The signless quadratic form forces f_x=−f_y along support edges. A connected bipartite component contributes one signed-indicator direction; an odd cycle forces zero on a nonbipartite component. |
| G29 | 243–244 | Weighted degree count gives 3|C+|=3|C−| on every bipartite component. Thus each signed indicator has zero total sum and J vanishes on their span. |
| G30 | 246–249 | Commutation preserves the full B=-3 eigenspace. Restricting the actual identity with J=0 and B=-3I gives A²+A=4I. |
| G31 | 251–254 | In signed-indicator coordinates, M_ij is the difference of two integer neighbor counts evaluated on C_i+. Invariance forces its negative value on C_i−. Thus M is integral even when A mixes components. |
| G32 | 254–257 | Irreducibility of x²+x−4 and the integer characteristic polynomial give equal multiplicities, ell even and trace M=−ell/2. The case ell=0 is vacuous and valid. |
| G33 | 259–266 | For x∈C, equitability gives s(x)+t(x)=r_CC. The diagonal signed coefficient gives s(x)−t(x)=M_CC on both sides. Thus s,t are constant and (11) follows. |
| G34 | 268–270 | The D0 B-bipartition is {0,b} versus {w,a}. MATCH has no internal original edges and contributes zero; BOUT edges 0b and wa lie within sides and contribute +1. |
| G35 | 271–274 | If a D0 exists then ell>0, so signed trace is negative while all D0 contributions are nonnegative. Some non-D0 bipartite component has t>s. Bipartiteness forbids unit B triangles; every generated or original G-triangle gives such a triangle, so none occurs there. |
| G36 | 5–12,276–284 | Conclusions match the local/global necessary restrictions actually proved. Components may contain both heavy edges and generated triangles; neither quotient nor signed component parity establishes double-edge parity or nonexistence. |

The audit uses only finite sums and finite-dimensional real/integer linear algebra. There are no analytic interchanges, probabilistic modes, asymptotics, hidden constant dependencies, or induction hypotheses.
