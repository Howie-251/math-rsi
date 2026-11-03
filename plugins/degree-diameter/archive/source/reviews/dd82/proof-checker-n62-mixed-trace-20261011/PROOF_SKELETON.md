# Mixed-trace proof obligations

Date: 2026-10-11. Fresh reviewer: `/root/proof_review_n62_mixed_trace`.
Scope: the complete `proofs/dd82/n62/CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md`, with original local proof dependencies. Same-family review; acceptance remains provisional.

## Quantified statement and assumptions

For every finite simple undirected graph G on 62 vertices satisfying maximum degree at most eight, diameter at most two, and connected positive support of its actual repeat matrix B, use the stated upstream reductions B≤2, triangle-freeness, and the D1 description of every double pair. The assertions reviewed are necessary identities, bounds, and local patterns for such G. No existence or exclusion assertion is included.

Eight-regularity follows directly: a vertex of degree at most seven reaches at most 1+7+7·7=57 vertices. Thus A1=8·1 and B=A²+A−7I−J has row sum three, zero diagonal, symmetric nonnegative integral entries, and AB=BA. The bound B≤2 and the template classification are upstream reduction inputs, not newly certified here. Connectedness is an explicit hypothesis, so the computational proof that connectedness is automatic is not needed for this audit.

Triangle pairing makes an original triangle part of a closed six-point repeat component; the D0 component theorem makes a D0 double part of a closed four-point component. Their application here uses connected support on all 62 vertices. D1 hard-branch rows, their rerooting at either heavy endpoint, and the C4 refinement are applied only to these actual D1 roots.

## Symbols

| Symbol | Type and meaning |
|---|---|
| A, B, I, J | Real 62×62 matrices; A adjacency, B actual repeat matrix, I identity, J all ones |
| d, c4, c5 | Nonnegative integers counting unordered double pairs and unoriented simple cycles |
| D, S, W | Vertex sets: heavy endpoints, generated triangles, and complement of their union |
| m_B(w) | Nonnegative integer weighted original-edge count inside the B-neighborhood |
| m(w), ell(w) | For w in W: original edges among its three unit mates, and number of heavy mates |
| L3 | Number of w in W with ell(w)=3 |
| P_z | Two-element subset N_G(w)∩N_G(z), for each unit mate z of w |
| F_w | Simple three-edge graph on N_G(w), edges the three distinct P_z |
| tau | Integer tr(AB²), equal to twice the sum of local weighted counts |

All sums are finite. There are no limiting, probabilistic, asymptotic, or uniformity claims.

## Dependency DAG

Actual identities + connectedness + upstream reductions → triangle-free/D1 setting.
D1 rows + C4 light-mate theorem → disjoint D,S; every heavy light mate in W; heavy mates isolated locally.
These facts + row sum three → d odd, 17d≤186, c4=(93+d)/2.
Actual polynomial + four/five-cycle counts → mixed trace identity.
Trace expansion by entries + D1 rows → local contribution formula on W.
Local formula + heavy incidence/isolation → port bound and numerical ranges.
Local positivity + parent sets + generated-triangle exclusion → five parent patterns.
Two-edge second pattern + heavy isolation → type-one nongenerated unit triangle.

There is no dependency on tau=0, on all unit triangles being generated, or on the new note itself through its imports.

## Obligation ledger

| ID | Obligation and discharged hypotheses | Verification |
|---|---|---|
| M01 | Generated triangles are disjoint from D and each other | D1 generated rows supply three unit pairs; two shared vertices would have four heavy common neighbors, while one shared vertex would require four positive row entries. Original source: GLOBAL_DOUBLE_TRIANGLE_QUOTIENT §1. |
| M02 | d∈{1,3,5,7,9}, c4=(93+d)/2 | With triangle-freeness and B≤2, opposite-pair counting gives 2c4=(93−2d)+3d=93+d, so d is odd and positive. The 2d heavy-unit incidences enter W of size 62−5d, giving 2d≤3(62−5d) and d≤10. |
| M03 | Polynomial and J terms | Q=A²+A−7I has row sum 65; QJ=JQ=65J, AJ=8J, J²=62J. Hence J correction is −33728; AQ²=A⁵+2A⁴−13A³−14A²+49A. |
| M04 | Closed-walk counts | Simplicity and regularity give tr(A)=0, tr(A²)=496; triangle-freeness gives tr(A³)=0. Length-four counting yields 7440+8c4=7812+4d. A non-simple closed five-walk would contain a closed odd walk of length one or three, impossible; tr(A⁵)=10c5. |
| M05 | Exact mixed trace | Substitution gives 10c5+8d+15624−6944−33728=10c5+8d−25048. |
| M06 | Weighted local interpretation | tr(AB²)=sum_{w,u,v} A_uv B_wu B_wv. Diagonal A terms vanish; symmetry counts each unordered pair twice. This retains weights at heavy rows. |
| M07 | D and S contributions vanish | At a heavy endpoint the heavy mate and light mate are original nonneighbors. Generated rows {2,3,4}, {1,3,b}, {1,2,c} are independent: b∈C4∪…∪C8 and c∈C5∪…∪C8. Apply the normalized D1 description separately to each double. |
| M08 | Port incidence and isolation | Every heavy endpoint has exactly one unit mate; hard-branch rows make it nonheavy and C4 refinement puts it on no unit triangle, hence outside S. Each incidence is counted once, even if different heavy endpoints share a light mate. At light mate a, B_a=e_0+e_p+e_q and p,q are outside N_G(0). |
| M09 | Local and global inequality | Triangle-free graphs on three vertices with ell isolated vertices have at most 2,1,0,0 edges for ell=0,1,2,3. Sum to obtain 2[2(62−5d)−2d+L3]=248−24d+2L3. Also 3L3≤2d. Nonnegativity follows from M06. |
| M10 | Table and zero-trace conditional | Exact integer arithmetic verifies all five rows. At tau=0, 8d≡25048 mod 10 gives d≡1 mod 5; only d=1 remains, with c5=2504. |
| M11 | Parent pairs distinct | A unit repeat in a triangle-free graph is a nonedge with exactly two common neighbors. If P_a=P_b, their two parents have exactly the three common neighbors w,a,b by B≤2, generating a triangle containing w, contradicting w∈W. |
| M12 | Five positive parent patterns | An original edge requires disjoint parent pairs. Start with two disjoint edges of F_w: the third uses two new vertices, one new vertex, or joins the old edges, producing 3K2, P3+K2, or P4. The permitted mate-edge graphs are respectively subgraphs of K3, P3, and K2; positive triangle-free choices yield 2+2+1 cases. |
| M13 | Heavy restrictions on patterns | Heavy mates are isolated by M08; a two-edge path therefore has no heavy mate, and a single edge has at most one, at its isolated vertex. |
| M14 | Type-one conclusion | In the second pattern with a~b~c, a,c are nonheavy by M13 and nonadjacent by triangle-freeness. h and b are distinct common neighbors since h~w but b is a repeat mate and not adjacent to w. Hence 1≤B_ac≤1. The unit triangle {w,a,c} has common-neighbor set P_a∩P_c={h}; generated triangles have two common neighbors, so this one is nongenerated. |
| M15 | Remaining light-mate obstruction | C4 refinement gives B_pq=0, p∈C3, q∈C4, and a five-edge original matching avoiding u3,W4. The exclusions p≠u3 and q≠W4 make pairing p with q possible at the level of those matching statements; they do not prove it occurs in an actual graph. |

All obligations above are discharged at the stated conditional scope. Upstream triple-repeat/template reductions and their full certification remain imports; no new automatic-connectedness or order-62 exclusion theorem is certified.
