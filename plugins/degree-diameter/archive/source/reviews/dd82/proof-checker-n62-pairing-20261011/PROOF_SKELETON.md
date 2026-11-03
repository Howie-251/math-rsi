# Proof skeleton and obligation ledger

All line references below refer to the reviewed versions read on 2026-10-11.
`P` denotes `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`, `S` denotes
`S_TOUCH_SATURATED_ROW_EXCLUSION.md`, and `R` denotes
`RECOVERED_REDUCTION.md`, all in `proofs/dd82/n62/`.

## Typed symbols and hypotheses

- G: finite simple undirected graph with vertex set V, |V|=62, maximum degree
  at most 8, and diameter at most 2.
- A: V×V symmetric 0/1 adjacency matrix, diagonal zero.
- I,J: identity and all-ones V×V matrices.
- B=A²+A−7I−J: exact repeat matrix of G, not an independent relaxation.
- c(x,y): nonnegative integer common-neighbor count, for distinct vertices.
- t(x): number of actual triangles through x; T: total number of actual
  triangles. T0 is instead a three-vertex triangle set.
- f(v): the unique extra unit B neighbor of a triangle vertex v, outside its
  two triangle partners. The definition is intrinsic because t(v)=1.
- F: the set {f(v):v∈T0}; C=N(T0)\T0, using union of open neighborhoods.
- 1_D: actual 0/1 column vector of a vertex subset D⊆V.
- X=N(0), Y=V\({0}∪X), P(y)=N(y)∩X: local root-parent notation.
- C_i={y∈Y\{w}:P(y)={i}}: S_TOUCH singleton-parent classes. These are
  distinct notation from the triangle's neighborhood set C.
- C4: nonnegative integer number of non-oriented, not necessarily induced
  four-cycles, with the usual cycle equivalence.

No symbol changes type. The letter b denotes a triangle partner in P and the
extra repeat neighbor of 2 in S; these are separate local arguments, and the
relabeling makes their use unambiguous.

## Canonical quantified statements

Q1. For every G satisfying the original assumptions, the map from each actual
triangle T0 to {f(v):v∈T0} is a well-defined fixed-point-free involution on the
finite set of actual triangles of G. Consequently T is even.

Q2. For every G satisfying those assumptions, if its exact B has only 0/1
entries, a contradiction follows. Equivalently, no such graph with simple B
exists.

Q3. Local dependency strengthening: for every such actual G, no root has the
S_TOUCH parent structure (only edge 12 in X, one outside vertex with parents
{1,3}, all other outside vertices with singleton parent sets). This statement
does not assume globally simple B.

## Minimal assumption ledger

| Result | Hypotheses actually used | Where discharged |
|---|---|---|
| Regularity and exact B properties | Original graph assumptions | R44–46; re-derived below |
| t(x)≤1 and unit triangle edges | Exact pair equation; nonnegative row sum 3 | R48–52, P23–29 |
| Q3 local S_TOUCH exclusion | Exact graph identities, row sum 3, integrality, prescribed actual root parent structure | S27–75; all steps rechecked in audit |
| Mate avoidance | Any actual triangle and Q3 | P26–56 constructs all Q3 hypotheses |
| Mate distinctness | Mate avoidance, complete root repeat rows, AB=BA | P62–69 |
| Indicator identities | Actual A,B; unique unit mates; distinct mates; t≤1 | P71–85 |
| Mate triangle | Identities, AB=BA, B≥0, G simple, |F|=3 | P85–101 |
| Q1 involution | Mate triangle, unit triangle weights, row sum 3, disjointness | P105–112 |
| Q2 simple-B exclusion | Q1 plus simple B and elementary four-cycle count | P116–128 |

## Micro-claim inventory

Every row below is a discharged sequent: the context implies the stated goal
by the rule and hypothesis verification shown.

| ID | Context ⊢ goal | Rule and discharge | Location |
|---|---|---|---|
| MC01 | Original G ⊢ every degree is 8 | A root of degree ≤7 reaches at most 1+7+7·7=57 vertices; 62 are required. | P17–18; R44 |
| MC02 | MC01 and actual A ⊢ B is symmetric, integral, zero diagonal, nonnegative, row sum 3 | Diagonal: 8−7−1=0; off diagonal: c+A−1≥0 by diameter; row sum: 64+8−7−62=3. | P18–21; R44–46 |
| MC03 | MC01 and B definition ⊢ AB=BA | A commutes with its polynomials and AJ=JA=8J. | P19; R46 |
| MC04 | MC02 ⊢ 2t(x)=Σ_{y∼x}Bxy≤3, so t(x)≤1 | On an edge Bxy=c(x,y); each triangle through x is counted twice; t is integral. | P23–24; R48–52 |
| MC05 | MC04 and triangle T0 ⊢ two partner entries equal 1 and exactly one extra mate of unit weight | Each triangle edge has exactly one common neighbor; residual nonnegative integral row mass is 1. | P26–28 |
| MC06 | MC04–05 ⊢ v is nonadjacent to f(v) | Two partner edges already account for the whole incident repeat sum 2. | P29–30 |
| MC07 | Local S_TOUCH parents, MC02–04 ⊢ rows 0 and 1 are exactly {1,2,w} and {0,2,3}, unit weight | Parent counts give B0w=B13=1; triangle gives remaining specified entries; row mass saturates. | S27–32 |
| MC08 | Same local context ⊢ row 2 has exactly one extra unit neighbor b∈Y and A2b=0 | X\{1,2} pairs have precisely common neighbor 0; residual integer mass 1 and incident sum 2. | S34–42 |
| MC09 | MC07–08 and MC03 ⊢ b≠w | If equal, AB1w≥2 but BA1w=1. | S46–52 |
| MC10 | MC07–09 and MC03 ⊢ b∈C3 | b is a singleton-parent vertex, AB1b≥1, BA1b=A3b. | S54–59 |
| MC11 | MC07–10 and MC03 ⊢ Awb=1 | AB0b≥1, BA0b=Awb. | S63–68 |
| MC12 | MC11 ⊢ local contradiction Q3 | Triangle w3b gives B3b≥1; AB0b≥2 but BA0b=1. | S70–75 |
| MC13 | MC05–06 and f(r)∼a ⊢ local S_TOUCH hypotheses | P(w)={a,c}; c≠b avoids second triangle; only edge ab in N(r); all other root repeat entries zero give singleton parents. | P39–48 |
| MC14 | MC12–13 for each triangle vertex ⊢ F∩(T0∪N(T0))=∅ | Q3 contradiction, applied to arbitrary relabelings; mates are already outside T0. | P50–58 |
| MC15 | MC03, MC05, MC14 ⊢ three distinct mates | Two equal mates give A_ra B_aw=1 in AB_rw, while BA_rw=0. | P62–69 |
| MC16 | MC05, MC15 and B symmetry ⊢ B1_T0=2·1_T0+1_F | Complete rows of T0 determine all columns into T0; distinctness gives coefficient 1 on F. | P71–75 |
| MC17 | MC04 and triangle T0 ⊢ A1_T0=2·1_T0+1_C | Each outside vertex has at most one triangle neighbor, or it makes a second triangle. | P79–83 |
| MC18 | MC03, MC16–17 ⊢ B1_C=2·1_C−2·1_F+A1_F | Apply A and B respectively; equate AB1_T0 and BA1_T0; subtract equal terms. | P85–93 |
| MC19 | MC02, MC14–15, MC18 ⊢ F is a triangle | At v∈F: 0≤(B1_C)v=−2+deg_F(v)≤0, so deg_F(v)=2. | P95–101 |
| MC20 | MC04–05, MC19 ⊢ the mate map on triangles is involutive | At f(v), its two triangle edges and unit edge to v exhaust row sum 3. | P105–108 |
| MC21 | MC14, MC20 and finiteness ⊢ T even | The intrinsic triangle map has no fixed point and all orbits size 2; empty set allowed. | P110–112 |
| MC22 | MC02 plus simple B ⊢ 93 unordered repeat edges | Symmetry, zero diagonal and 62·3/2=93. | P116–117 |
| MC23 | MC04, MC22 ⊢ 2C4=93−3T | Exactly 3T repeat edges are original; pair equation and binomial common-neighbor count account for all unordered pairs. | P117–125 |
| MC24 | MC21, MC23 ⊢ Q2 contradiction | 93−3T even gives T odd, against T even. | P127–128 |

The dependency ordering in this inventory is acyclic. MC07–12 use no simple-B
premise, and MC01–21 use no triple-repeat elimination or template enumeration.
The only extra hypothesis in MC22–24 is simple B, explicitly stated at its
application.

No limits, integrals, derivatives, probabilistic modes, or asymptotic notation
occur; no limit-order or uniformity conditions arise.
