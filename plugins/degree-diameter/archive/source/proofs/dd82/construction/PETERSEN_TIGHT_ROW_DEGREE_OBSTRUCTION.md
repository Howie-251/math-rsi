# Tight external rows constrain the internal cubic graphs jointly

Date: 2026-10-12. The previous tiny LRAT proof led to a direct, useful
external-to-internal constraint: a row whose five fixed external slots
reach exactly four targets forbids six internal edges. Combining these
constraints gives a **three-row degree contradiction** for the saved
186-bad-pair skeleton, without assuming internal girth.

One authorized matching repair then maintained the previous external
condition \(F=0\) and removed every vertex-level allowed-neighbor deficit.
It produced a new complete 60-vertex eight-regular graph with 286 bad
pairs. One new all-six-internal completion input was checked UNSAT.
The new skeleton has a different explicit degree obstruction: four
vertices force four internal edges at vertex 50. No further repair or
solver was launched.

## From actual coverage clauses to a tight-row lemma

All 64 original binary coverage clauses referenced by the prior 87-step
proof were translated back to their vertex pair and the two possible
internal edges. The
[translation](../../../computations/dd82/construction/petersen_tight_row_obstruction_run/proof_binary_clauses.json)
records the original clause ID, the uncovered cross-fiber pair, the
variable IDs, and both actual internal edges. Each clause has the meaning

\[
e_{u,M_{ji}(v)}\lor e_{M_{ij}(u),v}.
\]

This is a translation of the saved proof references, not a minimal-core
claim. The simpler argument below uses complete coverage of three actual
rows; it is not asserted to use only those 64 proof-referenced clauses.

Let \(u\in F_i\) and let

\[
B_{ij}(u)=\{M_{ij}(u)\}\cup
\{M_{kj}(M_{ik}(u)):k\notin\{i,j\}\}
\]

be the set of targets reached by the direct matching and four other-fiber
two-edge paths. Suppose \(|B_{ij}(u)|=4\). These five fixed slots already
contain one repetition. The two internal cubic graphs contribute exactly
six more route slots. To cover all ten targets, those six slots must be
distinct and must all lie outside \(B_{ij}(u)\). Therefore:

\[
\begin{split}
M_{ij}(w)\in B_{ij}(u),\ w\ne u
&\Longrightarrow uw\notin E(P_i),\\
v\in B_{ij}(u),\ v\ne M_{ij}(u)
&\Longrightarrow M_{ij}(u)v\notin E(P_j).
\end{split}
\]

Each such row forbids three source-internal edges and three
target-internal edges. This conclusion uses only internal degree three;
it does not require Petersen structure, triangle-freeness, or girth five.

For each fiber, remove from \(K_{10}\) every edge forbidden by any tight
row, including symmetry of the internal edges. Write the resulting
allowed graph as \(H_i\). Every successful internal graph must be a
spanning cubic subgraph of \(H_i\). In particular define

\[
K=\sum_{i=0}^5\sum_{u\in F_i}\max(0,3-d_{H_i}(u));
\qquad K=0
\]

as a necessary condition. This condition connects all fifteen matching
interfaces to the same six internal graphs; it is stronger than checking
the fixed route row cardinalities separately.

## Three real rows already exclude the preceding external skeleton

In the
[186-pair graph](../../../computations/dd82/construction/petersen_fixed_route_repair_run/candidate.json),
consider these three tight rows:

| Row | Fixed targets | Forbidden neighbors of vertex 9 |
|---|---|---|
| \(9\to F_2\) | \(21,23,27,28\) | \(1,5,8\) |
| \(9\to F_5\) | \(52,56,57,59\) | \(0,1,6\) |
| \(57\to F_0\) | \(2,3,4,9\) | \(2,3,4\) |

Their union forbids the eight neighbors

\[
0,1,2,3,4,5,6,8
\]

of vertex 9, leaving only vertex 7 available inside \(F_0\). This
contradicts internal degree three. Every direct and two-edge path behind
the table is recorded in the
[three-row witness](../../../computations/dd82/construction/petersen_tight_row_obstruction_run/three_row_witness.json).

For this actual skeleton, 130 tight rows forbid 213 of the 270 possible
internal edges. The allowed-degree distribution is

\[
d_H=0:4,\quad1:18,\quad2:21,\quad3:14,\quad4:3.
\]

There are 43 vertices with fewer than three allowed neighbors and
\(K=69\). Thus the earlier fixed-external completion is analytically
impossible even for arbitrary cubic internal graphs. This stronger
conclusion comes from the new direct argument, not from deleting the
girth assumptions in the previous SAT certificate.

## One actual repair, with the old conflict removed

Starting from that exact external skeleton, a switch swaps two images of
one matching permutation and updates its inverse. The new episode used
\(F=0\) as a hard invariant and minimized \(K\). It accepted only strict
improvements or equal-score moves; it had a ten-CPU-second limit, a
9.8-second internal stop and a cap of 2,000 stored states. There was no
random restart and no graph-distance annealing.

The endpoint has **\(F=0\) and \(K=0\)**. Its path contains 40 switches:
35 strict improvements and five neutral moves. The episode checked 10,943
switches, expanded 42 states and stored 61 states. The launcher separately
reconstructed the complete edge set at every path step, confirmed the
recorded switch, and recomputed both \(F\) and \(K\).

The new skeleton has 36 tight rows and 124 forbidden internal edges. Its
allowed-degree distribution is

\[
3:14,\quad4:13,\quad5:14,\quad6:11,\quad7:3,\quad8:4,\quad9:1.
\]

The old three-row contradiction is gone, as are all 43 old vertex-level
degree failures. The changed interfaces are

\[
01,02,03,04,05,12,13,14,15,23,24,25,34.
\]

Putting back the original six internal Petersen graphs gives the actual
[new candidate](../../../computations/dd82/construction/petersen_tight_row_repair_run/candidate.json):
60 vertices, 240 edges, every degree eight. Independent BFS found diameter
three and **286 bad pairs**; the recorded route energy is 336. Its complete
edge list, exact edits, all matching permutations and every bad pair are
saved. It is a failed graph, not a target or a bad-pair improvement.

## The permitted new completion check and its concrete failure

Only after this actual new skeleton had removed the old explicit
obstruction was a new completion CNF generated. It uses the same exact
candidate-preserving encoding explained in
[the preceding completion report](PETERSEN_FIXED_ROUTE_REPAIR_AND_INTERNAL_COMPLETION.md):
all 270 internal edge variables free, exact internal degree three, no
internal triangle or four-cycle, and the precise binary clause for every
cross pair not already covered externally. There are no fixed internal
edges or symmetry-breaking clauses. The new totals are

\[
9720+720+3780+768=14988\text{ clauses}.
\]

Inserting the actual seed's internal graphs violates exactly 286 binary
clauses, agreeing as a set of vertex pairs with the saved independent BFS.
The sole new CaDiCaL call returned UNSAT. Its 1,631-byte LRAT proof passed
one independent `lrat-trim --no-trim` check on this exact new CNF.

A subsequent small read-only inspection of \(H_5\) explains the failure
without another search. These four vertices each have exactly the three
displayed allowed internal neighbors:

\[
\begin{array}{c|c}
51&\{50,52,56\}\\
53&\{50,52,54\}\\
54&\{50,53,57\}\\
58&\{50,55,56\}
\end{array}
\]

Degree three forces every edge in each displayed row, including

\[
50\!\sim\!51,\quad50\!\sim\!53,\quad50\!\sim\!54,\quad50\!\sim\!58.
\]

Vertex 50 would have internal degree at least four, a contradiction.
There is also a forced triangle \(50,53,54\), but the degree contradiction
already excludes arbitrary cubic completion of this particular skeleton.
The actual allowed sets and forced edges are saved in
[the failure diagnostic](../../../computations/dd82/construction/petersen_tight_row_repair_run/forced_edges_diagnostic.json).

Thus \(d_{H_i}(u)\ge3\) for every vertex is not sufficient: the allowed
graphs must jointly admit their cubic internal choices. The four forced
incidences above are the specific remaining failure, not an additional
claim that the entire six-Petersen family is impossible. No second repair
episode or second new completion input was run.

## Reproducibility and actual resources

- [Proof translation and three-row extractor](../../../computations/dd82/construction/petersen_tight_row_obstruction.py),
  [all tight-row constraints](../../../computations/dd82/construction/petersen_tight_row_obstruction_run/all_tight_row_constraints.json),
  [translation resources](../../../computations/dd82/construction/petersen_tight_row_obstruction_run/resources.json).
- [Dedicated repair source](../../../computations/dd82/construction/petersen_tight_row_repair.cpp),
  [launcher](../../../computations/dd82/construction/petersen_tight_row_repair_run.py),
  [exact path](../../../computations/dd82/construction/petersen_tight_row_repair_run/search.json),
  [resource record](../../../computations/dd82/construction/petersen_tight_row_repair_run/resources.json).
- [Complete new edge list](../../../computations/dd82/construction/petersen_tight_row_repair_run/candidate.edges),
  [independent BFS and every bad pair](../../../computations/dd82/construction/petersen_tight_row_repair_run/candidate.verification.json),
  [current allowed internal graphs and their causes](../../../computations/dd82/construction/petersen_tight_row_repair_run/tight_row_constraints.json),
  [old witness after repair](../../../computations/dd82/construction/petersen_tight_row_repair_run/old_witness_after_repair.json).
- [New completion encoder](../../../computations/dd82/construction/petersen_tight_row_internal_completion.py),
  [encoding map](../../../computations/dd82/construction/petersen_tight_row_internal_completion_run/encoding.json),
  [CNF](../../../computations/dd82/construction/petersen_tight_row_internal_completion_run/input.cnf),
  [result](../../../computations/dd82/construction/petersen_tight_row_internal_completion_run/result.json),
  [LRAT](../../../computations/dd82/construction/petersen_tight_row_internal_completion_run/proof.lrat),
  [independent checker log](../../../computations/dd82/construction/petersen_tight_row_internal_completion_run/certificate_check.log).

| Operation | CPU seconds | Wall seconds |
|---|---:|---:|
| Original-proof translation and actual three-row witness | 0.025941408 | 0.067905098 |
| One matching repair child | 0.030486 | 0.033222266 |
| Independent BFS child | 0.031566 | Included below |
| Repair launcher and path reconstruction | 0.084048765 | 0.150342155 including children |
| New CNF preparation | 0.038042098 | 0.039386552 |
| Sole new SAT call | 0.010246 | 0.050498288 |
| Sole new independent LRAT check | 0.003723 | 0.005641010 |

The SAT call had the authorized 180-CPU-second, one-CPU, 8-GiB memory,
768-MiB proof limits. All processes are finished. No shared wiki or global
checkpoint was changed.
