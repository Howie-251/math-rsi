# 103个完整图：三个参数的确定性生成包

| 最大度 | 直径 | 完整例子的阶数 | 例子数 |
|---:|---:|---|---:|
| 11 | 5 | 37629至37631，每个整数 | 3 |
| 12 | 5 | 42343至42402，每个整数 | 60 |
| 13 | 5 | 51418至51457，每个整数 | 40 |

当前数学下界为N(11,5)≥37631、N(12,5)≥42402、N(13,5)≥51457；公开基线分别为37628、42342、51417，核对日期2026-10-27。这是103个不同阶数完整例子、3个参数格，不是103种独立方法或最优值声明。完整Lean图实例仍0，Goal保持ACTIVE。

## 生成任意例子

在解压目录或项目root运行，仅Python标准库，没有搜索或BFS：

~~~bash
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 13 --order 51457 --output graph51457.edges
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42402 --output graph42402.edges
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 11 --order 37631 --output graph37631.edges
~~~

order可取表内任何整数。输出首行为n m，其后每行u v一条无向边。独立放置程序和families.json时，可用--source指定对应原作者raw adjacency。专家包包含三个完整原始源、字面序列及生成器。

[families.json](families.json)保存每步完整pins、mandatory_pins、anchors、实际旧degree、当前source_n/m及证据路径。D13续批actual_base字段已归一化为生成器source_n/m，旧11/12步骤没有改动。D13最强图为51457/324863；边数为324451加所用字面步骤实际邻集大小之和。

首D13实例51418只做了一次统一生成器dry-run边集比较：header及全部边完全一致，missing/extra/repeated均0；见[dry_run_d13_51418.json](dry_run_d13_51418.json)。该交付检查没有运行BFS，没有重验旧11/12实例。

## D13新邻域规则及完整性

原型51013的10邻点中，11352因已满degree13不进入拟新增邻集。保留其余9点，加入free guard50577，得到首个新点51417的完整邻集：

    [2813,9214,15101,25662,33884,38121,38574,42842,48533,50577]

这没有删除旧图任何边。该规则为near-complete old-star加guard，不是Q-line或Baer/Rédei blocking set，也不假设当前D13 raw点映射已经证明。原51417图D≤5作为公开完整基图继承。root独立重建官方raw边集并读取新边表，确认旧边全部保留、max13、newroot偏心率5；见[首图独立检查](../d13_D5_h9_transfer/singlefault_star_probe/independent_newroot51418.json)。

后续39步每次检查实际current图的degree与完整R4覆盖，包括此前所有新点。旧旧路径保留，新旧距离≤5，逐步归纳得到全部前缀；不从最大图删点推断中间图合法，也不逐图重复source全源BFS。[accepted_family40.json](../d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json)及families.json保存完整字面序列。

三个族分别超过D4 Moore上界12222、17569、24506，所以直径恰5。完整桥接证明见[FINAL_RESULTS_PROOF.md](../FINAL_RESULTS_PROOF.md)。

## 原作者、验证与审阅范围

三个完整原作者基图属于Dharunish Yugeswardeenoo，H9 duality/partial-fold基础归Rishabh Rajiv；公开表及原作者链接归F.Comellas。source_urls、完整原图和署名在families.json。本项目新增的是明确邻域、增点及实际whole-current覆盖构造；已知基图与经典blocking理论不计新成果。

历史独立全源代表检查包含37631、42377；后续按适量验证要求复用基图，每步验新增degree与完整currentR4。新机制或新参数首次命中做一次必要独立新root检查。历史reviewed_example_count保留38；早先Rédei15有一次集中规则审阅，不表示全部103例逐图互审或重复全源验收。本轮D13集中审阅的实际处置记录见[d13_singlefault_star_20261027.disposition.json](../../../../reviews/ddp/d13_singlefault_star_20261027.disposition.json)。

完整Lean实例仍0。较早63例说明保存在README_history_63.md，旧图及原证据保留。ZIP在root当前HTML和集中处置齐备后更新，不声称外部发表、表格采用或最优性。
