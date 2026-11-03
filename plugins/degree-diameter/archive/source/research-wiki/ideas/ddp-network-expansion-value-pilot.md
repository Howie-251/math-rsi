---
type: idea
node_id: idea:ddp-network-expansion-value-pilot
title: "保边扩张的网络价值：端口诊断与待检验性能"
stage: piloted
outcome: pending
added: 2026-10-29T15:20:37Z
based_on: ["paper:ddp-record-sources-20261026"]
target_gaps: ["gap:DDP3"]
tags: ["ddp", "engineering-diagnostic", "pending-performance"]
---

# 保边扩张的网络价值：端口诊断与待检验性能

**stage:** `piloted`  ·  **outcome:** `pending`

端口子任务已执行；未有吞吐／延迟证据，不计数学新下界。

## Thesis
状态：D13符号端口账本已完成，性能仍pending；数学新下界仍是主目标。本提案没有吞吐／延迟结果，不改数学完成标准、不成为第三条永久主线。

先选既有三族之一，复用原公开完整源、中间图、项目最终图，明确把点作为何种设备、每点总端口r以及端点／网络链路占用。端口账P=rn−2m、变化ΔP=ar−2b只是假设下的潜在端点槽位，不等于服务器容量、吞吐或时延收益。原空余端口若已接业务，新增网络边也可能挤占业务端口；新增设备与链路成本必须计入。

只有先定路由、需求、链路容量与公平预算，才作一次有界诊断。旧业务保持与新增容量分开；固定最短路、逐跳ECMP和所有最短路径均匀分流不能混用名称。样本负载可以作诊断，不能代替严格图直径；没有排队／硬件模型不称实测延迟，没有布局不称线长或能耗收益。

可复用的数学对象为[11D5](../experiments/ddp-h9-qline-d11-family-37631.md)、[12D5](../experiments/ddp-h9-qline-d12-family-42377.md)、[13D5](../experiments/ddp-d13-singlefault-star-family-51457-20261027.md)和[字面生成器／families](../../research/ddp/more_graphs_20261027/delivery/families.json)。这些旧实验验证图构造，不验证本提案的网络性能。

## 背景来源与未执行边界

以新包[SOURCES W6–W8](../../context/DD_PORTFOLIO_REFRESH_20261029/SOURCES.md)为继承阅读范围：[Slim Fly研究组页](https://spcl.inf.ethz.ch/Research/Scalable_Networking/SlimFly/)、[Jellyfish NSDI官方摘要](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/singla)、[PolarFly作者摘要](https://arxiv.org/abs/2208.01695)。本次Wiki合并未重新访问这些页面、未声称全文复算，不将文献性能比例移植到本项目，也不因D2网络背景重开D2求解。

完整待执行定义见[ENGINEERING_PILOT](../../context/DD_PORTFOLIO_REFRESH_20261029/ENGINEERING_PILOT.md)、[原提案草稿](../../context/DD_PORTFOLIO_REFRESH_20261029/wiki_import/ddp-network-expansion-value-pilot.md)。首次诊断可支持、反驳或保持未决，结果都只属于声明规模／路由／负载；进一步工程投入取决于实际问题与人工意见。尚未创建任何性能experiment或claim。


## 已完成的端口子实验，性能仍待检验

[exp:ddp-network-d13-symbolic-port-ledger-20261029](../experiments/ddp-network-d13-symbolic-port-ledger-20261029.md)复用原51417／中51437／终51457三张已验图的保存n,m。新增40台设备／412条网络边给ΔP=40r−824；整数r≤20槽位减少，r≥21才可能净增。CPU0.00201922。它只是端口记账，不是路由、吞吐、延迟或硬件性能模拟；性能和公平成本判断仍未执行。

## Key risks
Symbolic spare-port balances are model dependent; performance, cost and endpoint placement remain pending. No industrial benefit is established.

<!-- TWO_METHODS_FINAL_RESULTS_20261101 -->
## 2026-11-01 有限静态路由pilot已实际完成

[新非数学实验节点](../experiments/ddp-f5-clone-fixed16-old-router-engineering-pilot-20261101.md)记录原3750、3900与4125图的同一固定16旧标签、240项有序需求（各1/15，总16）；每条完整最短路径等权分流、每有向边容量1，仅48次路由源BFS，CPU0.50115918。不是旧3750源D3复验，也不是硬件或包级吞吐实验。

主配置24口的剩余端点槽为15000/12600/9000；新增设备150/375，新增网络边3000/7500；r32/48仅作槽位计数。峰值有向负载为0.266667/0.266667/0.213333，最后一图在该静态模型下降20%；平均跳数均2.941667。新增边承载流量比例3.40278%/11.19643%，不等于新边hop-volume比例2.31350%/7.61230%。RMS按所有2m有向边含零负载平均，新增边也改变分母。

完整旧邻域clone可折叠回原中心，故全部旧旧最短距离严格不变，但最短路条数可增，等路径分流负载因此改变。新增路由器未作为流量端点；故障、布线、功耗、队列、收敛及货币成本均未测，不作产业收益结论。本pilot已停止，不成为第三条长期数学研究线，不新增method-ledger行。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

