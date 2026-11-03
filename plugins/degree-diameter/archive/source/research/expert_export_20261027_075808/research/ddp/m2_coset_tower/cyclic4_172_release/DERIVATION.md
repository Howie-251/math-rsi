# Derivation Package

## Target

Give an exact four-orbit cyclic-voltage representation of the saved 172-vertex bicayley graph, then identify the mathematical conditions removed when the fourteen base-edge voltages are made independent. The subsequent search is a fixed bounded construction batch on that base, not an exhaustive family decision.

## Status

COHERENT AS STATED. The raw parameter increase is three, but after each model's appropriate translation gauge the true independent increase is two. No approximation is used in the graph identities or distance score.

## Invariant Object

The invariant object is the complete simple undirected graph, including all 602 edges, considered under explicit vertex relabeling. For new candidates, the invariant distance objective is the exact number of unordered vertex pairs at distance greater than three.

## Assumptions

- Coordinates lie in F43; the old group is D86 with `(x,j)(y,k)=(x+(-1)^j*y,j+k mod2)`.
- The old bicayley sides A and B have reflection coordinates A=`[0,4,11,37]`, B=`[41,16,12,24]` and cross elements T=`[(0,0),(24,0),(25,1)]`.
- The new base has four vertices and fourteen undirected edges: four 01 edges, four 23 edges, two 02 edges, two 13 edges, one 03 edge and one 12 edge. These are the three perfect matchings with multiplicities 4,2,1.
- Parallel edges with the same endpoints must have distinct voltages. Reverse orientation always negates voltage. There are no base loops.

## Notation

The orbit order is `(A0,A1,B0,B1)`, numbered 0 through 3. A lifted vertex is `(v,x)`, encoded `43*v+x`. An oriented base edge from u to v with voltage z joins `(u,x)` to `(v,x+z)` for every x. Edge-array indices are 0..3=01, 4..7=23, 8..9=02, 10..11=13, 12=03, 13=12.

## Derivation Strategy

Derive each voltage directly from old right multiplication, compare the entire edge set, gauge a spanning tree to zero, and retain the cyclic translation action to justify four complete BFS roots.

## Derivation Map

1. Old right multiplication determines the raw fourteen voltages exactly.
2. An explicit orbitwise translation gauges three tree edges to zero without changing the graph.
3. The old dihedral coupling becomes two linear equations on the eleven remaining coordinates.
4. Removing only those equations gives the authorized larger family.
5. Cyclic translation on each orbit gives an exact four-root distance score.

## Main Derivation

### 1. Exact old voltage representation

For a reflection `(a,1)`, old phase-zero x is adjacent to phase-one `x+a`; its reverse is `x+a -> x`. Thus internal voltages 01 and 23 are the respective reflection coordinates.

A cross element `(t,0)` sends A0 x to B0 `x+t`, and A1 x to B1 `x-t`. A cross element `(t,1)` sends A0 x to B1 `x+t`, and A1 x to B0 `x-t`. These identities give

- 01: `[0,4,11,37]`;
- 23: `[41,16,12,24]`;
- 02: `[0,24]`;
- 13: `[0,19]`;
- 03: `[25]`;
- 12: `[18]`.

The old encoding `86*side+x+43*j` already equals `43*(2*side+j)+x`, so no preliminary coordinate permutation is needed. `run.py` independently rebuilds the old D86 edges and the raw voltage edges, and compares both sets with all 602 saved edges.

### 2. Exact spanning-tree gauge

Use tree edges 01#0, 02#0, 03#0, whose array indices are 0,8,12. Under new coordinate `x'=x+c_v`, an oriented voltage changes by `z'=z+c_v-c_u`. Set c0=0 and choose c1,c2,c3 to make these three voltages zero. For the actual seed, `c=[0,0,0,18]`.

The normalized seed is

`[0,4,11,37, 16,34,30,42, 0,24, 18,37, 0,18]`.

The three zero coordinates remain fixed during search; the other eleven coordinates are free. The normalized edge set is compared with the explicit permutation of all old edges. This also transfers the old independently checked graph's diameter and full spectrum to the seed without a repeated all-root BFS. A single four-root diagnostic in the new evaluator is reused as the first production evaluation.

### 3. Actual released degrees of freedom

Before gauge, an old representation has four A reflections, four B reflections, two even cross coordinates e0,e1, and one odd cross coordinate o: eleven field parameters. In the new fourteen-voltage representation, the old raw couplings are `v13_even=-v02_even` componentwise and `v12=-v03`.

Write a0 for the first A reflection and use the tree shifts `(0,-a0,-e0,-o)`. The normalized relevant coordinates satisfy

`v9=e1-e0`, `v10=a0-o-e0`, `v11=a0-o-e1`, `v13=a0-o-e0`.

Consequently the old image obeys exactly

`v10=v13`, and `v9+v11=v13 mod43`.

These are independent linear constraints on the eleven free tree-gauged coordinates; the internal A and B coordinates remain arbitrary subject to within-group distinctness. The old normalized family therefore has dimension nine and the new family eleven. Removing these two equations is the actual structural change. A common scalar quotient, if imposed on both, would change these counts to eight and ten; this batch does not impose that extra quotient.

### 4. Exact legality and root score

Every base vertex has incident multiplicity seven. Distinct voltages within a parallel class prevent repeated lifted edges, and distinct base endpoints prevent loops. Thus every accepted state expands to a simple 172-vertex 7-regular graph with 602 edges.

Simultaneous translation `(v,x)->(v,x+c)` preserves every voltage edge and acts transitively on each of the four 43-vertex orbits. For root v at coordinate zero, let m_v be its number of vertices unreachable within three steps. A complete BFS from each of the four roots determines all distances in the graph. The total unordered defect is exactly

`(43/2)*(m0+m1+m2+m3)`.

No equality between the A0/A1 or B0/B1 root scores is assumed after the release. The old seed's scores are `(6,6,10,10)`, giving 688 bad unordered pairs. D3 succeeds precisely when all four deficits are zero.

## Remarks and Interpretation

The independent symbolic-capacity calculation in `CAPACITY_SCOPE.md/json` is a necessary condition only. Its passage does not substitute for any BFS. The search evaluates every legal trial through all four complete roots.

The actual finite search uses the exact old seed plus 32 distinct deterministic random starts (seed 20261026172), at most nine segments per start, at most thirty strict best single-coordinate descent moves per segment, and two-coordinate legal kicks between segments. Each completed coordinate neighborhood tests all legal new values of all eleven free coordinates. There are 438 legal neighbors: 117+156+41+82+42 from the five variable parallel classes.

## Boundaries and Non-Claims

Completing these starts and segments does not exhaust the eleven-dimensional voltage family. Only this base, this modulus and these 33 starts are authorized. No capacity filter is used to omit a candidate from the local neighborhood, and no other group or multiplicity pattern is searched. The parent owns the unique independent final graph check.

## Open Risks

No algebraic or edge-relabel mismatch remains after the exact 602-edge comparisons. Whether the enlarged family contains a D3 graph remains an experimental question; a failed bounded search is not an exclusion theorem.
