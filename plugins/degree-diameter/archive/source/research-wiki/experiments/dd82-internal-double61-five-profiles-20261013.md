---
type: experiment
node_id: exp:dd82-internal-double61-five-profiles-20261013
title: "Internal-double61: five actual profiles and checked h1 exclusion"
idea_id: "idea:dd82-internal-double-path61"
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "Single pinned CPU per profile; 4 GiB address-space cap"
duration: "Solver CPU total 232.086216 s; independent LRAT check 0.113276 s; CPU totals are not research elapsed time"
provenance: "computations/dd82/n61/internal_double_full61_run/all_results.json; prompts/26101315-1/final.md"
added: 2026-10-18T06:06:52Z
tags: ["dd82", "n61", "checked-cnf", "unknown"]
---

# Internal-double61: five actual profiles and checked h1 exclusion

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-internal-double-path61`

## Metrics
| Case | Original solver CPU s / result | Refined solver CPU s / result |
| --- | --- | --- |
| r0_h1_b0 | 4.012334 / CHECKED_UNSAT_CASE | Not rerun |
| r1_h0_b0 | 56.298772 / UNKNOWN | 57.788672 / UNKNOWN |
| r2_h0_b1 | 57.767905 / UNKNOWN | 56.218533 / UNKNOWN |

Original h1 input: 53046 variables, 163721 clauses; independent LRAT verified. Each profile had 60 CPU / 90 wall second limits, soft solver time 58 seconds. Five terminal profiles, one checked contradiction, no target graph.

## Reasoning
The verdict is partial for the scoped structural mechanism. With the reviewed inherited reductions and lossless original-A representation, the h1 contradiction proves universal h0/no101, while both remaining local types are open. It does not exclude all internal D paths or all order61 targets. The 4/4 review loop closed; no unchanged rerun occurred during wiki backfill. See [accepted common-neighbor inclusion](../claims/dd82-n61-internal-common-attachment-exclusion.md), [actual results](../../computations/dd82/n61/internal_double_full61_run/all_results.json), [final delivery](../../prompts/26101315-1/final.md) and [user comments / full remaining scope](../DD82_PROGRESS_AND_COMMENTS_20261018.md).

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

