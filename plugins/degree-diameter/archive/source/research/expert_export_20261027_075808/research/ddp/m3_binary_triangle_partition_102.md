# Binary 102-control profile with a fixed triangle partition

Date: 2026-10-26. This is the root-authorized follow-up to the unrestricted binary controller profile, incorporating its observed missing-triangle obstruction into generation. Scope is the explicit subfamily of simple6-regular102-vertex controllers containing the fixed34 vertex-disjoint triangles `{3k,3k+1,3k+2}`. The102 triangle edges are fixed. Every vertex has four additional external neighbors, for204 external edges; no extra edge is allowed inside a triangle block. Additional triangles using external edges are permitted.

## Mathematical entry check

The necessary conditions remain those proved in `m3_binary_capacity_102.md`:

- Every control vertex lies in a triangle, necessary because six binary return lines through a common point cover at most7 of8 points in its own fiber when there is no triangle.
- For distinct nonadjacent control vertices `u,v`, `2(A³)_uv+(A²)_uv≥2`; adjacent pairs pass the capacity inequality automatically.

The first requirement is now automatic for every generated candidate. The minimized score is exactly `sum max(0,8−C_uv)` with `C=8A³+4A²−44A−11I`; diagonal entries also pass automatically. A zero score would still be only a necessary controller, not an affine lift or new degree/diameter lower bound.

No immediate contradiction for102 vertices follows from the available capacity count. In every6-regular controller, each row of `C` sums to1597. With the fixed triangle, its diagonal entry is at least29, the two neighbors in that triangle have entries at least48 each, and its four other neighbors have entries at least44 each. Requiring all remaining entries to be at least8 gives

`1597 ≥29+2·48+4·44+8(n−7)=8n+245`, hence `n≤169`.

This elementary necessary bound permits102; it does not prove that the triangle-partition subfamily contains a feasible controller. No broad classification or new existence claim is made.

## Concrete generator and batch

`second_mechanism/control_binary102_triangles.cpp` keeps the fixed triangle edges in the first102 positions of the edge array. It starts the external graph with the modular offsets3 and6, giving each vertex external degree4, and randomizes only those external edges. Every mutation chooses two external edges `(a,b),(c,d)` and replaces them by `(a,c),(b,d)`, rejecting repeated endpoints, duplicate edges, and endpoints in the same triangle block. Thus all6 degrees, the triangle partition, simplicity, and the number of external edges are preserved. The reverse switch restores exactly the old graph when rejected by the annealing criterion.

The implementation reuses the exact walk-count routine and capacity score independently checked for the previous binary profile; the changed generator and invariants are checked from the saved graph. One single-CPU run has a120-second wall budget and stops early if capacity passes. It saves the complete graph and full `A²,A³` matrices. Actual tool handle:87795. No other parameter or unchanged budget extension is part of this batch.

## Result status

The final result is appended only after observing the actual terminal handle and independently rebuilding the saved adjacency. The scope remains this fixed triangle partition, even if a search miss occurs.

## Local affine assignment enabled by the triangle partition

There is a concrete way to solve the same-control-fiber obligation once a controller passes. On the three internal edges of each triangle, take identity linear maps, zero translations, and the three line directions of a basis of `F2^3`. A closed walk once around that triangle has these three independent parameters, so from every source point it covers all8 points of its own fiber. This guarantee is independent of the external charts. It is a constructive initial choice, not a claim that all successful charts can be normalized this way.

For two different control vertices in that triangle, the routes confined to the triangle give the union of the three coordinate planes, covering7 of8 fiber displacements. The missing displacement is the sum `t` of the three basis directions. If the source control vertex has some external edge whose two-step return line has direction `t`, following that return by the chosen internal edge supplies this missing displacement in3 steps. Thus choosing at least one such external return direction at each control vertex also resolves all pairs inside each triangle block. This does not resolve cross-triangle pairs. In particular, making every external transported direction globally identical would destroy full-rank coverage on many three-external-edge routes, so that extra restriction is not imposed in the controller profile.

## Observed terminal result

The run was polled to terminal exit0 on handle87795 after120 seconds,4,068,096 evaluated switches, and8 restarts. It did not find a necessary controller. The saved best graph has capacity deficit2800 and no triangle-free vertices. Its exact failure decomposition is

`2·124·8 + 2·102·4 = 2800`:

- 124 unordered control pairs have no two- or three-step walk;
- 102 unordered control pairs have exactly one common neighbor but no three-step walk.

The graph is simple6-regular on102 vertices, with306 edges. All34 prescribed triangles, all102 fixed triangle edges, all204 external edges, and external degree4 at every vertex were independently confirmed. Its diameter is4, and all-source BFS finds248 ordered pairs at distance greater than3, matching the124 unordered capacity-zero pairs.

Artifacts: `second_mechanism/control_binary_triangles_n102.edges`, `.json` (complete `A²,A³`), and `_validation.json` (independent NumPy matrix equality, exact capacity/triangle checks, and all-source BFS). The triangle obstruction has genuinely been removed from generation, but the global short-route shortage remains. This batch does not exclude all controllers with a triangle partition, arbitrary102-point controllers, or the binary affine lift mechanism. No candidate was handed off for affine chart implementation, because none passes the necessary control condition. No budget extension or additional parameter run was started, and the job is terminal.
