# HS59 with one deleted old edge: small design and obstruction

Date: 2026-10-11. Scope: order 59 constructions from a Hoffman–Singleton graph
by deleting exactly one old edge and adding nine new vertices. No old edges
are added. This follows the active construction-first Goal and applies the
project-local `formula-derivation` workflow.

## Target

Solve the simultaneous old adjacency, attachment, and auxiliary-graph design,
without imposing a fixed auxiliary controller. Produce an actual expanded
seed and either a graph or a precise obstruction.

## Status

**COHERENT AS STATED. The entire one-old-edge-deletion family at order 59 is
analytically impossible.** A separate, joint H/B SAT input for the explicit
HS edge (0,1) is independently LRAT-checked UNSAT. Neither statement excludes
arbitrary order-59 graphs.

## Invariant object and assumptions

Let Q be the 50-vertex, 7-regular Hoffman–Singleton graph. Its adjacent pairs
have no common neighbors, and each nonadjacent pair has exactly one common
neighbor. Delete an arbitrary edge uv and call the retained adjacency A'.
Let B be the 50-by-9 old–new incidence matrix and H the simple graph induced
on the nine new vertices. The intended full graph has maximum degree 8 and
diameter at most two.

Every target on 59 vertices is 8-regular: a degree-at-most-7 vertex has a
radius-two ball of size at most 1+7+7·7=57. Thus rows u,v of B have size two,
all other rows have size one, and

    sum B = 52,                 |E(H)| = (9·8−52)/2 = 10.

The new vertex a has old attachment capacity 8−d_H(a).

## Notation and derivation strategy

Write A=B_u and C=B_v for the two endpoint port sets. Write U=N_Q(u)\{v} and
V=N_Q(v)\{u}. The sets U and V are disjoint and each has six elements.

The organizing object is the actual expanded graph with block adjacency
[[A',B],[B^T,H]]. Its exact coverage obligations are

    A'+(A')²+BB^T > 0         off diagonal;
    B+A'B+BH > 0             at every entry;
    H+H²+B^TB > 0            off diagonal.

These use the same B and H. There is no approximation or relaxed matrix
substitution in the argument or generator.

Derivation map:

1. Old–old coverage forces A∩C nonempty and sends U into C, V into A.
2. New–new coverage leaves at most two pairs outside the two-ball relation
   inside H.
3. A nine-vertex graph with ten edges and at most two such pairs has a
   universal vertex.
4. The resulting auxiliary star plus two edges cannot provide the old–new
   paths from u.

## Main derivation

### 1. The thirteen old repair obligations

Deleting uv removes the only old path of length at most two for exactly
these thirteen pairs:

    {u,v};  {v,x} for x∈U;  {u,y} for y∈V.

The unique-common-neighbor property verifies this directly. Each requires a
shared new neighbor. Therefore

    A∩C ≠ ∅,       B_x ⊆ C for x∈U,       B_y ⊆ A for y∈V.

The subset statements concern singleton rows. In particular |A∪C|≤3.

### 2. H misses at most two new–new pairs

Only u and v have more than one new neighbor. Consequently B^TB can supply
new–new coverage only for the two unordered pairs represented by A and C.
They may coincide. Every other new pair must have an H edge or a common
H neighbor. This does **not** assume H itself has diameter two.

### 3. Small auxiliary-graph lemma

**Lemma.** If a simple graph H has nine vertices, ten edges, and at most two
unordered vertex pairs of distance greater than two (including disconnected
pairs), then H has a universal vertex.

**Proof.** H is connected: a disconnected graph on nine vertices has at least
8 pairs between different components, all at infinite distance. Put
W(H)=∑_a binom(d_H(a),2). Counting available edge and two-step witnesses gives

    36 ≤ 10 + W(H) + 2,              W(H) ≥ 24.

If H had minimum degree at least two, its degree sum 20 would leave just two
increments above the all-degree-two sequence. The largest possible W is
binom(4,2)+8·binom(2,2)=14, contradiction. Hence H has a leaf p.

If h is its unique neighbor, p is at distance greater than two from exactly
8−d_H(h) vertices. Thus d_H(h)≥6. There can be at most one vertex of degree at
least six: the union of the edges incident to two such vertices has at least
6+6−1=11 edges. Every leaf therefore has the same neighbor h.

Write d=d_H(h) and let L be the number of leaves. Every other vertex besides
h and the leaves has degree at least two, so

    20 ≥ d + L + 2(8−L),             L ≥ d−4.

Every leaf has a bad pair with each of the 8−d nonneighbors of h. Such a
nonneighbor is not a leaf, since all leaves are adjacent to h; these are
L(8−d) distinct pairs. If d=6 there are at least 2·2=4; if d=7 there are at
least 3·1=3. Both exceed two. Therefore d=8. ∎

This lemma was independently derived by the construction-literature-actions
agent during the bounded experiment. Its proof does not enumerate H graphs.

### 4. Final old–new coverage contradiction

Apply the lemma. H consists of a universal vertex h, its eight star edges,
and exactly two additional edges between the eight leaves. The degree
equation forces the h-column of B to be empty, so h∉A∪C.

Consider paths of length at most two from old vertex u to a new vertex:

- A supplies direct neighbors.
- The six retained old neighbors of u all have their singleton port in C.
- A new intermediate vertex belongs to A, so it supplies a vertex in N_H(A).

Thus every reachable new vertex is in A∪C∪N_H(A). The union A∪C contains at
most three leaves. N_H(A) can add h and at most two other leaves, because H
has only two edges between leaves. At most six of the nine new vertices can
therefore be reached from u in two steps. This contradicts diameter two. ∎

This argument applies to **every** choice of deleted HS edge uv, without an
edge-transitivity assumption or enumeration of embeddings.

## Actual complete object and bounded joint SAT experiment

Source: [hs59_one_delete.py](../../../computations/dd82/construction/hs59_one_delete.py).
All artifacts: [hs59_one_delete/](../../../computations/dd82/construction/hs59_one_delete/).
The calculation ran while the small-graph proof was being completed; it was
not repeated after the analytic contradiction was found.

The saved complete seed deletes edge (0,1), takes auxiliary edges

    {a,8} for 0≤a≤7, together with {3,4},{5,6},

and fixes B_0={0,1}, B_1={0,2}. All six vertices in U attach to 2, all six in V
to 1. The other 36 old vertices, in increasing label order, fill the remaining
capacities: five occurrences of label 0, six occurrences of each label
3,4,5,6, and seven of label 7. This defines every edge without an unresolved
completion step.

The independent checker reads the expanded edge list only, rebuilds adjacency,
and runs BFS from every vertex. It found:

| Object | Vertices | Edges | Degrees | Diameter | Bad pairs |
| --- | ---: | ---: | --- | ---: | ---: |
| Complete seed | 59 | 236 | all 8 | 3 | 82 |

All 82 bad pairs are old–new pairs. The seed satisfies all old–old and new–new
coverage. In particular each of old vertices 0 and 1 fails against new
vertices 53,54,55,56,57, exactly illustrating the endpoint obstruction.
Every bad pair, its distance, and its complete common-neighbor list is saved
in [seed.verification.json](../../../computations/dd82/construction/hs59_one_delete/seed.verification.json).
The full graph and generating ports are in
[seed.json](../../../computations/dd82/construction/hs59_one_delete/seed.json).

### Exact encoding and normalization

The SAT input keeps all 36 possible H edges variable. It imposes the old
row sizes and each new vertex's total degree eight, and redundantly imposes
ten H edges. It enforces the three exact coverage lines above using conjunction
variables and the existing generic exact-counter primitive. No old n62 graph
constraint is imported.

The normalization B_u={0,1}, B_v={0,2} is exhaustive for unequal intersecting
two-element port sets, by permuting the nine new labels. Equal sets are
independently impossible: if A=C, their two columns receive at least 4
incidences from u,v and 12 from U∪V, hence their combined H degree must be zero.
That gives two isolated vertices, contradicting the connectivity consequence
of at most two bad new pairs. Thus this normalization loses no candidate for
the fixed deleted edge.

Since only u,v have multiple ports, the pairs {0,1},{0,2} are already covered
through old vertices; every other new pair is explicitly required to have an
H edge or an H length-two witness. Every old–new entry enumerates its direct
edge, every retained old intermediate, and every possible new intermediate.

| Input/result | Value |
| --- | --- |
| Variables / clauses | 9,156 / 32,386 |
| Solver | existing CaDiCaL with LRAT output |
| Budget | ≤60 CPU seconds, one pinned CPU, ≤4 GiB address space |
| Actual solver CPU / wall | 0.123368 / 0.193024 seconds |
| Result | CHECKED_UNSAT |
| Independent certificate checker | lrat-trim 0.2.0 --no-trim |
| Checker result | exit 20, s VERIFIED |

The checker's reported peak memory was 16 MB. Exact input, variable maps,
command, proof, logs, and results are preserved in the artifact directory.
No checksum or hash was generated.

## Remarks and interpretation

This attempt did solve its smaller component obligation: the auxiliary graph
is forced to be a star plus two extra leaf edges, even though H was originally
free and was not required to have diameter two. The failed seed distinguishes
the actual remaining obstruction: old–old and new–new coverage can coexist,
but old–new coverage at the repaired edge endpoints cannot.

The analytic conclusion is stronger in scope than the saved SAT input: it
covers every deleted edge of an HS copy. The SAT certificate checks the
explicit fixed-label joint model and independently agrees with that result.

## Boundaries and non-claims

No valid 59-vertex graph was found. This excludes only deletion of exactly
one old HS edge with nine new vertices and no added old–old edges. It does
not exclude two or more deleted old edges, a different base graph, or arbitrary
order-59 graphs. It does not change the global interval 57≤N(8,2)≤61 and is
not a Lean theorem. No n62, n63, Brown, or A5 search was started.

## Open risks / next design implication

There is no unresolved gap in this finite-family mathematical argument.
A new HS order-59 proposal must change more than one old edge or permit old
edge additions; additional edits change both the released attachment degrees
and the small auxiliary-graph obligation. Do not rerun this same one-edge
family with another auxiliary controller or a relabeled HS edge.


## Cross-model review receipt

Root read the full argument and Gemini C2 subsequently found no mathematical gap; see [saved raw response](../../../reviews/dd82/20261011_C2_hs59_cyclic_constructions.json). Requested and CLI-selected model was gemini-3.8-flash-high/high, without independent backend attestation. This updates the earlier not-yet-reviewed snapshot; it is not a Lean certificate.
