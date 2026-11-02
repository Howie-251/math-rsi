# Independent check of the affine-line controller capacity bound

Date: 2026-10-26. Scope: a **simple undirected 4-regular** control graph with adjacency matrix `A`; each oriented edge has an invertible affine map on `F3^3` plus one scalar line parameter, and the opposite orientation describes the exact reverse relation. No assertion about arbitrary degree-12 graphs is intended.

## 1. Derivation

Fix a source fiber point. A specified control walk of length `l≤3` reaches an affine image of at most `3^l` points. For a two-step immediate reversal, inverse consistency makes the two parameter directions dependent; its rank is at most1 and capacity at most3. There are four such walks at each control vertex. Thus the naive two-step contribution `9A²` must be reduced by `4(9−3)I=24I`.

For an adjacent ordered pair `(u,v)`, the three-step walks with an immediate reversal are:

- `u v u v`, rank at most1, capacity3;
- `u w u v` with the three choices `w≠v`, rank at most2, capacity9;
- `u v w v` with the three choices `w≠u`, rank at most2, capacity9.

These seven walks are distinct; no three-step walk with immediate reversal ends at a nonadjacent vertex. Their naive capacity27 must be reduced by `(27−3)+6(27−9)=132` per adjacent ordered pair. Including the zero- and one-step contributions gives

`C=I+3A+9A²+27A³−24I−132A = 27A³+9A²−129A−23I`.

This is a valid **upper bound** on the number of reachable points in each endpoint fiber, because the sum still allows overlaps between distinct walks. A necessary condition for fiber coverage is `C_uv≥27` for every ordered pair. It is not sufficient: directions can lose rank, and different route images can overlap.

## 2. Complete combinatorial simplification

Let `t(u)` be the number of triangles containing `u`.

- Diagonal: `(A²)_uu=4`, `(A³)_uu=2t(u)`, so `C_uu=54t(u)+13`. The condition is exactly `t(u)≥1`.
- Adjacent `u,v`: the seven reversal walks above give `(A³)_uv≥7`; hence `C_uv≥60`, automatically.
- Nonadjacent distinct `u,v`: put `c=(A²)_uv`, `w=(A³)_uv`. The condition is `c+3w≥3`. Thus when `c≤2`, a length-three walk is required; when `c≥3`, the numerical inequality alone would pass.

The last exception disappears once the diagonal condition is imposed. If `u` belongs to a triangle, some two neighbors `x,y` of `u` are adjacent. If `u,v` have at least three common neighbors, at most one of the four neighbors of `u` lies outside `N(v)`. Therefore at least one of `x,y` is also adjacent to `v`, and `u→x→y→v` or `u→y→x→v` is a three-step walk. Consequently

**For simple 4-regular control graphs, `C≥27` entrywise is equivalent to `A³>0` entrywise.**

This includes diagonal entries: every control vertex must be in a triangle. For distinct nonadjacent vertices, an exact three-step walk exists. For a distance-three pair, any such route is nonbacktracking; if its three transported line directions have rank3, that single route covers the whole endpoint fiber. For distance-one/two and same-fiber pairs, passing the control condition still leaves nontrivial affine coverage obligations.

## 3. Immediate global consequence and its limit

Since `A³` has row sum64, diagonal entries are at least2, the four adjacent entries at least7 each, and every other entry at least1, a controller satisfying the condition has

`64 ≥ 2+4·7+(n−5) = n+25`, hence `n≤39`.

Equivalently `E=A³−J−6A−I` is a nonnegative integral symmetric matrix with constant row sum `39−n`. This is a bounded structural representation of the necessary condition, not a claim that any feasible `E` comes from a graph.

This calculation does **not** prove an upper bound30. The currently failed fixed triangle/K4-block and fixed permutation controllers do not exhaust arbitrary simple 4-regular controls on31–33 vertices. Releasing those fixed edges is a real change of search domain.

A tempting construction is the line graph of a cubic graph: each distance-two path can be padded to length3 within a triangle, so diameter≤3 implies the condition. But its radius-three edge-neighborhood has at most `1+4+8+16=29` vertices. Therefore that special construction cannot supply a31–33 vertex controller and should not become another long search.

## 4. Bounded unrestricted controller profile

Following root authorization, a separate C++ profile uses unrestricted degree-preserving two-edge switches on simple4-regular graphs of orders31,32,33. Its objective is the number of zero entries in `A³`, including the diagonal. The fixed triangle/K4 blocks and the three-partite permutation restrictions are removed. Each initial profile has one CPU and a120-second wall budget, with explicit best adjacency and terminal output. A zero score is only a necessary affine controller, not a complete degree-12 lift or new lower bound.

The implementation and results are kept under `research/ddp/second_mechanism/control_unrestricted*`. The recovered30-vertex control graph is used for baseline sanity, with direct matrix multiplication in Python compared against the C++ three-walk counts. Actual terminal results are recorded separately rather than assumed from an elapsed timeout.

### Terminal profile evidence

All three handles were polled to terminal exit0 (sessions27959,16602,1304); each used its120-second budget. Exit status is only process status. No controller passed.

|Control order|Evaluated switches|Best zero entries of A³|Zero diagonal entries|Optimistic fiber deficit|Actual control diameter|
|---|---:|---:|---:|---:|---:|
|31|71,606,009|4|0|108|4|
|32|73,056,930|8|2|118|3|
|33|71,018,519|14|2|316|4|

The31-vertex best has every vertex in a triangle and exactly two unordered pairs at distance greater than3: `(7,11)` and `(17,30)` in the saved numbering. The32-vertex best has diameter3 but lacks a triangle at two vertices and misses exact-three-step reachability for three other unordered pairs. These illustrate why diameter alone is insufficient.

`control_unrestricted_validation.json` independently rebuilds each graph from its edge list, checks simplicity and all degrees, compares the entire C++ A³ matrix to NumPy multiplication, evaluates the original capacity matrix, and performs all-source BFS. The same record contains the terminal handles, actual iterations, and missing-pair diagnostics. These heuristic misses do not exclude the three orders. The prior fixed-block domain has been materially enlarged, but no legal affine controller or new lower bound has been obtained.

The parameter-independent bound also means that a controller restricted to three equal fibers of size `m` has `m≤13`; `m≥14` cannot work in this precise affine-line model. For improvement over the810-point baseline, the remaining general control orders are31–39, giving candidate lift orders837–1053 before affine chart feasibility is considered.
