# Internal-Petersen reassembly and an exact four-missing-target obstruction

Date: 2026-10-12. One complete screen of all **30,240 labeled Petersen
graphs** in fiber 0 found no way to cover both fixed boundary fibers 2 and
3 of the saved 97-bad-pair construction. The smallest boundary deficit is
four, attained only by the original internal graph. The planned later
stages were stopped at this empty domain. The best genuinely changed full
graph has **111 bad pairs**, and its complete edge list and independent BFS
are saved. No SAT call was made.

A direct route witness, extracted after the screen, gives a stronger and
shorter explanation: with these external matchings and the saved internal
graph in fiber 2, vertex 0 has four missing targets there but only three
internal neighbors available to reach them. This obstruction holds even if
the other five internal cubic graphs are allowed to change.

## Choice of a coherent new domain

Changing internal Petersen graphs while retaining matching edges changes
the local seven-route matrices coherently across all five interfaces at
each changed fiber. It is therefore different from the completed binary
palette, which preserves all fifteen original seven-route matrices.
It also differs from the earlier fixed-internal-Petersen matching-switch
searches. The source graph here is the actual
[97-bad-pair four-fiber construction](PETERSEN_FOUR_FIBER_REASSEMBLY.md),
not the original twenty-bad-pair graph.

Two simpler proposals were rejected before being run:

1. In the original twenty-pair seed, all four intermediate 4-to-5
   matching routes coincide. For each source, these four slots reach only
   one target. The direct route and two internal triples can reach at most
   seven additional targets, regardless of the internal graphs. Thus
   internal-only changes leave at least twenty bad pairs in block 45.
2. In the 97-pair source, changing only internal graphs 4 and 5 cannot
   alter its existing bad blocks 01,02,03,12,13. That two-fiber-only proposal
   was never executed and is not counted as a failed search run.

The authorized revised domain fixed all fifteen external matching
interfaces and the internal graphs \(P_2,P_3\), while allowing
\(P_0,P_1,P_4,P_5\) to change. The first stage screens \(P_0\) and then
\(P_1\) for complete coverage to both boundary fibers 2 and 3. Only if both
domains survive does the construction proceed to the coupled 4--5 stage.

For that planned stage, let \(M=M_{45}\) and

\[
S=P_4+MP_5M^T.
\]

The two summands of the actual source are edge-disjoint Petersen graphs.
Choose a Petersen graph \(P'_4\subseteq S\) such that \(S-P'_4\) is also
Petersen, and set \(P'_5=M^T(S-P'_4)M\). Then

\[
P'_4M+MP'_5=P_4M+MP_5,
\]

so the already exact 4--5 route count is preserved. This is a concrete
coupled graph decomposition. It was **not run**, because the preceding
fiber-0 boundary domain was empty; the recorded zero decomposition count
means that the stage was not reached, not that it was enumerated.

## Complete labeled-Petersen domain and the boundary test

The standard Petersen graph uses an outer pentagon 0,...,4, spokes
\(i\sim i+5\), and inner star edges. Its automorphism group is the action
of \(S_5\) on two-element subsets. It is vertex-transitive; the stabilizer
of vertex 0 permutes its three neighbors 1,4,5 arbitrarily, and its residual
pointwise stabilizer swaps

\[
(2\ 6)(3\ 9)(7\ 8).
\]

Consequently one representative labeling is obtained by requiring
\(p(0)=0\), \(p(1)<p(4)<p(5)\), and \(p(2)<p(6)\). The generator visits
all permutations satisfying these conditions, creates their complete
edge sets, and checks distinctness with an ordered set. It obtains
\(9!/(6\cdot2)=30240\) different labeled Petersen graphs.

For source fiber \(i\) and fixed target fiber \(j\in\{2,3\}\), remove
only the three route slots through the source's internal neighbors.
The remaining direct, target-internal, and four intermediate-fiber routes
are fixed. Pull each uncovered target back through the fixed matching
\(M_{ij}\). Every pulled-back vertex must be an internal neighbor of the
source in \(P_i\). This condition is both necessary and sufficient for
coverage of that boundary block, since the only omitted routes are exactly
those through \(P_i\).

All 30,240 graphs were screened for \(i=0\). None passed both boundary
blocks; the minimum number of missing boundary pairs was four. The full
histogram is saved in
[boundary_domains.jsonl](../../../computations/dd82/construction/petersen_internal_reassembly_run/boundary_domains.jsonl).
The run stopped immediately at this complete empty domain. No fiber-1
screen, coupled 4--5 decomposition, or joint assembly was started.

## A direct obstruction in one actual boundary row

Consider old source vertex 0 and target fiber \(F_2=\{20,\ldots,29\}\).
Keep the external matching edges of the 97-pair source and its \(P_2\).
The eight routes not using an internal edge at source 0 are:

| Route type | Target label(s) |
|---|---|
| Direct matching | 25 |
| Internal edge at the target | 20,27,28 |
| Through fibers 1,3,4,5 | 28,26,21,25 |

They cover exactly \(\{20,21,25,26,27,28\}\). Therefore four targets,

\[
22,23,24,29,
\]

remain uncovered. They pull back through \(M_{02}\) to the four distinct
required source neighbors \(5,2,4,1\), respectively. A cubic internal graph
at vertex 0 can provide only three such neighbors. At least one target
therefore remains at distance greater than two, whatever the other
internal graphs are. This argument does not need the Petersen property,
only internal degree three.

For additional actual failure detail, combining both boundary fibers forces
the required neighbor sets \(\{1,2,4,5,7\}\) at vertex 0 and
\(\{0,2,3,6,8\}\) at vertex 1. These five-neighbor demands are consistent
with, but unnecessary for, the shorter single-block contradiction above.
The complete route labels and pullbacks are saved in
[required_neighbor_obstruction.json](../../../computations/dd82/construction/petersen_internal_reassembly_run/required_neighbor_obstruction.json).

Thus any future internal-only reconstruction retaining these external
matchings must also change \(P_2\). Alternatively it must change matching
edges contributing to the displayed routes. The present result does not
exclude a simultaneous change of all six internal graphs or arbitrary
six-Petersen constructions.

## Complete failed graphs and exact search scope

During the fiber-0 screen the program also evaluated the full expanded
60-vertex graph for every internal Petersen choice, with the other five
internal graphs still at their source values. The best graph is the
unchanged source, with 97 bad pairs and energy 118. The best *distinct*
replacement has 111 bad pairs and energy 132. It changes four internal
edges in fiber 0:

\[
\begin{aligned}
\text{remove }&12,16,57,58,\\
\text{add }&17,18,25,56.
\end{aligned}
\]

Here each two-digit expression denotes its two single-digit endpoints,
all within fiber 0. Every external matching edge is unchanged. The new
graph is simple, eight-regular, has 240 edges, and has diameter three.
No fiber omission produces HS50. Its bad-pair counts by affected block are

\[
(01,02,03,04,05)=(9,8,8,7,24).
\]

The unaffected bad blocks are \(12,13,14\), with two each; \(15\), with
nineteen; and \(25,35\), with fifteen each. Blocks 23,24,34,45 remain
fully covered. Every bad pair, distance, common-neighbor set, and every
block's route-count histogram is saved. The graph is a failed candidate,
not a target or an improvement in the original bad-pair objective.

This optimality claim concerns only the complete single-\(P_0\)
replacement screen. It is not an optimization over all four varying
internal graphs. The larger four-internal-graph *target* domain is excluded
by the independent boundary obligation and the explicit row obstruction,
not by a claimed joint enumeration.

## Files and actual resources

- [Enumerator](../../../computations/dd82/construction/petersen_internal_reassembly.cpp)
  and [single-run launcher](../../../computations/dd82/construction/petersen_internal_reassembly_run.py).
- [Search result](../../../computations/dd82/construction/petersen_internal_reassembly_run/search.json),
  [boundary domain](../../../computations/dd82/construction/petersen_internal_reassembly_run/boundary_domains.jsonl),
  [resource and stage record](../../../computations/dd82/construction/petersen_internal_reassembly_run/resources.json).
- [Best distinct full graph](../../../computations/dd82/construction/petersen_internal_reassembly_run/best_new.json),
  [edge list](../../../computations/dd82/construction/petersen_internal_reassembly_run/best_new.edges),
  [full independent BFS](../../../computations/dd82/construction/petersen_internal_reassembly_run/best_new.verification.json),
  [all block diagnostics](../../../computations/dd82/construction/petersen_internal_reassembly_run/best_new.diagnostic.json),
  [exact edits](../../../computations/dd82/construction/petersen_internal_reassembly_run/best_new.edits.json).
- [Read-only obstruction extractor](../../../computations/dd82/construction/petersen_internal_required_neighbors.py).

The single computation used 0.111903 child CPU seconds, including 0.108814
seconds reported internally. Independent BFS used 0.060616 child CPU
seconds, and the parent launcher/diagnostics used 0.010747469 CPU seconds.
Wall time was 0.189840049 seconds. Only two different expanded edge lists
were BFS-checked; files with identical complete edge lists reuse those
results explicitly. The subsequent read-only route witness used
0.000558771 CPU seconds. No SAT call or follow-up enumeration was launched;
all processes have finished.
