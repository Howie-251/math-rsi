# HS59 with exactly two deleted old edges

Date: 2026-10-11. Status: **analytic exclusion of this entire construction
family**, supported by a small exact auxiliary-graph enumeration and actual
expanded seeds. No SAT search was necessary.

## Target and exact design

Take any Hoffman–Singleton graph Q on 50 old vertices, delete exactly two
old edges, add nine new vertices, and add no old–old edges. Seek maximum degree
8 and diameter two. Every such 59-vertex graph must be 8-regular, because a
vertex of degree at most 7 reaches at most 57 vertices in two steps.

Let A' be the retained old adjacency, B the old–new incidence, and H the
induced graph on the new vertices. If r_x is the deleted degree of old x,
then

    |B_x|=1+r_x,      sum_x |B_x|=54,      |E(H)|=(72−54)/2=9.

The simultaneous coverage obligations remain

    A'+(A')²+BB^T > 0    off diagonal;
    B+A'B+BH > 0        at every entry;
    H+H²+B^TB > 0       off diagonal.

The derivation below uses all three for the same B and H. It allows every
embedding of the two deleted edges, without an automorphism reduction.

## 1. Only three small auxiliary graphs survive new–new counting

Call a new pair *bad in H* if its distance inside H exceeds two, including
infinite distance. Such a pair must be covered through a common old neighbor.

If the deleted edges meet, the three nonsingleton rows of B have sizes 3,2,2.
They can cover at most binom(3,2)+1+1=5 bad new pairs. If the edges are disjoint,
the four nonsingleton rows all have size 2 and cover at most four bad pairs.
In either case H has at most five bad pairs. It is connected: any disconnected
nine-vertex graph has at least eight pairs in different components. Since it
has nine edges, H is unicyclic.

Put W(H)=sum_a binom(d_H(a),2). Counting edges, two-step witnesses, and bad
pairs gives

    36 ≤ 9+W(H)+5,              W(H) ≥ 22.

H has degree sum 18 and all degrees are positive. If its maximum degree were
at most five, convexity maximizes W by concentrating the nine degree increments
above the all-one sequence as 4,4,1. This gives degree sequence
5,5,2,1,1,1,1,1,1 and W≤10+10+1=21, contradiction. Thus H has a vertex h of
degree d∈{6,7,8}. Only 9−d edges remain after its incident edges are removed.

### Degree six is impossible

Let S be the six neighbors of h and x,y the two nonneighbors. There are three
edges not incident to h.

If xy is absent, connectivity gives at least one S-neighbor for each of x,y.
Put a=|N(x)∩S|+|N(y)∩S| and let t be the number of remaining edges within S.
Then a+t=3 and t≤1. For either outside vertex, two-step coverage in S consists
of its own S-neighbors, plus at most one new S-vertex per S-edge. Consequently
x,y together have at least

    12−a−2t = 9−t ≥ 8

bad pairs with S.

If xy is present, the remaining two edges consist of a edges from {x,y} to S
and t edges within S, with a+t=2. Either outside vertex reaches at most a+t=2
vertices of S in two steps: it may use its own S-neighbors, the other outside
vertex's S-neighbors, and at most t further vertices via S-edges. Again at
least 12−4=8 outside-to-S pairs are bad. Both cases exceed five.

### Degree seven gives exactly two additional shapes

Let z be h's unique nonneighbor; let S be its seven neighbors. Exactly two
edges are not incident to h.

- If z has two neighbors x,y in S, these form the four-cycle h-x-z-y-h;
  the other five vertices are leaves at h. The five bad pairs are precisely
  z paired with those five leaves.
- If z has one neighbor x in S, the other remaining edge must touch x to
  leave at most five bad pairs. It is xy for y∈S, producing the triangle
  h-x-y-h with z pendant at x and five additional leaves at h. Again the
  five bad pairs are exactly z paired with those five leaves. If the other
  edge misses x there are six bad pairs.

Thus in either admissible degree-seven graph the bad-pair graph is K_{1,5}.

### Degree eight

H is K_{1,8} plus one edge between leaves and has no bad pairs.

We have therefore classified every possible H before considering old–new
coverage: it is the universal star plus one edge, or one of the two specified
degree-seven graphs. This small classification was independently derived by
the cyclic-lift agent; the proof above includes the full degree-six argument.

## 2. The degree-seven alternatives cannot be repaired

For disjoint deleted edges, B can supply only four new–new pairs, so it cannot
cover the five edges of K_{1,5}.

For adjacent deleted edges, B supplies a union of one triangle (the size-three
row) and two edges (the size-two rows). At any fixed new vertex, this union has
degree at most 2+1+1=4. It therefore cannot contain the bad-pair graph K_{1,5},
whose center has degree five.

In both deletion cases, **H must be K_{1,8} plus one leaf edge**. Its universal
vertex h has degree eight inside H and hence has no old neighbors.

## 3. Old–new coverage gives a contradiction

The following endpoint argument uses the unique old paths in the HS graph.
Deleting an old edge ab forces B_a∩B_b nonempty. It also forces B_b∩B_w
nonempty whenever w is an old neighbor of a other than b: the unique old
length-two path b-a-w was destroyed. Further deletions cannot restore it.

### Adjacent deleted edges xu and xv

Let S=B_x (size three), A=B_u (size two). The lost edge xu forces A∩S nonempty.
The six retained old neighbors of u are all ordinary singleton rows: x was
removed, and v is not adjacent to u by triangle-freeness of Q. Each of these
six singletons lies in S, because the old path from x through u was lost.

All new vertices reached from u in at most two steps consequently lie in

    A ∪ S ∪ N_H(A).

The first union has size at most four. Its elements exclude h. Since H is a
universal star plus one leaf edge, N_H(A) adds h and at most one further leaf.
Hence u reaches at most six new vertices, fewer than nine.

### Disjoint deleted edges uv and wz

Put A=B_u and C=B_v, both size two. Their intersection is nonempty. Among the
six retained old neighbors of u, at most one can be w or z: if both were
neighbors of u, the old edge wz would form a triangle in Q.

Every ordinary retained old neighbor has its singleton in C. If the one
exceptional neighbor exists, its size-two row intersects C and can contribute
at most one additional new label. Thus all new vertices reachable from u lie
in

    A ∪ C ∪ {at most one additional old-neighbor label} ∪ N_H(A).

The first union has size at most three, the exceptional old neighbor adds
at most one, and H contributes h and at most one extra leaf. Once again at
most six of the nine new vertices are reachable.

Both cases contradict diameter two. Therefore **every order-59 extension
obtained by deleting exactly two HS edges and adding nine vertices is
impossible**, irrespective of whether the deleted edges meet or how they
are embedded.

## 4. Actual bounded enumeration and expanded seed graphs

[Generator](../../../computations/dd82/construction/hs59_two_delete.py) and
[artifact directory](../../../computations/dd82/construction/hs59_two_delete/)
use a separate prefix and do not alter earlier one-edge or order-58 inputs.

After the proved reduction d≥6, the tiny enumerator labels h=0 and its
neighbors 1,...,d. It tries every 9−d-edge subset among the other eight
vertices. This covers every H up to the allowed relabeling; it does not assume
H is a fixed controller. The enumeration used **0.028215 CPU seconds** on one
pinned CPU:

| d | Inputs | Connected | Bad-pair counts among connected inputs |
| ---: | ---: | ---: | --- |
| 6 | 3,276 | 966 | 8:60; 9:120; 10:486; 11:300 |
| 7 | 378 | 168 | 5:63; 6:105 |
| 8 | 28 | 28 | 0:28 |

Among the 63 degree-seven survivors, 42 have the triangle-with-pendant shape
and 21 have the four-cycle shape. Explicit representatives and their complete
bad-pair sets are preserved in
[H_catalog.json](../../../computations/dd82/construction/hs59_two_delete/H_catalog.json).
These multiplicities are for the fixed labeled high-vertex neighborhood,
not claims about a quotient by the entire automorphism group.

Two full 59-vertex seeds use H with center 8 and leaf edge {6,7}. The adjacent
seed deletes {(0,1),(0,4)} and starts with ports

    B_0={1,2,3},     B_1={0,1},     B_4={0,2}.

A deterministic finite bipartite assignment fills the remaining singleton
ports subject to the exact column capacities and all 25 lost old-pair
requirements. This succeeds, giving a seed that satisfies **all old–old and
new–new coverage**, while exposing the remaining old–new failure.

The disjoint seed deletes {(0,1),(2,3)} and starts with

    B_0={0,1}, B_1={0,2}, B_2={0,3}, B_3={2,3}.

Its analogous capacity assignment cannot satisfy all old repairs for those
fixed ports; the generator explicitly records that failure and fills the
remaining capacities in label order to provide a complete degree-eight
candidate. Failure of this particular assignment is not used in the proof.

The independent existing BFS checker reads each saved expanded edge list,
rebuilds adjacency, and stores every bad pair, distance, and common-neighbor
list:

| Seed | n | Edges | Degrees | Diameter | Bad pairs |
| --- | ---: | ---: | --- | ---: | --- |
| Adjacent deletion | 59 | 236 | all 8 | 3 | 94 old–new |
| Disjoint deletion | 59 | 236 | all 8 | 3 | 20 old–old + 120 old–new |

The complete seeds and checks are `adjacent.seed.json`,
`adjacent.seed.verification.json`, `disjoint.seed.json`, and
`disjoint.seed.verification.json` in the artifact directory. The seeds are
failed constructions, not lower-bound witnesses. The structural contradiction
made a further SAT run unnecessary; no solver was launched for this task.

## Scope and next implication

This result excludes exactly two deletions from the old HS adjacency, with
nine added vertices and no added old–old edges. It is stronger than an
exclusion of fixed labeled edge patterns and does not rely on computational
orbit coverage. The small enumeration independently confirms an already
proved H classification; the universal mathematical conclusion does not
depend on treating the failed seeds as exhaustive.

Together with the earlier zero- and one-deletion results, any deletion-only
HS order-59 proposal must delete at least three old edges. Arbitrary
order-59 graphs remain unresolved. No new global DD82 bound or Lean theorem
is claimed, and no old order-58/n62/n63 search was restarted.

## External construction discussion C3

Gemini read the substantive argument above and found no gap, using the existing Antigravity thread and requested/CLI-selected gemini-3.8-flash-high/high. Raw response: `reviews/dd82/20261011_C3_petersen_hs59.json`. Root independently read the argument and retained exact result scopes. This discussion is provisional corroboration, not a Lean proof or backend model attestation.
C3 wording limits are recorded in `reviews/dd82/20261011_C3_root_notes.md`; route caps are necessary only and equal energy at two candidates is not a conservation law.
