# The 585-point polarity graph: a sharp bound for complete twin replication

## Target

Determine whether changing the multiplicities of vertices in the published
585-point degree-9, diameter-3 graph can exceed the saved degree-10/11/12
records 650/715/810 without deleting a nonabsolute vertex class or removing
any of the complete connections prescribed by the source graph.

## Status

COHERENT AS STATED. The bound below is an elementary consequence of the
actual adjacency partition; no graph search or optimization is needed.

## Invariant Object

The sum of the degrees of one chosen copy of each of the 520 nonabsolute
source vertices. Every source vertex has exactly eight neighbors among
these 520 vertices, so this sum counts every output vertex eight times.

## Assumptions

The source graph is the graph supplied on the UPC degree/diameter page at
[the implicit adjacency list](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n585d9k3.txt).
The downloaded rows, with zero-based row indices as labels, are retained in
`source585.implicit_adj.txt`. `SOURCE_PARTITION_CHECK.json` records a direct
check of simplicity, symmetry and the following partition data:

* A consists of 65 degree-8 vertices, each with 0 neighbors in A and 8 in B.
* B consists of 520 degree-9 vertices, each with 1 neighbor in A and 8 in B.

In particular, **every vertex has exactly eight neighbors in B**. The
partition check did not rerun the source graph's full-source diameter test.
The upper bound does not require its diameter to be assumed.

Replace each source vertex v by a class of w_v copies. Require w_b >= 1 for
each b in B, and allow any integer w_a >= 0 for a in A. For every original
edge uv, put all w_u*w_v edges between its two copy classes. Extra edges
inside or between classes are allowed, because they can only raise degrees.
There are no vertices outside these copy classes. All output degrees are
at most Delta.

## Notation

N=sum_v w_v is the output order. For each b in B select one output copy b*;
it exists by the assumption w_b >= 1. The original open neighborhood of b
is denoted N_G(b).

## Derivation Strategy

Use the 520 degree constraints at b*, and interchange the two finite sums.
The uniform eight-neighbor count in B gives a bound on total output order,
without assuming uniform multiplicities or a prescribed duplicated set.

## Derivation Map

1. Complete replication forces deg(b*) >= sum_{v in N_G(b)} w_v.
2. Summing the right side over all b in B counts each w_v exactly eight times.
3. The maximum-degree requirement bounds the left side by 520 Delta.
4. Compare the resulting order bound with the relevant public entries.

## Main Derivation

**Proposition.** Every graph satisfying the stated replication assumptions
and having maximum degree at most Delta has N <= 65 Delta.

For each b in B the prescribed cross-class edges give

    sum_{v in N_G(b)} w_v <= deg(b*) <= Delta.

Summing these inequalities gives the exact counting identity and inequality

    8 N = sum_{b in B} sum_{v in N_G(b)} w_v <= 520 Delta.

Dividing by eight proves the proposition. Extra edges cannot invalidate the
lower degree estimate. No independence between the duplicated vertices and
no upper bound on an individual multiplicity was used.

The bound is sharp for Delta >= 9: put w_b=1 on B and w_a=Delta-8 on A,
with no additional edges. Every B-copy has degree 8+(Delta-8)=Delta,
every A-copy has degree 8, and N=520+65(Delta-8)=65 Delta.
For this positive-weight construction, distances between distinct source
classes lift from the original graph, and two copies of one class have a
common neighbor. Thus the published source diameter-3 guarantee is retained.
This recovers an existing replication mechanism, not a new graph record.

| Maximum degree | Sharp order bound for this class | Public order on 2026-10-26 |
|---:|---:|---:|
| 9 | 585 | 585 |
| 10 | 650 | 650 |
| 11 | 715 | 715 |
| 12 | 780 | 810 |

The public values and the descriptions of the known 650/715 replication
graphs were read from the [UPC diameter-3 description page](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)
on 2026-10-26. This mathematical bound was derived here from the saved
adjacency partition; no originality claim is made for it.

## Remarks and Interpretation

Changing which vertices are duplicated, allowing unequal multiplicities,
or deleting some absolute classes cannot beat these bounds while every B
class remains present and all original complete cross-class edges remain.
Therefore there is no reason to launch a multiplicity ILP for this class.

The newly read paper by Isham, Lakhotia, Monroe and Petrini,
[arXiv:2608.27253v2](https://arxiv.org/html/2608.27253v2), sections 7.1–7.8,
describes polarity products and recalls replication of the absolute set.
Its cited new degree-18 diameter-3 record is outside the current Delta<=12
scope. The paper's full proofs were not independently verified here; the
bound in this note uses only the explicitly checked finite partition.

## Boundaries and Non-Claims

Deleting an entire B class removes one of the degree constraints used in
the sum. Replacing complete cross-class connections by sparser connections
also changes the premise. Such modifications require separate distance
analysis and are not excluded. Arbitrary graphs of these orders and degrees
are not excluded. No new lower bound, formal Lean proof or external review
has been produced by this note.

## Open Risks

There is no unresolved step in the stated counting argument. Whether an
altered connection rule can retain all diameter-3 paths while exceeding a
public order remains a construction problem outside this complete
replication class. No such search was launched in this task.


## Independent paper check

The math agent independently checked the counting identity, degree inequality, sharpness construction and exclusions from scope. No source BFS or second partition computation was requested. This checks the stated argument, not its literature originality.
