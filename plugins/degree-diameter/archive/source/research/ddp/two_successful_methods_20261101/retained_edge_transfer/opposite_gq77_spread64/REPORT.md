# 新固定候选：(64,3)160050点／5121600边

GF7／GF49的400点、400线GQ与50条有序slope spread均已实际构造。奇特征修正为普通mod7减法及Tr(z)=2z0；全部156800个非incident投影、160000组输入索引与spread分割通过。

从公开160000点opposite-GQ源的3200个度63旗标点出发，每条spreadline聚64flags新增一点，50步恰用尽全部余度。每步在当前完整图重查R2，包括此前新点；50步全部覆盖，最终160050点全64正则、保5118400旧边、仅增3200边、无new-new边，数学上直径恰3。

完整排序边表已close：首行`160050 5121600`，随后严格`u<v`，文件64,591,375字节。几何＋编译＋生产实际childCPU合3.8717秒，单worker／300CPU预算；未跑16万旧根或全源BFS，无solver／Lean／hash。

这是一张完整候选，独立RREF几何／字面公式和50新增根验收由root另派，正式新增计数由parent决定。具体Lean也单独进行。相对此次best-located公开160000保证多50点，但全球最高／首创未认证；源160000复现不算新图。

[完整图](graph_d64_D3_n160050.edges) · [生成参数](PARAMETERS.json) · [自含覆盖证明](PROOF.md) · [50步当前R2证据](EXTENSION_STEPS.json) · [实际CPU与生产](BUILD_RUN.json) · [结果](RESULT.json) · [公开比较](../../public_baseline_audit/DEGREE64_SPREAD_TARGET_GATE_20261101.md)。
