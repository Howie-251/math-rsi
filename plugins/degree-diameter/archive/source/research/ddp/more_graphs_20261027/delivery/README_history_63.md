# 63个完整图：当前确定性生成包

| 最大度 | 直径 | 完整例子的阶数 | 例子数 |
|---:|---:|---|---:|
| 11 | 5 | 37629至37631，每个整数 | 3 |
| 12 | 5 | 42343至42402，每个整数 | 60 |

数学最强N(11,5)≥37631、N(12,5)≥42402；对照2026-10-27 12:58:40 UTC核对的公开快照37628/42342。不同阶数保证这些图不同，不能把例子数当独立方法数或最优值。完整Lean图实例仍0；Goal ACTIVE。

## 生成任意例子

在解压目录或项目root运行（仅Python标准库，无搜索/BFS）：

```bash
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42402 --output graph42402.edges
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 11 --order 37631 --output graph37631.edges
```

将order改成表内任意整数即可。输出第一行n m，其后每行u v一条无向边。若独立放置程序和families.json，可用`--source /path/to/deg12_diam5_n42342.txt`或degree11对应源文件。程序按字面步骤检查邻集、原度数与实际边数，无外部库或网络依赖。

families.json保存每步完整pins（全邻集）、mandatory_pins、anchors、原degree和证据路径。所有原图边保留，m等于原边数加已用步骤的实际邻集cardinality总和。最新强图边表在`../h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges`。

## 为什么是完整合法图

每次在实际更早图B中，对完整新点邻集S检查R4_B(S)=V(B)，并检查全部新增degree。保留旧边，故旧旧距离不增加，新旧距离≤5。每个步骤独立具备这个完整条件，归纳保证所有前缀，不是从最大图删点推断。

早期邻集包含完整Q-line像；42397步骤改为删去饱和pin13863、保留9pins并补3anchors。该子集不依赖“仍自动覆盖核心”的假设，实际完整R4为其证明。字面完整邻集是[60,3881,5499,11733,13135,22612,22626,28441,31353,34220,38043,41614]。

42398步骤使用新的Baer子平面邻域：13raw点折到11pins，再补anchor41666。它的完整邻集是[1928,2576,7337,8710,14217,14622,23929,30347,34888,35165,40153,41666]。rank-nullity保证core覆盖，实际selectedR4确认全部旧点覆盖；只对该新机制首点作了一次fresh-edge-list newroot独立检查，没有重算旧旧距离。Baer证明与生产见../h9_baer_plane_pool/THEOREM.md、../h9_baer_plane_extensions/REPORT.md。

阶数超过D4 Moore界（degree11为12222、degree12为17569），所以直径恰5。旧全源验收代表为37631/42377；其后的同族生产只验新增degree与完整coverage，不重复全源BFS/互审。旧Gemini审阅覆盖前38例，完整Lean仍未完成。

42399–42402使用新的Rédei15阻塞邻域，每项10个mandatory pins加2anchors。每步均保存实际degree与全currentR4覆盖；新机制首步从展开边表独立检查新root及旧边完整保留，CPU0.400秒。没有逐图重扫旧root。新规则证明、85候选池与生产见`../h9_redei15/`；63例覆盖的参数仍为2，完整Lean仍0。

Rédei15新规则的单次集中Gemini数学审阅已接受条件core定理与四个完整扩张；85项账目已纠正为4接受+23度数阻断+58覆盖失败。历史reviewed_example_count仍38，不把新规则审阅说成全部63例重新全源核验。处置记录见reviews/ddp/redei15_20261027.disposition.json，完整总结见../h9_redei15/REPORT.md。

## 原作者与证据

两份完整基图属于Dharunish Yugeswardeenoo，partial-fold/duality基础归Rishabh Rajiv。原始来源[Zenodo23653049](https://zenodo.org/records/23653049)；原图保存于`research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt`及对应degree12文件。raw adjacency每行是vertex后跟全部邻居，不含n/m头。

本项目的新工作是这些明确增点、有限覆盖构造与可复现参数。source_urls和署名均保存在families.json。完整数学说明见`../FINAL_RESULTS_PROOF.md`，各生产批的REPORT/RESULT保存准确命中、限时未决、未试范围和成本。历史57例说明另存README_history_57.md；旧图与原证据保留，不重算。
