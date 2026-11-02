# Binary affine-line lifts: capacity derivation and a bounded 102-control profile

Date: 2026-10-26. Scope: a simple undirected6-regular controller `H`, invertible affine edge maps on `F2^3`, one binary line parameter per edge, and inverse-consistent reverse edge relations. The prospective full graph has `8|H|` vertices and degree12. Thus a102-point controller would give816 vertices, above the currently saved810-point `(12,3)` baseline, **only if all affine coverage obligations are also met**.

This changes the field and control degree from the earlier `F3^3`/4-regular mechanism; it is not a new seed in that unchanged family.

## 1. Route-sum bound

A fixed control walk of length0,1,2,3 reaches at most1,2,4,8 fiber points. An immediate edge reversal has two dependent transported directions, so a length-two reversal reaches at most2. There are6 such walks at each vertex, reducing the naive bound by `6(4−2)I=12I`.

For each adjacent ordered pair `(u,v)`, the immediate-reversal length-three walks consist of one `u v u v` (capacity2), five `u w u v` with `w≠v` (capacity≤4), and five `u v w v` with `w≠u` (capacity≤4). The reduction is `(8−2)+10(8−4)=46` per adjacent pair. Therefore

`C=I+2A+4A²+8A³−12I−46A = 8A³+4A²−44A−11I`.

This is an upper bound, not a sufficient routing condition. A necessary condition is `C_uv≥8` for every ordered pair.

For adjacent vertices, `(A³)_uv≥11` by the listed reversal walks, so their capacity is automatically≥44. For distinct nonadjacent vertices, the condition is exactly

`2(A³)_uv+(A²)_uv≥2`.

In particular, zero or one common neighbor requires a three-step walk. Two or more common neighbors may pass this numerical condition without any three-step walk. The earlier ternary equivalence `A³>0` cannot be imposed as a necessary condition here.

## 2. A stronger same-fiber union obstruction

If a control vertex `u` is not in any triangle, there is no closed control walk of length3 at `u`. The only returning walks of length≤3 are the length-zero walk and the6 edge reversals. For a forward edge map

`y=Mx+t+lambda*b`,

the reverse relation gives after two steps

`x+(lambda+mu)M^-1 b`.

Thus each returning image is a binary line through the same original point `x`. Six such lines have union size at most `1+6=7`, including the zero-length route. This is strictly smaller than8. Hence **every controller vertex must belong to a triangle**.

This condition is genuinely stronger than the route-sum polynomial on the diagonal: without a triangle, that polynomial gives `C_uu=4·6−11=13`, which would incorrectly appear sufficient. We are not asserting the polynomial is invalid; it is an intentionally loose upper bound that misses overlap.

With at least one triangle, `(A³)_uu≥2` and the polynomial diagonal condition passes automatically, but actual affine same-fiber coverage still needs checking.

## 3. An exact two-route obligation for a future affine chart

Suppose distinct nonadjacent controller vertices have exactly two common neighbors and no length-three walk. The two length-two route images must cover all8 points. Each has size≤4; hence both must be affine planes of rank2, and they must be disjoint. In `F2^3`, two nonparallel affine planes intersect, so they must share one direction plane `V` and be its two distinct cosets.

For the two route maps `M_i x+t_i+V`, let `ell` be the nonzero linear functional with kernel `V`. Coverage for **every** source point `x` is equivalent to

`ell(M_1−M_2)=0` and `ell(t_1−t_2)=1`.

This is not imposed in controller search, which has not yet chosen edge charts. It identifies the real next affine obligation if such a controller is found. In particular, limiting every edge translation to zero would fail at these pairs; the present mechanism allows general affine translations and is not silently narrowed to that special case.

## 4. Profile domain, objective, and baseline checks

`research/ddp/second_mechanism/control_binary102.cpp` performs unrestricted degree-preserving two-edge switches on simple6-regular102-vertex controllers. No triangle blocks or permutation decomposition are held fixed. One single-CPU batch was authorized with a120-second wall budget. It saves its best full edge list and full `A²,A³` matrices; it stops early if the necessary conditions hold.

The minimized score is

`sum_(u,v) max(0,8−C_uv) + number of vertices in no triangle`.

This is a count of necessarily missing endpoint-fiber points under the stated upper bounds: each missing-triangle vertex contributes at least one, by §2. It introduces no arbitrary tradeoff weight. A score ofzero only identifies a necessary controller; it does not provide affine charts or a valid816-vertex graph.

Before search, the full C++ `A²,A³` matrices and score were compared to independent NumPy multiplication for two explicit6-regular graphs:

- `K7`: passes the necessary conditions, score0.
- The recovered public120-vertex `(6,3)` graph: all120 control vertices are triangle-free, and its non-diagonal capacity deficit is6240, total score6360. Thus that known graph is not an immediate controller for this binary lift, even apart from the diagonal obstruction.

Evidence: `control_binary102_sanity.json`. The actual search handle is95849; its terminal state and final bottleneck are recorded below after observing completion. No further parameter cascade is authorized by a miss in this batch.

## 5. Observed terminal result and exact bottleneck

The single job was polled to terminal exit0, session95849, after120 seconds,4,810,410 evaluated switches, and8 restarts. Its best necessary-condition score is2516, so **no qualifying controller was found**. The saved graph is simple6-regular with102 vertices and306 edges; its actual diameter is4.

The failure is localized as follows:

- 85 unordered control pairs have no walk of length2 or3. Each ordered direction has route capacity0 and lacks all8 endpoint-fiber values under the bound.
- 135 further unordered pairs have exactly one common neighbor and no length-three walk. Each ordered direction has route capacity4 and lacks at least4 fiber values.
- 76 control vertices lie in no triangle; each necessarily misses at least one value in its own fiber.

Thus the objective decomposes exactly as `2·85·8 + 2·135·4 + 76 = 2516`. The failure is not just an affine rank choice: these control-pair shortages already make every chart over this particular controller invalid.

Evidence: `control_binary_n102.edges`, `control_binary_n102.json` (both full matrices), and `control_binary_n102_validation.json`. The independent Python check rebuilds adjacency from the edge list, checks simple6-regularity, compares the entire `A²,A³` matrices, recomputes the polynomial and triangle obstruction, and performs all-source BFS. It finds170 ordered control pairs at distance greater than3, agreeing with the85 unordered capacity-zero pairs.

This was a heuristic search over a larger genuine mechanism domain, not an exhaustive enumeration of102-point controllers. It does not exclude the binary affine mechanism, the controller order, or arbitrary816-point degree12 diameter3 graphs. No additional parameter or seed cascade was started, and no search process remains running.
