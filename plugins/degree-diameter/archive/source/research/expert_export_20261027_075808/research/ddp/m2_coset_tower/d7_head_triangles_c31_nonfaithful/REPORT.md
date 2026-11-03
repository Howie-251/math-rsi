# c31 非忠实作用三角头塔：完整有限检查终态

**此固定塔的完整 HH 可能族没有直径至多5的图。** 全部 **405,000 个规范商键**已完成精确 BB 检查，通过数为0，最小 BB 缺失为12（两个商键达到）。由中心商保留 block 端点距离的证明，同一商键的全部8种原提升均失败。因此无须展开生产提升；本结论只适用于下面固定的群、子群和三角头构造，不是一般度径排除或新纪录。

## 固定范围与判定

固定 $G=(\mathbb F_{31}\rtimes_9 C_{30})\times C_3$，$K=C_{30}$，$H=\langle k^5\rangle$ 阶6。原塔有2790叶、465个block、93个head，共3348点，head的三角边使完整图7正则。作用根9的阶为15。

[STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md) 证明：任何可能满足 HH 的六元逆闭非单位集合，必须由两个跨 $w$ 逆对和一个内部非零逆对组成；两个 $w=1$ 代表分属两个非零field轨道。缩放及安全的商锚反演将完整范围保留在405,000个商键内：锚指数0至7、另一跨field值15种、另一跨指数15种、内部非零商逆对225种。每键8种中心提升，覆盖3,240,000个原提升输入；这些是保全参数数目，不是不同同构类数目。

中心元 $k^{15}\in H$ 固定所有block/head、交换叶对。故商与原图之间，凡至少一个端点为block/head的距离完全相等，且与8种提升选择无关。商叶的原目标计数权重为2，block/head权重为1。BB 使用精确五步集合

\[
HW_3H\;\cup\;KW_1H\;\cup\;HW_1K\;\cup\;ZK,
\]

其中 $Z$ 是两个非零中心 $C_3$ 平移。商 LL 距离没有被当作原 LL 判据。

## 实际完成量

| 项目 | 实际值 |
|---|---:|
| 已检查商键 / 完整范围 | 405,000 / 405,000 |
| 下一游标 | 405,000（结束） |
| BB 通过商键 | 0 |
| 生产中完整 B/H 商 BFS | 0 |
| B/H 全覆盖商键 | 0 |
| 生产中展开的原提升 / 原叶根 BFS | 0 / 0 |
| 最小 BB 缺失 | 12，达到者2个 |

前10,000键实际 CPU 0.020472秒，BB 通过数0；完整生产实际 CPU 0.788038秒，其中 BB 计时0.622292秒。完整缺失直方图及终止游标见 [production.terminal.json](production.terminal.json)，首段数据见 [production.first10000.json](production.first10000.json)。唯一生产进程正常 exit 0，无重启、无运行中作业。

正式生产前只做了一例原图/商图校准。两个原 B/H 根对全部原目标的6696项距离比较与商逐项一致；按原权重还原的缺失数为1896和1440。465个 BB 目标也全部吻合精确掩码，见 [calibration.json](calibration.json)。这例校准和下述保存图均与“生产中展开提升数0”分开记录。

## 保存图与唯一独立验收

因没有 BB 通过键，保存的是一个最小 BB 键的一种原提升，**不是整个族的最小坏点对图**。键游标143848：锚指数2，另一跨field为27、指数9，内部商逆对索引73、代表215，提升位000。原群编码为 $x+31w+93j$，保存生成元为

```
S = [218, 2679, 895, 2016, 215, 2609]
```

[production.best.edges](production.best.edges) 与 [production.best.json](production.best.json) 保存完整图和参数。独立实现从真实阶15作用重新生成的11,718条边与文件完全相等；一次全部3348根的通用 BFS 确认简单、连通、7正则、直径6、坏无序点对111,600。叶/block/head三个代表根缺失分别为57、120、90；BB 缺失12，全部465个 BB 目标和保存的33位轨道掩码逐项一致。

| 坏点对类型 | LL | LB | LH | BB | BH | HH |
|---|---:|---:|---:|---:|---:|---:|
| 数量 | 55,800 | 44,640 | 2,790 | 2,790 | 5,580 | 0 |

独立检查结果在 [best.independent_verify.json](best.independent_verify.json) 与 [production.best.independent_check.json](production.best.independent_check.json)。该唯一最终检查实际 CPU 为 **0.255313477秒**，由父代理另行安排；没有重复检查其他样本，当前无验证待办。

## CPU 与复现文件

本生产任务的**已记录实测 CPU 为2.502766秒**，包括成功编译、校准、生产及驱动开销。另有第一次编译失败：只保存了约0.3385秒墙钟，未保存精确 CPU，因此从120秒预算中另扣 **1.0秒保守额度**。预算计账合计 **3.502766秒**；该1秒不是实测 CPU。后续独立最终检查的0.255313477秒单列于上节。

首次编译的标识符冲突已修复；失败发生在任何候选计算启动前，日志保存在 `compile.attempt1.log`。成功生产只有一次，没有冷启动续跑。

可复现源码为 [production.cpp](production.cpp) 和 [run_production.py](run_production.py)。准备、预算和进程终态分别在 [production.prepare.json](production.prepare.json)、[production.summary.json](production.summary.json)、[production.run.json](production.run.json)。本批完整结束，不追加候选或搜索。
