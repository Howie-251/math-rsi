# Repairing fixed matching routes, then completing all six internal graphs

Date: 2026-10-12. One dedicated matching repair reduced the immutable
route deficit from **26 to zero**, producing a new complete 60-vertex,
240-edge, eight-regular graph. Its original internal Petersen graphs leave
**186 bad pairs**, so it is a failed full candidate. One exact SAT input
then allowed **all six internal graphs** to change independently. The
result was **UNSAT with an independently checked LRAT proof**. This closes
completion of this specific new external matching skeleton, not the full
six-Petersen family. No second input or solver attempt was run.

## Why the external matching skeleton changed first

The starting graph was the actual
[97-pair construction](../../../computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.json).
Keeping its fifteen external matchings while freeing all six internal
graphs is already impossible by the direct
[fixed-route obstruction](PETERSEN_ALL_INTERNAL_COMPLETION.md): some five
fixed route slots reach only two or three targets. That planned SAT call
was cancelled before encoding.

For each ordered pair of different fibers and source vertex, define

\[
B_{ij}(u)=\{M_{ij}(u)\}\cup
 \{M_{kj}(M_{ik}(u)):k\notin\{i,j\}\},
\qquad
F=\sum_{i\ne j}\sum_{u\in F_i}\max(0,4-|B_{ij}(u)|).
\]

Every valid target has \(F=0\): the two internal cubic graphs can add only
six route slots to each row. The new repair objective is precisely \(F\),
not the full graph's bad-pair objective. A move swaps two outputs of any
one of the fifteen matching permutations and updates its inverse. Thus
all external interfaces remain perfect matchings.

The deterministic routine scans matching pairs and source pairs in
lexicographic order. At the first strict improvement it resets the current
level; equal-score states may be queued for a nonincreasing level search.
It stops at \(F=0\), closure of the current neutral component, 500 total
stored states, or 4.8 internal CPU seconds, with a five-second process CPU
limit. In the actual run **every one of the 21 moves on the resulting path
strictly improved \(F\)**; no neutral move was used on that path.

This domain changes local seven-route matrices. It is not the previously
closed binary palette preserving all original \(M+PM+MP\), nor a replay
of a fixed-root completion: the actual source is different, external
interfaces move, and the subsequent completion fixes no internal graph.
In particular the altered interfaces 02,03,12,13 change matrices that the
97-pair seed had retained from the original twenty-pair graph.

## Actual repair and complete failed graph

The score path was

\[
26,23,22,20,19,18,17,16,15,14,12,11,10,8,7,6,5,4,3,2,1,0.
\]

The run checked 1,791 switches, expanded 21 states and stored 161 states.
At the endpoint, 130 of the 300 directed rows have four distinct fixed
targets and 170 have five. The actual changed interfaces are

\[
01,02,03,05,12,13.
\]

There are 24 net removed and 24 net added matching edges. The complete
switch path, every permutation, and the exact net edits are saved. The
Python launcher independently reconstructed every state on the returned
path, checked its degree and score, and verified each recorded two-edge
switch against the full edge sets.

Adding the original six internal Petersen graphs gives a simple
eight-regular graph with 60 vertices and 240 edges. An independent BFS
found diameter three and 186 bad pairs; the existing route energy is 209.
The bad-pair counts by unordered fiber block are:

| Block | Bad pairs | Block | Bad pairs | Block | Bad pairs |
|---|---:|---|---:|---|---:|
| 01 | 15 | 02 | 18 | 03 | 18 |
| 04 | 14 | 05 | 19 | 12 | 14 |
| 13 | 14 | 14 | 9 | 15 | 17 |
| 23 | 12 | 24 | 6 | 25 | 12 |
| 34 | 2 | 35 | 13 | 45 | 3 |

Omitting any one fiber does not produce HS50. The graph satisfies the new
external-route requirement but is not an improvement in bad-pair count and
is not a target graph.

## Exact completion input: all six internal graphs free

The new skeleton's 150 external edges are fixed. Introduce a Boolean
variable \(e_{uv}\) for each of the 45 unordered internal pairs in each
fiber: **270 variables**, with no fixed internal edge and no symmetry
breaking. Every vertex has exactly three internal neighbors. The direct
cardinality encoding uses a negative clause for each four incident edges
and a positive clause for each seven incident edges. This is exactly
degree three among nine possible neighbors.

Within each fiber, forbid every triangle and every four-cycle. Every
Petersen graph satisfies these clauses. Conversely, in any cubic graph on
ten vertices with no triangle or four-cycle, the radius-two expansion at
any vertex consists of \(1+3+6=10\) distinct vertices. Thus the internal
graph has diameter two, which is all that is needed for the target
reduction. No separate Petersen uniqueness theorem is required for the
SAT-to-target direction.

Now take \(u\in F_i,v\in F_j\) with \(i\ne j\). If the direct matching
or a route through another fiber already covers the pair, no clause is
needed. Otherwise the only two possible kinds of remaining route are

\[
u\;\mathord{-}\;M_{ji}(v)\;\mathord{-}\;v,
\qquad
u\;\mathord{-}\;M_{ij}(u)\;\mathord{-}\;v,
\]

using one internal edge in the source or target fiber, respectively.
Therefore the exact remaining coverage clause is

\[
e_{u,M_{ji}(v)}\ \lor\ e_{M_{ij}(u),v}.
\]

The two variables are valid distinct internal pairs: if either were a
loop, the direct matching would already have covered \((u,v)\). There are
815 such uncovered cross pairs. Internal pairs are covered by the local
radius-two argument. Consequently every target with these external
matchings maps to this CNF, and any satisfying assignment expands to a
60-vertex eight-regular diameter-two graph.

The exact clause counts are:

| Constraint | Clauses | Original clause IDs |
|---|---:|---|
| Exactly three internal neighbors | 9,720 | 1–9,720 |
| No internal triangles | 720 | 9,721–10,440 |
| No internal four-cycles | 3,780 | 10,441–14,220 |
| Binary cross-pair coverage | 815 | 14,221–15,035 |
| Total | 15,035 | |

As a concrete encoding check, inserting the saved candidate's six original
Petersen graphs satisfies every local clause. Its 186 falsified binary
clauses correspond exactly, as a set of vertex pairs, to the independently
saved BFS's 186 bad pairs.

## Single solve and exact scope

The one CaDiCaL invocation had a 180-CPU-second limit, one CPU, 8 GiB
address-space limit and 768 MiB proof limit. It returned UNSAT in
0.009957 CPU seconds, using twelve conflicts and twelve decisions. Its
1,771-byte LRAT proof has 87 added clauses. A separate `lrat-trim --no-trim`
invocation on the exact saved CNF and proof returned `s VERIFIED`.

A subsequent read of the existing proof's references found 140 distinct
original clauses: 24 degree clauses, 35 triangle clauses, 17 four-cycle
clauses and 64 binary coverage clauses. All antecedents are positive.
This inspection was not a new solve or proof check. Since the actual
certificate references both girth families, it does **not** justify
extending the conclusion to unrestricted cubic internal graphs. No
minimality claim is made about those references.

The conclusion is only that **this repaired external skeleton has no
completion by six arbitrary internal cubic girth-at-least-five graphs**,
and hence no completion by six labeled Petersen graphs. The passing
five-slot condition alone does not ensure joint internal realizability.
The experiment did not enumerate all external skeletons, and the full
six-Petersen construction problem remains open.

## Files and measured resources

- [Repair source](../../../computations/dd82/construction/petersen_fixed_route_repair.cpp)
  and [launcher](../../../computations/dd82/construction/petersen_fixed_route_repair_run.py).
- [Exact path and permutations](../../../computations/dd82/construction/petersen_fixed_route_repair_run/search.json),
  [all fixed rows](../../../computations/dd82/construction/petersen_fixed_route_repair_run/fixed_routes.json),
  [resource record](../../../computations/dd82/construction/petersen_fixed_route_repair_run/resources.json).
- [Complete candidate and net edits](../../../computations/dd82/construction/petersen_fixed_route_repair_run/candidate.json),
  [edge list](../../../computations/dd82/construction/petersen_fixed_route_repair_run/candidate.edges),
  [independent BFS with all bad pairs](../../../computations/dd82/construction/petersen_fixed_route_repair_run/candidate.verification.json),
  [block diagnostics](../../../computations/dd82/construction/petersen_fixed_route_repair_run/candidate.diagnostic.json).
- [Completion encoder and runner](../../../computations/dd82/construction/petersen_repaired_external_completion.py),
  [encoding map](../../../computations/dd82/construction/petersen_repaired_external_completion_run/encoding.json),
  [all binary-clause meanings](../../../computations/dd82/construction/petersen_repaired_external_completion_run/coverage.json),
  [CNF](../../../computations/dd82/construction/petersen_repaired_external_completion_run/input.cnf).
- [Result and checker resources](../../../computations/dd82/construction/petersen_repaired_external_completion_run/result.json),
  [LRAT](../../../computations/dd82/construction/petersen_repaired_external_completion_run/proof.lrat),
  [checker log](../../../computations/dd82/construction/petersen_repaired_external_completion_run/certificate_check.log),
  [proof-reference ranges](../../../computations/dd82/construction/petersen_repaired_external_completion_run/proof_references.json).

| Operation | CPU seconds | Wall seconds |
|---|---:|---:|
| Matching repair child | 0.005582 | 0.067978602 |
| Independent candidate BFS child | 0.030683 | Included below |
| Repair launcher, reconstruction and diagnostics | 0.031486967 | 0.149270672 including its children |
| CNF preparation | 0.037395348 | 0.038629536 |
| Sole SAT call | 0.009957 | 0.036712158 |
| Sole independent LRAT check | 0.003624 | 0.005445786 |

All runs are finished. There was no repeated solver, extra search episode,
or general annealing run.
