# Fixed 7531 graph: one-point retained-edge cap-26 obstruction

Let G be exactly the literal graph ../graph_d26_D3_n7531.edges. The degree and full-neighborhood check reads only this edge table. No source reconstruction, radius-2 expansion, BFS, new graph or solver is used.

Partition its vertices into L, the 306 vertices of degree 25, and H, the 7225 vertices of degree 26. The literal check establishes:

- Every vertex of L has a full neighborhood of size 25 contained in H; there are no edges inside L.
- Equality of full neighborhoods partitions L into 289 classes C_1,...,C_289: 272 singleton classes and 17 doubleton classes.
- Writing A_i=N_G(v) for any v in C_i, the 289 sets A_i are pairwise disjoint, each has size 25, and their union is H. Equivalently, for h in A_i its low neighbors are exactly C_i.

The 289 newly added clones are all in L. The other 17 low vertices are the old chosen flag centers. RESULT.json gives their labels and the exact 17 doubleton classes. Each doubleton contains one old flag center and its corresponding clone. These facts follow directly from the final literal adjacency, without reading earlier geometry or pin-generation algorithms.

Now suppose a graph F is obtained by retaining every edge of G, adding exactly one vertex x, and maintaining maximum degree at most 26. Suppose its diameter is at most 3. Every vertex of H was already saturated, so it gains no edges. Every neighbor s of x must therefore lie in L and uses its only spare degree on x. In particular s gains no further old-old edge.

Fix s in C_i. Any path from x to an old low vertex t of length at most 3 can be chosen simple. If it begins x,s and has length 1, then t=s lies in C_i. A length-2 path x,s,t is impossible for t in L because s's old neighbors are all in H and s has no further spare degree. A length-3 path x,s,h,t has h in A_i; the already saturated h has no new edges and all its low neighbors lie in C_i. Hence t also lies in C_i. This reasoning also allows arbitrary additional old-old edges compatible with the retained-edge and degree assumptions: none can touch s or h, so none affects these short routes.

Consequently x can reach low vertices within distance 3 only in the low classes that contain one of its own neighbors. To have diameter at most 3, x must have a neighbor in every one of the 289 nonempty low classes. Thus

    degree_F(x) >= 289 > 26,

contradicting the cap. Therefore this fixed 7531 graph has no retained-edge extension by exactly one new vertex with maximum degree 26 and diameter at most 3.

This is a source-specific obstruction, not a bound on N(26,3). Cooperative additions of multiple new vertices, rewiring that deletes old edges, and other sources remain open. It does not generate a graph or run an n+1 search.

Actual diagnostic cost: 0.086647286 CPU seconds, one worker, within the 5 CPU-second budget. Zero radius-2 expansions, BFS runs and solver calls. The original candidate edge table and parameters were not modified.
