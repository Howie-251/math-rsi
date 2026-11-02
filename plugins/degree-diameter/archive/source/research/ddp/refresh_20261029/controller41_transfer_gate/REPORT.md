# The saved Allwright 41-vertex graph fails the triangle gate

The single literal source is Allwright Graph 1(a), obtained previously from the Comellas-maintained [primary adjacency](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/deg4D3-41_1a_allwr_adjlist.txt) and saved at `research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges`. Its existing source check establishes 41 vertices, 82 edges, simplicity, 4-regularity and diameter 3. Those distance checks were reused, not repeated. The earlier experiment on this source excludes ordinary cyclic C9 covers; it is a different scope from the proposed F5 affine-line transfer.

The frozen triangle test stopped after vertices 0 and 1:

- Vertex 0 has neighbors {1,2,11,22} and lies in the triangle 0–11–22–0.
- Vertex 1 has neighbors {0,3,4,5}. No pair of these four neighbors is an edge, so vertex 1 belongs to no triangle.

This is a decisive self-fiber obstruction. For the proposed q-point affine-line edge relation on fibers Fq³, a two-step edge/reverse return reaches only a line through the starting fiber point. At a triangle-free controller vertex, there is no three-step closed controller walk. Hence all paths of length at most three returning to that controller vertex reach at most

\[
1+4(q-1)
\]

fiber points. This is at most 17 of 125 for F5, or 13 of 64 for F4. Three-turn full-rank properties cannot supply a missing closed controller route. Thus this literal graph cannot yield the proposed 5,125-vertex degree-20 diameter-3 lift, nor the analogous 2,624-vertex F4 lift of this affine-line type.

The result does not exclude other 41-vertex graphs or different fiber relations. As authorized, the first obstruction ended the task: no complete nonadjacent NB3 test, graph lift, BFS, solver, adjacency modification, or additional source was attempted.

Evidence: PREDICTION.md was saved before execution; check_gate.py and RESULT.json retain the literal neighbor witness and stopping point. Actual gate CPU was 0.000321952 seconds. No Wiki or parent status file was changed.
