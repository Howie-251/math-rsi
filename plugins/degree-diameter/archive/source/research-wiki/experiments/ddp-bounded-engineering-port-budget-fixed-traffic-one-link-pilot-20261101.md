---
type: experiment
node_id: exp:ddp-bounded-engineering-port-budget-fixed-traffic-one-link-pilot-20261101
title: "有限工程pilot：16port余度16200→4554；3750图240固定流单边删除后平均2.875→2.9hop"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/PRED.md; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/RESULT.json; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/TERMINAL.json; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/NOTE.md; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/run_once.py; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/flow_paths.csv; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/pilot.html; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/pilot.html.txt; research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/REPORT.md; research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/ROOT_DISPOSITION.json"
added: 2026-11-01T19:08:28Z
tags: ["ddp", "method-ledger"]
---

# 有限工程pilot：16port余度16200→4554；3750图240固定流单边删除后平均2.875→2.9hop

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** bounded_engineering_evaluation

**目标与阶数：** (?,?)；L=不适用／见变体

**距目标的证据：** Engineering-only fixed workload and port arithmetic; no new graph validity/diameter claim；16port模型：15552源余16200portslots，16389终图余4554，+837switches却−11646slots，因为+12519网络边占25038端口、大于新增物理端口13392。3750固定240流baseline总hop690/均2.875/峰directedload4/共同flowrate上界1/4。仅删sample最忙(122,1171)，双向负载8：240流仍通，总hop696/均2.9/峰4/上界1/4，8路径变化、6流绕1hop、maxdetour1。预测该样本仍连通且detour≤1得到支持。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "mathematical_method_entry": false,
  "engineering_only": true,
  "inherited_sources_and_accepted_graphs": true,
  "physical_ports_per_switch_A": 16,
  "port_accounting_16ports": [
    {
      "name": "published_source15552",
      "switches": 15552,
      "network_links": 116316,
      "inherited_degree_histogram": {
        "14": 648,
        "15": 14904
      },
      "physical_ports_per_switch": 16,
      "network_port_endpoints": 232632,
      "available_non_network_switch_port_slots": 16200,
      "slots_identity_Pn_minus2m": 16200
    },
    {
      "name": "accepted_clone16389",
      "switches": 16389,
      "network_links": 128835,
      "inherited_degree_histogram": {
        "14": 72,
        "15": 4410,
        "16": 11907
      },
      "physical_ports_per_switch": 16,
      "network_port_endpoints": 257670,
      "available_non_network_switch_port_slots": 4554,
      "slots_identity_Pn_minus2m": 4554
    }
  ],
  "port_accounting_change": {
    "switches_added": 837,
    "network_links_added": 12519,
    "server_port_slot_change": -11646
  },
  "source3750_P24_P32_inherited_server_port_slots": {
    "24": 15000,
    "32": 45000
  },
  "endpoints": [
    0,
    234,
    468,
    703,
    937,
    1171,
    1406,
    1640,
    1875,
    2109,
    2343,
    2578,
    2812,
    3046,
    3281,
    3515
  ],
  "ordered_nonself_unit_flows": 240,
  "routing": "sort neighbors; BFS first parent; one shortest path per flow",
  "link_capacity_model": "each directed link capacity1, full duplex; independent ideal static link capacities",
  "baseline": {
    "reachable_flows": 240,
    "unreachable_flows": 0,
    "total_hops_of_routed_flows": 690,
    "mean_hops_of_routed_flows": 2.875,
    "peak_directed_link_unit_flow_load": 4,
    "fixed_route_common_flow_rate_upper_bound": 0.25
  },
  "one_link_removed": {
    "reachable_flows": 240,
    "unreachable_flows": 0,
    "total_hops_of_routed_flows": 696,
    "mean_hops_of_routed_flows": 2.9,
    "peak_directed_link_unit_flow_load": 4,
    "fixed_route_common_flow_rate_upper_bound": 0.25
  },
  "changes": {
    "removed_undirected_link": [
      122,
      1171
    ],
    "baseline_bidirectional_unit_flow_load_on_removed_link": 8,
    "rerouted_path_count": 8,
    "max_detour_hops_among_still_routed_flows": 1,
    "detour_histogram": {
      "0": 234,
      "1": 6
    },
    "mean_hop_change": 0.02499999999999991,
    "peak_directed_load_change": 0
  },
  "prediction_supported": true,
  "new_workload_differs_from_old_pilot": "endpoints floor(i*n/16), unit demand, deterministic single shortest path, one link failure",
  "new_traffic_graph_parses": 1,
  "source15552_final16389_graph_parses": 0,
  "new_traffic_route_BFS_total": 32,
  "old_allroot_validity_D3_BFS": 0,
  "cumulative_charged_CPU_seconds": 0.322702775,
  "CPU_budget_seconds": 5,
  "industrial_advantage_claimed": false,
  "hardware_throughput_measured": false,
  "global_fault_diameter_claimed": false,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/PRED.md](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/PRED.md)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/RESULT.json](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/RESULT.json)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/NOTE.md](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/NOTE.md)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/run_once.py](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/run_once.py)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/flow_paths.csv](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/flow_paths.csv)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/pilot.html](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/pilot.html)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/pilot.html.txt](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/pilot.html.txt)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/REPORT.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/engineering_pilot/REPORT.md)；[research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/engineering_pilot_20261101/ROOT_DISPOSITION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 240 fixed sampled flows, one selected failed link, fixed routing and abstract port model; no global fault diameter or allpairs traffic inference A: inherited15552/final16389 degree histograms with physical16ports, each networkedge consumes2 endpoints; no large graph parse. B: acceptedF5/3750 parsedonce for16 endpoints floor(i*3750/16),240 ordered nonself unit flows, sorted-neighbor first-parent shortest paths; each directedlink capacity1 full duplex. Delete only the sample busiest undirectedlink (sum two directions,tie lex) and reroute sameflows. Prior engineering workload differs; not a graph/method or throughput/faultdiameter certificate.

**仍未完成：** Only the stated completed or sampled scope stops. Same Goal remains ACTIVE; no new graph or global record is claimed.

**启发与重启依据：** STOP independent finite engineering pilot. Keep results as abstract port accounting and this fixed workload/link/router only; no industrial advantage, hardware measurement, optimal network throughput, allpair/global failure diameter, bisection, wiring or cost inference. Capacity1/L is the fixed-route common-flow upperbound under the stated link units; do not compare directly with prior1/15 ECMP demand. No new graph, parameter, Lean instance or mathematical method.

**单独的重启条件：** STOP independent finite engineering pilot. Keep results as abstract port accounting and this fixed workload/link/router only; no industrial advantage, hardware measurement, optimal network throughput, allpair/global failure diameter, bisection, wiring or cost inference. Capacity1/L is the fixed-route common-flow upperbound under the stated link units; do not compare directly with prior1/15 ECMP demand. No new graph, parameter, Lean instance or mathematical method.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

