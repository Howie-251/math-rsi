# HS59 with exactly six deleted old edges

Date: 2026-10-11. **Analytic exclusion of the entire six-edge-deletion
family.** The component and attachment budgets leave no open design. The
proof was independently checked by the cyclic-lift agent. No SAT or graph
search was run.

## Target and exact budgets

Start with a Hoffman–Singleton graph Q on 50 old vertices. Delete exactly
six old edges, add nine new vertices, and add no old–old edges. Suppose the
result has maximum degree eight and diameter at most two. It must be
8-regular, because a degree-at-most-seven vertex reaches at most 57 vertices
in two steps.

Let D be the deleted graph, r_x=d_D(x), B_x the new neighbors of old x, and
H the graph induced by the nine new vertices. Then

    0≤r_x≤6,     |B_x|=1+r_x,     sum_x r_x=12,
    sum_x |B_x|=62,               |E(H)|=(72−62)/2=5.

Write W(D)=sum_x binom(r_x,2), the number of pairs of deleted edges sharing
an endpoint. There are only binom(6,2)=15 pairs of deleted edges, so

    W(D)≤15,
    total old-mediated new-pair slots
      =sum_x binom(1+r_x,2)=12+W(D)≤27.             (1)

These slots count actual shared-old-neighbor witnesses in the same graph.
Every pair in distinct components of H must use one of them.

## 1. Complete component-size reduction

H has at least four components, since it has nine vertices and five edges.
For component sizes c_1,...,c_k, the number of cross-component pairs is

    C=36−sum_i binom(c_i,2).

Six or more components give C≥30, attained minimally at sizes 4,1,1,1,1,1,
and therefore contradict (1). For five components, the only partition with
C≤27 is 5,1,1,1,1; the next most concentrated partition 4,2,1,1,1 has C=29.
For four components, the only partitions with C≤27 are those listed below;
the next partition 4,2,2,1 already has C=28.

| Component sizes | Cross pairs C | Isolated vertices | Necessary W(D)≥C−12 |
| --- | ---: | ---: | ---: |
| 6,1,1,1 | 21 | 3 | 9 |
| 5,2,1,1 | 25 | 2 | 13 |
| 4,3,1,1 | 27 | 2 | 15 |
| 5,1,1,1,1 | 26 | 4 | 14 |

Thus every possible H has at least two isolated vertices. The next two
sections exclude respectively exactly two and at least three isolates.
No assumption that nontrivial components have diameter two is made.

## 2. Exactly two isolates force an impossible six-edge star

The two relevant component partitions have C≥25, hence W(D)≥13.
This forces D to be a six-edge star, as follows.

If the maximum deleted degree is at most three, binom(r_x,2)≤r_x gives
W(D)≤12. If a vertex c has maximum deleted degree d=4 or d=5, remove c and
let R be the remaining deleted graph, with 6−d edges. The exact wedge identity
is

    W(D)=binom(d,2)+W(R)+sum_{x∈N_D(c)}d_R(x).

Since Q has no triangles, N_D(c) is independent. Every edge of R therefore
has at most one endpoint in N_D(c), so the final sum is at most 6−d. Also
W(R)≤binom(6−d,2). Consequently

    d=4: W(D)≤6+1+2=9;
    d=5: W(D)≤10+0+1=11.

Both contradict W(D)≥13. Thus d=6; all six deleted edges meet c and D is a
six-edge star.

Its center has seven new neighbors, so its row B_c alone supplies all
binom(7,2)=21 pairs within a seven-set. Partition that seven-set among the
four components of H. There are at least three pairs whose two labels lie
in the same component: if the nonempty intersection sizes are n_i, then

    sum_i binom(n_i,2) ≥ sum_i(n_i−1) ≥7−4=3.

Those three slots do not cover any cross-component pair. The total budget
in (1) is 27, so at most 24 slots can cover the required C≥25 distinct cross
pairs. This contradiction excludes both exactly-two-isolate partitions.

## 3. Three isolated vertices force incompatible old-leaf ports

Suppose H has at least three isolates and select any three of them as Z.
Let Y be the other six new vertices. All 18 pairs between Z and Y must be
covered through old vertices, because a vertex in Z has no incident H edge.
This is true even if Y contains a further isolate.

At old vertex x, put

    a_x=|B_x∩Z|,       b_x=|B_x∩Y|=1+r_x−a_x.

The row supplies a_x b_x cross pairs. Since 0≤a_x≤min(3,1+r_x), its largest
possible contribution for each deleted degree is:

| r | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| f(r)=max_a a(1+r−a) | 0 | 1 | 2 | 4 | 6 | 9 | 12 |

For each integer 0≤r≤6, direct substitution gives

    5f(r) ≤ 5r+2·binom(r,2)=r(r+4).

Thus

    18 ≤ sum_x a_x b_x
       ≤ sum_x f(r_x)
       ≤ 12+(2/5)W(D)
       ≤ 18.                                      (2)

Every inequality is therefore an equality. In particular W(D)=15, so every
pair of the six deleted edges intersects. A simple triangle-free graph with
six pairwise-intersecting edges is a star. To see the common endpoint
explicitly, write two intersecting edges as ca,cb: an edge intersecting both
without meeting c would have to be ab, which would create a triangle.
Therefore D=K_{1,6}.

The maximizing value in the table is unique for the relevant degrees:

- At the star center c, r_c=6 and a_c=3, b_c=4. Hence B_c contains all three
  labels in Z and a four-set T⊂Y.
- Each of the six old leaves has r=1 and a=b=1. Its port set is one label
  from Z and one from Y.

Equality in the first line of (2) means the 18 required cross pairs are
covered exactly once. The center already covers precisely Z×T. If
Y\T={p,q}, the six leaf port sets must therefore be exactly the six edges

    {{z,p},{z,q}: z∈Z},

that is, the full edge set of K_{3,2} on Z and {p,q}. This is a concrete
forced attachment design, not merely a numerical lower bound.

But every pair of the six old leaves has lost its unique old path of length
two through c: Q has no triangles, and each nonadjacent pair has exactly one
common old neighbor. All six incident edges at c were deleted, and no old
edges are added. Consequently the six leaf port sets must be pairwise
intersecting, in order to repair these old–old pairs through new vertices.
The six edges of K_{3,2} are not pairwise intersecting: choose distinct
z,z'∈Z; then {z,p} and {z',q} are disjoint. This is the final contradiction.

## 4. Exact finite arithmetic check and scope

[hs59_six_delete_budget.py](../../../computations/dd82/construction/hs59_six_delete_budget.py)
independently enumerates the integer partitions of nine with at least four
parts and cross-pair count at most 27. It reproduces exactly the four rows
in Section 1. It also computes every entry of f(r), its maximizing isolate
counts, and the seven integer inequalities used in (2). The result is saved
in [hs59_six_delete_budget.json](../../../computations/dd82/construction/hs59_six_delete_budget.json).
The complete finite arithmetic check used approximately **0.000122 CPU
seconds**. It does not enumerate graphs or substitute for the proof.

The cyclic-lift agent independently checked the component classification,
the deleted-degree bounds, the equality chain, and the final K_{3,2}
old-leaf contradiction. No unresolved attachment design remains; therefore
no SAT run or additional failed seed was required for this bounded task.

This theorem covers every embedding of exactly six deleted edges of an HS
copy, with nine added vertices and no added old–old edges. It assumes neither
an HS edge-orbit normalization nor an auxiliary controller or attachment
symmetry. Arbitrary order-59 graphs remain unresolved.

Together with the preceding zero-through-five deletion exclusions, a
successful deletion-only HS order-59 construction would have to delete at
least seven old edges. This task does not analyze seven deletions and does
not change the global DD82 interval or Lean status.

## External discussion C6

Gemini read this proof and found no mathematical gap, via the existing
Antigravity conversation with requested/CLI-selected gemini-3.8-flash-high/high.
Root independently read the substantive argument. Raw response:
`reviews/dd82/20261011_C6_hs59_layer_capacity.json`; response wording and the
rejected unrelated C5 construction suggestion are recorded in
`reviews/dd82/20261011_C6_root_notes.md`. This is corroborating discussion,
not a Lean proof or independent backend model attestation.
