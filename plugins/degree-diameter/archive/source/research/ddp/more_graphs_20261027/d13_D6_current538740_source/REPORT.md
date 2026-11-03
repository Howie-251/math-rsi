# Current538740 source: no complete-neighborhood clone or exact local proxy

The actual current(13,6) source was obtained and parsed once. It has538740 vertices3494842 edges, maximum degree13, and degree histogram11:3149,12:7638,13:527953. There are10787 vertices with degree slack and13936 spare slots. Nevertheless every prototype has at least4 saturated neighbors: minSatN=4 at exactly two vertices,316978 and524504; zero-fault and one-fault counts are both0. The prediction of a directly legal complete-neighborhood false twin was refuted. No candidate graph, BFS, distance cache, guard search or solver was run.

The exact primary file is deg13_diam6_n538740.txt.xz in Zenodo record23691325. Its11949252 compressed bytes are explicitly listed in the previously saved current author metadata, and the actual download returned HTTP200. It decompresses to51147499 bytes of zero-based explicit adjacency rows. No535495,534234 or538440 graph was substituted. The current author README identifies this graph as R.Rajiv's compound of four incidence graphs of H(9), with cut matchings and7300 added vertices. It separately lists538440 as superseded. That source description is inherited; the compact cut-matching or T4 coordinate recipe was not reconstructed here.

The native profile checks row labels, all degrees, simplicity and reciprocal adjacency, then counts saturated neighbors of every vertex. Source D6 is inherited from the public author construction and is not an actual all-root measurement in this work; actual_D is therefore null. The exact profile needed0.661351 native CPU seconds; compilation and driver1.368847 seconds total. Including decompression, preparation/profile CPU was2.5004925 seconds, within the10CPU budget. Primary download wall time was35.509374 seconds and separately used0.046323 CPU seconds.

## Two minimum prototypes

The literal local neighborhoods and neighbor degrees are in MIN_SAT4_LOCAL.json. Both prototypes have degree13 and their neighbor sets are disjoint.

| Prototype | Four saturated neighbors | Induced edges among the four |
|---|---|---|
|316978|117688,350682,449838,516268|117688-449838 only|
|524504|192354,258784,325214,461404|none|

For each group, the intersection of all four full-pin neighborhoods consists only of its prototype. They are not four identical-neighborhood full vertices. No unsupported assignment of these labels to a single compound T4 block or H9 coordinate class is made.

The parent's corrected sufficient replacement condition was then checked locally: for a prototype v and full neighbor u, seek a degree-free guard w such that N(u) minus {v,w} is contained in N(w). This preserves each old second-step target when u is replaced by w; the exceptional target u is within3 through any shared neighbor. The stronger condition N(u) contained in N(w) is degree-trivial for full degree13 versus free degree≤12, and is not recorded as an experimental finding.

Every possible guard for the corrected test lies in the union of free neighbors of N(u) minus {v}: the required set has at least11 elements, so a valid guard must meet at least one of them. The program generates this complete local set and checks the exact containment; it does not sample guards. All eight full pins have zero valid guards. Candidate counts are1,1,4,6 and2,5,4,0 respectively, and the required-neighborhood overlap is at most1. Only124 local adjacency rows were parsed for this test,0.159512 CPU seconds. No R5 balls, source geometry rebuild, set cover or solver was used. The initial two-neighborhood export cost0.203377 CPU seconds.

All fixed-source complete-open-neighborhood false-twin insertions are excluded by minSatN≥4. The corrected exact proxy rule is empty for these two minimum prototypes. This does not exclude arbitrary degree13 monotone neighborhoods, other prototypes or source surgery, and is not an upper bound for N(13,6). Per instruction the mechanism stops: no satN5 continuation, proxy weakening or guard ladder is started.

Reproduce the source profile with prepare_source.py followed by run_profile.py; the former reuses the exact locally saved archive if present. The executed proxy evidence is captured in PARTIAL_PROXY_CHECK.json. No new lower bound or complete candidate was produced.
