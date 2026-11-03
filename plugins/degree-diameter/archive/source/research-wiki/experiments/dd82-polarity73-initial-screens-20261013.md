---
type: experiment
node_id: exp:dd82-polarity73-initial-screens-20261013
title: "Polarity73: two SAT deletion screens, both saved candidates uncompletable"
idea_id: "idea:dd82-polarity73-monotone-reduction"
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "Single pinned CPU per screen; 4 GiB address-space cap; 256 MiB per-file cap"
duration: "Solver CPU 0.013380 + 0.060981 = 0.074361 s; individual wall 0.115486 / 0.187628 s"
provenance: "computations/dd82/construction/polarity73_reduction_run/n58/result.json; n59/result.json; n58/candidate_analysis.json; n59/candidate_analysis.json; reviews/dd82/20261013_V3_polarity73_initial_results_review.json"
added: 2026-10-18T06:06:52Z
tags: ["dd82", "construction", "polarity73", "necessary-screen"]
---

# Polarity73: two SAT deletion screens, both saved candidates uncompletable

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-polarity73-monotone-reduction`

## Metrics
| Order | Variables / clauses | Solver status | Old bad pairs | Saved deletion candidate |
| --- | --- | --- | ---: | --- |
| 58 | 2830 / 12508 | SCREEN_SAT_CHECKED | 330 | Unit-deficit vertex8 cannot meet disjoint saturated neighborhoods16/40 |
| 59 | 2772 / 12277 | SCREEN_SAT_CHECKED | 415 | Vertex20 requires common neighbor43, but43 is saturated |

One solve per order, limits 30 CPU / 45 wall seconds (soft28); both complete DIMACS assignments and direct screen predicates passed decode checks. No target graph was encoded or constructed. SAT-side partial LRAT files are not UNSAT certificates.

## Reasoning
The screen covers variable deletion sets of the saved ambient geometry but only necessary monotone-completion conditions. Both actual assignments are provably uncompletable; this is not a family exclusion. Separate scoped results exclude monotone60/61, require at least8 outer deletions at58/59, exclude the two-fiber59 shape, and exclude a fixed-label58 example via complete98-node/7-code exact cover. [Proof and scope](../../proofs/dd82/construction/POLARITY73_REDUCTION_CANDIDATE.md).

[Round2 actual response](../../reviews/dd82/20261013_V3_polarity73_initial_results_review.json) accepts the scoped results and approves a unit-deficit choice refinement. The 2/4 loop remains incomplete. Refined source exists but has no prepared CNF or solver result; this record does not evaluate that implementation. See [58 result](../../computations/dd82/construction/polarity73_reduction_run/n58/result.json), [58 candidate analysis](../../computations/dd82/construction/polarity73_reduction_run/n58/candidate_analysis.json), [59 result](../../computations/dd82/construction/polarity73_reduction_run/n59/result.json), [59 candidate analysis](../../computations/dd82/construction/polarity73_reduction_run/n59/candidate_analysis.json), and [progress / comments](../DD82_PROGRESS_AND_COMMENTS_20261018.md).

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

