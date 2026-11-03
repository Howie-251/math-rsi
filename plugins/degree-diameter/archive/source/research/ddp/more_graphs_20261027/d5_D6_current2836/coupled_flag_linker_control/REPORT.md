# One coupled H4 flag/linker subdivision control

The one frozen 2838-vertex control is refuted by its first new root and is stopped. It is simple, connected and 5-regular, but new vertex2836 has eccentricity7 and thirteen old targets outside radius6. Global diameter and the total ordinary unordered bad-pair count were not computed.

The source is the author's actual 2836-vertex graph: a 2730-vertex H(4) incidence core with106 flags subdivided, with a cubic linker F on the106 inserted vertices. The local construction.author.json is an edge-list recipe; the author's README gives the geometry and actual source2836.author.edges.txt binds all flags and linker edges. The existing Wiki closes only preservation of every source edge, because all old vertices have degree5. The present four-edge deletion rule is outside that closed scope. The author's source diameter6 evidence was inherited, not repeated.

## Frozen structural prediction

Choose the first lexicographic linker edge, then the first vertex-disjoint linker edge. For each smaller endpoint take its original flag's point, and that point's smallest still-unsubdivided incidence line. Each new vertex simultaneously subdivides that core flag and its linker edge; join the two new vertices. The intended complement is that a new root sees both ends of a working linker edge and shares a point with an existing flag, while its buddy supplies a second linker pair.

The chosen incidences are (911,1775),(308,1760). The chosen linker edges are (2730,2765),(2731,2788). Remove these four edges. Put

    A={911,1775,2730,2765}, B={308,1760,2731,2788},
    N(2836)=A union {2837}, N(2837)=B union {2836}.

Only two new vertices are used. Each has two flag endpoints, two linker endpoints, and its buddy: degree5. Each old endpoint loses and regains one edge. The graph has2838 vertices and7095 edges; the in-memory actual adjacency was checked simple and5-regular. The prediction, frozen in PREDICTION.json before radius computation, was that both new roots would cover all old targets within6. This is a necessary condition, not an old-old diameter guarantee.

## Exact obstruction in this control

Let G0 be the source with the four chosen edges removed. A shortest path from the first new root to an old target either enters G0 through A or uses the buddy edge immediately and enters through B. If it uses the buddy later, replacing the prefix by the direct buddy edge is shorter. Therefore

    d(2836,t)=min(1+d_G0(A,t),2+d_G0(B,t)).

For target408, the two G0 distances are6 and5. Both routes therefore need7 steps. One actual shortest path is

    2836-2730-2785-2822-2781-2744-2819-408.

The first-root BFS visited all2838 vertices and found exactly13 old targets beyond6: ten points, two lines and one old flag. These are one root's missing targets, not thirteen total unordered graph bad pairs. The second new root and old-old pairs were not checked after this necessary condition failed. A single target-root traversal in G0 supplied the exact distance decomposition above, without any old-source diameter revalidation.

Passing the two new roots would still leave old-old coverage: shortest old-old paths can stay in G0, use one new root as a two-edge bridge between its neighbor set, or use the three-edge bridge through both roots. Source-edge subdivision can lengthen old routes; degree arithmetic alone cannot resolve this obligation. Here the first new root already disproves diameter6.

CPU used0.022448017 seconds. One actual implicit graph, one new-root BFS, one diagnostic single-target BFS in G0, zero original-source diameter BFS. No alternate incidences, linker choices, buddy rules or helper grid were evaluated. No complete graph edge file was exported because the necessary condition failed. This closes exactly this frozen control and leaves other H4 flag/linker surgeries open; the thirteen-target count does not authorize local score tuning.
