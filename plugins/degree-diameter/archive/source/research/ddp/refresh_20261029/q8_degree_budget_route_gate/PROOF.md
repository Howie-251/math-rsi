# The q8 auxiliary graph must be 5-regular

**Theorem.** Let H be a simple graph on 64 vertices containing eight specified vertex-disjoint cubes Q3. Let I be the union of their cube edges and let E = E(H) \ I. Assume every vertex has E-degree at most 2. If H has diameter at most 3, every vertex has E-degree exactly 2. Consequently E is a spanning 2-factor and H is 5-regular.

Extra edges inside a pencil are allowed. The cubes need not be induced subgraphs, and no symmetry or voltage assumption is made.

## Proof

Fix a root u and write s = deg_E(u). There are 56 vertices outside its own eight-vertex pencil. Any shortest path from u to one of those vertices contains an E edge. Classify such paths of length at most 3 by the number of initial I edges before their first E edge. This is the first **extra** edge, not necessarily the first edge leaving the pencil.

A shortest path has no immediate reversal. Arriving along an E edge leaves at most one further E choice, since the E-degree is at most 2. In a cube, two different successive I flips reach only three distance-two vertices: the six orders give each endpoint twice. Repeating the same flip returns to the previous vertex and cannot occur in a shortest path.

1. **No initial I edge.** For each of the s choices u E z, the endpoint upper bounds for all possible word types are:

   | Word | E | EI | EE | EII | EIE | EEI | EEE |
   |---|---:|---:|---:|---:|---:|---:|---:|
   | Endpoints per first E choice | 1 | 3 | 1 | 3 | 6 | 3 | 1 |

   Their sum is 18. Thus this class contributes at most 18s endpoints. In particular, EII contributes three endpoints, not six.

2. **One initial I edge.** There are three choices for u I x and at most two for x E y. From y the remaining path has length at most one: it can stop, take one of three I edges, or take at most one E edge other than yx. Therefore the words IE, IEI, IEE contribute at most

   \[
   3\cdot2\cdot(1+3+1)=30.
   \]

3. **Two initial I edges.** The nonbacktracking II prefixes end at just three cube vertices. Each has at most two E edges. Thus IIE contributes at most 6 endpoints. A backtracking II prefix produces no endpoint beyond those already reached by the shorter word E.

These are all eleven I/E word types of lengths 1 through 3 containing E. Counting endpoints that coincide, or that lie in u's own pencil, can only increase the upper bound. Hence

\[
|B_H^3(u)\setminus P(u)|\le 18s+30+6=18s+36.
\]

If s = 0 the bound is 36; if s = 1 it is 54. Both are less than 56. Diameter at most 3 therefore requires s = 2. Since u was arbitrary, E is 2-regular. A finite simple 2-regular graph is a disjoint union of cycles, proving the claim. No completion operation is needed. ∎

## Consequence for the existing q8 search scopes

- The general 8Q3 plus maximum-extra-degree-2 existence problem is exactly equivalent to the corresponding 2-factor problem. A nonregular auxiliary graph cannot supply a missing degree-13 construction.
- The earlier 1,792-edge SAT model is still restricted by requiring every extra edge to cross pencils. Its exact-degree-2 constraints are necessary, not an additional restriction. Its UNKNOWN outcome is unchanged.
- The 244-orbit SAT model allows extra edges within pencils. Within its Z8-equivariant scope, exact degree 2 likewise loses no diameter-3 candidate. The cyclic symmetry remains a restriction, and UNKNOWN remains UNKNOWN.
- General 2-factors, including those without cyclic symmetry and with extra edges inside pencils, are still unresolved. This lemma produces no K64 graph or 1,088-vertex main graph, and does not justify repeating any closed solver call.

For future generation, impose exactly two extra neighbors at each vertex from the outset; there is no separate degree-0/1 case or 2-factor-completion search. Existing documentation treating nonregular maximum-extra-degree-2 gadgets as an additional open scope can be updated by the parent agent.

## Bounded check and evidence

PREDICTION.md was written before the arithmetic check. check_local_routes.py checks the exhaustive eleven word types and only the nine ordered two-flip words at an abstract cube vertex; their endpoint multiplicities are 0:3 and 3:2, 5:2, 6:2. LOCAL_CHECK.json records the sums 18, 30, 6 and bounds 36, 54. The local calculation used 0.000063797 CPU seconds, with zero generated 64-vertex graphs, zero BFS runs, and zero solver calls. The arbitrary-graph implication is the proof above, not a graph enumeration or a Lean certification. A separate paper-only check of the word classification agreed; no additional computation was requested.
