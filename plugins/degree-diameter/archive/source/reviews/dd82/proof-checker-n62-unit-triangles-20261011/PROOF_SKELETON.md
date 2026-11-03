# Proof-obligation ledger

Scope: `CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`, all 310 lines. Each statement below quantifies over every actual simple graph G on 62 vertices with maximum degree ≤8 and diameter ≤2 whose actual repeat matrix has connected positive support, with the established B≤2/root-template reductions available. Every reference to a unit triangle quantifies over all three-sets S with B_xy=1 on all three pairs. No existence of such a graph or of a particular nongenerated type is asserted.

## Typed symbols

| Symbol | Type and meaning |
| --- | --- |
| V,G,A | A 62-element vertex set, a simple undirected graph, and its symmetric 0–1 adjacency matrix. |
| B | Actual symmetric nonnegative integral 62×62 matrix A²+A−7I−J, zero diagonal, row sum 3, entries ≤2. |
| N(v) | Subset of V consisting of original G neighbors of v. |
| S={x,y,z} | Unit B triangle, independent in G after triangle-freeness. |
| t(S) | Integer size of N(x)∩N(y)∩N(z), in {0,1,2}. |
| d,D,𝒮 | Number of unordered heavy B edges, their 2d endpoints, and union of their d generated triples. |
| u,a,b,c | Type-one center and three distinct pair witnesses, all outside S. These are local symbols, not the identically named normalized D1 vertices. |
| a_i,b_i,c_i | Six distinct type-zero pair witnesses, outside S. |
| p_x,p_y,p_z | Unique residual unit-repeat neighbors outside S; repetitions allowed. |
| q=d_S | Integer column vector A1_S, with entries between 0 and 3. |
| n_i | Number of all vertices v∈V with q(v)=i; includes S in the zero stratum. |
| h | Nonnegative integral column vector recording external-port multiplicities; support outside S, total 3. |
| U,v_extra | Union of vertices of all unit B triangles, and cardinality of U\𝒮. |
| s,k | Nonnegative integer numbers of nongenerated single-triangle and diamond clusters under vertex overlap. |

No symbol changes mathematical type inside the target. In particular q is a vector in the target, while the number of diamond clusters is k.

## Dependency DAG

Actual graph → regularity and exact repeat identities.

Actual identities + S_TOUCH saturated-row argument → triangle pairing → closed six-point component at an original triangle.

Established B≤2 import + actual root parent counts → complete root-template coverage. Coverage + D2/BIN exclusions + D0 closed-component theorem + connected support → every double is D1. Triangle pairing + connected support → global triangle-freeness. Four-cycle count + pairing → odd d.

D1 hard rows → distinct external generated-triangle ports and persistent D1 reroot. D1 hard rows → C4 row → C3–C4 zero block → no-unit-triangle light mates at both endpoints.

Exact unit pair counts → intersection classification → type-one rows and type-zero witness sets. Distinct D1 ports + row budgets → generated-triangle separation → type-zero no-double restriction. Type-one row → exact center-neighborhood repeat graph → center injection.

Degree/pair counts → strata. Exact port rows + commutation → transport identity. Generated disjointness + no-unit-triangle light mates → strengthened packing. Maximum unit-support degree three + connectedness → triangle/diamond clusters → cluster form of packing.

No directed or semantic cycle was found. Automatic connectedness is not a node or an import.

## Obligations and hypothesis discharge

| ID | Target location | Sequent / rule and discharged hypotheses | Result |
| --- | --- | --- | --- |
| P01 | 16–27 | Actual G ⇒ regularity, B identities, AB=BA. Degree ≤7 would reach ≤57 vertices. Regularity makes AJ=JA; diameter gives off-diagonal nonnegativity. B≤2 is explicitly imported. | Discharged with stated import. |
| P02 | 29–32; 269–271 | Connected support + triangle pairing/D0 closure + template exclusions ⇒ triangle-free G and all doubles D1. A proper closed set of size 6 or 4 contradicts 62-vertex connectedness. Odd d follows from 2C4=93+d−3T with even T. | Discharged. |
| P03 | 33–41 | Each arbitrary heavy pair ⇒ one generated unit triple, generated triples pairwise disjoint and disjoint from D. Global quotient §1 supplies exact parent intersections after D2 exclusion. | Discharged. |
| P04 | 43–67 | Any unit S ⇒ S independent in G, each pair has two common neighbors, hence t∈{0,1,2}. Uses triangle-freeness and identity (1). | Discharged. |
| P05 | 69–81 | t=2 iff generated. Two centers are nonadjacent, have at least three common neighbors, and B≤2 gives exactly three; converse bounded by pair counts. | Discharged. |
| P06 | 83–94 | t=1 ⇒ exactly three distinct additional pair witnesses with the prescribed two-neighbor incidences. Collision would create a second center. | Discharged. |
| P07 | 96–108 | t=0 ⇒ six distinct pair witnesses. Collision between different pair sets would be a common center. | Discharged. |
| P08 | 112–126 | Generated S and any distinct unit T ⇒ S∩T=∅. Intersection size 1 violates row sum; size 2 violates three distinct D1 ports 4,b,c. | Discharged. |
| P09 | 128–131; 255 | Unit-triangle vertex cannot be heavy: two unit entries plus a double would require row weight at least 4. | Discharged. |
| P10 | 135–141 | Type one ⇒ {u,a,b,c} independent and B_u=e_a+e_b+e_c. Shared G neighbor rules out adjacency; three unit lower bounds exhaust the row. | Discharged. |
| P11 | 143–157 | Type-one ports, repeated or distinct ⇒ A_(u,p_x)=A_(u,p_y)=A_(u,p_z)=0. Uses the exact root row and AB=BA at (x,u), etc. | Discharged. |
| P12 | 159–175 | Type-one center u∉D∪𝒮. Exact pair intersections make every unit triangle through u type one; three-unit row excludes a heavy edge. | Discharged. |
| P13 | 177–185 | Type-one center ⇒ B[N(u)] is exactly S plus five isolated vertices. Positive repeat v,w gives second center r; B_ur>0 forces r∈{a,b,c}; their exact N(u)-neighbor pairs lie in S. | Discharged. |
| P14 | 187–189 | Two type-one triangles sharing their unique center must coincide by P13; center map is injective. No disjointness between center set and all triangles is asserted. | Discharged. |
| P15 | 193–195 | Type-zero witness six-set is G independent: any two two-subsets of S intersect, and hence any two witnesses share an S neighbor. | Discharged. |
| P16 | 195–198 | No double repeat among type-zero witnesses: its generated triple would contain a shared S neighbor, contradicting P08 and t(S)=0. | Discharged. |
| P17 | 200–213 | The three designated witness pairs have exact unit repeats and exactly their two prescribed common neighbors. Other witness unit entries remain possible. | Discharged. |
| P18 | 217–231 | For every t, (n0,n1,n2,n3)=(44−t,12+3t,6−3t,t). Counts use three degree-eight vertices, three common-neighbor pairs of size two, and all 62 vertices. | Discharged. |
| P19 | 233–238 | Complete unit-triangle rows and symmetry ⇒ B1_S=2·1_S+h, A1_S=q, h≥0, Σh=3, supp h outside S. Multiplicities are retained. | Discharged. |
| P20 | 240–247 | AB=BA applied to 1_S and P19 ⇒ (B−2I)q=Ah≥0. Finite matrix multiplication; no inversion or positivity of B−2I assumed. | Discharged. |
| P21 | 257–259 | Each D1 heavy endpoint's unique unit mate lies outside D and all U. Exact hard rows exclude D; C4 block zero and persistent D1 reroot exclude all unit triangles. | Discharged. |
| P22 | 251–266 | P03,P09,P21 ⇒ 2d≤3(62−2d−|U|), |U|=3d+v_extra ⇒ 17d+3v_extra≤186. Multiple heavy endpoints may share a mate; row capacity counts incidences. | Discharged. |
| P23 | 268–271 | P22 with v_extra≥0 plus odd nonnegative d ⇒ d∈{1,3,5,7,9}; d=9 ⇒ v_extra≤11. | Discharged. |
| P24 | 273–284 | Unit-support maximum degree ≤3 and connected B support on 62 vertices ⇒ each overlap cluster is a single triangle or diamond. A third triangle on a diamond forces a closed unit K4. | Discharged. |
| P25 | 286–293 | P08,P24 ⇒ nongenerated clusters are disjoint from all generated triangles and from one another; v_extra=3s+4k and packing gives 17d+9s+12k≤186. | Discharged. |

## Quantifiers and limits

P04–P20 hold for every eligible unit triangle individually. P14 quantifies over every pair of type-one triangles. P08 quantifies over every generated triangle and every distinct unit triangle, including all three possible t values. P21 quantifies over both endpoints of every heavy edge, not just the initially normalized root. P22–P25 quantify over the entire actual graph. No limiting operation, asymptotic estimate, probability mode, or uniformity parameter is present.

## Explicitly unresolved

The proof does not eliminate t=0 or t=1, does not prove every unit B triangle generated, does not establish any integer packing choice realizable, does not prove automatic connectedness, and does not construct or exclude the remaining order-62 graph. Triple-repeat exclusion remains an established imported reduction rather than a newly rerun enumeration in this audit.
