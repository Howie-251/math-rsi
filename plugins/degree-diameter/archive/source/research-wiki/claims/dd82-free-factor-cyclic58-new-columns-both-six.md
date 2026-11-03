---
type: claim
node_id: claim:dd82-free-factor-cyclic58-new-columns-both-six
name: "当前固定循环来源58目标的两新增列必须均为6度"
description: ""
node_type: claim
status: verified
provenance: "computations/dd82/construction/free_factors_cyclic58_run/DELETION_56_FEASIBILITY.md; computations/dd82/construction/free_factors_cyclic58_run/DELETION_56_LOCAL_REVIEW.md; reviews/dd82/20261018_free_factors_cyclic58_56_review.json"
tags: ["dd82", "58", "construction"]
date: 2026-10-18
added: 2026-10-18T12:31:52Z
---

# 当前固定循环来源58目标的两新增列必须均为6度

**status:** `verified`

## Statement
当前固定A旧跨关联只删、两侧任意二因子及右匹配的58目标，两新增跨列度均为6。因此全部六条匹配边位于28旧列；旧列恰12条跨度5、16条跨度6。

## Honest scope
5+6完整纸面证明与已有5+5合并；允许支撑重叠和一行双删，非全58排除。6+6未决。正式输入未生成，两exact6剪枝代码在独立delta复核中。

## Evidence chain
5+6的11次删除给|T|≤11,k≤3；两奇偶类各需高删除，其中一类仅一次，迫连续步长10段；偏移14/19及异侧容量/旧列唯一性最终均矛盾。根核读、独立PASS及round3实际直接ACCEPT。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

