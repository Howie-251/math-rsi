# One nonlocal mechanism for the actual (11,6) source: parity anchors on its tower

Read-only mathematical task, 2026-10-29. No source redownload, source-distance computation, new ball, candidate graph or solver. The original fixed9+atmost2guard experiment remains closed. The following is a conditional new rule, not a claim that its port precondition holds.

## What the primary paper actually proves

Rishabh Rajiv, New lower bounds for the degree-diameter problem from generalized quadrangles and hexagons, DOI10.5281/zenodo.23052995, Section3/Definition2/Theorem2/Table2. The actual182618 graph is a tower of incidence hexagons H(9),H(7),H(5),H(4), not a single folded H9 graph and not the separate compound-surgery construction of Section4.

The levels have orders132860,39216,7812,2730. For each vertex at levelb and every earlier levela, one edge goes to each of the two bipartite parts A_a,B_a; destinations within either part are distinct over all later vertices.

The common coverage guarantee is the paper's elementary parity lemma: in a bipartite graph with even diameter atmost6, vertices in opposite parts are at distance atmost5. A new vertex adjacent to one point and one line therefore reaches the entire level in atmost6, independent of its particular anchors. Induction gives the tower diameter bound. It is a whole-level guarantee, not neighborhood similarity.

At levela, degrees are (q_a+1)+2a+h, where h is0/1 according to whether an attachment from a later level used that port. In the published tower, all levels have maximum degree11.

The primary D6 description says the actual186033 graph preserves all182618 edges and adds3415 vertices,29185 new-old edges, and4147 new-new edges. It does not supply a parity certificate for those3415 vertices. Its label prefix indicates legacy origin, not a proved coordinate/part map.

Primary references:
- https://zenodo.org/records/23052995
- https://zenodo.org/api/records/23052995/files/README.md/content
- https://zenodo.org/api/records/23052995/files/new-lower-bounds-degree-diameter-generalized-quadrangles-hexagons.pdf/content
- https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html , current11D6 and former182618 sections.

The downloaded primary README is3462bytes and PDF308325bytes/10pages. The59MB data-and-verification.zip was not downloaded. In particular, the actual source-witness vertex-to-level/part labeling has not been recovered here. The author identifies the old file graph_d11_k6_n182618.edges.xz inside that archive; its exact witness member and label map still need binding if this rule is selected.

## Exact free-point categories derived without a new source scan

The tower formulas give the original unsaturated vertices, all degree10:

- H9: two parts of66430,49758 used in each, so33344 free vertices.
- H7: two parts of19608,10542 used in each, so18132 free.
- H5: two parts of3906,2730 used in each, so2352 free.
- H4: internal degree5 plus6 anchors to previous levels, already11 everywhere, so0 free.

Total53828 original degree10 and128790 degree11 vertices give exactly977485 edges, matching the published old-edge count. Every new-old edge in the current expansion consumes one distinct single spare slot, since original vertices have degree10 or11. After29185 such edges,24643 old vertices remain free and all have degree10.

The saved actual current profile has24685 free vertices, hence42 are from the3415 appended vertices. Their degrees are7:3,8:11,9:13,10:15, contributing86 spare slots; old free vertices contribute24643 slots, matching24729 in the actual profile.

The lowest H4 level was already full before the3415 expansion. Since all old edges are retained, no appended vertex can have a neighbor in that level. This is a genuine obstruction to simply extending the tower by another level. The counts do not locate individual original labels in their four levels; that remains a witness-binding gap.

## One concrete new connection rule, not a larger guard set

Use six new helper vertices forming K6. Give every helper exactly six distinct old neighbors: one free point and one free line from each of the first three original levels H9,H7,H5. All36 old pins are distinct; the source old pins have only one free slot. Thus every helper has degree5+6=11 and all old endpoints remain degreeatmost11. Keep every current186033 edge.

For each helper, the parity lemma automatically covers all132860+39216+7812=179888 vertices of the first three levels within6. New-new distances are1 and all old-old routes are retained. The only remaining targets to check are the bottom H4's2730 vertices and the3415 appended vertices, total6145.

Let G denote the full actual186033 graph, and S_i its six pins for helperi. The condition for every helper to reach these remaining targets is exactly

    for every i,t:
    t in closedR5_G(S_i) union closedR4_G(union_{j!=i} S_j).

To see exactness, take the last new helper on any shortest path to an old target. If it is helperi, shortcut its prefix to length0; otherwise shortcut its prefix to the direct clique edge of length1. The suffix uses only G after one spoke. Conversely, each displayed term gives a path of lengthatmost6. The clique structure makes multiple new-old-new crossings unnecessary.

If this condition and actual degree/port constraints hold, the whole graph is validD6 on186039 vertices with1010868edges. Those numbers are hypothetical only; no graph was generated. This is not a source-geometry-only proof of the6145-target condition.

The proposed connection rule differs from the closed prototype19161: no mandatory9, no deleted saturated neighbor78477, no atmost2guards, no immediate-neighbor proxy. It selects36 type-constrained ports jointly for6 cooperating new vertices, while a whole179888-vertex part is covered by a source theorem.

## Smallest falsifiable prerequisite and remaining gap

First bind the primary old-tower vertex labels and its six upper half-levels to the current source labels, without redownloading or rechecking its diameter. Then ask only:

    Does each of those six half-levels contain at least6 current free vertices?

This is necessary to provide disjoint anchors to the6helpers; aggregate24643 oldfree is not enough to infer it. If any part has fewer than6, stop this particularK6 rule. No actual part-count measurement was run here.

Even a positive part-count result would not certify6145-target coverage. It would only justify one precise finite joint-cover model using the inherited CSR and complete current-graph R5/R4 masks on that target set. The old4201-hole guard masks cannot be substituted: they refer to one different mandatory9 set. No coverage premise for the3415 appended vertices has yet been proved.

If the witness-level binding cannot be supplied, there is currently no sufficiently bound geometric implementation of this rule. Do not label first132860 IDs as H9 or invent part intervals from the counts.

## Existing source and cache interfaces

All under research/ddp/more_graphs_20261027/d11_D6_current186033/:

- source186033.header.edges: actual186033/1010817, firstline n m,0-based undirected edges.
- adjacency.csr.u32le.bin: little-endian u32 n,2m; offsets[n+1]; neighbors[2m].
- degrees.u8.bin: actual current degrees by vertexlabel.
- SOURCE_PROFILE.json and REPORT.md: inherited degree/free/minSatN and original-source provenance.
- PROTOTYPES.json, EXACT_RESULT.json, RESULT.json: the closed uniqueonefault rule.
- guard_labels.txt, mandatory_missing.txt, guard_masks.u64le.bin: only the24676guards versus fixed4201oldholes of that earlier rule.
- exact_guard.cpp: the existing multi-target bit-propagation interface; a future selected experiment would need the different6145targets and both radii4/5, not a new all-source diameter check.

The former source data filename is identified by the author, but the level/part map is not among these existing local caches. That is the minimal remaining source-binding gap. No new experimental prediction has been frozen or executed for K6.

## Separate primary comparison for the F5 positive control

The same paper's Table1 and README report degree19/D3 order2783 and degree20/D3 order2783, the latter supplied by the same19regular graph. The earlier degree20 bound was2750, and the comparison date is September2026.

Thus the already proved localF5 construction's3750 would exceed this identified historical published2783. This read does not establish the latest degree20 record or novelty; the main Comellas table presently ends at degree16. It is incorrect either to call3750 a fresh global record from this alone, or to dismiss it as non-record on the basis of this paper.
