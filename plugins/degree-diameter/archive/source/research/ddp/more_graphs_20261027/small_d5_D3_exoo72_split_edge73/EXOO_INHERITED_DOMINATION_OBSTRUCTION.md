# Exoo72: inherited domination obstruction closes split plus absorbed edge

Status: **VALID deductive exclusion of the frozen operation, with zero new enumeration**. No radius-two cache, candidate, source BFS, solver or modified-graph check is required. This deduction uses the already completed original-radius-two coverage enumeration; it does not rerun it or assume its earlier hub interpretation was its only mathematical consequence.

## What the old enumeration actually proved

The existing result is `research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/RESULT.json`, explained by the adjacent `REPORT.md` and implemented in `enumerate.cpp`.

It completed all 832020 three-edge matchings in the fixed five-regular 72-vertex source. For each matching it considered all six choices of the omitted endpoint: 4992120 five-vertex sets in total, with multiplicities retained. Its count `necessary_original_R2_cover` is zero. Thus, if T is the six endpoints of **any** three-edge matching and T5 is **any** five-element subset of T, then

    B2_G(T5) != V(G).

This is a statement about closed balls in the unchanged source G, not just about a graph after deleting the three edges. The old report explicitly says the original necessary test already failed in every case. Its scope is therefore usable in a different construction whose necessary condition is domination in that same original source.

The old execution had native CPU0.014127 seconds, compilation1.541390 seconds and driver-measured child CPU1.556940 seconds. All those execution figures are inherited once, not claimed as costs or repetitions of the present deduction. The old run generated no augmented graph and performed no candidate or source-diameter BFS.

## Four vertices containing one edge extend into three matching edges

Let S be any set of at most four source vertices containing the endpoints of an old edge e. Start a matching with e. Process the at most two vertices of S not already covered. Before adding an edge for an uncovered s, there are at most two matching edges, occupying at most four vertices. Since s has five old neighbours, at least one neighbour is unoccupied. Match s to it. This preserves disjointness and covers s; its partner may also cover the other remaining vertex of S.

After this process, the matching covers S and has at most three edges. If fewer than three were needed, choose an unoccupied vertex. There are plenty in the 72-vertex source, and at most four vertices are occupied. Its degree five again supplies an unoccupied neighbour. Pad until there are exactly three disjoint edges.

Consequently S is contained in their six-endpoint set T. Choose a five-element subset T5 of T containing S, which is possible because |S|<=4. Closed-ball coverage is monotone in its seed set:

    B2_G(S) subset B2_G(T5) != V(G).

So **no source set of at most four vertices containing an old edge is radius-two dominating**. The proof needs the contained edge: it does not establish that an arbitrary independent four-vertex set fails to dominate.

## Apply this to the smaller new child

In the frozen operation, N_G(v)=A union B with |A|=2 and |B|=3. The cut x-y has both endpoints outside the closed B1_G(v). The new children have edges u-A, w-B, u-w, u-x and w-y, after deleting v and x-y as specified in `ANALYSIS_COVERAGE.md`.

For the degree-four child u, set

    S={v} union A union {x}.

This has four distinct vertices in the clean domain and contains the two old edges from v to A. The preceding lemma therefore proves B2_G(S)!=V(G).

On the other hand, the source has diameter three. Its targets at distance at most two from v are covered by the seed v. For a target t in S3_G(v), coverage by A is equivalent to having a geodesic first neighbour in A; the remaining extra coverage is exactly B2_G(x). Thus

    B2_G(S)=V(G)
    if and only if E_A subset B2_G(x).

The exact new-root theorem in `ANALYSIS_COVERAGE.md` shows that the latter is precisely the condition for u to cover all old vertices within three steps, including the endpoint-port absorption of routes affected by the cut. This equivalence depends on x-y being an old edge and the stated surgery; it is not asserted for arbitrary extra ports or arbitrary matching data.

The necessary condition fails for every legal frozen choice of v,A/B,x-y. The smaller child therefore already fails diameter-three coverage. The old-old checks and the proposed new radius-two cache are unnecessary, and no Exoo72 split-edge candidate needs to be generated.

## Exact scope and chronology

This closes the fixed Exoo72, two-plus-three split, one absorbed outside-edge family deductively. It does not label a new finite batch as executed, enlarge 4992120 into another measured count, or report a failed actual73-vertex graph. Actual new graph order, exact global diameter and ordinary unordered bad pairs remain null.

The conclusion does not exclude arbitrary73-vertex degree-five diameter-three graphs, other sources, independent four-point dominating sets, additional deleted edges, further helpers or other connection rules. Although the embedding lemma is general within the fixed source, the construction application here stays with the parent-frozen outside-B1(v) endpoint domain; no broader surgery family is silently registered as tested.

The earlier 59-to85 root-capacity comparison remains true but was only a necessary capacity opening. The present inherited domination obstruction supplies the stronger complete root failure without new numerical work. Any future source for the same surgery needs to permit an appropriate four-point radius-two dominating set containing the source v-to-A star; sufficient formal degree capacity alone does not provide that property.
