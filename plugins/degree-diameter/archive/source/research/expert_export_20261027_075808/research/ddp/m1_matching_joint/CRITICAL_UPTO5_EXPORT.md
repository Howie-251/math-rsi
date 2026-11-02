# 完整单删边损伤：长度至多 5 的共同边 DP

2026-10-26。为将已经观察到的原距离小于 5 的坏对纳入当前有限任务，另行导出 `critical_upto5_pairs.txt`。旧 `critical_pairs.txt`、原 distance-5 导出器和旧预处理程序均保留，没有覆盖或改写。没有开启搜索。

## 新表的精确范围与格式

设 G 为已验证的 2810 点直径 5 基线。新集合为

\[
\widehat C_e=\{\{x,y\}:x<y,\ d_{G-e}(x,y)>5\}.
\]

因 G 本身直径为 5，这包含所有原距离 1 至 5 的单删边损伤，而非只取原距离 5。它仍不是多条边共同删除的全部损伤；例如某点对所有短路需要两条不同删边共同截断时，可能不属于任一单边集合。

`critical_upto5_pairs.txt` 第一行为

```
2810 9835 996145
```

随后每条原边一行 `eid count encoded_pair...`，编码 `x*2810+y`、x<y，边序与 `baseline_normalized.edges` 完全相同。所有列表严格递增且无重复。对**全部 9835 条边**，从新表取出原 `dG=5` 的切片，与旧 `critical_pairs.txt` 的列表逐项相等。

## DP 的定义与正确性

令 `W_k(v)` 为从固定 root 到 v 的所有长度至多 k 的游走，I_k(v) 是其所有游走的共同边集合。不可达时 I_k(v) 不参与集合运算，不能把“不可达”误当“可达且共同边为空”。

初始只有 root 可达，`I_0(root)=∅`。对 k≥1，游走族恰分为保留的 `W_(k−1)(v)`，以及对每个邻居 u 从 `W_(k−1)(u)` 末尾附加边 uv 的族，因此

\[
I_k(v)=I_{k-1}(v)\ \cap\!
\bigcap_{u\sim v}\bigl(I_{k-1}(u)\cup\{uv\}\bigr),
\]

其中只包含实际可达的族；若旧 v 不可达，就没有最前面的 carry 项。一个新附加族的共同边确为 `I_(k−1)(u)∪{uv}`，因为与固定集合取并对交集分配。边 uv 已经在共同边集合内时，不能重复插入。

实现冻结上一层并使用两套数组逐层交换，按已验证的原距离矩阵判断 `v` 在层 k 是否可达。可达且为空的 carry 项直接把新的交集固定为空；不可达项始终跳过。任何可达共同边集合都包含于一条长度至多 k 的游走边集中，故大小至多 k，五个整数槽足够。

最后 `e∈I_5(v)` 当且仅当原图每条至多五步的 root→v 游走都用 e，即删除 e 后不存在至多五步游走。游走存在与长度不增的路径存在等价，因此这恰好是所需的 `d_(G−e)(root,v)>5`。只在 root<v 时导出，保证无序点对只计一次。

`voltage_math_check` 已独立核对该递推，包括可达空集、冻结前层及 union 去重三个实现义务。

## 完整导出与七轨道独立比较

新代码为 `preprocess_upto5_pairs.cpp`。各原距离层的边—点对 incidence 数为：

|原距离|incidences|
|---:|---:|
|1|7025|
|2|5620|
|3|68845|
|4|170005|
|5|744650|
|合计|996145|

较旧表新增 251495 项。七个边轨道各有 1405 条边，新列表长度分别为 85、90、96、98、99、107、134，各出现 1405 次。

独立代码 `verify_critical_upto5_pairs.cpp` 对同七个轨道代表再次真实删边，执行全部 2810 根 BFS，直接收集**所有**原距离层的新坏点对，并与新列表逐项比较。这次重取是新增范围的集合验证，不是重复确认旧 distance-5 范围。

|轨道|eid|完整导出数量|完整 BFS 数量|点对列表精确相等|
|---|---:|---:|---:|---|
|内部 A|0|96|96|是|
|内部 B|8431|90|90|是|
|跨 e|2|85|85|是|
|跨 412|5|134|134|是|
|跨 1338|6|107|107|是|
|跨 186|4|99|99|是|
|跨 45|3|98|98|是|

七轨道的完备性依据与代表边见 `CRITICAL_PAIRS_EXPORT.md`。原距离小于 5 的损伤现在已全部计入单边集合，包括删除跨 e 边后由距离 1 变成距离 6 的两个端点。

## 终态与成本

- `critical_upto5_export.json`：COMPLETE、退出码 0，0.91846 CPU 秒 / 0.921914 墙钟秒。
- `critical_upto5_verification.json`：`all_seven_exact=true`、session 62963 退出码 0，1.32298 CPU 秒 / 1.32352 墙钟秒。
- 合计 2.24144 CPU 秒。导出单进程单核，设定 29 CPU 秒检查阈值以保持在授权的 30 秒以内；未接近该阈值。
- 新表已通知根代理与数学代理使用；没有运行匹配搜索、重跑旧十图或生成哈希，无在途任务。

从项目根目录复现已编译程序：

```
research/ddp/m1_matching_joint/preprocess_upto5_pairs research/ddp/m1_d7d5_source/baseline_normalized.edges research/ddp/m1_matching_augmentation/baseline.distances.u8 research/ddp/m1_matching_joint/critical_pairs.txt research/ddp/m1_matching_joint/critical_upto5_pairs.txt research/ddp/m1_matching_joint/critical_upto5_export.json 29
research/ddp/m1_matching_joint/verify_critical_upto5_pairs research/ddp/m1_d7d5_source/baseline_normalized.edges research/ddp/m1_matching_augmentation/baseline.distances.u8 research/ddp/m1_matching_joint/critical_upto5_pairs.txt research/ddp/m1_matching_joint/critical_upto5_verification.json
```
