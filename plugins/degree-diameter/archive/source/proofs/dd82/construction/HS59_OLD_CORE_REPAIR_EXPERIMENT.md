# HS59 old-core repair and a complete finite attachment experiment

Date: 2026-10-12. **Result:** the seven requested old cores all fail necessary
conditions. A revised old-core rule has 139 passing cores. Applying the
specified four-port completion to all of them produces 141,805 complete
59-vertex, 236-edge, 8-regular graphs; the minimum is **41 bad pairs**, worse
than the source graph's 26. No valid diameter-two graph is obtained.

## Input and labels

The inputs were read directly from
[component.path2.edges](../../../computations/dd82/construction/twin59_neutral_component_run/component.path2.edges)
and
[component.path2.old_core_obstruction.json](../../../computations/dd82/construction/twin59_neutral_component_run/component.path2.old_core_obstruction.json).
The edge file uses compressed labels 0 through 58. This note and all edit
parameters use the original order-60 labels: restore a label v≥41 to v+1,
with original vertex 41 absent.

The 50 old vertices are 0 through 39 and 50 through 59; the nine new vertices
are 40 and 42 through 49. Restoring old edge 50–55 and removing old additions
9–14 and 38–55 recovers the actual HS base Q from the input. Its 175 edges,
degree seven at every vertex, zero common neighbors at adjacent pairs, and
one common neighbor at nonadjacent pairs were checked directly. Its complete
original-label edge list is saved in `hs59_old_core_repair_run/base.json`.

For any proposed old core K, its old vertex x has p_x=8−d_K(x) available
new-neighbor ports. A negative p_x is impossible. If p_x=0, all old vertices
must lie within distance two of x in K: x cannot acquire a new intermediate
vertex. Also

    sum_{y∈N_K(x)} p_y ≥ 9                              (1)

is necessary, since all nine new vertices must be reached through old
neighbors of x. Passing (1) counts available incidences only; it does not
construct distinct new labels or attachments.

## Seven specified candidates: all fail

The specified final differences from Q are

    D={(50,55),(14,q)},   A={(9,14),(38,55),(14,55)},
    q∈N_Q(14)={2,10,13,19,20,37,50}.

All seven are valid net edit sets: the two deletions are distinct original
edges, the three additions are distinct original nonedges, and all port
sizes are nonnegative. Each old core has 176 edges. Its zero-port vertices
are exactly 9,14,38,55.

Every case has the three forced uncovered pairs

    (28,55), (51,55), (54,55).

The other forced uncovered old pairs are listed below. These lists, together
with the common three pairs, are complete.

| q | Other forced uncovered old pairs | Total |
| ---: | --- | ---: |
| 2 | (1,14), (2,14), (3,14), (14,23), (14,36) | 8 |
| 10 | (10,14), (11,14), (14,15), (14,22), (14,56) | 8 |
| 13 | (8,14), (12,14), (13,14), (14,33), (14,53) | 8 |
| 19 | (5,14), (14,16), (14,19), (14,29), (14,34) | 8 |
| 20 | (14,20), (14,24), (14,25), (14,30), (14,52) | 8 |
| 37 | (14,26), (14,35), (14,37), (14,39), (14,59) | 8 |
| 50 | (14,28), (14,51), (14,54) | 6 |

Each pair has no old edge and no common old neighbor, and at least one
endpoint has no attachment port. An independent all-source BFS on each
saved complete old edge list confirms the exact failure list. Each witness
also retains its old distance, port sizes, and both full neighbor lists in
`initial_q*.json`. All seven additionally fail (1); for example, vertex 55
has only six available neighbor-port incidences in every case.

The common failure has a concrete cause: adding 14–55 makes 55 a zero-port
vertex, so further old paths lost at 50–55 become mandatory old-core repairs.

## Revised old-core rule and its finite screening

Instead, undo the original addition 9–14, retain addition 38–55, and do not
add 14–55. Keep the deletion 50–55 and choose one further HS edge xy to
delete. Before execution the finite family was fixed as

    D={(50,55),(x,y)},   A={(38,55)},
    (x,y)∈E(Q)\{(50,55)}.

This releases the ports at 9 and 14 and leaves 55 with a positive port.
The new edge 38–55 directly repairs the affected old pair at zero-port
vertex 38. Every core has 174 edges and 52 total old-to-new ports.

The one-CPU screen covered all 174 choices in 0.234873 CPU seconds, below
its predeclared 10-second limit:

| Necessary screen | Outcome |
| --- | ---: |
| Nonnegative ports | 174 pass |
| Every old pair with a zero-port endpoint has old distance ≤2 | 139 pass, 35 fail |
| Inequality (1) for all zero-port vertices | 174 pass |
| All screens together | 139 pass |

Each failed case has exactly one forced uncovered old pair, saved with BFS
witnesses. Among the 139 passing cores, 132 have zero-port set {38}; the
other seven delete a second edge incident to 38 and have no zero-port
vertices. The second-edge list and all screening results are saved, with
no isomorphism reduction or assumption about HS automorphisms.

One actual passing core, saved in full in `passing_core.json`, is

    D={(50,55),(2,14)},   A={(38,55)}.

Its port histogram is {0:1,1:46,2:3}; the double-port vertices are 2,14,50,
and the only zero-port vertex is 38. Its old neighbors are

    N_K(38)={5,11,24,33,35,36,50,55}.

Their port sum is nine: vertex 50 contributes two and the other seven
contribute one. All 49 old vertices are within old distance two of 38.
This demonstrates that these necessary screens do not exclude every
two-deletion core with an added edge.

## Applying the cores to the same complete 59-vertex graph

The next authorized experiment supplied an explicit attachment rule rather
than stopping at a port-feasible core. Starting with the same complete
26-bad-pair source graph, for each of the 139 passing second edges xy:

1. Remove old edges 9–14 and xy. The old degree deficits form the multiset
   {9,14,x,y}; repeated old vertices are allowed.
2. Choose any two of the source H's twelve edges and delete them. Their
   four endpoints form the new degree-deficit multiset.
3. Match the four old slots to the four new slots in every distinct way.
   Identify repeated edge sets caused by repeated slots. Reject any
   assignment creating a repeated or already-present edge.
4. Add the four distinct old–new edges. Every resulting candidate is a
   complete simple 59-vertex graph with all degrees eight and 236 edges.

All other source edges remain fixed. Thus this is a specific, finite
completion rule; it is not general attachment search for the 139 cores.

The C++ generator evaluates each full graph's actual radius-two coverage
with adjacency bitsets. One pinned CPU, a 10-CPU-second process limit, and
a 9.5-second internal stopping condition were set before execution. The
whole finite search finished normally:

| Measurement | Result |
| --- | ---: |
| Core / pair-of-H-edges combinations | 139·66 = 9,174 |
| Distinct permutations of each new-slot multiset, before old-slot deduplication | 185,148 |
| Distinct four-edge assignments | 177,408 |
| Rejected assignments | 35,603 |
| Valid complete graphs evaluated | 141,805 |
| Minimum bad pairs | 41 |
| Assignments attaining that minimum | 3 |
| Process CPU / wall seconds | 0.185895 / 0.190148 |
| Peak reported resident memory | 8,948 KiB |

The complete bad-pair histogram is saved in `completion.json`. Ten strict
minimum updates were saved as complete edge lists, with scores
58,55,52,51,50,49,48,45,42,41. Independent Python BFS reads each saved edge
list, verifies simplicity, all 59 degrees and 236 edges, checks the exact
edit replay, and saves every bad pair, distance, common-neighbor set and
both full neighbor lists. All ten graphs have diameter three.

### Best saved complete candidate and exact failure change

The final saved record is `completion.record9.edges`. Its original-label
changes relative to the 26-bad-pair source are

    remove old edges:       (9,14), (0,55);
    remove auxiliary edges:(42,43), (42,47);
    add old–new edges:     (0,47), (9,42), (14,42), (43,55).

Its final old differences from Q are D={(50,55),(0,55)}, A={(38,55)}.
Independent BFS finds 8 bad old–old pairs, 25 bad old–new pairs and 8 bad
new–new pairs, totaling 41.

Of the original 26 bad pairs, 9 are repaired and 17 persist; 24 formerly
covered pairs become uncovered. For every newly uncovered pair, the saved
failure analysis lists all original one- or two-edge paths and identifies
which removed edges break each path. Thus the loss is measured in the same
complete graph, rather than inferred from core feasibility alone.

## Artifacts and stopping point

The sources are
[hs59_old_core_repair.py](../../../computations/dd82/construction/hs59_old_core_repair.py),
[hs59_old_core_completion.cpp](../../../computations/dd82/construction/hs59_old_core_completion.cpp)
and
[hs59_old_core_completion.py](../../../computations/dd82/construction/hs59_old_core_completion.py).
All results are under
[hs59_old_core_repair_run/](../../../computations/dd82/construction/hs59_old_core_repair_run/):

- `base.json`, `initial_q*.json`: recovered HS base, complete seven proposed
  old cores and all exact failure witnesses.
- `enumerated_family.json`, `passing_core.json`, `result.json`: all 174
  revised cores' parameters and screening results, one full passing core,
  and the exact 139-member survivor list.
- `completion_input.txt`, `completion.json`, `.resources.json`, `.log`:
  finite completion input, counts, histogram, edit parameters and limits.
- `completion.record*.edges`, corresponding `.verification.json`, and
  `completion.verification.json`: all ten complete strict-best records and
  independent BFS results. Edge files use compressed 59 labels; verification
  files also include the complete edges and failures in original 60 labels.
- `completion.failure_analysis.json`: persistent, repaired and newly
  uncovered pairs, including every destroyed original short-path witness.

Passing an old-core screen is not a full graph. The full graphs here are
degree-correct failed candidates; none improves the source's 26 bad pairs.
The computed minimum 41 applies only to the stated finite four-port rule.
It neither excludes arbitrary completions of the 139 cores nor proves an
HS59 or general order-59 impossibility theorem. No attachment SAT, auxiliary
graph search, old UNKNOWN rerun, budget extension, or Lean work was started.
