# H(9) 几何入口：任意配对的直径保证与局部度预算

本地先前只有主表抓取文件中的 H(9) 条目，没有找到部分折叠的源实现或试验。此次取得并读完作者两份论文及其数据：

- [22907863：order-four duality 原始构造](https://zenodo.org/records/22907863)，给 τ、未正则化的 33397 点 quotient F，以及其正则化/旧 twins 扩张。
- [23056128：Partial folds of the split Cayley hexagon H(9) and large graphs of diameter five](https://zenodo.org/records/23056128)，给部分折叠定理、三个逐点 witness、显式边表和标准库 Python 生成函数。主表部分折叠条目的链接文本仍写前一个 DOI，但实际 href 指向这个新 deposit。

下载的作者原件在本目录对应 record 前缀的文件及 `duality_source/`、`partial_fold_source/`。没有安装依赖，没有执行作者默认 verifier；其默认路径含哈希计算，未调用该部分，也未自行计算哈希。

## 能直接改变阶数与度数的规则

H(9) 有 66430 点与同样多的线。τ 为交换点线的四阶 duality，φ=τ²；364 个固定点形成 H(3)，其余点组成 33033 对 `{p,φp}`，称 generic fiber。完全合并后的 F 有 33397 顶点。generic fibers 诱导图记 Q。

部分折叠选择 `S⊆V(Q)` 与二色 `c:S→{0,1}`。S 中每个 fiber 保留两个点，其他 fiber 合并为一个点。对点 p，按其 fiber 颜色选择 `σ(p)=τp` 或 `τ⁻¹p`；颜色在 `{p,φp}` 内相同，这使 σ 是点到线的双射。作者 Lemma 4.1 给出：两个 split fiber 同色时连 K2,2，异色时连 perfect matching；一个 split 与一个 merged fiber 保留其 quotient 关系；H(3) 邻点接到 split fiber 的两个点。

作者 Lemma 3.1 的直径保证不依赖 S 的搜索技巧：对任意点线双射 σ，从 x 到线 σ(y) 的 incidence 奇路径长度至多五。若该路径为 `x0,L1,x1,…,x(j−1),Lj=σ(y)`，令 `yi=σ⁻¹(Li)`，则得到点配对图中的 `x0,y1,x1,…,x(j−1),yj=y`，仍至多五步。删除连续重复点不增加长度。之后合并未 split 的 fiber 也不增加距离。因此任意 S/c 均保证直径至多五；搜索只需满足以下精确度预算。

再把 H(3) 点 h 替换为 `1+z_h` 个互不邻接 copies，邻接的两类点之间使用完整二部连接。它与事后添加普通 twins 是两项不同操作。令 h(f) 为 generic f 唯一可能的 H(3) 邻点，s(h) 为 h 的三个 generic 邻 fiber 中被 split 的数目，a(h) 表示其是否为 28 个 absolute point 之一，则：

```
n_core = 33397 + |S| + Σ_h z_h
merged f degree = 10 + |N_Q(f)∩S| + z_h(f)
each point of split f degree = 10 + |{g∈N_Q(f)∩S:c(g)=c(f)}| + z_h(f)
each copy of h degree = 7−a(h)+s(h)+Σ_{h'∈N_H3(h)} z_h'
```

目标最大度 `10+δ`。对未 split 的 f，若 `|N_Q(f)∩S|>δ−z_h(f)`，它必须进入 S；这是控制 split-set 闭包的具体规则。闭包只处理 merged 条件，仍须满足 split 的同色负载与 H(3) 条件，不能单凭闭包宣称合法。

等价的逐点整数模型可用二元变量 x_f0、x_f1，`s_f=x_f0+x_f1≤1` 及整数 `0≤z_h≤δ`。令 d_f=deg_Q(f)，无 H(3) 邻点的 z 取零，约束为：

```
Σ_{g∈NQ(f)} s_g + z_h(f) ≤ δ + d_f s_f
Σ_{g∈NQ(f)} x_gk + z_h(f) ≤ δ + d_f(1−x_fk), k=0,1
Σ_{f∈HQ(h)} s_f + Σ_{h'∈NH3(h)} z_h' ≤ 3+δ+a(h).
```

事后普通 twin of v 只能复制原核心图中 v 的旧邻居；新 twins 之间不加边。若复制次数为 t_v，旧点 u 的度增加 `Σ_{v∈N(u)}t_v`，每个新 twin 度为原 deg(v)，须分别满足最大度预算。作者 Lemma 2.2 通过旧图路径及最多三步处理 twins 对，仍保证直径至多五。不能任意选择少量邻居并援引该 twin 引理。

## 可直接执行的数据与 12 度 witness

由 τ 的 orbit 按最小成员编号，与原始未正则化 F 边表的编号完全一致。因此不需要先坐标重建 H(9) 的所有线，便能得到 Q、H(3) 子图及两者相邻关系。`inspect_structure.py` 已按此恢复：

- Q：33033 顶点、164619 边；1092 点度九，其余 31941 点度十。每个 H(3) 点接三个 Q 顶点，每个 Q 顶点至多接一个 H(3) 点。
- H(3) 子图：364 顶点、714 边，28 个 absolute 点；H(3) 与 Q 间共 1092 条边。
- `Q_data.json` 保存完整邻接与索引，`witness12_state.json` 保存每个 Q 点的三态（merged / split-color0 / split-color1）、H(3) copies 和原 pad 列表。直接可用于逐点非对称搜索。

作者 12 度 witness 为 `|S|=7959`、`Σz_h=280`、普通 twins=63，阶数 41699。split 两色数为 4158 与 3801；H(3) 额外 copy 数为 224 点各一份、28 点各两份，112 点不加。去掉普通 twins 后核心为 41636 点。

|类别|核心点数|核心剩余度 slots|加回作者63 twins 后 slots|
|---|---:|---:|---:|
|merged generic|25074|12600|12348|
|split generic 的实际点|15918|12600|12159|
|原 H(3) 点|364|252|252|
|H(3) 新 copies|280|168|168|
|普通 padding twins|0 / 63|0|63|
|合计|41636 / 41699|25620|24990|

核心度分布为 10:5950、11:13720、12:21966；最终度分布为 10:5635、11:13720、12:22344。63 个普通 twins 均度十一，共接 693 条旧邻边；逐项核对其邻居确实等于所复制核心点的旧邻居，且核心局部度公式完全重现原边表度数。这些为局部结构核验，未做全根 BFS。具体逐类分布见 `structure_check.json`，本次结构核验 CPU 0.769 秒。

当前需超过的值为 42342，而非论文旧值 41699。最终阶需至少 42343，即相对作者成品增加 644。若先不加普通 twins，则需 `|S|+Σz≥8946`，较作者核心 8239 增加 707。固定 280 copies 时需 `|S|≥8666`。

作者 δ=2 只在 PSL(2,8)（阶504）轨道常值状态中优化，δ=3 用 PΓL(2,8)（阶1512）；取消前者是一个有原文依据的实质参数限制变化。两个公开 deposit 没有提供这些群作用的生成元、轨道表、轨道数或最小轨道；不能由单个 witness 恢复或猜测这些值。逐点解除该约束不需要先恢复该群。

主表新纪录提到的 pencil vertices 来自后续 Dhar 构造；本次两份 Rajiv 原文、代码与 witnesses 没有其构造规则。因此 pencil 的邻接、degree 预算与直径论证是准确缺项，不能仅凭主表文字自行套用。本入口只使用已完整给出的部分折叠、H(3) copies 与普通 twins。

root 已选择的首次有限任务在相邻 `hexagon_partial_fold_greedy/` 中执行：固定作者颜色与 280 copies，移除 63 普通 twins，四个固定顶点优先序只加入合法 split；它没有新增。root 随后通过满载 merged 点强迫闭包，关闭了固定原 S 和280 copies 的全部真 S 超集，包括同时加入及任意重染，见该目录 `root_monotone_closure.json`。后续真正构造必须允许移除旧 S 点或改变 copies；本代理没有继续该已闭单调范围。
