# The existing matching computation excludes every at-most-three-cut single hub

The matching-extension lemma is valid. Applied to this fixed120-vertex source, it extends the already completed matching computation to every operation that deletes at most three old edges and adds one new vertex adjacent to any subset of their endpoints. None has diameter at most3. This is a deduction from saved evidence, not a new enumeration or graph computation.

## Inherited evidence and its exact scope

The source is [d6_D3_known.edges](../../../../context/DD_PORTFOLIO_START_20261026/baselines/d6_D3_known.edges). Its existing [validation](../../../../context/DD_PORTFOLIO_START_20261026/validation/d6_D3_bfs.json) records120 vertices,360 edges, minimum and maximum degree6, and D3 from all120 roots. No source verification is repeated.

The saved [RESULT.json](RESULT.json) records all7711320 unordered triples of the360 source edges visited, including all7080720 triples of pairwise disjoint edges. Every such matching triple has an endpoint set T with R2_G(T) not equal to V(G). The remaining630600 triples were rejected as nonmatching, rather than tested as candidate graphs. The final cursor is357,358,359, CPU_limited is false, and newroot_gate_pass is zero. The [producer](probe.cpp) explicitly loops a<b<c, rejects shared endpoints, and tests the OR of the complete source closed-R2 endpoint masks. The [report](REPORT.md) and [1920-byte cache](source_R2.u64le.bin) preserve the same scope. These are inherited computations; no cache query or enumeration was rerun for this deduction.

## General matching-extension lemma

Let G be a finite simple graph with minimum degree at least2k. Let F be a set of at most k edges, and let S be the union of their endpoints. Then there is a matching M of exactly k edges such that S is contained in V(M).

Write s=|S|, so s<=2k. First consider the induced graph G[S]. The edges F form an edge cover of S, of size at most k. Therefore a maximum matching M0 in G[S], of size m, satisfies m>=s-k. This is the standard matching/edge-cover identity, but only its elementary inequality is needed: take an inclusion-minimal edge cover contained in F. Its components are stars, because an edge whose two endpoints have degree at least2 could be removed. Selecting one edge from each star gives a matching of size s minus the number of cover edges, at least s-k.

There are r=s-2m unmatched vertices U in S. Thus r<=2k-s. Every u in U has at least

    degree_G(u) - (s-1) >= 2k-s+1 >= r+1

neighbors outside S. Greedily give the r vertices of U distinct partners outside S. At each step fewer than r partners have been used, so a new partner exists. These new edges are disjoint from M0 and from one another. The resulting matching covers S and has

    m+r = s-m <= k

edges.

If it has only l<k edges, delete its2l endpoints temporarily. The remaining graph has minimum degree at least2k-2l>=2, and hence contains an edge. Add such an edge to the matching and repeat until its size is exactly k. The resulting matching still covers S. The case S empty is handled by this same padding step.

The proof does not assume that F itself is a matching, and does not assume that the graph is vertex-transitive or regular. The stated sufficient degree hypothesis is all that is used.

## Apply the lemma to this source

Here k=3 and the inherited minimum degree is6. For any F consisting of at most three old edges, let S be its endpoint set. The lemma gives a three-edge matching M with S contained in T=V(M). Closed-radius neighborhoods are monotone under adding starting vertices, so

    R2_G(S) is contained in R2_G(T), which is not V(G).

The last assertion holds for every three-edge matching by the existing complete7080720-item result. Consequently no such endpoint set S R2-dominates the source. The particular containing matching need not be constructed: its existence and the universal saved computation suffice.

## Exact new-root consequence, including nonmatching cuts

Put H=G-F. Every edge of F has both endpoints in S. Deleting edges entirely inside S cannot change the distance from S to any old vertex: a shortest path starting anywhere in S may be chosen to meet S only at its starting point, and therefore uses no edge inside S. Thus

    d_H(S,t) = d_G(S,t)

for every old t.

Add one new hub x with all of S as its neighborhood, and retain every other old edge. A shortest path from x to an old vertex starts with one spoke and need not revisit x, giving the exact identity

    d_new(x,t) = 1 + d_H(S,t) = 1 + d_G(S,t).

Because R2_G(S) is not all of G, the new root cannot reach all old vertices in three steps. Hence no member of this operation has D<=3, irrespective of what happens to old-old distances.

Allowing the hub to use only a subset A of S does not escape the result. One may add the missing spokes to all of S: |S|<=6 keeps the hub degree at most6, and every endpoint lost at least one old edge, so one added spoke keeps its old degree at most6. Adding edges cannot increase diameter. A successful subset version would therefore produce a successful all-S version, which has just been ruled out. Alternatively, A is itself contained in T, so even the source radius2 upper bound already fails.

Because this source is full6regular, an old vertex outside S has lost no edge and still has degree6. It cannot be made adjacent to the hub in a maximum-degree6 graph. Thus, with no other old-edge edits, restricting the hub to a subset of S is forced by the degree bound rather than an extra construction hypothesis.

## Closure and limits

The closed family is this one actual120/360 source, at most three deleted old edges, one added hub, hub neighbors restricted to the deleted-edge endpoints, and no other new old-old edges or structural changes. The cuts may share endpoints and may number zero, one, two, or three. The result includes all subset-of-endpoints spoke choices that respect maximum degree6.

It does not exclude four cuts, two helpers, other edits that release additional old-vertex slots, another source, or arbitrary121-vertex maximum-degree6 diameter3 graphs. No121-vertex graph was generated here or by the inherited matching experiment, so actual candidate n, D, and ordinary unordered bad-pair counts remain null.

New work in this deduction: zero numerical trials, zero source or candidate BFS, zero word enumeration, zero solver calls, and zero graphs. Merge the single deductive variant in [wiki_rows_endpoint_extension.json](wiki_rows_endpoint_extension.json) into the original matching-insertion row; it is not an independent construction method or another batch of7080720 trials.
