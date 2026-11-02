# C37 diagnosis of the 666-vertex 4+1 graph

The 18-vertex quotient has enough distinct formal five-step voltage expressions for every target fiber. However, the seed is a strict local minimum under every single-voltage change that changes its lifted edge set. No optimization trajectory was run.

## Exact quotient and legality

The source is `computations/ddp/m1/d5_four_one/p37_m9_r7.search.best.edges`. Its positive generators in `(a,c,b,d)` order are `(1,0),(0,1),(21,4),(15,4)` in `F37 ⋊ C9`, with action 7. The only cross voltage is identity. A group vertex is `(side,x,i)` with source label `side*333+x*9+i`.

Retain only simultaneous translations `x→x+t`, the normal `C37`. Base vertices are `(side,i)`, encoded `side*9+i`, and each oriented base edge carries an additive `F37` voltage. For each `i` modulo 9, the 45 edges are:

| Edge type | Oriented base edge | Voltage |
|---|---|---|
| a | `(0,i)→(0,i)` | `7^i` |
| c | `(0,i)→(0,i+1)` | `0` |
| b | `(1,i)→(1,i+4)` | `21·7^i` |
| d | `(1,i)→(1,i+4)` | `15·7^i` |
| cross | `(0,i)→(1,i)` | `0` |

Thus there are nine loops and nine pairs of parallel nonloop edges. Each loop contributes both directions and degree two. Its voltage must be nonzero. Parallel edges must have different voltages when oriented in the same direction. Other nonloop edges may have zero voltage. For a loop, voltages `v` and `−v` define exactly the same undirected lifted edge set.

`diagnose.py` expanded these oriented edges for all 37 translations and checked exact edge-set equality with the saved source. Every lifted vertex has degree 5. The calculation does not replace the multigraph with a simple base graph or permit a zero loop.

## Symbolic path capacity and actual failures

For each of the 18 roots at fiber coordinate zero, the script enumerated all base walks of length at most 5, accumulating a vector of signed edge-use coefficients over `F37`. Identical vectors at the same target base vertex were deduplicated. The corresponding linear expression evaluates the endpoint fiber coordinate. These are all walks, so the test includes the root itself and backtracking; no shortest-path assumption is used in enumerating expressions.

Across the 324 ordered base pairs, the number of distinct expressions ranges from **71 to 105**, always exceeding 37. This gives no immediate fiber-capacity obstruction. It does not prove simultaneous solvability of all coverage conditions.

Every evaluated coordinate set was compared, element for element, with independent BFS in the original 666-vertex edge list from the corresponding root. All 18 comparisons agree. The 9 roots on side 0 each miss three vertices; the 9 roots on side 1 each miss one. The sum is **36**, giving exactly `37*36/2=666` bad unordered pairs. All missing vertices are at distance 6.

The only deficient ordered base fibers are:

- Nine diagonal side-0 fibers: 79 formal expressions evaluate to 35 distinct values, missing `±10·7^i` at `(0,i)`.
- Nine forward cross fibers from `(0,i)` to `(1,i+2)`: 89 expressions evaluate to 36 values, missing `3·7^i`.
- The nine reverse cross fibers, with the opposite missing displacement.

All other 297 ordered base pairs cover every field element. The deficiencies are therefore caused by collisions among actual evaluated expressions, rather than a shortage of formal expressions.

There are 333 bad pairs within side 0, 333 across the sides, and none within side 1. For each residue `i`, the bad edges on the 37 vertices `(0,x,i)` form the cycle with step `10·7^i`, which is a 37-cycle because this step is nonzero. Every cycle vertex has one bad cross partner `(1,x+3·7^i,i+2)`, and these partners are distinct leaves. The complete bad-pair graph is precisely **nine disjoint 37-cycles, each with one leaf attached to every cycle vertex**: nine connected components of size 74. Its degrees are 3 on side 0 and 1 on side 1.

## Complete single-voltage neighborhood

The C++ measurement changes one of the 45 edge voltages to each of the other 36 values, always restoring the exact seed before the next trial. Of 1620 changes:

- 9 create zero loops and are rejected.
- 18 merge a parallel pair and are rejected.
- 1593 are legal and receive complete depth-5 BFS from all 18 representatives.

There are **0 improving changes**, **9 neutral changes**, and **1584 worsening changes**. Every neutral change is a loop orientation reversal `v→−v`, which leaves the full graph unchanged. The remaining parameter changes all produce a different edge set from the seed. They were not deduplicated against one another; for example, `v` and `−v` also describe the same changed loop graph.

For graph-changing moves the missing-sum increase has minimum **44**, median **92**, and maximum **232**:

| Changed edge type | Graph-changing moves | Minimum increase | Median increase | Maximum increase |
|---|---:|---:|---:|---:|
| a loop | 306 | 44 | 88 | 132 |
| c cycle edge | 324 | 44 | 78 | 110 |
| b parallel edge | 315 | 56 | 116 | 170 |
| d parallel edge | 315 | 60 | 144 | 232 |
| cross | 324 | 54 | 91 | 128 |

One minimizing change replaces the loop at base vertex `(0,0)` from voltage 1 by voltage 4. It fixes 10 representative misses but creates 54, so the total rises from 36 to 80. Its full bad-pair total is **1480**, versus the seed's 666. The independent all-666-root verifier confirms that this measured neighbor is simple, connected, 5-regular, has diameter 6, and has exactly 1480 bad pairs.

## Consequence and scope

The quotient does not admit an immediate capacity-based rejection. The measured one-coordinate repair cannot improve the seed, and even the least damaging real change more than doubles its representative deficit. Any continuation on this quotient would need a reasoned coupled-voltage change or another construction change. This measurement supplies no evidence that a random trajectory will succeed, and no trajectory was started. It also does not exclude a simultaneous voltage assignment achieving diameter 5.

The formal diagnosis used 0.087054 CPU seconds; the complete neighbor measurement used 0.196771 CPU seconds. The independent best-neighbor all-root verification took about 0.012 seconds. These computations are within the authorized 30-CPU-second limit.

## Saved evidence

All files are in `research/ddp/m1_c37_diagnosis/`:

- `diagnose.py`, `diagnosis.json`: exact quotient, all 45 voltages, all formal counts and evaluated fiber sets summarized by count, every missing fiber displacement, and original-edge/BFS agreement.
- `base.txt`: the oriented 18-vertex, 45-edge multigraph input, including loops and parallel edges.
- `measure.cpp`, `measure`: complete legal single-voltage measurement code and executable.
- `measurement.moves.jsonl`, `measurement.summary.json`, `delta_by_generator.json`: every legal move, changes to old/new misses, full delta distribution and terminal counts.
- `measurement.best_distinct.edges`, `measurement.best_distinct.independent_bfs.json`: the complete best graph-changing neighbor and its independent all-root check.

No process remains live. The original 666-vertex source graph is unchanged.
