# Brown eight-deletion obstruction: proof obligations

Audit date: 2026-10-11. Fresh reviewer: `/root/proof_review_brown8`.
Scope: the explicit labelled Brown graph and its edit distance from a putative
58-vertex graph. This ledger does not assert nonexistence of such a graph.

## Canonical statements and hypotheses

Let B be the finite simple undirected graph on V={0,...,56}, with the edges in
`computations/dd82/construction/brown57.edges`. Equivalently these are the
orthogonality edges on the listed normalized projective points over F_7.
For every finite simple undirected G on V union {x}, x outside V, assume
maximum degree at most 8 and diameter at most 2. Define net old-edge deletions
R=E(B) minus E(G), additions A=E(G[V]) minus E(B), and r=|R|.

- Brown construction: B has 57 vertices, maximum degree 8, diameter at most 2,
  224 edges, and the concrete structural premises listed below.
- Imported extension lemma: under the displayed G hypotheses, r >= 8.
- New theorem: under the same hypotheses, r cannot equal 8.
- Combined result: r >= 9 and |A|=r.

The last conclusion imposes an edit-distance restriction relative to B. It
does not exclude r >= 9, construct G, or prove an arbitrary-graph upper bound.

## Typed symbols

| Symbol | Type and definition |
|---|---|
| B,G | Finite simple undirected graphs, on V and V union {x} respectively |
| C,I,E | Pairwise disjoint subsets partitioning V; sizes 8,21,28 |
| C | Brown vertices of degree 7; all their neighbors lie in E |
| I | Brown vertices of degree 8 with no neighbor in C |
| E | Remaining Brown vertices, all degree 8; differs from edge-set notation E(B) |
| R,A | Sets of unordered pairs of distinct old vertices, net deletion/addition sets |
| S | Subset N_G(x) of V, cardinality 8 |
| d_v | Nonnegative integer, number of R edges incident to v |
| k_v | Nonnegative integer d_v + indicator(v in C), deficit after deletion |
| j,e | Integers |S intersect I| and |S intersect E|, j+e <= 8 |
| sigma | Nonnegative integer sum over s in S of (k_s-1); added old-edge incidences at S |
| h | Number of C outside S reached by surviving old S-C edges, or an upper bound for it |
| a,b | Numbers of distinct old III and IEE triangles with an edge in R |
| d_i^0 | Base-deletion incidence count at i for the seven chosen III edges |
| epsilon | Indicator that the I endpoint of the extra IE deletion belongs to S |

No symbol changes type. The document uses E for a vertex class and E(B) for
an edge set; their arguments distinguish them.

## Dependency DAG

Projective coordinates -> Brown degrees and diameter.
Explicit edge list -> checked C/I/E and triangle premises.
58 vertices + degree bound + diameter bound -> 8-regularity -> edge balance and deficits.
8-regularity + diameter bound -> local triangle budget.
Triangle premises + local budget -> every I vertex belongs to a destroyed triangle.
Destroyed-triangle coverage + r=8 -> exhaustive cases A--E.
Deficits + distance from x -> common spare-incidence resource bound.
Cases A--E + resource bound -> r != 8.
Imported r>=8 lemma + r!=8 -> r>=9.

No dependency points backwards. The imported r>=8 proof does not use the new theorem.

## Obligation ledger

All entries are discharged in this same-family provisional mathematical review.
Finite checks supplement, rather than replace, the uniform case arguments.

| ID | Context implies goal | Justification and hypothesis discharge |
|---|---|---|
| O01 | Projective construction -> B has order 57, maximum degree 8 and diameter <=2 | Nonzero vectors normalize uniquely; one linear equation gives 8 projective kernel points; two independent equations give a common neighbor for nonadjacent vertices. Rechecked coordinate list and every pair. |
| O02 | Explicit B -> class sizes and degree data | Read-only exact check: degrees 7^8,8^49; C/I/E sizes 8/21/28; all C neighbors in E; every E has 2 C and 3 I neighbors; every I has 4 I neighbors. |
| O03 | Explicit B -> triangle and edge types | Exact enumeration gives 14 III,42 IEE and no other triangles; each I lies in two of each type; II,IE,EE edges in exactly one triangle, CE in none. |
| O04 | G hypotheses -> every degree is 8 | A degree <=7 root reaches at most 1+7+7*7=57 vertices, contradicting diameter <=2 and order 58. |
| O05 | O04 and |E(B)|=224 -> |S|=8 and |A|=r | |E(G)|=58*8/2=232; subtract 8 x-edges. Net old-edge count remains 224. |
| O06 | O04 and diameter <=2 -> every G vertex lies in <=3 triangles | At root v, the 56 neighbor incidences excluding v lose two per edge inside N(v), giving 58<=65-2t(v). |
| O07 | O03,O06 -> destroyed old triangles cover I | Four surviving old triangles at any i would violate O06; edge additions never destroy a surviving old triangle. |
| O08 | r=8,O03,O07 -> (a,b) constraints and a=7 or 8 | Edge-disjointness of old triangles gives a+b<=8; covering I gives 3a+b>=21; hence 7<=a<=8. |
| O09 | O08 -> exhaustive cases A--E | a=8 uses one edge from each distinct III triangle. For a=7 choose seven distinct base edges; the remaining old edge has one of II,CE,IE,EE types. |
| O10 | O04 and deletion counts -> exact spare budget | Every s in S needs k_s>=1; x uses one incidence; exactly k_s-1 added old-edge incidences remain. |
| O11 | O10 and distance from x -> C coverage consumes at least max(0,j+e-h) incidences | C outside S has size j+e. Each not reached by a surviving old edge needs its own added edge from S. Its target is outside S, so it consumes one S incidence. |
| O12 | O10,O11 -> leftover incidences upper-bound new I coverage | A new length-two path x-s-i to previously unreached i outside S needs an added S-I edge. Distinct new targets require distinct incidences. Edges inside S consume two incidences and create no new exterior target. |
| O13 | Case A -> at most three repeated deletion endpoints | 8 III triangles covering 21 vertices give 24 incidences; each I is in at most two III triangles, so exactly three repeated triangle vertices. One edge per triangle implies d_i<=2 with at most three values 2. |
| O14 | Case A and O11 -> j<=3, every selected I has d_i=2, all spare incidences spent on C | e=h=0; sigma<=j and sigma>=j force equality. Each such I covers itself and only two surviving I neighbors; total <=3j<=9. |
| O15 | Case B -> at most one repeated deleted endpoint and I coverage <=3 | No IEE deletion means seven III triangles partition I. The extra II edge lies in one selected triangle and shares exactly one endpoint with its base edge. Thus sigma<=1 and j<=sigma; equality for j=1 makes its I deficit 2. |
| O16 | Case C -> coverage <=7 | Base deletions form a matching; the extra CE edge gives one possible C spare and one E deficit. That E retains only one C neighbor, so C needs >=j additions; e<=1,sigma<=1,j<=1. I coverage <=4j+3e+sigma-j<=7. |
| O17 | Cases D,E -> base deletions have at most one repeated endpoint | At most one IEE triangle is destroyed, covering at most one I; seven III triangles thus cover >=20 I. Their 21 incidences and multiplicity <=2 permit at most one repeated vertex. |
| O18 | Case D -> sigma<=2 and j<=3 | C and E have no spare; sigma=sum(d_i^0 over S intersect I)+epsilon-j<=2. At most one deficient E gives e<=1 and h<=2e; O11 gives j<=e+sigma<=3. |
| O19 | Case D -> I coverage <=13 | Each selected I covers <=5-d_i^0 old I points including itself; the E endpoint retains two I neighbors. Substituting the exact sigma identity gives 4j+2e+epsilon-max(0,j-e). If j>=e this is <=13; if j<e, j=0,e=1,epsilon=0, giving 2. |
| O20 | Case E -> I coverage <=17 | e<=2,sigma<=1; sigma=sum(d_i^0)-j and O11 yield j<=e+1<=3. Each selected E still has 3 I neighbors. Coverage <=4j+3e-max(0,j-e), at most 17 for j>=e and at most 10 otherwise. |
| O21 | O13--O20 and O09 -> no r=8 | Every exhaustive case reaches fewer than all 21 I vertices from x within two steps, contradicting the G diameter hypothesis. |
| O22 | Imported extension proof -> no r<=7 | Triangle coverage yields 21<=3r. If r=7, the destroyed III triangles partition I, deleted edges form a matching, and all deficits are one on C plus 14 I endpoints. Thus no added old edge touches S; reaching C forces S=C, which cannot reach I. |
| O23 | O21,O22,O05 -> r>=9 and |A|=r | Integer r satisfies r>=8 and r!=8; edge balance is already established independently. |

## Assumption applications and inapplicable analytic checks

Every application of the local triangle bound uses the same G with order 58,
maximum degree 8 and diameter at most 2. Every class/triangle statement concerns
the fixed B, not G after edits. Reachability uses surviving B edges plus arbitrary
added old edges; no matching assumption is imposed outside the r=7 dependency.
The case bounds deliberately overcount overlaps, which preserves upper-bound
direction. No limits, integrals, probability assertions, big-O estimates,
uniformity issue, induction or symmetry quotient occurs.
