# CM253 cached-witness gate and complete future seam interface

This paper reviews the actual `HISTORY_SOURCE_GATE.json` and `PRED.md`. It repeats no source/field validation, unique-path calculation, graph BFS, matching/cut enumeration, solver or Lean work. The inherited one-path-per-edge cache is a subset of valid obligations, not a full diameter certificate.

## Actual source and safe symmetry

The source is the Comellas–Mitjana graph CM_253, obtained08/1994,253vertices/1012edges,8-regular and diameter3. The cached baseline edge table and old all253-root/independent-bitset validation are inherited. Its actual RIGHT recipe is

(x,y)*(u,v)=(x+u mod11,y*9^u+v mod23), label(x,y)=23*x+y.

The four positive generators and corresponding inverses are

```text
(7,2)   <-> (4,11)
(10,4)  <-> (1,10)
(1,16)  <-> (10,11)
(9,17)  <-> (2,3).
```

Left multiplication is a graph automorphism. These four inverse-pair classes cover all undirected old edges under the left action; no transitivity between classes under the full automorphism group is assumed. Classes must be identified by the full group element, not just its phase: for example two different listed elements have phase1 but different normal coordinates.

The old `source253_to_degree7.forced_edges.json` cache records one valid unique length-three source path for each of1012 old edges; the old metadata separately counted9108 unique unordered distance-three pairs. The cache is not a list of all those pairs. It supported a spanning-delete-only obstruction, which does not itself exclude a new star that repairs routes. An example path0–33–7–245 contains the indicated edge0–33 first, not in the middle. The old adjacent vertex-split NO and other-source polynomial/chart NO scopes are also distinct and are not rerun.

## Intended edit and exact distances to pins

Delete four vertex-disjoint old edges F. Let P be their eight endpoints and add one new vertex z adjacent to all P. Every old endpoint loses and regains one edge, so the hypothetical result is254vertices/1016edges and8-regular;1008 old edges remain.

Write H=G−F. Because every deleted edge has both endpoints in P, a nearest P-to-v source path cannot use a deleted edge: its later endpoint would be another, closer source in P. Thus

d_H(P,v)=d_G(P,v),
d_new(z,v)=1+d_G(P,v),
d_new(u,v)=min(d_H(u,v),d_G(u,P)+2+d_G(v,P)).

Consequently newroot radius≤3 is exactly B2_G(P)=V(G). It does not certify old–old pairs.

## Canonicalizing each cached witness without changing its position

For a cached cut edge, choose its orientation h→h*s_i in one of the four positive classes. If the saved source path traverses the edge in the reverse direction, reverse the entire four-vertex path first. Then left-multiply every path vertex by h^(-1). The selected cut is now e→s_i; its actual position is first,middle or last. Reversing the path swaps first and last; it does not convert them to middle. Uniqueness, source distance3 and the selected cut's occurrence are preserved by the automorphism.

Let the canonical saved source geodesic be q0–q1–q2–q3 and the first-cut pins be e,s. It is the unique old route of length≤3 between q0,q3. Deleting that cut therefore destroys every old≤3 route for this pair, no matter which other edges are deleted. Repair is possible only through z, with nearest-pin distance sum≤1.

- Middle position u–e–s–v: the endpoint distances to the first two pins are1 and1. The cross distances are2, otherwise the source pair would already have a2-step route. A star repairs the pair exactly when another pin equals u or v.
- First position e–s–a–v: e is already a pin, while v has distances3 from e and2 from s. Repair is exact when another pin belongs to the **closed** old ball B1(v), including v itself.
- Last position u–a–e–s: the dual condition is another pin in closed B1(u).

The first-cut pins themselves satisfy none of these hit conditions. The criteria use the full pin-set distance lemma, so they remain exact even if the source routes to a chosen other pin would individually traverse one of the other deleted edges.

## Valid subset masks and a strict three-edge capacity bound

For each canonical first type, keep every normalized cached witness's corresponding hit set above. A vertex's mask records which of these obligations it satisfies; an other-edge mask is the OR of its two endpoint masks. Every possible completion must have the three other cuts' masks OR to all obligation bits.

A maximum hit M over all old source edges is a valid upper bound for each of the three other cuts, even if the scanned pool includes source edges disallowed by the final disjointness constraints. If3M is strictly less than the number of obligation bits, no three other edges can cover the list, and the canonical first type is excluded. Restricting the maximum to edges already disjoint from the first cut is also valid for the stated disjoint-cut rule, provided that filtering is applied before any representative truncation. There is no need to infer compatibility from raw edge counts.

The obligations need not be complete for this negative implication: every listed witness is a true damaged pair, and failure to repair even one prevents diameter3. A positive capacity test, or even one actual edge triple covering the subset, is not a graph certificate. It may miss uncached unique paths, multiple-geodesic bottlenecks, newroot coverage or other cuts' obligations. Repeated normalized obligations may be deduplicated for clarity, but every mask and bound must use the same literal obligation universe.

If all four canonical first types are excluded, any hypothetical four-cut completion can be left-translated and reoriented at any chosen first cut into one of those types, contradicting its necessary mask cover. A failure for fewer types does not exclude cuts solely of unclosed types. This uses only vertex transitivity of the left Cayley action and its four edge classes, not an unproved edge-transitivity assumption.

## What a seven-edge middle matching would actually prove

A canonical middle obligation u–e–s–v has u in N(e) minus{s} and v in N(s) minus{e}. It asks the six other pins to cover the graph edge{u,v}. Thus a certificate of seven pairwise vertex-disjoint obligation edges is impossible to cover with six pins and closes that first type.

Neither seven total obligations nor nominal7-by7 part sizes imply such a matching. The actual vertex labels must be bound. A label in both neighbor parts is isolated in a true middle-critical graph: if u were also adjacent to s, then u–s–v would have length2, contradicting the source distance3. The dual argument holds on the other part. Hence active left/right labels are disjoint, but this follows from true critical witnesses, not from treating duplicated labels as distinct abstract vertices.

The cached subset may have no seven-matching even when the complete middle-critical graph does. Conversely a small matching number does not guarantee that a valid three-old-edge pin set exists, much less a diameter-three completion. No such matching is calculated by this paper.

## Complete future D3 seam verifier, distinct from the subset gate

For one separately authorized fixed candidate, every source-distance≤2 old pair is safe: a shortest path with one cut becomes at most one step longer, and replacing the whole first-to-last-pin segment handles multiple cuts. All candidate distances are≤4 from the inherited source diameter3. A source-distance-three pair is safe through z whenever r(u)+r(v)≤1, where r=d_G(P,·).

If r(u)+r(v)≥2, no source3-geodesic can contain two disjoint cuts: their first-to-last-cut segment has at least3 steps and would force r(u)+r(v)≤0. Therefore the directed-cut geodesic families are disjoint. For source distance3, the exact avoiding count is

A_F(u,v)=c(u^(-1)*v)
 −sum over all EIGHT directed orientations(a,b) of the four cuts,
             d_G(u,a)+d_G(b,v)=2
      c(u^(-1)*a)*c(b^(-1)*v),

using exact source shortest-word counts in the RIGHT model. Positive leaves a source3-geodesic in H; zero with r-sum2 gives a distance4 old pair. These counts are not supplied by merely storing one unique witness for each old edge.

Choose one orientation per cut for parameter enumeration. For k=0,1,2 enumerate u in S_k(a), v in S_(2−k)(b). Any damaged unordered pair has a source3-geodesic through a cut; reversing the pair if necessary places it in one of these chosen-orientation seams. This reduces enumeration orientations, **not** the eight orientations in the count subtraction.

The degree-eight sphere bounds give at most56+64+56=176 seam parameters per cut, or704 over four cuts. They are mathematical upper bounds, not measured or executed counts. Skip source distance≤2 and r-sum≤1; the remaining possible bad seam parameters have source distance3 and r-sum2. Passing every complete seam and the newroot B2(P) test proves all distances≤3. Exact diameter3 then follows from the maximum-degree-eight diameter-two Moore bound65<254.

Full source identity distances/counts are not currently supplied by the old witness cache. Any future data export or complete candidate verifier needs explicit authorization and must not be presented as a repeated old source-validity check. This note executes none of them.

## Stop boundary

The current authorized finite owner may test the inherited cached-obligation subset and report its exact scope. A strict negative capacity or genuine seven-matching certificate can suffice; passing the subset cannot. No new field, source, four-cut search, solver, full candidate graph, BFS, Lean or external review is started by this paper. Graph/parameter/Lean counts remain unchanged.


## Paper-only correction of the early all-four-types seven-matching prediction

The old accepted ordered distance histogram has13156 distance-two ordered pairs. Because the actual source is vertex-transitive under its left Cayley action, every root has exactly52 distance-two vertices. Let t be the number of triangles through a root; vertex transitivity makes t independent of the root. Each root has8*7=56 nonbacktracking two-step walks. Exactly2t of them end at an old neighbor, while the52 distinct distance-two vertices each require at least one of the other walks. Therefore52≤56−2t, so0≤t≤2. Counting vertex–triangle incidences gives253*t=3*T, with T the total number of triangles. Since253 is not divisible by3,3 divides t; consequently t=0. This uses only inherited source transitivity and histogram data, not a new triangle scan.

All56 nonbacktracking two-step walks at a root now end at distance-two vertices, but there are only52 such vertices. Two different middle neighbors must lead to the same distance-two endpoint, giving a genuine simple four-cycle. Thus the source has a four-cycle without needing a new cycle enumeration.

Choose an edge e–s on such a cycle and write it e–u–v–s–e after left translation and, if needed, reversing the positive first-edge orientation. Then u belongs to the left middle-neighbor part and v to the right part. The pair(u,v) has an old edge and is not middle-critical. For any other right neighbor w of s, a putative source-distance-three pair(u,w) has both u–e–s–w and the alternate u–v–s–w, the latter avoiding e–s. Under the putative distance-three assumption this alternate is a genuine three-edge geodesic: w cannot equal u (distance0) or v (already adjacent), and all remaining vertices are distinct. If a shorter route exists instead, the pair is likewise not critical. Therefore the whole u row in the full middle-critical relation is zero. Dually z–e–u–v avoids e–s for any putative critical left endpoint z, so the v column is zero.

This canonical first-edge class has a middle-critical matching of size at most6. At least one of the four left-Cayley edge classes contains an edge on a four-cycle, so the early prediction that **all four complete middle graphs have a seven-edge matching is false**. The argument does not identify which class, does not assert that every edge class lies in a four-cycle, and does not determine the other full middle matching numbers. It also does not infer a full-middle matching number from the cached middle subset.

The correction reinforces why first/last-position obligations must be retained. The actual numeric owner has separately reported a mixed-position cached-obligation gate with27 normalized witnesses per class and one-other-edge hit bound6, giving3*6<27. That gate, if accepted from its actual receipts, has a different valid negative premise and does not depend on the refuted all-middle-seven prediction. This paragraph does not rerun or validate its masks and does not replace its actual RESULT/TERMINAL. No numeric/source/field/BFS/solver or graph process was run for this correction.
