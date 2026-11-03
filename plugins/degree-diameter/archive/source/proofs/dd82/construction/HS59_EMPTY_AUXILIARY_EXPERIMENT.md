# HS59 with empty auxiliary graph: one joint deletion/attachment experiment

Date: 2026-10-11. **Result: UNKNOWN after the single authorized bounded SAT
run.** No valid target graph or family exclusion was obtained. The full
expanded seed, all bad-pair witnesses, exact CNF, variable maps, solver log,
and partial proof output are preserved. The experiment was not repeated.

## Exact construction family

The old vertices form the explicit 50-vertex Hoffman–Singleton graph Q before
deletions. All 175 original old edges have Boolean retained-edge variables
R_uv. All 450 possible old–new edges have variables B_xa, where x∈{0,...,49}
and a∈{0,...,8}. The nine new vertices have no mutual edges: H is empty.
No old–old edge outside Q may be added.

Every vertex has degree eight. Thus each new column of B has size eight,
there are 72 old–new edges, and the retained old graph has
(50·8−72)/2=164 edges. Exactly eleven of the original 175 edges are deleted.
All deletion positions and all attachment sets are variables in this one
input. The seed's matching deletion pattern is only its generating parameter;
the SAT formula covers every deletion pattern in the stated family.

The sole symmetry normalization is B_00=true. Each old vertex must have at
least one new neighbor, since it has at most seven old neighbors, and the
nine new labels are completely symmetric. Therefore a permutation of new
labels always supplies this normalization. No symmetry of the old HS graph
is assumed or used.

## Actual complete seed and independent BFS

The seed builder uses deterministic random seed 20261011 and tries at most
100 greedily generated eleven-edge matchings. It accepts the first one whose
22 deleted-edge endpoints form a total dominating set in the retained old
graph. The second attempt succeeded, with deleted edges

    (1,36), (2,47), (3,48), (8,34), (10,32), (12,45),
    (15,25), (16,37), (19,35), (23,40), (26,29).

An integral bipartite degree flow assigns each endpoint two distinct new
neighbors, each other old vertex one, and each new vertex eight old neighbors.
A new-label permutation makes B_00 true. This gives a complete graph with no
unresolved attachment step.

The independent checker reads the saved expanded edge list, rebuilds all
adjacency, and runs BFS from each of the 59 vertices. Its result is:

| n | Edges | Degrees | Diameter | Bad old–old pairs | Bad old–new pairs | Bad new–new pairs |
| ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 59 | 236 | all 8 | 3 | 104 | 113 | 27 |

All **244** bad pairs, their distances, and their complete common-neighbor
lists are saved in
[seed.verification.json](../../../computations/dd82/construction/hs59_empty_auxiliary/seed.verification.json).
The complete expanded edges and ports are in
[seed.json](../../../computations/dd82/construction/hs59_empty_auxiliary/seed.json).
This is a failed seed, not a lower-bound witness. A matching deletion alone
has too few shared-old pair slots to solve the H-empty family; the experiment
uses it only to produce and check a complete degree-correct initial object.

## Full exact coverage encoding

Each old vertex has

    sum_{y∈N_Q(x)}R_xy + sum_a B_xa = 8,

and each new column satisfies sum_x B_xa=8. The input also explicitly imposes
sum_{uv∈E(Q)}(1−R_uv)=11, consistent with those degree equations.

Conjunction variables are defined in both directions, using the existing
generic CNF helper. The existing generic exact counter is reused without
any old n62 graph constraints.

Every one of the 1,711 unordered full-graph pairs is covered:

- For an adjacent old pair x,y, the clause is R_xy or a shared new neighbor.
  HS adjacent vertices have no common old neighbor.
- For a nonadjacent old pair x,y with unique HS common neighbor w, the clause
  is (R_xw and R_yw) or a shared new neighbor. These are all possible old
  paths and all possible new intermediates.
- For an old–new pair x,a, the clause is B_xa or, for some y∈N_Q(x),
  (R_xy and B_ya). There is no new intermediate because H is empty.
- For a new–new pair a,b, the clause requires some x with B_xa and B_xb.

These are the exact three block-matrix coverage obligations for the same
retained old graph and the same B. The source records 1,225 old–old pairs,
450 old–new pairs, and 36 new–new pairs.

### Additional necessary clauses

Each old vertex has at least one retained old neighbor. This follows directly
for H empty: otherwise its degree-eight neighborhood consists of eight new
vertices, and the ninth new vertex has no path of length at most two from it.
Thus the maximum deleted degree is at most six. This clause is also consistent
with the previously proved sparse-auxiliary obstruction.

Let E_y mean that y is incident to at least one deleted edge. It is defined
exactly by E_y iff OR_{z∈N_Q(y)} NOT R_yz. Every old vertex x is required to
have a retained old neighbor y with E_y=true. This is necessary: if every
retained neighbor were an ordinary singleton-port vertex, then writing
r_x for x's deleted degree, x could reach at most

    (1+r_x)+(7−r_x)=8

new vertices through its direct and old-intermediate routes. All nine are
required. This total-domination condition is a redundant consequence of the
full coverage constraints, included to expose the derived structure promptly.

The mathematical candidate-preservation argument, including this condition,
the minimum retained degree, every coverage clause, and the normalization,
was independently checked by the cyclic-lift agent before the result was
interpreted.

The same agent subsequently read the actual experiment source and the
generic counter implementation. The signed literals −R are counted as
deleted edges, the E_y clauses define the stated equivalence in both
directions, and the four coverage classes and additional clauses match the
mathematical model. This was a source review, with no code changes or new
solver/checker run; the observed result remains UNKNOWN.

## One bounded run and observed result

[Source](../../../computations/dd82/construction/hs59_empty_auxiliary.py)
and [artifact directory](../../../computations/dd82/construction/hs59_empty_auxiliary/)
are separate from the fixed-deletion HS experiments.

| Field | Observed value |
| --- | --- |
| Variables / clauses | 29,210 / 97,179 |
| Solver | existing CaDiCaL, LRAT output enabled |
| Limits | one pinned CPU; 30 CPU seconds; 4 GiB address space; 128 MiB proof output |
| Actual solver CPU / wall | 29.660543 / 30.144580 seconds |
| Reported maximum resident memory | 42.88 MB |
| Solver status / exit | UNKNOWN / 0 |
| Proof-output bytes | 86,089,104 |
| Solver attempts | exactly one |

The solver stopped at its wall-time limit before using 30 CPU seconds. The
saved `proof.lrat` is **partial output from an UNKNOWN run**, not a checked
UNSAT certificate. It was not passed off as a completed proof, and no LRAT
UNSAT check was warranted. No satisfying assignment was returned, so there
is no solver candidate to expand.

The script would expand any SAT assignment into a full edge list and invoke
the independent BFS checker, or run the existing LRAT checker on a completed
UNSAT proof. Neither branch was triggered in this run. `result.json` records
the actual command, limits, seed check, and UNKNOWN status. The script refuses
to repeat the same experiment when a solver log or result already exists.

## Scope and stopping point

This is a simultaneous test of all eleven-edge deletion patterns of the
fixed explicit HS graph, with empty H and unrestricted old–new attachments
subject to the exact graph conditions. It is materially broader than a
fixed-deletion or fixed-port input. It addresses one of the seventeen
remaining auxiliary representatives from the sparse-auxiliary analysis.

UNKNOWN does not exclude this family and does not supply a graph. No budget
extension, unchanged rerun, Lean task, or solver run for another auxiliary
graph was started. The partial proof and all inputs remain available for
inspection; no solver checkpoint or resumable search state is claimed.
