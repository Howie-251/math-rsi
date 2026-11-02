# 自然364＋Petersen九边细分H19：限定历史与assignment输入门

限定历史未定位该same-scope的NO或UNKNOWN终态：自然364/714固定源保边；Petersen10的15条边中选9条各细分一次得到H19/24；十个原degree3 helper各接1个旧port，九个degree2 helper各接2个旧port，共28spokes。此次仅查现存natural364/714范围、H14读取目录、canonical节点与actual460行ledger中的Petersen记录，并按文件名定位Petersen缓存。未枚举5005细分选择、未构造H、未算helper距离、未运行assignment或SAT。“未定位”不是断言没人做过。

不同旧范围：`stale_record_transfer_d3D6/petersen_c14_140_route_gate/` 是Petersen作电压cover的3D6任务；`stale_record_transfer_d11D3/cooperative715_interface/PETERSEN10_*` 是715源helper任务。均不是自然364端口与H19分配，不继承它们的NO。原1–13helper及后来的14树/单环NO也不能自动排19helper；本门不重跑它们。

最小固定输入如下（均为现成文件，无下载或新BFS）：

1. **自然源与标签。** `research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single/PORT_BINDING.json` 给source_n364、source_m714、degree3的28个端口、实际升序 `eligible_ports`。同目录 `source364.edges` 首行 `364 714`，随后0..363的无向边表。自然源原邻接缓存为 `research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json` 的 `H3_graph`；原导出程序 `source_and_single/run.py` 直接使用这些同标签邻接并去loop，没有重标号。不要改用公开Delorme364/728全4正则源。
2. **R3/R4及距离阈值。** `source_and_single/PORT_BALLS.json` 的 `ports`/`rows_port_order` 为28个实际端口，`R3_words_u64`、`R4_words_u64` 是对应闭球；`words_per_row`=6，vertex0为bit0，末尾364..383位为零。也可使用同目录 `R3.u64le.bin`、`R4.u64le.bin`，每行六个little-endian uint64。不要当成19 helper的距离表。
3. **R2。** `source_and_single/PORT_CLASSES.json` 的 `R2_class_members` 与上述端口顺序对齐；`R2_class_sizes` 全13，`R2_classes_partition_all364` 为true。这就是完整闭R2数据，不是仅一个大小摘要。
4. **R1/R0。** 原PORT_BALLS没有R1字段；无需新BFS，后续数值owner可从已存 `Q_data.json['H3_graph'][actual_port]` 取邻接，加自身得到闭R1，R0就是实际port自身。它们不能用R2近似。本读取门没有执行这一步数据抽取。
5. **唯一Petersen骨架的可复用小字面。** `research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/petersen_c14_140_route_gate/INPUT_AND_TREE_GAUGE.json` 的 `edges` 已保存10点15边标准Petersen：[[0,1],[0,4],[0,5],[1,2],[1,6],[2,3],[2,7],[3,4],[3,8],[4,9],[5,7],[5,8],[6,8],[6,9],[7,9]]。仅复用此小骨架，不导入其电压约束或NO。新19-helper的细分选择、标签与距离尚未产生，不把旧Petersen10距离当H19距离。

给定一个实际H19且确认Hdiam≤4后，完整assignment SAT可用owner变量x[g,p]：每个旧port p恰归一个helper，十个原helper各恰有1port，九个细分helper各恰有2ports。对每个helper h和旧目标t，要求以下exact OR：

    OR x[g,p] over d_H(h,g)≤4 and t∈R_(4−d_H(h,g))(p).

这是新点至旧点≤5的精确式：不同旧port旧距5，所以≤5路线不能在两不同port之间穿过旧源后再返回H。helper之间由Hdiam≤4足够，old–old D5保边继承。所有helper都有spoke反过来要求Hdiam≤4（从helper到另一helper的旧port≤5）；这项必须由实际细分H确认，不由原Petersen直径继承。R0..R4输入全可由上列现成小缓存得到，建完整assignment模型无需重验源D5或重做28个端口球。

若以后SAT真可行，条件完整图应为383点、766边：保714旧边＋24 H边＋28spokes，全部degree4。此处只是规则的参数账，未生成图、未声称覆盖成功。旧good(T)=0障碍不是对任意helper所有分配的通用NO，不能不核其route hypotheses就套用到该无叶H。

本门保守read/prep0.5 CPU秒。新增sourceparse、source/port BFS、H pattern枚举、helper距离运算、SAT/solver、图、Lean均0。未修改Wiki/STATE/ROUND/pages。停止历史门，后续数值由root另行授权，不自动试pattern或assignment。
