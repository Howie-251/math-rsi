---
type: experiment
node_id: exp:dd82-full-false-twin58-cnf
title: "General false-twin58 matching CNF: original and strengthened runs undecided"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-13"
hardware: "one CPU per sequential solver attempt"
duration: "original87.819016CPU/112.245409wall; strengthened117.424474CPU/120.089353wall"
provenance: "proofs/dd82/construction/FULL_MATCHING58_STRENGTHENED_DISCOVERY.md"
added: 2026-10-13T08:48:33Z
tags: ["dd82", "false-twins", "cnf"]
---

# General false-twin58 matching CNF: original and strengthened runs undecided

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
Original37296vars/115500clauses:OUTPUT_LIMIT_UNKNOWN. Strengthened37307vars/116197clauses:630 valid root binaries plus all11Q12 conjugacy types, proof-disabled UNKNOWN. One attempt on each distinct input.

## Reasoning
Both encodings preserve the whole false-twin58 family up to relabeling. Neither bounded attempt produced a model or mathematical exclusion. The second changed propagation and normalization; no unchanged retry.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

