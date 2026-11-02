# P10：首个42343点完整图已通过root独立验收

**P10 命中。** 固定P9的第0个10-pin Q-line附件，只加两个现有顶点 **4633、20168** 作为 anchors，便覆盖此前全部25个缺项。新点的完整12邻集为

`[452,4633,6195,10312,12353,13822,20168,21068,24695,29805,36474,38101]`。

这些旧点在42342图中的度数依次是 `[11,11,11,11,11,11,10,11,11,11,10,11]`，添加一边后均≤12，新点度为12。完整邻接和25条≤4旧base路径在发现后立即交给root；`first_success.json`保存全部证据。本代理没有生成图或重跑全源BFS；root随后生成的42343点边表已通过完整独立验收，终态为 **ROOT_VERIFIED_FIRST_HIT**。

已验图为 `../candidate42343/graph_d12_D5_n42343.edges`，n42343、m245229、simple、最大度12、直径恰5。`../candidate42343/independent_all_source_BFS.json`确认全部42343根均检查、bad unordered pairs=0、unreachable pairs=0；4workers、15.1209wall秒、60.3519CPU秒。root在2026-10-27实时读取的Comellas公开基线仍为42342，因此本图给出 **N(12,5)≥42343**，不主张最优值或已Lean形式化。可复现生成脚本、完整参数/credit、README已保存 `../candidate42343/`。

## 冻结范围与精确性

`PREDICTION.json` 在执行前冻结“固定7条 degree-feasible Q-lines 中至少一条可用≤2 anchors补成完整42343图”。base是当前完整42342点、245217边的图，最大度12、D≤5。所有14396个当前degree<12的顶点均可作 anchor，含existing extras；每个candidate排除其10个mandatory pins后有14386个候选。不修改线、中心、mandatory pins或旧边，不允许第三anchor。

只读取 `quadric_extension/RESULT.json` 已保存的7组 missing targets，没有重跑其7次mandatory R4检查。这7组的缺项并集共276个点，对每个点在固定base中只运行**一次反向radius4 BFS**，获得它能被哪些可用anchor覆盖。因图无向，此关系与anchor到目标的R4覆盖等价。

先将该candidate所有目标的coverers相交，精确判断单anchor。若为空，枚举每个允许first anchor v，对所有未被v覆盖的目标，把它们的coverers作交集，并排除v与mandatory pins；交集非空即得到一个不同second anchor。这遍历覆盖所有≤2方案，不是按缺项数量优化，也没有14k²的Python双循环或greedy。

候选0单anchor交集为空；枚举到第1270个允许first anchor时，得到 `(4633,20168)`。25个缺项均在两者R4并内。每个目标的覆盖anchor、旧base距离和实际路径保存于 `first_success.json`，其余所有目标由既有mandatory覆盖结果继承。所以12邻集的R4并覆盖全部42342个旧点。

若保留全部旧边并添新点z，旧—旧D≤5继承；对每个旧点v，有一个完整邻点p满足d_base(p,v)≤4，因此d(z,v)≤5。这给出了候选图完整D≤5的有限覆盖证书，不依赖把quadric line本身当作新—新覆盖定理。

## 真实执行与停止

- reverse R4 BFS：276次，每个union target一次；不是全源BFS。
- mandatory R4重算：0次；候选图生成：0。
- 当前阶段已找到存在性witness，因此其余6个candidate不继续分类；不能把它们记作失败或成功。
- 单worker，读图、276次反向BFS与精确求解合计测得CPU **1.212575638秒**（计时点为完成求解、写缓存之前），远低于60秒预算。
- `RESULT.json`终态为 `ROOT_VERIFIED_FIRST_HIT`，`pending=[]`。独立验收由root执行，已验证新下界计1；其余6项未继续，不再搜索更多点。

复用缓存 `reverse_R4_distances.u8.bin`、`reverse_coverers.u8.bin` 与 `coverage_cache.json` 保留这276个target的精确数据和14396个anchor的编码；它们是距离/bitset数据，不是哈希或校验文件。本批没有新中心/line枚举、第三anchor、缺项下降续轮、旧14396-ball greedy、全源BFS或依赖安装。

证据：冻结预测、`solve.py`、`RESULT.json`、`first_success.json`、coverage缓存；输入固定来自 `quadric_extension/RESULT.json` 和 `h9_quadric_line_extension_pool/pool.json`。正式图与完整独立验收在 `../candidate42343/`；此次交付只读取该图作不写入的生成结构对照，未再次运行BFS或改写已验边表。
