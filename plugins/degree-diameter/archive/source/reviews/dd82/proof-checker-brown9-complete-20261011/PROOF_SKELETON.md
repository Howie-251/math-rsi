# Proof skeleton and obligation ledger

Canonical statement: for every finite simple undirected graph $G$ on $V(B)\cup\{x\}$, where $B$ is the supplied 57-label graph, maximum degree at most 8 and diameter at most 2 imply $r=|E(B)\setminus E(G)|\ge10$, and $|E(G[V(B)])\setminus E(B)|=r$.

All 28 obligations below are discharged by the actual mathematics and finite computations. Status is ordinary computer-assisted proof review, same-family/provisional; there is no formal-verification claim.

## Typed symbols and domains

| Symbol | Type and meaning |
|---|---|
| $B$ | Fixed simple graph on integer labels $0,\ldots,56$, from `brown57.edges` |
| $G$ | Universally quantified simple graph on those labels plus a new $x$, with the degree/diameter hypotheses |
| $C,I,E$ | Pairwise disjoint old vertex sets of sizes $8,21,28$; $E(B),E(G)$ instead denote edge sets |
| $R_{\rm del},r$ | Old-edge deletion set $E(B)\setminus E(G)$, and its nonnegative integer size |
| $a,b$ | Numbers of distinct old III and IEE triangles destroyed by deletions |
| $d_v,d_v^0$ | Nonnegative integer old deletion degree and base-II-deletion degree at old vertex $v$ |
| $k_v$ | Exact integer old deficit to degree eight before new edges: $d_v+1_C(v)$ |
| $S$ | The eight distinct old neighbors of $x$; every $s\in S$ has $k_s>0$ |
| $j,e$ | Integers $\vert S\cap I\vert ,\vert S\cap E\vert $, with $j+e\le8$ |
| $\sigma$ | Nonnegative integer $\sum_{s\in S}(k_s-1)$, exactly the new old–old incidence count available at $S$ |
| $R_{\rm rep}$ | In triangle-family subproofs, the set of repeated internal vertices; distinct from $R_{\rm del}$ |
| $K$ | Set of already fixed deleted edges in a finite-search case |
| $u_K(S)$ | Integer $57-\vert S\cup N_{B-K}(S)\vert $ |
| $h(S)$ | Number of unaffected singleton-selected triangles for which both possible partners have a unique $S$-neighbor |
| $M$ | Global spare-weight upper bound of the search case: zero in a6, at most two in a7/19, at most three in a7/21 |
| $\varepsilon_C,\varepsilon$ | Zero/one indicators that the special CE absolute endpoint or IE internal endpoint is selected |
| $Z$ | Six-point union of the two isolated selected III triangles in an a8/EE 20-cover family |

The overloaded $R$ in different source documents is local and explicitly scoped; it causes no substitution or type error. There are no analytic limit orders, asymptotic constants, random variables, or measurable-space assumptions.

## Usage-minimal assumptions and application checks

1. The universal root bounds use only 58 vertices, simplicity, maximum degree eight, and diameter at most two.
2. Every Brown-specific step uses the fixed edge list and the directly checked finite premises B01–B03. No arbitrary order-58 graph is assumed to share Brown's local structure.
3. The deficit argument uses the regularity consequence G01, the original degree-seven/eight partition, and exact retained old edges. It makes no matching assumption about repair edges.
4. The matching deduction applies in a6 and in partition base deletions. It is rederived there; it is not imported into repeated-endpoint cases.
5. The a7 reductions cover exactly the relevant unions, verified by complete finite enumeration. Their relaxations contain every genuine extension neighborhood.
6. The search proof uses a fixed successful-set witness, exact known weights, disjoint unknown blocks, and an upper bound on global spare weight. The leaf correction $h(S)$ additionally requires that known deletions avoid unaffected triangles; the extras-first construction and independent enumeration verify that condition.
7. The a8/EE $Z$-argument uses six explicit finite incidence facts for all 42 applicable families and both EE choices; each was independently checked.
8. The final theorem uses the earlier $r\le8$ exclusion and every branch of P01, with no cycle and no prior-review verdict as an assumption.

## Micro-claim sequents and dependency DAG

In each row, the listed dependencies form the context; the statement is the goal, and the justification supplies the inference rule and its checked side conditions. All rows have status **discharged**.

### B01: Concrete input is the 57-vertex simple Brown graph

Context: the supplied explicit graph data. Goal: Concrete input is the 57-vertex simple Brown graph.

Rule and side conditions: Independently checked 224 distinct ordered pairs u<v, labels 0..56, and equality with the displayed F7 orthogonality rule.

Evidence: `RAW_FINITE_CHECK.json`.

### B02: C,I,E degrees and neighbor counts

Context: B01. Goal: C,I,E degrees and neighbor counts.

Rule and side conditions: Independent reconstruction gives sizes 8,21,28; C degree 7 with neighbors only E; other degrees 8; E has two C and three I neighbors; I has four I neighbors.

Evidence: `RAW_FINITE_CHECK.json`.

### B03: Triangle and edge-type premises

Context: B01, B02. Goal: Triangle and edge-type premises.

Rule and side conditions: 14 III, 42 IEE, exactly two of each at every I; II/CE/IE/EE counts 42/56/84/42; each non-CE edge in one triangle and every CE edge in none.

Evidence: `RAW_FINITE_CHECK.json`.

### G01: Order-58 regularity and edge balance

Context: B01. Goal: Order-58 regularity and edge balance.

Rule and side conditions: 1+7+7*7=57 forces every candidate degree to be 8; candidate has 232 edges, x has 8, so 224 old-old edges and equal old deletion/addition counts.

Evidence: `BROWN_EXTENSION_OBSTRUCTION.md:29`.

### G02: Every internal vertex loses an old triangle

Context: G01, B03. Goal: Every internal vertex loses an old triangle.

Rule and side conditions: 58 <= 65-2*t(v) gives t(v)<=3, while every old I vertex starts in four. Added edges cannot remove surviving triangles.

Evidence: `BROWN_EXTENSION_OBSTRUCTION.md:31`.

### G03: Exact deficits and necessary coverage budget

Context: G01, B02. Goal: Exact deficits and necessary coverage budget.

Rule and side conditions: k=d+1_C; S has size 8 and k>0; sigma=sum_S(k-1). Every old vertex outside the retained closed neighborhood needs a new incidence from S. Unreached C and I targets consume distinct such incidences.

Evidence: `BROWN_NINE_DELETE_OBSTRUCTION.md:30`.

### L01: Exclusion of r<=7

Context: B02, B03, G01, G02, G03. Goal: Exclusion of r<=7.

Rule and side conditions: 21<=3r; equality makes seven III triangles a partition and deletions a matching. No added edge touches S; C forces S=C, which fails to reach I.

Evidence: `BROWN_EXTENSION_OBSTRUCTION.md:33`.

### L02: r=8, a=8

Context: B02, B03, G02, G03. Goal: r=8, a=8.

Rule and side conditions: At most three double endpoints; C demand forces all selected I endpoints double, j<=3 and no spare for I, giving <=9 reachable I.

Evidence: `BROWN_EIGHT_DELETE_OBSTRUCTION.md:66`.

### L03: r=8, a=7, II extra

Context: B02, B03, G02, G03. Goal: r=8, a=7, II extra.

Rule and side conditions: Seven triangles partition I; distinct extra edge of an already selected triangle gives one double endpoint, j<=1 and I coverage <=3.

Evidence: `BROWN_EIGHT_DELETE_OBSTRUCTION.md:80`.

### L04: r=8, a=7, CE extra

Context: B02, B03, G02, G03. Goal: r=8, a=7, CE extra.

Rule and side conditions: Seven triangles partition I; sigma<=1, e<=1, retained C coverage <=e, j<=1; I upper bound <=7.

Evidence: `BROWN_EIGHT_DELETE_OBSTRUCTION.md:92`.

### L05: r=8, a=7, IE extra

Context: B02, B03, G02, G03. Goal: r=8, a=7, IE extra.

Rule and side conditions: Union at least20 implies at most one repeated vertex; sigma<=2, e<=1, j<=3; I upper bounds 13 or 2.

Evidence: `BROWN_EIGHT_DELETE_OBSTRUCTION.md:106`.

### L06: r=8, a=7, EE extra

Context: B02, B03, G02, G03. Goal: r=8, a=7, EE extra.

Rule and side conditions: Union at least20 gives sigma<=1, e<=2, j<=3; I upper bounds17 or10. Together L02-L06 cover all r=8 cases.

Evidence: `BROWN_EIGHT_DELETE_OBSTRUCTION.md:134`.

### P01: Exhaustive r=9 split

Context: B03, G02. Goal: Exhaustive r=9 split.

Rule and side conditions: a+b<=9 and 3a+b>=21 imply 6<=a<=9. At a=8 choose eight base III edges and one extra of one of four actual edge types; a=9 is all II.

Evidence: `BROWN_NINE_DELETE_OBSTRUCTION.md:11`.

### P02: a=6 block reduction

Context: B02, B03, G02, G03. Goal: a=6 block reduction.

Rule and side conditions: Equality forces six disjoint III blocks and three IEE blocks at missing vertices. The missing triple is an III triangle in each of14 families; external neighbor sets are disjoint, so deletions form a matching and S must dominate the original graph.

Evidence: `BROWN_R9_SIX_III_OBSTRUCTION.md:11; RAW_FINITE_CHECK.json`.

### P03: All relevant seven-III family sizes

Context: B01, B03. Goal: All relevant seven-III family sizes.

Rule and side conditions: Independent enumeration:42 cover19, zero cover20, two cover21; no other family covers at least19.

Evidence: `RAW_FINITE_CHECK.json`.

### P04: a=7, cover19, complete known-deletion reduction

Context: P02, P03, G03. Goal: a=7, cover19, complete known-deletion reduction.

Rule and side conditions: Each family has a unique central triangle on both repeated vertices; six remaining triangles disjoint. Extras occupy two disjoint five-point blocks at the missing vertices. Three central choices yield9+3+3=15 fixed cases; only fixed repeated endpoints carry spare weight.

Evidence: `BROWN_R9_SEVEN_III_OBSTRUCTION.md:37; RAW_FINITE_CHECK.json`.

### P05: a=7, cover21, complete extras-first enumeration

Context: P03, B03, G03. Goal: a=7, cover21, complete extras-first enumeration.

Rule and side conditions: Two partitions; extras pool203=21+56+84+42. Every actual deletion set has a representation. Fix at most two affected base triangles excluding extra edges. Independent enumeration gives145040 cases and verifies known/unknown disjointness and total spare<=3.

Evidence: `BROWN_R9_SEVEN_III_OBSTRUCTION.md:73; RAW_FINITE_CHECK.json`.

### P06: Exact residual h(S) correction

Context: P05. Goal: Exact residual h(S) correction.

Rule and side conditions: For every unaffected triangle, selecting0 or2 causes no extra uncovered vertex under the appropriate deletion; selecting1 permits two partners and forces one loss iff both have only that S-neighbor. Distinct blocks cause independent new losses, disjoint from initial uncovered vertices.

Evidence: `BROWN_R9_SEVEN_III_OBSTRUCTION.md:89`.

### C01: Candidate and block coverage of the C++ searches

Context: P02, P04, P05. Goal: Candidate and block coverage of the C++ searches.

Rule and side conditions: C and all possible positive-deficit vertices are included; known weights exact, unknown blocks weight0. At most two per block; five-point blocks additionally enforce original adjacency. Each genuine S obeys all restrictions.

Evidence: `brown_r9_a6_domination.cpp:4; brown_r9_a7_cover19.cpp:8; brown_r9_a7_cover21.cpp:9`.

### C02: DFS target/ignore branching completeness

Context: C01. Goal: DFS target/ignore branching completeness.

Rule and side conditions: For a putative successful S*, maintain chosen subset S* and ignored targets outside its known retained closed neighborhood. Select its first available target dominator, or ignore a target truly uncovered by S*. Excluding earlier dominators loses no such path. M bounds its final uncovered count.

Evidence: `brown_r9_a6_domination.cpp:7; brown_r9_a7_cover19.cpp:9; brown_r9_a7_cover21.cpp:10`.

### C03: Pruning, terminal predicates and termination

Context: C02. Goal: Pruning, terminal predicates and termination.

Rule and side conditions: Candidate count and largest individual gains give optimistic bounds. The witness path has sufficient remaining ignore budget. Empty unignored target set still branches to eight selections. Leaves use real uncovered/spare counts and cover21 adds h. Every recursive step increases selection depth or ignored count.

Evidence: `brown_r9_a6_domination.cpp:5; brown_r9_a7_cover19.cpp:9; brown_r9_a7_cover21.cpp:10`.

### C04: Concrete completed finite exclusions

Context: C03, P06. Goal: Concrete completed finite exclusions.

Rule and side conditions: Fresh compilation and one-CPU runs finish with a6:14/1189/zero; a7-19:42/630/107074/zero; a7-21:2/145040/5805357/zero, complete=1. Node arrays and normalized type counts match author JSON.

Evidence: `RAW_CPP_CHECKS.json`.

### P07: a=8, EE extra, full21 union

Context: B03, G03. Goal: a=8, EE extra, full21 union.

Rule and side conditions: All14 families have the three repeated points as a selected triangle. Its one deleted edge permits at most two double endpoints. sigma<=2,e<=2,j<=4; retained I plus repairs <=20.

Evidence: `BROWN_R9_EIGHT_III_OBSTRUCTION.md:33; RAW_FINITE_CHECK.json`.

### P08: a=8, EE extra, union20

Context: B02, B03, G03. Goal: a=8, EE extra, union20.

Rule and side conditions: All42 families and their two EE options satisfy the six Z-incidence facts. For e<=1 reach <=19 I. At e=2 only k=j-sigma<=2 degree-one I points cover Z; old coverage 0,3,5 plus new budget2-k gives2,4,5<6.

Evidence: `BROWN_R9_EIGHT_III_OBSTRUCTION.md:44; RAW_FINITE_CHECK.json`.

### P09: Every all-II r=9 pattern

Context: B02, B03, G02, G03. Goal: Every all-II r=9 pattern.

Rule and side conditions: Union covers I; base spare <=R=3a-21 and remaining II deletions add at most2 each, so sigma<=a-3<=6. e=0 and C demand requires j<=sigma; exact substitution yields I coverage<=3j<=18.

Evidence: `BROWN_NINE_DELETE_OBSTRUCTION.md:41`.

### P10: a=8, CE extra

Context: B02, B03, G02, G03. Goal: a=8, CE extra.

Rule and side conditions: III union covers21; base spare<=3 and CE gives at most1 at C. sigma<=4,e<=1, retained C coverage<=e, hence j<=4. With sigma=D-j+epsilon_C, I bound=3j+3e+epsilon_C<=16.

Evidence: `BROWN_NINE_DELETE_OBSTRUCTION.md:59`.

### P11: a=8, IE extra

Context: B02, B03, G02, G03. Goal: a=8, IE extra.

Rule and side conditions: Union21:base spare<=3 plus1; union20:base spare<=4 and extra I endpoint is the missing vertex, giving no extra spare. sigma<=4,e<=1,j<=5. Exact substitution gives I bound<=19 (j>=e), or2 when j=0,e=1.

Evidence: `BROWN_NINE_DELETE_OBSTRUCTION.md:74`.

### T01: Fixed-Brown extension requires at least10 old deletions and equally many old-old additions

Context: L01, L02, L03, L04, L05, L06, P01, P02, P03, P04, P05, P06, C04, P07, P08, P09, P10, P11. Goal: Fixed-Brown extension requires at least10 old deletions and equally many old-old additions.

Rule and side conditions: Cases r<=7,r=8,r=9 are exhausted. All dependencies are read and discharged by local mathematics plus explicit completed finite checks; no arbitrary-order58 nonexistence inference.

Evidence: `BROWN_NINE_DELETE_OBSTRUCTION.md:95`.

## Final closure and boundaries

The DAG runs from concrete finite facts and the order-58 hypotheses through the root resource lemma, earlier deletion exclusions, finite r9 cases, and algebraic r9 cases to T01. There is no dependence on T01 from an earlier node. The known-deletion enumeration can repeat actual deletion sets, but need not identify a unique representation; existence of one representation per candidate is enough for exclusion.

The single reported issue was a cosmetic universal-wording error in a6 line27. The parent/author corrected “one triangle” to “at most one triangle”; the reviewer re-read it. No assumption, theorem statement, computational input, or proof dependency changed.

The full exact degree-diameter optimum, arbitrary order-58 nonexistence, attainable edit distance ten, and any Lean theorem remain outside this audit's claims.

