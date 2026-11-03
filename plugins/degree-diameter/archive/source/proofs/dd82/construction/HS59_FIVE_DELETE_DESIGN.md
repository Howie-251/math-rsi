# HS59 with exactly five deleted old edges

Date: 2026-10-11. **Analytic exclusion of the entire stated construction
family.** The proposed two-isolate slot argument is correct. This note gives
a self-contained proof; no SAT, enumeration, or new seed was needed.

Let Q be a Hoffman–Singleton graph on 50 old vertices. Delete exactly five
old edges, add nine new vertices, and add no old–old edges. Suppose the
resulting graph has maximum degree eight and diameter at most two. It must
be 8-regular: a vertex of degree at most seven reaches at most 57 vertices
in two steps.

Let D be the deleted graph, r_x=d_D(x), B_x the new neighbors of old vertex x,
and H the graph induced by the nine new vertices. Then

    |B_x|=1+r_x,     sum_x r_x=10,
    sum_x |B_x|=60,  |E(H)|=(72−60)/2=6.             (1)

Every pair of new vertices in different components of H must be covered
through a common old neighbor. The total number of old-mediated pair slots,
counting multiplicity, satisfies

    sum_x binom(1+r_x,2)
      =10+sum_x binom(r_x,2)
      ≤10+binom(5,2)=20.                            (2)

The last sum counts pairs of deleted edges sharing an endpoint, so each of
the ten pairs of deleted edges contributes at most one.

## 1. H has three components, of sizes 1+1+7 or 1+2+6

A graph on nine vertices with six edges has at least three components.
Four or more components give at least 21 cross-component pairs: the minimum
for four components is attained at sizes 6,1,1,1 and equals
binom(9,2)−binom(6,2)=21; splitting components increases the count.
This contradicts (2), so H has exactly three components.

Write their positive sizes as a≤b≤c, a+b+c=9. If a≥2, the smallest possible
cross-component count is at sizes 2,2,5 and equals 24. Thus a=1. If b≥3,
the minimum is at sizes 1,3,5 and equals 23. Hence the only possibilities
with at most 20 cross-component pairs are

    1+1+7, with 15 cross pairs;
    1+2+6, with 20 cross pairs.

Since the component count is three and the total edge count is six, each
component is a tree, although only their separation is used below.

The 1+2+6 case is impossible. All 20 slots in (2) must cover its 20 distinct
cross pairs, forcing equality in (2). Thus all five deleted edges are
pairwise intersecting. Since Q is triangle-free, they form a five-edge star:
a pairwise-intersecting family of edges without a triangle has a common
endpoint. At the star center, B_x has size six. Among these six labels,
at least two belong to the same one of the three components of H. Their
pair consumes an old-mediated slot that is not a cross pair. This contradicts
the required equality, under which every slot must cover a distinct cross
pair.

Therefore H has two isolated vertices z,w and a seven-vertex component.

## 2. Two isolated vertices require too much deleted degree

Let

    S={x : z,w∈B_x},       s=|S|,
    R_0=sum_{x : z,w∉B_x} r_x,
    a_x=|B_x∩{z,w}|∈{0,1,2}.

The pair z,w must have a common old neighbor, so s≥1. From each isolated
new vertex all eight other new vertices must be reached through old
intermediates. At an old vertex x, each incident isolate has exactly r_x
other new neighbors available. Thus the total number of directed
isolate-to-new-vertex slots is

    T=sum_x a_x r_x.

The sixteen distinct directed destinations must all occur. In addition,
z→w appears once for each x∈S, and w→z does likewise. These two destinations
therefore create at least 2(s−1) repetitions beyond the necessary sixteen:

    T ≥16+2(s−1)=14+2s.                            (3)

This is a count of actual length-two paths in the same graph, with their
forced multiplicities; other repetitions can only increase the lower bound.
On the other hand, (1) gives the exact decomposition

    T=10−R_0+sum_{x∈S}r_x.                         (4)

Combining (3) and (4) yields

    sum_{x∈S}(r_x−2) ≥4+R_0 ≥4.                    (5)

## 3. A five-edge HS subgraph has positive excess at most three

Q has girth five. Hence D, with only five edges, is either a forest or a
five-cycle together with isolated vertices. In the cycle case all positive
degrees are two, so

    sum_x max(r_x−2,0)=0.

For a nontrivial tree component with e edges and L leaves, the degree-sum
identity gives

    sum_x max(r_x−2,0)=L−2.

If e=1 this is zero. If e≥2, at most e vertices are leaves, so the sum is
at most e−2. Summing over the components of a forest with five edges gives

    sum_x max(r_x−2,0) ≤3.                         (6)

Indeed, if any component has at least three edges, subtracting at least two
from its edge count and using the total of five gives this bound; otherwise
every component contributes zero.

But for every subset S,

    sum_{x∈S}(r_x−2) ≤ sum_x max(r_x−2,0) ≤3,

contradicting (5). This excludes the remaining 1+1+7 case and finishes the
proof.

## Scope

The result covers every embedding of five deleted HS edges with nine added
vertices and no added old–old edges. No assumption about HS edge orbits,
attachment symmetry, or a fixed auxiliary graph is used. The argument does
not exclude arbitrary 59-vertex graphs and does not change the global DD82
bound or Lean status.

Combined with the existing exclusions for zero through four deletions, a
deletion-only HS order-59 construction would have to delete at least six old
edges. No further deletion count was analyzed in this bounded subtask.

## External construction discussion C5

The final bounded C5 discussion read this proof and accepted its substantive implications. Raw response: `reviews/dd82/20261011_C5_hs59_cayley.json`; requested and CLI-selected model gemini-3.8-flash-high/high, using the existing Antigravity thread. Root also checked the argument and exact evidence boundaries. This is provisional corroboration, not Lean or independent backend attestation.

The response's concluding description of all results as pure mathematics is not adopted: the order-60 Cayley exclusion remains computer-assisted, depending on the saved quotient screen and A5 enumeration. The A5 source was inspected locally; C5 listed the proof notes and A5 result JSON as its actual reads.
