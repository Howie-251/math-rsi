# One full type-6 HS58 assembly attempt

Date: 2026-10-12. The single bounded call returned **UNKNOWN**. It does
not exclude this type or prove that a fifth old addition is necessary.
No unchanged restart is scheduled, and no learned solver state was saved.

After the ten other auxiliary types had mathematical exclusions, the
remaining type was a star on eight vertices with two disjoint extra leaf
edges. In the catalog labeling its edges are

```
01,02,03,04,05,06,07,14,23.
```

All 175 original HS edges have independent retention variables, with
exactly two false. All 1,050 original nonedges have addition variables,
with exactly four true. All 400 old-new edges are free. Thus neither
the deleted-edge geometry nor any added edge or port is fixed. Every
old degree is exactly eight; each new column has sum `8-d_H(a)`.
There is no symmetry normalization and no optional structural pruning.

Every old-old and old-new pair is constrained by its actual direct edge
or every possible two-edge route, with exact AND definitions for two
variable edges. All new-new pairs already have distance at most two
inside H. The formula therefore covers all placements in this exact
HS50 extension model with auxiliary type6. Any isomorphic labeling of H
can be relabeled to this representative without changing old labels.

Before solving, the explicit four-addition old core from the previous
`parent3_h4_7.json` was retained, and an integral capacity flow assigned
all 46 attachments to the new H columns. This produced a complete graph
with 58 vertices, 232 edges and degree eight everywhere. Independent BFS
found **114 bad pairs and diameter three**. The seed is saved as an actual
failed graph; none of its old edits or attachments is fixed in the CNF.

The CNF has 121,968 variables and 389,930 clauses, including 1,625
coverage clauses: all 1,225 old-old pairs and all 400 old-new pairs.
The 1,625 primary variables are the 175 retention, 1,050 addition and
400 attachment choices. Preparation used 0.459816343 parent CPU seconds,
0.030757 independent BFS child CPU seconds, and 0.501381762 wall seconds.

CaDiCaL was given ten CPU seconds, one CPU, 4 GiB memory and a 128 MiB
proof-output cap. It returned exit0 / UNKNOWN after 9.865733 CPU seconds
and 10.149353072 wall seconds. The emitted partial proof is not an UNSAT
certificate and was not treated or checked as one. A rerun would be a
cold start, not continuation of a saved search tree.

The analytic results excluding `v in W`, and any later stronger
endpoint restrictions, are separate mathematical information. They
were not clauses of this executed input. The fixed-D type8 checked
UNSAT input from the earlier experiment is likewise a different domain.

Artifacts:

- [Source](../../../computations/dd82/construction/hs58_four_add_type6_all_edits.py).
- [Full seed](../../../computations/dd82/construction/hs58_four_add_type6_all_edits_run/seed.json),
  [edge list](../../../computations/dd82/construction/hs58_four_add_type6_all_edits_run/seed.edges),
  [independent BFS and all failures](../../../computations/dd82/construction/hs58_four_add_type6_all_edits_run/seed.verification.json).
- [Actual encoding and maps](../../../computations/dd82/construction/hs58_four_add_type6_all_edits_run/encoding.json),
  [result and resource record](../../../computations/dd82/construction/hs58_four_add_type6_all_edits_run/result.json),
  [solver log](../../../computations/dd82/construction/hs58_four_add_type6_all_edits_run/solver.log).

## Subsequent analytic closure

The completed endpoint arguments in [the integrated four-addition proof](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md) now close this entire type-6 domain independently. The root agent read and checked those proofs. This experiment remains UNKNOWN; it is not a proof dependency and will not be restarted. External review remains unfinished after authentication errors.
