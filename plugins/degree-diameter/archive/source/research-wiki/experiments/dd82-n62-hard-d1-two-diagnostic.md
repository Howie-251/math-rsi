---
type: experiment
node_id: exp:dd82-n62-hard-d1-two-diagnostic
title: "Two short canonical D1 diagnostics"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-11"
hardware: "One pinned CPU,≤305MB RSS per run; host quota55CPU/300GiB"
duration: "10.215s and10.096s wall; ten solver seconds per cold start"
provenance: "computations/dd82/n62/d1_hard_diagnostic/results.json"
added: 2026-10-11T10:56:00Z
tags: ["dd82", "n62", "diagnostic"]
---

# Two short canonical D1 diagnostics

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
b28 andb41 both UNKNOWN, exit0; noSAT, noUNSAT, partialLRAT traces only.

## Reasoning
Canonical coverage and added facts PASS14; this experiment establishes only bounded solver behavior, no mathematical exclusion. No unchanged retry scheduled.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

