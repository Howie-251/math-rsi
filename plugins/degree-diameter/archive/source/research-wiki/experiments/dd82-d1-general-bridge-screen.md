---
type: experiment
node_id: exp:dd82-d1-general-bridge-screen
title: "Complete necessary bridge domain for arbitrary degree-one six-fiber interfaces"
idea_id: ""
verdict: no
confidence: high
date: "2026-10-12"
hardware: "One CPU thread"
duration: "0.121869 processCPU seconds;0.124736 wall seconds"
provenance: "proofs/dd82/construction/D1_GENERAL_BRIDGE_EXCLUSION.md;computations/dd82/construction/d1_general_bridge_run/"
added: 2026-10-12T03:43:40Z
tags: ["dd82", "construction", "n60", "design"]
---

# Complete necessary bridge domain for arbitrary degree-one six-fiber interfaces

**verdict:** `no`  ·  **confidence:** `high`

## Metrics
80092 baseY alignments exactly cover4278652 state-Y bridges;531 states;left M0,right M0;1157968 existence calls,1163728 DFS nodes;complete=true,exit0.

## Reasoning
Generic local M support and disjointness only;no homogeneous triangle relation, no fixed-point/cycle restriction. Grouping varies omitted source-dual/target-primal choices separately with exact Cartesian-product weights. No surviving bridge, so no fullgraph or global triangle search.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

