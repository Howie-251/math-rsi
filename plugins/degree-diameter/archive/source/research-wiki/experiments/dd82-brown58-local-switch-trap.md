---
type: experiment
node_id: exp:dd82-brown58-local-switch-trap
title: "Brown+hub seed is a strict single-switch local minimum"
idea_id: "idea:dd82-brown57-extension"
verdict: partial
confidence: high
date: ""
hardware: "oneCPU per check;noGPU"
duration: "5seconds profile and2.54CPU seconds exact neighborhood"
provenance: "computations/dd82/construction/brown58_one_switch.json; search58_profile.json; search58_profile.verification.json"
added: 2026-10-11T08:07:09Z
tags: ["dd82", "exact-scope"]
---

# Brown+hub seed is a strict single-switch local minimum

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-brown57-extension`

## Metrics
Seed21 uncovered pairs;all39200 legal single switches have>=26. Five-second search:8212021 legal proposals,no improvement. Independent BFS confirms21 pairs distance3.

## Reasoning
Explains local-search failure in this exact seed neighborhood; does not exclude longer sequences or any full graph order.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

