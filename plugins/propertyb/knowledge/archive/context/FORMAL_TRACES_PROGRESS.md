# 实际截面、类型恢复与解析 K4 分类

`formal/Aris4Math/Traces.lean` 把选定锁点集与实际五元超图的边集相接：
证明多点截面的唯一性、精确类型计数恢复、删点操作的一致性，
并将七点避坏型引理用于实际 25 点超图。K4 三型分类也已采用解析论证形式化。

## 定义及实际语义

所有定义位于 `Aris4Math.Simple5Hypergraph` 命名空间，使用有限集而非 Numeric 的位置列表。

| 定义 | 含义 |
|---|---|
| `H.UnitCodegrees S` | S 内任意不同两点的实际共度均为 1 |
| `H.traceTypes S` | 实际截面集合 `{e ∩ S : e ∈ H.edges}` |
| `H.multiTraces S` | 上述集合中大小至少 2 的截面 |
| `H.typeCount S T` | 实际满足 `e ∩ S = T` 的边数 |

每个集合和数量均从 H.edges 定义，没有把剖面表或概率输出当作输入假设。

## 已形式化的连接

- `multiTraces_subset`、`multiTraces_card_le_five`：每块在 S 内，且大小至多 5。
- `edge_eq_of_same_large_trace`：在 UnitCodegrees 下，同一个至少两点的截面不能来自两条不同边。
- `typeCount_eq_one_of_multiTrace`：每个实际多点块对应的全局边恰有一条。
- `existsUnique_multiTrace_pair` / `existsUnique_multiTrace_containing_pair`：每对锁点恰好由一个块覆盖。
- `multiTraces_inter_card_le_one`：不同块的交集至多一个点。
- `typeCount_large`：任意大小至少 2 的类型，其计数等于“在块族中则 1，否则 0”。
- `singleton_typeCount_add_blocks` / `singleton_typeCount_eq`：
  单点类型数加含该点的块数等于实际度数，从而得到所需减法公式。
- `typeCount_partition` / `empty_typeCount_eq`：
  空类型、全部单点类型及多点块恰好分完实际边集，得到空类型恢复式。

类型计数的证明使用有限纤维求和：先按实际 `e ∩ S` 把边分组，
再利用多点类型恰为一条边的定理。
自然数减法在已证明的加法分解后使用，不预设差非负，也不掩盖计数不足。

对六度锁点，只需把 `degree x = 6` 代入 `singleton_typeCount_eq`；
边数 32 代入 `empty_typeCount_eq`，就得到纸面 TYPE 公式。
两式本身更一般，允许其他实际度数和边数。

## 删点与实际六锁选择

`trace_erase` 证明
`e ∩ (S.erase u) = (e ∩ S).erase u`。

`multiTraces_erase` 证明实际截面集合满足
`H.multiTraces (S.erase u) = Avoidance.restrictBlocks (H.multiTraces S) u`。
该集合等式本身不需要 UnitCodegrees；截面对应全局边的唯一性另有上面的定理，未混为一谈。

`exists_six_good_locks` 已完成以下完整连接：

> 任意 25 点、32 边、点对覆盖的实际简单五元超图，都存在一个六点集合 S，
> 其中每点度数为 6、不同点的共度为 1，且其实际多点截面族不满足 TwoTripleShape。

证明先调用 Structure 的七点选择，随后把真实块族的包含关系和五元上界
交给 Avoidance 的解析删点定理，最后通过 `multiTraces_erase` 拉回实际六点截面。
TwoTripleShape 表示所有块至多三点、恰有两个三元块；
避免这个形状足以避免“两块不交三元块”这一坏型。

## K4：解析完备分类

`classify_four_lock_traces` 对 `S.card = 4` 且 `H.UnitCodegrees S` 证明下列三者之一：

1. 块族恰为 S 的全部二元子集。
2. 存在三元子集 B，块族恰为 B，加上所有不包含于 B 的二元子集。
3. 块族仅含 S 这个四元整块。

证明按最大块大小分情况：整四点块排除其他块；
两个不同三元块的并至多四点、交至多一点，与总大小六矛盾，因此三元块至多一个；
剩余点对由唯一覆盖条件强制恢复。
这是对任意实际超图和四点集的一般论证，没有枚举候选块族。

## 核验及边界

复现：

```sh
export ELAN_HOME="$PWD/.tools/elan"
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build Aris4Math.Traces
```

模块已成功编译（整条构建命令 2.991 秒）。全部 28 个定理从已编译模块导入后审计公理依赖，
均仅使用 `propext`、`Classical.choice`、`Quot.sound` 的子集；无 `sorryAx`、新公理或 `native_decide`。
日志和元数据保存在 `.aris/traces/proof-checker/2026-10-06_run06/lean-traces-*`。
Numeric 与 Structure 源文件保持冻结。

尚未在本模块完成：K6 的解析九型分类、从有限锁点集合到 Numeric 固定标签/锁位列表的重标桥，
以及概率事件计数与闭式求值器的连接。
K4 给出了精确的未标号块族描述，尚未把它编码为三个静态 Numeric 剖面的 Lean 等式。
这些仍是顶层 `Aris4Math.Target` 的独立连接义务。
