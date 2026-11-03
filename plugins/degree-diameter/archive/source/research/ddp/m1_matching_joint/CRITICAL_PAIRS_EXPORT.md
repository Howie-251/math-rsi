# 逐边 distance-5 临界点对列表

2026-10-26。本次只导出和验证数据，不执行匹配或图构造搜索。原程序 `research/ddp/m1_matching_augmentation/preprocess.cpp` 未修改，距离矩阵复用 `baseline.distances.u8`。

## 文件格式与定义

`critical_pairs.txt` 第一行为

```
2810 9835 744650
```

依次是 n、m、总 incidence 数。随后恰 9835 行，每行为

```
eid count encoded_pair...
```

`eid` 从 0 起，顺序与 `research/ddp/m1_d7d5_source/baseline_normalized.edges` 中的原边顺序完全一致。每个点对满足 x<y，编码为 `x*2810+y`；解码为整除与余数。每条边的编码列表严格递增且无重复。所有 9835 个列表长度与旧 `baseline.edge_critical5.txt` 的对应计数逐项相等。

定义严格为

\[
C_e=\{\{x,y\}:d_G(x,y)=5,\ \text{每条 }x\text{ 到 }y\text{ 的最短路都经过 }e\}.
\]

等价条件是 `dG(x,y)=5` 且 `d_(G−e)(x,y)>5`，后者包含不可达情形。它**不包含原距离小于 5 的新坏对**，也不声称覆盖多边共同删除后才出现的全部损伤。

## 导出算法

新代码 `preprocess_pairs.cpp` 对每个根，利用已有距离按 0 至 5 层处理最短路 DAG。令 I(v) 为该根到 v 的所有最短路的共同边集合，则

\[
I(root)=\varnothing,\qquad
I(v)=\bigcap_{u:\ d(u)+1=d(v)}(I(u)\cup\{uv\}).
\]

每个 I(v) 至多有五条边，用小数组直接交集。只对 `d(v)=5` 且 `root<v` 的点对，把编码加入每条 `e∈I(v)` 的列表，保证无序对只计一次。算法不枚举或抽样路径。最终共处理 1,867,245 个原距离 5 的无序点对，导出 744,650 个边-点对 incidences。

## 七个边轨道的独立验证

独立代码 `verify_critical_pairs.cpp` 不用 DAG 共同边算法。它对七个代表分别真实删除一条边，再运行全部 2810 根 BFS，直接收集原距离 5 且删后距离超过 5 的全部无序对，并与导出列表逐项比较。

已知左正则群作用保留两轨道。内部 A、B 各有一个边轨道，五个跨电压各给一个边轨道；每个轨道大小为 1405。内部生成元不是对合，内部无向边稳定子也平凡。因此这七类恰覆盖全部 `7*1405=9835` 条边。

|边轨道|代表 eid|代表边|导出及 BFS 的 C_e 大小|原距离<5 的额外新坏对|完整列表相等|
|---|---:|---|---:|---:|---|
|内部 A|0|(0,1176)|70|26|是|
|内部 B|8431|(1405,2552)|69|21|是|
|跨 e|2|(0,1405)|65|20|是|
|跨 412|5|(0,1817)|90|44|是|
|跨 1338|6|(0,2743)|87|20|是|
|跨 186|4|(0,1591)|78|21|是|
|跨 45|3|(0,1450)|71|27|是|

七份删边图均连通、直径 6。一个具体范围反例是删除跨 e 的代表边 `(0,1405)`：这两个端点原距离 1，删后距离 6，所以它们是实际新坏对，却不属于本文件定义的任一原距离 5 的 C_e。额外坏对按原距离的完整分布保存在验证 JSON 中，未混入导出列表。

## 完成状态与成本

- 导出：`critical_pairs_export.json`，状态 COMPLETE，退出码 0，0.556527 CPU 秒 / 0.559907 墙钟秒。
- 七代表验证：`critical_pairs_verification.json`，`all_seven_exact=true`，session 97422 退出码 0，1.3095 CPU 秒 / 1.31037 墙钟秒。
- 代码与二进制分别为 `preprocess_pairs.cpp` / `preprocess_pairs`、`verify_critical_pairs.cpp` / `verify_critical_pairs`。
- 没有计算哈希，没有开启搜索或留下运行作业。

从项目根目录复现已编译程序：

```
research/ddp/m1_matching_joint/preprocess_pairs research/ddp/m1_d7d5_source/baseline_normalized.edges research/ddp/m1_matching_augmentation/baseline.distances.u8 research/ddp/m1_matching_augmentation/baseline.edge_critical5.txt research/ddp/m1_matching_joint/critical_pairs.txt research/ddp/m1_matching_joint/critical_pairs_export.json
research/ddp/m1_matching_joint/verify_critical_pairs research/ddp/m1_d7d5_source/baseline_normalized.edges research/ddp/m1_matching_augmentation/baseline.distances.u8 research/ddp/m1_matching_joint/critical_pairs.txt research/ddp/m1_matching_joint/critical_pairs_verification.json
```
