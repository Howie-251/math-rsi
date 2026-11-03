# q16 duality-product replication: comparison correction

Checked2026-11-01UTC. **The guarantees can be strengthened to N(54,3)≥55512, N(55,3)≥56540 and N(56,3)≥57568.** These are direct corollaries derived here from Delorme's published construction and general induced-subgraph duplication, with one explicit standard12-vertex controller. We did not find these numerical values printed in the1985 paper or obtain corresponding published edgefiles. They are suitable as reproducible comparison guarantees under the same convention already used for the earlier55350/56375 substitutions. They are not certified global maxima or priority claims.

The potentially dangerous interface is the selected center set: **it induces514 disjoint edges; it is not independent.** The distances-at-least3 duplication special case does not justify this application. The general theorem in§7 does, as proved below.

## Published ingredients and exact scope

The primary source is [Charles Delorme, Grands Graphes de Degré et Diamètre Donnés, European Journal of Combinatorics6(1985),291–302](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf). The full primary text is already stored in `delorme1985_primary_text.txt`.

- §1,pp291–292 describes the classical symplectic generalized quadrangle with points ofPG(3,q), q+1points on each block, (q+1)(q²+1)points, and a duality for every power of2q. Thus q16 is allowed; no polarity at q16 is assumed.
- §6,pp295–296 gives the degree3(q+1),order12(q+1)(q²+1),diameter3 duality construction over a cubic12-vertex controller, with arbitrary edge orientation. Its stated diameter reason is that every ordered controller pair, including equal endpoints, has a walk of exactly3edges. The argument depends on that property, rather than a special vertex drawing; we explicitly justify this substitution below.
- §8(a),pp298–299 constructs a spread ofq²+1 mutually disjoint blocks covering all points in this same symplectic quadrangle, for prime-powerq. Combining that published spread with the published q16 duality supplies the required257-point ovoid. We do not assume that an arbitrary generalized quadrangle has an ovoid.
- §7,pp297–298 gives general induced-subgraph duplication subject to conditions(a)–(c), and discusses degree augmentation. Its general form, with the selected induced graph being a matching, is the relevant published theorem here.

We have **not identified the actual drawing of the paper's D1**. One primaryURL open returned the text; a requested page screenshot timed out. No further download, broad search or speculative claim about Fig5/D1 was made. The certificate instead uses the standard truncated-tetrahedron graph and verifies the exact sufficient condition used by§6. This distinction must remain in attribution.

## 1. One explicit12-vertex controller

Let H have vertices(i,j) with0≤i,j≤3 andi≠j. Join(i,j) to(j,i), and to(i,k) for the other two choicesk≠i,j. These are four triangles joined by the reversal matching corresponding to the six edges ofK4: the standard truncated-tetrahedron graph.

The attached tiny certificate checks simplicity, cubic regularity and an actual length-three walk for all144ordered endpoint pairs. It records each witness. There is no graph-parameter or controller-family search.

Choose

    C={(0,1),(1,0),(2,3),(3,2)}.

Their open neighborhoods are pairwise disjoint and partition the12controller vertices. The induced graph onC is2K2. In the certificate's lexicographic labels, C=[0,3,8,11] and its open neighborhoods are[1,2,3],[0,4,5],[6,7,11],[8,9,10]. The same finite run checked the495 four-subsets of this one fixed graph and found three equivalent open-neighborhood partitions; this is not a claim about other12-vertex controllers.

## 2. Why§6 permits this controller, even without identifying the paper's D1

Write I for the incidence graph of the published quadrangle and f for its duality, an automorphism ofI exchanging point and block vertices. Let B be the incidence adjacency relation. Sincef is an automorphism, f andB commute as relations.

Orient each H edge arbitrarily. A positive dart on point coordinates has relation Bf, meaning y lies on the blockf(x); a reverse dart has relation Bf⁻¹. This reverse formula is also explicitly used in Delorme§3. For a length-three controller word with signsε1,ε2,ε3∈{+1,−1}, its coordinate relation is

    (Bf^ε3)(Bf^ε2)(Bf^ε1)=B³f^(ε1+ε2+ε3).

The exponent is odd. In a generalized quadrangle every point and block are at incidence distance1or3, so a length-three incidence walk exists between every point and block: pad a distance-one edge with a backtrack if necessary. Hence every one of these signed three-edge coordinate relations covers every target point. This proves the same degree/diameter result for any simple cubic12-vertex H having the verified exact-three-walk property. It applies to this explicit truncated tetrahedron, with no assumption that it is the paper's displayed D1 and no polarity/involution assumption onf.

For q16 the resulting graph G therefore has

    n0=12·17·257=52428, degree=3·17=51, diameter≤3.

There is no loss of degree from deleting self-loops: controller endpoints differ, so even a coordinate satisfying x∈f(x) still gives distinct graph vertices. Each of the three distinct neighboring controller fibers contributes exactly17 distinct neighbors. The order exceeds the degree51 radius-two Moore bound, so the diameter is exactly3.

## 3. Ovoid and full-neighborhood partition

Take the published spread S of257blocks in this specific symplecticGQ(16,16). Let O=f⁻¹(S), a257-point set. For any blockL, a pointo∈O is incident withL exactly when its spread blockf(o) contains the pointf(L). Exactly one spread block contains that point. Thus O meets each block once and is an ovoid. This argument obtains the needed ovoid entirely from the two ingredients already in Delorme§1and§8(a); no separate elliptic-quadric identification is needed.

More generally, either duality f orf⁻¹ sends the ovoid O to a spread. For a fixed oriented controller dart, the17-point neighborhoods in its target fiber of the257source coordinateso∈O therefore partition all4369target coordinates.

Set A=C×O, of size4·257=1028. Every controller vertex has exactly one neighboring element ofC, and for that unique controller dart the preceding spread partition gives exactly one adjacent element ofA. Consequently **every vertex ofG, including vertices ofA, has exactly one neighbor inA**. The1028immutable source full neighborhoods are pairwise disjoint and partition all52428vertices.

In particular each vertex ofA has degree1inG[A], so the induced graph G[A] is514K2. This disproves the preliminary independence assumption in PRED.md. It does not invalidate the numerical bounds, because the general published duplication theorem handles this matching.

## 4. Exact use of the published general duplication theorem

Use§7 with A0=A and A1=A2=…=∅. Condition(a) is then empty. Condition(b) holds because every outside vertex has exactly oneA-neighbor. For condition(c), a componentB ofA is a single edge. Each endpoint has50neighbors outsideA. If x,y are its two endpoints, choose any outside neighborzofx: d(x,z)+d(y,z)≤1+2=3. For x=y, choose an outside neighbor and obtain2. Thus condition(c) holds for every pair in each component.

The first duplication adds1028vertices and raises degree51to52. The copied induced matching edges must be retained: a new copy has51neighbors in the old graph plus its matching partner in the copiedA, hence degree52. This is the published induced-subgraph duplication, not the project's zero-new-new immutable-false-clone recipe.

The same original A remains an induced matching after every duplication, and every existing vertex outsideA still has exactly one neighbor in that originalA. The conditions therefore apply repeatedly. Afterknewcopies ofA, every vertex is exactly(51+k)-regular and the order is

    n_k=52428+1028k.

Equivalently, each of the514original matching edges becomes a complete bipartiteK_(k+1,k+1)on its original endpoints and copies; its50outside neighbors perendpoint type remain old. Outside vertices receivekextra copies of their unique A-neighbor. This explicitly accounts for internal/new-new matching connections and rules out a hidden degree surcharge. The diameter stays3by the published theorem, or its actual shortest-walk lifting argument; the order still excludes diameter2.

|Maximumdegree|k|Directly guaranteed order|Earlier comparison|Correction|
|---:|---:|---:|---:|---:|
|54|3|55512|55350|+162|
|55|4|56540|56375|+165|
|56|5|57568|not previously fixed here|—|

The current accepted project graphs56862at54and56943at55 consequently exceed these corrected guarantees by1350and403, respectively. This statement is a comparison to the present derived guarantees, not confirmation that the project graphs beat every currently published graph.

## Evidence, attribution and stopping point

The full graph construction scheme, duality, symplectic spread and general induced duplication are Delorme's published ingredients. The explicit standard truncated-tetrahedron substitution, its four-center packing and the numerical54/55/56corollary were assembled and checked in this audit. No novelty is claimed for that assembly; no matching numeric table or edgefile was found. The displayed D1figure remains unidentified, and the original JGT1985full-text gap from other audits remains separate.

`DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_SMALL_CERTIFICATE.json` contains the actual one-controller result and all144walk witnesses. The executed tiny Python run used0.0007805CPU seconds, within10CPU; only this12-vertex graph and scalar formulas were checked. The saved `_small_check.py` reproduces that calculation. There were no large graph reads/generations, BFS, Lean, solver, install or hash computations. All local execution is terminal. The prediction was supported on three-walk coverage, neighborhood partition and resulting orders, and corrected on center independence. No further controller, q, field or degree list is dispatched by this receipt.
