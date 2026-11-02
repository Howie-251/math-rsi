# Proof skeleton: D0 components and the D1 outlet

Date: 2026-10-11. Fresh reviewer: `/root/proof_review_n62_d0_outlet`.
Target: `proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`.
Review independence: same-family. Acceptance status: provisional. Requested
reviewer configuration was `gpt-6-astra` / `ultra`; the actual backend model
and reasoning setting were not attested by this invocation.

## Canonical statements

Let G be any finite simple undirected graph with exactly 62 vertices,
maximum degree at most eight, and diameter at most two. Let A be its actual
adjacency matrix and B=A²+A−7I−J its actual repeat matrix.

1. For every choice of root and labels realizing D0_MATCH, there exist four
   distinct vertices 0,w,b,a whose complete B rows are
   B₀=2e_w+e_a, B_w=2e₀+e_b, B_b=2e_a+e_w, B_a=e₀+2e_b.
   They constitute one connected component of the positive support of B,
   and the subgraph of G induced by these four vertices has no edge.
2. For every choice realizing D0_EDGE_BOUT, the same four complete rows
   hold, and the induced G edges are exactly 0b and wa.
3. Every such G has a choice of root and labels realizing D1_MATCH.
   This is a paper conclusion using the recovered triple-repeat exclusion,
   including its explicit exact finite enumeration. It is not an exclusion
   of D1_MATCH or of arbitrary order-62 graphs.

Here e_v is the coordinate row vector at vertex v. A row identity is an
identity on the whole vertex set, not just the displayed four vertices.

## Typed symbols

| Symbol | Type and meaning |
|---|---|
| V(G) | Finite vertex set of cardinality 62 |
| A | Symmetric 62×62 matrix over {0,1}, zero diagonal |
| B | Actual symmetric 62×62 nonnegative integer matrix, zero diagonal, row sum 3 |
| c(x,y) | Nonnegative integer, number of common G neighbors |
| t(x) | Nonnegative integer, number of triangles containing x; at most 1 |
| 0 | Chosen root vertex |
| X | N_G(0), an eight-element set; independent in the double-root cases |
| Y | V(G)\({0}∪X), of cardinality 53 |
| P(y) | N_G(y)∩X for y∈Y |
| S | {1,2,3}=P(w) |
| a | Unique point with P(a)={4,5} in D0, distinct from w |
| C_i | Ordinary singleton-parent vertices y with P(y)={i} |
| c_i | Unique remaining unit B endpoint of i∈S; subsequently shown ordinary and distinct |
| b | Unique remaining unit B endpoint of w; belongs to Y in MATCH, to X\(S∪P(a)) in BOUT |
| d | Number of unordered pairs {x,y} with B_xy=2 |
| T | Number of unordered actual G triangles |
| C₄ | Number of unoriented simple G cycles of length four, including cycles with chords |

The local symbol b denotes different kinds of vertex in the two branches;
this distinction is explicit and is never transferred between branches.
All counts are finite. No asymptotics, probabilities, limits, integral
interchanges, or hidden uniformity parameters occur.

## Dependency DAG

```text
Original G assumptions
  -> 8-regularity -> actual B identities -> triangle incidence budget
  -> root parent accounting

Actual B identities + D0 parent data
  -> rows at 0 and i∈S
  -> D0_MATCH closure
  -> D0_EDGE_BOUT closure

Actual B identities + S_TOUCH parent data -> local S_TOUCH contradiction
  -> triangle-mate avoidance -> distinct mates -> mate triangle
  -> fixed-point-free triangle pairing -> T even

Original G assumptions -> recovered triple-repeat structure
  -> exact finite L,Q,Gram enumeration + resolution contradiction
  -> B entries ≤2

B entries ≤2 + actual cycle count + T even -> d odd
Arbitrary double edge + root parent accounting -> D0/D1/D2 coverage
Actual D2 parent data -> D2 contradiction
Actual BIN parent data -> BIN contradiction
D0 closures + no D1 + D2/BIN contradictions -> d even
d odd + d even -> existence of a D1_MATCH root
```

There is no reverse dependency on the D1 outlet. The simple-B exclusion
follows from the same parity argument when d=0 and is redundant for this
outlet once d odd is derived. S_TOUCH is needed through triangle pairing;
its global simple-B premise is not used by its local row proof.

## Assumption and application ledger

| Application | Required hypotheses | Discharge |
|---|---|---|
| Actual matrix identities | Simple undirected G, 62 vertices, max degree ≤8, diameter ≤2 | Degree ≤7 reaches at most 57 vertices; hence degree=8. Row sum of B is 64+8−7−62=3; diagonal is 8−7−1=0; nonnegativity follows from diameter. Regularity implies AJ=JA and AB=BA. |
| Triangle budget | Actual B and zero loops | On adjacent pairs B_xy=c(x,y); summing gives 2t(x)≤3. Thus t(x)≤1 and adjacent repeat entries ≤1. |
| Complete D0 rows at i∈S | Independent X, unique exceptional parents 123 and 45 | The common neighbors of distinct X vertices are 0 and their shared exceptional parent(s), with no other possibilities. Thus exactly two unit entries into X occur for i∈S; B_i0=0. |
| MATCH row at w | Actual D0_MATCH parent data, w not adjacent to a | Five ordinary neighbors in Y avoid S; each of five remaining labels needs one common neighbor with w. Thus B_wx=0 on X and the additional endpoint lies in Y. |
| BOUT row at w | Actual D0_EDGE_BOUT parent data, b outside S∪P(a) | Recovered Step 6 derives B_w=2e₀+e_b from six parent incidences over five labels; BOUT chooses the outside orbit. |
| Triangle pairing | Actual G identities and local S_TOUCH contradiction | `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md:38–56` reconstructs the exact S_TOUCH parent structure for a mate touching its triangle. The S_TOUCH proof's three saturated rows are valid for integer B, without global simplicity. |
| Triple-repeat exclusion | Actual G identities, not an arbitrary repeat matrix | `RECOVERED_REDUCTION.md:60–195` derives every enumerated object from G. The finite source was inspected and its exact check rerun in this audit. |
| Cycle count | B_xy≤2, t(x)≤1, finite simple G | Supplied by the preceding two applications and original assumptions. Count unordered opposite pairs, so every four-cycle contributes twice. |
| Root-template coverage | A chosen actual pair with B_0w=2 | `RECOVERED_REDUCTION.md:205–219` is constructive for any chosen double edge and either endpoint; root and mate are triangle-free. This is stronger than merely some graph relabeling exists. |
| D2 exclusion | Parent sets 123,12; independent X; other points singleton; actual B | Exactly the intersection-size-two case of the preceding coverage; w and a cannot be adjacent because they share a parent and w is triangle-free. |
| BIN exclusion | Parent sets 123,45; w adjacent to a; residual endpoint b∈{4,5}; actual B | Exactly the inside orbit in the disjoint-adjacent case of coverage. |
| Even double-edge partition | Every double edge belongs to one of the D0 closed components | Applied only under the supposition of no D1 and after excluding D2 and BIN. Complete row identities forbid overlap of distinct components. |

## Micro-claim inventory

Each obligation below is discharged; the justifications also record the
required side conditions at the point of use.

| ID | Context ⊢ conclusion | Justification and source |
|---|---|---|
| MC-01 | Original G ⊢ G is 8-regular | Radius-two bound 1+7+7·7=57<62. Recovered reduction:44. |
| MC-02 | MC-01 + actual definition ⊢ B≥0, integral, symmetric, diagonal 0, row sum 3, AB=BA | Direct matrix and diameter calculations. Recovered:44–46. |
| MC-03 | MC-02 ⊢ 2t(x)=Σ_{y~x}B_xy≤3 and t(x)≤1 | Count triangle incidences twice; adjacent B equals common-neighbor count. Recovered:48–52. |
| MC-04 | B_0w=2 ⊢ 0,w are nonadjacent and triangle-free | MC-03 bounds an adjacent repeat by 1; remaining repeat budget is 1 and triangle incidence budget is even. |
| MC-05 | D0 parent sets ⊢ B₀=2e_w+e_a | Parent counts and row sum; target:20–23. |
| MC-06 | D0 parent sets + i∈S ⊢ B_i=e_j+e_k+e_{c_i}, c_i∈Y | Exact X common-neighbor counts and B_i0=0; target:27–31. |
| MC-07 | MATCH + MC-04 ⊢ five Y neighbors of w occupy C₄,…,C₈ once each | No parent in S is permitted by triangle-freeness; every outside label needs coverage; exactly five points. Target:37–40. |
| MC-08 | MC-07 ⊢ B_w=2e₀+e_b with b∈Y\{w} | B_wx=0 on X, exact B_w0=2, zero diagonal. Target:40–43. |
| MC-09 | MATCH + b=a ⊢ contradiction | (AB)_ia≥B₀a+B_wa=2 but (BA)_ia=A_{c_i a}≤1. Target:45–47. |
| MC-10 | MATCH + b≠a ⊢ A_{c_i a}=1 and c_i≠a,w | (AB)_ia≥B₀a=1, (BA)_ia=A_{c_i a}; B_wi=0 rules out w. Target:49–54. |
| MC-11 | MATCH + MC-08 ⊢ A_{c_i b}=1 and Σ_{h∈S}B_{c_i h}≤1 | At (c_i,w), AB=A_{c_i b}, whereas BA≥Σ_{h∈S}B_{c_i h}≥1. Target:54–61. |
| MC-12 | MC-11 ⊢ c₁,c₂,c₃ distinct and none equals b | A repeated endpoint contributes two distinct units to that sum; c_i=b would force a loop. Target:61–62. |
| MC-13 | MC-10–12 ⊢ c(a,b)≥3 | Three distinct common neighbors c_i of distinct a,b. Target:64. |
| MC-14 | MC-13 + B_a0=1 ⊢ A_ab=0, B_ab=2, B_a=e₀+2e_b | B_ab=c(a,b)+A_ab−1≥2+A_ab; total row budget 3. Target:66–69. |
| MC-15 | MC-08 + MC-14 + symmetry ⊢ B_b=2e_a+e_w | Two known entries sum to 3. Four points are distinct by endpoint locations and MC-09. Target:69–73. |
| MC-16 | MC-08,14,15 ⊢ a closed connected four-point B component | All rows exhausted and the displayed weighted cycle is connected. Target:71–73. |
| MC-17 | MATCH + MC-04,14 ⊢ induced G is empty on these four vertices | 0 avoids Y; w avoids a by branch; w avoids b by triangle-freeness and B_wb=1; a avoids b by MC-14. Target:75–78. |
| MC-18 | BOUT + MC-06 ⊢ A_{c_i w}=0 | At (i,w), AB=2A_i0+A_ib=2, BA=2+A_{c_i w}; i,b distinct in independent X. Target:82–86. |
| MC-19 | BOUT + MC-18 ⊢ A_{a c_i}=1, c_i≠a,w | At (0,c_i), AB≥B_{i c_i}=1, BA=A_{a c_i}; B_wi=0 excludes w. Target:87–88. |
| MC-20 | BOUT + c_i∈Y ⊢ A_{b c_i}=1 and P(c_i)={b} | At (c_i,w), AB=A_{c_i b} and BA≥B_{c_i i}A_iw=1. MC-19 makes c_i ordinary. Target:89–90. |
| MC-21 | BOUT + MC-18–19 ⊢ Σ_{x∈X}B_{x c_i}=1 and c_i distinct | At (0,c_i), BA=A_{a c_i}=1; repeated c_i would give two units in AB. Target:92–93. |
| MC-22 | BOUT + MC-20–21 ⊢ B_ab=2, B_a=e₀+2e_b, B_b=2e_a+e_w | b outside P(a) ensures A_ab=0; c_i give three common neighbors; rows saturate. Target:93–95. |
| MC-23 | BOUT + MC-22 ⊢ component closed and induced G edges exactly 0b,wa | b∈X\(S∪P(a)), w,a∈Y; all six pairs determined. Target:95–99. |
| MC-24 | Actual G ⊢ B entries ≤2 | Recovered triple-repeat proof, exact finite enumeration, and resolution contradiction; independently inspected and rerun. Target:103. |
| MC-25 | MC-24 + MC-02 ⊢ number of unit edges=93−2d | Total unordered weight is 62·3/2=93 and every positive weight is 1 or 2. Target:104–106. |
| MC-26 | MC-03,24,25 ⊢ 2C₄=93+d−3T | Adjacent repeats are exactly the 3T triangle edges; nonadjacent unit and double repeats contribute choose(2,2)=1 and choose(3,2)=3. Target:106–109. |
| MC-27 | Actual G ⊢ T is even | Triangle pairing theorem; all its local hypotheses discharged above. Includes T=0. Target:111. |
| MC-28 | MC-26–27 ⊢ d odd and d>0 | Reduce 93+d−3T modulo 2. Target:111–113. |
| MC-29 | Any chosen double edge ⊢ some D0, D1, or D2 root template for that edge | Root parent excess is 3; exceptional sizes 3,2; intersections have sizes 0,1,2. If adjacent, size is 0 and the residual endpoint has the BIN/BOUT alternatives. Target:115–119; recovered:205–219. |
| MC-30 | MC-29 + D2/BIN exclusions + no D1 root ⊢ chosen edge lies in MATCH or BOUT | Exclusions apply to the exact actual parent data produced by MC-29. Target:120–121. |
| MC-31 | MC-16,23,30 ⊢ all double edges partition into groups of two | Every such component has exactly two double edges; closed connected components sharing a vertex coincide. Target:123–126. |
| MC-32 | MC-28,31 ⊢ existence of a D1_MATCH root | No-D1 supposition makes d both odd and even. Target:127–129. |

## Source set and dependency boundaries

The complete target and these source proofs were read directly, without
using prior audit verdicts as premises:

- `proofs/dd82/n62/RECOVERED_REDUCTION.md` (the original-G derivation and template coverage, through Step 6).
- `proofs/dd82/n62/S_TOUCH_SATURATED_ROW_EXCLUSION.md`.
- `proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`.
- `proofs/dd82/n62/D2_MATCH_SATURATED_ROW_EXCLUSION.md`.
- `proofs/dd82/n62/D0_EDGE_BIN_SATURATED_ROW_EXCLUSION.md`.
- `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_triple_edge_elimination.py`.

The S_TOUCH three-case reduction was also read for context, but its search
records and canonical solver cases play no role. No solver evidence,
known order-63–65 exclusion, arbitrary assigned cubic matrix, or unproved
D1 contradiction enters the DAG.
